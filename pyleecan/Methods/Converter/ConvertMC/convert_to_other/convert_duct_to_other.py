from .....Classes.VentilationCirc import VentilationCirc
from .....Classes.VentilationPolar import VentilationPolar
from .....Classes.VentilationTrap import VentilationTrap


def convert_duct_to_other(self, is_stator):
    """selects step to add rules for duct

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor
    """
    # Single type
    # Multi set

    if is_stator:
        lam_name_MC = "Stator"
        axial_vent = self.machine.stator.axial_vent

    else:
        lam_name_MC = "Rotor"
        axial_vent = self.machine.rotor.axial_vent

    # If there is any axial_vent, then do nothing
    if len(axial_vent) == 0:
        return

    elif len(axial_vent) > 1:
        for duct in axial_vent:
            if isinstance(duct, axial_vent[0].__class__):
                self.get_logger().error(
                    "A Motor-cad machine can only have one type of axial duct"
                )
                break

    # selection type duct, single type in Motor-CAD
    if isinstance(axial_vent[0], VentilationCirc):
        # CircularDuct
        duct_MC_name = "Rotor_Circular_Ducts"

    elif isinstance(axial_vent[0], VentilationPolar):
        # Arcduct
        duct_MC_name = "Rotor_Arc_Ducts"

    elif isinstance(axial_vent[0], VentilationTrap):
        # RectangularDuct
        duct_MC_name = "Rotor_Rectangular_Ducts"
    else:
        raise NotImplementedError(
            f"Type of duct {axial_vent[0].__name__} has not equivalent or has not been implementated"
        )

    # writting in dict
    if "[Through_Vent]" not in self.other_dict:
        self.other_dict["[Through_Vent]"] = {f"{lam_name_MC}_Duct_Type": duct_MC_name}
    else:
        self.other_dict["[Through_Vent]"][f"{lam_name_MC}_Duct_Type"] = duct_MC_name

    self.get_logger().info(f"Conversion {axial_vent[0].__name__} into {duct_MC_name}")
