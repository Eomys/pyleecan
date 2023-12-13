from numpy import arccos, pi


def other_to_P(self, machine, other_dict, other_unit_dict):
    """Conversion of the slot arc duct (motor-cad) into polar duct (pyleecan)

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

    if isinstance(self.param_dict["duct_id"], int):
        duct_id = self.param_dict["duct_id"]
    else:
        ValueError("duct_id isn't int")

    lam_name_MC = self.param_dict["lam_name_MC"]
    lam_name_py = self.param_dict["lam_name_py"]

    other_path_list = [
        "[Through_Vent]",
        f"{lam_name_MC}CircularDuctLayer_Channels[{duct_id}]",
    ]
    self.unit_type = ""
    Zh = self.get_other(other_dict, other_path_list, other_unit_dict)
    gamma = 2 * pi / Zh

    self.unit_type = "m"
    other_path_list = [
        "[Through_Vent]",
        f"{lam_name_MC}ArcDuctLayer_InnerDiameter[{duct_id}]",
    ]
    H0 = self.get_other(other_dict, other_path_list, other_unit_dict)
    H0 = H0 * 0.5

    self.unit_type = "m"
    other_path_list = [
        "[Through_Vent]",
        f"{lam_name_MC}ArcDuctLayer_WebWidth[{duct_id}]",
    ]
    A = self.get_other(other_dict, other_path_list, other_unit_dict)

    other_value = gamma - (pi / 180) * arccos((2 * H0 * H0 - A * A) / (2 * H0))

    path = f"machine.{lam_name_py}.axial_vent[{duct_id}].W1"
    self.set_P(machine, other_value, path)
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
