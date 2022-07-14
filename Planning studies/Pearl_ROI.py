#   Creates all of the derived CTV and PTV volumes, combined OARs and Rings for the objective function in the PEARL study
# "Inf_Box" ROI needs to be created to contain the inferior section of the nodes
# "Sup_Box" ROI needs to be created to contain the superior section of the nodes
# The two above boxes should overlap by at least 4cm to give space for a gradient junction
#   Jamil Lambert 02/11/2020

from connect import *

case = get_current("Case")
examination = get_current("Examination")

#Check that all the required ROIs exist
required_ROIs = ['Inf_Box', 'Sup_Box', 'CTV1_N', 'CTV1_P', 'CTV2_N', 'CTV2_P', 'CTV3_N_L', 'CTV3_N_R', 'GTV_N', 'GTV_P', 'BrainStem', 'Cricopharyngeus', 'GLOTTIS', 'IPCM', 'L PAROTID', 'L SMG', 'MPCM', 'ORAL CAVITY', 'R PAROTID', 'R SMG', 'SPCM', 'SUPRAGLOTTIS']

existing_ROIs = [s.OfRoi.Name for s in case.PatientModel.StructureSets[examination.Name].RoiGeometries if s.PrimaryShape is not None]
missing_ROIs = [x for x in required_ROIs if x not in existing_ROIs]

if len(missing_ROIs) > 0:
    missing_ROI_Text = ", ".join(missing_ROIs)
    errorMessage = 'ROI Dependency failed no ROIs will be created. The following ROIs are missing:\n\n' + missing_ROI_Text
    ctypes.windll.user32.MessageBoxW(0, errorMessage, 'ROI Dependency Failed', 0)
    exit(1)
    
if ctypes.windll.user32.MessageBoxW(0, 'All required ROIs found.  Script may take several minutes to create all new ROIs\n\nDo you wish to continue?', 'ROI Dependency Passed', 4) == 7:
    print(' \n\nUser cancelled script, nothing done')
    exit(1)

with CompositeAction('PEARL Script Target ROI creation'):
    newROI_0 = case.PatientModel.CreateRoi(Name=r"CTV_24.5Gy", Color="Aqua", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_0.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV3_N_R", r"CTV3_N_L"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.2, 'Inferior': 0.2, 'Anterior': 0.2, 'Posterior': 0.2, 'Right': 0.2, 'Left': 0.2 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV2_P"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Union", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_0.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_1 = case.PatientModel.CreateRoi(Name=r"CTV_27.3Gy", Color="Cyan", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_1.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV2_N", r"CTV1_N"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.2, 'Inferior': 0.2, 'Anterior': 0.2, 'Posterior': 0.2, 'Right': 0.2, 'Left': 0.2 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV1_P"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Union", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_1.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_2 = case.PatientModel.CreateRoi(Name=r"CTV_29.5Gy", Color="Cyan", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_2.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV3_N_R", r"CTV3_N_L"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.2, 'Inferior': 0.2, 'Anterior': 0.2, 'Posterior': 0.2, 'Right': 0.2, 'Left': 0.2 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV2_P"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Union", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_2.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_3 = case.PatientModel.CreateRoi(Name=r"CTV_32.7Gy", Color="Cyan", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_3.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV1_P", r"CTV2_N"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_3.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_4 = case.PatientModel.CreateRoi(Name=r"CTV_38.7Gy", Color="Cyan", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_4.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV1_N", r"bCTV1_P"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_4.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_5 = case.PatientModel.CreateRoi(Name=r"CTV_All+5mm", Color="Red", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_5.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"GTV_P", r"CTV2_P", r"CTV1_P", r"GTV_N", r"CTV2_N", r"CTV1_N", r"CTV3_N_R", r"CTV3_N_L"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_5.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_6 = case.PatientModel.CreateRoi(Name=r"CTV_3_N_R-CTV2+1cm", Color="Aqua", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_6.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV3_N_R"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV2_P", r"CTV2_N"], 'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 'Anterior': 1, 'Posterior': 1, 'Right': 1, 'Left': 1 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_6.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
    
    newROI_6a = case.PatientModel.CreateRoi(Name=r"CTV_3_N_L-CTV2+1cm", Color="Aqua", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_6a.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV3_N_L"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV2_P", r"CTV2_N"], 'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 'Anterior': 1, 'Posterior': 1, 'Right': 1, 'Left': 1 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_6a.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_7 = case.PatientModel.CreateRoi(Name=r"CTV_29.5-CTV32.7+1cm", Color="Aqua", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_7.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_29.5Gy"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_32.7Gy", r"CTV_38.7Gy"], 'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 'Anterior': 1, 'Posterior': 1, 'Right': 1, 'Left': 1 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_7.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_8 = case.PatientModel.CreateRoi(Name=r"CTV1_P+3mm", Color="Green", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_8.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV1_P"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.3, 'Inferior': 0.3, 'Anterior': 0.3, 'Posterior': 0.3, 'Right': 0.3, 'Left': 0.3 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_8.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_9 = case.PatientModel.CreateRoi(Name=r"CTV2+5mm-CTV1+5mm", Color="64, 0, 0", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_9.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV2_P", r"CTV2_N"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV1_P", r"CTV1_N"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_9.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_10 = case.PatientModel.CreateRoi(Name=r"CTV3+5mm-CTV1&2+5mm", Color="64, 0, 128", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_10.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV3_N_R", r"CTV3_N_L"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV2_P", r"CTV1_P", r"CTV2_N", r"CTV1_N"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_10.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_11 = case.PatientModel.CreateRoi(Name=r"CTV32.7-CTV38.7+5mm", Color="Yellow", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_11.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_32.7Gy"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_38.7Gy"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_11.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_12 = case.PatientModel.CreateRoi(Name=r"PTV24.5-CTV27.3+1cm", Color="128, 64, 0", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_12.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_24.5Gy"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.3, 'Inferior': 0.3, 'Anterior': 0.3, 'Posterior': 0.3, 'Right': 0.3, 'Left': 0.3 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_27.3Gy"], 'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 'Anterior': 1, 'Posterior': 1, 'Right': 1, 'Left': 1 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_12.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_13 = case.PatientModel.CreateRoi(Name=r"CTV_N_R+5mm", Color="128, 64, 0", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_13.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV3_N_R"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_13.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_14 = case.PatientModel.CreateRoi(Name=r"CTV_N_L+5mm", Color="Maroon", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_14.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV3_N_L"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_14.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_15 = case.PatientModel.CreateRoi(Name=r"CTV2_P+3mm", Color="255, 128, 128", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_15.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV2_P"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.3, 'Inferior': 0.3, 'Anterior': 0.3, 'Posterior': 0.3, 'Right': 0.3, 'Left': 0.3 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_15.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

with CompositeAction('PEARL Script splitting of nodes sup and inf)'):
    newROI_16 = case.PatientModel.CreateRoi(Name=r"CTV_N_Inf+5mm", Color="Purple", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_16.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV3_N_R", r"CTV3_N_L"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"Inf_Box"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Intersection", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_16.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_17 = case.PatientModel.CreateRoi(Name=r"CTV_N_L_Sup+5mm", Color="Navy", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_17.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV3_N_L"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"Sup_Box"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Intersection", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_17.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_18 = case.PatientModel.CreateRoi(Name=r"CTV_N_R_Sup+5mm", Color="Navy", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_18.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV3_N_R"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"Sup_Box"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Intersection", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_18.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

with CompositeAction('PEARL Script composite OAR creation'):
    newROI_19 = case.PatientModel.CreateRoi(Name=r"Glottis + Cricopharyngeus", Color="128, 64, 0", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_19.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"SUPRAGLOTTIS", r"GLOTTIS", r"Cricopharyngeus"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_19.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_20 = case.PatientModel.CreateRoi(Name=r"PCM-PTV", Color="Red", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_20.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"SPCM", r"MPCM", r"IPCM"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_24.5Gy", r"CTV_27.3Gy", r"CTV_29.5Gy", r"CTV_32.7Gy", r"CTV_38.7Gy"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0.5, 'Inferior': 0.5, 'Anterior': 0.5, 'Posterior': 0.5, 'Right': 0.5, 'Left': 0.5 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_20.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

with CompositeAction('PEARL Script Ring creation'):
    newROI_21 = case.PatientModel.CreateRoi(Name=r"CTV2+1cm", Color="Cyan", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_21.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV2_P", r"CTV2_N"], 'MarginSettings': { 'Type': "Expand", 'Superior': 1, 'Inferior': 1, 'Anterior': 1, 'Posterior': 1, 'Right': 1, 'Left': 1 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_21.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_22 = case.PatientModel.CreateRoi(Name=r"CTV27.3+3mm", Color="Red", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_22.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_27.3Gy"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_22.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_23 = case.PatientModel.CreateRoi(Name=r"CTV_32.7+3mm", Color="Red", Type="Ptv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_23.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_32.7Gy"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_23.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_24 = case.PatientModel.CreateRoi(Name=r"Ring_27.3", Color="Red", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_24.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_27.3Gy"], 'MarginSettings': { 'Type': "Expand", 'Superior': 3, 'Inferior': 3, 'Anterior': 3, 'Posterior': 3, 'Right': 3, 'Left': 3 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV27.3+3mm"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_24.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_25 = case.PatientModel.CreateRoi(Name=r"Ring_32.7", Color="Red", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_25.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_32.7Gy"], 'MarginSettings': { 'Type': "Expand", 'Superior': 3, 'Inferior': 3, 'Anterior': 3, 'Posterior': 3, 'Right': 3, 'Left': 3 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_32.7+3mm"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_25.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_26 = case.PatientModel.CreateRoi(Name=r"Ring_PTV_all", Color="Red", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_26.SetAlgebraExpression(ExpressionA={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_All+5mm"], 'MarginSettings': { 'Type': "Expand", 'Superior': 3, 'Inferior': 3, 'Anterior': 3, 'Posterior': 3, 'Right': 3, 'Left': 3 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV_All+5mm", r"CTV2+1cm"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_26.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")

    newROI_27 = case.PatientModel.CreateRoi(Name=r"Ring_Nodes", Color="Green", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
    newROI_27.SetAlgebraExpression(ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': [r"External", r"Ring_PTV_all"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [r"CTV2+1cm"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
    newROI_27.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
