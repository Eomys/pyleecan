def other_to_P(self, machine, other_dict, other_unit_dict=None):
    """Converts the pole pair number

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    machine : Machine
        A pyleecan machine
    other_dict : dict
        A dict with the conversion obj machine
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)

    Returns
    ---------
    machine : Machine
        A pyleecan machine
    """
    other_value = other_dict["[Dimensions]"]["Pole_Number"]
    machine.set_pole_pair_number(other_value // 2)

    return machine


def P_to_other(self, machine, other_dict, other_unit_dict=None):
    """conversion obj machine in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    machine : Machine
        A pyleecan machine
    other_dict : dict
        A dict with the conversion obj machine
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)

    Returns
    ---------
    other_dict : dict
        A dict with the conversion obj machine
    """

    pole_pair_number = machine.get_pole_pair_number() * 2

    if not "[Dimensions]" in other_dict:
        other_dict["[Dimensions]"] = {}

    other_dict["[Dimensions]"]["Pole_Number"] = pole_pair_number

    return other_dict
