from pyleecan.Methods.Converter.Convert.convert_to_other import convert_to_other
from pyleecan.Methods.Converter.Convert.convert_to_P import convert_to_P

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

    machine = convert_to_P(path)
    other_dict = convert_to_other(machine)
    print("Done")
    # save_dict(path_save, other_dict)
