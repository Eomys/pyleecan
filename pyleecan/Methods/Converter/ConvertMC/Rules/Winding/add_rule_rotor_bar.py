from ......Classes.RuleSimple import RuleSimple
from ......Classes.RuleEquation import RuleEquation
from ......Classes.RuleComplex import RuleComplex


def add_rule_rotor_bar(self, is_stator):
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
        raise KeyError("Those rules are for rotor slot only")

    self.rules_list.append(RuleComplex(fct_name="rotor_bar", folder="MotorCAD"))
