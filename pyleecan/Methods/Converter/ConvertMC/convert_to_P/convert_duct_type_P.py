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

    # selection of number and type layers
    try:
        type_duct = self.other_dict["[Through_Vent]"][f"{lam_name}_Duct_Type"]
    except:
        type_duct = f"No_{lam_name}_Duct"

    if type_duct == f"No_{lam_name}_Duct":
        self.get_logger().info(f"not axial cooling duct at {lam_name}")

    elif type_duct == f"{lam_name}_Circular_Ducts":  # CircularDuct
        number_duct = self.other_dict["[Dimensions]"][f"{lam_name}RadialDuct_Number"]
        for duct_id in range(number_duct):
            if is_stator == True:
                self.machine.stator.axial_vent.append(VentilationCirc())
            else:
                self.machine.rotor.axial_vent.append(VentilationCirc())
            self.add_rule_circular_duct_circular(is_stator, duct_id)

    elif type_duct == 2:  # Shaft_spoke
        self.get_logger().info(f"ShaftSpoke ins't define in pyleecan")

    elif type_duct == f"{lam_name}_Arc_Ducts":  # Arcduct
        number_duct = self.other_dict["[Dimensions]"][f"{lam_name}RadialDuct_Number"]
        for duct_id in range(number_duct):
            if is_stator == True:
                self.machine.stator.axial_vent.append(VentilationPolar())
            else:
                self.machine.rotor.axial_vent.append(VentilationPolar())
            self.add_rule_arc_duct_polar(is_stator, duct_id)

    elif type_duct == f"{lam_name}_Rectangular_Ducts":  # RectangularDuct
        number_duct = self.other_dict["[Dimensions]"][f"{lam_name}RadialDuct_Number"]
        for duct_id in range(number_duct):
            if is_stator == True:
                self.machine.stator.axial_vent.append(VentilationTrap())
            else:
                self.machine.rotor.axial_vent.append(VentilationTrap())
            self.add_rule_rectangular_duct_trapeze(is_stator, duct_id)

    else:
        raise NameError("type of duct have not equivalent in pyleecan")
