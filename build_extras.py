# -*- coding: utf-8 -*-
"""Generates the extra 9609 study materials:
   - Calculation Drills (+ answers)
   - Past-paper-style Case Studies (+ answers)
   - Topic-by-topic Mini-Tests (+ answers)
All ASCII only. Uses pdfgen.build_pdf.
"""
import pdfgen


def mk(blocks):
    """helper: returns a fresh list wrapper with builder funcs bound to it."""
    B = blocks
    return (lambda t: B.append(('body', t)),
            lambda t: B.append(('bullet', t)),
            lambda t: B.append(('h1', t)),
            lambda t: B.append(('h2', t)),
            lambda t: B.append(('h3', t)),
            lambda: B.append(('spacer', '')))


# ===========================================================================
# 1) CALCULATION DRILLS
# ===========================================================================
CD = []
p, b, h1, h2, h3, sp = mk(CD)
CD.append(('title', 'AS Business 9609 - Calculation Drills'))
p('Every quantitative skill in the AS syllabus, with repeated practice. '
  'Show all working and always state units ($, %, units). Worked answers are '
  'in the separate Calculation Drills - Answers booklet.')
sp()

h1('A. Added value  (selling price - bought-in material cost)')
p('A1. A bakery buys ingredients for $2 per loaf and sells each loaf for $5. Calculate the added value per loaf.')
p('A2. A furniture maker buys $120 of materials per table and sells each table for $450. Calculate added value per table and total added value on 30 tables.')
p('A3. A phone case costs $1.20 in materials and sells for $9.99. State the added value per case.')

h1('B. Labour turnover  ((staff leaving / average staff) x 100)')
p('B1. 24 staff left during the year; average staff employed was 160. Calculate labour turnover.')
p('B2. A firm employs on average 480 people and 36 left last year. Calculate labour turnover.')
p('B3. Labour turnover is 15% and average staff is 200. How many staff left?')

h1('C. Labour productivity  (total output / number of employees)')
p('C1. 18,000 units are produced by 45 workers. Calculate output per worker.')
p('C2. A team of 12 assembles 3,600 units per week. Calculate weekly productivity per worker.')
p('C3. Productivity is 250 units per worker and there are 60 workers. Calculate total output.')

h1('D. Market share  ((firm sales / total market sales) x 100)')
p('D1. A firm sells $6m in a market worth $48m. Calculate its market share.')
p('D2. Total market sales are 500,000 units; the firm sells 90,000 units. Calculate market share.')
p('D3. A firm has 12% share of a $250m market. Calculate its sales revenue.')

h1('E. Market growth  ((change in market size / original size) x 100)')
p('E1. A market grew from $80m to $92m. Calculate market growth.')
p('E2. Market size fell from 400,000 to 360,000 units. Calculate the growth rate (state if negative).')
p('E3. A $150m market grows by 8%. Calculate the new market size.')

h1('F. Capacity utilisation  ((actual output / maximum output) x 100)')
p('F1. Maximum output is 5,000 units; actual output is 3,750. Calculate capacity utilisation.')
p('F2. A cinema has 250 seats; on average 175 are filled. Calculate capacity utilisation.')
p('F3. A factory runs at 90% utilisation with maximum capacity of 20,000 units. Calculate actual output.')

h1('G. Working capital  (current assets - current liabilities)')
p('G1. Current assets $90,000; current liabilities $62,000. Calculate working capital.')
p('G2. Current assets $45,000; current liabilities $51,000. Calculate working capital and comment.')

h1('H. Total cost & average cost')
p('H1. Fixed costs $30,000; variable cost per unit $4; output 6,000 units. Calculate total variable cost, total cost and average cost per unit.')
p('H2. Fixed costs $18,000; variable cost per unit $7; output 3,000 units. Calculate total cost and average cost.')

h1('I. Cash flow  (net cash flow; closing = opening + net)')
p('I1. Opening balance $8,000; inflows $30,000; outflows $34,000. Calculate net cash flow and closing balance.')
p('I2. A firm has these months. Jan: open $2,000, inflow $18,000, outflow $15,000. Feb: inflow $16,000, outflow $20,000. Calculate the closing balance for Jan and for Feb.')

h1('J. Contribution, total contribution & profit')
p('J1. Selling price $25; variable cost per unit $10. Calculate contribution per unit.')
p('J2. Contribution per unit $15; units sold 4,000; fixed costs $40,000. Calculate total contribution and profit.')
p('J3. Selling price $12, variable cost $7, fixed costs $25,000, units sold 7,000. Calculate profit.')

h1('K. Break-even, margin of safety & target profit')
p('K1. Fixed costs $60,000; selling price $30; variable cost $18. Calculate contribution per unit and break-even output.')
p('K2. Using K1, current output is 7,000 units. Calculate the margin of safety and the profit at that output.')
p('K3. Fixed costs $45,000; selling price $20; variable cost $11. How many units must be sold to make a target profit of $18,000?')

h1('L. Variances  (actual - budget; state favourable/adverse)')
p('L1. Budgeted revenue $80,000; actual revenue $86,000. Calculate the variance and state its type.')
p('L2. Budgeted costs $50,000; actual costs $57,000. Calculate the variance and state its type.')
p('L3. Budgeted profit $30,000; actual profit $26,000. Calculate the profit variance and state its type.')
sp()
CD.append(('body', 'END OF DRILLS - work them without a calculator first, then check.'))

# ---- Calculation Drills ANSWERS ----
CDA = []
p, b, h1, h2, h3, sp = mk(CDA)
CDA.append(('title', 'Calculation Drills - Answers'))
p('Full working shown. Marks in a real exam are given for method as well as the final answer, so always show your steps.')
sp()
h1('A. Added value')
p('A1. 5 - 2 = $3 per loaf.')
p('A2. 450 - 120 = $330 per table; total = 330 x 30 = $9,900.')
p('A3. 9.99 - 1.20 = $8.79 per case.')
h1('B. Labour turnover')
p('B1. (24/160) x 100 = 15%.')
p('B2. (36/480) x 100 = 7.5%.')
p('B3. 15% of 200 = 30 staff left.')
h1('C. Labour productivity')
p('C1. 18,000/45 = 400 units per worker.')
p('C2. 3,600/12 = 300 units per worker per week.')
p('C3. 250 x 60 = 15,000 units.')
h1('D. Market share')
p('D1. (6/48) x 100 = 12.5%.')
p('D2. (90,000/500,000) x 100 = 18%.')
p('D3. 12% of $250m = $30m.')
h1('E. Market growth')
p('E1. ((92-80)/80) x 100 = 15%.')
p('E2. ((360,000-400,000)/400,000) x 100 = -10% (a 10% fall).')
p('E3. 150m x 1.08 = $162m.')
h1('F. Capacity utilisation')
p('F1. (3,750/5,000) x 100 = 75%.')
p('F2. (175/250) x 100 = 70%.')
p('F3. 90% of 20,000 = 18,000 units.')
h1('G. Working capital')
p('G1. 90,000 - 62,000 = $28,000 (positive - can meet short-term debts).')
p('G2. 45,000 - 51,000 = -$6,000 (negative - a liquidity problem; may struggle to pay bills).')
h1('H. Total & average cost')
p('H1. Total variable cost = 4 x 6,000 = $24,000. Total cost = 30,000 + 24,000 = $54,000. Average cost = 54,000/6,000 = $9 per unit.')
p('H2. Total cost = 18,000 + (7 x 3,000) = 18,000 + 21,000 = $39,000. Average cost = 39,000/3,000 = $13 per unit.')
h1('I. Cash flow')
p('I1. Net cash flow = 30,000 - 34,000 = -$4,000. Closing = 8,000 + (-4,000) = $4,000.')
p('I2. Jan: net = 18,000 - 15,000 = +3,000; closing = 2,000 + 3,000 = $5,000. Feb: opening = $5,000; net = 16,000 - 20,000 = -4,000; closing = 5,000 - 4,000 = $1,000.')
h1('J. Contribution & profit')
p('J1. 25 - 10 = $15 per unit.')
p('J2. Total contribution = 15 x 4,000 = $60,000. Profit = 60,000 - 40,000 = $20,000.')
p('J3. Contribution = 12 - 7 = $5. Total = 5 x 7,000 = $35,000. Profit = 35,000 - 25,000 = $10,000.')
h1('K. Break-even & margin of safety')
p('K1. Contribution = 30 - 18 = $12. Break-even = 60,000/12 = 5,000 units.')
p('K2. Margin of safety = 7,000 - 5,000 = 2,000 units. Profit = (12 x 7,000) - 60,000 = 84,000 - 60,000 = $24,000.')
p('K3. Contribution = 20 - 11 = $9. Units for target profit = (fixed costs + target profit)/contribution = (45,000 + 18,000)/9 = 63,000/9 = 7,000 units.')
h1('L. Variances')
p('L1. 86,000 - 80,000 = +$6,000 FAVOURABLE (revenue above budget).')
p('L2. 57,000 - 50,000 = $7,000 higher costs = ADVERSE.')
p('L3. 26,000 - 30,000 = -$4,000 ADVERSE (profit below budget).')

# ===========================================================================
# 2) CASE STUDIES (past-paper style)
# ===========================================================================
CS = []
p, b, h1, h2, h3, sp = mk(CS)
CS.append(('title', 'AS Business 9609 - Case Study Practice'))
p('Five data-response case studies in exam style, one per AS topic. Each builds '
  'from short knowledge questions to an extended evaluation. Suggested timing: '
  'about 1.25 minutes per mark. Model answers are in the separate booklet.')
sp()

h1('Case Study 1: Amara\'s Kitchen (Topic 1)')
p('Amara runs Amara\'s Kitchen (AK), a vegan street-food business, as a sole trader. '
  'Demand has grown fast and she now wants to open three more outlets. She is '
  'considering forming a private limited company (Ltd) and is also being offered the '
  'chance to expand by selling franchises. Amara worries about losing control and '
  'about the unlimited liability she currently faces. Her main objective has changed '
  'from survival to growth.')
p('(a) Define "unlimited liability". [2]')
p('(b) Explain one benefit to Amara of forming a private limited company. [3]')
p('(c) Analyse two factors AK should consider before opening more outlets. [8]')
p('(d) Amara wants to grow quickly. Recommend whether she should grow by opening her '
  'own outlets (organic growth) or by selling franchises. Justify your answer. [12]')
sp()

h1('Case Study 2: TechNova (Topic 2)')
p('TechNova runs a customer call centre employing an average of 300 staff. Last year '
  '45 employees left. Managers use an autocratic style and pay a low basic wage with '
  'no bonuses. Labour turnover is high, morale is low and absenteeism is rising. A new '
  'HR manager suggests introducing training, team working and empowerment, and warns '
  'that the current style is demotivating skilled workers.')
p('(a) Calculate TechNova\'s labour turnover. [2]')
p('(b) Define "empowerment". [2]')
p('(c) Analyse how non-financial motivators could reduce labour turnover at TechNova. [8]')
p('(d) Evaluate whether changing the management style is the best way to improve '
  'morale at TechNova. [12]')
sp()

h1('Case Study 3: FreshFizz (Topic 3)')
p('FreshFizz makes soft drinks and is launching a new low-sugar drink aimed at health-'
  'conscious young adults. The total market is worth $40m and FreshFizz currently sells '
  '$5m of drinks. The marketing team is deciding between penetration pricing and '
  'skimming, and is unsure whether to spend heavily on primary market research first.')
p('(a) Define "market segmentation". [2]')
p('(b) Calculate FreshFizz\'s current market share. [2]')
p('(c) Analyse the benefits to FreshFizz of carrying out primary market research before the launch. [8]')
p('(d) Recommend the most suitable pricing method for the new drink. Justify your answer. [12]')
sp()

h1('Case Study 4: BuildRight (Topic 4)')
p('BuildRight makes wooden furniture using batch production. Its factory has a maximum '
  'capacity of 8,000 units per month but currently produces 5,200. Demand is rising and '
  'managers are considering switching to flow production and adopting Just-in-Time (JIT) '
  'inventory. Some managers worry about reliability of suppliers and the cost of new '
  'machinery.')
p('(a) Calculate BuildRight\'s capacity utilisation. [2]')
p('(b) Define "lead time". [2]')
p('(c) Analyse the benefits to BuildRight of adopting JIT inventory management. [8]')
p('(d) Evaluate whether BuildRight should switch from batch to flow production. [12]')
sp()

h1('Case Study 5: GreenGro (Topic 5)')
p('GreenGro sells garden products. Each unit sells for $40 and has a variable cost of '
  '$24. Fixed costs are $96,000 per year. The owner wants to expand and needs finance. '
  'In January the business expects an opening balance of $10,000, cash inflows of '
  '$60,000 and cash outflows of $68,000. The owner is deciding between a bank loan and '
  'issuing new shares to a partner.')
p('(a) Calculate the contribution per unit and the break-even level of output. [4]')
p('(b) Calculate the net cash flow and closing balance for January. [4]')
p('(c) Analyse two suitable sources of finance for GreenGro\'s expansion. [8]')
p('(d) Evaluate the usefulness of break-even analysis to the owner of GreenGro. [12]')
sp()
CS.append(('body', 'END OF CASE STUDIES.'))

# ---- Case Studies ANSWERS ----
CSA = []
p, b, h1, h2, h3, sp = mk(CSA)
CSA.append(('title', 'Case Study Practice - Answers'))
p('Indicative content and mark guidance. Parts (c) need developed analysis chains '
  '(point - because - leads to - therefore) applied to the business; parts (d) need a '
  'clear, justified judgement/recommendation.')
sp()
h1('Case Study 1: Amara\'s Kitchen')
p('(a) Unlimited liability = the owner is personally responsible for all business debts; '
  'personal assets can be used to pay them. [2]')
p('(b) Any one, developed: limited liability protects Amara\'s personal savings if AK '
  'fails; OR easier to raise capital to fund the three new outlets; OR greater status/'
  'credibility with suppliers and lenders. [3]')
p('(c) Two factors developed, e.g.: (i) FINANCE - opening outlets needs large capital; '
  'if funded by debt, interest and repayments strain cash flow and risk insolvency. '
  '(ii) MANAGEMENT/QUALITY CONTROL - Amara cannot be everywhere; poor staff could '
  'damage the brand she built. Also demand reliability, location, competition. [8]')
p('(d) Organic (own outlets): keeps full control and all profit, protects the brand, but '
  'is slow and needs a lot of her own capital. Franchising: rapid growth funded by '
  'franchisees\' money, less capital/risk for Amara, but less control over quality and '
  'she shares profit (royalties). Judgement: if speed and limited capital matter most, '
  'franchising fits her growth objective, PROVIDED she can enforce quality standards; '
  'if protecting the brand is paramount, organic growth is safer. State which and why. [12]')
h1('Case Study 2: TechNova')
p('(a) (45/300) x 100 = 15%. [2]')
p('(b) Empowerment = giving employees greater control and authority over their own work/'
  'decisions. [2]')
p('(c) Chains, e.g.: training raises skills and confidence -> staff feel valued and cope '
  'better -> higher job satisfaction -> fewer leave. Team working meets social needs '
  '(Mayo) -> belonging -> lower turnover. Empowerment gives responsibility (Herzberg '
  'motivator/Maslow esteem) -> motivation -> retention. Link to lower recruitment/'
  'training costs. [8]')
p('(d) Changing from autocratic to a more democratic/paternalistic style could raise '
  'morale by involving staff and meeting higher needs, BUT low pay is also a cause '
  '(Herzberg hygiene factor) so style change alone may not fix dissatisfaction; training '
  'and better pay may be needed too. Judgement: style change helps but is unlikely to be '
  'sufficient on its own - a combination is best. [12]')
h1('Case Study 3: FreshFizz')
p('(a) Market segmentation = dividing a market into groups of customers with similar '
  'characteristics/needs. [2]')
p('(b) (5/40) x 100 = 12.5%. [2]')
p('(c) Primary research gives up-to-date, specific data on what health-conscious young '
  'adults want -> better product/price decisions -> lower risk of launch failure -> less '
  'wasted marketing spend -> higher chance of sales. Note cost/time as a balancing point. [8]')
p('(d) Penetration (low price) wins share fast in a competitive drinks market and '
  'encourages trial, but earns low margins. Skimming (high price) suits a distinctive/'
  'premium health product and recovers development costs, but risks low volume and rival '
  'entry. Judgement: because it is a new entrant with only 12.5% share in a mass market, '
  'penetration is likely better to build share and awareness - unless the drink is truly '
  'unique, when skimming fits. Justify choice. [12]')
h1('Case Study 4: BuildRight')
p('(a) (5,200/8,000) x 100 = 65%. [2]')
p('(b) Lead time = the time between placing an order for inventory and receiving it. [2]')
p('(c) JIT reduces inventory held -> lower storage costs and less capital tied up -> '
  'improved cash flow; less waste/obsolescence of materials. But note dependence on '
  'reliable suppliers as the balancing analysis. [8]')
p('(d) Flow production: lower unit costs, faster output to meet rising demand, economies '
  'of scale, BUT high machinery cost, inflexible (harder to make varied/custom furniture), '
  'disruption and possible redundancies during changeover, and only worthwhile if demand '
  'is high and steady. Judgement: switch only if demand is large and standardised enough '
  'to justify the investment; otherwise batch keeps flexibility. [12]')
h1('Case Study 5: GreenGro')
p('(a) Contribution per unit = 40 - 24 = $16. Break-even = 96,000/16 = 6,000 units. [4]')
p('(b) Net cash flow = 60,000 - 68,000 = -$8,000. Closing balance = 10,000 - 8,000 = $2,000. [4]')
p('(c) Two sources developed, e.g.: bank loan - large lump sum, control kept, but interest '
  'and repayments strain cash flow (already tight per part b). New partner/share capital - '
  'raises funds without repayment/interest, shares risk, BUT dilutes control and profit. '
  'Match to the situation. [8]')
p('(d) Break-even shows the 6,000-unit target, the margin of safety and the effect of '
  'price/cost changes - useful for planning and persuading lenders. BUT it assumes all '
  'output is sold and constant costs/price, ignores market changes, and is only as good '
  'as the estimates used. Judgement: a useful planning guide for the owner but should not '
  'be relied on alone. [12]')

# ===========================================================================
# 3) TOPIC MINI-TESTS
# ===========================================================================
MT = []
p, b, h1, h2, h3, sp = mk(MT)
MT.append(('title', 'AS Business 9609 - Topic Mini-Tests'))
p('Five short timed self-tests, one per AS topic (about 15 minutes each). Great for '
  'quick recall before the exam. Answers are in the separate booklet.')
sp()

h1('Mini-Test 1: Business and its Environment')
p('1. State the four factors of production. [4]')
p('2. Give the formula for added value. [1]')
p('3. Define opportunity cost. [2]')
p('4. Name the four economic sectors. [4]')
p('5. Distinguish between limited and unlimited liability. [2]')
p('6. Give two advantages of a franchise to the franchisee. [2]')
p('7. Name the four types of integration (external growth). [4]')
p('8. What do the letters SMART stand for? [5]')
p('9. Give two internal and two external stakeholders. [4]')
p('10. State the three parts of the triple bottom line. [3]')
sp()

h1('Mini-Test 2: Human Resource Management')
p('1. Give the labour turnover formula. [1]')
p('2. Distinguish between a job description and a person specification. [2]')
p('3. Distinguish between redundancy and dismissal. [2]')
p('4. Name the three types of training. [3]')
p('5. State the five levels of Maslow\'s hierarchy (in order). [5]')
p('6. In Herzberg\'s theory, name two hygiene factors and two motivators. [4]')
p('7. Give Vroom\'s expectancy equation (the three parts). [3]')
p('8. Name four payment (financial motivator) methods. [4]')
p('9. Name the four management styles. [4]')
p('10. State the difference between McGregor\'s Theory X and Theory Y. [2]')
sp()

h1('Mini-Test 3: Marketing')
p('1. Give the market share formula. [1]')
p('2. Give the market growth formula. [1]')
p('3. Distinguish between product and market orientation. [2]')
p('4. Name the three methods of market segmentation. [3]')
p('5. Distinguish between primary and secondary research. [2]')
p('6. State the 4Ps. [4]')
p('7. Name the stages of the product life cycle. [5]')
p('8. Name the four categories of the Boston Matrix. [4]')
p('9. Define penetration pricing and skimming. [2]')
p('10. Give one benefit of branding in promotion. [1]')
sp()

h1('Mini-Test 4: Operations Management')
p('1. Give the labour productivity formula. [1]')
p('2. Give the capacity utilisation formula. [1]')
p('3. Name the four production methods. [4]')
p('4. Distinguish between capital-intensive and labour-intensive operations. [2]')
p('5. Name the three types of inventory. [3]')
p('6. Define buffer inventory, re-order level and lead time. [3]')
p('7. Distinguish between JIT and JIC. [2]')
p('8. State two problems of operating at 100% capacity. [2]')
p('9. Give two methods of improving capacity utilisation. [2]')
p('10. State one benefit and one drawback of outsourcing. [2]')
sp()

h1('Mini-Test 5: Finance and Accounting')
p('1. Give the working capital formula. [1]')
p('2. Explain the difference between cash and profit. [2]')
p('3. Distinguish between capital and revenue expenditure. [2]')
p('4. Name three internal and three external sources of finance. [6]')
p('5. Give the formula for closing cash balance. [1]')
p('6. Distinguish between fixed and variable costs. [2]')
p('7. Give the contribution per unit and break-even formulas. [2]')
p('8. Define margin of safety. [1]')
p('9. Name the three types of budget. [3]')
p('10. Distinguish between a favourable and an adverse variance. [2]')
sp()
MT.append(('body', 'END OF MINI-TESTS.'))

# ---- Mini-Tests ANSWERS ----
MTA = []
p, b, h1, h2, h3, sp = mk(MTA)
MTA.append(('title', 'Topic Mini-Tests - Answers'))
sp()
h1('Mini-Test 1: Business and its Environment')
p('1. Land, labour, capital, enterprise. 2. Selling price - cost of bought-in materials. '
  '3. The benefit of the next best alternative given up. 4. Primary, secondary, tertiary, '
  'quaternary. 5. Limited = losses limited to amount invested; unlimited = owner personally '
  'liable for all debts. 6. Proven idea/brand recognition; training/support (lower risk). '
  '7. Horizontal, vertical backward, vertical forward, conglomerate. 8. Specific, Measurable, '
  'Achievable, Realistic, Time-limited. 9. Internal: owners, managers, employees. External: '
  'customers, suppliers, government, community. 10. Profit (economic), people (social), '
  'planet (environmental).')
h1('Mini-Test 2: Human Resource Management')
p('1. (Number leaving / average number employed) x 100. 2. Job description = duties/'
  'responsibilities; person specification = skills/qualities of the ideal candidate. '
  '3. Redundancy = job no longer exists (not worker\'s fault); dismissal = ended due to '
  'conduct/performance. 4. Induction, on-the-job, off-the-job. 5. Physiological, safety, '
  'social, esteem, self-actualisation. 6. Hygiene: pay, conditions, supervision, security. '
  'Motivators: achievement, recognition, responsibility, advancement. 7. Motivation = '
  'expectancy x instrumentality x valence. 8. Any four: time-based wage, salary, piece rate, '
  'commission, bonus, profit sharing, PRP, fringe benefits. 9. Autocratic, democratic, '
  'laissez-faire, paternalistic. 10. Theory X assumes staff are lazy and need control; '
  'Theory Y assumes staff enjoy work and seek responsibility.')
h1('Mini-Test 3: Marketing')
p('1. (Firm sales / total market sales) x 100. 2. (Change in market size / original size) '
  'x 100. 3. Product orientation = product-led then find buyers; market orientation = '
  'research needs first then produce. 4. Geographic, demographic, psychographic. 5. Primary '
  '= new first-hand data; secondary = existing data collected by others. 6. Product, Price, '
  'Promotion, Place. 7. Development, introduction, growth, maturity, decline. 8. Star, cash '
  'cow, question mark (problem child), dog. 9. Penetration = low price to enter/gain share; '
  'skimming = high initial price then lower. 10. Recognition/loyalty/premium price/'
  'differentiation (any one).')
h1('Mini-Test 4: Operations Management')
p('1. Total output / number of employees. 2. (Actual output / maximum output) x 100. '
  '3. Job, batch, flow, mass customisation. 4. Capital-intensive relies mainly on machines; '
  'labour-intensive relies mainly on workers. 5. Raw materials, work in progress, finished '
  'goods. 6. Buffer = minimum safety stock; re-order level = stock level triggering a new '
  'order; lead time = time between ordering and receiving. 7. JIT = little/no stock, arrives '
  'when needed; JIC = holds buffer stock just in case. 8. No time for maintenance; staff '
  'stress; quality may fall; cannot meet extra orders (any two). 9. Increase demand/marketing; '
  'reduce capacity; subcontract; cut price (any two). 10. Benefit: lower cost/specialist '
  'skills. Drawback: less control over quality/reliability.')
h1('Mini-Test 5: Finance and Accounting')
p('1. Current assets - current liabilities. 2. Cash = money available now to pay bills; '
  'profit = revenue - total costs over a period. 3. Capital expenditure = on non-current '
  'assets (long-term); revenue expenditure = day-to-day running costs. 4. Internal: owner\'s '
  'investment, retained earnings, sale of assets. External: share capital, bank loan, '
  'overdraft, leasing, trade credit, crowdfunding (any three). 5. Opening balance + net cash '
  'flow. 6. Fixed costs do not change with output; variable costs change with output. '
  '7. Contribution = selling price - variable cost per unit; break-even = fixed costs / '
  'contribution per unit. 8. Actual output - break-even output (how far sales can fall before '
  'a loss). 9. Incremental, flexible, zero-based. 10. Favourable = actual better than budget '
  '(higher revenue/lower cost); adverse = actual worse than budget.')

# ===========================================================================
# GENERATE
# ===========================================================================
jobs = [
    (CD,  'AS_Business_9609_Calculation_Drills.pdf',        'Calculation Drills - Page'),
    (CDA, 'AS_Business_9609_Calculation_Drills_Answers.pdf','Drills Answers - Page'),
    (CS,  'AS_Business_9609_Case_Studies.pdf',              'Case Studies - Page'),
    (CSA, 'AS_Business_9609_Case_Studies_Answers.pdf',      'Case Study Answers - Page'),
    (MT,  'AS_Business_9609_Topic_MiniTests.pdf',           'Mini-Tests - Page'),
    (MTA, 'AS_Business_9609_Topic_MiniTests_Answers.pdf',   'Mini-Test Answers - Page'),
]
for blocks, fn, ft in jobs:
    pages = pdfgen.build_pdf(blocks, fn, footer_prefix=ft)
    print('%-52s %d pages' % (fn, pages))
