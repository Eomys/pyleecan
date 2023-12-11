def other_to_P(self, machine, other_dict, other_unit_dict):
    """Conversion of the slot interior_U_shape (motor-cad) into the holeM61 (pyleecan)

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
    other_path_list = ["[Dimensions]", f"UShape_InnerDiameter_Array[{hole_id}]"]
    H1 = self.get_other(other_dict, other_path_list, other_unit_dict)

    Rbo = machine.rotor.get_Rbo()

    # Set H0
    machine.rotor.hole[hole_id].H0 = Rbo - H1 / 2

    # Set W2
    other_path_list = ["[Dimensions]", f"UMagnet_Length_Outer_Array[{hole_id}]"]
    H1 = self.get_other(other_dict, other_path_list, other_unit_dict)
    if H1 == 0:
        machine.rotor.hole[hole_id].W2 = None

    # Set W1
    other_path_list = ["[Dimensions]", f"UMagnet_Length_Inner_Array[{hole_id}]"]
    H2 = self.get_other(other_dict, other_path_list, other_unit_dict)
    if H2 == 0:
        machine.rotor.hole[hole_id].W1 = None

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
