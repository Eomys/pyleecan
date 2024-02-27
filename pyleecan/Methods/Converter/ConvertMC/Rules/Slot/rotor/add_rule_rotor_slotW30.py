from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_rotor_slotW30(self, is_stator):
    """Create and adapt all the rules related to slotW23 (lam radius,...)
    Extend rules_list within Converter object
    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        A booleen to know, position in lamination
    """
    if is_stator:
        raise KeyError("Those rules are for rotor slot only")

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Rotor_Bars"],
            P_obj_path=f"machine.rotor.slot.Zs",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )
    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Bar_Opening_[T]"],
            P_obj_path=f"machine.rotor.slot.W0",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )
    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Bar_Opening_Depth_[T]"],
            P_obj_path=f"machine.rotor.slot.H0",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Rotor_Tooth_Width_T"],
            P_obj_path=f"machine.rotor.slot.W3",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )
    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Bar_Depth_[T]"],
            P_obj_path=f"machine.rotor.slot.H1",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "BarT_Opening_Radius"],
            P_obj_path=f"machine.rotor.slot.R1",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "BarT_Opening_Radius"],
            P_obj_path=f"machine.rotor.slot.R2",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )
