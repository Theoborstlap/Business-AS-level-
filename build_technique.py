# -*- coding: utf-8 -*-
"""Builds AS_Business_9609_Exam_Technique.pdf into the cloned repo folder."""
import pdfgen

B = []
def p(t): B.append(('body', t))
def bu(t): B.append(('bullet', t))
def h1(t): B.append(('h1', t))
def h2(t): B.append(('h2', t))
def h3(t): B.append(('h3', t))
def sp(): B.append(('spacer', ''))

B.append(('title', 'AS Business 9609 - Exam Technique'))
p('How to lay out 3, 5, 8 and 12 mark answers to pick up every available mark. '
  'For the Oct/Nov 2026 exam (syllabus 2026-2028). Includes worked model answers.')
sp()

h1('1. Match your effort to the marks')
p('The mark tariff tells you how much to write and which skills are tested:')
bu('3 marks - "Define / State / Identify" - tests Knowledge (+ a little Application). Write a precise definition plus a brief example. About 4 minutes.')
bu('5 marks - "Explain" - tests Knowledge + Application + a little Analysis. Point, define, apply, then develop ONE step. About 6 minutes.')
bu('8 marks - "Analyse" - tests Knowledge + Application + Analysis. Two developed chains. No judgement. About 10 minutes.')
bu('12 marks - "Evaluate / Discuss / Recommend / To what extent" - tests Knowledge + Application + Analysis + Evaluation. Two developed chains PLUS a weighed judgement. About 15 minutes.')

h1('2. The four skills (Assessment Objectives)')
bu('[K] Knowledge (AO1): define and state relevant terms and theory.')
bu('[App] Application (AO2): use the specific business/context given in the question.')
bu('[An] Analysis (AO3): develop cause-and-effect chains - push each point to its final effect on the business.')
bu('[Ev] Evaluation (AO4): make and justify a judgement. Needed ONLY on 12 (and higher) mark questions.')

# ---------------- 3 MARK ----------------
h1('3. The 3-mark layout - "Define / State"')
p('Recipe: Definition [K] + a short example or extra detail [K/App].')
p('Template: [Term] is [clear precise definition]. For example, [quick example].')
bu('2 marks for the definition, 1 for the example/expansion.')
bu('Do: use the exact key words. Do NOT: explain consequences or write chains.')
h3('Worked example - "Define added value" [3]')
p('Added value is the difference between the selling price of a product and the cost of the bought-in materials used to make it [K]. For example, a coffee shop buying beans for $0.30 and selling a coffee for $3.00 adds $2.70 of value [App].')

# ---------------- 5 MARK ----------------
h1('4. The 5-mark layout - "Explain"')
p('Recipe: Point, then define [K], then apply to the business [App], then develop ONE step [An].')
p('Template: One [benefit/reason] is [point], which means [define] [K]. In the case of [business/context] this [apply] [App], so [one consequence] [An].')
bu('If the question says "Explain two...", write two shorter versions (about 2-3 marks each).')
bu('Do: always link to the context. Do NOT: write a full evaluation or list undeveloped points.')
h3('Worked example - "Explain one benefit to a firm of low labour turnover" [5]')
p('One benefit is a more experienced workforce [K], as fewer staff leave so skills are retained [K]. For a manufacturer relying on skilled machine operators [App], this means higher quality and productivity [An] and lower recruitment and training costs [An].')

# ---------------- 8 MARK ----------------
h1('5. The 8-mark layout - "Analyse"')
p('Recipe: TWO points. Each = Point, define [K], apply [App], then chain 2-3 steps: because... which leads to... therefore... [An].')
p('Paragraph template (write it twice): One [way/benefit/drawback] is [point] [K]. This means [define] [K]. For [business/context] this [apply] [App]. As a result [effect 1] [An], which in turn [effect 2] [An], meaning [final effect on profit/costs/competitiveness] [An].')
bu('The key skill is CHAINS - push each point to its final business effect; do not stop at the first consequence.')
bu('Do NOT write an introduction or a conclusion. Go straight into Point 1.')
p('Analysis connectives: this means... because... which leads to... as a result... this in turn... therefore... ultimately...')
h3('Worked model - "Analyse two ways business enterprise can help the development of a country" [8]')
p('Point 1 - Job creation: One way business enterprise helps development is by creating employment [K]. Enterprise involves entrepreneurs setting up and expanding businesses that combine the factors of production and must hire workers [K]. In a developing country where unemployment is high [App], these new businesses employ local people [App]. As a result more households earn an income [An], so they spend more in the local economy [An], which raises demand for other firms and creates further jobs through a multiplier effect [An], gradually raising living standards and reducing poverty [An].')
p('Point 2 - Higher output and tax revenue: A second way is by increasing national output (GDP) and tax revenue [K]. As enterprises produce and sell goods and services they add value and generate profits and wages [K]. In a developing economy [App] this extra output raises GDP and means firms and workers pay more corporate and income tax [App/An]. As a result the government receives more revenue [An], which it can invest in infrastructure, education and healthcare [An], improving the workforce productivity and quality of life and driving further long-term development [An].')
p('Note: there is NO judgement - an 8-mark analyse question does not need one.')

# ---------------- 12 MARK ----------------
h1('6. The 12-mark layout - "Evaluate / Recommend / Discuss"')
p('Structure: (optional 1-line intro), Argument 1 as a full chain, Argument 2 or counter as a full chain, then the JUDGEMENT.')
bu('Argument FOR / benefit - same chain as an 8-marker (K + App + An).')
bu('Argument AGAINST / drawback / alternative - another full applied chain.')
bu('Judgement [Ev] - where the top marks are. Include: a clear decision; WHY one side outweighs the other (rank them); an "it depends on..." named factor; a short-term vs long-term point; and a link back to the specific business.')
p('Judgement sentence starters:')
bu('"Overall, the most important factor is X, because..."')
bu('"This depends largely on [named factor]: if [condition] then [choice A], but if [condition] then [choice B]..."')
bu('"In the short term [effect], but in the long term [effect], so on balance..."')
bu('"Therefore I recommend X, provided that [condition]."')
bu('Do: spend about a third of your time on the judgement. Do NOT: stop after two arguments - no judgement caps you at about half marks.')
h3('Worked model - "Intrapreneurship is the most important factor that will ensure the success of a computer entertainment business." Evaluate this view. [12]')
p('Intro: Intrapreneurship means employees using entrepreneurial skills to innovate within an existing business [K], and its importance to a games company must be weighed against other success factors.')
p('FOR: Intrapreneurship is important because success in computer entertainment depends on constant innovation [App]. Intrapreneurs generate new game ideas, features and technologies from within the business [K/App]. This means the company keeps launching fresh titles [An], helping it stay ahead of fast-moving competitors [An], attracting and retaining players [An], leading to repeat sales, a strong brand and higher long-term profit [An].')
p('AGAINST: However, intrapreneurship alone cannot guarantee success. Finance and marketing may matter more [K]. Even the most innovative game needs large sums to fund long development and testing [App]; without enough finance it may never be completed or launched at poor quality [An], so it fails despite good ideas [An]. Equally, the market is crowded, so without effective marketing and branding [K/App] customers will not know the product exists [An], meaning low sales even for an excellent game [An].')
p('JUDGEMENT: Overall, intrapreneurship is a major factor but not necessarily THE most important [Ev]. It is necessary but not sufficient - the innovation it produces only creates success if supported by finance to develop the games and marketing to sell them [Ev]. Its importance also depends on the situation [Ev]: for a new start-up studio, securing finance is probably most critical in the short term, whereas for an established studio intrapreneurship is the key to staying competitive in the long term [Ev]. Therefore the statement is only partly true: intrapreneurship drives the long-term innovation this industry relies on, but the single most important factor changes with the business size, stage and objectives, so it must be combined with sound finance and marketing rather than relied on alone [Ev].')

# ---------------- SUMMARY ----------------
h1('7. One-look revision card')
p('3 marks: 1 definition. K yes, App small, An no, Ev no. No intro/conclusion.')
p('5 marks: 1-2 points. K yes, App yes, An one step, Ev no. No intro/conclusion.')
p('8 marks: 2 points. K yes, App yes, An 2-3 steps, Ev no. No intro/conclusion.')
p('12 marks: 2 points + judgement. K yes, App yes, An 2-3 steps, Ev ESSENTIAL. Judgement only, no long intro.')

h1('8. The three biggest mark-losers to avoid')
bu('Not linking to the business given in the question - you lose all Application marks.')
bu('Listing many points without developing them - you lose Analysis marks. Fewer, deeper chains score higher.')
bu('Writing no judgement on a 12-mark question - you cap your mark at roughly half.')
sp()
B.append(('body', 'Apply every point to the specific business and justify your judgements to reach the top mark bands.'))

pages = pdfgen.build_pdf(
    B, '/projects/sandbox/Business-AS-level-/AS_Business_9609_Exam_Technique.pdf',
    footer_prefix='Exam Technique - Page')
print('Exam technique PDF:', pages, 'pages')
