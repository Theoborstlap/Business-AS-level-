# -*- coding: utf-8 -*-
"""Builds AS_Business_9609_Analysis_Chains.pdf into the repo folder.

A bank of ready-to-use ANALYSIS chains for the 9609 exam. Each chain is written
in the exam format: point (+ definition) -> apply -> develop links -> final
effect on the business. Deploy these to turn a point into full Analysis marks.
"""
import pdfgen

B = []
def p(t): B.append(('body', t))
def bu(t): B.append(('bullet', t))
def h1(t): B.append(('h1', t))
def h2(t): B.append(('h2', t))
def h3(t): B.append(('h3', t))
def sp(): B.append(('spacer', ''))

B.append(('title', 'AS Business 9609 - Analysis Chains'))
p('A bank of ready-to-use cause-and-effect chains for building Analysis (AO3) marks. '
  'For the Oct/Nov 2026 exam (syllabus 2026-2028). Use with the Exam Technique guide.')
sp()

# ---------------- HOW ANALYSIS WORKS ----------------
h1('1. What an analysis chain is')
p('Analysis [An] is developed reasoning. You take one point and push it, link by link, '
  'until it reaches a final effect on the business. Each "link" is a consequence of the one before. '
  'A single undeveloped point earns Knowledge only; the CHAIN of links is what earns the Analysis marks.')
p('The full exam sentence has this shape:')
p('Point + definition [K] -> link to the actual business [App] -> which means... -> so... -> as a result... [An] '
  '(-> on balance / it depends... [Ev] on 12-mark questions only).')
p('Where to put each mark: K goes first (define), App goes second (name the business), '
  'and every "so.../which means..." link after that is An.')

h1('2. The connective toolkit (the words that build a chain)')
p('String your links together with these. Using them forces you to develop, not just list:')
bu('which means... / this means that...')
bu('so... / therefore... / as a result... / consequently...')
bu('this leads to... / this in turn...')
bu('ultimately... / which finally... (use to reach the destination)')
p('Rule of thumb: aim for at least 2-3 links per point before you stop. If you have not reached '
  'one of the destinations below, the chain is not finished.')

h1('3. The destinations - always end on one of these')
p('Every chain must arrive at a measurable business effect. If your point does not reach one of these, keep going:')
bu('Higher / lower REVENUE or SALES volume')
bu('Higher / lower COSTS (or unit/average cost)')
bu('Higher / lower PROFIT or profit margin')
bu('Improved / worse CASH FLOW')
bu('Higher / lower MARKET SHARE or COMPETITIVENESS')
bu('Higher / lower PRODUCTIVITY, motivation or labour turnover')
bu('Greater / lower chance of SURVIVAL or growth')

# ---------------- PEOPLE ----------------
h1('4. People in organisations - chains')
h3('Financial motivation (performance bonus / piece rate)')
bu('A performance bonus [K] -> workers can earn more by producing more -> they see extra effort is '
   'rewarded (Taylor) -> motivation and effort rise -> output per worker (productivity) increases -> '
   'unit labour costs fall and orders are met faster -> higher profit and competitiveness [An].')
h3('Training')
bu('Training gives employees new skills [K] -> they make fewer mistakes and work faster -> quality and '
   'productivity rise -> less waste and reworking -> lower costs and a better reputation -> higher profit [An].')
h3('Empowerment / job enrichment (Maslow, Herzberg)')
bu('Giving workers more responsibility [K] -> meets esteem/self-actualisation needs (Maslow) and acts as a '
   'motivator (Herzberg) -> job satisfaction rises -> labour turnover and absenteeism fall -> lower '
   'recruitment/training costs and experience is retained -> higher productivity and profit [An].')
h3('Poor motivation (the negative chain)')
bu('Low pay and no recognition [K] -> workers feel undervalued (unmet esteem needs) -> motivation falls -> '
   'absenteeism and labour turnover rise -> production is disrupted and recruitment costs rise -> lower '
   'productivity and profit [An].')
h3('Democratic leadership')
bu('A democratic style [K] -> employees are consulted on decisions -> they feel valued and share ideas -> '
   'motivation and commitment rise -> lower turnover and better-quality decisions -> higher productivity [An]. '
   '(Counter-link: consulting takes time -> slower decisions -> slower response to market changes.)')
h3('Delayering / organisational structure')
bu('Removing a layer of management [K] -> a shorter chain of command and lower salary costs -> communication '
   'is faster and overheads fall -> quicker decisions and lower costs -> more competitive and profitable [An]. '
   '(Counter-link: wider span of control -> managers stretched -> less support for staff.)')

# ---------------- MARKETING ----------------
h1('5. Marketing - chains')
h3('Market research')
bu('Primary market research [K] -> the business gathers data on real customer needs -> the product is designed '
   'to match what customers want -> fewer failed launches and higher sales -> higher revenue and less wasted '
   'marketing spend [An].')
h3('Market segmentation')
bu('Segmenting the market [K] -> the firm targets each group with a tailored product and message -> less '
   'marketing is wasted and each group finds products that fit -> higher sales and stronger loyalty -> higher '
   'revenue [An].')
h3('Advertising / promotion')
bu('Advertising [K] -> raises awareness and improves brand image -> the demand curve shifts right (more sold at '
   'each price) -> sales volume rises -> if extra revenue exceeds the advertising cost -> higher profit [An].')
h3('Price elasticity of demand')
bu('The product is price-INELASTIC (few substitutes) [K] -> raising the price -> quantity demanded falls by a '
   'smaller % than the price rise -> total revenue rises [An]. (For an ELASTIC good the opposite holds: a price '
   'rise -> a larger % fall in quantity -> revenue falls.)')
h3('Penetration pricing / price skimming')
bu('Penetration pricing (low launch price) [K] -> attracts price-sensitive customers from rivals -> market share '
   'is built quickly -> higher sales volume spreads fixed costs -> lower unit cost and word-of-mouth growth [An].')
bu('Price skimming (high launch price for a new product) [K] -> early adopters pay a premium -> high revenue per '
   'unit -> R&D costs are recovered quickly -> funds reinvestment [An].')
h3('Unique selling point / differentiation')
bu('A clear USP [K] -> the product stands out from rivals -> customers become more brand loyal and less '
   'price-sensitive -> the firm can charge a premium and keep customers -> higher margins and revenue [An].')

# ---------------- OPERATIONS ----------------
h1('6. Operations management - chains')
h3('Economies of scale')
bu('Producing on a larger scale [K] -> fixed costs are spread over more units and bulk-buying earns discounts -> '
   'average (unit) cost falls -> the firm can cut price or widen its margin -> more competitive and more '
   'profitable [An].')
h3('Just-in-time (JIT) inventory')
bu('JIT holds little or no stock [K] -> storage, insurance and capital tied up in inventory all fall -> lower '
   'costs and improved cash flow -> higher profit [An]. (Counter-link: no buffer stock -> one supplier delay -> '
   'production halts and orders are missed.)')
h3('Quality management / TQM')
bu('Improving quality [K] -> fewer defects, returns and reworking + a stronger reputation -> lower waste costs '
   'and more repeat custom -> higher sales and profit [An].')
h3('Automation / capital-intensive production')
bu('Investing in machinery [K] -> output is produced faster and more consistently -> productivity and quality rise '
   'and labour cost per unit falls -> lower unit costs -> more competitive [An]. (Counter-link: high fixed cost -> '
   'break-even output rises -> risky if demand is low.)')

# ---------------- FINANCE ----------------
h1('7. Finance and accounting - chains')
h3('Bank loan')
bu('A bank loan [K] -> provides a large lump sum while the owner keeps control -> the firm can buy assets now and '
   'spread repayments over years -> capacity and sales rise with manageable cash flow -> higher profit [An]. '
   '(Counter-link: fixed interest must be paid whether or not sales rise -> break-even and risk rise.)')
h3('Retained profit')
bu('Using retained profit [K] -> no interest and no loss of control -> cheaper than borrowing with no repayment '
   'pressure -> expansion is funded while cash flow is protected -> lower risk [An]. (Counter-link: opportunity '
   'cost -> less available for dividends or reserves.)')
h3('Break-even and margin of safety')
bu('Cutting fixed costs [K] -> the break-even output falls -> the firm becomes profitable at a lower level of '
   'sales and its margin of safety widens -> lower risk of making a loss [An].')
h3('Cash-flow management')
bu('Negotiating longer credit terms with suppliers [K] -> cash stays in the business for longer -> cash flow '
   'improves -> wages and bills can be paid on time -> the firm avoids insolvency [An].')

# ---------------- ENVIRONMENT ----------------
h1('8. Business and its environment - chains')
h3('Recession')
bu('A recession [K] -> consumer incomes and confidence fall -> demand for luxury/income-elastic goods falls -> '
   'sales revenue drops -> the firm may cut costs or staff -> survival is threatened [An].')
h3('Exchange rate (a weaker domestic currency)')
bu('The domestic currency weakens [K] -> exports become cheaper for overseas buyers -> foreign demand rises -> '
   'export sales and revenue increase for an exporter [An]. (Counter-link: imported raw materials become dearer '
   '-> input costs rise.)')
h3('Interest rate rise')
bu('Interest rates rise [K] -> borrowing costs increase and consumers have less disposable income -> demand '
   'falls while the firm\'s loan repayments rise -> lower sales and higher costs -> lower profit [An].')
h3('Minimum wage / legislation')
bu('A minimum-wage rise [K] -> labour costs increase -> unit costs rise -> the firm must accept lower margins or '
   'raise prices -> less competitive or lower profit [An]. (Counter-link: higher pay -> better motivation and '
   'lower turnover.)')
h3('Limited liability (becoming a private limited company)')
bu('Becoming a private limited company [K] -> shareholders gain limited liability -> personal assets are '
   'protected and capital is easier to raise by selling shares -> growth can be funded with less personal risk '
   '[An]. (Counter-link: more legal/admin requirements and profits shared.)')

# ---------------- BUILD YOUR OWN ----------------
h1('9. Build your own chain (fill in the blanks)')
p('Use this skeleton for any point in any topic. Never stop before the final effect:')
p('[Name the point] is [define it] [K]. For [the business in the question] [App], this means that ______, '
  'so ______, which as a result ______, ultimately leading to [higher/lower profit, sales, costs, cash flow, '
  'market share, productivity or survival] [An].')
sp()
p('For a 12-mark question, add a judgement afterwards: On balance this ______ is/ is not worthwhile because '
  '______; however it depends on ______, and in the short term ______ while in the long term ______ [Ev].')

# ---------------- MISTAKES ----------------
h1('10. The three chain mistakes to avoid')
bu('Stopping too early - ending on "so sales rise" without the final effect (e.g. on profit or survival). Add the last link.')
bu('Listing instead of linking - writing separate facts with no "so/which means" between them earns Knowledge, not Analysis.')
bu('No application - a chain that never names the actual business loses the Application marks even if the reasoning is good.')
sp()
p('Learn a few chains per topic and adapt the wording to the business in front of you. Depth beats breadth: '
  'two fully developed chains score higher than five half-finished ones.')

pages = pdfgen.build_pdf(B, 'AS_Business_9609_Analysis_Chains.pdf',
                         footer_prefix='AS Business 9609 - Analysis Chains - Page')
print('Analysis chains PDF: %d pages' % pages)
