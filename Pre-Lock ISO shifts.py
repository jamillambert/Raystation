#this script adds the correct shifts and ISO DICOM position to the current plan comment.
from connect import *
import ctypes
import sys

#establishing variables
examination = get_current("Examination")
setupcheck = examination.PatientPosition
case = get_current("Case")
beam_set = get_current("BeamSet")
plan = get_current('Plan')
structure_set = case.PatientModel.StructureSets[examination.Name]
comment = plan.Comments
new_line = ""
poi_name = ""
iso_position = beam_set.Beams[0].Isocenter.Position
beam_name = beam_set.Beams[0].Name
beam_name_new = ""
x_dir = "Right"
y_dir = "Ant"
Z_dir = "Sup"
laser_loc = ""
laser_x = 999
laser_y = 999
laser_z = 999

# Check if the plan is approved and exit if it is
if plan.QueryBeamSetInfo(Filter = {'ApprovalStatus':'Approved'}):
    ctypes.windll.user32.MessageBoxW(0, "Plan locked, unable to update plan comment.", "Error!", 1)
    sys.exit(1)

# Checking whether line break is needed
if comment == "":
    new_line = ""
else:
    new_line = "\n"
# Finding POI with LocalizationPoint Type
try:
    i = 0
    for points in case.PatientModel.PointsOfInterest:
        if case.PatientModel.PointsOfInterest[i].Type == 'LocalizationPoint':
            poi_name = case.PatientModel.PointsOfInterest[i].Name
            laser_loc = structure_set.PoiGeometries[poi_name].Point
            # Get POI coordinates
        i+=1
    laser_x = laser_loc['x']
    laser_y = laser_loc['y']
    laser_z = laser_loc['z']
except:
    ctypes.windll.user32.MessageBoxW(0, "Script failed, Laser Loc doesn't exist or set to wrong type.", "Error!", 1)
    sys.exit(1)

# Conditional Moves
x_pos = (round((iso_position['x'] - laser_x)*100))/100
y_pos = (round((iso_position['y'] - laser_y)*100))/100
z_pos = (round((iso_position['z'] - laser_z)*100))/100
if x_pos < 0:
    x_dir = "cm Right"
elif x_pos == 0:
    x_dir = "cm Right / Left"
else:
    x_dir = "cm Left"

if y_pos < 0:
    y_dir = "cm Ant"
elif y_pos == 0:
    y_dir = "cm Ant / Post"
else:
    y_dir = "cm Post"

if z_pos > 0:
    z_dir = "cm Sup"
elif z_pos == 0:
    z_dir = "cm Sup / Inf"
else:
    z_dir = "cm Inf"
x_pos = abs(x_pos)
y_pos = abs(y_pos)
z_pos = abs(z_pos)
plan.Comments = (comment + new_line + setupcheck + "\nMoves from Laser Loc to " + beam_name + " isocentre:\n" + str(z_pos) + z_dir + "\n" + str(x_pos) + x_dir + "\n" + str(y_pos) + y_dir)
comment = plan.Comments

# cycling through all beams to see if there are multiple isocentres and providing sequential moves for them
for beam in beam_set.Beams:
    if beam.Isocenter.Position != iso_position:
        beam_name_new = beam.Name
        iso_position_new = beam.Isocenter.Position
        x_pos = (round((iso_position_new['x'] - iso_position['x']) * 100)) / 100
        y_pos = (round((iso_position_new['y'] - iso_position['y']) * 100)) / 100
        z_pos = (round((iso_position_new['z'] - iso_position['z']) * 100)) / 100
        if x_pos < 0:
            x_dir = "cm Right"
        elif x_pos == 0:
            x_dir = "cm Right / Left"
        else:
            x_dir = "cm Left"

        if y_pos < 0:
            y_dir = "cm Ant"
        elif y_pos == 0:
            y_dir = "cm Ant / Post"
        else:
            y_dir = "cm Post"

        if z_pos > 0:
            z_dir = "cm Sup"
        elif z_pos == 0:
            z_dir = "cm Sup / Inf"
        else:
            z_dir = "cm Inf"
        x_pos = abs(x_pos)
        y_pos = abs(y_pos)
        z_pos = abs(z_pos)
        plan.Comments = (comment + "\n\nMoves from " + beam_name +" isocentre to " + beam_name_new + " isocentre:\n" + str(z_pos) + z_dir + "\n" + str(x_pos) + x_dir + "\n" + str(y_pos) + y_dir)
        comment = plan.Comments
        print(setupcheck)
