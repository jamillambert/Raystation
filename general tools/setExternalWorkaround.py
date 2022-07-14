# Adds "External1" to "External" due to a bug preventing ROI algebra when the External is locked on another image

from connect import *

case = get_current("Case")
examination = get_current("Examination")


with CompositeAction('ROI Algebra(Add External1 to External)'):

  case.PatientModel.RegionsOfInterest['External'].CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"External", r"External1"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })

  # CompositeAction ends 

