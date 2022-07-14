# Update derived geometires created with Pearl_ROI script on CT2 and then create 3 empty plans
# Pearl_ROI.py must have been run on CT1 first
# Jamil Lambert 02/11/2020

from connect import *

case = get_current("Case")
examination = get_current("Examination")
    
if ctypes.windll.user32.MessageBoxW(0, 'PEARL ROI script must have been run first on CT1 and then CT2 set as primary.\n\nScript may take a several minutes to create all ROIs.\n\nDo you wish to continue?', 'PEARL ROI update on CT2', 4) == 7:
    print('User cancelled script, nothing done')
    exit(1)

with CompositeAction('PEARL Script updating derived geometries'):    
    case.PatientModel.RegionsOfInterest['CTV_24.5Gy'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV_27.3Gy'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV_29.5Gy'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV_32.7Gy'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV_38.7Gy'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV_All+5mm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV_3_N_R-CTV2+1cm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV_29.5-CTV32.7+1cm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV1_P+3mm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV2+5mm-CTV1+5mm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV3+5mm-CTV1&2+5mm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV32.7-CTV38.7+5mm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['PTV24.5-CTV27.3+1cm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV_N_R+5mm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV_N_L+5mm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV2_P+3mm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV_N_Inf+5mm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV_N_L_Sup+5mm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV_N_R_Sup+5mm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV2+1cm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV27.3+3mm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['CTV_32.7+3mm'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['Glottis + Cricopharyngeus'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['PCM-PTV'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['Ring_27.3'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['Ring_32.7'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    case.PatientModel.RegionsOfInterest['Ring_PTV_all'].UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

with CompositeAction('PEARL Script creating empty plans'):
    retval_0 = case.AddNewPlan(PlanName=r"Phase1", PlannedBy=r"JL", Comment=r"", ExaminationName=r"CT 1", AllowDuplicateNames=False)
    retval_0.SetDefaultDoseGrid(VoxelSize={ 'x': 0.25, 'y': 0.25, 'z': 0.25 })
    retval_1 = retval_0.AddNewBeamSet(Name=r"Phase1", ExaminationName=r"CT 1", MachineName=r"iPOne004_B", Modality="Protons", TreatmentTechnique="ProtonPencilBeamScanning", PatientPosition="HeadFirstSupine", NumberOfFractions=15, CreateSetupBeams=False, UseLocalizationPointAsSetupIsocenter=False, Comment=r"", RbeModelReference=None, EnableDynamicTrackingForVero=False, NewDoseSpecificationPointNames=[], NewDoseSpecificationPoints=[], RespiratoryMotionCompensationTechnique="Disabled", RespiratorySignalSource="Disabled")
    retval_1.AddDosePrescriptionToRoi(RoiName=r"CTV1_P", DoseVolume=0, PrescriptionType="AverageDose", DoseValue=2730, RelativePrescriptionLevel=1, AutoScaleDose=False)

    retval_2 = case.AddNewPlan(PlanName=r"Phase2", PlannedBy=r"JL", Comment=r"", ExaminationName=r"CT 2", AllowDuplicateNames=False)
    retval_2.SetDefaultDoseGrid(VoxelSize={ 'x': 0.25, 'y': 0.25, 'z': 0.25 })
    retval_3 = retval_2.AddNewBeamSet(Name=r"Phase2", ExaminationName=r"CT 2", MachineName=r"iPOne004_B", Modality="Protons", TreatmentTechnique="ProtonPencilBeamScanning", PatientPosition="HeadFirstSupine", NumberOfFractions=18, CreateSetupBeams=False, UseLocalizationPointAsSetupIsocenter=False, Comment=r"", RbeModelReference=None, EnableDynamicTrackingForVero=False, NewDoseSpecificationPointNames=[], NewDoseSpecificationPoints=[], RespiratoryMotionCompensationTechnique="Disabled", RespiratorySignalSource="Disabled")
    retval_3.AddDosePrescriptionToRoi(RoiName=r"bCTV1_P", DoseVolume=0, PrescriptionType="AverageDose", DoseValue=3870, RelativePrescriptionLevel=1, AutoScaleDose=False)

    retval_4 = case.AddNewPlan(PlanName=r"Standard", PlannedBy=r"JL", Comment=r"", ExaminationName=r"CT 2", AllowDuplicateNames=False)
    retval_4.SetDefaultDoseGrid(VoxelSize={ 'x': 0.25, 'y': 0.25, 'z': 0.25 })
    retval_5 = retval_4.AddNewBeamSet(Name=r"Standard", ExaminationName=r"CT 2", MachineName=r"iPOne004_B", Modality="Protons", TreatmentTechnique="ProtonPencilBeamScanning", PatientPosition="HeadFirstSupine", NumberOfFractions=33, CreateSetupBeams=False, UseLocalizationPointAsSetupIsocenter=False, Comment=r"", RbeModelReference=None, EnableDynamicTrackingForVero=False, NewDoseSpecificationPointNames=[], NewDoseSpecificationPoints=[], RespiratoryMotionCompensationTechnique="Disabled", RespiratorySignalSource="Disabled")
    retval_5.AddDosePrescriptionToRoi(RoiName=r"CTV1_P", DoseVolume=0, PrescriptionType="AverageDose", DoseValue=6600, RelativePrescriptionLevel=1, AutoScaleDose=False)

