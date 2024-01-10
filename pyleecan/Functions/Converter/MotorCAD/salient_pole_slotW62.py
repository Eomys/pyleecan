from numpy import sin, exp


def other_to_P(self, machine, other_dict, other_unit_dict):
    """Conversion of the slot salient_pole (motor-cad) into the slotW62 (pyleecan)

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

    self.unit_type = "m"
    other_path_list = ["[Dimensions]", "Pole_Tip_Depth"]
    H1 = self.get_other(other_dict, other_path_list, other_unit_dict)

    Rbo = machine.rotor.get_Rbo()

    machine.rotor.slot.H1 = H1
    point_dict = machine.rotor.slot._comp_point_coordinate()

    Z1 = Rbo * exp(-1j * 0)
    Z7 = point_dict["Z7"]

    H = abs(Z7.real - Z1.real)

    machine.rotor.slot.H1 = H1 - H

    return machine


def P_to_other(self, machine, other_dict, other_unit_dict=None):
    """conversion obj machine into dict

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
