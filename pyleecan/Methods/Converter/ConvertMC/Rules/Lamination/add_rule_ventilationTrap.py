from ......Classes.RuleSimple import RuleSimple


def add_rule_ventilationTrap(self, is_stator, duct_id):
    """Create and adapt all the rules related to duct
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        A booleen to know, position in lamination
    duct_id : int
        a int to know the number of duct
    """

    if is_stator:
        lam_name_MC = "Stator"

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"iCircularDuctL{duct_id}RadialDiameter",
                ],
                P_obj_path=f"machine.stator.axial_vent[{duct_id}].H0",
                unit_type="m",
                scaling_to_P=0.5,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"{lam_name_MC}RectangularDuctLayer_OffsetAngle[{duct_id}]",
                ],
                P_obj_path=f"machine.stator.axial_vent[{duct_id}].Alpha0",
                unit_type="m",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"{lam_name_MC}RectangularDuctLayer_ChannelDiameter[{duct_id}]",
                ],
                P_obj_path=f"machine.stator.axial_vent[{duct_id}].D0",
                unit_type="m",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"CircularDuctL{duct_id}Channels",
                ],
                P_obj_path=f"machine.stator.axial_vent[{duct_id}].Zh",
                unit_type="",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"{lam_name_MC}RectangularDuctLayer_Width[{duct_id}]",
                ],
                P_obj_path=f"machine.stator.axial_vent[{duct_id}].W1",
                unit_type="m",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"{lam_name_MC}RectangularDuctLayer_Width[{duct_id}]",
                ],
                P_obj_path=f"machine.stator.axial_vent[{duct_id}].W2",
                unit_type="m",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

    else:
        lam_name_MC = "Rotor"
        lam_name_py = "rotor"

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"{lam_name_MC}RectangularDuctlayers_RadialDiameter[{duct_id}]",
                ],
                P_obj_path=f"machine.{lam_name_py}.axial_vent[{duct_id}].H0",
                unit_type="m",
                scaling_to_P=0.5,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"{lam_name_MC}RectangularDuctLayer_OffsetAngle[{duct_id}]",
                ],
                P_obj_path=f"machine.{lam_name_py}.axial_vent[{duct_id}].Alpha0",
                unit_type="m",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"{lam_name_MC}RectangularDuctLayer_ChannelDiameter[{duct_id}]",
                ],
                P_obj_path=f"machine.{lam_name_py}.axial_vent[{duct_id}].D0",
                unit_type="m",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"{lam_name_MC}RectangularDuctLayer_Channels[{duct_id}]",
                ],
                P_obj_path=f"machine.{lam_name_py}.axial_vent[{duct_id}].Zh",
                unit_type="",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"{lam_name_MC}RectangularDuctLayer_Width[{duct_id}]",
                ],
                P_obj_path=f"machine.{lam_name_py}.axial_vent[{duct_id}].W1",
                unit_type="m",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"{lam_name_MC}RectangularDuctLayer_Width[{duct_id}]",
                ],
                P_obj_path=f"machine.{lam_name_py}.axial_vent[{duct_id}].W2",
                unit_type="m",
                scaling_to_P=1,
                file_name=__file__,
            )
        )
