# Script recorded 08 Apr 2020, 10:32:53

#   RayStation version: 9.0.0.113
#   Selected patient: ...

from connect import *
import ctypes

case = get_current("Case")
examination = get_current("Examination")
structure_set = case.PatientModel.StructureSets[examination.Name]
setupcheck = examination.PatientPosition


try:
	for points in case.PatientModel.PointsOfInterest:
		print(points.Type)
		if str(points.Type) == 'Isocenter':
			poi_name = points.Name
			iso_pos = structure_set.PoiGeometries[poi_name].Point
# Get POI coordinates

	iso_x = iso_pos.x
	iso_y = iso_pos.y
	iso_z = iso_pos.z
except:
	ctypes.windll.user32.MessageBoxW(0, "Script failed, Isocentre doesn't exist or set to wrong type.", "Error!", 1)
	sys.exit(1)

for structure in structure_set.RoiGeometries:
	if structure.OfRoi.Name == 'CBCT_SFOV':
		structure.OfRoi.DeleteRoi()


with CompositeAction('Create Cylinder ROI (CBCT_SFOV, Image set: pCT_2mm_290120)'):
	retval_0 = case.PatientModel.CreateRoi(Name=r"CBCT_SFOV", Color="255, 128, 255", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	retval_0.CreateCylinderGeometry(Radius=13.5, Axis={ 'x': 0, 'y': 0, 'z': 1 }, Length=27, Examination=examination, Center={ 'x': iso_x, 'y': iso_y, 'z': iso_z }, Representation="TriangleMesh", VoxelSize=None)

try:
	for points in case.PatientModel.PointsOfInterest:
		print(points.Name)
		if str(points.Name).lower() == 'couch':
			poi_name = points.Name
			couch_pos = structure_set.PoiGeometries[poi_name].Point
			print(points.Name)
	couch_x = couch_pos.x
	couch_y = couch_pos.y
	couch_z = couch_pos.z

	iso_height = couch_y - iso_y
	if setupcheck == 'HFS' or setupcheck == 'FFS':
		box_y = couch_y + 5
	else:
		box_y = couch_y - 5
		iso_height = iso_y - couch_y
	if iso_height >= 14:
		ctypes.windll.user32.MessageBoxW(0, "Isocentre is > 14cm above couch.",
										 "Error!", 1)
		sys.exit(1)
	print(str(iso_y) + ' ' + str(couch_y) + ' ' + str(iso_height))


except:
	ctypes.windll.user32.MessageBoxW(0, "SFOV created, but no couch POI found to remove couch or check distance.", "Error!", 1)
	sys.exit(1)

#create a box with x from ISO, z from ISO, y from couch. 27 sup inf left right, move 5 post and do 10cm ant post


with CompositeAction('Create Box ROI'):
	retval_0 = case.PatientModel.CreateRoi(Name=r"box_temp", Color="Blue", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	retval_0.CreateBoxGeometry(Size={ 'x': 27, 'y': 10, 'z': 27 }, Examination=examination, Center={ 'x': iso_x, 'y': box_y , 'z': iso_z },
							   Representation="TriangleMesh", VoxelSize=None)


with CompositeAction('ROI Algebra (CBCT_SFOV)'):
	case.PatientModel.RegionsOfInterest['CBCT_SFOV'].CreateAlgebraGeometry(Examination=examination, Algorithm="Auto",
																		   ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CBCT_SFOV"], 'MarginSettings':
																			   { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } },
																		   ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"box_temp"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } },
																		   ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
for structure in structure_set.RoiGeometries:
	if structure.OfRoi.Name == 'box_temp':
		structure.OfRoi.DeleteRoi()











