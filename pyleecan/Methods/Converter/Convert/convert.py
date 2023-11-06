from pyleecan.Classes.ConvertMC import ConvertMC
from pyleecan.Methods.Converter.ConvertMC.convert import convert


def selection_file():
    print("Enter path file other : ")
    path = input()

    return path


def convert_to_other(machine, path_to_other):
    liste_path = path_to_other.split(".")

    if liste_path[1] == "mot":
        convert(file_path=path_to_other, machine=machine, is_P_to_other=True)


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
    convert_to_P(path)
