from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_tapered_slot_slotW23(self, is_stator):
    """Create and adapt all the rules related to slotW23 (lam radius,...)
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        A booleen to know, position in lamination
    """
    rule_list = self.rules_list

    if is_stator == True:
        lam_name = "stator"
    else:
        lam_name = "rotor"

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Slot_Number"],
            P_obj_path=f"machine.{lam_name}.slot.Zs",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Slot_Opening"],
            P_obj_path=f"machine.{lam_name}.slot.W0",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Slot_Width_Top"],
            P_obj_path=f"machine.{lam_name}.slot.W1",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Slot_Width_Bottom"],
            P_obj_path=f"machine.{lam_name}.slot.W2",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Tooth_Tip_Depth"],
            P_obj_path=f"machine.{lam_name}.slot.H0",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Slot_Depth"],
            P_obj_path=f"machine.{lam_name}.slot.H2",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Tooth_Tip_Angle"],
            P_obj_path=f"machine.{lam_name}.slot.H1",
            unit_type="deg",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    # rule_list.append(RuleComplex(fct_name="slotW23_H1", folder="MotorCAD"))

    """
    rule_list.append(
        RuleEquation(
            param=[
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Slot_Depth"],
                    "variable": "y",
                },
                {
                    "src": "pyleecan",
                    "path": f"machine.{lam_name}.slot.H2",
                    "variable": "x",
                },
                {
                    "src": "pyleecan",
                    "path": f"machine.{lam_name}.slot.H1",
                    "variable": "a",
                },
                {
                    "src": "pyleecan",
                    "path": f"machine.{lam_name}.slot.H0",
                    "variable": "b",
                },
            ],
            unit_type="m",
            equation="y = b+a+x",
            file_name=__file__,
        )
    )"""

    return rule_list
