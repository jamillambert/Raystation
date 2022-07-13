# Script to create a proton QA plan, Jamil Lambert 15/11/2019

from connect import *

plan = get_current("Plan")
beam_set = get_current("BeamSet")

with CompositeAction('Create QA Plan from Script'):
    beam_set.CreateQAPlan(PhantomName=r"40cm WaterPhantom", PhantomId=r"2QA-RCC-180919", QAPlanName="QA_"+plan.Name[0:12], IsoCenter={ 'x': 0, 'y': -20, 'z': 0 }, DoseGrid={ 'x': 0.1, 'y': 0.1, 'z': 0.1 }, GantryAngle=0, CouchRotationAngle=0, CollimatorAngle=None, ComputeDoseWhenPlanIsCreated=False, NumberOfMonteCarloHistories=None)   
    i = -1
    for j in plan.VerificationPlans:
        i = i + 1
    plan.VerificationPlans[i].UpdateVerificationPlanDoseGrid(Corner={ 'x': -12, 'y': -20.05, 'z': -14 }, VoxelSize={ 'x': 0.1, 'y': 0.1, 'z': 0.1 }, NumberOfVoxels={ 'x': 240, 'y': 340, 'z': 280 })


