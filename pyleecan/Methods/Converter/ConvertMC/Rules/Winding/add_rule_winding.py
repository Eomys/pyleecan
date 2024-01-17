from ......Classes.RuleSimple import RuleSimple
from ......Classes.RuleEquation import RuleEquation
from ......Classes.RuleComplex import RuleComplex


def add_rule_winding(self, is_stator):
    """Create and adapt all the rules related to winding
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

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "MagPhases"],
            P_obj_path=f"machine.{lam_name}.winding.qs",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "MagTurnsConductor"],
            P_obj_path=f"machine.{lam_name}.winding.Ntcoil",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "MagThrow"],
            P_obj_path=f"machine.{lam_name}.winding.coil_pitch",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "ParallelPaths"],
            P_obj_path=f"machine.{lam_name}.winding.Npcp",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleComplex(
            fct_name="winding_layer",
            folder="MotorCAD",
            param_dict={is_stator: lam_name},
        )
    )
