# -*- coding: utf-8 -*-
"""Builds AS_Business_9609_Exam_Technique.pdf into the cloned repo folder.

Structured around the OFFICIAL 9609 mark grids (AO1/AO2/AO3/AO4 splits).
ASCII-only content (pdfgen supports standard Helvetica glyphs only).
Use '->' for arrows and straight quotes.
"""
import pdfgen

B = []
def p(t): B.append(('body', t))
def bu(t): B.append(('bullet', t))
def h1(t): B.append(('h1', t))
def h2(t): B.append(('h2', t))
def h3(t): B.append(('h3', t))
def sp(): B.append(('spacer', ''))

B.append(('title', 'AS Business 9609 - Exam Technique'))
p('A step-by-step guide built around the OFFICIAL mark grids, so you write '
  'exactly what each Assessment Objective (AO) rewards. For the Oct/Nov 2026 '
  'exam (syllabus 2026-2028). Each mark tariff shows: the exact AO split, the '
  'structure, WHERE the K and APP go, key words to write, an "ask yourself" '
  'checklist, and THREE tagged worked examples.')
sp()

# =====================================================================
h1('PART A - THE FOUNDATIONS')
# =====================================================================

h2('1. The four skills (Assessment Objectives)')
p('Every mark comes from one of these four skills. Learn the tags - they are '
  'used on every worked example below.')
bu('[K]  AO1 Knowledge and understanding: define terms / state relevant '
   'points correctly.')
bu('[App] AO2 Application: use the SPECIFIC business/context in the question '
   '(its name, product, market, numbers, situation).')
bu('[An]  AO3 Analysis: build cause-and-effect chains - connect causes, '
   'impacts and consequences of a point.')
bu('[Ev]  AO4 Evaluation: make and justify a balanced judgement IN CONTEXT. '
   'Only on 12-mark questions.')
p('"Developed" vs "limited": examiners award the top mark in each column only '
  'when the skill is DEVELOPED (a full definition, application that clearly '
  'fits the case, a chain pushed to its final effect, a judgement that '
  'balances arguments in context). A vague or half-done attempt scores the '
  'lower "limited" mark.')

h2('2. The mark grids - what each question is worth (learn this)')
p('The AS papers use fixed AO splits. This is the single most important table '
  'in this guide - it tells you precisely what to include:')
bu('2 marks (a) "What is meant by...": AO1 = 2. Knowledge ONLY.')
bu('3 marks 1(b) 2(b) 3(b): AO1 = 1, AO2 = 2. Knowledge + DEVELOPED '
   'application. NO analysis.')
bu('5 marks 1(c) 2(c) 3(c): AO1 = 1, AO2 = 2, AO3 = 2. ONE point: knowledge '
   '+ application + developed analysis.')
bu('8 marks 5(a) 6(a): AO1 = 2, AO2 = 2, AO3 = 4. TWO points, each applied '
   'and analysed. NO evaluation.')
bu('12 marks 5(b) 6(b): AO1 = 2, AO2 = 2, AO3 = 2, AO4 = 6. Applied '
   'analytical points PLUS a developed, balanced judgement IN CONTEXT. '
   'Evaluation is HALF the marks.')
p('Timing rule: about 1 to 1.5 minutes per mark.')

h2('3. Command words - what each one is really asking')
bu('State / Identify / Give / What is meant by / Define - name or define it. '
   'Knowledge only.')
bu('Explain (3 marks) - give one point and DEVELOP it into the business '
   'context. No chain of consequences needed.')
bu('Analyse (5 and 8 marks) - build cause-and-effect chains. No judgement.')
bu('Evaluate / Discuss / Assess / To what extent / Recommend (12 marks) - '
   'argue BOTH sides, then a justified judgement in context.')

h2('4. WHERE to put the K and the APP (the golden order)')
p('For any developed answer (5, 8 or 12 marks) write each paragraph in this '
  'fixed order so you hit each AO in turn:')
bu('STEP 1 - [K] first: state your point and DEFINE the key term. '
   'Opener: "One [benefit/reason] is X, which means [definition]."')
bu('STEP 2 - [App] next: tie it to THIS business. '
   'Opener: "In the case of [business], which [detail from the case]..."')
bu('STEP 3 - [An] next: develop the chain with "which means... because... '
   'leads to... therefore..." until you reach profit, cost, cash or '
   'competitiveness. (Skip this for a 3-mark answer.)')
bu('STEP 4 - [Ev] last (12 marks only): judge - which side wins, why, and '
   'what it depends on, all in the business context.')
p('Memory hook: DEFINE it (K) -> LOCATE it in the business (APP) -> DEVELOP '
  'it (AN) -> DECIDE (EV).')

# =====================================================================
h1('PART B - LAYOUT AND EXAMPLES BY MARK TARIFF')
# =====================================================================

# ---------------- 2 MARK ----------------
h2('5. The 2-mark answer - "What is meant by..." (AO1 = 2)')
p('Marks: AO1 only. 2 marks = knowledge of the term showing a SOUND '
  'understanding; 1 mark = only a PARTIAL understanding.')
h3('Structure')
bu('Give a full, precise meaning. A two-part definition is the safest way to '
   'show "sound" (not partial) understanding.')
bu('"[Term] is [part 1] [K] which [part 2] [K]."')
h3('Key words to write')
bu('"is defined as...", "refers to...", "is the difference between...", '
   '"is when...".')
h3('Ask yourself')
bu('Is my definition FULL (two parts), not a vague half-sentence (which '
   'scores only 1)?')
bu('Have I used the exact syllabus term?')
bu('Have I resisted wasting time on examples or consequences (no marks for '
   'them here)?')
h3('Worked examples')
p('(a) "What is meant by opportunity cost?" [2]: Opportunity cost is the '
  'benefit of the next best alternative [K] that is given up when a choice is '
  'made [K].')
p('(b) "What is meant by added value?" [2]: Added value is the difference '
  'between the selling price of a product [K] and the cost of the bought-in '
  'materials used to make it [K].')
p('(c) "What is meant by market segmentation?" [2]: Market segmentation is '
  'dividing a market into groups of customers [K] who share similar '
  'characteristics or needs [K].')

# ---------------- 3 MARK ----------------
h2('6. The 3-mark answer - Q1(b)/2(b)/3(b) (AO1 = 1, AO2 = 2)')
p('Marks: 1 for knowledge of ONE relevant point, 2 for DEVELOPED application '
  'of that point to the business context. There is NO analysis mark - do not '
  'write a chain of consequences.')
h3('Structures (the 1 knowledge mark changes with the wording)')
bu('Wording A - "Explain one benefit/reason/way...": K = STATE one relevant '
   'point (the benefit/reason itself) [K]. Then develop it into the business '
   '[App][App].')
bu('Wording B - "Explain one benefit of [named term]" or "...the importance '
   'of [term]": K = DEFINE the term [K]. Then apply that term to the business '
   '[App][App].')
bu('Either way AO2 is worth 2: to score 2 (developed) not 1 (limited), use '
   'real case detail and show how it fits THIS firm, not businesses in '
   'general. Do NOT add an analysis chain.')
h3('Key words to write')
bu('"In the case of [business]...", "because [business] [case detail]...", '
   '"for a firm that [case detail]...", "this fits [business] as...".')
h3('Ask yourself')
bu('Have I stated one relevant point (the 1 knowledge mark)?')
bu('Have I applied it to THIS business using specific case detail (2 marks)?')
bu('Have I stopped at application - NOT drifted into a "leads to... '
   'therefore..." analysis chain (no marks for it here)?')
h3('Worked examples')
p('(a) "ZR is a fast-fashion retailer. Explain one way ZR could add value." '
  '[3]: Adding value means raising the price paid above the cost of bought-in '
  'materials [K]. ZR could add value through its strong brand and rapid '
  'turnaround of on-trend designs [App], so its fashion-conscious shoppers '
  'will pay a premium for up-to-date styles they cannot get quickly elsewhere '
  '[App].')
p('(b) "BK is a small bakery on a busy high street. Explain one benefit to BK '
  'of its location." [3]: A good location means a site with high customer '
  'footfall [K]. BK sits on a busy high street surrounded by offices [App], so '
  'many passing workers can buy its bread and lunch items each day [App].')
p('(c) "TF manufactures toys and sells to large retailers. Explain one reason '
  'TF holds inventory." [3]: Inventory is the stock of materials and finished '
  'goods a business holds [K]. TF builds up finished toys before the December '
  'festive season [App], so it can supply the large orders its retail '
  'customers place at that peak time [App].')

# ---------------- 5 MARK ----------------
h2('7. The 5-mark answer - Q1(c)/2(c)/3(c) (AO1 = 1, AO2 = 2, AO3 = 2)')
p('Marks: 1 knowledge + 2 developed application + 2 developed analysis, all '
  'for ONE point. Analyse a single point in depth - do not list several.')
h3('Structures (the 1 knowledge mark can be a POINT or a DEFINITION)')
bu('Wording A - "Explain/Analyse one benefit/drawback/reason/way...": K = '
   'STATE the one point, e.g. name the benefit [K]. App = apply to the '
   'business [App][App]. An = chain to a final effect [An][An].')
bu('Wording B - "Explain the importance of [term]" / "Explain why a manager '
   'needs to understand [term]" / "Explain why [term] matters": K = DEFINE '
   'the term - here the knowledge mark IS the definition, not a benefit [K]. '
   'App = apply the term to the business [App][App]. An = chain showing why '
   'it matters -> effect [An][An].')
bu('Wording C - "Explain how a business might [do X]": K = STATE one method '
   '[K]. App = apply the method to the business [App][App]. An = chain to the '
   'outcome [An][An].')
bu('Universal template: [knowledge - a point OR a definition] [K]. For '
   '[business + detail] this [apply] [App][App]. This means [effect] [An], '
   'which leads to [final effect on profit/cost/competitiveness] [An].')
h3('Key words to write')
bu('"One [reason] is...", "which means...", "In the case of [business]...", '
   '"this means that...", "which leads to...", "as a result...".')
h3('Ask yourself')
bu('Have I DEFINED my one point (the knowledge mark)?')
bu('Have I applied it to THIS business with case detail (2 marks)?')
bu('Have I developed a chain to a FINAL business effect (2 analysis marks)?')
bu('Have I avoided writing an evaluation (none is rewarded here)?')
h3('Worked examples (benefit / limitation / analyse)')
p('(a) BENEFIT - "Analyse one benefit to a manufacturer of low labour '
  'turnover." [5]: One benefit is a more experienced workforce, as low '
  'turnover means few staff leave and need replacing [K]. For a manufacturer '
  'relying on skilled machine operators [App], experienced staff are retained '
  'rather than constantly retrained [App]. This means higher productivity and '
  'quality [An], which lowers unit costs and recruitment spending, raising '
  'profit [An].')
p('(b) LIMITATION - "Analyse one limitation to a start-up of relying on a '
  'business plan." [5]: One limitation is that a plan is built on forecasts '
  'that may be inaccurate [K]. For a new bakery estimating sales in an area '
  'where it has never traded [App][App], if real demand is far below forecast '
  '[An], the owner may overspend on stock and staff and run short of cash, '
  'threatening survival [An].')
p('(c) ANALYSE - "Analyse one reason a supermarket holds buffer inventory." '
  '[5]: One reason is to avoid stock-outs, as buffer inventory is a safety '
  'level of stock [K]. For a supermarket selling fast-moving fresh food with '
  'uncertain daily demand [App][App], buffer stock keeps shelves full if '
  'demand spikes [An], so it does not lose sales and customers to nearby '
  'rivals [An].')
h3('Real past-paper [5] questions (Paper 1 style)')
p('Paper 1 (Papers 12/13) has no case study, so these "Explain" questions are '
  'general. You still earn the 2 application marks by applying to a realistic '
  'business situation (e.g. "a new business", "a firm waiting for payment"), '
  'then push a short analysis chain for the 2 analysis marks.')
p('(d) Cambridge June 2021 Paper 12: "Explain the importance of working '
  'capital to a new business." [5]: Working capital is the finance available '
  'for day-to-day running, found by current assets minus current liabilities '
  '[K]. For a new business with small cash reserves and uncertain early sales '
  '[App], having enough working capital lets it pay wages, suppliers and rent '
  'on time [App]. This means it avoids running out of cash [An], so it can '
  'keep trading and survive its risky first months rather than becoming '
  'insolvent [An].')
p('(e) Cambridge June 2022 Paper 12: "Explain why a business manager needs to '
  'understand the difference between capital expenditure and revenue '
  'expenditure." [5]: Capital expenditure is spending on non-current assets '
  'such as machinery, while revenue expenditure is day-to-day spending such as '
  'wages and materials [K]. A manager who understands this [App] can fund '
  'long-term assets with long-term finance and day-to-day costs from cash flow '
  '[App]. This means budgeting and profit figures are accurate [An], so the '
  'manager avoids paying for a long-term asset out of short-term cash and '
  'causing a cash shortage [An].')
p('(f) Cambridge November 2022 Paper 13: "Explain how a business might improve '
  'its cash flow." [5]: One way is to speed up cash inflows, for example by '
  'chasing trade receivables or offering early-payment discounts [K]. For a '
  'business kept waiting a long time by its customers [App], collecting cash '
  'sooner raises the cash available each month [App]. This means it can pay '
  'its own bills on time [An], reducing the need for a costly overdraft and '
  'lowering the risk of insolvency [An].')

# ---------------- 8 MARK ----------------
h2('8. The 8-mark answer - Q5(a)/6(a) (AO1 = 2, AO2 = 2, AO3 = 4)')
p('Marks: 2 knowledge + 2 application + 4 analysis. Write TWO developed, '
  'applied points, each pushed to a final effect. NO intro, NO conclusion, NO '
  'judgement. The big score here is ANALYSIS (4 marks), so develop each chain '
  'fully.')
h3('Structures (all use TWO points; the wording sets what the points are)')
bu('Wording A - "Analyse two benefits/drawbacks/ways/reasons...": the two '
   'points ARE the two benefits/ways. Each point: K = state it [K], App = '
   'apply [App], An = develop chain [An][An].')
bu('Wording B - "Analyse the impact of [X] on a business": briefly define X '
   '[K], then give TWO impacts as your two points, each applied [App] and '
   'analysed [An][An].')
bu('Wording C - "Analyse the factors [a business] should consider before '
   '[decision]": pick TWO factors as your points; state each [K], apply '
   '[App], analyse [An][An].')
bu('Per point template: "One [point] is... [K]. For [business + detail] this '
   '[apply] [App]. As a result [effect 1] [An], which in turn [effect 2] '
   '[An], meaning [final effect] [An]." Analysis is 4 of 8 marks - develop '
   'both chains. NO judgement.')
h3('Key words to write (analysis connectives)')
bu('"this means...", "because...", "which leads to...", "as a result...", '
   '"this in turn...", "therefore...", "ultimately...".')
h3('Ask yourself')
bu('Do I have TWO separate, different points (for the 2 knowledge marks)?')
bu('Is each applied to THIS business (for the 2 application marks)?')
bu('Have I DEVELOPED each chain to a final effect (this is where 4 of the 8 '
   'marks are)?')
bu('Have I written NO judgement (none is rewarded at 8 marks)?')
h3('Worked example 1 - "Analyse two ways business enterprise can help the '
   'development of a country." [8]')
p('Point 1 - Job creation: One way is by creating employment [K]. In a '
  'developing country where unemployment is high [App], new enterprises hire '
  'local people. As a result more households earn an income [An], so they '
  'spend more locally [An], raising demand for other firms and creating '
  'further jobs through a multiplier effect [An], gradually raising living '
  'standards [An].')
p('Point 2 - Higher output and tax revenue: A second way is by raising output '
  '(GDP) and tax revenue [K]. In a developing economy [App], as enterprises '
  'produce and sell they generate profits and wages. As a result the '
  'government collects more tax [An], which it can invest in infrastructure, '
  'education and healthcare [An], improving productivity and driving further '
  'development [An].')
h3('Worked example 2 - "Analyse two benefits to a clothing retailer of market '
   'segmentation." [8]')
p('Point 1 - Better-matched products: One benefit is that segmentation lets '
  'the firm target groups with similar needs [K]. For a fashion chain '
  'splitting its market by age and income [App], it designs ranges that fit '
  'each group [An], so customers are more satisfied and buy more [An], raising '
  'sales revenue [An].')
p('Point 2 - Less wasted marketing spend: A second benefit is more efficient '
  'promotion [K]. For the retailer advertising a teen range on social media '
  'rather than TV [App], less money is spent reaching people who will not buy '
  '[An], so the cost per sale falls [An] and profit margins improve [An].')
h3('Worked example 3 - "Analyse two ways a business could improve its cash '
   'flow." [8]')
p('Point 1 - Collect receivables faster: One way is to shorten the credit '
  'period given to customers [K]. For a wholesaler currently waiting 60 days '
  'for payment [App], cutting this to 30 days brings cash in sooner [An], so '
  'it can pay wages and suppliers on time [An], reducing the risk of '
  'insolvency [An].')
p('Point 2 - Delay paying payables: A second way is to negotiate longer credit '
  'from suppliers [K]. For the same wholesaler [App], paying after 60 rather '
  'than 30 days keeps cash in the business longer [An], so it can fund '
  'day-to-day costs without a costly overdraft [An], lowering interest costs '
  '[An].')
p('Reminder: an 8-mark "Analyse" question does NOT need a judgement.')

# ---------------- 12 MARK ----------------
h2('9. The 12-mark answer - Q5(b)/6(b) (AO1 = 2, AO2 = 2, AO3 = 2, AO4 = 6)')
p('Marks: 2 knowledge + 2 application + 2 analysis + 6 EVALUATION. Evaluation '
  'is HALF the marks, so it is where you win or lose the grade. You only need '
  'enough K/App/An to set up the arguments (about 6 marks); then spend the '
  'most time on a developed, balanced judgement IN CONTEXT (6 marks).')
h3('Structures (the wording sets the two sides; AO4 judgement is always 6)')
bu('Common spine: (optional define key term [K]) -> Side 1 applied point + '
   'short chain [K/App/An] -> Side 2 applied point + short chain [K/App/An] '
   '-> JUDGEMENT [Ev].')
bu('Wording A - "Evaluate whether [business] should do X": Side 1 = arguments '
   'FOR doing X; Side 2 = arguments AGAINST. Judge whether it should.')
bu('Wording B - "[Statement]. To what extent do you agree? / Evaluate this '
   'view": Side 1 = arguments SUPPORTING the statement; Side 2 = arguments '
   'CHALLENGING it. Judge HOW FAR you agree.')
bu('Wording C - "Recommend whether [business] should choose X or Y": Side 1 = '
   'the case for X; Side 2 = the case for Y. End with a clear RECOMMENDATION.')
bu('Wording D - "Discuss the factors [business] should consider when '
   '[decision]": give two or more factors (each applied + analysed), then '
   'judge WHICH factor matters most for this business.')
bu('JUDGEMENT [Ev] (always the 6 marks): a clear decision; WHY one side wins; '
   'an "it depends on..." named factor; a short-term vs long-term point; all '
   'tied to the SPECIFIC business.')
p('Level ladder for AO4: limited judgement (1-2) -> developed judgement that '
  'balances arguments (3-4) -> developed judgement that balances arguments IN '
  'CONTEXT of the business (5-6). Naming the business in your judgement is '
  'what reaches the top level.')
h3('Key words to write (judgement starters)')
bu('"Overall, the most important factor for [business] is X because..."')
bu('"This depends largely on [named factor]: if [condition] then A, but if '
   '[condition] then B..."')
bu('"In the short term [effect], but in the long term [effect], so on '
   'balance..."')
bu('"Therefore [business] should X, provided that [condition]."')
h3('Ask yourself')
bu('Have I argued BOTH sides, each applied to the business?')
bu('Have I made a CLEAR decision (not "it could go either way")?')
bu('Have I said WHY one side outweighs the other?')
bu('Have I added an "it depends on..." factor and a short vs long term point?')
bu('Is my judgement clearly IN CONTEXT (names the business + its situation)? '
   'This is the difference between 4 and 6 marks.')
bu('Did I spend close to HALF my time on the judgement?')
h3('Worked example 1 - "Intrapreneurship is the most important factor for the '
   'success of a computer games business." Evaluate. [12]')
p('Intro: Intrapreneurship means employees using entrepreneurial skills to '
  'innovate within an existing business [K].')
p('FOR: Success in games depends on constant innovation [App]. Intrapreneurs '
  'create new ideas from within, so the firm keeps launching fresh titles '
  '[An] and stays ahead of rivals [An].')
p('AGAINST: However, finance and marketing may matter more [K]. Even a great '
  'game needs large sums for long development [App]; without finance it may '
  'never launch [An], failing despite good ideas [An].')
p('JUDGEMENT: Overall, for this games business intrapreneurship is a major '
  'but not sufficient factor [Ev]. Innovation only creates success if it is '
  'funded and marketed, so it must be combined with finance and branding [Ev]. '
  'It depends on the stage of the firm [Ev]: for a new studio securing finance '
  'is most critical in the short term, whereas for an established studio '
  'intrapreneurship is the key to staying competitive in the long term [Ev]. '
  'So the statement is only partly true for this business [Ev].')
h3('Worked example 2 - "A private limited company (JB) should become a public '
   'limited company (Plc)." Evaluate. [12]')
p('FOR: Floating lets JB sell shares to the public and raise large capital '
  '[K]. For JB wanting to expand nationally [App], this funds new outlets '
  '[An] and enables economies of scale that lower unit costs [An].')
p('AGAINST: However, selling public shares dilutes ownership [K]. For JB\'s '
  'founding family [App], this risks losing control and even a hostile '
  'takeover [An], plus pressure for short-term dividends [An].')
p('JUDGEMENT: Whether JB should float depends mainly on how much finance it '
  'needs and how much control the family will give up [Ev]. If the planned '
  'expansion is large and cannot be funded by loans or retained profit, '
  'becoming a Plc is justified for JB [Ev]; but if the family values control '
  'and the sum needed is modest, a bank loan is the better route [Ev]. On '
  'balance, for a family firm like JB the loss of control usually outweighs '
  'the benefit unless the capital required is very large [Ev].')
h3('Worked example 3 - "For its new innovative product, TX should use '
   'penetration pricing rather than skimming." Evaluate. [12]')
p('FOR penetration: A low launch price attracts price-sensitive buyers '
  'quickly [K]. For TX entering a crowded streaming market [App], this wins '
  'market share fast [An] and builds a large subscriber base [An].')
p('AGAINST (skimming): A high initial price earns a large margin from '
  'customers who want it first [K]. If TX\'s product is genuinely unique with '
  'few rivals [App], skimming recovers high development costs quickly [An] and '
  'builds a premium image [An].')
p('JUDGEMENT: The best method for TX depends on how much competition it faces '
  'and how unique its product really is [Ev]. In the crowded streaming market '
  'described, where rivals are many and services are easy to copy, penetration '
  'is the stronger choice to grab share fast [Ev]; skimming would only suit TX '
  'if the product were truly unique [Ev]. So for TX in this context, '
  'penetration pricing is justified in the short term, though it must plan to '
  'raise prices later to protect margins [Ev].')

# =====================================================================
h1('PART C - QUICK REFERENCE')
# =====================================================================

h2('10. AO split at a glance')
p('2 marks: AO1 2. (Define.)')
p('3 marks: AO1 1 + AO2 2. (Knowledge + developed application. No analysis.)')
p('5 marks: AO1 1 + AO2 2 + AO3 2. (One point, applied and analysed.)')
p('8 marks: AO1 2 + AO2 2 + AO3 4. (Two points, applied and analysed. No '
  'evaluation.)')
p('12 marks: AO1 2 + AO2 2 + AO3 2 + AO4 6. (Two applied points + balanced '
  'judgement in context. Evaluation = half.)')

h2('11. Analysis connective bank (build your chains)')
bu('this means... / because... / which leads to... / as a result...')
bu('this in turn... / consequently... / therefore... / ultimately...')
bu('End every chain on profit, cost, cash flow or competitiveness.')

h2('12. Evaluation / judgement bank (12-mark answers)')
bu('"The most important factor for [business] is... because..."')
bu('"This depends on... (size of the firm, its objectives, the economy, the '
   'level of competition)."')
bu('"In the short term... whereas in the long term..."')
bu('"On balance, [business] should... provided that..."')

h2('13. The three biggest mark-losers to avoid')
bu('Not applying to the business in the question - you lose ALL AO2 marks (and '
   'the top AO4 level).')
bu('On 3-mark questions, writing a long analysis chain - it earns nothing; '
   'develop the APPLICATION instead.')
bu('On 12-mark questions, a weak or missing judgement - AO4 is 6 of the 12 '
   'marks, so you cannot pass without a developed judgement in context.')
sp()
p('Golden rule: DEFINE it (K) -> LOCATE it in the business (APP) -> DEVELOP it '
  '(AN) -> DECIDE (EV). Match what you write to the AO split for that tariff, '
  'apply every point to the business, and put your judgement in context.')

pages = pdfgen.build_pdf(
    B, '/projects/sandbox/Business-AS-level-/AS_Business_9609_Exam_Technique.pdf',
    footer_prefix='Exam Technique - Page')
print('Exam technique PDF:', pages, 'pages')
