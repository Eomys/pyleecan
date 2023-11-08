from pyleecan.Methods.Converter.Convert.convert_to_other import convert_to_other
from pyleecan.Methods.Converter.Convert.convert_to_P import convert_to_P
from pyleecan.Classes.ConvertMC import ConvertMC

import json


def selection_file():
    print("Enter path file other : ")
    path = input()

    return path


def save_dict(path_save, other_dict):
    file = open("Tests//Methods//Converter" + "//" + path_save, "x")
    json.dump(other_dict, file)
    file.close()


if __name__ == "__main__":
    # path = selection_file()
    # path = "EMD240_v16.mot"

    path = "Matlab_Test_2.mot"
    # path_save = "other_dict.json"

    converter = ConvertMC()
    converter.file_path = path

    converter.machine = convert_to_P(converter)

    other_dict = convert_to_other(converter)
    print("Done")
    # save_dict(path_save, other_dict)
