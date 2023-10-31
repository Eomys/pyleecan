from pyleecan.Classes.MachineIPMSM import MachineIPMSM


def rule_convert(rule_list, other_dict, unit_list, machine):
    for rule in rule_list:
        rule.convert_to_P(other_dict, unit_list, machine)

    return machine
