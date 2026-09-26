# Voice Family Pilot — Teacher Handbook

<!--
ДЛЯ ВЛАДЕЛЬЦА (RU, коротко)

Что это: готовая памятка для 2 педагогов ручного пилота «Недели 0–2» (VF-001, VF-011, VF-025, VF-030,
VF-035, VF-036, VF-043, VF-044, VF-054, VF-058, VF-063). Всё ниже линии — английский текст для педагогов,
его можно отдавать как есть (PDF / Google Doc / Notion).

Что осталось заполнить или утвердить перед выдачей (помечено [OWNER] / [SLP] в тексте):
1. Имена и контакты: методист, ops-дежурный по флагам здоровья (ответ в тот же день), канал связи.
2. Refer-out текст (шаблон 9) и список red flags — черновик по weekly-homework-spec §2.6; до выдачи
   должен одобрить SLP/фониатр (VF-065, 1–2 ч). Без одобрения шаблон 9 не используем, пишем только
   «please check in with a doctor or voice specialist».
3. Кто пишет подписи в n8n (решение №1 раздела 9). Памятка написана под вариант «пишет педагог,
   LLM-шаг снят до DPA». Если LLM останется — раздел 8 надо переписать.
4. Оплата минут сверх 20/нед и Snapshot (решение №5) — в разделе 9 стоит заглушка.
5. Числа (4 мин на студента, 5 студентов, 25 мин/день, ≤48 ч) — [Д] из плана, не факты; пересмотр
   после хронометража недели 2.
Текст — US English. Для UK: practice→practise (глагол), semester→term; «pupil» допустим в разговоре педагогов, но в текстах
для взрослых студентов остаётся «student» (как в 02 и 05). Шаблоны §12 написаны без слов, которые расходятся в US/UK.
Цены в памятке не упоминаются намеренно: педагог их студенту не называет.
-->

**Version 0.1 · Pilot weeks 0–2 · Internal — for pilot teachers only**

---

## 0. The one-page version

If you read nothing else, read this.

1. **Teach your lesson exactly as you do now.** Nothing new happens during the lesson.
2. **After the lesson, spend about 4 minutes per student:** pick 2–4 timecodes (your demo, the student's best take, the two halves of a Before/Now pair) and give 1–2 tasks. Once a week, send one voice reply to the home take the student chose.
3. **Never judge talent.** No "natural," no "not a singer," no voice-type labels before diagnosis.
4. **Every piece of feedback = one specific win → why it worked → 1–2 tasks.**
5. **Nothing goes home to sing unless you marked it "OK to sing at home."** The default is no.
6. **"It hurts" means stop. You reply the same day.** You don't diagnose — you refer out.
7. **Recordings are private by default.** The student hears their first recording with you, not alone.
8. **No numbers about the voice** — no scores, percentages, or ratings to the student.
9. **Every word the student sees was written or approved by you.** No AI text goes out unreviewed.
10. **Log your minutes.** Our limit is 20 minutes per week for all your pilot students. If you go over, tell us — that's our problem to solve, not yours.
11. **Adults only (18+).** Age is confirmed before any recording.

---

## 1. Why this pilot exists

Most adult students practice alone between lessons, without a reference, and can't tell whether they are getting better. Many arrive carrying an old label — "too late," "not a singer" — and one careless word can confirm it.

The pilot tests one simple loop, done by hand, with no new software for you:

**lesson → reference clip + task → home attempt → your voice reply → Before/Now pair**

We want to learn three things:

- Will students record at least once a week if a real teacher answers?
- Can students *hear* their own progress when they get a Before/Now pair?
- Can you run this in **20 minutes a week or less** for five students?

Your honest feedback — including "this takes too long" or "students don't care" — is exactly what we need. A "no" is a useful result.

**Pilot size:** 2 teachers × 5 students each. Adults 18+ only. Duration: at least 4 weeks after setup.

---

## 2. What you do

### 2.1 During the lesson: nothing new

- No pedals, no apps, no marking, no extra screens.
- The lesson is recorded as usual (with the student's signed consent — we check this before lesson 1).
- **Lesson 1 only:** at the end, the student makes their first home-style recording *with you in the room*, and you listen back together (see §6). Until this happens, the student does not record on their own.

### 2.2 After the lesson: about 4 minutes per student

| Step | What you do | Time (estimate) |
|---|---|---|
| 1 | Pick **2–4 timecodes** from the recording: your demonstration (reference), the student's best take, and the two halves of the Before/Now pair (step 3) | ~0.5 min |
| 2 | Choose **one reference clip** — your demo of the phrase or exercise the student will practice | included above |
| 3 | Pick the **Before/Now pair** (see §2.4) | ~0.5 min |
| 4 | Write or approve the **captions** and the **task** (1–2 tasks max), using the Feedback Template (§4) | ~1 min |
| 5 | Run the **Home Assignment Checklist** (§5.1) — especially the "OK to sing at home" flag | ~0.5 min |
| 6 | **Once a week:** listen to the take the student chose and send a **voice reply** (§2.3) | ~1 min listen + ~1 min reply |

Timecodes go into the usual n8n form as the moment the phrase **starts**, in **whole seconds** (e.g., `02:14`). Fractional seconds (`02:14.5`) work only after the VF-023 fix is live; until then they come back as failed clips (Runbook §4.3).

### 2.3 The weekly voice reply

- The student picks **one** home take for you to hear. You reply to that take — you do not have to hear every take, and we never promise that you will.
- **One voice reply per week is included.** Reply within **48 hours** of the student sending it.
- Use the Feedback Template: one specific win → why → 1–2 tasks. Aim for **30–60 seconds**.
- The student can react to your reply with **"closer," "same,"** or **"let's discuss."** If they choose "same" or "let's discuss," answer by **voice**, not text — it lands better, and it counts as that week's reply.
- After the lesson, students answer one short reflection question and can mark "⭐ my best moment." Glance at it if you have time — it often tells you what to praise.
- **Health flags are separate.** A pain or hoarseness message is never "wait for the weekly reply." See §5.

### 2.4 The Before/Now pair

A Before/Now pair is two short clips of **the same phrase, in the same key**, so the student can hear what changed.

- **Lessons 1–2:** the pair comes from *inside the same lesson* — an early attempt and a later attempt. Caption it **"in this lesson."**
- **From lesson 3:** you may also pair a take from an earlier lesson with one from this lesson.
- Add one line: **"What changed:"** — concrete and audible. ("What changed: the last note stays on pitch instead of sliding down.")
- If there is no honest improvement to show, **don't force one.** Skip the pair and say so in your reply ("Not a Before/Now week — we built the foundation today."). A fake pair costs trust.
- Target: a pair in most lessons (roughly 7 out of 10), not every single one.

---

## 3. No Talent Verdicts

Many adults start singing late because someone once told them they couldn't. Our single most important rule: **we talk about skills and actions, never about gifts, talent, or fixed traits.**

**Never say or write:**

- anything about talent, gift, being "natural," or "having it / not having it";
- "tone-deaf," "no ear," "not a singer," "too old," "too late";
- a voice type (soprano, baritone, etc.) before the diagnostic lesson — and even then, only you decide it, and only as a working guide;
- comparisons with other students or famous singers;
- predictions ("you'll never…", "you'll be ready for X by…").

### Instead of → Say

| Instead of | Say |
|---|---|
| "You're a natural!" | "Your breath held all the way to the end of that phrase — that's the support work paying off." |
| "You're a bit tone-deaf." | "The first note landed. The jump up to the second is where it drifts — let's slow that jump down." |
| "Singing just isn't your thing." | "This is a skill, and we're at the start of it. Here's the next small step." |
| "You're definitely a soprano." | "Let's work in this comfortable range for now. We'll learn more about your voice as we go." |
| "You're too old to fix that." | "Voices keep learning at any age. This week, just this one change." |
| "Wow, you have such a good voice." | "The vowel on 'home' was open and relaxed — that's why it rang." |
| "That was bad." / "That was off." | "The second half pulled sharp. Try it at half the volume and see what happens." |
| "You sound like [famous singer]." | "The phrasing on the chorus was really clear — I could hear every word." |
| "Everyone else gets this by now." | "This one takes time for most people. We'll come back to it next week." |

If a student uses a verdict about themselves ("I'm just tone-deaf"), don't argue and don't agree. Redirect to the evidence: "Let's listen — the first two notes were right on. We're working on one jump, not your whole ear."

---

## 4. Feedback Template

Every piece of feedback — captions, tasks, text replies, voice replies — follows the same shape:

> **1. One specific win** — something concrete that happened in *this* take.
> **2. Why it worked** — the action or sensation behind it, so the student can repeat it.
> **3. One or two tasks** — what to do, and *how* to do it.

Rules:

- "Good," "nice," "great job," or "keep practicing" **on their own** are not feedback. They're fine as a warm-up word *before* the specific win.
- Answer the **how**, not just the what. A student should never finish reading or listening and think, "but how?"
- **Maximum two tasks.** If you gave five corrections in the lesson, pick the two that matter most. The rest become "listen to this" clips.
- Tasks must be sung within the limits in §5 (comfortable range, no higher than the top of the lesson).

### Good vs. not good

**Example 1 — voice reply to a home take**

- **Not this:** "Great job! Sounding good. Keep practicing!"
- **This:** "The first line of the chorus was steady and relaxed all the way through — you kept your shoulders down on the breath, and that's why it didn't wobble. This week: sing just the last line on a lip trill three times, then on the words once. Keep it at the volume you'd use to talk to a friend."

**Example 2 — caption for a lesson clip**

- **Not this:** "Pitch issues in the bridge."
- **This:** "Win: the bridge started right on the note. Why: you heard it first before singing — you hummed it. Task: hum the first note of each bridge line before you sing it."

**Example 3 — when not much improved**

- **Not this:** "Same as last week. Needs more work."
- **This:** "Your breath was quieter this time — I didn't hear you gasp before the second phrase, and that's new. The high note still tightens, so let's leave it out this week: sing the phrase and stop one note before the top. Two times per practice session, max."

**Example 4 — beginner, first week**

- **Not this:** "Nice start!"
- **This:** "You matched my first note on your second try — you listened, then sang. That's the whole skill in small form. Task: play my clip, hum along once, then sing along once. That's it."

---

## 5. Voice Safety Rules

*Not medical advice. We coach singing; we do not diagnose.*

These rules are not optional and they are not up for trade against any metric. When in doubt, choose the safer option and tell the methodologist.

### 5.1 Home Assignment Checklist (run before every assignment goes out)

Tick every box before you approve an assignment. If one box fails, fix it or don't send.

- [ ] **"OK to sing at home" is set on purpose.** The default is **no**. Clips without the flag go home as *listen-only*.
- [ ] **Top note ≤ the top note the student sang comfortably in this lesson** (and ≤ their working range). The home top never goes higher than the lesson top.
- [ ] **No load-3 work at home:** no range edges, no belt, no loud climaxes, no loud mix, no fry/distortion/screaming, no hard onsets, no breath-holding, no "endurance" drills — **unless you personally assigned it and wrote why.**
- [ ] **Session length and daily limit stated:** a normal home session is **10–15 minutes** (12–15 in the first two weeks, up to 20 later only if you decide). **25 minutes of singing a day is a hard ceiling, not a target** — the task says so. One session a day at most; missed sessions don't pile up.
- [ ] **Rest built in:** no singing on the lesson day itself; the day after the lesson is **listening only**; at least **one more full rest day** in the week; the day before the next lesson is a light version (no top notes, medium-soft volume). No two sessions in a row that touch the top of the range.
- [ ] **Stop line included:** every task ends with the stop line — *"If your throat tickles, pulls, or hurts, stop. That's not being lazy, that's looking after your voice."*
- [ ] **Words are yours:** you wrote or approved every word of the caption and task (§8), and it follows the Feedback Template (§4).

Across a week, range and volume **never go up.** Only tempo, phrase length, and number of repetitions can grow. Exercises are sung in a key comfortable for the student, not the original recording's key.

### 5.2 "How's your voice today?"

Students answer this before each home session:

- **Feels fine** — do the plan as written.
- **A bit tired** — light version only: warm-up, listening, cool-down. *If a student says "tired" two sessions in a row, you'll get a heads-up the same day — check in.*
- **Hoarse, sore or it hurts** — all singing stops (see 5.4).

Students also have an **"I'm sick"** option (same four answers as the pre-lesson check-in, Student copy §6). It pauses the plan for 1–7 days; that week doesn't count as missed and nobody chases them. After a pause, the first session is only gentle exercises (lip trills, humming) and listening.

### 5.3 Stop signals (for the student, and for you)

Stop immediately at: pain, burning, scratching, "clicks," the voice cutting out, coughing, dizziness — or hoarseness that doesn't clear after 10 minutes of rest.

Tell students plainly in lesson 1: *"Stopping early is always the right call. You will never be in trouble for stopping."* Students sometimes hide pain so they don't "fall behind." Make it safe to tell you.

### 5.4 "It hurts" → stop, same-day reply

When a student reports pain, hoarseness, or a stop signal:

1. **All singing homework is off** until *you* decide otherwise. There's no automatic timeout. Listening and silent breathing only.
2. **Reply the same day** (template 8 or 9). This does not come out of your 20-minute budget and is never cut to save time.
3. If you can't reply that day, the **on-call flags contact** does: [OWNER: name, contact].
4. **Do not diagnose.** Don't guess causes, don't suggest medication, don't say "it's probably nothing."
5. Health messages are handled **by people only** — never paste them into any AI tool.
6. Don't keep health details in your notes beyond "flag raised / replied / referred."

### 5.5 Where our job ends: SLP / ENT

We're voice teachers, not clinicians. **Refer out** — recommend the student see an ENT (laryngologist) or a speech-language pathologist (SLP) who works with singers — when:

- hoarseness or voice change lasts **more than 2 weeks** [SLP: confirm threshold];
- pain when singing or speaking that doesn't go away with rest;
- sudden voice loss, or the voice "cracks" or cuts out in a new way;
- the student mentions a known voice or medical condition, surgery, or medication that dries the throat;
- anything that feels outside your training.

**Don't wait for any threshold — tell the student to get medical help now** [SLP: confirm list] if they mention: trouble breathing (emergency services), coughing up blood, severe or sudden pain, or a sudden complete loss of voice after a shout, strain or injury. Then tell the methodologist the same day.

Use template 9 (pending SLP approval). When in doubt, refer — referring out is never wrong.

---

## 6. Private by Default

Hearing your own recording for the first time is a shock for many adults — some stop singing for years after it. So:

- **Every recording is Private.** Only the student and you listen to it. One named ops person handles the files (cutting clips, fixing technical problems) but does not review the singing. The methodologist or owner opens a recording only for a logged safety or privacy review, or if the student ticked the optional "head coach may listen" box. The school owner sees nothing otherwise.
- The student's **first recording happens in lesson 1, with you.** You listen together, and you speak first — with one specific win.
- Before playback, say something like: *"Almost everyone thinks their voice sounds strange on a recording. That's because you normally hear yourself partly through your own head. The recording is how everyone else already hears you — and it usually sounds better to them than it does to you."*
- Default setting for home takes: **"Coach hears it first."**
- Never share, play, or post a student's recording (class, social media, other students, "as an example") without their explicit, written, per-recording permission.

---

## 7. Honest Metrics

- **No numbers about the voice go to the student.** No scores, percentages, star ratings, "pitch accuracy," "range: X notes," or charts.
- No XP, streaks, badges, leaderboards, "you missed X days," or comparisons with others. Practice days may be mentioned only as "how much you practiced" — never as "how much your voice improved."
- Progress is shown by **ears, not numbers**: Before/Now pairs and your words.
- Claims must be **comparable:** same phrase, same key. Don't compare a warm-up to a performance.
- With fewer than 3 lessons, don't draw conclusions: *"We're still building your baseline."*
- **Bad news comes from you**, by voice, before the student reads it anywhere else.
- Don't promise results ("you'll hit that note in a month"). Describe what you heard.

---

## 8. AI Gate: every word is yours

For the pilot, **the LLM step is switched off.** You write the captions and tasks yourself. The principle for now and later: **tools assist you, they never replace you** — the judgement, the words and the relationship are yours.

- In n8n, every caption and task needs your decision: **✓ approve · ✎ edit · ✗ reject.**
- Each caption records who wrote it (`caption_source`). Don't mark text as yours if you didn't write or fully approve it.
- **Nothing reaches the student without your ✓.** Zero exceptions.
- Never paste student recordings, health messages, or personal details into any AI tool (ChatGPT etc.) — including your own accounts.
- If AI assistance is switched back on later, it will only rephrase *your* words, and you'll still approve every line. We'll tell you before it changes.

---

## 9. Teacher Time Budget

- **Budget: 20 minutes per week** of async work for all your pilot students (≈4 minutes × 5 students).
- **Log your minutes** every time — start/stop, per student — in the tracking sheet [OWNER: link]. Rough is fine; missing is not. This is the single most important number in the pilot.
- **Outside the budget** (log separately, never cut): health-flag replies, Snapshot replies.
- **If you go over 20 minutes,** don't cut corners and don't work for free — log it and tell the methodologist. The fix is ours: fewer students, a reply every two weeks, or handing the approval step to the methodologist.
- Pay for minutes over 20 and for Snapshots: [OWNER: to be confirmed].
- Honest minutes help us more than fast-looking minutes. A slow week is data, not failure.

---

## 10. Adults only (18+)

- Every pilot student is **18 or older.** Age is confirmed **before any recording** — including the lesson-1 recording.
- If you find out a student is under 18, **stop recording immediately**, don't send anything, and tell the methodologist the same day. We'll handle the rest.
- Don't bring students under 18 into the pilot, even with a parent's permission. That decision sits with our lawyer and owner, not with us.

---

## 11. When a clip fails

Clips are cut by our tool from the lesson recording. Sometimes that breaks.

| What you see | What you do |
|---|---|
| Clip is empty, 0 seconds, or silent | Don't send it. Recheck timecodes (format `mm:ss`, whole seconds until VF-023 is live), resubmit once |
| Clip is the wrong moment | Fix the timecodes, resubmit. Don't send "close enough" as a Before/Now pair |
| A clip shows as "skipped," or you get an error | Don't retry more than once. Send the tech contact [OWNER: name] the student ID, lesson date, and timecodes |
| Lesson recording missing or unusable | Tell the student honestly (template 10), send the text task without a clip, and use the next lesson for the pair |
| Clip arrives but you're not sure it's right | Listen before you approve. You approve everything the student receives |

Never send a broken or wrong clip just to hit a deadline. A short honest message is better. Log the failure in the tracking sheet so we can fix the tool.

---

## 12. Reply templates

Fill the brackets. Adapt freely to your own voice — but keep the shape (win → why → 1–2 tasks) and the safety lines. The templates avoid words that differ between US and UK English, so they work as is for both.

**1. Weekly voice reply — progress heard**
> "Hi [name], I listened to your take of [song/exercise]. [Specific win — e.g., the long note at the end stayed steady.] That happened because [why — e.g., you took the breath earlier and didn't rush it]. This week, [task 1 — what + how]. [Optional task 2.] Keep it comfortable and short — 10 to 15 minutes is enough, never more than 25 minutes of singing in a day — and stop if anything feels tight."

**2. Weekly voice reply — "same" / no clear change**
> "Hi [name], thanks for sending this. [Small real win — e.g., your start was calmer than last week.] The [part] still feels the same, and that's normal — this kind of change often takes time, and it's different for everyone. Let's make it smaller: [simplified task — e.g., just the first three notes, slowly, on 'ng']. Send me that one next week."

**3. Reply to "let's discuss"**
> "Hi [name], glad you asked. [Answer their question in one or two sentences.] Here's how to try it: [concrete how]. If it still doesn't click, we'll go through it at the start of our next lesson."

**4. Lesson recap caption (text)**
> "Win: [what worked in today's lesson]. Why: [what you did]. This week: [task 1]; [task 2 if any]. Clips: my demo, your best take, and a Before/Now 'in this lesson.' Listen-only clips are marked — please don't sing those at home yet."

**5. Before/Now caption**
> "Before/Now (in this lesson): [phrase]. What changed: [one audible change — e.g., the vowel on 'light' opened up, so the note rang instead of pinching]."

**6. First recording (lesson 1, together)**
> "Before we listen: almost everyone thinks their voice sounds strange on a recording — you usually hear yourself through your own head. Let's listen once, and I'll tell you the first thing I hear that's working."

**7. Student said "I'm just not a singer / too old"**
> "I hear that a lot, and I get it. Singing is a skill, not a gift — and skills build at any age. Today you [specific win]. That's real, and it's yours. Next small step: [task]."

**8. Tired twice in a row**
> "Hi [name], I saw 'tired' twice this week — thanks for telling me, that's exactly right. Let's go easy: warm-up, listening, and cool-down only until our next lesson. How's your voice when you're speaking? If it feels scratchy or hoarse, stop singing completely and let me know today."

**9. "It hurts" / hoarse — same-day reply** *[SLP: approve wording before use]*
> "Hi [name], thank you for telling me. Please stop all singing for now — listening only, no humming or warm-ups until we talk. Rest your voice, sip water, and avoid shouting or whispering. I'm not able to diagnose anything, but if the hoarseness or pain lasts more than [2 weeks — SLP to confirm], or it's getting worse, please see an ENT or a speech-language pathologist who works with singers [UK: your GP, an ENT, or a speech and language therapist]. If you have trouble breathing, cough up blood, have severe pain, or lost your voice completely and suddenly, please get medical help straight away — don't wait for me. Stopping early is always the right call — you're not behind. Let me know how it feels [tomorrow / in two days]."

**10. Clip failed / recording missing**
> "Hi [name], quick heads-up: the recording from today's lesson didn't come through properly, so your clips are missing this week — sorry about that. Your task still stands: [task in words]. We'll make a new reference clip in our next lesson."

---

## 13. Contacts

| Role | Name | How to reach | When |
|---|---|---|---|
| Methodologist | [OWNER] | [OWNER] | Questions on rules, over-budget weeks, under-18 cases |
| On-call for health flags | [OWNER] | [OWNER] | Same day, if you can't reply |
| Tech (clips, n8n) | [OWNER] | [OWNER] | Clip failures, missing recordings |
| Time log | — | [OWNER: sheet link] | Every session |

*Questions or disagreements with any rule here? Raise them — the rules exist to protect students and you, and we'll change wording that doesn't work in a real lesson. Safety, privacy, 18+, the AI Gate, and the 20-minute budget stay fixed.*
