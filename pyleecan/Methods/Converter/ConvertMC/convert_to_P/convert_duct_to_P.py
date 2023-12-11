from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap


def convert_duct_to_P(self, is_stator):
    """selection step to add rules for duct

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True lam is in stator, False lam is in rotor

    """
    # selection of lamination
    if is_stator == True:
        self.get_logger().info("stator_duct, not implemented")
        return

    else:
        lam_name = "Rotor"
        axial_vent = self.machine.rotor.axial_vent

    # selection type layers
    if f"{lam_name}_Duct_Type" in self.other_dict["[Through_Vent]"]:
        type_duct = self.other_dict["[Through_Vent]"][f"{lam_name}_Duct_Type"]
    else:
        type_duct = f"No_{lam_name}_Ducts"

    # Selection type of duct
    if type_duct == f"No_{lam_name}_Ducts":
        self.get_logger().debug(f"No duct to convert at {lam_name}")

    else:
        number_duct = self.other_dict["[Through_Vent]"][f"{lam_name}CircularDuctLayers"]
        # CircularDuct
        if type_duct == f"{lam_name}_Circ_Ducts" or type_duct == "Circ_Ducts":
            Ventilation_class = VentilationCirc

        # Shaft_spoke
        elif type_duct == f"{lam_name}_Shaft_Spoke_Ducts":
            self.get_logger().info(f"ShaftSpoke ins't define in pyleecan")

        # Arcduct
        elif type_duct == f"{lam_name}_Arc_Ducts":
            Ventilation_class = VentilationPolar

        # RectangularDuct
        elif type_duct == f"{lam_name}_Rect_Ducts" or type_duct == "Rect_Ducts":
            # Error convert is not Implemented
            self.get_logger().info("Rect_Ducts, Not Implemented")
            return
            # Ventilation_class = VentilationTrap

        else:
            raise NotImplementedError(
                f"Type of duct {type_duct} has any equivalent in pyleecan or has not been implemented"
            )

        for duct_id in range(number_duct):
            axial_vent.append(Ventilation_class())
            self.get_logger().info(
                f"Conversion {type_duct} into {Ventilation_class.__name__}"
            )
