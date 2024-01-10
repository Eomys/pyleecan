from ......Classes.RuleSimple import RuleSimple
from ......Classes.RuleComplex import RuleComplex


def add_rule_ventilationPolar(self, is_stator, duct_id):
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

    if is_stator:
        self.get_logger().info("stator_duct, not implemented")
        return
    else:
        lam_name_MC = "Rotor"
        lam_name_py = "rotor"

    self.rules_list.append(
        RuleSimple(
            other_key_list=[
                "[Through_Vent]",
                f"{lam_name_MC}ArcDuctLayer_InnerDiameter[{duct_id}]",
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
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=[
                "[Through_Vent]",
                f"{lam_name_MC}ArcDuctLayer_Depth[{duct_id}]",
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
                f"{lam_name_MC}CircularDuctLayer_Channels[{duct_id}]",
            ],
            P_obj_path=f"machine.{lam_name_py}.axial_vent[{duct_id}].Zh",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleComplex(
            fct_name="arc_duct_polar",
            folder="MotorCAD",
            param_dict={
                "duct_id": duct_id,
                "lam_name_py": lam_name_py,
                "lam_name_MC": lam_name_MC,
            },
        )
    )
