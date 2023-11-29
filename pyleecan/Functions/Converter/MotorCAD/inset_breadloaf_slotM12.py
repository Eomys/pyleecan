from numpy import sin


def other_to_P(self, machine, other_dict, other_unit_dict):
    """Conversion of the slot inset_breadloaf (motor-cad) into the slotM12 (pyleecan)

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
    other_path_list = ["[Dimensions]", "Magnet_Thickness"]
    H1 = self.get_other(other_dict, other_path_list, other_unit_dict)

    self.unit_type = "ED"
    other_path_list = ["[Dimensions]", "Magnet_Arc_[ED]"]
    W1 = self.get_other(other_dict, other_path_list, other_unit_dict)

    Rbo = machine.rotor.get_Rbo()

    slot_width = (Rbo + H1) * sin(W1 / 2)
    machine.rotor.slot.W1 = 2 * slot_width
    machine.rotor.slot.W0 = 2 * slot_width

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
