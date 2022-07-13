from connect import *
import ctypes, sys

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

# cycling through beams
for beam in beam_set.Beams:
    print(beam.Name)

    # cycling through layers
    for segment in beam.Segments:
        spots_x = []
        spots_y = []
        spots_weight = []
        nominal_energy = segment.NominalEnergy
        z = 0

        # cycling through spots
        for spots in segment.Spots.Positions:
            temp_spot_weight = segment.Spots.Weights[z]

            # checking if spot is in adjustment zone
            if spots.x < -3.8 and spots.x > -5.4:
                if spots.y < -5.4 and spots.y > -6.1:
                    temp_spot_weight = temp_spot_weight * 0.89

            # setting layer spot data
            spots_x.append(spots.x)
            spots_y.append(spots.y)
            spots_weight.append(temp_spot_weight)

            z += 1

        print('finished layer')
        beam.AddEnergyLayerWithSpots(Energy=nominal_energy, SpotPositionsX=spots_x,
                                     SpotPositionsY=spots_y, SpotWeights=spots_weight)
        segment.RemoveEnergyLayer()
