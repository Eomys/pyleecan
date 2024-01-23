from ....Functions.Converter.Utils.ConvertionError import ConvertionError
from numpy import pi


def other_to_P(self, machine, other_dict, other_unit_dict):
    """Converts motor-cad skew into pyleecan skew

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

    skew_step = other_dict["[Magnetics]"]["RotorSkewSlices"]

    # Exemple list of skew in dict
    # "RotorSkewAngle_Array[0]": -4,
    # "RotorSkewAngle_Array[1]": -2,
    # "RotorSkewAngle_Array[2]": 0,
    # "RotorSkewAngle_Array[3]": 2,
    # "RotorSkewAngle_Array[4]": 4,

    idx_skew = 0
    skew_list = []

    # selection of all parameter for skew
    for idx_skew in range(skew_step):
        try:
            skew_value = other_dict[f"[Magnetics]"][f"RotorSkewAngle_Array[{idx_skew}]"]

            # convertion deg in rad
            skew_value = skew_value * pi / 180

            idx_skew += 1
            skew_list.append(skew_value)

        except:
            pass

    # add skew in obj machine
    if len(skew_list) == 0:
        other_value = None
        raise ConvertionError("Error for convertion, list of skew angle are not set")
    else:
        path = f"machine.rotor.skew.angle_list"

        self.set_P(machine, skew_list, path)

    # set overall of skew
    min_ele = min(skew_list)
    max_ele = max(skew_list)

    angle_overall = abs(max_ele - min_ele)
    path_name = "machine.rotor.skew.angle_overall"
    other_value = angle_overall
    self.set_P(machine, other_value, path_name)

    # set name of skew
    path_name = f"machine.rotor.skew.type_skew"
    other_value = "user-defined"
    self.set_P(machine, other_value, path_name)

    # set number of step for skew
    path_name = f"machine.rotor.skew.Nstep"
    other_value = skew_step
    self.set_P(machine, other_value, path_name)
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
