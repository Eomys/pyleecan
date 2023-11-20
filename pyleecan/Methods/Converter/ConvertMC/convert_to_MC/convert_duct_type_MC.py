def convert_duct_type_MC(self, is_stator):
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
    else:
        lam_name_MC = "Rotor"

    # conversion to motor-cad
    if (len(self.machine.rotor.axial_vent)) == 0:
        pass
    elif (len(self.machine.stator.axial_vent)) == 0:
        pass
    else:
        type_duct = type(self.machine.rotor.axial_vent[0]).__name__

        for nb_duct in range(len(self.machine.rotor.axial_vent)):
            if type_duct != self.machine.rotor.axial_vent[nb_duct]:
                self.get_logger().error(
                    "in Motor-cad, we have just the possibility to have 1 type od duct"
                )

            if is_stator == True:
                type_duct = type(self.machine.stator.axial_vent[nb_duct]).__name__
            else:
                type_duct = type(self.machine.rotor.axial_vent[nb_duct]).__name__

            # selection of number and type layers

            if type_duct == None:
                pass

            elif type_duct == "VentilationCirc":  # CircularDuct
                self.add_rule_circular_duct_circular(is_stator, nb_duct)
                self.other_dict["[Through_Vent]"][
                    f"{lam_name_MC}_Duct_Type"
                ] = "Rotor_Circular_Ducts"
                self.get_logger().info(
                    f"Conversion {type_duct} into Rotor_Circular_Ducts"
                )

            elif type_duct == "VentilationPolar":  # Arcduct
                self.add_rule_arc_duct_polar(is_stator, nb_duct)
                self.other_dict["[Through_Vent]"][
                    f"{lam_name_MC}_Duct_Type"
                ] = "Rotor_Arc_Ducts"
                self.get_logger().info(f"Conversion {type_duct} into Rotor_Arc_Ducts")

            elif type_duct == "VentilationTrap":  # RectangularDuct
                self.add_rule_rectangular_duct_trapeze(is_stator, nb_duct)
                self.other_dict["[Through_Vent]"][
                    f"{lam_name_MC}_Duct_Type"
                ] = "Rotor_Rectangular_Ducts"

                self.get_logger().info(
                    f"Conversion {type_duct} into Rotor_Rectangular_Ducts"
                )

            else:
                raise NameError("type of duct have not equivalent in pyleecan")
