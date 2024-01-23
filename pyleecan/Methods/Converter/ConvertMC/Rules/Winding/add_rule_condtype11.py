from ......Classes.RuleSimple import RuleSimple
from ......Classes.RuleEquation import RuleEquation
from ......Classes.RuleComplex import RuleComplex


def add_rule_condtype11(self, is_stator):
    """Create and adapt all the rules related to condtype11
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        True slot is in stator, False slot is in rotor
    """
    # definie the correct position in rotor or in stator
    if is_stator == True:
        lam_name = "stator"
    else:
        lam_name = "rotor"

    # conversion problem, possibility of having these rules
    """
    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "NumberStrandsHand"],
            P_obj_path=f"machine.{lam_name}.winding.conductor.Nwppc_rad",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "NumberStrandsHand"],
            P_obj_path=f"machine.{lam_name}.winding.conductor.Nwppc_tan",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )"""

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Winding_Design]", "Copper_Height"],
            P_obj_path=f"machine.{lam_name}.winding.conductor.Wwire",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Winding_Design]", "Copper_Width"],
            P_obj_path=f"machine.{lam_name}.winding.conductor.Hwire",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    # not implemented
    """
    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Calc_Options]", "WireInsThicknessCalculation"],
            P_obj_path=f"machine.{lam_name}.winding.conductor.Wins_wire",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )"""

    self.rules_list.append(
        RuleComplex(fct_name="end_winding_lenght", folder="MotorCAD")
    )
