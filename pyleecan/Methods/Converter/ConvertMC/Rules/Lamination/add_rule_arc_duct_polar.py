from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_arc_duct_polar(self, is_stator, duct_id):
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

    if is_stator == True:
        lam_name_MC = "Stator"
        lam_name_py = "stator"
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
                f"{lam_name_MC}ArcDuctLayer_CornerRadius[{duct_id}]",
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

    if self.is_P_to_other == False:
        self.rules_list.append(
            RuleEquation(
                param=[
                    {
                        "src": "other",
                        "path": [
                            "[Through_Vent]",
                            f"{lam_name_MC}ArcDuctLayer_InnerDiameter[{duct_id}]",
                        ],
                        "variable": "a",
                    },
                    {
                        "src": "other",
                        "path": [
                            "[Through_Vent]",
                            f"{lam_name_MC}ArcDuctLayer_WebWidth[{duct_id}]",
                        ],
                        "variable": "y",
                    },
                    {
                        "src": "pyleecan",
                        "path": f"machine.{lam_name_py}.axial_vent[{duct_id}].W1",
                        "variable": "x",
                    },
                ],
                unit_type="m",
                equation="cos(x)= 1 - (2*y*y / (a*a)) ",
                file_name=__file__,
            )
        )
