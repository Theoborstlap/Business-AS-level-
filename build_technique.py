# -*- coding: utf-8 -*-
"""Builds AS_Business_9609_Exam_Technique.pdf into the cloned repo folder.

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
p('A step-by-step guide to laying out 2, 3, 5, 8 and 12 mark answers so you '
  'pick up every available mark. For the Oct/Nov 2026 exam (syllabus '
  '2026-2028). Each mark tariff shows: what it tests, the structure, WHERE the '
  'K and APP go, the key words to write, an "ask yourself" checklist, and '
  'THREE tagged worked examples.')
sp()

# =====================================================================
h1('PART A - THE FOUNDATIONS')
# =====================================================================

h2('1. The four skills (Assessment Objectives)')
p('Every mark you earn comes from one of these four skills. Learn the tags - '
  'they are used on every worked example below.')
bu('[K]  Knowledge (AO1): define terms and state relevant theory correctly.')
bu('[App] Application (AO2): use the SPECIFIC business/context in the question '
   '(its name, product, market, numbers, situation).')
bu('[An]  Analysis (AO3): build cause-and-effect chains - push each point to '
   'its final effect on the business.')
bu('[Ev]  Evaluation (AO4): make and justify a judgement. Needed ONLY on 12 '
   '(and higher) mark questions.')

h2('2. Match your effort to the marks')
p('The tariff tells you how much to write and which skills are tested:')
bu('2 marks - Define / State - [K] only. One or two sentences. ~3 min.')
bu('3 marks - Define / State / Identify - [K] (+ small [App]). Definition plus '
   'a short example. ~4 min.')
bu('5 marks - Explain - [K] + [App] + a little [An]. Point, define, apply, '
   'develop ONE step. ~6 min.')
bu('8 marks - Analyse - [K] + [App] + [An]. Two developed chains, NO judgement. '
   '~10 min.')
bu('12 marks - Evaluate / Discuss / Recommend / To what extent - [K] + [App] + '
   '[An] + [Ev]. Two chains PLUS a weighed judgement. ~15 min.')
p('Rough timing rule: about 1 to 1.5 minutes per mark. Never leave a '
  '12-marker unfinished to over-write a 3-marker.')

h2('3. Command words - what each one is really asking')
bu('State / Identify / Give / What is meant by - just name it or define it. '
   'Knowledge only.')
bu('Define - give a precise meaning using the exact key words.')
bu('Explain - give a reason AND develop it one step, applied to the business.')
bu('Analyse - build full cause-and-effect chains. No opinion, no judgement.')
bu('Evaluate / Discuss / Assess / To what extent / Recommend - argue BOTH '
   'sides in chains, then give a justified judgement.')

h2('4. WHERE to put the K and the APP (the golden order)')
p('For any developed answer (5, 8 or 12 marks) write each paragraph in this '
  'fixed order. This guarantees you hit each skill in turn:')
bu('STEP 1 - [K] first: state your point and DEFINE the key term. '
   'Example opener: "One benefit is X, which means [definition]."')
bu('STEP 2 - [App] next: immediately tie it to THIS business. '
   'Example opener: "In the case of [business name], which [context from '
   'the case]..."')
bu('STEP 3 - [An] next: develop the chain. '
   'Use: "this means... because... which leads to... therefore..." until you '
   'reach profit, cost, cash flow or competitiveness.')
bu('STEP 4 - [Ev] last (12 marks only): stand back and judge - which side '
   'wins, why, and what it depends on.')
p('Memory hook: DEFINE it (K) -> LOCATE it in the business (APP) -> DEVELOP it '
  '(AN) -> DECIDE (EV).')

# =====================================================================
h1('PART B - LAYOUT AND EXAMPLES BY MARK TARIFF')
# =====================================================================

# ---------------- 2 MARK ----------------
h2('5. The 2-mark answer - "Define / State"')
p('Tests: [K] only. A precise definition made of TWO parts, OR two clearly '
  'stated items (1 mark each). One or two sentences.')
h3('Structure')
bu('Define: "[Term] is [part 1] [K] which [part 2] [K]."')
bu('State two: "Two [items] are [item 1] [K] and [item 2] [K]."')
h3('Key words to write')
bu('"is defined as...", "refers to...", "is when...", "Two examples are... '
   'and...".')
h3('Ask yourself')
bu('Have I given TWO precise elements (or two items)?')
bu('Have I used the exact syllabus term?')
bu('Have I resisted wasting time on examples or explanation (no marks here)?')
h3('Worked examples')
p('(a) "Define opportunity cost" [2]: Opportunity cost is the benefit of the '
  'next best alternative [K] that is given up when a choice is made [K].')
p('(b) "State two factors of production" [2]: Two factors of production are '
  'land [K] and labour [K].')
p('(c) "Define market segmentation" [2]: Market segmentation is dividing a '
  'market into distinct groups of customers [K] who share similar '
  'characteristics or needs [K].')

# ---------------- 3 MARK ----------------
h2('6. The 3-mark answer - "Define / State (+ example)"')
p('Tests: [K] (+ a small [App]). A precise definition (2 marks) PLUS a short '
  'example or expansion (1 mark).')
h3('Structure')
bu('"[Term] is [clear precise definition] [K][K]. For example, [quick '
   'example] [App]."')
h3('Key words to write')
bu('"...is the difference between...", "...is the amount by which...", '
   '"For example...", "such as...".')
h3('Ask yourself')
bu('Is my definition precise and made of two parts?')
bu('Have I added ONE relevant example or piece of extra detail?')
bu('Have I still kept it short (no chains, no consequences)?')
h3('Worked examples')
p('(a) "Define added value" [3]: Added value is the difference between the '
  'selling price of a product and the cost of the bought-in materials used to '
  'make it [K][K]. For example, a coffee shop buying beans for $0.30 and '
  'selling a coffee for $3.00 adds $2.70 of value [App].')
p('(b) "Define productivity" [3]: Productivity is a measure of the output '
  'produced per unit of input, such as per worker, in a period [K][K]. For '
  'example, output per employee = total output / number of employees [App].')
p('(c) "Define limited liability" [3]: Limited liability means the owners are '
  'only responsible for business debts up to the amount they invested [K][K], '
  'so a shareholder who buys $500 of shares can lose at most $500 [App].')

# ---------------- 5 MARK ----------------
h2('7. The 5-mark answer - "Explain"')
p('Tests: [K] + [App] + one step of [An]. Point -> define [K] -> apply to the '
  'business [App] -> develop ONE consequence [An].')
h3('Structure')
bu('"One [benefit/reason] is [point], which means [define] [K]. For '
   '[business/context] this [apply] [App], so [one consequence] [An]."')
bu('If it says "Explain two...", write two shorter versions (~2-3 marks each).')
h3('Key words to write')
bu('"One reason is...", "which means...", "In the case of [business]...", '
   '"this means that...", "so...", "as a result...".')
h3('Ask yourself')
bu('Have I clearly stated and DEFINED my point (K)?')
bu('Have I linked it to THIS business, not businesses in general (App)?')
bu('Have I developed at least one consequence (An)?')
bu('Have I avoided writing a full evaluation (not needed)?')
h3('Worked examples')
p('(a) "Explain one benefit to a firm of low labour turnover" [5]: One benefit '
  'is a more experienced workforce, as low turnover means fewer staff leave so '
  'skills are retained [K]. For a manufacturer relying on skilled machine '
  'operators [App], this means higher quality and productivity [An] and lower '
  'recruitment and training costs [An].')
p('(b) "Explain one limitation of a business plan" [5]: One limitation is that '
  'a business plan relies on forecasts that may prove inaccurate, because it is '
  'based on assumptions about future sales and costs [K]. For a new bakery '
  'predicting demand it cannot yet know [App], if actual sales are far lower '
  'than forecast [An], the plan can give false confidence and lead to poor '
  'decisions, so the firm may run short of cash [An].')
p('(c) "Explain one reason a business holds inventory" [5]: One reason is to '
  'avoid stock-outs, since holding buffer inventory lets production and sales '
  'continue if demand rises or a delivery is late [K]. For a supermarket '
  'selling fast-moving food [App], this means shelves stay full [An], so it '
  'keeps customers and does not lose sales to rivals [An].')

# ---------------- 8 MARK ----------------
h2('8. The 8-mark answer - "Analyse"')
p('Tests: [K] + [App] + [An]. TWO points, each a full chain. NO intro, NO '
  'conclusion, NO judgement.')
h3('Structure (write this twice)')
bu('"One [way/benefit/drawback] is [point] [K]. This means [define] [K]. For '
   '[business/context] this [apply] [App]. As a result [effect 1] [An], which '
   'in turn [effect 2] [An], meaning [final effect on profit/cost/'
   'competitiveness] [An]."')
h3('Key words to write (analysis connectives)')
bu('"this means...", "because...", "which leads to...", "as a result...", '
   '"this in turn...", "therefore...", "ultimately...".')
h3('Ask yourself')
bu('Do I have TWO separate, different points?')
bu('Is each point defined (K) and applied to THIS business (App)?')
bu('Have I pushed each chain to a FINAL effect (profit, cost, cash, '
   'competitiveness) - not stopped at the first consequence?')
bu('Have I correctly written NO judgement (none needed at 8 marks)?')
h3('Worked example 1 - "Analyse two ways business enterprise can help the '
   'development of a country" [8]')
p('Point 1 - Job creation: One way is by creating employment [K]. Enterprise '
  'involves entrepreneurs setting up businesses that combine the factors of '
  'production and must hire workers [K]. In a developing country where '
  'unemployment is high [App], these new businesses employ local people [App]. '
  'As a result more households earn an income [An], so they spend more locally '
  '[An], raising demand for other firms and creating further jobs through a '
  'multiplier effect [An], gradually raising living standards [An].')
p('Point 2 - Higher output and tax revenue: A second way is by increasing '
  'national output (GDP) and tax revenue [K]. As enterprises produce and sell, '
  'they add value and generate profits and wages [K]. In a developing economy '
  '[App] this raises GDP and means firms and workers pay more tax [App]. As a '
  'result the government receives more revenue [An], which it can invest in '
  'infrastructure, education and healthcare [An], improving productivity and '
  'driving further long-term development [An].')
h3('Worked example 2 - "Analyse two benefits to a clothing retailer of market '
   'segmentation" [8]')
p('Point 1 - Better-matched products: One benefit is that segmentation lets '
  'the retailer target groups with similar needs [K]. In the case of a fashion '
  'chain splitting its market by age and income [App], it can design ranges '
  'that fit each group precisely [An], so customers are more satisfied and buy '
  'more [An], raising sales revenue [An].')
p('Point 2 - Less wasted marketing spend: A second benefit is more efficient '
  'promotion, because messages are aimed only at the relevant segment [K]. For '
  'the retailer advertising a teen range on social media rather than on TV '
  '[App], less money is spent reaching people who will not buy [An], so the '
  'cost per sale falls [An] and profit margins improve [An].')
h3('Worked example 3 - "Analyse two ways a business could improve its cash '
   'flow" [8]')
p('Point 1 - Chase trade receivables faster: One way is to shorten the credit '
  'period given to customers [K], since cash owed is collected sooner [K]. For '
  'a wholesaler waiting 60 days for payment [App], cutting this to 30 days '
  'brings cash in earlier [An], so it has enough cash to pay wages and '
  'suppliers on time [An], reducing the risk of insolvency [An].')
p('Point 2 - Negotiate longer credit from suppliers: A second way is to delay '
  'paying trade payables [K], keeping cash in the business for longer [K]. For '
  'the same wholesaler [App], paying suppliers after 60 rather than 30 days '
  'improves the net cash position each month [An], so it can fund day-to-day '
  'costs without an expensive overdraft [An], lowering interest costs [An].')
p('Reminder: an 8-mark "Analyse" question does NOT need a judgement.')

# ---------------- 12 MARK ----------------
h2('9. The 12-mark answer - "Evaluate / Discuss / Recommend"')
p('Tests: [K] + [App] + [An] + [Ev]. Argument FOR as a full chain, argument '
  'AGAINST (or an alternative) as a full chain, then the JUDGEMENT - where the '
  'top marks are.')
h3('Structure')
bu('(Optional) one-line intro that defines the key term.')
bu('Argument 1 (FOR / benefit) - a full applied chain (like an 8-marker).')
bu('Argument 2 (AGAINST / drawback / alternative) - another full applied '
   'chain.')
bu('Judgement [Ev]: a clear decision; WHY one side outweighs the other (rank '
   'them); an "it depends on..." named factor; a short-term vs long-term '
   'point; and a link back to the specific business.')
h3('Key words to write (judgement starters)')
bu('"Overall, the most important factor is X because..."')
bu('"This depends largely on [named factor]: if [condition] then [choice A], '
   'but if [condition] then [choice B]..."')
bu('"In the short term [effect], but in the long term [effect], so on '
   'balance..."')
bu('"Therefore I recommend X, provided that [condition]."')
h3('Ask yourself')
bu('Have I argued BOTH sides, each as a developed chain (K+App+An)?')
bu('Have I made a CLEAR decision (not "it could go either way")?')
bu('Have I said WHY one side outweighs the other (ranked them)?')
bu('Have I added an "it depends on..." factor and a short vs long term point?')
bu('Have I linked the judgement back to THIS specific business?')
bu('Did I spend about a third of my time on the judgement?')
h3('Worked example 1 - "Intrapreneurship is the most important factor for the '
   'success of a computer games business." Evaluate. [12]')
p('Intro: Intrapreneurship means employees using entrepreneurial skills to '
  'innovate within an existing business [K].')
p('FOR: It is important because success in games depends on constant '
  'innovation [App]. Intrapreneurs create new ideas and features from within '
  '[K/App], so the firm keeps launching fresh titles [An], stays ahead of '
  'fast-moving rivals [An] and earns repeat sales and higher long-term profit '
  '[An].')
p('AGAINST: However, finance and marketing may matter more [K]. Even a great '
  'game needs large sums for long development [App]; without finance it may '
  'never launch [An], so it fails despite good ideas [An]. Equally, in a '
  'crowded market, without marketing customers will not know it exists [App], '
  'meaning low sales even for an excellent game [An].')
p('JUDGEMENT: Overall, intrapreneurship is a major factor but not '
  'automatically THE most important [Ev]. It is necessary but not sufficient - '
  'innovation only creates success if funded and marketed [Ev]. It depends on '
  'the situation [Ev]: for a new studio, securing finance is most critical in '
  'the short term, whereas for an established studio intrapreneurship is key to '
  'staying competitive long term [Ev]. So the statement is only partly true '
  '[Ev].')
h3('Worked example 2 - "A private limited company should become a public '
   'limited company (Plc)." Evaluate. [12]')
p('FOR: Floating raises large amounts of share capital because shares can be '
  'sold to the public [K/App]. For a firm wanting to expand nationally [App], '
  'this funds new factories and outlets [An], so it can grow faster and gain '
  'economies of scale [An], lowering unit costs and raising profit [An].')
p('AGAINST: However, selling shares to the public dilutes ownership [K]. For '
  'the founding family [App], this risks losing control and even a hostile '
  'takeover [An]; it also brings pressure for short-term dividends and costly '
  'disclosure of accounts [An], which can harm long-term decisions [An].')
p('JUDGEMENT: Whether to float depends mainly on how much finance is needed '
  'and how much control the owners will accept [Ev]. If the expansion is large '
  'and cannot be funded by loans or retained profit, becoming a Plc is '
  'justified [Ev]; but if the owners value control and the sum is modest, a '
  'bank loan is better [Ev]. On balance, for most growing firms the loss of '
  'control outweighs the benefit unless the capital required is very large '
  '[Ev].')
h3('Worked example 3 - "For a new innovative product, penetration pricing is '
   'better than skimming." Evaluate. [12]')
p('FOR penetration: A low launch price attracts price-sensitive buyers quickly '
  '[K]. For a new streaming service entering a crowded market [App], this wins '
  'market share fast [An], builds a large subscriber base and brand awareness '
  '[An], and enables economies of scale [An].')
p('AGAINST (skimming may be better): A high initial price earns a large margin '
  'from customers who want the product first [K]. For a genuinely innovative '
  'tech gadget with few rivals [App], skimming recovers high development costs '
  'quickly [An] and creates a premium image [An], though it risks slow early '
  'sales [An].')
p('JUDGEMENT: The best method depends on the level of competition and how '
  'unique the product is [Ev]. Where rivals are many and the product is easy '
  'to copy, penetration is better to grab share [Ev]; where the product is '
  'truly unique with high development costs, skimming is better in the short '
  'term before rivals enter [Ev]. So penetration is not always better - it '
  'suits crowded markets, not genuinely new innovations [Ev].')

# =====================================================================
h1('PART C - QUICK REFERENCE')
# =====================================================================

h2('10. Analysis connective bank (use these to build chains)')
bu('this means... / this results in... / because... / which leads to...')
bu('as a result... / this in turn... / consequently... / therefore...')
bu('ultimately... / meaning that... (end on profit, cost, cash or '
   'competitiveness).')

h2('11. Evaluation / judgement bank (12-mark answers)')
bu('"The most important factor is... because..."')
bu('"This depends on... (e.g. the size of the firm, its objectives, the state '
   'of the economy, the level of competition)."')
bu('"In the short term... whereas in the long term..."')
bu('"On balance... provided that..."')

h2('12. One-look revision card')
p('2 marks: definition (2 parts) OR two items. [K] yes. No example needed.')
p('3 marks: definition + example. [K] yes, [App] small. No chains.')
p('5 marks: 1 point. [K] + [App] + one [An] step. No intro/conclusion.')
p('8 marks: 2 points. [K] + [App] + 2-3 [An] steps each. No judgement.')
p('12 marks: 2 points + JUDGEMENT. [K] + [App] + [An] + [Ev] essential.')

h2('13. The three biggest mark-losers to avoid')
bu('Not linking to the business in the question - you lose ALL Application '
   'marks.')
bu('Listing many points without developing them - you lose Analysis marks. '
   'Fewer, deeper chains score higher.')
bu('Writing no judgement on a 12-marker - you cap your mark at roughly half.')
sp()
p('Golden rule: DEFINE it (K) -> LOCATE it in the business (APP) -> DEVELOP it '
  '(AN) -> DECIDE (EV). Apply every point to the specific business and justify '
  'every judgement to reach the top mark bands.')

pages = pdfgen.build_pdf(
    B, '/projects/sandbox/Business-AS-level-/AS_Business_9609_Exam_Technique.pdf',
    footer_prefix='Exam Technique - Page')
print('Exam technique PDF:', pages, 'pages')
