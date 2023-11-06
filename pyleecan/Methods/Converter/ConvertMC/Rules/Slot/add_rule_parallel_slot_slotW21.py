from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_parallel_slot_slotW21(rule_list, is_stator):
    if is_stator == True:
        lam_name = "stator"
    else:
        lam_name = "rotor"

    rule_list.append(RuleComplex(fct_name="parallel_slot_slotW21", src="pyleecan"))

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Slot_Opening"],
            P_obj_path=f"machine.{lam_name}.slot.W0",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Tooth_Width"],
            P_obj_path=f"machine.{lam_name}.slot.W1",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Tooth_Width"],
            P_obj_path=f"machine.{lam_name}.slot.W2",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Tooth_Tip_Depth"],
            P_obj_path=f"machine.{lam_name}.slot.H0",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Tooth_Tip_Angle"],
            P_obj_path=f"machine.{lam_name}.slot.H1",
            unit_type="rad",
            scaling_to_P=1,
        )
    )

    rule_list.append(RuleComplex(fct_name="slotW21_H1", src="pyleecan"))

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
            scaling_to_P="y = b+a+x",
        )
    )

    return rule_list