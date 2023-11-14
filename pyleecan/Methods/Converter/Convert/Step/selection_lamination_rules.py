from pyleecan.Classes.VentilationCirc import VentilationCirc


def selection_lamination_rules(self, is_stator):
    """selection step to add rules for lamination

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """
    if is_stator == True:
        lam_name = "Stator"
    else:
        lam_name = "Rotor"

    # sélection of number and type layers
    if not self.is_P_to_other:
        try:
            type_duct = self.other_dict["[Through_Vent]"][f"{lam_name}DuctType"]
        except:
            type_duct = 0

        if type_duct != 0:
            self.convert_duct_type_P(is_stator)

        else:
            print(f"not axial cooling duct at {lam_name}")
