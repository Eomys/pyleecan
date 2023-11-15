from numpy import sin, tan


def other_to_P(self, machine, other_dict, other_unit_dict):
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
    machine : Machine
        A pyleecan machine
    """
    self.unit_type = "m"
    other_path_list = ["[Dimensions]", f"UShape_InnerDiameter_Array[{self.id}]"]
    H1 = self.get_other(other_dict, other_path_list, other_unit_dict)

    Rbo = machine.rotor.get_Rbo()

    machine.rotor.hole[self.id].H0 = Rbo - H1 / 2
    machine.rotor.hole[self.id].W1 = 0.001
    machine.rotor.hole[self.id].W2 = 0.001

    return machine


def P_to_other(self, machine, other_dict):
    """conversion obj machine in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    machine : Machine
        A pyleecan machine
    other_dict : dict
        A dict with the conversion obj machine

    Returns
    ---------
    other_dict : dict
        A dict with the conversion obj machine
    """

    return other_dict
