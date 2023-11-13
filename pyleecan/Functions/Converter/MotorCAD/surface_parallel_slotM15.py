def other_to_P(self, machine, other_dict):
    """conversion obj machine in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    machine : Machine
        A pyleecan machine
    other_dict : dict
        A dict with the conversion obj machine

    Returns
    ---------
    machine : Machine
        A pyleecan machine
    """
    Rbo = machine.rotor.get_Rbo()
    H1 = other_dict["[Dimensions]"]["Magnet_Thickness"] * 0.001
    machine.rotor.slot.Rtopm = Rbo + H1

    return machine


def P_to_other(self, machine, other_dict):
    """conversion obj machine in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    machine : Machine
        A pyleecan machine
    other_dict : dict
        A dict with the conversion obj machine

    Returns
    ---------
    other_dict : dict
        A dict with the conversion obj machine
    """

    return other_dict
