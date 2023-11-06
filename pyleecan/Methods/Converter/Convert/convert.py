from pyleecan.Classes.ConvertMC import ConvertMC
from pyleecan.Methods.Converter.ConvertMC.convert import convert


def selection_file():
    print("Enter path file other : ")
    path = input()

    return path


def convert_to_other(machine, dict_to_other):
    # liste_path = path_to_other.split(".")

    # if liste_path[1] == "mot":
    self = ConvertMC()
    self.is_P_to_other = True
    self.machine = machine
    self.other_dict = {}

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

    path = "pyleecan\pyleecan\Methods\Converter\ConvertMC\EMD240_v16.mot"
    machine = convert_to_P(path)
    dict_to_other = {}
    convert_to_other(machine, dict_to_other)
