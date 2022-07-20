from connect import *
import numpy as np
import pandas as pd
import string

try:
	patient = get_current('Patient')
	plan = get_current('Plan')
except:
	print('Could not load plan')
	exit()

structure_set = plan.GetStructureSet()
roi_names = [r.OfRoi.Name for r in structure_set.RoiGeometries if r.HasContours() == True]
plan_dose = plan.TreatmentCourse.TotalDose

data_dict ={}
r_v=np.linspace(1,0,101)

for roi_name in roi_names:
	data_rel_list = plan_dose.GetDoseAtRelativeVolumes(RoiName=roi_name, RelativeVolumes=r_v)
	data_dict[roi_name] = data_rel_list

df = pd.DataFrame(data_dict, index=r_v*100)

writer = pd.ExcelWriter('DVH_export.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')
df.to_excel(writer, sheet_name='Sheet1')

workbook = writer.book
worksheet = writer.sheets['Sheet1']
chart = workbook.add_chart({'type': 'scatter', 'subtype': 'straight'})
i=66
for roi_name in roi_names:
	rangeString = r'=Sheet1!$' + chr(i) + r'2:$' + chr(i) + r'102'
	chart.add_series({'name':roi_name, 'values':'=Sheet1!$A2:$A102', 'categories':rangeString})
	i=i+1
chart.set_x_axis({'name': 'Dose (cGy)'})
chart.set_y_axis({'name': 'Volume', 'major_gridlines': {'visible': False}})
chart.set_title({'name': 'DVH'})

worksheet.insert_chart('I2', chart)

writer.save()