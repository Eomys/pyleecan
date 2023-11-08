from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_parallel_tooth_slotW11(self, is_stator):
    """Create and adapt all the rules related to slotW11 (lam radius,...)
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        A booleen to know, position in lamination
    """
    # definie the correct position in rotor or in stator
    if is_stator == True:
        lam_name = "stator"
    else:
        lam_name = "rotor"

    rules_list = self.rules_list

    rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Slot_Number"],
            P_obj_path=f"machine.{lam_name}.slot.Zs",
            unit_type="",
            scaling_to_P=1,
        )
    )

    rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Slot_Opening"],
            P_obj_path=f"machine.{lam_name}.slot.W0",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Tooth_Width"],
            P_obj_path=f"machine.{lam_name}.slot.W3",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Tooth_Tip_Depth"],
            P_obj_path=f"machine.{lam_name}.slot.H0",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Slot_Corner_Radius"],
            P_obj_path=f"machine.{lam_name}.slot.R1",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    if not self.is_P_to_other:
        rules_list.append(
            RuleSimple(
                other_key_list=["[Dimensions]", "Tooth_Tip_Angle"],
                P_obj_path=f"machine.{lam_name}.slot.H1",
                unit_type="rad",
                scaling_to_P=1,
            )
        )

        rules_list.append(RuleComplex(fct_name="slotW11_H1", folder="MotorCAD"))

        rules_list.append(
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

    else:
        print("error type conversion to tooth_tip_depth_H1 is not in rad ")
