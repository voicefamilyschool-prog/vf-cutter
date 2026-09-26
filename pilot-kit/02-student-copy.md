# 02 — Student copy: landing, offers, Voice Snapshot

*Пакет пилота Voice Family, недели 0–2. Решения плана: VF-002, VF-003, VF-004, VF-005, VF-007, VF-008, VF-009, VF-045, VF-047, VF-054, VF-063. Источник: `reports/voice-family-product-plan.md` v1.1 и `reports/voice-family-backlog.csv`.*

## Для владельца (коротко)

- **Синхронизировано с планом v1.1 (2026-09-26).** Правки — по разделу 11 плана.
- **Что это.** Готовые тексты для no-code лендинга (VF-006), страниц оффера, Snapshot, писем и двух форм (Tally/Typeform). Всё, что видит студент, — на английском (US). UK-варианты слов помечены `[UK: …]` и собраны в таблице в конце.
- **Цены — только тестовые [Д]**, из плана §4.3: Snapshot $0 без карты; диагностика $29 (вариант B $49); Starter Month 4 × 30 мин — **$140 или $180 за месяц** (v1.1: цена за месяц, а не «за урок-эквивалент»). Финансовое правило (план §4.3): связку $140 + $29 держим, только если медиана Snapshot ≤3 мин **или** Snapshot → диагностика ≥20%; иначе поднимаем одну из цен. В тексте цены стоят в фигурных скобках `{…}`. Меняйте их в одном месте конструктора.
- **Чего в текстах нет специально:** баллов, вердиктов о таланте и типе голоса, диапазона и Key Card в Snapshot, сроков вида «30 days to…», счётчиков дефицита и таймеров, отзывов и статистики. Отзывов нет, потому что их нет [Ф]; до первых реальных отзывов блок не ставим.
- **Нельзя публиковать без проверки** (помечено `[CHECK: …]`):
  1. «A person listens. No AI scores your voice» — верно, пока LLM-шаг снят (нет DPA, решение №15 плана). Если LLM вернётся, фразу меняем.
  2. «Never used to train AI» — только если это правда для всех подрядчиков (VF-064). Пока фраза стоит как условная.
  3. Возврат, автопродление, согласие на запись, хранение 90 дней — юрист (раздел 9, п. 4).
  4. Refer-out, стоп-сигналы и инструкцию к записи Snapshot — текст должен одобрить SLP (VF-065). Все места с `[CHECK: SLP…]` **не публиковать до одобрения SLP**; пометки снимаем только после одобрения. Ни одной неодобренной пометки [SLP] — условие стоп-ворот недели 2.
  5. Упражнения в ответах Snapshot — только нагрузки 1 без верха, из списка, одобренного SLP. Если списка нет, упражнения в ответе нет (VF-009).
- **Snapshot только после цены и контакта** (правка R3). Поэтому на странице Snapshot блок цен стоит над формой, а форма начинается с email.
- **Потолок Snapshot — ≤5 в неделю на педагога (≤20 мин), отдельный лимит [Д].** Общий потолок педагога ≤40 мин/нед [Д], утверждает владелец; флаги вне лимита. Вместо счётчика — честный лист ожидания с датой (VF-007, VF-009).
- **Перед записью Snapshot — вопрос о здоровье** («Is your voice hurting or hoarse…»). Ответ «Yes» ведёт к Refer-out без записи (VF-009, VF-065).
- **Окно возврата {7} дней** остаётся в скобках `{…}` до ответа юриста (VF-008).
- **Если H1 откатится до «ответа раз в 2 недели»**, до продаж заменить "one voice reply a week" во всех местах (§1.3, §1.5, §2, §3, письмо 5.4) — одновременно с текстами VF-006 и VF-008.
- **Before/Now:** в первых уроках — пара «in this lesson». Пары между уроками — не раньше урока 3 (решение №12). Тексты это соблюдают.
- **Подписи в recap** названы «a short note from your coach». Формулировку «your words» не используем, пока нет ответа по №15.

---

## Contents

1. Landing page
   - 1.1 Hero (A/B)
   - 1.2 How it works
   - 1.3 What you get every week
   - 1.4 Safe by design
   - 1.5 Honest pricing (landing block)
   - 1.6 FAQ (12 questions)
   - 1.7 Footer rules
2. Honest Pricing Rules (site page)
3. Starter Month offer page
4. Voice Snapshot page + coach reply template
5. Emails (5 + 1)
6. No-Blame Pre-Lesson Check-in
7. First Week Setup form
8. UK wording table
9. Copy QA checklist (before publishing anything)

---

## 1. Landing page

> Порядок блоков: Hero → How it works → What you get every week → Safe by design → Honest pricing → FAQ → Footer. HOME («соседи», «тонкие стены») в hero не ставим (решение №1): он только в FAQ.

### 1.1 Hero — two variants for A/B (VF-006, H7)

**Variant A — "Coach, not a score" (VF-003)**

> **A real coach replies to your practice every week. No scores, no verdicts.**
> Just a real voice coach, your lesson, and a plan you can actually practice. [UK: practise]
>
> [ Get a free Voice Snapshot ]  [ See prices ]
>
> *Free. No card. A coach replies within 48 hours. Adults 18+.*

**Variant B — "Start from zero" (VF-002)**

> **Too old? Told you can't sing?**
> **Singing is a skill, not a gift.**
> We start where your voice is today — even if you can't match pitch yet. A real coach, one small step at a time.
>
> [ Get a free Voice Snapshot ]  [ See prices ]
>
> *Free. No card. A coach replies within 48 hours. Adults 18+.*

Под hero (для обоих вариантов), одна строка:

> Sing for 60 seconds — or just hum. A coach tells you one thing that's already working and one thing to try first.

> Метрика A/B: клик «Get a free Voice Snapshot» → отправленная форма Snapshot. Вариант держим до ≥100 визитов на ветку или 2 недель [Д]; при малом трафике это «направление», а не вывод (R1).

---

### 1.2 How it works

**How it works**

1. **Sing or hum for 60 seconds.**
   Record on your phone, wherever you feel OK. Humming is fine. Nobody else hears it — only one coach.

2. **A coach replies within 48 hours.**
   You get a short voice message: one thing that's already working, and one simple thing to try first. No scores. No "talent" verdicts.

3. **Book a diagnostic lesson — only if you want to.**
   30 minutes with your coach. You get your **Starting Point**: your goal, what's already working, what we'll work on first, and an honest idea of the pace.

4. **Start your Starter Month.**
   Four 30-minute lessons. Between lessons, your lesson keeps working: your coach's demo, your take, and one clear task for the week.

---

### 1.3 What you get every week

**What you get every week**

- **One 30-minute lesson with a real voice coach.** Online, at a time that suits you.
- **Your lesson, saved.** A short recap: the moment your coach showed it, your take, and exactly what to practice this week. [UK: practise] No more leaving a lesson thinking "but how?"
- **One voice reply a week — already included.** Pick one home take and send it — no need to redo it many times. Your coach replies by voice within 48 hours. No "sorry to bother you" needed: it's part of your plan.
- **Before/Now you can hear.** In most lessons, we save a "before" and a "now" of the same phrase, in the same key — when there's an honest change to hear. From your third lesson, you can also compare across lessons. Changes you can hear — not a score. *Results vary from person to person.*
- **A practice plan that fits your life.** Short sessions. Tell us where you can practice and when, and your coach plans around it. [UK: practise]
- **A short note from your coach** under each clip — so you remember what to listen for.

*What you won't get: points, streaks, leaderboards, a "vocal score", or a verdict on your talent.*

> Если H1 откатится до «ответа раз в 2 недели», до продаж заменить "One voice reply a week" здесь, в §1.5, §2 п. 8, §3 и письме 5.4 — одновременно с VF-006 и VF-008 (план, раздел 0 №31).

---

### 1.4 Safe by design

**Safe by design**

We would rather be slow and safe than fast and sorry.

- **Private by default.** Your recordings are listened to by you and your coach — nobody else. (One member of our small team handles the files to cut your clips; they don't review your singing.) Nothing is shared or posted unless you choose to, every time.
- **Your coach hears it first.** You make your first home recording in your first lesson, with your coach, and you listen to it together. Most people find their recorded voice strange at first — that's normal, and we'll explain why.
- **Home practice stays inside what your coach allowed.** You only practice at home what your coach marked as safe to do on your own. Your plan never goes higher than your lesson. Short sessions — most are 10–15 minutes, and never more than 25 minutes of singing a day. Rest days are part of the plan. [UK: practise]
- **It stops the moment something hurts.** If your voice hurts, stop singing and tell your coach. You'll hear back the same day, and we'll tell you if it's time to see a doctor or a voice specialist. If it's severe or sudden, or you have trouble breathing, get medical help right away — don't wait for us. [CHECK: SLP-approved wording, VF-065 — не публиковать до одобрения SLP]
- **Feeling sick? Press pause.** Missing practice because you're ill is not "falling behind".
- **A person listens.** A real coach listens to your recording. No AI scores your voice. [CHECK: true only while no LLM step touches student content — plan №15]
- **Adults only, for now.** Our lessons and recordings are for people aged 18 and over.

*We're voice coaches, not doctors. Nothing here is medical advice.*

---

### 1.5 Honest pricing (landing block)

**Honest pricing. See it before you sing a note.**

| | What it is | Price |
|---|---|---|
| **Voice Snapshot** | Sing or hum for 60 seconds. A coach replies by voice within 48 hours. | **Free.** No card. |
| **Diagnostic lesson** | 30 minutes with a coach + your Starting Point. | **{$29}** one-time |
| **Starter Month** | 4 × 30-minute lessons, weekly practice plan, 1 voice reply a week, Before/Now. | **{$140}** one-time *(= {$35} per lesson)* |

- **Pay once. Nothing renews.** We will never charge you again unless you choose to buy again.
- **Not happy after your first month? Full refund.**
- No countdowns, no "only 3 spots left", no quiz before you see the price.

[ Get a free Voice Snapshot ]  [ Read our Honest Pricing Rules ]

> Для A/B цены (H4): ветка B — диагностика {$49}, Starter {$180} (= {$45} за урок). Обе цены [Д], утверждает владелец (раздел 9, п. 8).

---

### 1.6 FAQ — 12 questions

> Вопросы 1–8 дословно повторяют подсказки Google (US, собраны 2026-09-26, AUD) — делайте их H2 на странице. 9–12 — возражения из отзывов (AUD, SPR). В ответах нет цифр и обещаний сроков.

**1. Why can't I sing?**
Usually it's not "can't" — it's "haven't learned yet". Singing is a set of skills: hearing a note, finding it, and letting your voice do it without pushing. Most of those skills are learnable, and a coach can hear which one to start with. We never give talent verdicts. We tell you one thing that's already working and one thing to try first.

**2. Is it too late to learn how to sing?**
No. Adults start singing lessons at every age. Your voice today is the voice we work with — not the one you had at 18, and not someone else's. What changes with age is the plan, not whether you're allowed to start.

**3. Can anyone learn to sing?**
Most people can learn to sing better than they do today. How far and how fast depends on your starting point, how often you practice, and your goals — so we won't promise a timeline. [UK: practise] If matching pitch is hard for you right now, that's a starting point, not a verdict.

**4. Can voice lessons help a bad singer?**
"Bad singer" is usually a label someone gave you, not a diagnosis. Lessons help by breaking singing into small, practical steps and giving you feedback from someone who can hear what's going on. You'll hear it too: in most lessons we save a "before" and "now" of the same phrase, so you can compare for yourself.

**5. Are voice lessons worth it as an adult?**
That depends on what you want from singing — and you should be able to find out cheaply. That's why the Voice Snapshot is free and the Starter Month doesn't renew. If you're not happy after your first month, you get a full refund.

**6. Why can't I sing like I used to?**
Voices change over time, and a long break changes how easy things feel. A coach can help you find where your voice is comfortable now and rebuild from there. If you have pain, hoarseness that doesn't go away, or a sudden change in your voice, please see a doctor (an ENT) or a speech-language pathologist first. [UK: your GP, an ENT or a speech and language therapist] [CHECK: SLP-approved wording — не публиковать до одобрения SLP]

**7. How do I practice singing in an apartment?** [UK: How do I practise singing in a flat?]
Tell us where you can practice when you sign up — a room with a door, only quietly, only in the car, or nowhere right now. Your coach plans your week around it. Please don't "whisper-sing" to stay quiet: it can strain your voice. Humming and other quiet exercises your coach gives you are fine.

**8. I'm afraid to sing in front of others. Can I still take lessons?**
Yes. Many people who start lessons feel exactly this. Your recordings are private by default: only you and your coach hear them. Your first lesson is one-to-one, and you can start by just humming. You never have to perform for anyone unless you want to.

**9. Why not just use an app or YouTube?**
Apps and videos are great for routines. What they can't do is listen to *you* and explain what to change and how. As one app reviewer put it: "It gives you a score, but doesn't explain what's wrong." [CHECK: public app-store review, source [43] in audience-open-sources-report; re-verify the original before publishing and don't name the app] A coach can. We're not a score — we're a person who replies.

**10. Will I have to hear my own recordings? I hate how my voice sounds.**
Almost everyone is surprised by their recorded voice at first. You make your first home recording in your first lesson, and you listen to it together with your coach — never alone first. After that, you compare your takes only with your own earlier takes, never with anyone else.

**11. Is there a subscription? How do I cancel?**
No subscription. The Starter Month is paid once and doesn't renew — there's nothing to cancel. If you want to continue after your month, we'll show you the options and the price before you pay anything.

**12. What if I miss a week of practice?**
Life happens. Nobody will scold you, and there's no "streak" to lose. Before each lesson we'll simply ask what got in the way, so your coach can plan a week that actually fits.

> Возможные дополнительные вопросы (если нужно 13+): "How much should voice lessons cost?" → ссылка на Honest Pricing; "How long should I practice singing each day?" → «short sessions, never more than 25 minutes of singing a day; your coach sets it». Оба — реальные подсказки Google из того же сбора.

---

### 1.7 Footer rules

> Короткие правила для футера всех страниц. Отдельной строкой, мелко не прятать.

**Our rules**
- Prices are shown before you sign up. No card for the free Voice Snapshot.
- Nothing renews automatically. Ever. [CHECK: legal — state automatic renewal laws]
- Not happy after your first month? Full refund.
- No scores, no talent verdicts, no leaderboards.
- Private by default. Nothing you record is shared without your permission.
- A real coach listens. No AI scores your voice. [CHECK: plan №15]
- Adults 18+ only.
- We're voice coaches, not doctors. Nothing here is medical advice.

Links: Honest Pricing Rules · Privacy & recordings · Refunds · Contact · Terms

---

## 2. Honest Pricing Rules (site page, VF-007)

> Отдельная страница, ссылка из футера и блока цен. Каждое правило — обязательство. Не публикуйте правило, которое вы пока не выполняете.

**Our Honest Pricing Rules**

We've all been caught by a free trial that quietly became a subscription. We don't do that. Here's exactly how we charge.

1. **You see the price before you sign up.** All our prices are on this site. No quiz, no "book a call to find out".
2. **The Voice Snapshot is free, with no card.** We'll never ask for payment details to hear your 60 seconds.
3. **No fake urgency.** No countdown timers, no "offer ends in 10 minutes", no "only 2 spots left today". If our coaches are fully booked for the week, we'll tell you plainly and give you a date.
4. **We reply to every Voice Snapshot within 48 hours.** If we can't, we won't take your recording until we can.
5. **Pay once. Nothing renews by itself.** The diagnostic lesson and the Starter Month are one-time payments. We will not charge your card again unless you choose to buy again.
6. **Not happy after your first month? Full refund.** No need to prove anything. Just email us within {7} days after your last Starter lesson. [CHECK: legal; refund window is a test assumption — {7} оставить в скобках до ответа юриста]
7. **If we ever offer a plan that renews, cancelling will take one click** — and we'll email you {7} days before any renewal. [For later plans; nothing renews today]
8. **No add-ons you didn't ask for.** One voice reply a week is included in your plan. We won't charge you extra for asking your coach a question.
9. **Your recordings are yours.** Ask us, and we'll send you your recordings or delete them. [CHECK: VF-064, export/delete process]
10. **If a rule is broken, tell us.** Write to {contact email}. A person will reply.

---

## 3. Starter Month offer page (VF-008)

**Starter Month**
**Four lessons with a real coach. Pay once. Nothing renews.**

{$140} one-time *(= {$35} per 30-minute lesson)*
[ Book your Starter Month ]

*Not happy after your first month? Full refund.*

---

**What's included**

- **4 one-to-one lessons, 30 minutes each**, online, with the same coach. Usually one a week.
- **A weekly practice plan** made from your own lesson: your coach's demo, your take, and one clear task. [UK: practise]
- **1 voice reply a week.** [OWNER: если H1 откатится до «раз в 2 недели» — заменить до продаж, VF-008] Pick one home take and send it — no need to redo it many times; your coach replies by voice within 48 hours.
- **Before/Now in most lessons.** The same phrase, the same key — "before" and "now", whenever there's an honest change to hear. From lesson 3, you can compare across lessons too.
- **Safe home practice.** Only what your coach marked as safe to do alone, never higher than your lesson, never more than 25 minutes of singing a day.
- **Private by default.** Only you and your coach hear your recordings.

**What it's not**
- Not a subscription. Nothing renews. There is nothing to cancel.
- Not a promise of a specific result by a specific date. Voices are different, and plateaus are normal. We'll tell you honestly how things are going.
- Not a score. You won't get points, percentages, or a talent verdict.

**Who it's for**
- Adults (18+) who are starting from zero, coming back to singing, or stuck on their own.
- Pop, contemporary, worship and musical theatre singers. [UK: musical theatre; US: musical theater]
- People who'd like to practice at home but don't know what to practice. [UK: practise]

**Before you book**
Most people start with a free Voice Snapshot and a diagnostic lesson ({$29}), so you know your coach before you commit. You can also book the Starter Month directly. [OWNER: засчитывается ли диагностика в Starter — см. решения ниже]

**Refunds**
Not happy after your first month? Full refund. Email {contact email} within {7} days after your fourth lesson. You don't need to explain or prove anything. [CHECK: legal — {7} оставить в скобках до ответа юриста]

**If you miss a lesson**
Reschedule at least {24 hours} before your lesson and it moves, no charge. If you're sick, tell us — we'll move it. [OWNER: правило переноса не зафиксировано в плане, это заглушка]

**After your month**
Your coach will send you a short summary: what changed, what's next. If you want to continue, we'll show you the options and the price. If you don't, that's it — nothing renews.

[ Book your Starter Month ] [ Start with a free Voice Snapshot ]

---

## 4. Voice Snapshot (VF-009, VF-063, VF-064)

### 4.1 Snapshot page

> Страница = цены сверху → возрастной гейт → вопрос о здоровье → согласие → запись (v1.1: вопрос о здоровье — до записи, VF-009). Порядок важен: Snapshot только тем, кто видел цену и оставил контакт (R3), возраст — до записи (VF-063).

**Voice Snapshot**
**Sing or hum for 60 seconds. A real coach replies by voice.**

Free. No card. **We reply to every Snapshot within 48 hours.**

**What you'll get**
A short voice message (about a minute) from one of our coaches:
- one thing that's already working in your voice,
- where your voice sounded most comfortable in this take,
- one simple thing to try first.

**What you won't get**
- No score, no grade, no "talent" verdict.
- No voice-type label. That's something your coach can explore with you later, in a lesson — and even then it's a description, not a limit.

**Our prices, so there are no surprises later**
Voice Snapshot — free · Diagnostic lesson — {$29} · Starter Month (4 lessons) — {$140}, pays once, nothing renews.
[Honest Pricing Rules]

---

**Step 1 — About you**

- Your first name: `____`
- Your email: `____` (We'll send your coach's reply here.)
- Your time zone: `[dropdown]`
- **How old are you?** *(required, before any recording)*
  - ( ) Under 18
  - ( ) 18 or over

> Логика формы: «Under 18» → запись не показываем, данные не сохраняем, показываем текст ниже.

*If "Under 18" is selected:*
> Thank you for your interest! Right now our lessons and Voice Snapshots are for adults (18+) only, so we can't take your recording. Please don't send one. We haven't saved anything you entered.
> [Правка: поле «email родителя» убрано — на ветке «Under 18» не собираем никаких данных (VF-063). CHECK: legal — COPPA]

**Step 2 — What would you like from singing?** *(optional, one line)*
`e.g. "sing at my sister's wedding", "join a choir", "just for me"`

**Step 3 — Your recording**

> v1.1 (VF-009, VF-065): сначала вопрос о здоровье (тот же, что в §7, Q24). «Yes» → запись не показываем, показываем Refer-out. Запись делается без педагога и без распевки, поэтому инструкцию к записи одобряет SLP. Тексты с `[CHECK: SLP…]` не публиковать до одобрения SLP.

**Before you record: is your voice hurting or hoarse right now, or has it been for a while?** *(required)*
- ( ) No → continue
- ( ) Yes → *[recording hidden]* "Thanks for telling us. Please don't record or sing for now — see a doctor first. [UK: your GP] If it's severe or sudden, or you have trouble breathing, get medical help right away." [CHECK: SLP-approved Refer-out text — не публиковать до одобрения SLP]

Record up to 60 seconds on your phone. Choose one:
- ( ) **Sing** a bit of any song you like — no backing track needed.
- ( ) **Hum only** — hum any tune you know. That's completely fine.

Tips:
- Sing something comfortable — no high notes, no warm-up needed, stop if anything feels tight. [CHECK: SLP-approved recording instruction — не публиковать до одобрения SLP]
- If anything hurts, stop. Don't send a recording that hurt to make.
- Somewhere quiet-ish is fine. Perfect sound isn't needed.

`[ Record ]` or `[ Upload a file ]`

**Step 4 — Your permission** *(each box separate; none pre-ticked)*

- [ ] **I'm 18 or over.** *(required)*
- [ ] **I agree that Voice Family may store this recording so a coach can listen and reply.** We keep it for up to {90 days}, then delete it. Only the coach who replies will hear it (our head coach only if there's a voice-safety concern). *(required)* [CHECK: legal, VF-064]
- [ ] **You may use this recording to train our coaches** (never public, never shared outside Voice Family). *(optional — leaving this unticked changes nothing)*

We don't sell your data. A person listens to your recording; no AI scores your voice. [CHECK: plan №15] {We never use your recordings to train AI.} [CHECK: only if true for all vendors — VF-064]

[ Send my Snapshot ]

**If this week is full** *(показываем вместо кнопки, когда у педагога 5/5 Snapshot на неделе [Д])*
> Our coaches have replied to all the Snapshots they can this week. We don't want to keep you waiting, so we're not taking new recordings until **{date}**. Leave your email and we'll write to you that day — once, no spam. [ Tell me on {date} ]

---

### 4.2 Coach reply template (≤4 minutes total)

> Для педагогов. Внутренний текст, студент его не видит. У Snapshot отдельный лимит: ≤5 в неделю на педагога (≤20 мин), общий потолок ≤40 мин/нед [Д]; оплачивается поштучно (решение владельца, план §9, п. 5–6). Флаги — вне лимита. Хронометраж — в `teacher_seconds` каждый раз.

**Time budget (target median ≤4 min)**

| Step | Time |
|---|---|
| Listen once, all the way through (twice max) | ≤1.5 min |
| Pick the one "working" thing + the one "try first" from the SLP-approved list (no list → no "try first") | ≤0.5 min |
| Record the voice reply (60–90 seconds; one take, don't redo for polish) | ≤1.5 min |
| Send + log `teacher_seconds` | ≤0.5 min |

If you're over 6 minutes on one Snapshot, stop and send the short version. Tell the methodologist in the weekly notes.

**Structure of the voice reply (60–90 seconds)**

1. **Hello + thanks (≈5 s).** Use their name. Thank them for sending it — it takes courage.
2. **One thing that's already working (≈15–20 s).** Specific and true: something you actually heard. Not "great voice!" — say *what*.
3. **Where your voice sounded comfortable in this take (≈10–15 s).** Describe it in plain words ("the middle of that tune sat really easily"). **No note names, no range, no voice type, no Key Card.**
4. **One thing to try first (≈20–30 s).** One load-1 exercise with no high notes, from the **SLP-approved list** only [CHECK: SLP-approved list — не использовать до одобрения SLP]. **If there is no approved list yet, skip this step** — no exercise in the reply. Say how long (1–3 minutes), how loud (comfortable), and the stop rule ("if anything feels tight or hurts, stop").
5. **Next step, no pressure (≈10 s).** "If you'd like to keep going, a diagnostic lesson is the next step. The link is in the email. No rush."

**Never say** (VF-001, VF-043, VF-044)
- Talent or ear verdicts: "you're a natural", "you have no ear", "tone deaf", "you're not a singer", "you have a gift".
- Voice type or range: "you're a baritone", "your range is…".
- Scores or numbers: "7 out of 10", "80% on pitch".
- Timelines: "in 30 days you'll…".
- Urgency: "spots are filling up", "book today".
- Anything medical: diagnoses, "it's probably nodules".

**Red-flag rule (VF-030, VF-065)**
If the student mentions pain, hoarseness that won't go away, or losing their voice — or you hear something that worries you — **don't give an exercise**. Send the Refer-out Card text instead [CHECK: SLP-approved — не использовать до одобрения SLP]: say "See a doctor first" and **don't include the diagnostic-lesson link** (skip step 5). Tell the on-duty flag person the same day, and log it. This is outside your Snapshot time budget; never cut it short.

**Three example replies**

*Example 1 — beginner, "I was told I can't sing"* (they sang a verse of a pop song)
> "Hi Maria, thank you for sending this — I know that's a big step. Something that's already working: you kept a steady rhythm the whole way through, and your words were really clear. In this take, your voice sounded most comfortable in the lower, speaking part of the verse — it felt relaxed there. One thing to try first: {SLP-approved load-1 exercise, only if the list exists; otherwise skip this sentence — e.g. a gentle hum on one easy note, then sliding up and down a little, like a siren, only where it feels easy — about two minutes, quiet volume}. If anything feels tight, just stop. If you'd like to keep going, a diagnostic lesson is the next step — the link's in the email. No rush at all."

*Example 2 — returning adult, "I can't sing like I used to"* (they sang a chorus they used to sing)
> "Hi James, thanks for this. Something that's already working: you clearly still know how to shape a phrase — the way you ended each line was lovely. In this take, your voice sounded easiest in the middle of the chorus; the very top felt like more effort, which is really common after a break. One thing to try first: {SLP-approved load-1 exercise, only if the list exists; otherwise skip this sentence — e.g. lip bubbles on an easy slide, two minutes, gentle}. And please don't push for the old high notes yet — if you'd like, that's something to work on step by step in lessons. If you'd like, a diagnostic lesson is the next step. The link's in the email."

*Example 3 — very nervous, "Hum only"*
> "Hi Sam, thank you — humming counts, and it told me a lot. Something that's already working: your hum was steady and you stayed with the tune all the way to the end. It sounded most comfortable around the middle of the melody, nice and relaxed. One thing to try first: {SLP-approved load-1 exercise, only if the list exists; otherwise skip this sentence — e.g. hum the same tune again, even softer, and notice where it feels easiest — about one minute}. That's it. No one else hears these. If you'd like to go further, a diagnostic lesson is the next step — whenever you're ready."

> Все упражнения в фигурных скобках — заглушки. В реальный ответ идёт только упражнение нагрузки 1 без верха из списка, одобренного SLP (VF-009, v1.1). Если списка нет, шаг 4 пропускаем и упражнения в ответе нет. Пример 2 не должен вести к верху: только лёгкое упражнение в удобной зоне.

---

## 5. Emails

> Отправитель — реальный человек (имя педагога или «{Name} from Voice Family»). Без таймеров и «last chance». Каждое письмо — максимум одно действие. Письма 5 и 6 уходят один раз, повторов нет.

### 5.1 Snapshot received (instant)

**Subject:** We've got your Voice Snapshot
**Preview:** A coach will reply by voice within 48 hours.

> Hi {first_name},
>
> Thank you for sending your Voice Snapshot. That takes courage — especially if you haven't sung for anyone in a while.
>
> **What happens next:** one of our coaches, {coach_name}, will listen and reply with a short voice message by **{date/time, 48h}**. You'll get one thing that's already working and one simple thing to try first. No scores, no verdicts.
>
> Your recording is private: only your coach hears it. We keep it for up to {90 days} and then delete it. Want it deleted sooner? Just reply to this email.
>
> Talk soon,
> {sender_name}, Voice Family
>
> *Our prices, so there are no surprises: diagnostic lesson {$29}; Starter Month {$140}, pays once, nothing renews.*

### 5.2 Your coach has replied

**Subject:** {coach_name} listened to your Snapshot
**Preview:** A one-minute voice reply is waiting for you.

> Hi {first_name},
>
> {coach_name} has listened to your Voice Snapshot and recorded a reply for you. It's about a minute long.
>
> [ ▶ Listen to your reply ]
>
> A tip: listen somewhere you can try the exercise straight away. Keep it gentle — if anything feels tight or hurts, stop.
>
> If you have a question about the reply, just hit reply. A person reads every email.
>
> {sender_name}, Voice Family

### 5.3 Invitation to a diagnostic lesson (2 days after 5.2)

**Subject:** Want to go one step further with {coach_name}?
**Preview:** A 30-minute lesson and your Starting Point. Only if you want it.

> Hi {first_name},
>
> Did you get a chance to try {coach_name}'s exercise? However it went, that's useful information.
>
> If you'd like to keep going, the next step is a **diagnostic lesson**: 30 minutes, one-to-one, online.
>
> **What you get:**
> - a relaxed lesson — we start with easy things, and humming is fine;
> - your **Starting Point**: your goal, what's already working, the first two things we'll work on, and an honest idea of the pace;
> - a song-key note for a song you'd like to sing, if your coach can prepare it. [OWNER: Song Key Card — VF-031, в неделях 0–2 только вручную или не выдаём]
>
> **Price:** {$29}, paid once. Nothing renews.
>
> [ Choose a time ]
>
> Not ready? That's completely fine. You don't need to reply, and we won't keep chasing you.
>
> {sender_name}, Voice Family

### 5.4 After the diagnostic — your Starting Point (within 24h of the lesson)

**Subject:** Your Starting Point
**Preview:** Where you are today, and what we'll work on first.

> Hi {first_name},
>
> Thank you for today's lesson. Here's your **Starting Point** — a snapshot of where your voice is today, so later you can compare and hear what's changed.
>
> **Your goal:** {goal, in the student's words}
>
> **What's already working:**
> - {one specific thing}
> - {one specific thing}
>
> **What we'll work on first:**
> 1. {theme 1, plain words}
> 2. {theme 2, plain words}
>
> **Your "before" recording:** [ ▶ Listen ] — this is today's phrase. We'll record the same phrase, in the same key, later on, so you can compare. It's private: only you and {coach_name} can hear it.
>
> **An honest word about pace:** everyone's voice is different, so we won't promise a date. Progress in singing usually comes in steps, with flat bits in between — plateaus are normal, not a sign you're doing it wrong. {coach_name} will tell you honestly how it's going.
>
> **Practice for now:** {one safe task, only if marked safe for home; otherwise "Nothing to practice yet — just listen back to today's clip once."} [UK: practise]
>
> **If you'd like to continue:** the Starter Month is 4 × 30-minute lessons, a weekly practice plan and one voice reply a week [OWNER: если H1 откатится — заменить до продаж, VF-008], for {$140}, paid once. Nothing renews. Not happy after the month? Full refund.
>
> [ Book your Starter Month ]
>
> {coach_name} and {sender_name}, Voice Family

### 5.5 Gentle reminder (7 days after 5.3 or 5.4, only if no booking; sent once)

**Subject:** No pressure — just leaving this here
**Preview:** Your reply and Starting Point stay available.

> Hi {first_name},
>
> Just a short note, and then we'll leave you be.
>
> Your {coach's reply / Starting Point} is still here whenever you want it: [ ▶ Listen again ]
>
> If you'd like to continue, you can book any time: [ See times ]. If now isn't the right moment, that's okay — singing will still be there when you are.
>
> We won't send another reminder. If you'd like us to delete your recording now, just reply "delete".
>
> {sender_name}, Voice Family

### 5.6 (Bonus) Starter Month — last lesson done, nothing renews

**Subject:** Your Starter Month is complete
**Preview:** Here's what changed — and nothing will renew.

> Hi {first_name},
>
> That's your four lessons done. Well done for showing up.
>
> **Before/Now:** [ ▶ Lesson 1 ] [ ▶ Lesson 4 ] — same phrase, same key. {one sentence from coach about what changed, or "Let's talk about it in your next lesson" if nothing is clearly audible yet}
>
> **Your month was a one-time payment. Nothing renews,** and we won't charge you again.
>
> If you'd like to continue, here are your options and prices: [ See options ]. [OWNER: оффер продолжения не определён планом]
>
> Not happy with your month? Reply within {7} days and we'll refund you in full. No questions.
>
> [CHECK: legal — окно {7} оставить в скобках до ответа юриста, VF-008]
>
> {coach_name} and {sender_name}, Voice Family

---

## 6. No-Blame Pre-Lesson Check-in (VF-045, VF-030)

> Форма или сообщение за {24 ч} до урока. 3 вопроса, ≤1 минуты. Ответ видит только педагог. Вопрос 2 — самоотчёт «practice days» для WCP (R7). Он показывает, сколько студент занимался, а не «прогресс голоса» (VF-044). «Sore/hurts» — флаг здоровья: ответ педагога в тот же день, вне бюджета.

**Before your lesson — 3 quick questions**
*Takes under a minute. Only your coach sees this. There are no wrong answers.*

**1. How's your voice today?**
- ( ) Feels fine
- ( ) A bit tired
- ( ) Hoarse, sore or it hurts
- ( ) I'm sick

*If you choose "Hoarse, sore or it hurts":* Please don't sing until you hear from your coach — they'll get back to you today. If it's severe or sudden, or you have trouble breathing, get medical help right away. [CHECK: SLP-approved wording — не публиковать до одобрения SLP]
*If you choose "I'm sick":* Rest first. Want to move your lesson? [ Move my lesson ] — no charge, no problem.

**2. On how many days did you get to practice this week?** [UK: practise]
- ( ) 0 ( ) 1 ( ) 2 ( ) 3 ( ) 4 ( ) 5+

*Life happens — tell me what got in the way.* (optional)
`____`

*Hint (under the field):* "No time", "nowhere quiet", "didn't know what to do", "felt awkward" — all useful. Your coach will plan around it.

**3. What would you like from today's lesson?** (optional)
`e.g. "the high bit of the chorus", "I felt stuck on the exercise", "just a calm lesson"`

[ Send to my coach ]

*Thanks! See you at {lesson time}.*

---

## 7. First Week Setup — form (VF-047, VF-063, VF-064, VF-054)

> Tally/Typeform, ≈5 минут. Порядок важен: возраст — первым, до любой записи и любых данных о голосе. Ответы на «Where can you practice?» — решение по Quiet Plan (порог ≥30% «quiet/none», H8). Страна — чтобы понять, где живут студенты (раздел 9, п. 2). Медицинских данных не собираем (VF-066).

**Welcome to Voice Family**
*A few questions so your coach can plan your first weeks. About 5 minutes. Mistakes welcome — here and in lessons.*

**Section 1 — First, your age** *(required)*

1. **How old are you?**
   - ( ) Under 18 → *[form ends]* "Thank you! Right now our lessons are for adults (18+) only. We haven't saved your answers." [CHECK: legal]
   - ( ) 18 or over → continue

**Section 2 — The basics**

2. First name `____`
3. Email `____`
4. **Your time zone** `[dropdown, e.g. America/New_York, Europe/London]`
5. Country you live in `[dropdown]`
6. When are you usually free for a 30-minute lesson? *(tick all that apply)*
   - [ ] Weekday mornings [ ] Weekday lunchtime [ ] Weekday evenings [ ] Weekends

**Section 3 — Why you sing** *(from S4, S5: singing for someone helps)*

7. **What would you like singing to do for you?** *(tick all that apply)*
   - [ ] Just for me — I want to enjoy it
   - [ ] Sing for someone (a wedding, a birthday, my family)
   - [ ] Join or do better in a choir or worship team
   - [ ] Audition or perform (musical theatre, a band, open mic) [UK: musical theatre; US: musical theater]
   - [ ] Speak or present with a more confident voice
   - [ ] Get back to singing after a break
   - [ ] Something else: `____`
8. **Is there someone you'd like to sing for one day?** (optional) `____`
9. **A song you'd love to be able to sing** (optional) `____`
10. **What kind of music do you like singing?** *(tick all that apply)*
    - [ ] Pop [ ] Rock [ ] R&B / soul [ ] Musical theatre [ ] Worship / gospel [ ] Folk / country [ ] Jazz [ ] Not sure yet

**Section 4 — Where you're starting from** *(no test, no score; S5 blocks: sound, hearing, feelings)*

11. **Which sounds most like you right now?**
    - ( ) I've never really sung, apart from in the car or shower
    - ( ) I sang as a kid or teen and stopped
    - ( ) I sing now and then, on my own
    - ( ) I sing regularly (choir, band, church, shows)

    > v1.1 (VF-047): возвращающимся (Q11 «I sang as a kid or teen and stopped» или Q7 «Get back to singing after a break») и студентам 40+ показывать текст ниже. Поля возраста 40+ в форме нет — как определять 40+, решает владелец. [CHECK: SLP-approved wording — не публиковать до одобрения SLP]

    *Voices change over time, and a long break changes how easy things feel. A coach can help you find where your voice is comfortable now and rebuild from there. If you have pain, hoarseness that doesn't go away, or a sudden change in your voice, please see a doctor (an ENT) or a speech-language pathologist first.* [UK: your GP, an ENT or a speech and language therapist]
12. **Have you had singing lessons before?** ( ) No ( ) Yes, a few ( ) Yes, for a while
13. **When you try to sing a note you hear, how does it usually go?** *(there's no right answer)*
    - ( ) Usually I find it
    - ( ) Sometimes
    - ( ) I often can't tell if I've got it
    - ( ) Not sure
14. **How do you feel about singing right now?** *(tick all that apply)*
    - [ ] Excited [ ] Nervous [ ] Embarrassed [ ] I was told I can't sing [ ] Worried I'll hurt my voice [ ] Relaxed [ ] Not sure
15. **Anything your coach should know about how you like to learn?** (optional) `e.g. "I freeze if I'm put on the spot"`

**Section 5 — Where and when you can practice** [UK: practise]

16. **Where can you practice?** *(required)*
    - ( ) A room where I can sing at normal volume
    - ( ) Only quietly (thin walls, family at home, neighbors) [UK: neighbours]
    - ( ) Only in the car
    - ( ) Nowhere right now
17. **When could you practice most weeks?** *(tick all that apply)*
    - [ ] Mornings [ ] Lunch break [ ] Evenings [ ] Weekends [ ] It changes every week
18. **How many minutes could you realistically give it on a practice day?**
    - ( ) 5–10 ( ) 10–15 ( ) 15–20 ( ) Not sure yet
    *Your coach keeps it short. We never plan more than 25 minutes of singing in a day.*

**Section 6 — Your device**

19. **What will you use for lessons and practice?** *(tick all that apply)*
    - [ ] iPhone [ ] Android phone [ ] Laptop / computer [ ] Tablet
20. **Do you have headphones?** ( ) Yes, wired ( ) Yes, wireless ( ) No
    *Tip: for lessons, wired headphones usually work best. Not required.*
21. **Can you record a voice memo on your phone?** ( ) Yes ( ) Not sure — please show me

**Section 7 — Recordings and privacy** *(each box separate, none pre-ticked; VF-064, VF-054)*

Your recordings are **private by default**: only you and your coach hear them. You make your first home recording in your first lesson, and you'll listen to it together with your coach.

*One team member handles the files to cut your clips, but doesn't review your singing.*

> Галочки ниже — сокращённая версия формы 05-legal-drafts §1.1 (те же 3 обязательные + 2 необязательные). После проверки юристом ставим полный текст из 05.

22. **What we need to run your lessons** *(required to take part in the pilot)*
    - [ ] **Record my lessons** so I get my recap, clips and Before/Now.
    - [ ] **Store the recordings I make at home** so my coach can reply.
    - [ ] **Let my coach hear my recordings** — my own coach listens, adds notes and picks clips for me.
23. **Optional — saying no changes nothing about your lessons**
    - [ ] **Our head coach may listen for quality checks** (to check that feedback is safe and helpful).
    - [ ] **Use my recordings to improve Voice Family** — for example, to train our coaches. Never public. *(off by default)*

    Publishing your voice, face or name anywhere always needs a separate form — never this one.

    Raw recordings are deleted after {90 days}. Your before/now clips stay while you're a student and for {12 months} after, unless you ask us to delete them sooner. [CHECK: legal — consent, retention, state recording laws]

**Section 8 — Your voice today** *(no medical details, please)*

> v1.1 (VF-047): форма должна быть заполнена и вопрос 24 получен **до урока 1**. Ответ «Yes» → флаг дежурному до урока (ответ в тот же день).

24. **Is your voice hurting or hoarse right now, or has it been for a while?**
    - ( ) No
    - ( ) Yes → "Thanks for telling us. Please don't sing until your coach contacts you — they'll reply the same day. If it's severe or sudden, or you have trouble breathing, get medical help right away. Please don't write medical details here." [flag → same-day coach reply; CHECK: SLP-approved Refer-out text — не публиковать до одобрения SLP]

**Last thing**

25. **Anything else you'd like your coach to know?** (optional) `____`

[ Send ]

*Thank you, {first_name}! Your coach {coach_name} will read this before your first lesson. Remember: mistakes welcome.*

---

## 8. UK wording table

> UK-версия — после интервью и DPA (план v1.1, раздел 9, п. 13). Сейчас только замены слов; цены для студентов в £ план не задаёт (есть только £24 для Founding Coach), поэтому в UK-версии их не ставим до решения владельца.

| US (default) | UK | Where |
|---|---|---|
| practice (verb) | **practise** (verb); *practice* stays as a noun ("your practice plan") | everywhere |
| student | student (adults); **pupil** only if targeting school-age — not in this pilot | — |
| semester / season | **term** | later plans, Starting Point ("this term") |
| musical theater | **musical theatre** | Starter, forms |
| neighbors | **neighbours** | FAQ 7, form Q16 |
| apartment | **flat** | FAQ 7 |
| cell phone | **mobile** | device questions, if used |
| ENT / doctor | **GP**, ENT | FAQ 6, Refer-out |
| speech-language pathologist (SLP) | **speech and language therapist (SLT)** | FAQ 6, Refer-out |
| enroll | **enrol** | if used |
| check (payment) | **cheque** | if used |
| $ | £ — prices not set for UK | pricing |

---

## 9. Copy QA checklist (before publishing anything)

- [ ] No scores, percentages, points, streaks, leaderboards or voice numbers anywhere (VF-043, VF-044, VF-091).
- [ ] No talent/ear verdicts, no voice type, no range or Key Card in Snapshot (VF-001, VF-009).
- [ ] No timers, "spots left", countdowns or quizzes before price (VF-007).
- [ ] Every price is the approved test price and matches Stripe exactly; "nothing renews" is true in Stripe settings.
- [ ] Refund line reads exactly: "Not happy after your first month? Full refund." — no conditions about "hearing progress".
- [ ] No testimonials, statistics or "students improve X%" claims (FTC; no data yet).
- [ ] "A person listens / No AI scores your voice" is still true (№15). "Never used to train AI" removed unless verified.
- [ ] Age question comes before any recording on every form (VF-063).
- [ ] Consent boxes are separate and not pre-ticked (VF-064).
- [ ] Safety and Refer-out wording signed off by SLP (VF-065).
- [ ] No "best take" anywhere — only "your take" / "one home take" (VF-011).
- [ ] Snapshot reply and page: no note names and no range (VF-009).
- [ ] No unapproved [SLP] / [CHECK: SLP…] marks left in anything published (VF-065).
- [ ] Before/Now: no cross-lesson pairs promised before lesson 3.
- [ ] HOME is not in the hero.
