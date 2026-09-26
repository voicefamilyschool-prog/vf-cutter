# Voice Family Pilot — Runbook

<!--
ДЛЯ ВЛАДЕЛЬЦА (RU, коротко)

Что это: рабочий регламент ручного пилота «Недели 0–2 → 8» (VF-011, VF-036, VF-022, VF-023, VF-056,
VF-058, VF-060, VF-073, VF-088). Всё ниже линии — английский текст для команды пилота; приложение A —
готовый текст PDF «Online Studio Check» для студентов (US; UK-варианты в скобках).
Таблицы — в pilot-kit/templates/*.csv (только заголовки). Словарь колонок — раздел 10.

Что заполнить / утвердить до старта (в тексте помечено [OWNER], [SLP], [DEV]):
1. Имена людей на ролях, особенно ops-дежурный по флагам здоровья (решение №9 раздела 9 плана), и час,
   после которого флаг закрывает ops-дежурный (сейчас заглушка [OWNER: 6 pm]).
2. Где хранятся файлы (Drive-папка) и кто к ней имеет доступ; срок 90 дней — [Д] из VF-064, ждёт юриста.
3. Платят ли пилотные студенты VF за пилот отдельно (в плане не решено). Тестовые цены (диагностика
   $29/$49, Starter ≈$35/$45 за урок-эквивалент, без автопродления) — [Д], для пилота своих студентов
   их не используем, пока владелец не решит.
4. Порог «слышу разницу ≥4/5» из плана трактован как «медиана самооценки студента ≥4 по шкале 1–5» —
   подтвердите или поправьте ДО начала замера (правило плана §10: пороги не меняем после старта).
5. Правила недели 4 — «ранние сигналы» [Д], ими нельзя закрыть или масштабировать пилот; это наша
   надстройка над планом, её тоже надо утвердить до старта.
Технически: VF-023 в коде ветки уже исправлен — «02:14.5» принимается (секунды округляются вниз),
«2.35» без двоеточия отклоняется как неоднозначное. Действует после выката ветки на Railway; до этого
вводим целые секунды (памятка 01, §2.2, §11). lead_in один на весь запрос — эталоны режем отдельным
запросом (раздел 4).
-->

**Version 0.1 · Pilot weeks 0–8 · Internal — pilot team only**

The pilot: **2 teachers × 5 adult students (18+), n = 10**, run by hand on the existing `/cut` service and the n8n "lesson review" workflow. Nothing new happens during the lesson. The loop is:

**lesson → moments in n8n → `/cut` → recap to student → home take → coach voice reply → Before/Now check → pre-lesson check-in → next lesson**

Fixed for the whole pilot (not up for trade-offs against metrics): voice safety, privacy, adults only, every student-facing word approved by the teacher (AI Gate), and ≤20 min/week of async teacher time.

---

## 1. Roles

| Role | Who | Owns | Time (estimate [Д]) |
|---|---|---|---|
| **Owner** | [OWNER] | Go / no-go at weeks 2, 4, 8; consent forms and retention; prices; admin tools (§7); teacher pay for minutes over 20 and for Snapshots | ~1 h/week for decisions |
| **Methodologist** | [OWNER] | Home Assignment Checklist audit; wording of replies and check-ins; Online Studio Check PDF sign-off; "over budget" weeks; reviews every health flag within 24 h | ≤8 h/week total, pilot share ~1 h |
| **Teachers (T1, T2)** | [OWNER] | Lesson as usual; moments; captions and tasks; weekly voice reply; Before/Now pair; logging their own minutes | ≤20 min/week async for 5 students |
| **Ops on-call** | [OWNER] — a named person, not "the team" | Runs `/cut` when the teacher doesn't; checks `ok / failed / skipped`; sends recaps the teacher approved; keeps all tables; Quiet Churn review; covers health flags the teacher can't answer the same day | ~2–3 h/week [Д] |
| **Developer** | [OWNER] | VF-023 fixes, VF-022 alert and status table, n8n workflow; fixes anything logged as `pipeline` in `pilot-flags.csv` | Per plan: 6.5 of 8 days in weeks 0–2 |
| **SLP / voice doctor** | [OWNER] | Approves the refer-out card and "it hurts" template before the first home assignment | 1–2 h |

**Escalation in one line:** health → teacher, then ops on-call, same day; tech → ops, then developer; time over budget → methodologist; anything about age, consent, or privacy → owner, and recording stops until resolved.

---

## 2. Before the first lesson (week 0–1 checklist)

Nothing is recorded until every line is ✓.

- [ ] **Stop gate:** signed consent form with three separate checkboxes (record my lessons / store my home recordings / let my coach hear my recordings — Legal drafts 05 §1.1; the optional head-coach and improve-service boxes are logged too) for every student. No consent → no recording.
- [ ] **LLM step removed** from the n8n workflow until a DPA is signed. Captions are written by the teacher; `caption_source = teacher`.
- [ ] Age 18+ confirmed **before** any recording (First Week Setup form); logged in `pilot-students.csv`.
- [ ] "Where can you practice?" answered (quiet / some noise / none) and logged.
- [ ] Online students received the **Online Studio Check** (Appendix A) at least 2 days before lesson 1 — **only if the methodologist has already signed it off.** Per plan §5.1 its review moves to week 3 (VF-056), so it is not a stop gate for recording.
- [ ] Refer-out card and "it hurts" template approved by SLP. Until then teachers use only: *"Please stop singing for now, and check in with a doctor or voice specialist."*
- [ ] VF-023 acceptance check passed in production (§4.5) — or ops knows the workarounds in §4.3.
- [ ] n8n Error Trigger alert goes to the ops on-call channel and was tested once with a deliberately broken request.
- [ ] Drive folders created with the access rules in §5.
- [ ] All six CSV tables created from `templates/`; teachers can open `pilot-teacher-time.csv` (or its form) from their phone.
- [ ] Scheduling and payment stay in My Music Staff or Calendly + Stripe (§7). No payment data enters pilot tables.

---

## 3. The weekly cycle, day by day

**L** = lesson day. All times are in the **student's** time zone.

| Day | Who | What happens | Done when | Log in |
|---|---|---|---|---|
| **L − 1** | Ops (auto-send if possible) | Pre-lesson check-in goes out (§3.1) | Sent | `pilot-homework.csv` → `checkin_sent_at` |
| **L** (lesson) | Teacher | Teach as usual. The lesson is recorded (Zoom cloud/local, or room recorder). Online students also run a backup recording (Appendix A). **Lesson 1 only:** the student's first home-style recording is made *in the lesson* and you listen together. Before that, the student does not record alone | Recording exists | `pilot-lessons.csv` → `recording_received_at`, `recording_source` |
| **L, within 2 h after** | Teacher | Enter 2–4 moments in the n8n form: your demo (reference), the student's best take, and the two halves of a Before/Now pair (§3.2). Timecode = the moment the phrase **starts** | Moments submitted | `pilot-teacher-time.csv` → `timecodes` |
| **L, same day** | n8n / ops | `/cut` runs with `lesson_id`, `lead_in=3`, each clip `duration` 15–20 (§4). Ops checks `ok / failed / skipped` | `failed = 0` and `skipped = []`, or §4.4 followed | `pilot-lessons.csv` → `cut_*` columns |
| **L + 0–1** | Teacher | Listen to each clip once. Approve / edit / reject captions (✓ / ✎ / ✗). Run the Home Assignment Checklist (Handbook §5.1); set **OK to sing at home** (default: no). Mark "Keep for next week" if the task carries over | All clips approved; checklist passed | `pilot-lessons.csv` → `ai_gate_*`, `checklist_passed`, `ok_to_sing_at_home` |
| **Within 24 h of lesson end** | Ops | Send the recap: reference clip, best take, Before/Now pair with "what changed," task (1–2 items), stop line. Only teacher-approved text | Recap sent | `pilot-lessons.csv` → `recap_sent_at` |
| **L + 1 … L + 5** | Student | Practices. Records as many takes as they like; **sends one** chosen take ("coach hears it first"). Answers the reflection question; may mark ⭐ best moment | Take received | `pilot-homework.csv` → `take_submitted_at` |
| **Within 48 h of the take** | Teacher | One voice reply, 30–60 s: one win → why → 1–2 tasks. If the student reacts "same" or "let's discuss," answer by voice — counts as that week's reply | Reply sent | `pilot-homework.csv` → `reply_sent_at`; `pilot-teacher-time.csv` |
| **With or after the reply** | Ops | Ask the student one question about the Before/Now pair (§3.2). Record whether they opened it | Answer or no answer logged | `pilot-homework.csv` → `pair_opened`, `hear_difference_1to5` |
| **L + 6 (= next L − 1)** | Ops | Next check-in (§3.1). Update the Quiet Churn view (§8) | Table updated | `pilot-homework.csv`, `pilot-flags.csv` |
| **Every Monday** | Ops | Fill one row of `pilot-metrics-weekly.csv` (§9) for the previous week | Row filled | `pilot-metrics-weekly.csv` |

**Any day, any time — health flag.** A student writes "it hurts," "hoarse," "I lost my voice," or picks "hurts": the teacher (or ops on-call if the teacher can't) replies **the same day** with the SLP-approved template, and all singing stops. If the student mentions trouble breathing, coughing up blood, severe or sudden pain, or a sudden complete loss of voice, the reply tells them to get medical help now (emergency services for breathing) — nobody waits for the refer-out threshold. Log in `pilot-flags.csv`. Health flags are **outside** the 20-minute budget and are never cut to save time.

### 3.1 Pre-lesson check-in (send as is)

The student-facing text is **Student copy (02) §6, "Before your lesson — 3 quick questions"** — one text for the whole pilot, don't send a second version. Summary of what ops logs:

> 1. How's your voice today? — Feels fine · A bit tired · Hoarse, sore or it hurts · I'm sick
> 2. On how many days did you get to practice this week? [UK: practise] — 0 · 1 · 2 · 3 · 4 · 5+ ; then optional "Life happens — tell me what got in the way."
> 3. What would you like from today's lesson? (optional)

Rules: never reply with "you missed…"; never show the student a count of days over time; "Hoarse, sore or it hurts" → health flag (same day); "I'm sick" → that week is excluded from metrics and nobody chases the student.

### 3.2 Before/Now pair

- Same phrase, same key, two takes. **Lessons 1–2:** both takes from the same lesson, captioned **"in this lesson."** **From lesson 3:** an earlier lesson may be the "Before."
- Caption: *"Before/Now (in this lesson): [phrase]. What changed: [one audible change]."*
- No honest change → no pair. Log `pair = skipped_no_honest_change`. Never force one.
- Question sent to the student after they've had time to listen:
 > *"Did you get a chance to listen to your Before/Now clip? If yes — how clearly can you hear a difference? 1 = not at all, 5 = very clearly. Any answer is useful."*
 This is the student's own rating of what they hear. It is never turned into a score about their voice, and never shown back to them as a number.

---

## 4. Cutting clips with `/cut`

### 4.1 Request

`POST /cut` (multipart form), header `X-API-Key: <CUT_API_KEY>`.

| Field | Value in the pilot |
|---|---|
| `file` | The lesson recording (or the student's backup recording, §4.6) |
| `lesson_id` | Always set. Format: `T1-S03-L02-20261005` (teacher – student – lesson number – date). The same ID goes in every table and in the Drive folder name |
| `lead_in` | **3** for reference, best take, and Before/Now clips. The clip starts 3 s before the timecode |
| `cuts` | JSON array, ≤20 items, e.g. `[{"time":"02:14","duration":18,"caption":"Coach demo - verse 1"}, {"time":"07:40","duration":16,"caption":"Best take - verse 1"}]` |

- `duration`: **15–20 s** per clip for reference and pairs. Enough for one phrase, short enough to replay many times.
- `caption` becomes part of the **file name** (`1. 02-14 — Coach demo - verse 1.mp3`, max 80 characters). Keep it a short label. **Never put the student's name** in it. The student-facing text goes in the recap message, not the file name.
- If the teacher also wants long "review" clips (performance + comments), send them as a **separate** request with the old defaults (`lead_in=55`, `duration` 80). Don't mix them with 3-second clips in one request.

### 4.2 Response — what ops checks every time

| Field | Meaning | Action |
|---|---|---|
| `ok` | Clips cut | Should equal the number of moments sent |
| `failed` | Clips that came back with an `error` field instead of `mp3` | **If > 0 → §4.4** |
| `skipped` | Timecodes over the 20-clip limit (never cut) | **If not empty → send them in a second request** |
| `lesson_id`, `request_id` | Echoed back | Copy `request_id` into `pilot-lessons.csv` → `cut_request_id`. The developer needs it to find the log line |

Then **listen to every clip once** (the teacher does this in the AI Gate step). A clip can be "ok" and still wrong: silent, too short, or the wrong moment. `ok` means "ffmpeg ran," not "the clip is right."

### 4.3 Known behavior until VF-023 is live [DEV: remove this section after release]

| Situation today | Workaround |
|---|---|
| Fractional seconds in text form (`"02:14.5"`) → clip comes back as `failed` ("unrecognized time") | Use whole seconds (`"02:14"`) |
| Numeric fractional time (`134.5`) is silently rounded down | Use whole seconds |
| `lead_in` applies to the whole request, not per clip | One request per clip type (§4.1) |
| If `CUT_API_KEY` is not set on the server, the service accepts requests without a key | Developer confirms the variable is set; ops confirms a request with no key gets `401` |
| A time beyond the end of the recording may produce an empty or very short "ok" clip [В — to verify] | Listening check in §4.2 catches it |

### 4.4 When `failed > 0` (or `skipped` is not empty, or the call errors)

1. **Don't send anything broken to the student.** Nothing partial goes out as "close enough," especially not a Before/Now pair.
2. Read each failed clip's `error` text:
   - *Unrecognized time* → fix the format (`mm:ss`, `h:mm:ss`, or seconds), resend **only the failed moments**, same `lesson_id`.
   - *ffmpeg error* → check the recording file opens and plays. If it doesn't, get the original from the teacher or the backup recording (§4.6).
   - HTTP `401` → wrong or missing key in n8n. HTTP `400` → empty file or broken `cuts` JSON. Fix and resend.
3. **Retry once.** If it fails again: log `flag_type = pipeline` in `pilot-flags.csv` with `lesson_id`, `request_id`, and the error text; message the developer.
4. If the recap will miss the 24-hour mark: send the student the task in words with the "clip failed" template (Handbook template 10). Log `recap_status = sent_without_clips`.
5. If the lesson recording is lost for good: `lesson_status = lost`. **Lost lessons are a guardrail metric (target 0)** — every one is reviewed by the developer and owner that week.
6. n8n Error Trigger alert arrived but nobody has acted: ops acknowledges within **4 working hours** [Д] by writing a line in `pilot-flags.csv`.

### 4.5 VF-023 / VF-022 acceptance check (developer, before "go" at week 2)

- [ ] Request without key → `401`. `CUT_API_KEY` is mandatory in production.
- [ ] `"02:14.5"` and `134.5` both cut from 134.5 s (±0.1 s).
- [ ] Unrecognized time → explicit error, never a clip from 0:00.
- [ ] Successful clips contain no `error` field.
- [ ] 22 moments → 20 clips + 2 in `skipped`, and n8n shows the skipped ones to ops.
- [ ] `lead_in` and `duration` can be set per clip.
- [ ] Deliberately broken request fires the n8n Error Trigger alert to ops.
- [ ] Status table (one row per `lesson_id`) fills automatically: received → cut → approved → recap sent.

### 4.6 Online lessons: using the student's backup recording

Zoom's sound is compressed and noise-suppressed; for reference clips and Before/Now pairs the student's own backup recording is better. If the student uploaded one:

1. Find the clap at the start in both files. `offset = clap time in backup − clap time in Zoom` (seconds). Log it in `clap_offset_s`.
2. Add `offset` to each teacher timecode and cut from the backup file.
3. If there's no clap or no backup, cut from the Zoom recording and note `recording_source = zoom`.

This is ops work — it is not in the teacher's time.

---

## 5. Storing files

`/cut` stores nothing; it returns clips and forgets. Everything lives in one Drive folder: [OWNER: link].

```
VF Pilot/
  raw/{lesson_id}/                 lesson recording, backup recording      — delete at 90 days [Д]
  students/{student_id}/
    {lesson_id}/lesson-clips/      reference, best take, Before/Now         — keep while a student + 12 months [Д]
    {lesson_id}/home-takes/        the take the student sent                — delete at 90 days [Д]
    {lesson_id}/replies/           teacher's voice reply                    — keep while a student + 12 months [Д]
  admin/                           the six tables
```

- **IDs, not names.** Folders and files use `student_id` (S01–S10) and `lesson_id`. The only place a name meets an ID is the contact record in My Music Staff / Calendly, which the pilot tables never copy.
- **Private by default.** Folder access: that student's teacher and the named ops on-call (file handling only — ops checks that clips play, and doesn't review the singing). Methodologist and owner open a student's recordings only for a logged safety or privacy review, or if the student ticked the optional "head coach may listen" box; each access is a line in `pilot-flags.csv`. The Home Assignment Checklist audit uses the lesson table (flags, top note, task text), not recordings. Share a clip with the student by their email only — **never "anyone with the link."** No public posting of anything, at any level, during the pilot.
- **Retention** (same as Legal drafts 05 §2.2 and Student copy §7) [Д, pending lawyer]: raw lesson recordings, backup recordings and home takes are deleted 90 days after they're made; clips, Before/Now pairs, recaps and replies are kept while the person is a student and for 12 months after their last lesson, unless they ask for earlier deletion. Ops puts `delete_after` in `pilot-lessons.csv` and deletes on the first Monday after that date.
- **Deletion on request:** the student asks → ops deletes all their files within 7 days [Д] and logs it.
- **Consent check:** a file for a student whose consent box for that use is unticked is deleted immediately and logged as `flag_type = privacy`.
- No downloads to personal devices except to listen; no voice clips in chat apps outside the agreed channel.

---

## 6. Service levels

| What | Target | Measured in | Who covers a miss |
|---|---|---|---|
| Health flag ("hurts," "hoarse," "lost my voice") → first reply | **Same day, 100%**. If it arrives after [OWNER: 6 pm], ops on-call sends the SLP-approved holding reply the same evening; the teacher follows up next day | `pilot-flags.csv` | Ops on-call |
| Weekly voice reply | **≤48 h** after the student sends their take | `pilot-homework.csv` → `reply_hours` | Teacher; if a teacher is off, ops tells the student when to expect the reply — no silence |
| Recap after lesson | **<24 h** in ≥90% of lessons (≥36 of 40) | `pilot-lessons.csv` → `recap_hours` | Ops |
| Lost lessons | **0** | `pilot-lessons.csv` → `lesson_status` | Developer + owner review |
| Pipeline alert acknowledged | ≤4 working hours [Д] | `pilot-flags.csv` | Ops |
| Quiet Churn check-in sent | Within 2 days of the signal [Д] | `pilot-flags.csv` | Teacher (message drafted by ops if needed) |

---

## 7. Admin Offload — what stays outside the pilot

We **connect, not build.** Scheduling and money stay in the tool the teacher already uses.

| Job | Where it lives | Not in pilot tables |
|---|---|---|
| Lesson times, booking, rescheduling, cancellations | **My Music Staff**, or **Calendly** | ✓ |
| Reminders before lessons | MMS / Calendly built-in reminders | ✓ (our check-in is separate and is about practice, not attendance) |
| Payments, invoices, prepaid packages | MMS built-in payments, or **Stripe** (one-time Payment Links / paid Calendly event types) | ✓ — no card data, amounts, or invoices in pilot files |
| Student contact details | MMS / Calendly | ✓ — pilot tables use `student_id` only |
| Voice work: clips, tasks, replies, Before/Now, check-ins | Voice Family pilot (n8n + Drive + tables) | — |

Rules:

- **Flexible prepaid packages, no auto-renewal** for anything we sell. Starter Month is a one-time payment. If Stripe is used, don't create a subscription product for students.
- **Test prices only [Д], owner approves before use:** diagnostic lesson $29 vs $49; Starter Month ≈ $35 vs ≈ $45 per lesson-equivalent, with *"Not happy after your first month? Full refund."* No countdowns, "only 2 spots left," or other scarcity counters — anywhere.
- Whether current VF students pay anything extra for the pilot: [OWNER — not decided in the plan].
- Teachers log **admin minutes separately** (`activity = admin` in `pilot-teacher-time.csv`, outside the 20-minute budget). This tells us whether offloading worked. We publish **no** "saves X hours" claims until this log supports them (VF-088).
- Setup: 1 day of owner time. Integration with our tools: not before month 3.

---

## 8. Quiet Churn table

Adults rarely announce they're leaving; they go quiet. Among (child) instrument learners, how *many days* someone practices separates those who quit from those who stay — minutes don't [S28, level A for instrumentalists; transfer to adult singers is our assumption].

**Signal (any one):**

1. **≤2 practice days in each of 2 consecutive weeks** (self-reported in the check-in; a week with no answer counts as unknown, not 0), or
2. **2 lessons in a row without a Before/Now pair**, or
3. **A rescheduled or cancelled lesson** (from MMS/Calendly).

**Never a signal:** weeks marked "I'm sick," "A bit tired," or a health flag. Those weeks are excluded — the student is doing the right thing.

**Ops, every Monday (~15 min):** filter `pilot-homework.csv` by the rules above → add a row per new signal to `pilot-flags.csv` (`flag_type = quiet_churn`, `trigger_rule = practice_days | no_pair | reschedule`). One open quiet-churn flag per student at a time.

**Who sees it:** the student's teacher only (plus ops and methodologist). Never the student, never other teachers. It is not a grade and never appears in any message.

**Teacher's check-in (send as is, adapt freely):**

> "Hi [name], just checking in — no agenda. Weeks get busy, and that's normal. Is the current task still working for you, or should we make it smaller? A 5-minute version is completely fine. Or if something else would help more in our next lesson, tell me."

If the signal was "no pair two lessons running," the teacher instead looks at whether the task is too big, and aims for a small, honest in-lesson pair next time.

Close the flag with `outcome = contact_made | no_reply | student_paused | student_left` and the date. Target reported at week 8: share of signals followed by contact (k of n), and whether flagged students stayed.

---

## 9. Evidence & Decision Rules

### 9.1 How we treat evidence (VF-088)

- **Cohorts, not A/B**, inside the product. With n = 10 we don't split students into groups. A/B only on the landing page.
- **n = 10 is small.** Every result is written as **"k of n"** and treated as a *direction*, not proof. Pilot data is at most reliability B, always with n.
- **Thresholds are fixed before we measure** and never moved afterwards. Changes go in the version log with a date.
- **Sick weeks** leave the denominator.
- **Success of the pilot** = students *say* they hear a difference (student-reported) and renew. Not activity, not minutes, not streaks.
- **Nothing public** from this pilot without the student's separate consent. No time-saving numbers in marketing until the time log supports them. Any ad or testimonial carries "Results vary" and, where applicable, #ad.
- Every decision is written into the backlog with its source and tag [Ф] / [В] / [Д].

### 9.2 What we measure

**North Star (months 0–3): Weekly Coached Recorders (WCR)** — students who, in that week, sent **≥1 home take** *and* received **≥1 teacher reply approved through the AI Gate**. Report as `k / (active − sick)`.

| Guardrail | Threshold | Source table |
|---|---|---|
| Singing after "hurts"; clip sent home without "OK to sing at home" or above the lesson's top note | **0**; checklist audit on 100% of assignments | `pilot-lessons`, `pilot-flags` |
| Health flag → teacher reply + refer-out when needed | **Same day, 100%** | `pilot-flags` |
| Teacher time | Median **≤20 min/week** per teacher; weeks over 20 min **≤1 of 5** | `pilot-teacher-time` |
| Trust | "I felt judged" **≤1 of 5** who answered; "anxious" **≤2 of 5** | Coach Fit Check after lesson 3 |
| AI Gate | **0** unapproved texts sent; **≥80%** of captions approved without edits | `pilot-lessons` |
| Numbers about the voice shown to a student | **0** | `pilot-flags` (any breach logged) |
| Reliability | Recap <24 h in **≥90%** of lessons; **0** lost lessons | `pilot-lessons` |
| Price honesty | **0** "scam / hidden renewal" complaints | `pilot-flags` |
| Privacy | **10 of 10** recordings with consent; **0** recordings of under-18s | `pilot-students`, `pilot-flags` |

**Pilot signals:** home takes per student per week; replies within 48 h (k of n); lessons with a Before/Now pair (k of n); pairs opened (k of 10 students); "hear a difference" (student-reported, 1–5); students who left (k of 10); minutes at the start of online lessons spent on sound problems; minutes per student per week (teacher).

Any guardrail breach is reviewed **the same week**, regardless of the calendar below. A safety or privacy breach pauses home assignments for that teacher until the methodologist signs off.

### 9.3 Week 2 — go / no-go on the setup

| Result | Condition | Action |
|---|---|---|
| **Stop** | Any student without signed consent is being recorded, **or** an LLM step is on without a DPA | Recording stops today. Nothing resumes until fixed |
| **Limit** | No owner answer on who writes captions (plan §9 decision 1 / conflict №15) | Pilot runs; "your words" is not used anywhere |
| **Go** | `/cut` fixes live and §4.5 passed; **10 of 10** with consent; ≥1 teacher running 5 students; landing page takes sign-ups; ≥5 teacher conversations booked | Continue to week 4 |
| **Rework** | No time log | Week 3 goes on getting the time log working |
| **Time check (H9)** | Median ≤3 min per student per week | Teacher may take a 6th student |
| | ≈4 min per student (≤20 min total) | Stay at 5 |
| | >4 min per student | Plan R2: keep 5 students, voice reply every 2 weeks (health flags excluded), move manual AI Gate work to methodologist; minutes over 20 paid explicitly |
| **Founding Coaches (R4)** | <8 teacher conversations | Owner reviews own hours (plan decision №3) |

### 9.4 Week 4 — early signals [Д, runbook proposal — owner approves before start]

Week 4 **cannot** close or scale anything; it only triggers a review.

| Signal | Condition | Action |
|---|---|---|
| Recording habit | ≤2 of 10 students sent a take in ≥3 of the last 4 weeks (sick weeks neutral) | Methodologist + teachers look at task size and reply timing; no threshold changes |
| Reply SLA | <8 of 10 replies within 48 h in weeks 3–4 | Rebalance teacher load; ops adds reminders |
| Before/Now | Pair in fewer than half of the pilot lessons so far (k of n) | Check that teachers aren't skipping because clips are slow to cut |
| Quiet space (H8) | ≥3 of 10 answered "quiet" or "none" to "Where can you practice?" | Quiet-practice content (VF-048) is triggered per plan; first card includes "don't whisper-sing" |
| Quiet Churn | Any open flag without contact for >7 days | Owner asks why |
| Time | Any teacher over 20 min in 2 of 4 weeks | Methodologist steps in now, don't wait for week 8 |

### 9.5 Week 8 — decisions (plan §5.2; direction, not proof)

| Decision | Scale | Rework | Close |
|---|---|---|---|
| **Homework loop (VF-011, n = 10)** | **≥5 of 10** send ≥1 take/week for 4 consecutive weeks **and** **≤2 of 10** left **and** teacher median ≤20 min | 3–4 of 10, **or** teacher spends 20–30 min → reply every 2 weeks (except health flags) | **≤2 of 10** → playlist only, no code written |
| **Before/Now (VF-036, ≈40 lessons)** | Pair in **≥28 of 40** lessons; opened by **≥5 of 10** students; "hear a difference" (student-reported) **≥4 of 5** [OWNER: confirm reading as median ≥4 on the 1–5 scale] | Pair in 20–27 of 40, **or** opened by 3–4 of 10 | Opened by **≤2 of 10** → passport (VF-038) not built |
| **Teacher time (VF-058)** | Median ≤20 min at week 2 **and** week 8 | 20–30 min → shorten the voice reply | >30 min → pilot stops; loop simplified |
| **Quiet Churn (VF-060)** | Report only: signals followed by contact (k of n); flagged students still active (k of n) | — | — |
| **Online Studio Check (VF-056)** | Report only: median minutes on sound at lesson start, before vs after the PDF; share of online lessons without sound problems (k of n) | — | — |

Retention is reported as k of 10 over 4 weeks. Renewal after lesson 5 is compared with **earlier VF cohorts**, and any positive gap is described only as "compatible with H2" — never as proof that hearing progress causes renewal.

---

## 10. Tables — what each file is for

All in `pilot-kit/templates/`, headers only. One row per:

| File | One row per | Filled by |
|---|---|---|
| `pilot-students.csv` | Student | Ops at setup; status updated weekly |
| `pilot-lessons.csv` | Lesson (`lesson_id`) — also the pipeline status table until VF-022 automates it | n8n / ops, teacher for AI Gate columns |
| `pilot-homework.csv` | Student × pilot week | Ops |
| `pilot-teacher-time.csv` | Work session (one activity, one student) | Teacher, at the moment of work — not reconstructed later |
| `pilot-flags.csv` | Flag (health, quiet churn, pipeline, safety, privacy, trust, price) | Whoever sees it first; ops owns closing |
| `pilot-metrics-weekly.csv` | Pilot week | Ops, every Monday |

**Coded values** (use exactly these):

- `yes` / `no` / blank = unknown.
- `activity` (teacher time): `timecodes`, `listen_clips`, `captions_ai_gate`, `checklist`, `pick_pair`, `listen_take`, `voice_reply`, `discuss_reply`, `quiet_churn_checkin`, `other_pilot` — **in budget**; `health_flag`, `snapshot`, `admin`, `fit_check_review` — **out of budget**.
- `flag_type`: `health_hurts`, `health_hoarse`, `health_tired_twice`, `sick_pause`, `quiet_churn`, `pipeline`, `safety_checklist`, `privacy`, `under_18`, `trust_judged`, `voice_number_shown`, `price_complaint`.
- `reaction`: `closer`, `same`, `lets_discuss`, `none`.
- `pair`: `in_this_lesson`, `across_lessons`, `skipped_no_honest_change`, `skipped_tech`.
- `lesson_status`: `recorded`, `cut`, `approved`, `recap_sent`, `sent_without_clips`, `lost`.

**`teacher_seconds` rule:** start a timer when you open the work, stop when you send. One row per activity. Round to the nearest 10 s. Don't estimate afterwards — a missing row is better than a guessed one (and mark the week `time_log_complete = no`).

---

## Appendix A — Online Studio Check (student PDF, send as is)

*[Methodologist: review before sending. Zoom menu names change between versions — check them on a current Zoom build before release.]*

---

# Your Online Studio Check

**5 minutes, once — and your lessons start with singing, not "Can you hear me?"**

Online lessons work. What they can't do well is carry the full sound of your voice — video calls squash it to make speech clearer. This page sets up your space so your coach hears as much of your real sound as possible, and gives you a backup so nothing important is lost.

Do this once, a day or two before your first lesson. If anything here doesn't work on your device, that's fine — skip it and tell your coach. We'll sort it out together.

## 1. Turn on "Original Sound" in Zoom

Zoom normally removes background noise — and it treats sustained singing as noise.

**On a computer (Zoom app):**
1. Open Zoom → **Settings** → **Audio**.
2. Under the audio profile, choose **Original sound for musicians**.
3. Tick **High-fidelity music mode** if you see it.
4. **Echo cancellation:** leave it **on** unless you're wearing headphones.
5. **In the lesson:** look for **"Original sound: Off"** at the top of the window and click it so it says **On**. You need to do this every lesson.

**On a phone or tablet (Zoom app):**
1. Zoom → **Settings** → **Meetings** (or **Audio**) → turn on **Original Sound** (it may be called "Original Sound for Musicians").
2. **In the lesson:** tap **More** → **Enable Original Sound**.

**On a Chromebook or in a web browser:** the Original Sound option may be missing or limited. Use Zoom's app if you can; if not, the backup recording in step 5 matters even more.

Can't find it? Search Zoom's settings for "original sound," or just tell your coach at the start of the lesson.

## 2. Your microphone

- **Built-in laptop or phone mic is fine** to start. You don't need to buy anything.
- **Distance:** about **8–12 inches (20–30 cm)** from your mouth, and keep it the same every lesson.
- **Face the mic** but don't sing straight into it from very close — that makes loud notes distort.
- **Headphones:** optional. If you use them, backing tracks won't leak into your mic. If you don't, keep echo cancellation on.
- **Quiet the device:** turn on **Do Not Disturb** so notifications don't cut into a take.

## 3. Camera: waist-up

Your coach needs to see more than your face — breathing, shoulders, jaw, and posture tell them a lot.

- Set the camera **at eye level**, far enough back to show you **from the waist up**, hands included.
- **Light in front of you** (a window or lamp behind the camera), not behind you.
- **Stand if you usually sing standing.** Prop the laptop or phone on a shelf or stack of books.
- Plain background is great; a tidy one is fine. Nobody is judging your room.

## 4. Gesture card — when the sound drops

Sometimes the connection freezes or the sound cuts out mid-exercise. Use these instead of talking over each other:

| Gesture | Means |
|---|---|
| Thumbs up | I can hear you fine |
| Hand cupped behind your ear | I can't hear you — please repeat |
| Rolling your hand forward | Keep going / play it again |
| Flat hand, palm out | Pause |
| **Hand resting on your throat** | **Something doesn't feel right in my voice — let's stop** |

That last one always wins. Stopping is never "being lazy" — it's looking after your voice.

## 5. Backup recording (your real sound)

**Your coach hears your real sound, not Zoom's.** A recording made on a second device near you captures your voice without the call squashing it. Your coach can use it for your reference clips and your Before/Now pair.

1. If you have a **second device** (phone, tablet), open its built-in **voice recorder** app (Voice Memos on iPhone, the Recorder app on Android).
2. Put it **8–12 inches (20–30 cm)** from you, **same side as your main mic**, and press record before the lesson starts.
3. **Clap once** clearly when the lesson begins. (It lets us line up the two recordings.)
4. After the lesson, stop the recording and upload it here: **[OWNER: private upload link]**.

If Zoom is running on your only phone, skip this — most phones can't record while on a call. That's fine.

**Private by default.** Only your coach listens to your recordings. One named person on our team handles the files to cut your clips, but doesn't review your singing. They're never posted anywhere, Full recordings are deleted after [90 days — OWNER to confirm]; your clips and Before/Now pairs stay while you're a student and for [12 months] after, unless you ask us to delete them sooner. You can ask us to delete them any time.

## 6. Two minutes before each lesson

- [ ] Somewhere you're comfortable being heard (a closed door is enough).
- [ ] Water nearby.
- [ ] No need to sing loudly or high to test the sound — a spoken sentence or a gentle hum is enough. Your coach will warm you up.
- [ ] Device charged or plugged in; Do Not Disturb on.
- [ ] Zoom open; **Original Sound → On** once the lesson starts.
- [ ] Camera waist-up, light in front.
- [ ] Backup recorder running (if you have a second device) — clap once at the start.

**Still stuck?** Tell your coach at the start of the lesson. We'd rather spend two minutes fixing it together than have you worry about it.

*UK version: "practise" (verb), "term" for teaching periods; distances unchanged. Keep "coach" in both versions.*

---

## Version log

| Version | Date | Change | Data |
|---|---|---|---|
| 0.1 | 2026-09-26 | First runbook from product plan v1.0, decisions VF-011, VF-022, VF-023, VF-036, VF-056, VF-058, VF-060, VF-073, VF-088 | None yet — all time estimates [Д] |
