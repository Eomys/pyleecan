from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_form_wound_slotW29(rule_list, is_stator):
    """Create and adapt all the rules related to slotW29 (lam radius,...)
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        A booleen to know, position in lamination
    """

    if is_stator == True:
        lam_name = "stator"
    else:
        lam_name = "rotor"

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Slot_Width"],
            P_obj_path=f"machine.{lam_name}.slot.W0",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    rule_list.append(
        RuleEquation(
            param=[
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Wedge_Inset"],
                    "variable": "y",
                },
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Slot_Width"],
                    "variable": "a",
                },
                {
                    "src": "pyleecan",
                    "path": f"machine.{lam_name}.slot.W1",
                    "variable": "x",
                },
            ],
            unit_type="m",
            equation="y+a = x",
            file_name=__file__,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Slot_Width"],
            P_obj_path=f"machine.{lam_name}.slot.W2",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Wedge_Depth"],
            P_obj_path=f"machine.{lam_name}.slot.H0",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Wedge_Thickeness"],
            P_obj_path=f"machine.{lam_name}.slot.H1",
            unit_type="deg",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    rule_list.append(
        RuleEquation(
            param=[
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Slot_Depth"],
                    "variable": "y",
                },
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Wedge_Thickness"],
                    "variable": "a",
                },
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Wedge_Depth"],
                    "variable": "b",
                },
                {
                    "src": "pyleecan",
                    "path": f"machine.{lam_name}.slot.H2",
                    "variable": "x",
                },
            ],
            unit_type="m",
            equation="y+b+a = x",
            file_name=__file__,
        )
    )

    return rule_list
