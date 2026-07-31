# -*- coding: utf-8 -*-
"""Builds AS_Business_9609_Model_Answers.pdf - a topic-sorted booklet of every
worked question and model answer, tagged [K] [App] [An] [Ev]. ASCII only."""
import pdfgen

B = []
def p(t): B.append(('body', t))
def bu(t): B.append(('bullet', t))
def h1(t): B.append(('h1', t))
def h2(t): B.append(('h2', t))
def h3(t): B.append(('h3', t))
def sp(): B.append(('spacer', ''))
def q(ref): B.append(('h3', ref))   # question header

B.append(('title', 'AS Business 9609 - Model Answers'))
p('A topic-sorted booklet of worked exam questions with model answers. Every mark is tagged '
  '[K] Knowledge, [App] Application, [An] Analysis, [Ev] Evaluation. For the 2026-2028 syllabus. '
  'Use alongside the Exam Technique, Analysis Chains and Cheat Sheet PDFs.')
sp()
p('Contents: 1. Business & its environment  2. People in organisations  3. Marketing  '
  '4. Operations management  5. Finance & accounting  6. Data-response case studies.')

# =====================================================================
h1('1. Business and its environment')

q('Identify one barrier to entrepreneurship [1] (GR)')
p('A lack of sufficient finance/capital to fund start-up costs [K].')

q('Explain the term partnership [3] (GR)')
p('A partnership is a business owned by two or more people [K] who share capital, decisions and profits, with unlimited liability [K]. GR is owned by three partners - Sanjay, Rukmal and Boris - who pool funds and share responsibility [App].')

q('Define social enterprise [2]')
p('A social enterprise trades to achieve social or environmental objectives [K], reinvesting most profits to benefit society rather than to maximise owner profit [K].')

q('Explain one weakness of family businesses [3]')
p('Conflict between family members [K] can spill from personal disagreements into business decisions [App], slowing decision-making and harming the running of the business [An].')

q('Define organic growth [2]')
p('Organic (internal) growth is expansion using a business own resources [K], such as opening new outlets, rather than by merger or takeover [K].')

q('Explain one reason a business may choose to remain small [3]')
p('The owner may wish to keep full control [K], since growth often means bringing in partners or shareholders [App], so staying small retains decision-making and all the profit [An].')

q('Define outsourcing [2]')
p('Outsourcing is paying an external third party [K] to carry out tasks or produce goods/services previously done in-house [K].')

q('Define social enterprise / entrepreneur qualities - see People section for entrepreneur.')

q('Analyse two reasons why a business might grow internally (organically) [8]')
p('Reason 1 - Lower risk, retained control: organic growth is gradual and self-financed [K], so owners keep control and avoid culture clashes [App], growth stays manageable [An], reducing the risk of overtrading [An].')
p('Reason 2 - Cheaper than external growth: it avoids the high cost of buying another firm [K] and can use retained profit [App], so no expensive debt or overpayment [An], keeping financial risk low and profit within the firm [An].')

q("'Even a friendly merger between two social media companies may not be successful.' Evaluate [12]")
p('For failure: different cultures/systems cause integration problems and loss of key staff [App/An]; technical integration, regulatory scrutiny and user/privacy backlash can lose users and ad revenue [An].')
p('For success: cooperation, shared vision and combined user bases create network effects, shared technology and cost savings [App/An].')
p('Judgement: being friendly lowers resistance but does not guarantee success [Ev]; it depends on cultural fit, integration, regulatory approval and user retention [Ev]. Network-effect gains are large but risks are equally large, so a friendly merger may still fail [Ev].')

q('Analyse two benefits of a vertical merger for growth [8]')
p('Backward (with a supplier): control over raw materials [K/App], giving reliable supply, lower input costs and quality control [An], fewer disruptions and better margins [An].')
p('Forward (with a distributor/retailer): guaranteed market access [K/App], controlling how the product reaches customers and capturing the retailer margin [An], giving secure outlets and higher revenue [An].')

q("'Risk-taking is the most important quality for an entrepreneur in clothing design.' Evaluate [12]")
p('For: fashion is fast-moving and uncertain [App], so the entrepreneur must risk money on new designs before knowing demand [An], seizing trends ahead of cautious rivals [An].')
p('Against: creativity and trend-awareness are arguably more important [App], since original designs differentiate the product [An]; a risk-taker with no flair still fails [An].')
p('Judgement: risk-taking is necessary but not the single most important quality [Ev]; creativity and market awareness matter at least as much in clothing design [Ev], so the view is only partly valid [Ev].')

q('Analyse two barriers to an entrepreneur when starting up [8]')
p('Lack of finance: banks are reluctant to lend without a track record [K/App], so the entrepreneur cannot afford equipment/stock [An], limiting the scale or preventing launch [An].')
p('Competition from established firms: rivals have brand loyalty and economies of scale [K/App], so the start-up struggles to win customers [An], causing low sales and cash-flow problems [An].')

q("'The most important objective of a public sector energy supplier is the environmental objective.' Evaluate [12]")
p('For: energy has a huge environmental impact [App], and as a public body it should lead on emissions/renewables [An] for the long-term public interest [An].')
p('Against: the core purpose is a reliable, affordable supply to all citizens [App]; unreliable or unaffordable energy harms people immediately [An], so security/affordability may be more fundamental [An].')
p('Judgement: the environmental objective is very important, but ensuring secure, affordable supply is usually the most important [Ev]; it depends on the country context [Ev], so the view is only partially valid [Ev].')

q('Analyse the disadvantages to a sole trader of changing to a partnership [8]')
p('Loss of control: decisions must now be shared [K/App], causing possible disagreements over direction [An], slowing decisions and creating conflict [An].')
p('Shared profits and liability: profit is divided among partners [K/App], and with unlimited liability each partner is liable for the others actions [An], so one partner mistake could create debts the original owner is responsible for [An].')

q('Discuss whether a franchise is the best way for a new entrepreneur to start a business [12]')
p('For: a proven model and recognised brand [App] mean customers already trust it and sales are more likely [An]; training, support and easier finance raise the survival chance [An].')
p('Against: high initial fee plus ongoing royalties reduce profit [App/An]; the franchisee must follow rules, limiting independence, and suffers if the brand is damaged [An].')
p('Judgement: franchising is one of the best routes for a risk-averse first-timer [Ev], but not best for everyone - it depends on capital and desire for independence/creativity [Ev]; an innovative entrepreneur may prefer an independent start-up, so it is often a strong option but not universally best [Ev].')

q('Define stakeholders [2]')
p('A stakeholder is any individual or group [K] with an interest in, or affected by, the activities of a business [K].')

q('Explain one responsibility of a stakeholder group [3]')
p('Employees have a responsibility to work productively to the required standard [K]; by doing their duties well [App], they help the business operate efficiently and meet customer needs [An].')

q('Explain one reason why conflict might arise between different stakeholders [3]')
p('Stakeholders have competing objectives [K]; shareholders want higher profit while employees want higher wages [App], and since higher wages reduce profit the aims clash [An].')

q('Explain why there might be conflict between two stakeholder groups of a large mining company [5]')
p('Stakeholders have conflicting objectives [K]. Shareholders want maximum profit, pushing for higher output and lower costs [App]. But mining increases pollution and land damage [App], harming the local community who want their environment protected [An]; since profit-seeking worsens the community environment, the two conflict [An].')

q('Explain how the interests of two stakeholder groups could affect business decisions [5]')
p('Customers want low prices and quality [App], so the business keeps prices competitive and invests in quality, shaping pricing/production decisions [An]. Shareholders want profit and dividends [App], so it controls costs and pursues profitable strategies [An] - both groups interests shape its choices [K].')

q('Analyse the advantages of a plc as a legal structure [8]')
p('Raising large capital: a plc can sell shares to the public on the stock exchange [K/App], raising large sums [An] to fund expansion and economies of scale [An].')
p('Limited liability: shareholders lose only what they invested [K], protecting personal assets [App], which reduces investment risk [An] and attracts more shareholders and capital [An].')

q('Discuss the view that banks activities should be significantly influenced by ethics [12]')
p('For: banks depend on trust [App], so ethical conduct builds trust and reputation [An], generating loyalty and avoiding scandals, fines and crises [An].')
p('Against: ethics can raise costs and cut profit [App/An], conflicting with shareholders profit aim, and less-ethical rivals may win business [An].')
p('Judgement: ethics should strongly influence banks because trust is their core asset and misconduct causes crises and lasting damage [Ev]; but they must balance ethics with commercial viability [Ev]. As the two align long term, the view is largely valid [Ev].')

q('Analyse two limitations of using number of employees to measure size [8]')
p('Capital-intensive firms use few workers but much machinery [K/App], so a large, high-output firm looks small [An], giving misleading comparisons [An].')
p('Part-time/seasonal staff are counted like full-timers [K/App], so a firm with many part-timers looks larger than it is in hours worked [An], distorting the measure [An].')

q('Evaluate whether small retail businesses have an important role in the economy [12]')
p('For: collectively they provide employment, local service, competition, choice and entrepreneurship, and support local suppliers [App/An].')
p('Against: individually each contributes little to output/employment, lacks economies of scale, is dearer and often fails, while large chains dominate [App/An].')
p('Judgement: together they are important, especially locally and for competition [Ev], even if each is small and big firms contribute more overall [Ev]; it depends on the economy, so the view is largely valid [Ev].')

q('Analyse two limitations to a business of using a business plan [8]')
p('Based on uncertain forecasts [K] that may be wrong if conditions change [App], so the plan becomes outdated [An] and rigid use leads to poor decisions [An].')
p('Time-consuming and costly to produce [K/App], diverting management from running the business [An], with a false sense of security reducing flexibility [An].')

q("'A chocolate manufacturer should use external methods of growth.' Evaluate [12]")
p('For external: taking over a rival gains market share, brands and scale quickly [App/An]; a vertical merger with a cocoa supplier secures raw materials cheaply [An].')
p('Against: external growth is costly and risky - culture clashes, integration, overpaying [App/An]; organic growth is cheaper, lower-risk and keeps control [An].')
p('Judgement: external growth can achieve fast objectives but is risky [Ev]; whether it should be used depends on the objective, finances and market [Ev]. A combination is often best, so the view is only partly valid [Ev].')

q('Analyse two reasons why changing a business objectives might affect its shareholders [8]')
p('Lower short-term profit: switching from profit maximisation to growth/social aims [K/App] may cut dividends [An], so shareholders receive less income and may sell shares [An].')
p('Changed risk/share price: an aggressive-expansion objective raises risk [K/App], making the share price volatile [An], directly affecting shareholders wealth [An].')

q("'The main reason niche cake businesses fail is that they grow too quickly.' Evaluate [12]")
p('For: overtrading - expanding beyond finance [App] - causes cash-flow problems so bills cannot be paid [An]; rapid growth erodes the quality/personal touch that defined the niche [An].')
p('Against: many fail for other reasons - too little finance, poor cash-flow management, too-small a niche, competition [App/An]; well-financed firms grow fast without failing [An].')
p('Judgement: growing too quickly is a common, serious cause but not necessarily the main one [Ev]; poor finance and weak demand are often more fundamental [Ev], so the view is only partly valid [Ev].')

q('Analyse two reasons why a business should set SMART objectives [8]')
p('Clear direction: specific, time-bound objectives [K] tell staff what to achieve and by when [App], focusing effort [An] and making the goal more likely to be met [An].')
p('Easier monitoring: measurable objectives [K] let progress be tracked [App], so managers take corrective action if behind [An], improving control and motivation [An].')

q("'Ethics should always influence the HRM activities of a mining business.' Evaluate [12]")
p('For: mining is dangerous, often where labour protection is weak [App], so ethical HRM - safe conditions, fair pay, no child labour [An] - protects lives, relations and reputation [An].')
p('Against: ethical HRM raises costs [App], cutting profit and competitiveness [An]; "always" is demanding when rivals cut corners [An].')
p('Judgement: given the life-and-death safety dimension, ethics should strongly - arguably always - influence mining HRM [Ev], though it involves cost trade-offs [Ev]; the view is largely valid [Ev].')

# =====================================================================
h1('2. People in organisations')

q('Define corporate social responsibility (CSR) [2]')
p('CSR is the idea that a business should act in the interests of society and the environment [K], beyond its legal obligations and profit motive [K].')

q('Explain one disadvantage of having CSR as an objective [3]')
p('CSR usually raises costs [K], e.g. ethically sourced materials or above-market pay [App], reducing margins and possibly forcing higher, less competitive prices [An].')

q('Define person specification [2]')
p('A person specification lists the qualifications, skills, experience and personal qualities [K] required of the ideal candidate for a job [K].')

q('Explain one purpose of a job description [3]')
p('A job description sets out a role duties and responsibilities [K]; its purpose is to tell applicants and staff what the job involves [App], so suitable people apply and performance improves [An].')

q('Define induction training [2]')
p('Induction training is training given to new employees when they first join [K] to introduce them to the business, role and procedures [K].')

q('Explain one benefit of training employees [3]')
p('Training improves skills [K], so employees work more efficiently with fewer mistakes [App], raising productivity and quality and lowering costs [An].')

q('Define dismissal [2]')
p('Dismissal is the ending of an employee contract by the employer [K], usually due to misconduct or poor performance [K].')

q('Explain how one human need may be satisfied at work [3]')
p('Social needs (Maslow) [K] are met by teamwork and interaction with colleagues [App], giving a sense of belonging [An].')

q('Define labour turnover [2]')
p('Labour turnover is the rate at which employees leave a business and are replaced over a period [K], usually as a percentage [K].')

q('Explain one role of a workforce plan [3]')
p('A workforce plan forecasts the number and type of employees needed [K]; it identifies future staffing needs [App] so the firm recruits/trains in time to meet demand [An].')

q('Define job description [2]')
p('A job description is a document setting out the duties, tasks and responsibilities [K] of a particular role [K].')

q('Explain one advantage to an employer of using a person specification [3]')
p('It lists the ideal candidate skills [K], letting the employer compare applicants against clear criteria [App], selecting the best person and avoiding costly hiring mistakes [An].')

q('Explain one impact on employees of being trade union members [3]')
p('Members gain collective bargaining [K]; the union negotiates on their behalf [App], giving more power to secure better pay/conditions than negotiating alone [An].')

q('Explain one benefit of internal recruitment [3]')
p('Internal recruitment fills a vacancy from existing staff [K]; it is cheaper and quicker and the candidate is known [App], lowering cost/risk and motivating staff through promotion [An].')

q('Define performance-related pay [2]')
p('Performance-related pay is extra pay linked to how well an employee performs [K], measured against targets/appraisal [K].')

q('Explain one advantage to employees of performance-related pay [3]')
p('It rewards good performance with higher pay [K], so hard workers who hit targets earn more [App], raising income and motivating them through recognition [An].')

q('Define commission [2]')
p('Commission is a payment based on the value or number of sales an employee makes [K], usually a percentage of sales [K].')

q('Explain one disadvantage of using empowerment to motivate employees [3]')
p('Empowerment gives more responsibility [K], but not all staff want or can handle it [App], so inexperienced workers may make poor decisions or feel stressed, harming the business [An].')

q('Define piece rate [2]')
p('Piece rate is a payment method where an employee is paid a fixed amount per unit produced [K], not per hour [K].')

q('Explain one advantage of a time-based payment method [3]')
p('Time-based pay [K] is simple to calculate and suits work where quality matters more than speed [App], so workers are not rushed and quality is maintained [An].')

q('Define motivation [2]')
p('Motivation is the desire and drive within employees [K] to put in effort and achieve goals [K].')

q('Explain one non-financial motivator [3]')
p('Job enrichment [K] gives employees more challenging, meaningful tasks [App], meeting higher-level needs and raising satisfaction and motivation [An].')

q('Analyse two reasons why an employee human needs may not be satisfied at work [8]')
p('Low pay: if pay is too low [K], workers cannot meet basic living costs [App], so physiological/security needs go unmet [An] and motivation stays low [An].')
p('Autocratic management with no recognition [K/App]: esteem and self-actualisation needs are unmet [An], so employees feel undervalued and unable to develop [An].')

q("'Non-financial motivators are the most effective way to motivate a hotel workforce.' Evaluate [12]")
p('For: hotels have high turnover [App]; recognition and empowerment raise satisfaction and cut turnover [An], improving service (Herzberg motivators) [An].')
p('Against: many hotel staff are low-paid [App], so financial rewards may motivate more by meeting basic needs [An]; without adequate pay dissatisfaction persists [An].')
p('Judgement: non-financial motivators are effective and sustainable once pay is adequate [Ev]; for low-paid staff pay may matter more initially [Ev]. A combination is best, so the view is only partly valid [Ev].')

q("'Good leaders will be more important than effective managers to improve an international hotel chain.' Discuss [20]")
p('Leaders set vision and inspire; managers plan, organise and control [K].')
p('For leaders: a multi-country chain needs vision, consistent brand standards and motivation, plus change and innovation to improve [App/An].')
p('For managers: a large chain is operationally complex, so effective management coordinates sites, budgets and quality; without it standards slip [App/An].')
p('Judgement: it depends what "improve" means [Ev]; leaders drive improvement, but they cannot succeed without managers to execute [Ev]. I agree to a large extent that leaders are more important for improvement, but the two are complementary [Ev].')

q('Analyse two benefits to the workforce of McGregor Theory X management [8]')
p('Clear direction: close supervision and detailed instructions [K/App] remove ambiguity [An], so less confident workers complete tasks correctly without decision stress [An].')
p('Structured, secure environment: tight rules suit workers who prefer to be told what to do [K/App], giving clear expectations and security [An], guided closely by managers [An].')

q('Evaluate whether cooperation between management and workforce is the most important factor for a car manufacturer [12]')
p('For: capital-intensive and unionised [App], so cooperation avoids costly strikes [An] and eases new methods, raising productivity [An].')
p('Against: quality, technology, brand and demand also matter [App]; poor cars fail regardless of cooperation [An], so competitiveness may matter more [An].')
p('Judgement: cooperation is very important given costly stoppages [Ev], but not clearly the most important - quality/technology are equally critical [Ev]; it depends on unionisation, so partly valid [Ev].')

q('Analyse two benefits of external recruitment to employ a manager [8]')
p('New skills and ideas: a manager from elsewhere [K/App] brings fresh perspectives and best practice [An], driving innovation and better decisions [An].')
p('Wider pool: the role opens to many applicants [K/App], raising the chance of a highly qualified candidate [An] and improving the appointment [An].')

q("'A motivated workforce is the most important factor for a low-price airline.' Evaluate [12]")
p('For: motivated crew give better service and fast turnarounds [App/An], cutting costs and encouraging repeat custom [An].')
p('Against: the model rests on cost leadership - fuel efficiency, high utilisation, low overheads [App/An]; cost control and safety are essential [An].')
p('Judgement: motivation supports success, but cost control is arguably the most important factor for a budget airline [Ev]; it depends on competition, so the view is only partly valid [Ev].')

q('Analyse two ways a business could use employee participation [8]')
p('Works councils/representatives: consulting elected reps [K/App] gives staff a voice [An], improving morale and decisions they then support [An].')
p('Quality circles: staff meet to solve operational problems [K/App], using front-line knowledge to suggest improvements [An], raising quality and motivation [An].')

q('Evaluate whether McClelland three-needs theory is the best way to meet employee needs in a software business [12]')
p('For: skilled professionals differ, so tailoring - challenge for achievers, teamwork for affiliation, leadership for power [App/An] - suits knowledge workers, raising motivation/retention [An].')
p('Against: identifying each need is hard and subjective [App]; Herzberg motivators and self-actualisation fit creative work, and high pay also motivates [An/An].')
p('Judgement: useful because employees differ, but hard to apply and not clearly best alone [Ev]; combining with Herzberg and fair pay works better [Ev], so partly valid [Ev].')

q('Analyse two benefits of low labour turnover [8]')
p('Lower recruitment/training costs [K]: fewer leavers means less spent replacing them [App], so costs fall and profit rises [An/An].')
p('Retained experience/continuity [K/App]: long-serving staff stay productive with strong customer relationships [An], giving stable, higher-quality teams [An].')

q("'Work-life balance is the most important HRM factor for welfare in a local bus service.' Evaluate [12]")
p('For: drivers work long, unsocial shifts [App], so work-life balance reduces fatigue and stress [An], improving welfare and cutting absence [An].')
p('Against: health and safety and fair pay also central [App]; fatigue is safety-critical and low pay harms welfare directly [An/An].')
p('Judgement: work-life balance is very important but arguably outweighed by safety, since fatigue affects welfare and public safety [Ev]; it depends on pay/conditions, so partly valid [Ev].')

q('Analyse two reasons why a business might use external recruitment [8]')
p('Access to new skills the firm lacks [K/App], bringing fresh expertise [An] and innovation the current staff could not provide [An].')
p('A wider pool when expanding or with no suitable internal candidate [K/App], raising the chance of finding the best person [An/An].')

q('Evaluate whether managers contribution will have the most influence on a new hospital performance [12]')
p('For: at set-up, managers coordinate staff, budgets and resources [App/An], affecting waiting times and costs [An].')
p('Against: clinical staff skill, equipment and funding may matter more [App], since outcomes depend on care quality [An], and managers cannot offset under-resourcing [An].')
p('Judgement: managers are highly influential at set-up but not clearly the most important - clinical staff and resources are at least as decisive [Ev]; depends on how performance is measured, so partly valid [Ev].')

q('Analyse two methods to help employees satisfy self-actualisation needs (Maslow) [8]')
p('Challenging, enriched work [K/App] stretches ability [An], giving achievement and growth toward potential [An].')
p('Development and promotion opportunities [K/App] let employees gain skills and responsibility [An], reaching their potential and feeling fulfilled [An].')

q('Evaluate whether ability to motivate others is the most important role of a hotel manager [12]')
p('For: hotels are people-intensive with high turnover [App], so motivating secures service, loyalty and low turnover [An], driving guest satisfaction [An].')
p('Against: managers must also plan operations, control costs and maintain standards [App]; motivation alone will not run the hotel [An/An].')
p('Judgement: motivating is among the most important roles given the service nature, but one of several [Ev]; it depends on the situation, so not the single most important in isolation [Ev].')

q('Analyse two qualities an intrapreneur should possess [8]')
p('Creativity/innovation [K/App]: generating new products/processes [An] gives the employer competitive advantage and revenue [An].')
p('Initiative and calculated risk-taking [K/App]: pursuing opportunities despite uncertainty [An] drives change and growth ahead of rivals [An].')

q("'Ethics should significantly influence the marketing of all retail clothing businesses.' Evaluate [12]")
p('For: consumers value ethical fashion [App], so ethical marketing builds trust and reputation [An], generating loyalty and avoiding backlash [An].')
p('Against: ethical practices raise costs and honest marketing can be less persuasive [App/An]; budget/fast-fashion customers prioritise price [An].')
p('Judgement: ethics should significantly influence many retailers marketing, but "all" is too strong [Ev]; for budget retailers it is less influential and costly [Ev], so partly valid [Ev].')

# =====================================================================
h1('3. Marketing')

q('Define market share [2]')
p('Market share is the proportion of total sales in a market [K] held by one business or product, as a percentage [K].')

q('Explain one way a retailer could increase its market share [3]')
p('Price promotions/lower prices [K] attract customers from competitors [App], so it sells more relative to rivals and its share rises [An].')

q('Define demand [2]')
p('Demand is the quantity of a good/service consumers are willing and able to buy [K] at a given price over a period [K].')

q('Explain one factor which might influence supply of a product [3]')
p('Cost of production [K]: if costs fall, e.g. cheaper materials [App], producers supply more at each price, so supply increases [An].')

q('Define market segmentation [2]')
p('Market segmentation is dividing a market into distinct groups of customers [K] with similar characteristics or needs [K].')

q('Explain one benefit of market segmentation [3]')
p('It allows targeted marketing [K]: tailoring product/promotion to a group [App], cutting wasted spend and better meeting needs, raising sales [An].')

q('Explain the link between corporate and marketing objectives [5]')
p('Corporate objectives are the whole-business goals; marketing objectives are the marketing function goals [K]. Marketing objectives derive from and support corporate ones [App] - e.g. a growth aim leading to a market-share target [App] - translating the wider aim into a specific target [An] so marketing contributes to overall goals [An].')

q('Define market research [2]')
p('Market research is the collection, analysis and interpretation of data [K] about a market, customers and competitors [K].')

q('Explain two advantages of primary (field) research data [3]')
p('It is collected first-hand for the firm specific purpose, so directly relevant [K], and up to date [K], answering the exact questions with current information [An].')

q('Explain two reasons a business might use secondary research data [3]')
p('It already exists, so it is cheaper and quicker than primary data [K/K], giving a broad market overview at low cost before any primary research [An].')

q('Analyse two benefits of customer relationship marketing [8]')
p('Higher loyalty/retention [K/App]: repeat purchases [An] give stable revenue and lower costs, since retention is cheaper than acquisition, raising profit [An].')
p('Better customer insight [K/App]: personalised offers and service [An] raise satisfaction and enable cross-selling, boosting sales [An].')

q("'Market research is essential for effective product development in a hotel.' Evaluate [12]")
p('For: research identifies guest needs [App], so the hotel develops the right services [An], cutting the risk of unused offerings and raising occupancy [An].')
p('Against: research is costly, slow and can be inaccurate [App]; feedback, experience and competitor observation also guide development [An/An].')
p('Judgement: research is very valuable but not strictly essential [Ev]; it depends on size/budget [Ev], so "essential" is too strong - partly valid [Ev].')

q('Analyse the benefits of market segmentation [8]')
p('Targeted marketing [K/App]: less waste and better-met needs [An], raising sales and loyalty [An].')
p('Identifying gaps [K/App]: developing products for unmet needs [An], differentiating and attracting new customers [An].')

q('Discuss whether marketing is the most important function for a car manufacturer [12]')
p('For: a competitive, image-driven market [App] where marketing strongly influences which cars are bought [An], driving sales [An].')
p('Against: operations/quality are at least as important [App]; an unreliable car fails regardless of marketing [An], and finance/labour are vital [An].')
p('Judgement: marketing is crucial but not clearly the single most important - quality underpins reputation and repeat sales, and functions are interdependent [Ev]; partly valid [Ev].')

q('Analyse the benefits of product portfolio analysis [8]')
p('Efficient resource allocation [K/App]: invest in stars, drop dogs [An], giving a balanced portfolio and steadier income [An].')
p('Funding new products [K/App]: cash cows fund stars/question marks [An], supporting development and long-term success [An].')

q('Discuss the importance of branding when promoting a soft drink [12]')
p('For: a saturated market of similar products [App], so a strong brand differentiates, builds recognition and loyalty [An], allowing repeat purchase and premium pricing [An].')
p('Against: branding is costly; taste, price and availability also matter [App]; price-sensitive buyers choose on price and branding cannot save a poor drink [An/An].')
p('Judgement: branding is highly important - arguably central - for soft-drink promotion, but must be backed by taste, price and availability [Ev]; largely valid [Ev].')

q('Analyse how marketing can add value to a product [8]')
p('Branding/image [K/App]: customers see the product as premium [An] and pay more, raising price/margin [An].')
p('Communicating a USP [K/App]: differentiation builds an emotional connection [An], so customers value it more and pay a premium [An].')

q('Discuss whether a hotel marketing objectives need close working between marketing, finance and HR [12]')
p('For: marketing needs finance to fund it and HR to deliver the promised service [App], so cooperation makes the experience match the advertising [An], hitting objectives [An].')
p('Against: "only" is strong - objectives can be partly met by strong marketing or favourable conditions [App/An], and external factors also matter [An].')
p('Judgement: cooperation is highly important, arguably necessary, but not the sole determinant [Ev]; partly valid [Ev].')

q('Analyse how product portfolio analysis helps achieve marketing objectives [8]')
p('It identifies products needing investment - stars/question marks [K/App] - so promotion is channelled to them [An], growing market share [An].')
p('It reveals cash cows and dogs [K/App], allocating resources efficiently and funding new products [An], giving a balanced portfolio supporting sales-growth objectives [An].')

q('Discuss reliance on penetration pricing for a new computer manufacturer to gain market share [12]')
p('For: a competitive market with loyal customers to established brands [App], so a low price attracts price-sensitive buyers [An], overcoming no brand recognition and building share [An].')
p('Against: computers are bought on spec/brand not just price [App], so differentiation could gain share [An]; low prices squeeze costly margins [An].')
p('Judgement: some reliance is needed to overcome the entry barrier [Ev], but not sole reliance - differentiation protects margins [Ev]; it depends on the product, so best combined [Ev].')

q('Analyse two reasons for a close link between marketing and corporate objectives [8]')
p('Alignment: marketing objectives support the corporate goal [K/App], so marketing contributes to what the business seeks [An], making the goal likely [An].')
p('Coordination: a close link keeps marketing consistent with the firm [K/App], avoiding conflicting directions [An] and wasted spend [An].')

q("'This new airline will only succeed if it offers the lowest prices.' Evaluate [12]")
p('For: air travel is price-competitive [App], so lowest prices attract price-sensitive travellers and fill seats [An/An].')
p('Against: reliability, safety, routes and service also matter [App]; premium travellers value service, and unsustainably low prices cause losses [An/An].')
p('Judgement: low prices can drive budget-airline success, but "only" is too strong [Ev]; success needs low costs, reliability and routes too [Ev], so partly valid [Ev].')

q('Analyse two limitations of sampling [8]')
p('Unrepresentative samples [K/App] give biased results [An], so decisions rest on misleading data, wasting money [An].')
p('Small sample size [K/App] has a large error margin [An], so conclusions may be inaccurate, leading to poor decisions [An].')

q("'Promotion is the most important element of the mix for a parcel delivery business.' Evaluate [12]")
p('For: promotion raises awareness and communicates speed/reliability [App], winning customers and contracts [An].')
p('Against: place (a reliable, wide network) is arguably more important [App], since customers choose on reliability, speed and price [An]; poor service loses them [An].')
p('Judgement: promotion matters but is not the most important - place and service quality dominate for this business [Ev]; partly valid [Ev].')

q('Define price discrimination [2]')
p('Price discrimination is charging different customers different prices [K] for the same product, based on willingness/ability to pay [K].')

q('Explain one disadvantage of price discrimination [3]')
p('Customers charged more may feel unfairly treated [K]; if they discover others pay less [App], they resent the business and switch to rivals, harming reputation and sales [An].')

q('Explain one disadvantage of competitive pricing [3]')
p('Competitive pricing sets prices from rivals prices [K], limiting the firm freedom to set its own [App], so matching low prices squeezes margins and cuts profit [An].')

q('Define product life cycle [2]')
p('The product life cycle shows the stages a product passes through over time [K] - introduction, growth, maturity and decline [K].')

q('Explain one way to extend the life of a product [3]')
p('An extension strategy such as updated features or rebranding [K], e.g. targeting a new segment [App], revives sales and delays decline [An].')

q('Define product differentiation [2]')
p('Product differentiation is making a product distinct from competitors [K] in the eyes of consumers, via features, quality or branding [K].')

q('Explain one reason product development may be important [3]')
p('It keeps the range fresh and competitive [K]; launching improved/new products [App] meets changing needs and stays ahead of rivals, maintaining sales [An].')

q('Analyse one impact of using product portfolio analysis on marketing decisions [5]')
p('Product portfolio analysis (Boston Matrix) classifies products by share and growth [K]. It identifies stars, cash cows, question marks and dogs [App], so the firm directs its marketing budget to stars and promising question marks and cuts dogs [An], giving efficient spend and a balanced portfolio [An].')

q('Analyse one reason product differentiation may be important [5]')
p('Differentiation makes a product stand out [K]. A clear USP [App] makes customers more brand loyal and less price-sensitive [An], so the firm can charge a premium and retain customers, raising revenue and margins [An].')

q('Analyse two benefits of a product with a USP [8]')
p('Standing out [K/App]: attracts customers who cannot get the feature elsewhere [An], raising sales/share [An].')
p('Reduced price sensitivity [K/App]: brand loyalty lets the firm charge a premium [An], widening margins [An].')

q("'Marketing is the most important factor for a new coffee shop.' Evaluate [12]")
p('For: a new shop is unknown [App], so marketing raises awareness and draws first-time customers [An], building a base [An].')
p('Against: location (footfall) and product quality are arguably more important [App]; poor location or coffee loses customers regardless [An/An].')
p('Judgement: marketing helps launch but is not the most important - location and quality drive repeat custom [Ev]; partly valid [Ev].')

q('Analyse two advantages of mass marketing [8]')
p('Economies of scale [K/App]: large-scale production spreads fixed costs and earns discounts [An], lowering unit costs [An].')
p('High sales/awareness [K/App]: reaching everyone gives wide brand awareness and high volume [An], producing large revenue [An].')

q('Evaluate whether primary sector businesses should use product differentiation to increase sales [12]')
p('For: some primary products can be differentiated - organic, fair-trade, certified [App] - standing out and commanding a premium [An/An].')
p('Against: most primary products are commodities sold on price [App], so differentiating raw materials is hard and costly [An/An].')
p('Judgement: differentiation can help where feasible (e.g. organic produce) but is hard for bulk commodities [Ev]; it depends on the product, so valid only in some cases [Ev].')

# =====================================================================
h1('4. Operations management')

q('Define factors of production [2]')
p('Factors of production are the resources used to produce goods/services [K] - land, labour, capital and enterprise [K].')

q('Explain one stage of the transformational process [3]')
p('The process turns inputs into outputs [K]. In the process stage, inputs such as materials and labour are combined and converted [App], e.g. assembling materials into a finished product, adding value [An].')

q('Analyse one reason why labour productivity is important [5]')
p('Labour productivity is output per worker per period [K]. Higher productivity means more output from the same workers [App], lowering labour cost per unit [An], so the firm prices competitively or earns higher margins, improving competitiveness and profit [An].')

q('Define efficiency [2]')
p('Efficiency is producing output using the minimum inputs [K], minimising waste and cost per unit [K].')

q('Explain one way to increase efficiency of manufacturing operations [3]')
p('Automation/new technology [K] lets machines produce faster and more consistently [App], giving more output per input with less waste and lower unit cost [An].')

q('Define transformation process [2]')
p('The transformation process is the conversion of inputs (resources) [K] into outputs of finished goods/services that add value [K].')

q('Explain one way process innovation could improve efficiency [3]')
p('Process innovation means improved production methods [K], e.g. a more automated line [App], producing goods faster with less waste and lower unit cost, improving efficiency [An].')

q('Analyse one way a business might raise productivity levels [5]')
p('Training [K]: workers perform tasks more skilfully [App], working faster with fewer errors [An], so output per worker rises, raising productivity and lowering unit cost [An].')

q('Define capital intensive [2]')
p('Capital intensive means production relying heavily on machinery/capital equipment [K] relative to labour [K].')

q('Explain one benefit of labour intensive operations [3]')
p('Labour-intensive operations rely mainly on workers [K], giving flexibility [App]: workers adapt to varied/customised tasks more easily than machines, allowing bespoke products and adjustable output [An].')

q('Analyse one way a business might improve efficiency of operations [5]')
p('Lean production to reduce waste [K]: cutting waste of materials and time, e.g. JIT [App], uses fewer inputs per unit [An], lowering unit cost and raising efficiency and competitiveness [An].')

q('Analyse two reasons why a business should measure labour productivity [8]')
p('Monitoring efficiency [K/App]: spotting rising/falling output per worker [An] so managers act to control costs [An].')
p('Benchmarking/targets [K/App]: comparing with rivals and setting targets [An], identifying underperformance to train and stay competitive [An].')

q('Evaluate whether sustainability of operations is the most important operational factor for a large retail distribution business [12]')
p('For: rising regulation and customer expectations [App], so sustainable operations protect reputation and cut some costs [An/An].')
p('Against: reliable, efficient delivery is arguably more important [App], being the core purpose [An]; poor reliability harms the business faster [An].')
p('Judgement: sustainability matters and is rising, but reliable, efficient distribution is likely the most important operational factor [Ev]; it depends on regulatory/customer pressure, so partly valid [Ev].')

q('Analyse two benefits of improving the sustainability of operations [8]')
p('Lower long-term costs [K/App]: less energy and waste [An], reducing unit cost and raising margins over time [An].')
p('Improved reputation [K/App]: appeals to eco-conscious customers, differentiating the brand [An], attracting customers and boosting sales/loyalty [An].')

q("'Supply Chain Management is the most important operations factor for a large internet retailer.' Evaluate [12]")
p('For: online retail depends on fast, reliable fulfilment [App], so SCM ensures stock availability and delivery [An], central to satisfaction and repeat orders [An].')
p('Against: IT reliability, inventory and cost control also matter [App]; a crashing site loses sales regardless of SCM [An/An].')
p('Judgement: SCM is arguably the most important operations factor since customers judge online retailers on delivery [Ev], but depends on IT and cost control alongside it [Ev]; largely valid [Ev].')

q('Analyse two benefits of JIT inventory control [8]')
p('Lower storage costs and freed cash [K/App]: little stock held [An], improving cash flow and cutting costs, raising profit [An].')
p('Fresh, quality output and short lead times [K/App]: reliable just-in-time deliveries [An] help meet demand for quality and speed in a competitive market [An].')

q('Analyse two benefits of holding high levels of inventory [8]')
p('Meeting demand/avoiding stock-outs [K/App]: always able to fulfil orders even in spikes [An], avoiding lost sales and protecting reputation [An].')
p('Buffer against supply problems [K/App]: production continues if a supplier is late [An], avoiding costly stoppages and missed deadlines [An].')

q('Evaluate whether SCM is the most important operational activity for an electric-car manufacturer [12]')
p('For: EV makers rely on scarce inputs like batteries/chips [App], so strong SCM secures these reliably and cheaply [An], keeping production running [An].')
p('Against: quality (safety-critical), capacity and innovation are also critical [App]; poor quality or outdated tech damages the firm regardless [An/An].')
p('Judgement: SCM is arguably the most important given supply risks [Ev], but depends on quality and innovation alongside it [Ev]; largely but not wholly valid [Ev].')

q('Analyse two ways operations contributes to added value [8]')
p('Improving quality [K/App]: customers perceive higher worth [An], allowing a higher price and more added value [An].')
p('Reducing waste/costs [K/App]: lean production lowers input costs [An], widening the gap between price and cost [An].')

q("'Supply chain management has the most significant impact on the effectiveness of a hospital.' Evaluate [12]")
p('For: constant supplies of medicines/equipment [App] mean good SCM prevents shortages that delay treatment [An/An].')
p('Against: clinical staff skill, funding and care quality matter more [App]; supplies cannot offset too few doctors [An/An].')
p('Judgement: SCM has a significant impact but is not the most significant - staff competence and resources influence outcomes more [Ev]; depends on the measure, so the view overstates its role [Ev].')

q('Analyse one impact of operating below maximum capacity [5]')
p('Spare capacity spreads fixed costs over fewer units [K/App], so fixed cost per unit rises [An], increasing average cost and reducing competitiveness and margins [An].')

q('Explain one purpose of JIC (Just in Case) inventory management [3]')
p('JIC holds buffer stock in case of unexpected demand or supply problems [K]; keeping spare inventory [App] lets the firm meet orders if a supplier is late or demand rises, avoiding lost sales [An].')

q('Analyse one impact of operating over maximum capacity [5]')
p('Overtime and heavy machine use [K/App] raise costs and the risk of breakdowns and mistakes [An], so quality and reliability fall, damaging reputation and satisfaction [An].')

q('Analyse one benefit of improving capacity utilisation [5]')
p('Producing more from the same fixed resources [K/App] spreads fixed costs over more units [An], lowering fixed cost per unit and average cost, improving competitiveness and profit [An].')

# =====================================================================
h1('5. Finance and accounting')

q('Explain the importance of working capital to a new business [5]')
p('Working capital is finance for day-to-day operations (current assets minus current liabilities) [K]. A new business needs it to pay short-term bills like wages, stock and rent [App] before revenue arrives [App]; with few reserves and limited credit, too little working capital means it cannot pay debts [An], becoming illiquid and failing, whereas enough keeps it trading until inflows build [An].')

q('Explain why a manager needs to understand capital vs revenue expenditure [5]')
p('Capital expenditure is on non-current assets used over years; revenue expenditure is day-to-day running costs [K]. The manager records them differently - capital on the statement of financial position, revenue on the income statement [App]; misclassifying a machine as a running cost understates profit [An], so budgeting, pricing and tax decisions rest on wrong figures [An].')

q('Explain how a business might improve its cash flow [5]')
p('Cash flow is the movement of cash in and out over time [K]. A retailer could negotiate longer supplier credit, e.g. 60 days not 30 [App]; cash then stays in the business longer [An], giving more cash to meet outflows like wages and reducing the risk of insolvency [An].')

q('Explain the advantages of sale and leaseback of non-current assets [5]')
p('Sale and leaseback means selling an asset then leasing it back to keep using it [K]. A manufacturer could sell its machinery yet still use it [App]; it raises an immediate lump sum without losing use [App], improving liquidity to reinvest [An] and avoiding a loan, with the cost spread as lease payments [An].')

q('Define overdraft [2]')
p('An overdraft lets a business withdraw more than it holds in its account [K], up to an agreed limit [K].')

q('Explain two reasons a business might use an overdraft [3]')
p('To cover short-term cash shortages [K], e.g. paying wages before customers pay [App], and for flexibility on one-off costs, as interest is only charged on the amount used [K/An].')

q('Explain internal sources of finance for growth [5]')
p('Internal sources come from within the business [K]. Retained profit - profit kept after tax/dividends [K] - can buy new equipment to expand [App], avoiding interest/control loss, cheaper than a loan [An]. Selling unused assets raises cash for growth [App] without debt or dilution [An].')

q('Analyse two benefits of government grants as a source of finance [8]')
p('No repayment/interest [K]: avoids adding debt or interest [App], improving cash flow and freeing funds for investment [An], enabling growth without a repayment burden [An].')
p('No dilution of control [K]: no shares issued [App], so owners keep control and can fund otherwise-unaffordable projects [An], improving competitiveness [An].')

q('Evaluate whether poor working-capital management is the most likely reason a small retailer fails [12]')
p('For: retailers depend on liquidity - stock, rent, wages [App]; poor working-capital management means they cannot pay short-term debts [An], so even a profitable shop is forced into insolvency [An].')
p('Against: many fail from falling sales, competition, poor location or downturn [App]; poor working capital is often a symptom of low sales, not the root cause [An/An].')
p('Judgement: it is the most likely immediate cause, since running out of cash forces closure [Ev], but often a symptom of deeper problems [Ev]; short term liquidity kills, long term competitiveness decides - a trigger more than the sole cause [Ev].')

q('Analyse the benefits of using a cash-flow forecast [8]')
p('Identifying shortages early [K/App]: arrange finance ahead of time [An], avoiding inability to pay bills and insolvency [An].')
p('Supporting planning/finance applications [K/App]: shown to lenders it demonstrates good planning [An], improving the chance of a loan and sensible investment timing [An].')

q('Discuss whether accurate cost information is the most important factor in a restaurant success [12]')
p('For: tight margins and perishable stock [App], so accurate costs enable correct pricing and cost control [An], protecting profit [An].')
p('Against: food quality, service, location and marketing also matter [App]; customers return for the experience, not the cost data [An/An].')
p('Judgement: accurate costing is important but not the most important - quality, service and location generate the customers success depends on [Ev]; partly valid [Ev].')

q('Analyse two factors influencing a business choice of sources of finance [8]')
p('Cost of finance [K/App]: comparing interest and charges [An], choosing a cheaper source to avoid repayments that cut profit [An].')
p('Purpose and time period [K/App]: long-term assets need long-term finance, short shortages suit an overdraft [An], so matching source to need avoids unnecessary cost and risk [An].')

q('Evaluate whether setting budgets is important to a farming business success [12]')
p('For: seasonal, uncertain income and large costs [App], so budgets aid planning, cost control and monitoring [An], cutting the risk of running short of cash [An].')
p('Against: weather, disease and volatile prices [App] can make budgets quickly inaccurate [An], so yields and prices may matter more [An].')
p('Judgement: budgets are important for planning but must be flexible [Ev]; uncontrollable factors can undermine them [Ev], so they contribute to rather than guarantee success [Ev].')

q('Analyse two ways accurate cost information improves business performance [8]')
p('Setting prices [K/App]: knowing true unit cost [An] lets the firm price to cover costs and add a margin, ensuring profitable sales [An].')
p('Controlling/cutting costs [K/App]: spotting high-cost areas [An] to target savings, reducing waste and improving margins [An].')

q('Evaluate whether cash flow forecasting is the most important activity for a new restaurant [12]')
p('For: high start-up costs and uncertain revenue [App], so forecasting warns of shortages [An], letting the owner arrange finance and avoid running out of cash [An].')
p('Against: food quality, location, service and marketing also decide success [App]; without customers no forecast helps [An/An].')
p('Judgement: forecasting is essential for survival but not the single most important - it works alongside the factors that attract customers [Ev]; partly valid [Ev].')

q('Analyse two purposes of a cash flow forecast [8]')
p('Anticipating shortages [K/App]: arrange an overdraft or delay spending [An], avoiding inability to pay wages/suppliers and insolvency [An].')
p('Supporting finance/planning [K/App]: shown to lenders and used to plan investment [An], improving loan chances and timing major spend [An].')

q('Evaluate whether break-even analysis is the most important finance activity for a new bicycle manufacturer [12]')
p('For: high fixed costs [App], so break-even shows how many bikes must sell to avoid a loss [An], helping set output/price and judge viability [An].')
p('Against: cash flow and finance sources are also crucial [App]; break-even ignores day-to-day cash and rests on estimates [An/An].')
p('Judgement: break-even is useful for planning but cash-flow management is arguably more important for survival [Ev]; it depends on the estimates, so partly valid [Ev].')

q('Analyse the benefits of using break-even analysis [8]')
p('Setting output/sales targets [K/App]: the minimum sales to avoid a loss [An], helping plan production and judge a launch [An].')
p('Assessing decisions/margin of safety [K/App]: modelling changes in price/costs and how far sales can fall [An], enabling lower-risk decisions [An].')

q('Discuss the most appropriate source of finance for a private limited company to buy a factory [12]')
p('Bank loan: a large lump sum repaid over years [App], matching the factory long life and keeping control [An], but adding interest and repayment risk [An].')
p('Share issue (to private investors): raises finance without interest [App], easing cash flow [An], but dilutes control and shares profit [An].')
p('Judgement: a long-term bank loan is usually most appropriate - it matches the asset and keeps ownership [Ev], provided cash flow covers repayments [Ev]; it depends on control wishes and existing debt, so a share issue is the alternative if debt is to be avoided [Ev].')

# =====================================================================
h1('6. Data-response case studies')

h2('Great Resources (GR) - marketing/finance')
q('(b)(i) Calculate GR market share by revenue [3]')
p('Market share = (GR revenue / total market) x 100 = (15/500) x 100 = 3%.')
q('(c) Analyse one advantage and one disadvantage of a bank overdraft [8]')
p('Advantage: an overdraft [K] gives flexible short-term cash for GR poor cash flow [App], covering day-to-day bills with interest only on the amount used [An], so GR keeps trading and avoids insolvency [An].')
p('Disadvantage: overdrafts have high interest and are repayable on demand [K]; as GR only debt with weak cash flow [App], interest adds cost [An] and a recall could force closure [An].')
q('(d) Evaluate whether price or promotion is the most important element of GR marketing mix [12]')
p('Promotion: GR problem is low awareness/conversion vs trusted EM, with tiny ad spend ($7,500 vs $45,000) [App], so promotion raises awareness and trials [An], lifting its 3% share and $15,000 revenue [An].')
p('Price: penetration pricing won its first 250 subscribers [App], and free-trial users not converting shows price/value drives retention [An/An].')
p('Judgement: promotion is most important now given low awareness and a dominant rival [Ev], but depends on limited finance and must pair with a converting price [Ev]; elements are interdependent but promotion is the priority [Ev].')

h2('Child Play (CP) - marketing/finance')
q('(c) Analyse one advantage and one disadvantage of using working capital to finance the new cafe [8]')
p('Advantage: working capital [K] avoids interest/debt and is immediately available [App]; as Su plans to open in four weeks [App], it is fast and cheap, so the cafe opens on time and earns sooner [An].')
p('Disadvantage: diverting it reduces cash to run CP [K/App], risking liquidity problems that stop CP paying its own bills [An], threatening the existing business (opportunity cost) [An].')
q('(d) Evaluate appropriate promotion methods for the new cafe [12]')
p('Low-cost social media [App] is quick and cheap, reaching local parents and driving footfall [An]; on-site promotion at the play-area entrance [App] targets a captive audience of parents at near-zero cost [An].')
p('Judgement: low-cost digital plus on-site promotion is most appropriate given her tight budget and four-week timescale [Ev]; mass advertising is not justified [Ev]; it depends on time/skill, so exploit the existing customer base first [Ev].')

h2('Cartoon Costumes (CC) - finance')
q('(b)(i) Calculate the change in working capital 2021-2022 [3]')
p('Working capital = current assets - current liabilities. 2021 = 50 - 45 = $5,000. 2022 = 60 - 40 = $20,000. Change = +$15,000 increase.')
q('(c) Analyse one advantage and one disadvantage of crowdfunding [8]')
p('Advantage: as an ecommerce firm with wide-appeal costumes [App], online crowdfunding raises funds without a loan/interest [An] and publicises the products, boosting sales [An].')
p('Disadvantage: it may miss its target and exposes the idea [K]; as costumes are easy to copy [App], rivals could imitate designs and, if the target is missed, CC gets nothing, stalling growth [An/An].')
q('(d) Recommend which person Ava should employ - Liu or Ahura [12]')
p('Ahura: 10 years managing a clothing shop, strong admin, motivated, works alone, no wish to leave [App], so Ava can focus on design with a stable, experienced salesperson [An/An].')
p('Liu: explicit customer-service skills and cheaper, but wants university and to run their own business [App], likely leaving soon and causing turnover [An/An].')
p('Judgement: recommend Ahura, because the role needs relevant experience, independence and stability to free Ava to design [Ev]; it depends on the employment gap and budget, but Liu likely short stay makes Ahura the stronger fit [Ev].')

h2("Priya's Bookshop (PB) - cash flow")
q('(b)(i) Calculate the month-3 closing balance (X) [2]')
p('Month 3 net = 11 - 13 = -2; closing = opening (-1) + (-2) = -$3 (in $000).')
q('(b)(ii) Analyse two benefits of a cash flow forecast [8]')
p('It shows shortages early - negative closing balances in months 2 and 3 [App] - so she can arrange finance or cut spending in advance [An], avoiding inability to pay bills [An].')
p('It strengthens the grant application, of which it formed part [App], showing careful planning [An], raising the chance of approval - as happened, giving PB $20,000 [An].')
q('(d) Recommend promotional methods to raise awareness of PB [12]')
p('Tie into the town booktown branding and tourist flow [App], cheaply reaching book-interested visitors [An]; low-cost social media guided by segmentation targets adult local readers [App/An].')
p('Judgement: combine booktown/tourist channels with segmentation-led social media, as both are cheap and targeted [Ev]; mass advertising is unjustified given weak early cash flow [Ev]; leverage free booktown publicity first [Ev].')

h2('Great Desks (GD) - cash flow/management')
q('(b)(i) Calculate the 2025 closing balance [3]')
p('2025 net = inflow 9.0 - outflow 12.0 = -3.0; opening = 2024 closing 1.0; closing = 1.0 + (-3.0) = -$2.0m.')
q('(c) Analyse two sources of finance for the new shop [8]')
p('Bank loan [K]: could give the full $2m [App] to open the shop and capture rising home-desk demand, spread over time [An], but interest/repayments raise risk as cash flow turns negative [An].')
p('Members capital/retained profit [K]: as an employee co-operative it can raise funds internally [App] with no interest or lost control [An], but low salaries and negative cash flow limit how much members can give [An].')
q('(d) Evaluate whether Steve management style will contribute to future success [12]')
p('For: a democratic, people-centred style fits a co-operative, raising motivation and commitment where salaries are low [App/An], supporting productivity and retention [An].')
p('Against: staff say he ignores long-term plans, threats and new ideas and decides by vote not merit [App]; in a competitive market with a $2m expansion this risks poor strategy [An/An].')
p('Judgement: his style is a strength for motivation but a weakness for strategy [Ev]; success needs decisive, forward-looking leadership too [Ev]; currently the weaknesses are more likely to harm success unless he adds strategic direction [Ev].')

h2('Fruit Farm (FF) - motivation/sustainability')
q('(b)(i) Calculate the difference between piece-rate and time-based pay [3]')
p('Piece rate = (5x2.00)+(2x1.50)+(4x3.00) = 10+3+12 = $25. Time-based = 8x$4.50 = $36. Difference = $11 more under time-based.')
q('(c) Analyse two non-financial motivators FF could use [8]')
p('Better induction and multi-skilling [K/App] make work varied and workers feel valued [An], raising motivation and productivity where morale is poor [An].')
p('A more participative style replacing autocratic management [K/App] makes pickers feel listened to, meeting esteem needs [An], improving morale and effort [An].')
q('(d) Evaluate the impact on FF stakeholders of improving sustainability [12]')
p('Positive: environment/community gain from less plastic and fewer chemicals [App/An]; customers and industry value it, improving reputation and B2B orders [An].')
p('Negative: owners face high machinery/method costs, cutting short-term profit [App/An]; capital-intensive packaging risks pickers jobs, and suppliers face disruption [An].')
p('Judgement: positive for environment/community/customers, costly for owners and risky for pickers jobs [Ev]; it depends on whether reputation/sales gains offset costs and on short vs long term [Ev]; likely net positive long term if well managed [Ev].')

h2('Plasshape (PS) - marketing/finance')
q('(b)(i) Calculate the change in forecast profit if the new product launches [3]')
p('Current profit = 40 - 26 - 6 = $8m. Launched: revenue 40x1.3 = 52; direct 26+6 = 32; indirect 6+1 = 7; profit = 52-32-7 = $13m. Change = +$5m.')
q('(c) Analyse two elements of the marketing mix for the new packaging [8]')
p('Price [K/App]: as it costs more but adds value, a premium price covers cost and reflects value [An], balanced against B2B price sensitivity to protect margins and demand [An].')
p('Promotion [K/App]: B2B personal selling/trade promotion emphasising the environmental USP [An] wins eco-conscious food and cosmetics customers [An].')
q('(d) Evaluate whether PS should use the same payment method and employee development in both factories [12]')
p('For: standardising is fairer, meeting employee demands and improving morale [App/An]; development in both raises skills/productivity everywhere [An].')
p('Against: countries differ in cost of living, law and culture [App], so piece rate may suit V and time-based Z, and forcing identical costly systems may not fit [An/An].')
p('Judgement: offer development in both (raises productivity, meets demands), but adapt pay to local conditions [Ev]; it depends on cost differences and equity concerns, so a partial standardisation is likely best [Ev].')

h2('Delicious Cocoa (DC) - operations')
q('(b)(i) Calculate expected labour productivity in 2023 [3]')
p('2022 = 2000/500 = 4 tonnes/worker; 2023 (+5%) = 4 x 1.05 = 4.2 tonnes per worker.')
q('(c) Analyse two ways DC can motivate young people to work on its farms [8]')
p('Invest in training [K/App]: young workers gain skills and feel valued [An], raising motivation to work on the farms [An].')
p('Mechanise/vary roles [K/App]: less manual, more varied work [An] meets young people preferences and improves motivation to stay [An].')
q('(d) Evaluate whether DC should open its new cocoa processing factory [12]')
p('For: cocoa butter is a premium, higher-margin product [App], so processing its own beans adds value and raises profit [An/An].')
p('Against: DC is a co-operative with no retained earnings [App], so it must find ~$265,000 external finance [An]; the capital-intensive factory raises fixed costs and risk [An].')
p('Judgement: growth could be strong via higher margins [Ev], but depends on securing affordable finance and sufficient demand [Ev]; short-term risk is high but long-term margins attractive, so proceed only if financeable [Ev].')

h2('MX Bikes (MXB) - operations/marketing')
q('(b)(i) Calculate MXB market share of the mountain-bike market [3]')
p('Total market = 265+85+178+230+185+95+115+50 = 1203 ($000). Share = 265/1203 x 100 = 22.0% (approx 22%).')
q('(c) Analyse one advantage and one disadvantage of launching electric scooters [8]')
p('Advantage: scooters target a new, growing urban youth market [K/App], reducing reliance on declining bike sales [An], spreading risk and adding a revenue stream [An].')
p('Disadvantage: a new product in an unfamiliar market [K/App] needs investment with no guarantee of success [An]; as a premium-bike brand MXB may lack scooter expertise/fit, risking losses [An].')
q('(d) Evaluate how MXB can change its marketing mix to extend the mountain-bike life cycle [12]')
p('Product/promotion: update design and re-promote to high-income leisure users [App/An], reviving interest and slowing decline [An].')
p('Price/place: cutting price or widening distribution [App] boosts access [An] but risks the premium, exclusive image [An].')
p('Judgement: product updates and fresh promotion suit MXB best, reviving the range without harming its premium position [Ev]; changing price/place is riskier [Ev]; as demand is static, redesign and promotion to existing users is the safest route [Ev].')

h2('Custom Motorcycles (CM) - operations')
q('(b)(i) Calculate total market growth summer 2022 to summer 2023 [3]')
p('Total market rose from 5 to 7.5 (000 units). Growth = (7.5-5)/5 x 100 = 50%.')
q('(c) Analyse two impacts on CM of employees having a poor work-life balance [8]')
p('Falling motivation/quality [K/App]: stress and fatigue lower motivation [An], reducing the quality of high-end products and harming reputation [An].')
p('Higher labour turnover [K/App]: overworked skilled engineers leave [An], and as they are hard to replace, recruitment/training costs rise and expertise is lost [An].')
q('(d) Evaluate whether CM should change its method of production [12]')
p('For batch: demand grew 50% and lead times doubled to 10 weeks [App], so batch raises output and cuts lead times [An], relieving overworked engineers [An].')
p('Against: reputation rests on unique, high-quality job production [App], so batch could cut customisation/quality customers pay a premium for [An], losing the specialist market [An].')
p('Judgement: it depends on balancing demand against quality/USP [Ev]; batch eases capacity but risks exclusivity [Ev]; a hybrid - more engineers plus some new technology - likely best, so CM should not fully abandon job production [Ev].')

h2("Fretter's Music (FM) - operations")
q('(b)(i) Calculate FM labour turnover for 2022 [3]')
p('Left = 4+6+5+3+6 = 24. Turnover = 24/108 x 100 = 22.2% (approx 22%).')
q('(c) Analyse two impacts on FM costs if it enters international markets [8]')
p('Higher marketing/distribution costs [K/App]: an unknown brand needs heavy marketing and new distribution [An], raising costs before international sales are earned [An].')
p('Higher supply-chain/production costs [K/App]: changing the supply chain and raising output increases purchasing, transport and possibly tariff costs [An], squeezing margins until volumes rise [An].')
q('(d) Evaluate the impact on FM stakeholders of moving from batch production to mass customisation [12]')
p('Positive: customers get personalised instruments at reasonable prices [App/An]; owners could gain higher sales and differentiation [An].')
p('Negative: employees face pressure on quality/speed, worsening FM already high turnover [App/An]; owners must invest in new technology, raising cost/risk short term [An].')
p('Judgement: positive for customers and, if successful, owners, but risky for employees and costly [Ev]; it depends on managing the transition and supporting staff [Ev]; net positive if FM tackles its turnover problem alongside it [Ev].')

h2('Motorcycle Components (MC) - operations')
q('(c) Analyse two benefits of JIT [8]')
p('Lower storage costs/freed cash: MC holds only $1m inventory [App], spending little on storage and tying up little capital [An], improving cash flow and profit [An].')
p('Fresh, quality output and short lead times: good supplier relationships make JIT reliable [App], helping meet demand for quality and short lead times in a competitive market [An].')
q('(d) Evaluate the possible impact of introducing process innovation [12]')
p('For: $4m automation raises productivity and consistency [App], lowering unit cost and improving quality [An], strengthening competitiveness and profit [An].')
p('Against: the large capital outlay raises fixed costs and break-even [App/An], and automation could cut skilled workers, harming morale and MC valued low turnover [An].')
p('Judgement: likely beneficial long term if well managed (Jay plans good communication and involvement) [Ev]; it depends on the payback and retaining skilled staff [Ev]; short-term cost/risk rises but long-term competitiveness improves [Ev].')

h2('Planting Pots (PP) - sources of finance')
q('(b)(i) Calculate the change in PP market share 2020-2021 [3]')
p('2020 = 0.8/3.2 x 100 = 25%. 2021 = 0.82/4.1 x 100 = 20%. Change = a fall of 5 percentage points.')
q('(c) Analyse two factors affecting PP choice of finance for the factory [8]')
p('Cost/size needed [K/App]: $1.5m is large and long-term, suiting a loan or share issue [An]; a short-term overdraft would be unsuitable and costly [An].')
p('Ownership/control [K/App]: as a plc it could issue shares, but this dilutes Kabir and Emily 50% stake [An], so wanting control may favour a loan despite interest [An].')
q('(d) Evaluate PP use of different payment methods for its employees [12]')
p('For: each method suits its role - piece rate for designers, time-based for machine workers, profit sharing for managers [App/An] - motivating each appropriately and raising productivity [An].')
p('Against: piece rate for creative designers may harm quality by rushing creativity [App/An], and different methods can seem unfair, lowering morale [An].')
p('Judgement: matching method to role is broadly sensible [Ev], but piece rate for designers is poorly matched, since quality matters more than speed [Ev]; it depends on perceived fairness, so PP should reconsider paying designers by piece rate [Ev].')

h2('Office Furniture Designs (OFD) - cash flow')
q('(b)(i) Calculate the August 2023 closing balance [3]')
p('August net = 39 - 72 = -33; opening = July closing -81; closing = -81 + (-33) = -$114 (in $000).')
q('(c) Analyse two benefits of induction training [8]')
p('Faster settling-in [K/App]: new staff understand roles quickly and become productive sooner [An], supporting the high-quality service Markus wants [An].')
p('Fewer errors and better morale [K/App]: clear procedures/safety mean fewer mistakes and supported staff [An], improving service and cutting early turnover [An].')
q('(d) Evaluate whether Markus needs accurate cost information before setting up OFD [12]')
p('For: accurate costs enable pricing to cover costs and a realistic cash-flow forecast [App/An] - vital given large forecast negative balances - avoiding underpricing and insolvency [An].')
p('Against: start-up costs are only estimates [App]; market research and service quality also matter, and over-analysis delays launch [An/An].')
p('Judgement: he needs reasonably accurate cost information for pricing, cash flow and viability [Ev], but "accurate" cannot mean perfect and is not the only requirement [Ev]; necessary but not sufficient [Ev].')

h2('Move Well (MW) - cash flow/growth')
q('(b)(i) Calculate the forecast profit margin for year one [3]')
p('Profit = 110 - 50 - 20 = 40 ($000). Profit margin = 40/110 x 100 = 36.4%.')
q('(c) Analyse two benefits of process innovation to update information systems [8]')
p('Less wasted time/cost savings [K/App]: coordinated, up-to-date systems reduce wasted time [An], delivering the cost savings Effie wants [An].')
p('Better management information [K/App]: integrating three separate systems and paper records gives accurate accounts and data [An], improving decisions and control [An].')
q('(d) Evaluate the factors John needs to consider before opening in country P [12]')
p('Forecast profitability: revenue 110 vs costs 70, profit 40, margin 36.4% [App], attractive and supported by a growing housing market [An/An].')
p('MW situation/risk: home locations make losses and cash flow is pressured [App]; foreign expansion adds risk and cost [An/An].')
p('Judgement: the P location looks worthwhile given its margin and a growing market [Ev], but John must weigh MW losses, cash-flow pressure and foreign risk [Ev]; it depends on finance and forecast reliability, so proceed only if financeable and demand is sound [Ev].')

h2('Seaside Hotel (SH) - break-even/management')
q('(b)(i) Calculate the average margin of safety April-September 2021 [2]')
p('Rooms sold = 95% x 120 = 114 per night; margin of safety = 114 - 72 = 42 rooms per night.')
q('(c) Analyse one advantage and one disadvantage of Tia autocratic style [8]')
p('Advantage: quick decisions and clear direction for cleaners [K/App], so cleaning is done to standard consistently [An], maintaining hygiene efficiently [An].')
p('Disadvantage: cleaners/marketing staff are not consulted [K/App], so they feel undervalued and creativity is stifled [An], lowering morale and weakening ideas [An].')
q('(d) Recommend how SH could increase value added [12]')
p('Improve service quality/experience via training [App] to raise perceived value [An], allowing higher room rates [An]; leverage the sea views and restaurant joint venture [App] to differentiate cheaply [An].')
p('Judgement: focus on service quality and promoting the unique location/joint venture, as these build on strengths at low cost and justify higher prices [Ev]; a new restaurant is costly/risky [Ev]; it depends on willingness to pay, so invest in service and marketing rather than costly facilities [Ev].')

h2('Bear Bears (BB) - break-even/inventory/HRM')
q('(b)(i) Calculate BB fixed costs last month [3]')
p('Break-even = actual - margin of safety = 4000 - 120 = 3880 units. Fixed costs = 3880 x $6 contribution = $23,280.')
q('(c) Analyse two impacts of adopting JIT [8]')
p('Lower storage costs (positive): BB holds large temperature-controlled stock [App], so JIT cuts storage/holding costs [An], lowering costs and freeing cash [An].')
p('Supply risk (negative): BB promises delivery within a week and relies on cotton/fibre [App]; with no buffer stock a supplier delay halts production [An], missing the delivery promise and losing customers [An].')
q('(d) Evaluate the most likely impact of increased equality in the stitching department [12]')
p('For: fair facilities, tasks and pay [App] raise morale and productivity [An] and avoid discrimination claims that could damage the small partnership [An].')
p('Against: new washroom facilities and higher pay raise costs [App], and reallocating heavy lifting/machine fixing could slow others piece-rate output [An/An].')
p('Judgement: most likely positive overall - fairer treatment boosts motivation and removes discrimination risk [Ev]; it depends on cost versus benefit [Ev]; short-term costs rise but long-term morale, retention and reputation improve, so benefits outweigh costs [Ev].')

h2('Benjamin\'s Beds (BB) - costs/markets')
q('(b)(i) Calculate BB total annual cost using the new machinery [3]')
p('Variable cost = 40 x 7500 = 300,000; fixed cost = 500,000 x 0.90 = 450,000; total = $750,000.')
q('(c) Analyse two disadvantages of decreased staff morale and welfare [8]')
p('Falling productivity/quality [K/App]: less motivated workers give lower output and more errors [An], raising costs and threatening the quality brand image [An].')
p('Higher labour turnover [K/App]: unhappy staff leave or are absent [An], raising recruitment/training costs and disrupting flow production [An].')
q('(d) Recommend whether BB should focus on B2B or B2C [12]')
p('B2C: online orders and share grow rapidly, higher long-term potential, but needs marketing, retraining and a wider range [App/An].')
p('B2B: constant orders with low marketing cost, but under pressure to cut prices, squeezing margins [App/An].')
p('Judgement: prioritise growing B2C for its rapid growth and potential while keeping the stable B2B base [Ev]; it depends on finance for marketing/retraining and capacity [Ev]; if forced to choose one, B2C - provided BB funds the investment [Ev].')

h2('Farm Produce (FP) - costs/stakeholders')
q('(b)(i) Calculate FP profit in April 2022 [4]')
p('Revenue = (400x10)+(300x20)+(150x35) = 15,250. Variable = (400x8)+(300x10)+(150x15) = 8,450. Fixed = 3x2000 = 6,000. Profit = 15,250 - 8,450 - 6,000 = $800.')
q('(c) Analyse how two stakeholders are affected by stopping the small box [8]')
p('Customers [K/App]: lose the product they want, so may become dissatisfied and switch supplier [An], reducing FP custom [An].')
p('Employees [K/App]: less volume packed/delivered means fewer hours needed [An], threatening income and morale in this labour-intensive co-operative [An].')
q('(d) Evaluate the most important factor affecting supply of FP boxes [12]')
p('Cost of production: labour-intensive with a 10% minimum-wage rise [App], so labour costs rise, reducing willingness to supply at each price [An/An].')
p('Weather/seasonality: fresh produce depends on season and weather [App], which physically limits supply regardless of costs [An/An].')
p('Judgement: for a fresh-produce farm, weather/seasonality is arguably most important as it limits what can be supplied [Ev], with rising labour costs a close second [Ev]; it depends on the season, so seasonality leads [Ev].')

h2('Gold Theme Park (GT) - costs/intrapreneurship')
q('(b)(i) Calculate the change in GT total costs 2020-2022 [3]')
p('Total cost = revenue - profit. 2020 = 3.4 - 0.9 = 2.5; 2022 = 2.8 - 0.2 = 2.6 ($m). Change = +$0.1m.')
q('(c) Analyse two sources of secondary market research [8]')
p('Government/tourism statistics [K/App]: cheap data on tourist trends [An], showing whether the fall is market-wide or GT-specific [An].')
p('GT internal records [K/App]: past sales/visitor data reveal patterns behind the fall [An], guiding pricing and attraction decisions [An].')
q('(d) Evaluate the importance of developing intrapreneurship to GT ongoing success [12]')
p('For: visitors and revenue are falling and customers find it not fun and too expensive [App], so intrapreneurial staff generate new attractions/ideas [An], attracting visitors and reviving revenue [An].')
p('Against: price, marketing and attraction quality may matter more [App]; intrapreneurship needs skilled, motivated staff and is costly/risky [An/An].')
p('Judgement: important for the innovation needed to reverse decline [Ev], but not the most important - cutting the high price and improving marketing may be quicker [Ev]; it depends on staff capability, so valuable alongside pricing/promotion fixes [Ev].')

h2('Pop-up Movies (PM) - break-even')
q('(b)(i) Calculate the break-even number of customers for Venue B [3]')
p('Contribution per customer = 19 - 5 = $14. Break-even = fixed costs / contribution = 2000/14 = 142.9, so 143 customers.')
q('(c) Analyse two advantages of training the customer service workers [8]')
p('Better service [K/App]: customers are seated and helped effectively [An], improving the experience and encouraging repeat attendance and good word-of-mouth [An].')
p('Higher food/drink sales [K/App]: trained staff sell snacks and drinks more effectively [An], raising spend per customer and PM revenue/profit [An].')

h2("Jake's Cakes (JC) - cash flow/finance")
q('(b)(i) Calculate the March 2024 closing balance [3]')
p('March net = 5 - 2.3 = +2.7; opening = Feb closing -0.5; closing = -0.5 + 2.7 = +$2.2 (in $000, i.e. $2,200).')
q('(c) Analyse two benefits of digital promotion [8]')
p('Low cost [K/App]: cheap versus traditional advertising, suiting a small firm on retained earnings [An], promoting widely while protecting limited cash [An].')
p('Wide reach/shareability [K/App]: posts spread fast (as when a celebrity shared them) [An], reaching a huge audience quickly and attracting customers at little cost [An].')
q('(d) Evaluate whether a bank loan is the most appropriate source of finance for JC growth [12]')
p('For loan: $15,000 funds the garage conversion while Jake keeps full control [App], which he wants over an equal partner [An], with repayments spread and a business plan to support it [An].')
p('Against: interest must be paid regardless of sales [App], risky for a small firm with tight cash [An]; the investor $25,000 is larger and interest-free but costs half the business [An].')
p('Judgement: a bank loan is likely most appropriate, funding growth while keeping the control Jake values [Ev]; it depends on cash flow covering repayments given tight early balances [Ev]; the investor offers more but demands half, so the loan fits best if repayments are managed [Ev].')

sp()
p('End of booklet. Cross-check every answer against the official 9609 mark scheme. '
  'Answers are model guidance in the K/App/An/Ev format, not official Cambridge marking.')

pages = pdfgen.build_pdf(B, 'AS_Business_9609_Model_Answers.pdf',
                         footer_prefix='AS Business 9609 - Model Answers - Page')
print('Model Answers PDF: %d pages' % pages)
