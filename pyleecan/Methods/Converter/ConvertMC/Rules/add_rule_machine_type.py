from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_machine_type(self):
    rules_list = self.rules_list
    # inutile pour le moment
    rules_list.append(RuleComplex(fct_name="machine_type", src="MC"))

    rules_list.append(RuleComplex(fct_name="set_pole_pair_number", src="pyleecan"))

    # ajout de la règle pour set le nom

    # ajout de la topology
