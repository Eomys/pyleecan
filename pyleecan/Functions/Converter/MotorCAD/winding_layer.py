def other_to_P(self, machine, other_dict, other_unit_dict=None):
    """Conversion of winding

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
    other_path_list = ["[Winding_Design]", "Winding_Type"]
    Nlayer = self.get_other(other_dict, other_path_list, other_unit_dict)

    self.unit_type = ""
    other_path_list = ["[Magnetics]", "MagPathType"]
    type = self.get_other(other_dict, other_path_list, other_unit_dict)

    if Nlayer == "Overlapping":
        machine.stator.winding.Nlayer = 2
        if type == 2:
            machine.stator.winding.is_change_layer = True
        else:
            machine.stator.winding.is_change_layer = False

    else:
        machine.stator.winding.Nlayer = 1
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
