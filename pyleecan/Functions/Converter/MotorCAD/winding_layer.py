def other_to_P(self, machine, other_dict, other_unit_dict=None):
    """Conversion of the set_pole_pair_number

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
    self.unit_type = ""
    other_path_list = ["[Winding_Design]", "Liner_Layers"]
    Nlayer = self.get_other(other_dict, other_path_list, other_unit_dict)

    if Nlayer == "Single_Layer":
        machine.stator.winding.Nlayer = 1
    elif Nlayer == "Double_Layer":
        machine.stator.winding.Nlayer = 2

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

    pass
