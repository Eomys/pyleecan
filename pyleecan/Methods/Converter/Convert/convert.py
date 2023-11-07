from pyleecan.Classes.ConvertMC import ConvertMC
from pyleecan.Methods.Converter.ConvertMC.convert import convert

import json


def selection_file():
    print("Enter path file other : ")
    path = input()

    return path


def save_dict(path_save, other_dict):
    file = open("Tests//Methods//Converter" + "//" + path_save, "x")
    json.dump(other_dict, file)
    file.close()


def convert_to_other(machine, dict_to_other):
    # liste_path = path_to_other.split(".")

    # if liste_path[1] == "mot":
    self = ConvertMC()
    self.is_P_to_other = True
    self.machine = machine

    dict_to_other = convert(self)
    return dict_to_other


def convert_to_P(path_to_other):
    liste_path = path_to_other.split(".")

    if liste_path[1] == "mot":
        self = ConvertMC()
        self.is_P_to_other = False
        self.file_path = path_to_other
        machine = convert(self)

    return machine


if __name__ == "__main__":
    # path = selection_file()

    # path = "EMD240_v16.mot"
    path = "Matlab_Test_2.mot"
    # path_save = "other_dict.json"
    machine = convert_to_P(path)
    dict_to_other = {}
    other_dict = convert_to_other(machine, dict_to_other)
    # save_dict(path_save, other_dict)
