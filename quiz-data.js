/* AS Business 9609 - 2-mark definitions quiz data + grading logic.
   Each item has two mark points (p1, p2). A point is awarded if the typed
   answer contains ANY of that point's accepted keywords/synonyms.
   2 points = correct, 1 = partially correct, 0 = wrong.
   Grading is keyword-based, so it is a guide - phrase answers in your own
   words and check against the model answer shown. */

function normalizeText(s) {
  return (" " + String(s).toLowerCase() + " ")
    .replace(/[^a-z0-9%.$ ]/g, " ")
    .replace(/\s+/g, " ");
}

function pointHit(answerNorm, synonyms) {
  for (var i = 0; i < synonyms.length; i++) {
    var k = normalizeText(synonyms[i]).trim();
    if (k && answerNorm.indexOf(k) !== -1) return true;
  }
  return false;
}

function gradeAnswer(answer, item) {
  var a = normalizeText(answer);
  var p1 = pointHit(a, item.p1);
  var p2 = pointHit(a, item.p2);
  var marks = (p1 ? 1 : 0) + (p2 ? 1 : 0);
  return { marks: marks, p1: p1, p2: p2 };
}

var QUIZ_DATA = [
  // ---------------- Topic 1 ----------------
  {q:"Added value", t:1, p1:["selling price","sales price","price it sells","price charged","difference between price"], p2:["bought-in","bought in","cost of material","cost of the material","raw material","input cost","cost of inputs"], m:"The difference between the selling price of a product and the cost of the bought-in materials/inputs used to make it."},
  {q:"Opportunity cost", t:1, p1:["next best","best alternative","alternative"], p2:["given up","give up","forgone","foregone","sacrific","not chosen","forego"], m:"The benefit of the next best alternative given up when a choice is made."},
  {q:"Factors of production", t:1, p1:["resource","input"], p2:["produc","goods","services","make"], m:"The resources (land, labour, capital and enterprise) used by a business to produce goods and services."},
  {q:"Entrepreneur", t:1, p1:["sets up","set up","starts","start a business","owns and runs","establishes","creates a business"], p2:["risk","combines the factors","organises"], m:"A person who sets up and runs a business, taking the financial risk in the hope of profit."},
  {q:"Intrapreneur", t:1, p1:["employee","within","existing business","inside"], p2:["innovat","new idea","new product","entrepreneurial","creative"], m:"An employee who uses entrepreneurial skills to develop new ideas/products within an existing business."},
  {q:"Business plan", t:1, p1:["document","written","report"], p2:["objective","strategy","forecast","future","aims","how the business"], m:"A document setting out a business's objectives, strategy and financial forecasts, often used to raise finance."},
  {q:"Franchise", t:1, p1:["right to","permission","licen","granted","trade under","use the brand","use the name","sell the products"], p2:["fee","royalt","payment","percentage","franchisor","existing business","another business","established business"], m:"An arrangement where a franchisee is granted the right to trade under a franchisor's brand/sell its products, usually in return for a fee/royalties."},
  {q:"Sole trader", t:1, p1:["one owner","single owner","one person","individual","owned by one"], p2:["unlimited liability","full control","alone","keeps all profit","sole"], m:"A business owned and controlled by one person, who has unlimited liability."},
  {q:"Partnership", t:1, p1:["two or more","2 or more","two to twenty","partners","more than one owner"], p2:["share","jointly","unlimited liability","deed"], m:"A business owned by two or more people who share responsibility, profits and (usually) unlimited liability."},
  {q:"Private limited company (Ltd)", t:1, p1:["shares","shareholders","privately","not sold to the public","cannot sell shares to the public"], p2:["limited liability","separate legal","incorporated"], m:"An incorporated business whose shares are sold privately and whose owners have limited liability."},
  {q:"Public limited company (Plc)", t:1, p1:["stock exchange","public","shares to the public"], p2:["limited liability","incorporated"], m:"An incorporated business that can sell its shares to the public on the stock exchange; owners have limited liability."},
  {q:"Co-operative", t:1, p1:["members","owned and run by","jointly owned"], p2:["share profit","shared profit","democratic","one member one vote","equal"], m:"A business owned and run by its members, who share the profits and decision-making equally."},
  {q:"Joint venture", t:1, p1:["two businesses","two or more businesses","two companies","two firms"], p2:["separate business","new business","share cost","share risk","combine"], m:"When two or more businesses join to form/run a separate business, sharing costs, risks and rewards."},
  {q:"Social enterprise", t:1, p1:["social","environmental","community"], p2:["reinvest","not for profit","surplus","trades","for society"], m:"A business that trades to achieve social/environmental objectives and reinvests its profits for society."},
  {q:"Limited liability", t:1, p1:["not personally","not responsible for all","only lose","limited to","separate legal"], p2:["amount invested","amount they invest","their investment","personal assets","personal possessions"], m:"Owners are only liable for the amount they invested; their personal assets are protected."},
  {q:"Unlimited liability", t:1, p1:["personally responsible","personally liable","responsible for all","liable for all debts"], p2:["personal assets","personal possessions","own assets","home","savings"], m:"The owner is personally responsible for all the business's debts; personal assets can be used to pay them."},
  {q:"Primary sector", t:1, p1:["extract","natural resource","raw material"], p2:["farming","agriculture","mining","fishing","oil","forestry"], m:"The sector that extracts natural resources/raw materials, e.g. farming, mining, fishing."},
  {q:"Secondary sector", t:1, p1:["manufactur","makes","produces","processes","construction"], p2:["raw material","into goods","finished goods","product"], m:"The sector that manufactures/processes raw materials into finished goods, e.g. car making, construction."},
  {q:"Tertiary sector", t:1, p1:["service"], p2:["retail","banking","transport","tourism","insurance","shop"], m:"The sector that provides services, e.g. retail, banking, transport."},
  {q:"Quaternary sector", t:1, p1:["knowledge","information","intellectual"], p2:["research","r d","ict","consult","technology","data"], m:"The knowledge/information-based sector, e.g. R&D, ICT, consultancy."},
  {q:"Public sector", t:1, p1:["government","state","local authority","council"], p2:["owned","controlled","provide","services","public"], m:"The part of the economy owned and controlled by the government, providing services to the public."},
  {q:"Private sector", t:1, p1:["private individual","individuals","businesses","not government","non-government"], p2:["owned","profit"], m:"The part of the economy owned and run by private individuals/businesses, usually to make a profit."},
  {q:"Organic (internal) growth", t:1, p1:["internal","own resources","from within","itself"], p2:["expand","more outlet","new product","increasing output","without merger","without takeover","opening"], m:"Internal growth achieved by a business expanding using its own resources, without merger or takeover."},
  {q:"Merger", t:1, p1:["two businesses","two companies","two firms","two or more"], p2:["agree to join","combine","join together","become one"], m:"When two businesses agree to join together to form one new business."},
  {q:"Takeover", t:1, p1:["buys","acquires","purchase"], p2:["control","majority","more than 50","another business","another company"], m:"When one business buys a controlling interest (over 50% of shares) in another business."},
  {q:"Horizontal integration", t:1, p1:["same industry","same stage","same type","same market"], p2:["merger","takeover","combine","join","two business"], m:"A merger/takeover between two businesses in the same industry and at the same stage of production."},
  {q:"Vertical integration", t:1, p1:["different stage","different level","same industry"], p2:["supplier","customer","backward","forward","distributor"], m:"A merger/takeover with a business at a different stage of the same industry (a supplier or a customer)."},
  {q:"Conglomerate (diversification)", t:1, p1:["unrelated","different industr","different market","no connection"], p2:["spread risk","diversif","merger","takeover"], m:"A merger/takeover between businesses in different, unrelated industries, which spreads risk."},
  {q:"Stakeholder", t:1, p1:["individual","group","person","organisation"], p2:["interest in","affected by","affect the business","affects the business","impact"], m:"An individual or group with an interest in, or affected by, the activities of a business."},
  {q:"Mission statement", t:1, p1:["purpose","reason","why"], p2:["overall aim","aim","goal","values","exists"], m:"A statement of the overall purpose and aims of a business - why it exists."},
  {q:"Corporate social responsibility (CSR)", t:1, p1:["society","social","environment","community","stakeholders"], p2:["responsib","duty","beyond profit","ethical","obligation"], m:"The idea that a business has a responsibility towards society and the environment, beyond just making a profit."},
  {q:"SMART objectives", t:1, p1:["specific","measurable"], p2:["achievable","realistic","time","attainable"], m:"Objectives that are Specific, Measurable, Achievable, Realistic and Time-limited."},
  {q:"Family business", t:1, p1:["owned","run","controlled","managed"], p2:["family","relatives"], m:"A business owned and/or controlled by members of the same family."},

  // ---------------- Topic 2 ----------------
  {q:"Human resource management (HRM)", t:2, p1:["managing","management of","people","employees","workforce","staff"], p2:["objective","recruit","train","motivat","develop","organisational"], m:"The management of an organisation's workforce - planning, recruiting, training and motivating staff to meet objectives."},
  {q:"Workforce planning", t:2, p1:["forecast","assess","planning","predict","future"], p2:["number","skills","workers needed","staff needed","employees needed"], m:"Forecasting the number and skills of workers a business will need in the future, and how to meet that need."},
  {q:"Labour turnover", t:2, p1:["percentage","proportion","rate","%"], p2:["leaving","leave","left"], m:"The percentage of a workforce that leaves a business over a period (usually one year)."},
  {q:"Recruitment", t:2, p1:["process","attract","find","identify"], p2:["employ","staff","worker","candidate","fill","vacancy","hire"], m:"The process of identifying the need for, and attracting/appointing, suitable employees."},
  {q:"Job description", t:2, p1:["duties","tasks","responsibilities"], p2:["job","role","post","position"], m:"A document outlining the duties, tasks and responsibilities of a particular job."},
  {q:"Person specification", t:2, p1:["skills","qualities","qualifications","characteristics","attributes","experience"], p2:["candidate","ideal","suitable","required for","needed for","employee"], m:"A document listing the skills, qualifications and qualities required of the ideal candidate for a job."},
  {q:"Internal recruitment", t:2, p1:["vacancy","post","position","job filled","appointing","recruiting"], p2:["within","existing employ","existing staff","inside the business","current employ"], m:"Filling a job vacancy with someone already employed within the business."},
  {q:"External recruitment", t:2, p1:["vacancy","post","position","appointing","recruiting"], p2:["outside","external","new to the business","not currently employed"], m:"Filling a job vacancy with someone from outside the business."},
  {q:"Induction training", t:2, p1:["new employ","new staff","new worker","new recruit"], p2:["introduce","familiaris","settle","learn about","workplace","the job"], m:"Training given to new employees to introduce them to the business and their role."},
  {q:"On-the-job training", t:2, p1:["training","learning"], p2:["while working","at work","workplace","doing the job","watching","alongside"], m:"Training carried out while doing the job, at the workplace."},
  {q:"Off-the-job training", t:2, p1:["training","learning","course"], p2:["away from","outside the workplace","external","college","off site"], m:"Training carried out away from the workplace (e.g. at a college or training centre)."},
  {q:"Redundancy", t:2, p1:["no longer needed","no longer required","not needed","let go"], p2:["job no longer exists","role no longer","not their fault","not the worker","restructur","closure"], m:"When an employee loses their job because it is no longer needed (the job ceases to exist), not due to their fault."},
  {q:"Dismissal", t:2, p1:["end","terminat","sack","fired","contract ended"], p2:["conduct","behaviour","performance","misconduct","broke","breach"], m:"When an employee's contract is ended because of their poor conduct or performance."},
  {q:"Motivation", t:2, p1:["desire","willingness","drive","reason","want"], p2:["work","achieve","effort","goals","tasks"], m:"The desire or drive that makes someone want to work hard and achieve goals."},
  {q:"Empowerment", t:2, p1:["giving","allowing","delegat"], p2:["control","authority","power","make decisions","own work","responsibility"], m:"Giving employees greater control and authority over their own work and decisions."},
  {q:"Job enrichment", t:2, p1:["challenging","meaningful","interesting","complex","varied"], p2:["responsibility","motivat","fulfil","develop"], m:"Giving employees more challenging, meaningful tasks and responsibility to motivate them."},
  {q:"Piece rate", t:2, p1:["pay","paid","payment","wage"], p2:["per unit","per item","per piece","each unit","amount produced","output"], m:"A payment method where workers are paid a set amount for each unit they produce."},
  {q:"Salary", t:2, p1:["fixed","set amount","annual","yearly"], p2:["monthly","month","per year","installments","regular"], m:"A fixed annual amount of pay, usually paid in equal monthly installments."},
  {q:"Commission", t:2, p1:["pay","payment","paid"], p2:["sales","percentage","% of","per sale","amount sold"], m:"Payment based on a percentage of the sales a worker makes."},
  {q:"Fringe benefits", t:2, p1:["non-cash","non cash","extra","perk","additional"], p2:["in addition to","on top of pay","car","insurance","discount","reward"], m:"Non-cash rewards given in addition to pay (e.g. company car, health insurance)."},
  {q:"Delegation", t:2, p1:["passing","giving","assign"], p2:["authority","task","responsibility","subordinate","junior","lower"], m:"Passing authority/tasks down from a manager to a subordinate."},
  {q:"Trade union", t:2, p1:["organisation","group of workers","group of employees","association"], p2:["represent","protect","interests","rights","negotiate","behalf"], m:"An organisation of workers that represents and protects their interests (e.g. pay and conditions)."},
  {q:"Collective bargaining", t:2, p1:["negotiat","bargain"], p2:["union","employer","on behalf","group of workers","collectively"], m:"Negotiation over pay/conditions between a trade union (on behalf of workers) and employers."},
  {q:"Autocratic leadership", t:2, p1:["makes all decisions","makes the decisions","sole decision","leader decides"], p2:["no consultation","without consulting","one-way","tells","orders","little input"], m:"A leadership style where the leader makes all the decisions with little consultation of staff."},
  {q:"Democratic leadership", t:2, p1:["consult","shared","share decision","discuss"], p2:["staff","employees","involved","participate","input","team"], m:"A leadership style where staff are consulted and involved in decision-making."},
  {q:"Laissez-faire leadership", t:2, p1:["little direction","minimal","hands off","leaves"], p2:["own decisions","freedom","decide for themselves","autonomy"], m:"A leadership style where the leader gives little direction and employees make their own decisions."},
  {q:"Paternalistic leadership", t:2, p1:["makes decision","leader decides","in charge"], p2:["best interest","welfare","consults","looks after","like a parent","staff needs"], m:"A leadership style where the leader makes decisions but in what they believe is the best interest of staff."},

  // ---------------- Topic 3 ----------------
  {q:"Marketing", t:3, p1:["identify","anticipat","meeting","finding"], p2:["customer needs","customer wants","satisf","profit","demand"], m:"The process of identifying, anticipating and satisfying customer needs profitably."},
  {q:"Market share", t:3, p1:["percentage","proportion","%","part of"], p2:["total sales","total market","one business","a firm","a product","company sales"], m:"The proportion of total sales in a market held by one business or product, as a percentage."},
  {q:"Market growth", t:3, p1:["increase","rise","expansion","change in size"], p2:["market","over time","total sales","period","percentage"], m:"The increase in the size (total sales) of a market over a period of time, as a percentage."},
  {q:"Market orientation", t:3, p1:["customer needs","market research","customer","market led","market-led"], p2:["produce to match","based on","design products","then produce","meet those needs"], m:"An approach where a business researches customer needs first, then designs products to match."},
  {q:"Product orientation", t:3, p1:["product","making the product","the good","technical"], p2:["then find","find buyers","product-led","product led","without research","then sell"], m:"An approach where a business focuses on making the product first, then tries to sell it."},
  {q:"Market segmentation", t:3, p1:["divid","split","break","separate"], p2:["groups","segments","similar","characteristics","needs"], m:"Dividing a market into distinct groups of customers with similar characteristics/needs."},
  {q:"Niche marketing", t:3, p1:["target","aim","focus"], p2:["small","specific","narrow","specialist","segment","gap"], m:"Aiming a product at a small, specific segment of a market."},
  {q:"Mass marketing", t:3, p1:["target","aim","sell to"], p2:["whole market","large market","entire","everyone","broad","undifferentiated"], m:"Aiming a product at the whole/large market rather than a specific segment."},
  {q:"Primary research", t:3, p1:["new data","first-hand","first hand","original","field"], p2:["specific purpose","survey","questionnaire","interview","observation","collected directly"], m:"The collection of new, first-hand data for a specific purpose (e.g. surveys, interviews)."},
  {q:"Secondary research", t:3, p1:["existing data","second-hand","second hand","desk","already"], p2:["collected by others","published","reports","internet","government","previously"], m:"The use of existing (second-hand) data that has already been collected by others."},
  {q:"Sampling", t:3, p1:["select","group","small number","sample"], p2:["represent","whole population","target market","larger group","population"], m:"Selecting a small group to represent the views of the whole population/target market."},
  {q:"Quantitative data", t:3, p1:["number","numerical","statistic","figures"], p2:["measured","how many","how much","quantity","amount"], m:"Data that can be measured and expressed in numbers (e.g. how many)."},
  {q:"Qualitative data", t:3, p1:["opinion","view","attitude","feeling","judgement"], p2:["why","reasons","non-numerical","descriptive","preferences"], m:"Data based on opinions, attitudes and reasons (why), rather than numbers."},
  {q:"Unique selling point (USP)", t:3, p1:["feature","special","unique","different","distinct","stands out"], p2:["competitor","rivals","other products","from others"], m:"The special feature of a product that makes it different from, and stand out against, competitors."},
  {q:"Product differentiation", t:3, p1:["different","distinct","stand out","distinguish","unique"], p2:["competitor","rivals","other products","from others"], m:"Making a product distinct/different from those of competitors."},
  {q:"Product life cycle", t:3, p1:["stages","phases"], p2:["launch","introduction","decline","over its life","sales over time"], m:"The stages a product passes through from introduction/launch to decline."},
  {q:"Brand", t:3, p1:["name","logo","symbol","design","identity"], p2:["identif","distinguish","recognis","different from","associated"], m:"A name, symbol or design that identifies a product and distinguishes it from competitors."},
  {q:"Penetration pricing", t:3, p1:["low price","low initial","cheap"], p2:["enter","gain market share","attract","new product","build sales"], m:"Setting a low initial price to enter a market and gain market share."},
  {q:"Price skimming", t:3, p1:["high price","high initial","premium"], p2:["new product","innovative","then lower","reduce later","unique"], m:"Setting a high initial price for a new/innovative product, then lowering it over time."},
  {q:"Price discrimination", t:3, p1:["different prices","varying price","vary the price"], p2:["different customer","different market","different times","different group","same product"], m:"Charging different prices to different customers/markets for the same product."},
  {q:"Dynamic pricing", t:3, p1:["prices change","varies","adjust","flexible price"], p2:["demand","real time","real-time","market conditions"], m:"Prices change in real time in response to the level of demand."},
  {q:"Psychological pricing", t:3, p1:["appear","seem","perception","attractive"], p2:["9.99","just below","round","feels cheaper"], m:"Setting a price that appears more attractive to customers (e.g. $9.99 instead of $10)."},
  {q:"Cost-plus pricing", t:3, p1:["mark-up","mark up","profit margin","percentage added","add profit"], p2:["cost","unit cost","cost of production"], m:"Setting price by adding a mark-up (profit margin) to the cost per unit."},
  {q:"Distribution channel", t:3, p1:["route","path","means","way","chain"], p2:["producer to consumer","manufacturer to customer","reach the customer","to the consumer","gets to"], m:"The route a product takes from the producer to the final consumer."},
  {q:"Customer relationship marketing (CRM)", t:3, p1:["relationship","building","maintaining"], p2:["customer","loyal","retain","long-term","repeat"], m:"Strategies to build long-term relationships with customers to increase loyalty and retention."},

  // ---------------- Topic 4 ----------------
  {q:"Productivity", t:4, p1:["output","production"], p2:["per worker","per input","per employee","per hour","per unit of input"], m:"A measure of output produced per unit of input (e.g. output per worker)."},
  {q:"Capacity utilisation", t:4, p1:["percentage","proportion","%"], p2:["maximum output","full capacity","potential output","being used","actual output"], m:"The proportion of a business's maximum possible output that is currently being used, as a percentage."},
  {q:"Efficiency", t:4, p1:["output","produc","making"], p2:["minimum waste","least cost","fewest resources","without waste","low cost"], m:"Producing output with the minimum waste of resources/at lowest cost."},
  {q:"Job production", t:4, p1:["one","single","individual"], p2:["at a time","made to order","custom","unique","one-off","bespoke"], m:"Producing a single, one-off item at a time, often made to a customer's specific order."},
  {q:"Batch production", t:4, p1:["group","batch","quantities"], p2:["identical","same","stages","together"], m:"Producing goods in groups (batches), where each batch goes through a stage before the next."},
  {q:"Flow production", t:4, p1:["continuous","mass"], p2:["large quantit","identical","standardised","assembly line","large scale"], m:"Continuous production of large quantities of identical products (mass production)."},
  {q:"Mass customisation", t:4, p1:["flow","mass production","large scale","assembly"], p2:["customis","tailored","individual","personalis","customer choice"], m:"Using flow-production methods to make products tailored to individual customers."},
  {q:"Capital intensive", t:4, p1:["relies","uses mainly","mostly","high proportion"], p2:["machiner","equipment","capital","technology","automat"], m:"Production that relies mainly on machinery/equipment rather than labour."},
  {q:"Labour intensive", t:4, p1:["relies","uses mainly","mostly","high proportion"], p2:["labour","workers","people","staff","human"], m:"Production that relies mainly on labour (workers) rather than machinery."},
  {q:"Buffer inventory", t:4, p1:["minimum stock","minimum inventory","spare stock","extra stock","reserve"], p2:["in case","emergency","shortage","safety","unexpected","runs out"], m:"The minimum level of inventory held as a safety net in case of shortages or delays."},
  {q:"Lead time", t:4, p1:["time","period","gap"], p2:["order","receiv","delivery","arrives","between placing"], m:"The time between placing an order for inventory and receiving it."},
  {q:"Re-order level", t:4, p1:["level of stock","level of inventory","stock level","point"], p2:["new order","reorder","order is placed","triggers an order","order more"], m:"The level of inventory at which a new order is automatically placed."},
  {q:"Just in Time (JIT)", t:4, p1:["arrive","delivered","supplies"], p2:["as needed","when needed","just in time","little stock","no stock","minimal inventory"], m:"An inventory system where stock/inputs arrive just as they are needed, so little/no inventory is held."},
  {q:"Just in Case (JIC)", t:4, p1:["buffer","extra stock","spare stock","holding stock","large stock"], p2:["in case","demand","shortage","supply problem","unexpected"], m:"An inventory approach of holding buffer stock in case of unexpected demand or supply problems."},
  {q:"Outsourcing", t:4, p1:["outside","external","another business","third party","other firm"], p2:["carry out","task","work","produce","service","in-house"], m:"Using an outside business to carry out tasks/work previously done within the business."},
  {q:"Supply chain management", t:4, p1:["managing","manage","coordinat","control the flow"], p2:["supplier to customer","materials","goods","flow of goods","from supplier"], m:"Managing the flow of goods and materials from suppliers through to the final customer."},

  // ---------------- Topic 5 ----------------
  {q:"Working capital", t:5, p1:["current asset","current liabilit","assets minus","subtract"], p2:["day-to-day","day to day","daily","short-term","running the business","liquid"], m:"The finance available for the day-to-day running of a business (current assets minus current liabilities)."},
  {q:"Cash flow", t:5, p1:["money in and out","in and out","inflows and outflows","cash in","cash out"], p2:["business","over time","period"], m:"The flow of money into and out of a business over a period of time."},
  {q:"Cash flow forecast", t:5, p1:["prediction","predict","estimate","forecast","plan"], p2:["future cash","inflows","outflows","cash in and out","money coming"], m:"A prediction of the future cash inflows and outflows of a business."},
  {q:"Profit", t:5, p1:["revenue","income","sales","turnover"], p2:["costs","expenses","minus cost","less cost","exceed cost"], m:"The amount left when total costs are subtracted from total revenue."},
  {q:"Fixed costs", t:5, p1:["do not change","don t change","stay the same","constant","remain"], p2:["output","production","level of production","quantity","how much produced"], m:"Costs that do not change with the level of output (e.g. rent)."},
  {q:"Variable costs", t:5, p1:["change","vary","increase","rise"], p2:["output","production","quantity","level of production","how much produced","units"], m:"Costs that change directly with the level of output (e.g. raw materials)."},
  {q:"Direct costs", t:5, p1:["directly linked","directly related","directly attribut","clearly linked"], p2:["product","unit","output","specific","item"], m:"Costs that can be directly linked to a particular product or unit of output (e.g. materials)."},
  {q:"Indirect costs (overheads)", t:5, p1:["not directly","cannot be linked","not linked to one","not attributable"], p2:["one product","whole business","overhead","general","across"], m:"Costs that cannot be linked to a single product (overheads), e.g. rent, admin."},
  {q:"Contribution", t:5, p1:["selling price","price minus variable","revenue minus variable"], p2:["variable cost","fixed costs","towards fixed","cover fixed"], m:"Selling price minus variable cost per unit; it contributes towards paying fixed costs and profit."},
  {q:"Break-even", t:5, p1:["output","point","level","quantity"], p2:["equal","total cost","no profit","no loss","covers cost","neither"], m:"The level of output where total revenue equals total costs, so no profit or loss is made."},
  {q:"Margin of safety", t:5, p1:["actual output","current output","actual sales","difference"], p2:["break-even","break even","fall before","before a loss","before making a loss"], m:"The difference between actual output and the break-even output - how far sales can fall before a loss."},
  {q:"Budget", t:5, p1:["financial plan","plan","forecast"], p2:["future","period","target","ahead","in advance"], m:"A financial plan/target for a future period."},
  {q:"Variance", t:5, p1:["difference","gap"], p2:["budget","actual","planned and actual","forecast and actual"], m:"The difference between a budgeted (planned) figure and the actual figure."},
  {q:"Capital expenditure", t:5, p1:["non-current asset","fixed asset","non current asset","long-term asset"], p2:["machiner","building","equipment","premises","vehicles","long-term"], m:"Spending on non-current (fixed) assets such as machinery or buildings."},
  {q:"Revenue expenditure", t:5, p1:["day-to-day","day to day","daily","running costs","short-term"], p2:["wages","materials","rent","bills","expenses"], m:"Spending on day-to-day running costs such as wages, rent and raw materials."},
  {q:"Retained profit (earnings)", t:5, p1:["profit kept","kept in the business","retained","held back"], p2:["reinvest","not distributed","not paid out","ploughed back","after dividends"], m:"Profit kept within the business (rather than paid out) and reinvested."},
  {q:"Bank overdraft", t:5, p1:["withdraw more","spend more","negative balance","borrow from the bank"], p2:["short-term","short term","temporary","flexible"], m:"A facility allowing a business to withdraw more money than it has in its account (short-term borrowing)."},
  {q:"Debt factoring", t:5, p1:["invoice","receivable","debts owed","money owed"], p2:["third party","factor","immediate cash","quick cash","in return for cash"], m:"Selling unpaid invoices (receivables) to a third party in return for immediate cash."},
  {q:"Trade credit", t:5, p1:["buy now","goods now","receive goods","purchase"], p2:["pay later","delay payment","supplier later","after a period","credit period"], m:"Buying goods/materials now and paying the supplier at a later date."},
  {q:"Crowdfunding", t:5, p1:["large number of people","many people","the public","crowd"], p2:["online","platform","small amounts","each contribute","internet"], m:"Raising finance from a large number of people, each contributing a small amount, usually online."},
  {q:"Venture capital", t:5, p1:["finance","investment","capital","funds"], p2:["risky","high-risk","high growth","start-up","in return for shares","stake"], m:"Investment provided to high-risk/high-growth businesses, usually in exchange for a share in the business."},
  {q:"Leasing", t:5, p1:["rent","renting","pay to use","hire"], p2:["without owning","not own","instead of buying","over a period"], m:"Renting an asset (paying to use it) rather than buying/owning it."},
  {q:"Share capital", t:5, p1:["finance","money","capital","funds"], p2:["selling shares","issuing shares","sale of shares","shareholders"], m:"Finance raised by a company through the sale of shares."},
  {q:"Liquidity", t:5, p1:["ability to pay","able to pay","meet"], p2:["short-term debt","short term debt","bills","cash","when due"], m:"The ability of a business to pay its short-term debts as they fall due."},
  {q:"Bankruptcy", t:5, p1:["individual","person","sole trader"], p2:["cannot pay","unable to pay","cannot repay","debts"], m:"When an individual is legally declared unable to pay their debts."},
  {q:"Liquidation", t:5, p1:["company is closed","wound up","closed down","ceases"], p2:["assets sold","sell assets","pay creditors","repay debts"], m:"When a company is closed down and its assets are sold to repay creditors."}
];

if (typeof module !== "undefined" && module.exports) {
  module.exports = { QUIZ_DATA: QUIZ_DATA, gradeAnswer: gradeAnswer, normalizeText: normalizeText };
}
