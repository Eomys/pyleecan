from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_slotM13(self):
    """Create and adapt all the rules related to slotM13
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        A booleen to know, position in lamination
    """

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"Pole_Number"],
            P_obj_path=f"machine.rotor.slot.Zs",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Magnet_Thickness"],
            P_obj_path=f"machine.rotor.slot.H1",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleComplex(fct_name="surface_breadloaf_slotM13", folder="MotorCAD")
    )
