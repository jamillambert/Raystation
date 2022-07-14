Procedure
Scripting:
	1. Before running the scripts
		a. Check ROI names match screenshot
		b. Check CTs are named "CT 1" and "CT 2"
		c. Register the two CTs
		d. Create two Boxs named "Inf_Box" and "Sup_Box" on CT 1 that contain the regions to be used for the superior section and inferior sections of the targets, the two should overlap by at least 4cm to create a gradient junction. 
		e. Copy "Inf_Box" and "Sup_Box" across to CT 2 and adjust as necessary
	2. Run Pearl_ROI.py
	3. Check created ROIs look reasonable and then set CT 2 as the primary
	4. Run Pearl_ROI_CT2_update.py
	5. Run Pearl_Create_Plans.py
	6. Load beam and objective templates for each of the 3 plans created

Some adjustments may need to be made due to left or right laterality of the primary. E.g. ..._R objective changed to _L or anterior beam angle

Create a deformable registration with CT 2 as the reference and CT 1 as the target

After running the optimisation deform the dose from Phase 1 to CT 2, sum that dose in 15fx with Phase 2 with 18fx on CT 2
