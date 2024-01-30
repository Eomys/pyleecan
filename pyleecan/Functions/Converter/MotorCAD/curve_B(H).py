from ....Classes.ImportMatrixVal import ImportMatrixVal


def other_to_P(self, machine, other_dict, other_unit_dict):
    """Converts motor-cad curve B(H) into pyleecan

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
    path_P = self.param_dict["path_P"]
    material = self.param_dict["material"]

    # exemple curve into file .mot
    # "BValue[0]": "0",
    # "HValue[0]": "0",
    # "BValue[1]": "0.015649299",
    # "HValue[1]": "5.925085189",
    # "BValue[2]": "0.029080305",
    # "HValue[2]": "9.92738115",

    is_BH = True
    idx_BH = 0
    curve_BH = []

    # selection all value in file.mot
    while is_BH:
        try:
            B_value = other_dict[f"[{material}]"][f"BValue[{idx_BH}]"]
            H_value = other_dict[f"[{material}]"][f"HValue[{idx_BH}]"]
            idx_BH += 1
            curve_BH.append([H_value, B_value])

        except:
            is_BH = False

    if len(curve_BH) == 0:
        other_value = None
    else:
        other_value = curve_BH

        path = f"{path_P}.mag.BH_curve"

        # set class ImportMatrixVal into machine
        # set value in object machine
        value_split = path.split(".")

        # value_split[-1] is the attribut that we want to set ("W1")
        # path is the attribut chain to set the attribut ("machine.stator.slot")
        path = ".".join(value_split[:-1])

        setattr(
            eval(path),
            value_split[-1],
            ImportMatrixVal(),
        )

        # set curve B(H) into class add previously
        path = f"{path_P}.mag.BH_curve.value"

        self.set_P(machine, other_value, path)

    # set name of material
    path_name = f"{path_P}.name"
    other_value = f"{material}"
    self.set_P(machine, other_value, path_name)

    # set is_isotropic
    path = f"{path_P}.is_isotropic"
    other_value = True
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
