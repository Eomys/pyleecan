from pyleecan.Classes.ConvertMC import ConvertMC
from pyleecan.Classes.CondType12 import CondType12

if __name__ == "__main__":
    # cleaning log file
    f = open("/Users\LAP17\AppData\Roaming\pyleecan/Pyleecan.log", "w")
    f.close()

    # path = selection_file()
    # path_save = "other_dict.json"
    # path = "/Users\LAP17\Documents\pyleecan\pyleecan\Methods\Converter\ConvertMC/EMD240_v16.mot"
    # path = "/Users\LAP17\Documents\pyleecan\pyleecan\Methods\Converter\ConvertMC/parallel_tooth_interior_V_simple.mot"
    # path = "/Users\LAP17\Documents\pyleecan\pyleecan\Methods\Converter\ConvertMC/Matlab_Test_2.mot"
    path = "/Users\LAP17\Documents/Documentation motor-CAD/fichier.mot/various_mot_files/VF_Manatee_Hairpin_winding.mot"

    conv = ConvertMC()

    machine = conv.convert_to_P(path)
    machine.plot()

    other_dict = conv.convert_to_other(machine)

    machine.stator.winding.conductor = CondType12()
    machine.stator.winding.conductor.Nwppc = 13

    machine.save(f"/Users/LAP17/Documents/machine_mot_convert_in_P/{machine.name}")
    print("Done")
    # save_dict(path_save, other_dict)
