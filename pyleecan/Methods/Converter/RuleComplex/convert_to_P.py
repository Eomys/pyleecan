from pyleecan.Functions.Converter.RuleComplex.parallel_tooth_slotW11 import (
    slotW11_H1,
    parallel_tooth_slotW11,
)
from pyleecan.Functions.Converter.RuleComplex.def_rotor_slotW11 import (
    rotor_slotW11,
    rotor_slotW11_H1,
)

from pyleecan.Functions.Converter import *


def convert_to_P(self, other_dict, unit_list, machine):
    if self.fct_name == "parallel_tooth_slotW11":
        machine = globals()[self.fct_name](machine)

    elif self.fct_name == "slotW11_H1":
        machine = slotW11_H1(machine)

    elif self.fct_name == "rotor_slotW11":
        machine = rotor_slotW11(machine)
    elif self.fct_name == "rotor_slotW11_H1":
        machine = rotor_slotW11_H1(machine)

        # machine = globals()[self.fct_name](machine)

    elif self.fct_name == "set_pole_pair_number_py":
        other_value = other_dict["[Dimensions]"]["Pole_Number"]
        # set_pole_pair_number(machine, other_value)

    else:
        print("complex")

    return machine
