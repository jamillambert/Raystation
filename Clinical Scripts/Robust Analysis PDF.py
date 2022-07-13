'''
Creates a pdf of the robust analysis for the current plan
prints out the worst case, second worst case and nominal 
values for all clinical goals with priority 1

Luke Murray 13/11/2020, modified Jamil Lambert 16/11/2020, modified JL 24/02/2021 to work with v10B
'''

from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak
from datetime import datetime

from connect import *
import ctypes, sys, textwrap

startTime = datetime.now()

print('Version 6.2:')

pdf_path = "//ppgbcipmsqdat01/MOSAIQ_DATA/DB/ESCAN/RaystationPrintouts"  #path where the generated pdf is saved

# getting all 'currents'
try:
    patient = get_current("Patient")
    plan = get_current("Plan")
    beam_set = get_current("BeamSet")
    case = get_current("Case")
    structure_set = plan.GetTotalDoseStructureSet()
except:
    ctypes.windll.user32.MessageBoxW(0, "Script failed, either no patient or no plan loaded.", "Error!", 1)
    sys.exit(1)

# setting variables used
cheight = 0.3 * inch
cwidth = 1.5 * inch
cell1 = 0.75 * cwidth
cell2 = 1.91666667 * cwidth
cell3 = 2.75 * cwidth
cell4 = 3.58333333333 * cwidth
fractions = beam_set.FractionationPattern.NumberOfFractions

# patient and plan information for each page initialisation
def page_setup():
    # creating header
    c.translate(inch, 11 * inch)
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica", 30)
    text_width = float(stringWidth("Robust Analysis", "Helvetica", 30))
    c.drawString((0 + (text_width / 2)), 0, "Robust Analysis")
    c.translate(0, -0.5 * inch)
    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(0.8671875, 0.69140625, 0.54296875, 0.75)
    c.rect(0, 0, 6 * inch, 0.3 * inch, fill=1)
    c.translate(0, 0.07 * inch)
    c.setFillColorRGB(0, 0, 0, 1)
    c.setFont("Helvetica", 12)
    now = datetime.now()
    dt_current = now.strftime("%d/%m/%Y, %H:%M:%S")
    header = 'Patient: ' + pname[1] + ' ' + pname[0] + ' | MRN:' + patient.PatientID + ' | ' + dt_current
    text_width = float(stringWidth(header, "Helvetica", 30))
    c.drawCentredString(3 * inch, 2, header)
    c.translate(0, -0.5 * inch)
    c.drawString(0, 0, "Plan Name: " + plan.Name)
    c.translate(0, -0.2 * inch)
    c.drawString(0, 0, "Beam Set: " + beam_set.DicomPlanLabel)
    c.translate(0, -0.2 * inch)
    try:
        c.drawString(0, 0, "Approval Status: " + plan.Review.ApprovalStatus)
        c.translate(0, -0.2 * inch)
        c.drawString(0, 0, "Approver: " + plan.Review.ReviewerName)
        c.translate(0, -0.2 * inch)
        c.drawString(0, 0, "Approval timestamp: " + str(plan.Review.ReviewTime))
    except:
        c.drawString(0, 0, 'Plan not approved!')
        c.translate(0, -0.2 * inch)
        c.drawString(0, 0, 'PDF for information only.')
    c.translate(0, -0.35 * inch)
    draw_topcell(robustname)
    draw_row()
    cell_titles()


# draws one off top cell for title
def draw_topcell(robustname):
    c.translate(0, -cheight)
    c.rect(0, 0, 6 * inch, cheight, fill=0)
    c.setFont("Helvetica", 12)
    temptext = 'Robust Analysis: ' + robustname
    c.drawCentredString((3 * inch), 2, temptext)


# draws table row
def draw_row():
    c.translate(0, -cheight)
    for i in range(0, 4):
        if i == 0:
            c.rect(0, 0, 1.5 * cwidth, cheight, 1, 0)
            c.translate(1.5 * cwidth, 0)
        else:
            c.rect(0, 0, (2.5 / 3) * cwidth, cheight, 1, 0)
            c.translate((2.5 / 3) * cwidth, 0)
    c.translate(-6 * inch, 0)


# inserting titles into first row
def cell_titles():
    draw_row()
    c.translate(0, cheight)
    c.setFont("Helvetica", 12)
    c.drawCentredString(cell1, 2, 'Clinical Goal')
    c.drawCentredString(cell2, 2, 'Worst Case')
    c.drawCentredString(cell3, 2, '2nd Worst Case')
    c.drawCentredString(cell4, 2, 'Nominal Value')

# setting colours based on tolerance
def colour_cell(x, tolerance):
    x = x - ((2.5 / 6)*cwidth)
    if tolerance == 0:
        c.setFillColorRGB(0.81640625, 0.2109375, 0.18359375, 0.75)
    else:
        c.setFillColorRGB(0.1796875, 0.375, 0.2890625, 0.75)
    c.rect(x, 0, (2.5 / 3) * cwidth, cheight, 1, fill=1)
    c.setFillColorRGB(0, 0, 0, 1)


# filling in clinical goal cell then calling for data to be filled in
def robustgoal(i, position):
    draw_row()
    criteria = ''
    tempstring = ''
    line = 15
    if i.PlanningGoal.GoalCriteria == 'AtMost':
        criteria = 'At most '
    else:
        criteria = 'At least '
    if i.PlanningGoal.Type == 'DoseAtVolume':
        tempstring = criteria + str(float("{:.2f}".format(
            i.PlanningGoal.AcceptanceLevel / 100))) + 'Gy to ' + str(
            float("{:.2f}".format(i.PlanningGoal.ParameterValue * 100))) + '% vol'
    if i.PlanningGoal.Type == 'DoseAtAbsoluteVolume':
        tempstring = criteria + str(float("{:.2f}".format(
            i.PlanningGoal.AcceptanceLevel / 100))) + 'Gy to ' + str(
            float("{:.2f}".format(i.PlanningGoal.ParameterValue))) + 'cc'
    if i.PlanningGoal.Type == 'VolumeAtDose':
        tempstring = criteria + str(float("{:.2f}".format(
            i.PlanningGoal.AcceptanceLevel * 100))) + '% vol at ' + str(
            float("{:.2f}".format(i.PlanningGoal.ParameterValue / 100))) + 'Gy'
    if i.PlanningGoal.Type == 'AbsoluteVolumeAtDose':
        tempstring = criteria + str(float("{:.2f}".format(
            i.PlanningGoal.AcceptanceLevel))) + 'cc at ' + str(
            float("{:.2f}".format(i.PlanningGoal.ParameterValue / 100))) + 'Gy'
    if i.PlanningGoal.Type == 'AverageDose':
        tempstring = criteria + str(float("{:.2f}".format(
            i.PlanningGoal.AcceptanceLevel / 100))) + 'Gy Average'
    c.setFont("Helvetica", 8)
    c.drawCentredString(cell1, 12, str(i.ForRegionOfInterest.Name) + ': ')
    c.drawCentredString(cell1, 4, tempstring)
    c.setFont("Helvetica", 12)
    worstsecondnominal(i, position)

    
# filling in data cells
def worstsecondnominal(i, doseScenarioList):
    templist = []
    worst = 0
    second = 0
    nominal = 0
    limit = 0    
    currentRoiName = i.ForRegionOfInterest.Name
    total_volume = doseScenarioList[0].GetDoseGridRoi(RoiName=currentRoiName).RoiVolumeDistribution.TotalVolume
    fxDiv100 = fractions / 100
    
    if i.PlanningGoal.Type == 'DoseAtVolume':
        relVol = i.PlanningGoal.ParameterValue
        for x in doseScenarioList:
            templist.append(x.GetDoseAtRelativeVolumes(RoiName=currentRoiName, RelativeVolumes=[relVol])[0] * fxDiv100)
        tempstring = 'Gy'
        limit = i.PlanningGoal.AcceptanceLevel / 100
        nominal = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=currentRoiName,RelativeVolumes=[relVol])[0] / 100

    if i.PlanningGoal.Type == 'DoseAtAbsoluteVolume':
        if i.PlanningGoal.ParameterValue / total_volume > 1:
            tempstring = 'NA'
            templist.append('')
            nominal = ''
        else:
            relVol = i.PlanningGoal.ParameterValue / total_volume
            for x in doseScenarioList:
                templist.append(x.GetDoseAtRelativeVolumes(RoiName=currentRoiName, RelativeVolumes=[relVol])[0] * fxDiv100)
            tempstring = 'Gy'
            nominal = plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName=currentRoiName, RelativeVolumes=[relVol])[0] / 100
        limit = i.PlanningGoal.AcceptanceLevel / 100

    if i.PlanningGoal.Type == 'VolumeAtDose':
        doseVal = i.PlanningGoal.ParameterValue
        fxDoseVal = doseVal / fractions
        for x in doseScenarioList:
            templist.append(x.GetRelativeVolumeAtDoseValues(RoiName=currentRoiName, DoseValues=[fxDoseVal])[0] * 100)
        tempstring = '%'
        nominal = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName=currentRoiName, DoseValues=[doseVal])[0] * 100
        limit = i.PlanningGoal.AcceptanceLevel * 100

    if i.PlanningGoal.Type == 'AbsoluteVolumeAtDose':
        doseVal = i.PlanningGoal.ParameterValue
        fxDoseVal = doseVal / fractions
        for x in doseScenarioList:
            z = templist.append(x.GetRelativeVolumeAtDoseValues(RoiName=currentRoiName, DoseValues=[fxDoseVal])[0] * total_volume)
        tempstring = 'cc'
        nominal = plan.TreatmentCourse.TotalDose.GetRelativeVolumeAtDoseValues(RoiName=currentRoiName, DoseValues=[doseVal])[0] * total_volume
        limit = i.PlanningGoal.AcceptanceLevel

    if i.PlanningGoal.Type == 'AverageDose':
        for x in doseScenarioList:
            templist.append(x.GetDoseStatistic(RoiName=currentRoiName, DoseType='Average') * fxDiv100)
        tempstring = 'Gy'
        nominal = plan.TreatmentCourse.TotalDose.GetDoseStatistic(RoiName=currentRoiName, DoseType='Average') / 100
        limit = i.PlanningGoal.AcceptanceLevel / 100

    if tempstring == 'NA':
        c.drawCentredString(cell2, 7, tempstring)
        c.drawCentredString(cell3, 7, tempstring)
        c.drawCentredString(cell4, 7, tempstring)
    else:
        if i.PlanningGoal.GoalCriteria == 'AtMost':
            x1 = 0
            x2 = 0
            for i in templist:
                if i > x1:
                    x2 = x1
                    x1 = i
                elif i > x2:
                    x2 = i
            if x1 > limit:
                colour_cell(cell2, 0)
            else:
                colour_cell(cell2, 1)
            if x2 > limit:
                colour_cell(cell3, 0)
            else:
                colour_cell(cell3, 1)
            if nominal > limit:
                colour_cell(cell4, 0)
            else:
                colour_cell(cell4, 1)

            c.drawCentredString(cell2, 7, str(float("{:.2f}".format(x1))) + tempstring)
            c.drawCentredString(cell3, 7, str(float("{:.2f}".format(x2))) + tempstring)
            c.drawCentredString(cell4, 7, str(float("{:.2f}".format(nominal))) + tempstring)
            return 1
        else:
            x1 = float('inf')
            x2 = float('inf')
            for i in templist:
                if i < x1:
                    x2 = x1
                    x1 = i

                elif i < x2:
                    x2 = i
            if x1 <= limit:
                colour_cell(cell2, 0)
            else:
                colour_cell(cell2, 1)
            if x2 <= limit:
                colour_cell(cell3, 0)
            else:
                colour_cell(cell3, 1)
            if nominal <= limit:
                colour_cell(cell4, 0)
            else:
                colour_cell(cell4, 1)
            c.drawCentredString(cell2, 7, str(float("{:.2f}".format(x1))) + tempstring)
            c.drawCentredString(cell3, 7, str(float("{:.2f}".format(x2))) + tempstring)
            c.drawCentredString(cell4, 7, str(float("{:.2f}".format(nominal))) + tempstring)
#end worstsecondnominal()    
    
# running program and gathering all clinical goals with priority 1

for x in case.TreatmentDelivery.RadiationSetScenarioGroups:
    num_beams = 0
    pass_beams = 0
    page_goals = 0
    if x.ReferencedRadiationSet.DicomPlanLabel == beam_set.DicomPlanLabel:
        if  x.ReferencedRadiationSet.UniqueId == beam_set.UniqueId:
            for beam in x.ReferencedRadiationSet.Beams:
                num_beams +=1
                if beam.BeamMU == beam_set.Beams[num_beams-1].BeamMU:
                    pass_beams+=1

            if num_beams == pass_beams:
                robustname = str(x.Name)
                pname = patient.Name.split("^")
                # creating document
                cm = 2.54
                pdf_name = (pname[0].upper() + '_' + pname[1].capitalize() + '_' + patient.PatientID + '_' + plan.Name + '_' + robustname + ".pdf")
                save_name = os.path.join(os.path.expanduser("~"), pdf_path, pdf_name)
                c = canvas.Canvas(save_name)
                page_setup()
                doseScenarioList = x.DiscreteFractionDoseScenarios
                for i in plan.TreatmentCourse.EvaluationSetup.EvaluationFunctions:
                    if i.PlanningGoal.Priority == 1:
                        page_goals = page_goals + 1
                        if page_goals > 25:
                            c.showPage()
                            page_setup()
                            page_goals = 1
                            robustgoal(i, doseScenarioList)
                        else:
                            robustgoal(i, doseScenarioList)

                c.translate(0, -0.25 * inch)
                c.drawString(0, 0, "Comment:")
                c.showPage()
                c.save()

endTime = datetime.now()
print('\n\nRuntime 1: ')
print(endTime-startTime)
