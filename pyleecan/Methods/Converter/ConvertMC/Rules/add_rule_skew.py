from .....Classes.RuleComplex import RuleComplex


def add_rule_skew(self):
    """Create and adapt all the rules related to skew
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    self.rules_list.append(
        RuleComplex(
            fct_name="skew",
            folder="MotorCAD",
        )
    )
