from pyleecan.Classes.ConvertMC import ConvertMC
from pyleecan.Methods.Converter.ConvertMC.convert_other_to_dict import (
    convert_other_to_dict,
)


def __init__():
    self = ConvertMC
    self.rules_list = []
    self.other_dict = {}
    self.machine = None
    self.is_P_to_other = True


def convert(self):
    """convert the file .mot in machine pyleecan or vice versa

    Parameters
    ----------
    class ConvertMC

    is_P_to_other : bool
        True conversion pyleecan to other, False conversion other to pyleecan
    rules_list : list
        list with all rules,
    other_dict : dict
        A dict with all parameters motor_cad used to conversion or implementation after conversion obj machine
    machine : Machine
        A Machine with all parameters pyleecan used to conversion or implementation after conversion dict
    file_path : str
        path file use to convert
    """

    # conversion file in dict
    if self.is_P_to_other == False:
        self.other_dict = convert_other_to_dict(self.file_path)

    self.selection_machine_rules()

    # conversion rules list
    if self.is_P_to_other == False:
        for rule in self.rules_list:
            self.machine = rule.convert_to_P(self.other_dict, self.machine)
        self.machine.stator.plot()
        self.machine.plot()
        print("Done")
        return self.machine

    else:
        for rule in self.rules_list:
            self.other_dict = rule.convert_to_other(
                self.other_dict,
                self.machine,
            )
        print("Done")
        return self.other_dict
