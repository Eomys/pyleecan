def other_to_P(self, machine, other_dict, other_unit_dict):
    """Converts the MLT motor-cad slot into pyleecan lewout

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
    other_path_list = ["[Winding_Design]", "EWdg_MLT"]
    MLT = self.get_other(other_dict, other_path_list, other_unit_dict)

    if machine.stator.winding.end_winding is None:
        cp = 0
    else:
        cp = machine.stator.winding.end_winding.comp_length()

    lewout = 1 / 2 * (MLT / 2 - machine.stator.comp_length()) - cp

    machine.stator.winding.Lewout = lewout / 1000  # convertion mm to m
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
