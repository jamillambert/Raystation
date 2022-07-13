# Creates 2 ROIs below the treatment couch where the support bars are in the fully out position
# It requires a POI called "Couch" to be on the top of the treatment couch
#
# Jamil Lambert

from connect import *
import math

width = 5.7 #width of bars
barthickness = 9 #thickness of bars
seperation = 19.6 #half the distance from the bar to centre of couch
couchthickness = 2.9 #thickness of proton couch

case = get_current("Case")
examination = get_current("Examination")
slice_positions = examination.Series[0].ImageStack.SlicePositions 
structure_set = case.PatientModel.StructureSets[examination.Name]
poi_geometry = structure_set.PoiGeometries["Couch"]
couch = poi_geometry.Point
setupcheck = examination.PatientPosition
length = examination.Series[0].ImageStack.SlicePositions[-1]
start = examination.Series[0].ImageStack.Corner.z
centre = 0

print "POI position: {0}, {1}, {2}".format(couch.x, couch.y, couch.z)
if setupcheck == 'HFS' or setupcheck == 'FFS':
  setupcorrection = 7.4
  centre = start + (length/2)
else:
  setupcorrection = -7.4
  centre = start - (length/2)

with CompositeAction('Create Box ROI (ROI Proton Bars OUT)'):

  retval_0 = case.PatientModel.CreateRoi(Name=r"pb_temp1", Color="Red", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
  retval_0.CreateBoxGeometry(Size={'x':5.7, 'y':9, 'z':length}, Examination=examination, Center={'x':2.85+seperation,'y':couch.y+setupcorrection,'z':centre})
  retval_1 = case.PatientModel.CreateRoi(Name=r"pb_temp2", Color="Red", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
  retval_1.CreateBoxGeometry(Size={'x':5.7, 'y':9, 'z':length}, Examination=examination, Center={'x':-2.85-seperation,'y':couch.y+setupcorrection,'z':centre}) 

with CompositeAction('ROI Algebra (Proton Bars OUT)'):

  retval_0 = case.PatientModel.CreateRoi(Name=r"Proton Bars OUT", Color="255, 128, 0", Type="Undefined", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
  retval_0.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"pb_temp1"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"pb_temp2"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Union", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })


with CompositeAction('Delete ROI (pb_temp1, pb_temp2)'):

  case.PatientModel.RegionsOfInterest['pb_temp1'].DeleteRoi()
  case.PatientModel.RegionsOfInterest['pb_temp2'].DeleteRoi()


