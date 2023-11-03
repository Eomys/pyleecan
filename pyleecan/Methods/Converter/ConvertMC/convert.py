from pyleecan.Classes.ConvertMC import ConvertMC
from pyleecan.Methods.Converter.ConvertMC.convert_mot_to_dict import mot_to_dict
from pyleecan.Methods.Converter.ConvertMC.selection_machine_type import (
    selection_machine_type,
)


def __init__():
    self = ConvertMC
    self.rules_list = []
    self.other_dict = {}
    self.machine = None
    self.P_to_other = False
    convert(self)


def convert(self):
    file_path = "EMD240_v16.mot"
    self.other_dict = mot_to_dict(file_path)

    selection_machine_type(self)

    for rule in self.rules_list:
        self.machine = rule.convert_to_P(self.other_dict, None, self.machine)

    self.machine.stator.plot()
    print("Done")


if __name__ == "__main__":
    __init__()
