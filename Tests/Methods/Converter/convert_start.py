from pyleecan.Classes.ConvertMC import ConvertMC

if __name__ == "__main__":
    # path = selection_file()
    # path = "EMD240_v16.mot"

    path = "Matlab_Test_2.mot"
    # path_save = "other_dict.json"

    conv = ConvertMC()

    conv.machine = conv.convert_to_P(path)

    other_dict = conv.convert_to_other()
    print("Done")
    # save_dict(path_save, other_dict)
