"""
Voice Family — сервис нарезки записей занятий.

Принимает запись урока и список моментов, возвращает нарезанные mp3.
Используется воркфлоу «Разбор занятий» в n8n.
"""

import base64
import json
import logging
import os
import re
import shutil
import subprocess
import tempfile
import uuid

from fastapi import FastAPI, File, Form, Header, HTTPException, UploadFile

app = FastAPI(title="Voice Family Cutter")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("vf-cutter")

API_KEY = os.environ.get("CUT_API_KEY", "")
MAX_CLIPS = 20
DEFAULT_LEAD_IN = 55      # сколько секунд захватываем ДО момента
DEFAULT_DURATION = 80     # длина фрагмента по умолчанию


def check_key(provided: str | None) -> None:
    if not API_KEY:
        return
    if provided != API_KEY:
        raise HTTPException(status_code=401, detail="Неверный ключ")


def to_seconds(value) -> int | None:
    """Принимает 125, '125', '02:05' или '1:02:05'. Не распознал — None."""
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return max(0, int(value))
    s = str(value).strip()
    if s.isdigit():
        return int(s)
    parts = s.split(":")
    try:
        parts = [int(p) for p in parts]
    except ValueError:
        return None
    if any(p < 0 for p in parts) or any(p > 59 for p in parts[1:]):
        return None
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    return None


def safe_name(s: str) -> str:
    """Имя файла без символов, которые ломают Drive и ссылки."""
    s = re.sub(r"[\\/:*?\"<>|\n\r\t]", " ", str(s))
    s = re.sub(r"\s+", " ", s).strip()
    return s[:80] if s else "фрагмент"


@app.get("/")
def health():
    return {"status": "ok", "service": "Voice Family Cutter"}


@app.post("/cut")
async def cut(
    file: UploadFile = File(...),
    cuts: str = Form(...),
    lead_in: int = Form(DEFAULT_LEAD_IN),
    lesson_id: str = Form(""),
    x_api_key: str | None = Header(default=None),
):
    """
    file  — запись занятия целиком
    cuts  — JSON-массив: [{"time": "02:35", "duration": 80, "caption": "текст"}]
    lead_in — сколько секунд захватить до указанного момента
    lesson_id — необязательный идентификатор урока, попадает в логи и ответ

    Возвращает: {"clips": [{"name": "...", "start": 100, "duration": 80, "mp3": "<base64>"}],
                 "count": N, "ok": N, "failed": N, "skipped": [...], "lesson_id": "...", "request_id": "..."}
    Фрагмент, который не удалось вырезать (в том числе из-за нераспознанного времени),
    приходит с полем "error" вместо "mp3".
    """
    request_id = uuid.uuid4().hex[:12]
    tag = f"lesson={lesson_id or '-'} request={request_id}"
    check_key(x_api_key)

    try:
        items = json.loads(cuts)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="cuts должен быть корректным JSON")

    if not isinstance(items, list) or not items:
        raise HTTPException(status_code=400, detail="cuts должен быть непустым массивом")

    skipped = [item.get("time", "") if isinstance(item, dict) else item for item in items[MAX_CLIPS:]]
    if skipped:
        log.warning("%s: %d moments over the limit of %d were skipped", tag, len(skipped), MAX_CLIPS)
    items = items[:MAX_CLIPS]
    workdir = tempfile.mkdtemp(prefix="vfcut_")

    try:
        src = os.path.join(workdir, "source" + (os.path.splitext(file.filename or "")[1] or ".m4a"))
        with open(src, "wb") as f:
            shutil.copyfileobj(file.file, f)

        if os.path.getsize(src) == 0:
            raise HTTPException(status_code=400, detail="Пустой файл записи")

        clips = []
        for i, item in enumerate(items, start=1):
            if not isinstance(item, dict):
                item = {"time": item}
            caption = safe_name(item.get("caption", ""))
            moment = to_seconds(item.get("time"))
            if moment is None:
                log.warning("%s: clip %d has unrecognized time %r", tag, i, item.get("time"))
                clips.append({
                    "name": f"{i}. ?? — {caption}.mp3",
                    "time": item.get("time", ""),
                    "caption": item.get("caption", ""),
                    "error": f"Не распознано время: {item.get('time')!r}. Нужно 125, '02:05' или '1:02:05'",
                })
                continue
            start = max(0, moment - int(lead_in))
            try:
                duration = int(item.get("duration") or DEFAULT_DURATION)
            except (TypeError, ValueError):
                duration = DEFAULT_DURATION
            duration = max(5, min(duration, 300))

            mmss = f"{moment // 60:02d}-{moment % 60:02d}"
            name = f"{i}. {mmss} — {caption}.mp3"

            out = os.path.join(workdir, f"clip_{i}.mp3")
            cmd = [
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                "-ss", str(start),
                "-t", str(duration),
                "-i", src,
                "-vn",
                "-acodec", "libmp3lame",
                "-q:a", "5",
                out,
            ]
            proc = subprocess.run(cmd, capture_output=True, timeout=300)

            if proc.returncode != 0 or not os.path.exists(out):
                log.error("%s: ffmpeg failed on clip %d: %s", tag, i, proc.stderr.decode("utf-8", "ignore")[:300])
                clips.append({
                    "name": name,
                    "start": start,
                    "duration": duration,
                    "error": proc.stderr.decode("utf-8", "ignore")[:300],
                })
                continue

            with open(out, "rb") as f:
                data = base64.b64encode(f.read()).decode("ascii")

            clips.append({
                "name": name,
                "start": start,
                "duration": duration,
                "caption": item.get("caption", ""),
                "time": item.get("time", ""),
                "mp3": data,
            })

        failed = sum(1 for c in clips if "error" in c)
        log.info("%s: %d clips ok, %d failed, %d skipped", tag, len(clips) - failed, failed, len(skipped))
        return {
            "clips": clips,
            "count": len(clips),
            "ok": len(clips) - failed,
            "failed": failed,
            "skipped": skipped,
            "lesson_id": lesson_id,
            "request_id": request_id,
        }

    finally:
        shutil.rmtree(workdir, ignore_errors=True)
