from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap


def convert_duct_type_P(self, is_stator):
    """selection step to add rules for slot

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

    type_duct = self.other_dict["[Through_Vent]"][f"{lam_name}DuctType"]

    if type_duct == 0:
        print(f"not axial cooling duct at {lam_name}")

    elif type_duct == 1:  # CircularDuct
        number_duct = self.other_dict["[Dimensions]"][f"{lam_name}RadialDuct_Number"]
        for duct_id in range(number_duct):
            self.machine.lam_name.axial_vent.append(VentilationCirc())
            self.add_rule_circular_duct_circular(is_stator)

    elif type_duct == 2:
        name_type_duct = "SahftSpoke"

    elif type_duct == 3:
        name_type_duct = "ArcDuct"
        number_duct = self.other_dict["[Dimensions]"][f"{lam_name}RadialDuct_Number"]
        for duct_id in range(number_duct):
            self.machine.lam_name.axial_vent.append(VentilationPolar())

    elif type_duct == 4:
        name_type_duct = "RectangularDuct"
        number_duct = self.other_dict["[Dimensions]"][f"{lam_name}RadialDuct_Number"]
        for duct_id in range(number_duct):
            self.machine.lam_name.axial_vent.append(VentilationTrap())

    temp = self.other_dict["[Through_Vent]"][f"{lam_name}{name_type_duct}Layers"]
    for nb_duct in range(temp):
        self.add_rules_duct_layer(
            self,
            lam_name,
            nb_duct,
            name_type_duct,
        )
