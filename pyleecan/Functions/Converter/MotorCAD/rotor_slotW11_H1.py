def other_to_P(self, machine, other_dict, other_unit_dict=None):
    """Conversion H1 in m to slotW11

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    machine : Machine
        A obj machine
    other_dict : dict
        A dict with the conversion obj machine
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)

    Return
    ---------
    machine : Machine
        A obj machine
    """
    # H1 has already been defined in [rad] with a RuleSimple
    H1 = machine.rotor.slot.get_H1()
    machine.rotor.slot.H1_is_rad = False
    machine.rotor.slot.H1 = H1

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
    return other_dict
