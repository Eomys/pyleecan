from pyleecan.Classes.ConvertMC import ConvertMC
from pyleecan.Methods.Converter.ConvertMC.convert_mot_to_dict import mot_to_dict
from pyleecan.Methods.Converter.ConvertMC.selection_machine_type import (
    selection_machine_type,
)


def __init__():
    self = ConvertMC
    self.rules_list = []
    self.other_dict = {}
    # self.file_path = None
    self.machine = None
    self.is_P_to_other = True
    convert(self)


def convert(self):
    # file_path = "EMD240_v16.mot"
    # self.rules_list = []
    # self.other_dict = {}

    file_path = "EMD240_v16.mot"
    self.other_dict = mot_to_dict(file_path)

    # if self.is_P_to_other == False:
    #    self.other_dict = mot_to_dict(self.file_path)

    selection_machine_type(self)

    for rule in self.rules_list:
        self.machine = rule.convert_to_P(
            self.other_dict, self.is_P_to_other, self.machine
        )

    self.machine.stator.plot()
    print("Done")
    if self.is_P_to_other == False:
        return self.machine


if __name__ == "__main__":
    __init__()
