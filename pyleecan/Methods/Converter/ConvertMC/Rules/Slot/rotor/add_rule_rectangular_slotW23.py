from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_rectangular_slotW23(self, is_stator):
    """Create and adapt all the rules related to slotW23
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        A booleen to know, position in lamination
    """
    if is_stator == True:
        raise KeyError("this rule is for slot in rotor")

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
            other_key_list=["[Dimensions]", "Bar_Tip_Angle_[T]"],
            P_obj_path=f"machine.rotor.slot.H1",
            unit_type="deg",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Bar_Depth_[T]"],
            P_obj_path=f"machine.rotor.slot.H2",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Bar_Width_[T]"],
            P_obj_path=f"machine.rotor.slot.W1",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Bar_Width_[T]"],
            P_obj_path=f"machine.rotor.slot.W2",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )
