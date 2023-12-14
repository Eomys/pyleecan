from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_condtype11(self):
    """Create and adapt all the rules related to condtype11
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    """
    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "NumberStrandsHand"],
            P_obj_path="machine.stator.winding.conductor.Nwppc_rad",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "NumberStrandsHand"],
            P_obj_path="machine.stator.winding.conductor.Nwppc_tan",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )"""

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "Copper_Height"],
            P_obj_path="machine.stator.winding.conductor.Wwire",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "Copper_Width"],
            P_obj_path="machine.stator.winding.conductor.Hwire",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "EWdg_MLT"],
            P_obj_path="machine.stator.winding.Lewout",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "WireInsThicknessCalculation"],
            P_obj_path="machine.stator.winding.conductor.Wins_wire",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )
