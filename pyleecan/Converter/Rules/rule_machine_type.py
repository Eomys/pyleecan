from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_machine_type(rules):
    rules.append(RuleComplex(src="MC", fct_name="machine_type"))

    rules.append(RuleComplex(src="MC", fct_name="set_pole_pair_number"))

    # ajout de la règke pour set le nom

    # ajout de la topology

    return rules
