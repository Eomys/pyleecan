from ......Classes.RuleSimple import RuleSimple


def add_rule_lamination(self, is_stator):
    """Create and adapt all the rules related to lamination (lam radius,...)
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        A booleen to know, position in lamination
    """

    # definie the correct position in rotor or in stator
    if is_stator:
        lam_name = "stator"
        lam_name_MC = "Stator"
    else:
        lam_name = "rotor"
        lam_name_MC = "Rotor"

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"{lam_name_MC}_Lam_Length"],
            P_obj_path=f"machine.{lam_name}.L1",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Miscellaneous]", f"Stacking_Factor_[{lam_name_MC}]"],
            P_obj_path=f"machine.{lam_name}.Kf1",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )
