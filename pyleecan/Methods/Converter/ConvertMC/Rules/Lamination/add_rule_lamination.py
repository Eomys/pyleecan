from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_lamination(rule_list, is_stator):
    print("add_rule_lamination")

    if is_stator == True:
        lam_name = "stator"
    else:
        lam_name = "rotor"

    rule_list.append(RuleComplex(fct_name="add_duct_layer", src="pyleecan"))

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Slot_Opening"],
            pyleecan=f"machine.{lam_name}.slot.W0",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Tooth_Width"],
            pyleecan=f"machine.{lam_name}.slot.W3",
            unit_type="m",
            scaling_to_P=1,
        )
    )
