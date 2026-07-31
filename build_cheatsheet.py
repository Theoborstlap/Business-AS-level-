# -*- coding: utf-8 -*-
"""Builds AS_Business_9609_Cheat_Sheet.pdf - a single-page exam cheat sheet."""
import pdfgen

B = []
def p(t): B.append(('body', t))
def bu(t): B.append(('bullet', t))
def h3(t): B.append(('h3', t))

B.append(('h1', 'AS Business 9609 - One-Page Cheat Sheet'))
p('Everything you need in the exam: how to score K / App / An / Ev on 2-12 mark questions.')

h3('Marks -> what to write')
bu('2 = Define/State: a precise definition (2 elements). Knowledge only.')
bu('3 = Define + one developed sentence. K (with a little Analysis).')
bu('5 = Explain: ONE point - define [K] -> apply [App] -> develop [An].')
bu('8 = Analyse: TWO points, each K -> App -> An chain. No judgement.')
bu('12 = Evaluate: intro [K], FOR + AGAINST (K/App/An), then a judgement [Ev].')

h3('The 4 skills')
bu('[K] Knowledge: define/state the correct term or theory.')
bu('[App] Application: use the actual business, product, people or data given.')
bu('[An] Analysis: a "so... / which means..." chain ending in a business effect.')
bu('[Ev] Evaluation: a justified judgement - 12-mark questions only.')

h3('The chain formula (use it every time)')
p('Point + define [K] -> link to the business [App] -> which means... -> so... -> as a result... [An] '
  '-> (on balance / it depends... [Ev], 12 marks only).')
p('Where each goes: K first, App second, every link after that = An, and Ev in a final paragraph.')

h3('Connectives -> destinations')
bu('Links: which means, so, therefore, as a result, this leads to, ultimately.')
bu('End on: revenue, costs, profit, cash flow, market share, productivity or survival.')

h3('Judgement - the Ev marks on 12-markers')
bu('Give a clear decision AND say WHY one side outweighs the other.')
bu('Add "it depends on...", short vs long term, and link to THIS business. Spend about a third here.')

h3('Ask yourself before moving on')
bu('Defined it? (K)   Named the business? (App)   Reached an effect? (An)   Judged it, if 12 marks? (Ev)')

h3('Avoid')
bu('Stopping the chain early; listing instead of linking; no application; no judgement on a 12-marker.')

pages = pdfgen.build_pdf(B, 'AS_Business_9609_Cheat_Sheet.pdf',
                         footer_prefix='AS Business 9609 - Cheat Sheet - Page')
print('Cheat sheet PDF: %d page(s)' % pages)
