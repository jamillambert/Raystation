# Script compares the commissioning time stamps of the three proton beam models and
# three CT to density curves to the reference values entered below
# Displays a message stating if it passes or what changes were found
#
# original by Luke Murray 23/09/2020
# edit by Jamil Lambert 23/09/2020
# Updated time stamps after 10B upgrade

from connect import *
import ctypes
machine_db = get_current("MachineDB")
ct_1 = '13/11/2019 10:16:56'
ct_2 = '13/11/2019 10:17:03'
ct_3 = '13/11/2019 10:17:11'
ct_4 = '26/02/2021 17:08:25'

np_pname = 'iPOne004_B'
ne_pname = 'iPOne006_B'
rg_pname = 'iPOne013_B'
np_ptime = '23/02/2021 15:22:10'
ne_ptime = '23/02/2021 15:54:52'
rg_ptime = '23/02/2021 16:38:46'

machine1 = machine_db.GetTreatmentMachine(machineName=np_pname, lockMode=None)
machine2 = machine_db.GetTreatmentMachine(machineName=ne_pname, lockMode=None)
machine3 = machine_db.GetTreatmentMachine(machineName=rg_pname, lockMode=None)
ct_machines =  machine_db.GetCtImagingSystemsNameAndCommissionTime()

changes = 0
errorMessage = 'QA Failed, the following changes were found:\n\n'

if str(ct_machines['HOST-760005']) != ct_1:
    errorMessage = errorMessage + 'HOST-760005 commission time does not match.\nOriginal: ' + str(ct_1) + ' found: ' + str(ct_machines['HOST-760005']) + '\n\n'
    changes = changes + 1
 
if str(ct_machines['HOST-760033']) != ct_2:
    errorMessage = errorMessage + 'HOST-760033 commission time does not match.\nOriginal: ' + str(ct_2) + ' found: ' + str(ct_machines['HOST-760033']) + '\n\n'
    changes = changes + 1
 
if str(ct_machines['HOST-760037']) != ct_3:
    errorMessage = errorMessage + 'HOST-760037 commission time does not match.\nOriginal: ' + str(ct_3) + ' found: ' + str(ct_machines['HOST-760037']) + '\n\n'
    changes = changes + 1 
    
if str(ct_machines['HOST-760080']) != ct_4:
    errorMessage = errorMessage + 'HOST-760080 commission time does not match.\nOriginal: ' + str(ct_3) + ' found: ' + str(ct_machines['HOST-760080']) + '\n\n'
    changes = changes + 1

if str(machine1.CommissionTime) != np_ptime:
    errorMessage = errorMessage + 'Newport\'s Proton machine commission time does not match.\nOriginal: ' + str(np_ptime) + ' found: ' + str(machine1.CommissionTime) + '\n\n'
    changes = changes + 1

if str(machine2.CommissionTime) != ne_ptime:
    errorMessage = errorMessage + 'Northumberland\'s Proton machine commission time does not match.\nOriginal: ' + str(ne_ptime) + ' found: ' + str(machine2.CommissionTime) + '\n\n'
    changes = changes + 1
 
if str(machine3.CommissionTime) != rg_ptime:
    errorMessage = errorMessage + 'Reading\'s Proton machine commission time does not match.\nOriginal: ' + str(rg_ptime) + ' found: ' + str(machine3.CommissionTime) + '\n'
    changes = changes + 1

if changes == 0:
    ctypes.windll.user32.MessageBoxW(0, 'QA Passed, no changes found', 'QA Passed', 0)
else:
    ctypes.windll.user32.MessageBoxW(0, errorMessage, 'QA Failed', 0)
