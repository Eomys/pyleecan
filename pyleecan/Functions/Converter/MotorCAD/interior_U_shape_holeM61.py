def other_to_P(self, machine, other_dict, other_unit_dict):
    """Converts interior_U_shape motor-cad slot into pyleecan holeM61
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
    other_path_list = ["[Dimensions]", "Magnet_Inner_Diameter"]
    H1 = self.get_other(other_dict, other_path_list, other_unit_dict)

    Rbo = machine.rotor.get_Rbo()

    self.unit_type = "m"
    other_path_list = ["[Dimensions]", "Magnet_Layer_Gap_Inner"]
    h = self.get_other(other_dict, other_path_list, other_unit_dict)

    self.unit_type = "m"
    other_path_list = ["[Dimensions]", "Magnet_Thickness"]
    h1 = self.get_other(other_dict, other_path_list, other_unit_dict)

    # In MC length of magnet is defined in % of the length of hole
    # In Pyleecan W1[m] and W2[m]
    # Set H0
    machine.rotor.hole[hole_id].H0 = Rbo - H1 / 2 - hole_id * (h + h1)

    point_dict = machine.rotor.hole[hole_id]._comp_point_coordinate()
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]

    # Set W2
    self.unit_type = ""
    other_path_list = ["[Dimensions]", "Magnet_Fill_Outer"]
    P2 = self.get_other(other_dict, other_path_list, other_unit_dict)
    if P2 == 0:
        machine.rotor.hole[hole_id].W2 = None
    else:
        machine.rotor.hole[hole_id].W2 = abs(Z4 - Z3) * P2 / 100

    # Set W1
    self.unit_type = ""
    other_path_list = ["[Dimensions]", "Magnet_Fill_Inner"]
    P1 = self.get_other(other_dict, other_path_list, other_unit_dict)
    if P1 == 0:
        machine.rotor.hole[hole_id].W1 = None
    else:
        machine.rotor.hole[hole_id].W1 = abs(Z3 - Z2) * P1 / 100

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
