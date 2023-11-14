from pyleecan.Classes.ConvertMC import ConvertMC

if __name__ == "__main__":
    # path = selection_file()
    # path = "/Users\LAP17\Documents\pyleecan\pyleecan\Methods\Converter\ConvertMC\EMD240_v16.mot"
    # path = "/Users\LAP17\Documents\pyleecan\pyleecan\Methods\Converter\ConvertMC\parallel_tooth_interior_V_simple.mot"
    path = "/Users\LAP17\Documents\pyleecan\pyleecan\Methods\Converter\ConvertMC\Matlab_Test_2.mot"
    # path_save = "other_dict.json"

    conv = ConvertMC()

    machine = conv.convert_to_P(path)
    machine.plot()

    other_dict = conv.convert_to_other(machine)
    print("Done")
    # save_dict(path_save, other_dict)
