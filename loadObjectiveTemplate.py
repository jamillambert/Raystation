
from connect import *

case = get_current("Case")
beam_set = get_current("BeamSet")
plan = get_current("Plan")
patient_db = get_current("PatientDB")
template1Name = 'JL_PEARL_Phase_1'

tbl = patient_db.LoadTemplateOptimizationFunctions(templateName = template1Name, lockMode = 'Read')
plan.PlanOptimizations[0].ApplyOptimizationTemplate(Template=tbl)

print('END')