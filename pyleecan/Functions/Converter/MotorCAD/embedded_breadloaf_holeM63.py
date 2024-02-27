from numpy import tan


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
    if isinstance(self.param_dict["hole_id"], int):
        hole_id = self.param_dict["hole_id"]
    else:
        ValueError("hole_id isn't int")

    self.unit_type = "m"
    other_path_list = ["[Dimensions]", "Magnet_Embed_Depth"]
    H1 = self.get_other(other_dict, other_path_list, other_unit_dict)
    Rbo = machine.rotor.get_Rbo()

    H = Rbo - H1
    self.unit_type = "ED"
    other_path_list = ["[Dimensions]", "Magnet_Arc_[ED]"]
    W0 = self.get_other(other_dict, other_path_list, other_unit_dict)

    Rbo = machine.rotor.get_Rbo()

    W0 = H * tan(W0 / 2)

    machine.rotor.hole[hole_id].W0 = W0 * 2

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
