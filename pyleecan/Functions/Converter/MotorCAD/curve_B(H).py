from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal


def other_to_P(self, machine, other_dict, other_unit_dict):
    """Converts motor-cad notch into pyleecan notch slotM19

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

    is_BH = True
    idx_BH = 0
    curve_BH = []
    while is_BH:
        try:
            B_value = other_dict[f"[{material}]"][f"BValue[{idx_BH}]"]
            H_value = other_dict[f"[{material}]"][f"HValue[{idx_BH}]"]
            idx_BH += 1
            curve_BH.append([B_value, H_value])

        except:
            is_BH = False

    if len(curve_BH) == 0:
        other_value = None
    else:
        other_value = curve_BH

        path = f"{path_P}.mag.BH_curve"

        if not isinstance(path.__class__, ImportMatrixVal):
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

        path = f"{path_P}.mag.BH_curve.value"

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
