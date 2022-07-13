# Creates a temporary plan with dose to allow a plan report to be generated
# Report views are created for every CT slice in the External ROI
# A plan report using the template "ROI printout report" is then created and
# saved in the path specified
#
# Amended by LM to include temp structure creation and update dose stats error catch
#
# 19.01.2021 Luke Murray
# 02.02.2021 Jamil Lambert - Added an option for pdf file compression using ghostscript

from connect import *
import ctypes
import System.Drawing
import sys, os, subprocess, time

try:
    case = get_current("Case")
    examination = get_current("Examination")
    patient = get_current("Patient")
    ui = get_current("ui")
    structure_set = case.PatientModel.StructureSets[examination.Name]
except:
    ctypes.windll.user32.MessageBoxW(0, "Script failed, either no patient or no exam loaded.", "Error!", 0x00010030)
    sys.exit(1)

# Save variables
planName = 'tempROIprintout'
pdf_path = "\\\ppgbcipmsqdat01\MOSAIQ_DATA\DB\ESCAN\RaystationPrintouts"
pname = patient.Name.split("^")
pdf_name = (pname[0].upper() + '_' + pname[1].capitalize() + '_' + patient.PatientID + "_ROI_Printout.pdf")
compressed_pdf_name = (pname[0].upper() + '_' + pname[1].capitalize() + '_' + patient.PatientID + "_ROI_Printout_compressed.pdf")
save_name = os.path.join(os.path.expanduser("~"), pdf_path, pdf_name)
save_name_compressed = os.path.join(os.path.expanduser("~"), pdf_path, compressed_pdf_name)

existing_ROIs = [s.OfRoi.Name for s in structure_set.RoiGeometries if s.PrimaryShape is not None]
if "External" not in existing_ROIs:
    errorMessage = 'External ROI is missing on Examination ' + examination.Name + '\nCreate an External ROI and then rerun the script'
    ctypes.windll.user32.MessageBoxW(0, errorMessage, 'ROI Dependency Failed', 0x00010030)
    exit(1)
    
rois_on = [x for x in existing_ROIs if patient.GetRoiVisibility(RoiName = x)]

# Create temp structure of all switched on ROIs to cover with views for report
with CompositeAction('ROI Algebra'):
    roiName = "_tempROI"
    temp_structure = case.PatientModel.CreateRoi(Name=roiName, Color="Yellow", Type="Organ", TissueName=None,
                                                 RbeCellTypeName=None, RoiMaterial=None)

    temp_structure.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={'Operation': "Union",
                                                                                          'SourceRoiNames': rois_on,
                                                                                          'MarginSettings': {
                                                                                              'Type': "Expand",
                                                                                              'Superior': 0, 'Inferior': 0,
                                                                                              'Anterior': 0,
                                                                                              'Posterior': 0, 'Right': 0,
                                                                                              'Left': 0}},
                                         ExpressionB={'Operation': "Union", 'SourceRoiNames': [],
                                                      'MarginSettings': {'Type': "Expand", 'Superior': 0, 'Inferior': 0,
                                                                         'Anterior': 0, 'Posterior': 0, 'Right': 0,
                                                                         'Left': 0}},
                                         ResultOperation="None",
                                         ResultMarginSettings={'Type': "Expand", 'Superior': 0.2, 'Inferior': 0.2,
                                                               'Anterior': 0,
                                                               'Posterior': 0, 'Right': 0, 'Left': 0})

    patient.SetRoiVisibility(RoiName=roiName, IsVisible=False)
    box = structure_set.RoiGeometries[roiName].GetBoundingBox()
    low_z = box[0].z
    high_z = box[1].z
    low_y = box[0].y
    high_y = box[1].y
    low_x = box[0].x
    high_x = box[1].x

# Create a temporary plan to anable a report to be generated
with CompositeAction('Create temporary plan for ROI report'):
    planNameList = [p.Name for p in case.TreatmentPlans]
    if planName in planNameList: # If the plan already exists clear existing views for report
        plan = case.TreatmentPlans[planName]
        beam_set = plan.BeamSets[planName]
        plan.SetReportViewPositions(Coordinates=[])
    else: # if the plan does not exist then create it
        plan = case.AddNewPlan(PlanName=planName, PlannedBy=r"", Comment=r"Temporary plan for ROI printout", ExaminationName=examination.Name, AllowDuplicateNames=False)
        plan.SetDefaultDoseGrid(VoxelSize={ 'x': 0.5, 'y': 0.5, 'z': 0.5 })
        beam_set = plan.AddNewBeamSet(Name=planName, ExaminationName=examination.Name, MachineName=r"EVER-RS-01", Modality="Photons", TreatmentTechnique="Conformal", PatientPosition="HeadFirstSupine", NumberOfFractions=1, CreateSetupBeams=True, UseLocalizationPointAsSetupIsocenter=False, Comment=r"", RbeModelReference=None, EnableDynamicTrackingForVero=False, NewDoseSpecificationPointNames=[], NewDoseSpecificationPoints=[], RespiratoryMotionCompensationTechnique="Disabled", RespiratorySignalSource="Disabled")
    isocentrePos = beam_set.CreateDefaultIsocenterData(Position=structure_set.RoiGeometries[roiName].GetCenterOfRoi())
    beam_1 = beam_set.CreatePhotonBeam(BeamQualityId=r"6", IsocenterData=isocentrePos, Name=r"beamName", Description=r"", GantryAngle=0, CouchAngle=0, CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=0)
    beam_1.CreateRectangularField(Width=10, Height=10, CenterCoordinate={ 'x': 0, 'y': 0 }, MoveMLC=True, MoveAllMLCLeaves=False, MoveJaw=True, JawMargins={ 'x': 0, 'y': 0 }, DeleteWedge=False, PreventExtraLeafPairFromOpening=False)
    beam_1.BeamMU = 0.01
    beam_set.ComputeDose(ComputeBeamDoses=True, DoseAlgorithm="CCDose", ForceRecompute=False)

# Add views for the report covering the selected ROIs
with CompositeAction('Add views for report'):
    box = structure_set.RoiGeometries[roiName].GetBoundingBox()
    sliceThickness = examination.Series[0].ImageStack.SlicePositions[1]
    z_top = box[1].z - 0.5 * sliceThickness
    z_bottom = box[0].z - 0.5 * sliceThickness
    coordinate_list = []
    z = z_bottom
    y = low_y
    x = low_x
    while z < z_top:
        coordinate_list.append({'x': round(x,2), 'y': round(y,2), 'z': round(z,2)})
        z += sliceThickness
        if y < (high_y + 0.2):
            y += 0.2
        if x < (high_x + 0.2):
            x += 0.2
    plan.SetReportViewPositions(Coordinates=coordinate_list)

# Set the dose colour table to not show any dose
case.CaseSettings.DoseColorMap.ColorMapReferenceType = 'ReferenceValue'
case.CaseSettings.DoseColorMap.PresentationType = 'Absolute'
case.CaseSettings.DoseColorMap.ReferenceValue = 0.4
dose_colour_table = ({100: System.Drawing.Color.FromArgb(0,0,0,0)}) # create a new colour table with only one value at 100% with the colour black
case.CaseSettings.DoseColorMap.ColorTable = dose_colour_table

# Update dose statistics
plan.BeamSets['tempROIprintout'].FractionDose.UpdateDoseGridStructures()

# Delete temp structure
temp_structure.DeleteRoi()

# Create the report and compress if requested
if ctypes.windll.user32.MessageBoxW(0, 'Dummy plan \"' + planName + '\" created.\n\nDo you want to save and create a report in ESCAN? (this will take a few minutes)', 'Save and create report?', 0x00010034) == 6:
    patient.Save()
    beam_set.CreateReport(templateName='ROI printout report', filename=save_name, ignoreWarnings=True)
    # Compress the pdf using ghostscript, stored on s drive
    if ctypes.windll.user32.MessageBoxW(0, 'Do you wish to compress the pdf file? (this will take a few minutes)\n\nYou can delete the plan \"' + planName + '\" when the pdf has been created.', 'Compress pdf report?', 0x00010034) == 6:
        if not os.path.isfile(save_name):
            ctypes.windll.user32.MessageBoxW(0, 'Invalid pdf file, nothing done', 'Error', 0x00010030)
            sys.exit(1)
        try:
            subprocess.call(['S:\\Clinical\\Radiotherapy\\Physics\\Software\\Ghostscript\\bin\\gswin64c.exe', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4', '-dPDFSETTINGS={}'.format('/printer'), '-dNOPAUSE', '-dQUIET', '-dBATCH', '-sOutputFile={}'.format(save_name_compressed), save_name])
            os.remove(save_name)
            time.sleep(2)
            os.startfile(save_name_compressed)
        except:
            ctypes.windll.user32.MessageBoxW(0, 'Ghostscript not found in S:\\Clinical\\Radiotherapy\\Physics\\Software\\Ghostscript\\ \n\nPdf not compressed', 'Error', 0x00010030)
            os.startfile(save_name)
    else:
        os.startfile(save_name)

# Set the colour table back to the default settings
case.CaseSettings.DoseColorMap.ColorMapReferenceType = 'RelativePrescription'
dose_colour_table[107] = System.Drawing.Color.FromArgb(255,255,0,0)
dose_colour_table[105] = System.Drawing.Color.FromArgb(255,255,83,76)
dose_colour_table[103] = System.Drawing.Color.FromArgb(255,255,150,0)
dose_colour_table[100] = System.Drawing.Color.FromArgb(255,255,255,0)
dose_colour_table[95] = System.Drawing.Color.FromArgb(255,0,255,0)
dose_colour_table[90] = System.Drawing.Color.FromArgb(255,0,255,255)
dose_colour_table[80] = System.Drawing.Color.FromArgb(255,0,0,255)
dose_colour_table[50] = System.Drawing.Color.FromArgb(255,255,0,255)
dose_colour_table[30] = System.Drawing.Color.FromArgb(255,200,180,255)
dose_colour_table[0] = System.Drawing.Color.FromArgb(255,0,0,0)
case.CaseSettings.DoseColorMap.ColorTable = dose_colour_table
beam_set.ClearBeams()

