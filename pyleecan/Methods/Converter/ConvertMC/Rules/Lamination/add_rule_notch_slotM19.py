from ......Classes.RuleSimple import RuleSimple
from ......Classes.RuleEquation import RuleEquation
from ......Classes.RuleComplex import RuleComplex


def add_rule_notch_slotM19(self, is_stator, nb_notch):
    """Create and adapt all the rules related to lamination (lam radius,...)
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        A booleen to know, position in lamination
    nb_notch : int
        number oh notch
    """
    self.rules_list.append(
        RuleSimple(
            other_key_list=[
                "[Dimensions]",
                "PoleNotchDepth",
            ],
            P_obj_path=f"machine.rotor.notch[0].notch_shape.H0",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=[
                "[Dimensions]",
                "Pole_Number",
            ],
            P_obj_path=f"machine.rotor.notch[0].notch_shape.Zs",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(RuleComplex(fct_name="add_notch_slotM19", folder="MotorCAD"))
