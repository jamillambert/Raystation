# Creates a Couch ROI and then moves to align the top with the Couch POI
# Jamil Lambert 22/04/2022

from connect import *

case = get_current("Case")
examination = get_current("Examination")
patient_db=get_current('PatientDB')
structure_set = case.PatientModel.StructureSets[examination.Name]
poi_geometry = structure_set.PoiGeometries["Couch"]
couch = poi_geometry.Point
orientation = examination.PatientPosition

CouchTemplate = patient_db.LoadTemplatePatientModel(templateName='EVO Couchtop')
case.PatientModel.CreateStructuresFromTemplate(SourceTemplate=CouchTemplate, SourceExaminationName="CT 1", SourceRoiNames=["Couch Core Foam", "Couch Shell Carbon Fiber"], SourcePoiNames=[], AssociateStructuresByName=True, TargetExamination=examination, InitializationOption="AlignImageCenters")

boundingBox = structure_set.RoiGeometries['Couch Shell Carbon Fiber'].GetBoundingBox()

dist = couch['y'] - boundingBox[0]['y']

if orientation == 'HFP' or orientation = 'FFP':
    TransMatrix = {'M11':-1, 'M12':0, 'M13':0, 'M14':0,
    'M21':0, 'M22':-1, 'M23':0, 'M24':dist,
    'M31':0, 'M32':0, 'M33':1, 'M34':0,
    'M41':0, 'M42':0, 'M43':0, 'M44':1}
if orientation == 'HFS' or orientation = 'FFS':
    TransMatrix = {'M11':1, 'M12':0, 'M13':0, 'M14':0,
    'M21':0, 'M22':1, 'M23':0, 'M24':dist,
    'M31':0, 'M32':0, 'M33':1, 'M34':0,
    'M41':0, 'M42':0, 'M43':0, 'M44':1}

case.PatientModel.RegionsOfInterest['Couch Shell Carbon Fiber'].TransformROI3D(Examination=examination, TransformationMatrix=TransMatrix)
case.PatientModel.RegionsOfInterest['Couch Core Foam'].TransformROI3D(Examination=examination, TransformationMatrix=TransMatrix)

print(TransMatrix)