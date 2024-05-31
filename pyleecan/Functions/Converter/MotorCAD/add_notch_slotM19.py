from numpy import cos, sqrt


def other_to_P(self, machine, other_dict, other_unit_dict):
    """Converts motor-cad notch into pyleecan notch slotM19

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
    other_path_list = ["[Dimensions]", "PoleNotchDepth"]
    H0 = self.get_other(other_dict, other_path_list, other_unit_dict)
    Rbo = machine.rotor.get_Rbo()

    self.unit_type = "ED"
    other_path_list = ["[Dimensions]", "PoleNotchArc_Outer"]
    W1 = self.get_other(other_dict, other_path_list, other_unit_dict)

    self.unit_type = "ED"
    other_path_list = ["[Dimensions]", "PoleNotchArc_Inner"]
    W0 = self.get_other(other_dict, other_path_list, other_unit_dict)

    machine.rotor.notch[0].notch_shape.W1 = sqrt(2 * Rbo**2 * (1 - cos(W1)))
    machine.rotor.notch[0].notch_shape.W0 = sqrt(2 * (Rbo - H0) ** 2 * (1 - cos(W0)))

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
