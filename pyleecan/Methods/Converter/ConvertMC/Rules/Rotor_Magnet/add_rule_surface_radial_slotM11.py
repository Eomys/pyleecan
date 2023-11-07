from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_surface_radial_slotM11(self, is_stator):
    print("surface_radial_slotM11")
    rule_list = self.rules_list
    rule_list.append(RuleComplex(fct_name="surface_radial_slotM11", src="pyleecan"))

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Magnet_Arc_[ED]"],
            P_obj_path=f"machine.rotor.slot.W0",
            unit_type="ED",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Magnet_Arc_[ED]"],
            P_obj_path=f"machine.rotor.slot.W1",
            unit_type="ED",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Magnet_Thickness"],
            P_obj_path=f"machine.rotor.slot.H1",
            unit_type="m",
            scaling_to_P=1,
        )
    )
