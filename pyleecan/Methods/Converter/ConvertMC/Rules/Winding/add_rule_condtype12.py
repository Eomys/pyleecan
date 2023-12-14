from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_condtype12(self):
    """Create and adapt all the rules related to condtype12
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "NumberStrandsHand"],
            P_obj_path="machine.stator.winding.conductor.Nwppc",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Winding_Design]", "Copper_Diameter"],
            P_obj_path="machine.stator.winding.conductor.Wwire",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Winding_Design]", "EWdg_MLT"],
            P_obj_path="machine.stator.winding.Lewout",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleEquation(
            param=[
                {
                    "src": "other",
                    "path": ["[Winding_Design]", "Copper_Diameter"],
                    "variable": "y",
                },
                {
                    "src": "other",
                    "path": ["[Winding_Design]", "Wire_Diameter"],
                    "variable": "b",
                },
                {
                    "src": "pyleecan",
                    "path": f"machine.stator.winding.conductor.Wins_wire",
                    "variable": "x",
                },
            ],
            unit_type="m",
            equation="y/2 + b = x",
            file_name=__file__,
        )
    )
