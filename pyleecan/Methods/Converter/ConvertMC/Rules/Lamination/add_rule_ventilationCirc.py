from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation


def add_rule_ventilationCirc(self, is_stator, duct_id):
    """Create and adapt all the rules related to lamination (lam radius,...)
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
    duct_id_mc = duct_id + 1
    if is_stator:
        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"CircularDuctL{duct_id_mc}Channels",
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
                    f"iCircularDuctL{duct_id_mc}RadialDiameter",
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
                    f"CircularDuctL{duct_id_mc}OffsetAngle",
                ],
                P_obj_path=f"machine.stator.axial_vent[{duct_id}].Alpha0",
                unit_type="deg",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"CircularDuctL{duct_id_mc}ChannelDiameter",
                ],
                P_obj_path=f"machine.stator.axial_vent[{duct_id}].D0",
                unit_type="m",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        if not self.is_P_to_other:
            self.rules_list.append(
                RuleEquation(
                    param=[
                        {
                            "src": "other",
                            "path": [
                                "[Dimensions]",
                                "Pole_Number",
                            ],
                            "variable": "a",
                        },
                        {
                            "src": "pyleecan",
                            "path": f"machine.stator.axial_vent[{duct_id}].Alpha0",
                            "variable": "b",
                        },
                        {
                            "src": "pyleecan",
                            "path": f"machine.stator.axial_vent[{duct_id}].Alpha0",
                            "variable": "x",
                        },
                    ],
                    unit_type="",
                    equation="(pi/a= x+b)",
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
                    f"{lam_name_MC}CircularDuctLayer_Channels[{duct_id}]",
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
                    f"{lam_name_MC}CircularDuctLayer_RadialDiameter[{duct_id}]",
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
                    f"{lam_name_MC}CircularDuctLayer_OffsetAngle[{duct_id}]",
                ],
                P_obj_path=f"machine.{lam_name_py}.axial_vent[{duct_id}].Alpha0",
                unit_type="deg",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[
                    "[Through_Vent]",
                    f"{lam_name_MC}CircularDuctLayer_ChannelDiameter[{duct_id}]",
                ],
                P_obj_path=f"machine.{lam_name_py}.axial_vent[{duct_id}].D0",
                unit_type="m",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        if not self.is_P_to_other:
            self.rules_list.append(
                RuleEquation(
                    param=[
                        {
                            "src": "other",
                            "path": [
                                "[Dimensions]",
                                "Pole_Number",
                            ],
                            "variable": "a",
                        },
                        {
                            "src": "pyleecan",
                            "path": f"machine.{lam_name_py}.axial_vent[{duct_id}].Alpha0",
                            "variable": "b",
                        },
                        {
                            "src": "pyleecan",
                            "path": f"machine.{lam_name_py}.axial_vent[{duct_id}].Alpha0",
                            "variable": "x",
                        },
                    ],
                    unit_type="",
                    equation="(pi/a= x+b)",
                    file_name=__file__,
                )
            )
