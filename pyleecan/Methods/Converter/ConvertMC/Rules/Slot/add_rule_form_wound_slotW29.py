from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_form_wound_slotW29(rule_list, is_stator):
    print("form_wound_slotW29")

    if is_stator == True:
        lam_name = "stator"
    else:
        lam_name = "rotor"

    rule_list.append(RuleComplex(fct_name="form_wound_slotW29", src="pyleecan"))

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Slot_Width"],
            pyleecan=f"machine.{lam_name}.slot.W0",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleEquation(
            param_other=[
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
            ],
            param_pyleecan=[
                {
                    "src": "pyleecan",
                    "path": f"machine.{lam_name}.slot.W1",
                    "variable": "x",
                },
            ],
            unit_type="m",
            scaling_to_P="y+a = x",
        )
    )

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Slot_Width"],
            pyleecan=f"machine.{lam_name}.slot.W2",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Wedge_Depth"],
            pyleecan=f"machine.{lam_name}.slot.H0",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Wedge_Thickeness"],
            pyleecan=f"machine.{lam_name}.slot.H1",
            unit_type="rad",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleEquation(
            param_other=[
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
            ],
            param_pyleecan=[
                {
                    "src": "pyleecan",
                    "path": f"machine.{lam_name}.slot.H2",
                    "variable": "x",
                }
            ],
            unit_type="m",
            scaling_to_P="y+b+a = x",
        )
    )

    return rule_list
