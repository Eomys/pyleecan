def other_to_P(self, machine, other_dict):
    other_value = other_dict["[Dimensions]"]["Pole_Number"]
    machine.set_pole_pair_number(int(other_value / 2))

    print(f"set pole pair number :{other_value/2}")
    return machine


def P_to_other(self, machine, other_dict):
    pole_pair_number = machine.get_pole_pair_number() * 2
    if not "[Dimensions]" in other_dict:
        other_dict["[Dimensions]"] = {}
        other_dict["[Dimensions]"]["Pole_Number"] = pole_pair_number

    else:
        other_dict["[Dimensions]"]["Pole_Number"] = pole_pair_number
    return other_dict
