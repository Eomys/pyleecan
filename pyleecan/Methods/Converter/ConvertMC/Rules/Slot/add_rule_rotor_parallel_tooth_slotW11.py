from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_rotor_parallel_tooth_slotW11(rule_list):
    """Create and adapt all the rules related to slotW11 (lam radius,...)
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        A booleen to know, position in lamination
    """
    print("rotor_parallel_tooth_slotW11")

    rule_list.append(RuleComplex(fct_name="rotor_slotW11", folder="MotorCAD"))

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Bar_Opening_[T]"],
            P_obj_path=f"machine.rotor.slot.W0",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Rotor_Tooth_Width"],
            P_obj_path=f"machine.rotor.slot.W3",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Bar_Opening_Depth_[T]"],
            P_obj_path=f"machine.rotor.slot.H0",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Bar_Corner_Radius[T]"],
            P_obj_path=f"machine.rotor.slot.R1",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    rule_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Bar_Tip_Angle_[T]"],
            P_obj_path=f"machine.rotor.slot.H1",
            unit_type="rad",
            scaling_to_P=1,
        )
    )

    rule_list.append(RuleComplex(fct_name="rotor_slotW11_H1", folder="MotorCAD"))

    rule_list.append(
        RuleEquation(
            param=[
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Bar_Depth_[T]"],
                    "variable": "y",
                },
                {
                    "src": "pyleecan",
                    "path": f"machine.rotor.slot.H2",
                    "variable": "x",
                },
                {
                    "src": "pyleecan",
                    "path": f"machine.rotor.slot.H1",
                    "variable": "a",
                },
            ],
            unit_type="m",
            scaling_to_P="y = a+x",
        )
    )

    return rule_list
