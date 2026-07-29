# Cambridge AS Level Business (9609) — Revision Pack

Complete self-study revision pack for the **Oct/Nov 2026** exam (syllabus **2026–2028**).
Covers the full AS syllabus: Topics 1–5.

## What's in this pack

### Notes
- **`AS_Business_9609_Notes.md`** — Full revision notes for the entire AS syllabus, with comparison tables, a formula sheet, and exam-technique reminders.

### Question bank
- **`AS_Business_9609_Question_Bank.pdf`** — 167 questions covering every syllabus sub-point (knowledge, application, analysis, evaluation and calculation).
- **`AS_Business_9609_Answers.pdf`** — Model answers / mark guidance for all 167.

### Calculation drills
- **`AS_Business_9609_Calculation_Drills.pdf`** — Practice for every AS formula (A–L): added value, labour turnover, labour productivity, market share & growth, capacity utilisation, working capital, total/average cost, cash flow, contribution & profit, break-even, margin of safety, target profit, and variances.
- **`AS_Business_9609_Calculation_Drills_Answers.pdf`** — Full worked solutions.

### Case study practice (past-paper style)
- **`AS_Business_9609_Case_Studies.pdf`** — 5 data-response case studies (one per topic), each building from define → calculate → analyse → evaluate.
- **`AS_Business_9609_Case_Studies_Answers.pdf`** — Model answers with judgements.

### Topic mini-tests
- **`AS_Business_9609_Topic_MiniTests.pdf`** — 5 quick ~15-minute recall quizzes, one per topic.
- **`AS_Business_9609_Topic_MiniTests_Answers.pdf`** — Answer keys.

### Exam technique
- **`AS_Business_9609_Exam_Technique.pdf`** — How to lay out 2, 3, 5, 8 and 12 mark answers to get all the marks (K/App/An/Ev), with worked model answers for each tariff.

### Interactive trainer (website)
- **`index.html`** + **`quiz-data.js`** — A browser quiz with two sections:
  - **127 two-mark definitions** — marked **Correct (2/2)**, **Partially (1/2)** or **Wrong (0/2)**.
  - **34 three-mark "explain" questions** — marked **Correct (3/3)**, **Partially (1-2/3)** or **Wrong (0/3)**.
- Answer **in your own words**: marking is keyword/synonym based with light word-stemming (so plurals and verb forms match), and it shows which mark points you hit plus the model answer whenever you miss any marks. Includes a **question-type selector** (2-mark / 3-mark / mixed), **topic filters**, **shuffle** and a **live score**.
- **Review my mistakes**: every question you don't get full marks on is saved. Open the review to see your answer next to the model answer for each, then hit **"Retry these"** to practise just those questions again.

**To use it:**
- Easiest: enable **GitHub Pages** (repo *Settings > Pages > Source: Deploy from a branch > Branch: `main` / root*), then open `https://<your-username>.github.io/Business-AS-level-/`.
- Or download `index.html` and `quiz-data.js` into the same folder and open `index.html` in any browser.

## Suggested revision routine
1. Read the relevant section of **Notes**.
2. Take the **Mini-Test** for that topic (closed book).
3. Drill the **Calculations** for that topic until they are automatic.
4. Work through the matching **Question Bank** questions.
5. Finish each topic with the **Case Study** under timed conditions (~1.25 min/mark).
6. Mark your work against the answer booklets and note weak areas.

## Formula quick list
| Formula | |
|---|---|
| Added value | Selling price − cost of bought-in materials |
| Labour turnover | (Number leaving ÷ average employed) × 100 |
| Labour productivity | Total output ÷ number of employees |
| Market share | (Firm sales ÷ total market sales) × 100 |
| Market growth | (Change in market size ÷ original size) × 100 |
| Capacity utilisation | (Actual output ÷ maximum output) × 100 |
| Working capital | Current assets − current liabilities |
| Total cost | Fixed costs + variable costs |
| Average (unit) cost | Total cost ÷ output |
| Net cash flow | Cash inflows − cash outflows |
| Closing balance | Opening balance + net cash flow |
| Contribution per unit | Selling price − variable cost per unit |
| Profit (contribution method) | Total contribution − fixed costs |
| Break-even output | Fixed costs ÷ contribution per unit |
| Margin of safety | Actual output − break-even output |
| Variance | Actual figure − budgeted figure |

## How the PDFs were generated
The PDFs are built with a small dependency-free Python generator:
- `pdfgen.py` — minimal pure-Python PDF writer (Helvetica, word-wrap, pagination).
- `build_papers.py` — builds the question bank + answers.
- `build_extras.py` — builds the drills, case studies and mini-tests (+ answers).

Regenerate everything with:
```bash
python3 build_papers.py && python3 build_extras.py
```

*Prepared as a study aid. Indicative answers — in the exam, apply points to the specific business and justify your judgements to reach the top mark bands.*
