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
    self.is_P_to_other = True


def convert(self):
    if self.is_P_to_other == False:
        self.other_dict = mot_to_dict(self.file_path)
    else:
        self.other_dict = {}
        # self.other_dict["[Header]"] = {}

    selection_machine_type(self)

    if self.is_P_to_other == False:
        for rule in self.rules_list:
            self.machine = rule.convert_to_P(
                self.other_dict, self.is_P_to_other, machine=self.machine
            )

    else:
        for rule in self.rules_list:
            self.other_dict = rule.convert_to_other(
                other_dict=self.other_dict, machine=self.machine, unit_list=None
            )

    # self.machine.stator.plot()
    print("Done")

    if self.is_P_to_other == False:
        return self.machine

    else:
        return self.other_dict
