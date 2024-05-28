# Script recorded 26 Nov 2020, 13:09:33

#   RayStation version: 9.0.0.113
#   Selected patient: ...

from connect import *

case = get_current("Case")
examination = get_current("Examination")


with CompositeAction('Create Cylinder ROI (P3_roi)'):

  retval_0 = case.PatientModel.CreateRoi(Name=r"R1_roi", Color="Blue", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)

  retval_0.CreateCylinderGeometry(Radius=0.145, Axis={ 'x': 0, 'y': 0, 'z': 1 }, Length=0.5, Examination=examination, Center={ 'x': 2.5, 'y': -10, 'z': -2.25 }, Representation="TriangleMesh", VoxelSize=None)

  retval_0 = case.PatientModel.CreateRoi(Name=r"R2_roi", Color="Blue", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)

  retval_0.CreateCylinderGeometry(Radius=0.145, Axis={ 'x': 0, 'y': 0, 'z': 1 }, Length=0.5, Examination=examination, Center={ 'x': -2.5, 'y': -10, 'z': 1.75 }, Representation="TriangleMesh", VoxelSize=None)

  retval_0 = case.PatientModel.CreateRoi(Name=r"R3_roi", Color="Blue", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)

  retval_0.CreateCylinderGeometry(Radius=0.145, Axis={ 'x': 0, 'y': 0, 'z': 1 }, Length=0.5, Examination=examination, Center={ 'x': 0, 'y': -10, 'z': 0 }, Representation="TriangleMesh", VoxelSize=None)

  retval_0 = case.PatientModel.CreateRoi(Name=r"P1_roi", Color="Blue", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)

  retval_0.CreateCylinderGeometry(Radius=0.145, Axis={ 'x': 0, 'y': 0, 'z': 1 }, Length=0.5, Examination=examination, Center={ 'x': 6, 'y': -10, 'z': 2.25 }, Representation="TriangleMesh", VoxelSize=None)

  retval_0 = case.PatientModel.CreateRoi(Name=r"P2_roi", Color="Blue", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)

  retval_0.CreateCylinderGeometry(Radius=0.145, Axis={ 'x': 0, 'y': 0, 'z': 1 }, Length=0.5, Examination=examination, Center={ 'x': 2, 'y': -10, 'z': 0.75 }, Representation="TriangleMesh", VoxelSize=None)

  retval_0 = case.PatientModel.CreateRoi(Name=r"P3_roi", Color="Blue", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)

  retval_0.CreateCylinderGeometry(Radius=0.145, Axis={ 'x': 0, 'y': 0, 'z': 1 }, Length=0.5, Examination=examination, Center={ 'x': -3, 'y': -10, 'z': 0 }, Representation="TriangleMesh", VoxelSize=None)

  retval_0 = case.PatientModel.CreateRoi(Name=r"P4_roi", Color="Pink", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)

  retval_0.CreateCylinderGeometry(Radius=0.145, Axis={ 'x': 0, 'y': 0, 'z': 1 }, Length=0.5, Examination=examination, Center={ 'x': 2.5, 'y': -10, 'z': 0 }, Representation="TriangleMesh", VoxelSize=None)

  retval_0 = case.PatientModel.CreateRoi(Name=r"P5_roi", Color="Black", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)

  retval_0.CreateCylinderGeometry(Radius=0.145, Axis={ 'x': 0, 'y': 0, 'z': 1 }, Length=0.5, Examination=examination, Center={ 'x': -8, 'y': -10, 'z': 0 }, Representation="TriangleMesh", VoxelSize=None)

# CompositeAction ends 




