from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_surface_radial_slotM11(rule_list, is_stator):
    print("surface_radial_slotM11")

    rule_list.append(RuleComplex(fct_name="surface_radial_slotM11", src="pyleecan"))

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Magnet_Arc_[ED]"],
            pyleecan=f"machine.rotor.slot.W0",
            unit_type="ED",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Magnet_Arc_[ED]"],
            pyleecan=f"machine.rotor.slot.W1",
            unit_type="ED",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Magnet_Thikness"],
            pyleecan=f"machine.Magnet_Arc_[ED].slot.H1",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    return rule_list
