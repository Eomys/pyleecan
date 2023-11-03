from pyleecan.Methods.Machine.Machine.set_pole_pair_number import set_pole_pair_number


def other_to_P(machine, other_dict):
    other_value = other_dict["[Dimensions]"]["Pole_Number"]

    # set_pole_pair_number(machine, other_value)

    return machine


def P_to_other(self, machine):
    print("other_to_P")
