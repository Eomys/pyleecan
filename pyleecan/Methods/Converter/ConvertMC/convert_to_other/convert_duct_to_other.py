def convert_duct_to_other(self, is_stator):
    """selection step to add rules for duct

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor
    """

    if is_stator == True:
        lam_name_MC = "Stator"
        axial_vent = self.machine.stator.axial_vent

    else:
        lam_name_MC = "Rotor"
        axial_vent = self.machine.rotor.axial_vent

    if len(axial_vent) != 0:
        type_duct = axial_vent[0].__class__.__name__

        for nb_duct, duct in enumerate(axial_vent):
            if type_duct != type(axial_vent[nb_duct]).__name__:
                self.get_logger().error(
                    "A Motor-cad machine can only have one type of axial duct"
                )
                return

            type_duct = type(duct).__name__

            # selection of number and type layers
            if type_duct == None:
                return
            # CircularDuct
            elif type_duct == "VentilationCirc":
                self.add_rule_circular_duct_circular(is_stator, nb_duct)
                duct_MC_name = "Rotor_Circular_Ducts"

            # Arcduct
            elif type_duct == "VentilationPolar":
                self.add_rule_arc_duct_polar(is_stator, nb_duct)
                duct_MC_name = "Rotor_Arc_Ducts"

            # RectangularDuct
            elif type_duct == "VentilationTrap":
                self.add_rule_rectangular_duct_trapeze(is_stator, nb_duct)
                duct_MC_name = "Rotor_Rectangular_Ducts"
            else:
                raise NotImplementedError(
                    f"Type of duct {type_duct} has not equivalent or has not implement"
                )

            # writting in dict
            if "[Through_Vent]" not in self.other_dict:
                self.other_dict["[Through_Vent]"] = {
                    f"{lam_name_MC}_Duct_Type": duct_MC_name
                }
            else:
                self.other_dict["[Through_Vent]"][
                    f"{lam_name_MC}_Duct_Type"
                ] = duct_MC_name

            self.get_logger().info(f"Conversion {type_duct} into {duct_MC_name}")
