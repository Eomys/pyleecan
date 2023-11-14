from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_circular_duct_circular(self, is_stator, duct_id):
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
        lam_name = "Stator"
    else:
        lam_name = "Rotor"

    self.rules_list.append(
        RuleSimple(
            other_key_list=[
                "[Dimensions]",
                f"{lam_name}CircularDuctlayers_RadialDiameter[{duct_id}]",
            ],
            P_obj_path=f"machine.{lam_name}.axial_vent[{duct_id}].H0",
            unit_type="m",
            scaling_to_P=0.5,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=[
                "[Dimensions]",
                f"{lam_name}CircularDuctLayer_OffsetAngle[{duct_id}]",
            ],
            P_obj_path=f"machine.{lam_name}.axial_vent[{duct_id}].Alpha0",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=[
                "[Dimensions]",
                f"{lam_name}CircularDuctLayer_ChannelDiameter[{duct_id}]",
            ],
            P_obj_path=f"machine.{lam_name}.axial_vent[{duct_id}].D0",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=[
                "[Dimensions]",
                f"{lam_name}CircularDuctLayer_Channels[{duct_id}]",
            ],
            P_obj_path=f"machine.{lam_name}.axial_vent[{duct_id}].Zh",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )
