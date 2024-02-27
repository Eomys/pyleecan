from ......Classes.RuleSimple import RuleSimple
from ......Classes.RuleEquation import RuleEquation
from ......Classes.RuleComplex import RuleComplex


def add_rule_condtype12(self, is_stator):
    """Create and adapt all the rules related to condtype12
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        True slot is in stator, False slot is in rotor
    """
    # definie the correct position in rotor or in stator
    if is_stator:
        lam_name = "stator"
    else:
        lam_name = "rotor"

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Magnetics]", "NumberStrandsHand"],
            P_obj_path=f"machine.{lam_name}.winding.conductor.Nwppc",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Winding_Design]", "Copper_Diameter"],
            P_obj_path=f"machine.{lam_name}.winding.conductor.Wwire",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    # Not implemented
    """
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
                    "path": f"machine.{lam_name}.winding.conductor.Wins_wire",
                    "variable": "x",
                },
            ],
            unit_type="m",
            equation="y/2 + b/2 = x",
            file_name=__file__,
        )
    )
    """
    self.rules_list.append(
        RuleComplex(fct_name="end_winding_lenght", folder="MotorCAD")
    )
