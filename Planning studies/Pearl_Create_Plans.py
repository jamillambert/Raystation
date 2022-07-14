# Creates 3 empty plans for the PEARL study, beam and objective templates for each plan can then be loaded manually
# Pearl_ROI.py must have been run on CT1 first, and Pearl_ROI_CT2_update.py on CT2
# Jamil Lambert 02/11/2020

from connect import *

case = get_current("Case")
patient_db = get_current("PatientDB")


plan1Name = 'Phase1'
prescription1ROI = 'CTV1_P'
prescription1Dose = 2730
prescription1Fx = 15

plan2Name = 'Phase2'
prescription2ROI = 'bCTV1_P'
prescription2Dose = 3870
prescription2Fx = 18

plan3Name = 'Standard'
prescription3ROI = 'CTV1_P'
prescription3Dose = 6600
prescription3Fx = 33

planMachine = 'iPOne004_B'
CT1name = 'CT 1'
CT2name = 'CT 2'
CT3name = 'CT 2'

# target1Name = 'CTV_All+5mm'  # Section does not yet function, isocentre can be set but the beam list template cannot be loaded
# target2Name = 'CTV_All+5mm'
# target3Name = 'CTV_All+5mm'
# template1Name = 'JL_Pearl_ph1'
# template2Name = 'JL_Pearl_ph2'
# template4Name = 'JL_Pearl'

# CT1IsoPos = beam_set.CreateDefaultIsocenterData(Position=case.PatientModel.StructureSets[CT1name] .RoiGeometries[target1Name].GetCenterOfRoi())
# CT2IsoPos = beam_set.CreateDefaultIsocenterData(Position=case.PatientModel.StructureSets[CT2name] .RoiGeometries[target2Name].GetCenterOfRoi())
# CT3IsoPos = beam_set.CreateDefaultIsocenterData(Position=case.PatientModel.StructureSets[CT3name] .RoiGeometries[target3Name].GetCenterOfRoi())

# beamListTemplate = patient_db.LoadTemplateBeamList(templateName = template1Name, lockMode = 'Read')  # Needs to be applied somehow like the objectives plan.PlanOptimizations[0].ApplyOptimizationTemplate(Template=template1Name)


#Create plan 1
plan1 = case.AddNewPlan(PlanName=plan1Name, PlannedBy=r"J", Comment=r"", ExaminationName=CT1name, AllowDuplicateNames=False)
plan1.SetDefaultDoseGrid(VoxelSize={ 'x': 0.25, 'y': 0.25, 'z': 0.25 })
plan1Beamset = plan1.AddNewBeamSet(Name=plan1Name, ExaminationName=CT1name, MachineName=planMachine, Modality="Protons", TreatmentTechnique="ProtonPencilBeamScanning", PatientPosition="HeadFirstSupine", NumberOfFractions=prescription1Fx, CreateSetupBeams=False, UseLocalizationPointAsSetupIsocenter=False, Comment=r"", RbeModelReference=None, EnableDynamicTrackingForVero=False, NewDoseSpecificationPointNames=[], NewDoseSpecificationPoints=[], RespiratoryMotionCompensationTechnique="Disabled", RespiratorySignalSource="Disabled")
plan1Beamset.AddDosePrescriptionToRoi(RoiName=prescription1ROI, DoseVolume=0, PrescriptionType="AverageDose", DoseValue=prescription1Dose, RelativePrescriptionLevel=1, AutoScaleDose=False)
plan1.PlanOptimizations[0].OptimizationParameters.Algorithm.MaxNumberOfIterations = 200
plan1.PlanOptimizations[0].OptimizationParameters.Algorithm.OptimalityTolerance = 1E-6
plan1.PlanOptimizations[0].OptimizationParameters.SaveRobustnessParameters(PositionUncertaintyAnterior=0.3, PositionUncertaintyPosterior=0.3, PositionUncertaintySuperior=0.3, PositionUncertaintyInferior=0.3, PositionUncertaintyLeft=0.3, PositionUncertaintyRight=0.3, DensityUncertainty=0.035, PositionUncertaintySetting="Universal", IndependentLeftRight=True, IndependentAnteriorPosterior=True, IndependentSuperiorInferior=True, ComputeExactScenarioDoses=False, NamesOfNonPlanningExaminations=[])


#Create plan 2
plan2 = case.AddNewPlan(PlanName=plan2Name, PlannedBy=r"", Comment=r"", ExaminationName=CT2name, AllowDuplicateNames=False)
plan2.SetDefaultDoseGrid(VoxelSize={ 'x': 0.25, 'y': 0.25, 'z': 0.25 })
plan2Beamset = plan2.AddNewBeamSet(Name=plan2Name, ExaminationName=CT2name, MachineName=planMachine, Modality="Protons", TreatmentTechnique="ProtonPencilBeamScanning", PatientPosition="HeadFirstSupine", NumberOfFractions=prescription2Fx, CreateSetupBeams=False, UseLocalizationPointAsSetupIsocenter=False, Comment=r"", RbeModelReference=None, EnableDynamicTrackingForVero=False, NewDoseSpecificationPointNames=[], NewDoseSpecificationPoints=[], RespiratoryMotionCompensationTechnique="Disabled", RespiratorySignalSource="Disabled")
plan2Beamset.AddDosePrescriptionToRoi(RoiName=prescription2ROI, DoseVolume=0, PrescriptionType="AverageDose", DoseValue=prescription2Dose, RelativePrescriptionLevel=1, AutoScaleDose=False)
plan2.PlanOptimizations[0].OptimizationParameters.Algorithm.MaxNumberOfIterations = 200
plan2.PlanOptimizations[0].OptimizationParameters.Algorithm.OptimalityTolerance = 1E-6
plan2.PlanOptimizations[0].OptimizationParameters.SaveRobustnessParameters(PositionUncertaintyAnterior=0.3, PositionUncertaintyPosterior=0.3, PositionUncertaintySuperior=0.3, PositionUncertaintyInferior=0.3, PositionUncertaintyLeft=0.3, PositionUncertaintyRight=0.3, DensityUncertainty=0.035, PositionUncertaintySetting="Universal", IndependentLeftRight=True, IndependentAnteriorPosterior=True, IndependentSuperiorInferior=True, ComputeExactScenarioDoses=False, NamesOfNonPlanningExaminations=[])

#Create plan 3
plan3 = case.AddNewPlan(PlanName=plan3Name, PlannedBy=r"", Comment=r"", ExaminationName=CT3name, AllowDuplicateNames=False)
plan3.SetDefaultDoseGrid(VoxelSize={ 'x': 0.25, 'y': 0.25, 'z': 0.25 })
plan3Beamset = plan3.AddNewBeamSet(Name=plan3Name, ExaminationName=CT3name, MachineName=planMachine, Modality="Protons", TreatmentTechnique="ProtonPencilBeamScanning", PatientPosition="HeadFirstSupine", NumberOfFractions=prescription3Fx, CreateSetupBeams=False, UseLocalizationPointAsSetupIsocenter=False, Comment=r"", RbeModelReference=None, EnableDynamicTrackingForVero=False, NewDoseSpecificationPointNames=[], NewDoseSpecificationPoints=[], RespiratoryMotionCompensationTechnique="Disabled", RespiratorySignalSource="Disabled")
plan3Beamset.AddDosePrescriptionToRoi(RoiName=prescription3ROI, DoseVolume=0, PrescriptionType="AverageDose", DoseValue=prescription3Dose, RelativePrescriptionLevel=1, AutoScaleDose=False)
plan3.PlanOptimizations[0].OptimizationParameters.Algorithm.MaxNumberOfIterations = 200
plan3.PlanOptimizations[0].OptimizationParameters.Algorithm.OptimalityTolerance = 1E-6
plan3.PlanOptimizations[0].OptimizationParameters.SaveRobustnessParameters(PositionUncertaintyAnterior=0.3, PositionUncertaintyPosterior=0.3, PositionUncertaintySuperior=0.3, PositionUncertaintyInferior=0.3, PositionUncertaintyLeft=0.3, PositionUncertaintyRight=0.3, DensityUncertainty=0.035, PositionUncertaintySetting="Universal", IndependentLeftRight=True, IndependentAnteriorPosterior=True, IndependentSuperiorInferior=True, ComputeExactScenarioDoses=False, NamesOfNonPlanningExaminations=[])
