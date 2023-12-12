from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_winding(self):
    """Create and adapt all the rules related to winding
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "MagPhases"],
            P_obj_path="machine.stator.winding.qs",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "MagTurnsConductor"],
            P_obj_path="machine.stator.winding.Ntcoil",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "MagThrow"],
            P_obj_path="machine.stator.winding.coil_pitch",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "ParallelPaths"],
            P_obj_path="machine.stator.winding.Npcp",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(RuleComplex(fct_name="winding_layer", folder="MotorCAD"))
