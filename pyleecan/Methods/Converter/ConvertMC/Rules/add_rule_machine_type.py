from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_machine_type(self):
    """Create and adapt all the rules related to machine type
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    self.rules_list.append(
        RuleComplex(fct_name="set_pole_pair_number", folder="MotorCAD")
    )
