from numpy import sin, tan
from pyleecan.Classes.Magnet import Magnet


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

    try:
        hole_id = self.param_dict["hole_id"]
    except:
        ValueError("hole_id isn't found")

    self.unit_type = "m"
    other_path_list = ["[Dimensions]", f"UShape_InnerDiameter_Array[{hole_id}]"]
    H1 = self.get_other(other_dict, other_path_list, other_unit_dict)

    Rbo = machine.rotor.get_Rbo()

    machine.rotor.hole[hole_id].H0 = Rbo - H1 / 2

    other_path_list = ["[Dimensions]", f"UMagnet_Length_Outer_Array[{hole_id}]"]
    H1 = self.get_other(other_dict, other_path_list, other_unit_dict)
    if H1 == 0:
        machine.rotor.hole[hole_id].W2 = None

    other_path_list = ["[Dimensions]", f"UMagnet_Length_Inner_Array[{hole_id}]"]
    H2 = self.get_other(other_dict, other_path_list, other_unit_dict)
    if H2 == 0:
        machine.rotor.hole[hole_id].W1 = None

    return machine


def P_to_other(self, machine, other_dict, other_unit_dict):
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
