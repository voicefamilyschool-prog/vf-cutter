# DRAFT — for review by a lawyer, not legal advice

**Voice Family — pilot legal drafts v0.1 (2026-09-26)**
Covers: consent to record (VF-064, VF-063), data retention & deletion (VF-064), Honest Pricing / refunds / no auto-renewal (VF-007, VF-008), teacher agreement checklist (VF-089, VF-058), AI Gate data rules (VF-025), questions for the lawyer.

---

## Для владельца (коротко, по-русски)

- Синхронизировано с планом v1.1 (2026-09-26).
- **Это черновики, а не юридические документы.** Ни один текст отсюда нельзя публиковать и давать на подпись, пока его не посмотрел юрист (US + UK). Каждый спорный момент помечен `[CHECK: legal]`, решения владельца — `[OWNER]`.
- **Ворота «Стоп» из плана §5.1 остаются:** нет подписанного согласия (раздел 1) — нет записи. LLM-шаг в n8n включён без DPA — нет записи. Пилот только 18+.
- **Все сроки и цены в фигурных скобках `{…}` — допущения [Д]** из плана (§4.3, VF-064): сырые записи {90 days}, пары Before/Now и якоря — пока студент учится + {12 months}, возврат — {7} дней после 4-го урока. Цены тестовые: Snapshot $0, диагностика {$29}/{$49}, Starter Month {$140}/{$180}, Founding Coach {$29/month} (первая волна FC — US и CA; UK {£24} — только после DPA и решения по стране, план v1.1, раздел 0 №23). Они совпадают с `02-student-copy.md`; меняйте в обоих местах.
- **Фраза «We never use your recordings to train AI»** стоит в фигурных скобках: её можно оставить, только если это правда для **всех** подрядчиков (транскрипция, LLM, хостинг) и подтверждено их DPA. Иначе — удалить.
- **Согласия в `02-student-copy.md` (Snapshot, раздел 7 анкеты) нужно заменить на форму из раздела 1 ниже** после проверки юристом: здесь галочки разделены точнее (доступ педагога, улучшение сервиса по умолчанию выкл., публикация — только отдельной формой).
- **Неконкуренцию в договор педагога не включаем** (решение плана). Раздел 4 — чек-лист для юриста, а не текст договора.
- Раздел 5 — 12 вопросов юристу; у каждого указан VF-ID, который он блокирует. Минимум до первой записи: вопросы 1, 2, 5, 6, 7.

---

## 1. Student consent: lesson and home recordings (US English)

> Shown before the first recorded lesson and before any home recording. Each box is separate, **none is pre-ticked**, and the form cannot be submitted until the required boxes are answered. We store: the form version, each box's value, the date/time, and the student's email. `[CHECK: legal — is click-to-agree enough, or is an e-signature needed? See Q2]`

### 1.1 Form text

**Your recordings, your choice**

Voice Family lessons work because your coach can hear you — in the lesson and between lessons. To do that, we need to record and store your voice. Here is exactly what we do, and what you can say yes or no to.

**First: your age**

- [ ] **I confirm I am 18 or older.** *(required — Voice Family pilots are for adults only)*

> If this box is not ticked: *"Thanks for your interest. Right now Voice Family is only open to adults (18+). We haven't stored anything you've entered."* — and we delete the form data. `[CHECK: legal — Q6]`

**What we need to run your lessons** *(required to take part in the pilot)*

- [ ] **Record my lessons.** Your lesson with your coach is recorded (audio and, if you're on video, video) so we can send you your recap, short clips and your Before/Now pair. Your coach also agrees to be recorded. `[CHECK: legal — all-party consent, Q1]`
- [ ] **Store the recordings I make at home.** When you record your practice and send it to us, we keep it so your coach can listen and reply.
- [ ] **Let my coach hear my recordings.** Your own coach (the one who teaches you) can listen to your lesson and home recordings, add notes, and pick clips for you. One named member of our operations team handles the files (cutting clips, fixing technical problems) but doesn't review your singing. `[CHECK: legal — disclose ops access]`

> `[OWNER]` If a student does not want lessons recorded: *"That's fine — you can still take lessons with us. You just won't get recaps, clips or Before/Now."* (Outside the pilot.) Recommendation: offer this; recording should not be a condition of being taught.

**Optional — each one is a separate choice, and saying no changes nothing about your lessons**

- [ ] **Our head coach may listen for quality checks.** Our head coach sometimes listens to lessons to check that feedback is safe and helpful. They never contact you about it unless there's a voice-health concern. *(optional)* `[OWNER: name the role; if unticked, quality checks skip this student]`
- [ ] **Use my recordings to improve Voice Family.** For example, to train our coaches, or to test that our clip-cutting works. Never public. Never shared outside Voice Family and the service providers listed below. *(optional, off by default)*

**Never without a separate form**

- **Publishing.** We will never post, show or share your voice, face or name publicly (website, social media, ads, showcases) based on this form. If we ever want to, we will ask you with a separate form that names the exact clip, where it will appear and for how long — and you can say no. See 1.3.

**What we don't do**

- **No voiceprints.** We don't create voiceprints or any other biometric identifier from your voice, and we don't use your voice to identify you. `[CHECK: legal — confirm with all vendors, incl. speaker separation in transcription; Q5]`
- **No scores about your voice.** A person — your coach — listens and replies. `[CHECK: plan №15 / VF-025 — only true once captions are teacher-written or teacher-approved]`
- **We don't sell your data**, and we don't share it for advertising. `[CHECK: legal — CCPA "sell/share" wording, Q3]`
- {**We never use your recordings to train AI.**} `[CHECK: only if true for every vendor below, with signed DPAs — VF-064, VF-025]`

**Who else handles your data (service providers)**

We use a small number of companies to run Voice Family. They may process your data only to provide their service to us, under a written agreement. `[CHECK: developer + lawyer fill this list; every row needs a DPA before the first recording]`

| Service | What it does for us | Where data is stored | Agreement signed |
|---|---|---|---|
| {Supabase} | Database and file storage | {US / EU-UK region} | {yes / pending} |
| {n8n — self-hosted or cloud?} | Runs our lesson-processing workflow | {…} | {…} |
| {Transcription provider} | Turns lesson audio into text so your coach can find moments | {…} | {…} |
| {LLM provider} — **off until a DPA is signed** | Rephrases your coach's notes; your coach approves every word | {…} | {…} |
| {Video call tool} | Online lessons | {…} | {…} |
| {Email provider} | Sends your recaps and replies | {…} | {…} |
| {Stripe} | Payments (we never see your full card number) | {…} | {…} |
| {Scheduling tool — MMS / Calendly} | Booking lessons | {…} | {…} |
| {Form tool — Tally} | Sign-up and Snapshot forms | {…} | {…} |

**How long we keep things** — see our Data Retention policy (section 2). In short: raw recordings are deleted after {90 days}; your Before/Now clips stay while you're a student and for {12 months} after, unless you ask us to delete them sooner.

**Changing your mind**

You can withdraw any of these choices at any time: email {privacy email} or reply to any email from your coach with "stop recording" or "delete". We'll confirm within {2 business days} and act within {30 days}. Withdrawing doesn't affect what we did before you withdrew, and it never affects your refund.

**Other people in the room**

When you record at home, please record only yourself. If someone else can be heard (a family member, an accompanist), make sure they're OK with it — or record somewhere else. `[CHECK: legal — Q1]`

**If your voice hurts**

If you tell us your voice hurts or is hoarse, we keep a short note of that so your coach can respond the same day and adjust your practice. Please don't send us medical details or documents. `[CHECK: legal — health-related data, Q4]`

[ Save my choices ]

*Form version {v0.1} · {date}. We'll email you a copy of your choices.*

### 1.2 UK wording (differences only)

| US | UK |
|---|---|
| practice (noun and verb) | practice (noun), **practise** (verb): "the recordings you make when you practise" |
| coach | coach / **singing teacher** |
| student | student (adults); avoid "pupil" for adults |
| "We don't sell your data" | "We don't sell your data or use it for advertising." + lawful basis line: "We use your recordings on the basis of your consent `[CHECK: legal — consent vs contract, Q11]`." |
| {privacy email} | + "You can also complain to the Information Commissioner's Office (ICO)." `[CHECK: legal, Q11]` |

### 1.3 Separate form: permission to publish one clip (use only after month 4, VF-053)

> Never bundled with 1.1. Never offered in the first month. Never a condition of a discount, refund or lesson. One form per use.

**May we share this clip?**

- Clip: {file name / 10-second preview}
- Where it would appear: {e.g., voicefamily.com "Student stories" page}
- For how long: {12 months}, then we remove it
- Shown with: ( ) no name  ( ) first name only  ( ) full name — *you choose*
- Paid? {No / $…} — if paid or given anything in return, we'll label it as such. `[CHECK: legal — FTC endorsements, Q9]`

- [ ] **Yes, you may publish this clip as described above.** *(optional)*

You can change your mind at any time: we'll take it down from our website and social accounts within {7 days}. We can't recall copies other people have already saved or shared. Results vary — we'll never present your clip as a typical result without saying so. `[CHECK: legal, Q9]`

---

## 2. Data retention and deletion policy (draft, public-facing + internal table)

### 2.1 Public text (US)

**How long we keep your data**

We keep your data only as long as we need it to teach you, then delete it.

- **Raw recordings** (full lesson recordings and home recordings): deleted **{90 days}** after they're made.
- **Clips and Before/Now pairs** your coach picked for you: kept while you're a Voice Family student and for **{12 months}** after your last lesson, so you can come back to them. Then deleted.
- **Lesson recaps and your coach's notes and replies:** same as clips.
- **Your consent choices:** kept for as long as we hold any of your recordings, plus {3 years}, so we can show what you agreed to. `[CHECK: legal]`
- **Payment records:** kept as long as tax law requires ({7 years} `[CHECK: legal]`). They don't include recordings.
- **Backups** are overwritten within {30 days}, so a deleted file may stay in a backup for up to {30 days}, where no one uses it.

**Delete anything, any time.** Email {privacy email} or reply "delete" to any of our emails. Tell us what to delete — one recording, all recordings, or your whole account. We'll confirm within {2 business days} and delete within {30 days}. `[CHECK: legal — CCPA 45 days / UK GDPR one month; pick the shorter]`

**Take your data with you.** Ask for an export at any time and we'll send, within {30 days}, a download link with:
- your recordings and clips (original audio/video files);
- your recaps, coach notes and replies (as text / PDF);
- a simple list of your lessons and assignments (CSV).

If Voice Family ever closes, we'll give you at least {60 days}' notice and a way to download everything first.

### 2.2 Internal retention table (for developer and ops)

| Data | Where | Retention [Д] | Deleted how | Owner of the job |
|---|---|---|---|---|
| Raw lesson recording | {Supabase bucket / Drive} | {90 days} from lesson date | Scheduled job, daily | Developer |
| Raw home recording | {…} | {90 days} from upload | Scheduled job, daily | Developer |
| Snapshot recording (no purchase) | {Tally / storage} | {90 days}; or {30 days} if no booking `[OWNER]` | Scheduled job | Developer |
| Clips, Before/Now pairs, passport anchors | {…} | Active + {12 months} after last lesson | Monthly job | Developer |
| Transcripts | {…} | Same as raw recording ({90 days}) | Scheduled job | Developer |
| Captions + `caption_source` + AI Gate decision (✓/✎/✗) | {…} | Same as clips | Monthly job | Developer |
| Health flag note ("hurts / hoarse", no medical details) | `pilot-flags.csv` | {90 days}, then keep only date + outcome, no free text `[CHECK: legal, Q4]` | Ops, monthly | Ops |
| Consent records | {…} | Longest data retention + {3 years} | Manual | Owner |
| `teacher_seconds` time log | `pilot-teacher-time.csv` | {24 months} (pay records) `[CHECK: legal]` | Manual | Ops |
| Age = under 18 answer | — | Not stored; form data discarded | Form logic | Developer |

**Rules**
- Data in another region is not copied: US students → {US region}, UK/EU → {EU/UK region} `[CHECK: legal, Q11]`.
- Teachers never download student recordings to personal devices; they listen in {the shared workspace}.
- Deletion request log: date received, what, date done, who did it. Target: 0 files older than the retention date [Д] (supports the plan §4.4 privacy guardrail).
- Any file for a student whose box for that use is unticked → deleted immediately, logged as `flag_type = privacy` (runbook).

---

## 3. Honest Pricing, refunds, no auto-renewal (terms draft, US)

> Short enough to read. Linked from every price. Must match Stripe settings exactly. `[CHECK: legal — Q8, Q9; UK version needs Q12]`

**Honest Pricing — our rules**

1. **Prices are on the page before you sign up.** No "book a call to see pricing."
2. **No countdown timers, no "only 3 spots left", no "price valid for 30 minutes".** If a week is full, we say so and tell you when we'll have room.
3. **The Voice Snapshot is free, with no card.** We reply to every Snapshot within 48 hours. `[OWNER: only if the ≤5/week cap per coach is enforced — plan v1.1]`
4. **No hidden fees.** The price you see is the price you pay{, plus sales tax / VAT where it applies}.
5. **Pay once. Nothing renews.** The diagnostic lesson ({$29}) and the Starter Month ({$140}, 4 × 30-minute lessons) are one-time payments. We will not charge your card again unless you choose to buy again.
6. **Not happy after your first month? Full refund.** Email {contact email} within {7 days} after your fourth Starter Month lesson. You don't need to give a reason or prove anything. We refund to your original payment method within {5 business days}.
7. **Diagnostic lesson:** if it doesn't happen because of us, full refund. If you're not happy with it, tell us within {7 days} and we'll refund it. `[OWNER — plan doesn't set this; recommended]`
8. **Missed or moved lessons:** move a lesson for free with {24 hours}' notice. **If your voice is sick, move it anytime, even the same day** — resting your voice is the right call. `[OWNER]`
9. **If we ever offer a plan that renews** (for example, a monthly plan after the Starter Month), we'll show the price and renewal date before you pay, ask you to tick a separate box to agree, email you {7 days} before every renewal, and let you cancel in one click from that email. `[CHECK: legal — state auto-renewal laws, FTC negative option, Q8]`
10. **We don't promise results.** Everyone's voice is different. We promise a real coach, a weekly reply, and honesty about what we hear.

**Founding Coach terms (teachers, monthly)** — the only product that renews:

- **6 weeks free, no card.** When the 6 weeks end, **we don't charge you automatically.** We email you: "Your free weeks end on {date}. Want to continue for {$29}/month?" You choose.
- If you continue: {$29}/month, billed monthly, **price locked for 12 months**, no percentage of your income, no annual prepayment.
- Cancel any time in one click; you keep access until the end of the month you paid for. Reminder email {7 days} before each renewal. `[CHECK: legal, Q8]`
- **Your data leaves with you:** export your clips, notes and student list at any time, including after you cancel (for {90 days}).

**UK differences** `[CHECK: legal — Q12]`: prices shown including VAT if registered; "cancel" rights for online purchases (14-day cancellation period and what happens if a lesson is delivered inside it) must be written in by the lawyer; wording "practise".

**Owner check before launch**
- [ ] Stripe: products set to **one-time**, not subscription (Starter, diagnostic).
- [ ] Founding Coach: no card collected at trial start; no automatic conversion.
- [ ] Refund flow tested end-to-end once.
- [ ] Refund reserve {20%} of Starter revenue set aside (plan §4.3).
- [ ] No timers/scarcity widgets in the landing builder template.

---

## 4. Teacher agreement — checklist for the lawyer (VF-089, VF-058, VF-030, VF-025)

> For VF teachers in the pilot (2–3 people). Not a contract text — the list of things the contract must cover. External Founding Coaches are **customers**, not VF teachers: they need a customer agreement + DPA (4.9).

**4.1 Status and scope**
- [ ] Employee vs independent contractor — per state/country of each teacher `[CHECK: legal — AB5 / ABC test, UK employment status, Q10]`.
- [ ] Scope: live lessons + asynchronous work (listening to home recordings, voice replies, approving captions ✓/✎/✗, Home Assignment Checklist, Voice Snapshots, same-day health-flag replies, filming days).

**4.2 Pay — no unpaid work (backlog VF-089: «работа педагога не бывает бесплатной»)**
- [ ] Live lesson rate: {…}.
- [ ] **Asynchronous work paid:** {hourly rate}, based on `teacher_seconds` log (teacher sees and can correct their own log). Budget ≤20 min/week per 5 students; **minutes over 20 are paid, not absorbed** `[OWNER: rate]`.
- [ ] **Voice Snapshot:** paid per Snapshot {$…}, outside the 20-minute budget.
- [ ] **Health-flag replies:** paid, outside the budget, never cut to save time.
- [ ] **Filming days / showcase / Demo Vault recording:** day or hourly rate {…} + any reuse fee `[OWNER]`.
- [ ] Payment terms: {net 14}, monthly statement.
- [ ] Time log is for pay and workload only — **not** used for performance ranking without the teacher's written consent (VF-080).

**4.3 IP assignment**
- [ ] Teacher assigns to VF the rights in materials **created for VF**: fix recipes, exercise cards, warm-up recordings, demo clips, videos, captions and written feedback templates.
- [ ] Assignment, not "work for hire" wording only `[CHECK: legal — Q10/Q11]`; UK: waiver of moral rights or agreed credit.
- [ ] **Carve-out:** teacher's pre-existing methods, exercises and materials stay theirs (attach a short list); VF gets a licence only if listed.
- [ ] Teacher keeps a **licence back** to show their own VF clips in their personal portfolio (non-commercial) `[OWNER]`.
- [ ] No third-party music in VF materials without clearance (covers → link to Appcompanist, VF-090) `[CHECK: legal]`.

**4.4 Talent release (name, voice, face)**
- [ ] Consent to use the teacher's voice, likeness and name in VF materials: where (site, social, library, ads), how long, whether paid.
- [ ] Teacher approves each public use before it goes live; can ask to remove future uses of their name `[OWNER]`.
- [ ] Separate from the IP assignment; signed **before** any filming (backlog VF-089: 100% of teachers signed before shoots).

**4.5 When a teacher leaves**
- [ ] VF keeps assigned materials (recipes, clips, videos) and may continue using them; credit line kept or removed at the teacher's choice `[OWNER]`.
- [ ] Access to all student data ends on the last day; teacher confirms in writing that no student recordings are kept on personal devices.
- [ ] Students are told and offered another coach; their data stays with VF under the student's consent.
- [ ] Final payment for all logged async minutes within {14 days}.

**4.6 No non-compete**
- [ ] **No non-compete clause.** The teacher may teach anywhere, including privately, during and after working with VF.
- [ ] Only: confidentiality of student data and of unpublished VF materials. `[CHECK: legal — whether even a non-solicit is advisable; recommendation is none]`

**4.7 Safety and quality rules (part of the agreement)**
- [ ] Pilot students are 18+ only; teacher stops recording and tells the owner if they learn a student is under 18.
- [ ] Home Assignment Checklist on 100% of assignments (VF-030); "OK to sing at home" defaults to no.
- [ ] Health flags: same-day reply; SLP-approved Refer-out Card (VF-065); no diagnoses. `[CHECK: SLP — do not use the Refer-out Card until the SLP approves it]`
- [ ] No verdicts about talent, no scores to students (VF-001, VF-091).
- [ ] **AI Gate (VF-025):** teacher approves every text a student sees; `caption_source` recorded; teacher may refuse any AI-rephrased text.

**4.8 Data protection duties of the teacher**
- [ ] Listen only in {shared workspace}; no downloads to personal devices; no sharing outside VF.
- [ ] Report any lost device / wrong recipient within {24 hours}.
- [ ] Teacher consents to their own voice being recorded in lessons and processed by the vendors in 1.1.

**4.9 Founding Coaches (external) — separate agreement**
- [ ] Customer terms (section 3, Founding Coach).
- [ ] **DPA: coach = controller, VF = processor**; our student consent template given to the coach; only 18+ students; VF-030 rules as terms of use.
- [ ] No Founding Coach recording is processed before the DPA is signed (plan §5.2).
- [ ] **Safety terms for Founding Coaches (VF-013, plan v1.1):** students **18+ only**; health flags handled with the **Refer-out Card** and a named **flag schedule** (who replies to flags and when); until the VF library is approved, only **fragments of the student's own lesson** go home as practice. `[CHECK: SLP — the Refer-out Card is not given to coaches or used until the SLP approves it (VF-065)]`

---

## 5. Questions for the lawyer (US + UK) and what each blocks

> Priority: **Q1, Q2, Q5, Q6, Q7 before the first recording** (stop gate, plan §5.1). The rest before the landing/offers go live or before filming.

| # | Question | Blocks |
|---|---|---|
| **Q1** | **US recording consent.** Which states require all-party consent to record a conversation? For an online lesson where teacher and student are in different states, which law applies, and does our form (student ticks + teacher contract) cover it? What about other people audible in a home recording? | VF-064, VF-011, VF-036, VF-013 |
| **Q2** | **Form of consent.** Is click-to-agree with stored timestamp and form version enough in the US and UK, or do we need an e-signature? Are three-to-five separate boxes the right granularity? Can lesson recording be required for the pilot? | VF-064 (stop gate) |
| **Q3** | **CCPA/CPRA and other state privacy laws.** Do we fall under CCPA at pilot scale? Even if not, what notice at collection, "do not sell/share" and deletion wording should we use? Is 30 days for deletion/export right? | VF-064 |
| **Q4** | **Health-related notes.** Is "my voice hurts / is hoarse" health data under state laws (e.g., Washington My Health My Data Act), the FTC Health Breach Notification Rule, or UK GDPR Article 9? What is the minimum we may store, and for how long? | VF-064, VF-030, VF-065 |
| **Q5** | **Biometrics: BIPA and similar laws (Texas, Washington, others).** We don't create voiceprints. Do raw voice recordings, transcription with speaker separation, or any vendor's processing count as biometric identifiers? What must vendors confirm in writing? Can we say "no voiceprints"? | VF-064, VF-025 |
| **Q6** | **COPPA and minors.** Is a self-declared "18 or older" checkbox enough for an adults-only pilot? What must we do if we learn a user is under 13 or 13–17? What do the COPPA amendments (per backlog VF-063: in force from 22.04.2026, voice as personal information — verify) change for a later teen/child offer? **Status of voice under COPPA:** is a voice recording personal information under COPPA as amended, and from what date? Until you answer, our plan treats this as a hypothesis, not a fact. | VF-063, VF-062 |
| **Q7** | **DPA with LLM and transcription providers.** Required terms: no training on our data, retention limits, sub-processor list, breach notice, US↔UK/EU transfers. Is the provider's standard DPA enough? Can we then say "never used to train AI"? | VF-025, VF-064, VF-013 |
| **Q8** | **Auto-renewal and cancellation.** Do state auto-renewal laws (e.g., California) and the FTC negative option rules apply to our one-time purchases at all? For the Founding Coach monthly plan: required disclosures, consent box, reminder timing, one-click cancel. Is "free 6 weeks with no automatic conversion" clean? | VF-007, VF-013 |
| **Q9** | **FTC: guarantees, claims, reviews.** Is "Not happy after your first month? Full refund" enough as written? Are "Singing is a skill, not a gift" and "A real coach replies to your practice every week. No scores, no verdicts." safe claims? Is a refund window of {7} days after the fourth Starter Month lesson acceptable, or should it be longer (US and UK)? Rules for student clips/testimonials (FTC Endorsement Guides, rule on consumer reviews and testimonials), "Results vary", disclosure when something is given in return. | VF-007, VF-008, VF-002, VF-053 |
| **Q10** | **Teacher status and pay.** Contractor vs employee for teachers paid per lesson, per Snapshot and hourly for async work (California AB5 / ABC test, other states; UK employment status). Does the `teacher_seconds` log or the VF-030 rules create "control" that points to employment? | VF-089, VF-058, VF-009 |
| **Q11** | **UK GDPR and ICO.** Lawful basis for recordings (consent vs contract); is a DPIA needed; ICO registration/fee; UK→US transfers (Supabase region, vendors); UK retention and deletion (one month); moral-rights waiver in teacher IP assignment. | VF-064, VF-089, VF-025 |
| **Q12** | **UK consumer terms.** 14-day cancellation rights for online purchases of lessons: what we must say, and how refunds work if lessons start within 14 days. VAT display. Does our Honest Pricing text need UK-specific changes? | VF-007, VF-008 |

---

*Sources: `reports/voice-family-product-plan.md` §3 (№7, №9, №15), §4.3, §5.1, §9 (п. 4, 5, 8); `reports/voice-family-backlog.csv` VF-007, VF-025, VF-063, VF-064, VF-089, VF-058; `reports/product-quality-and-b2b-report.md` (DPA, BIPA, all-party consent); `reports/audience-open-sources-report.md` (Honest Pricing, "sick voice = credit"). Laws named here that are not in those reports (e.g., Washington MHMDA, Texas biometric law, CCPA 45-day / UK GDPR one-month response times, UK 14-day cancellation) appear only inside `[CHECK: legal]` notes or lawyer questions and must be verified. Nothing here is a statement of law.*
