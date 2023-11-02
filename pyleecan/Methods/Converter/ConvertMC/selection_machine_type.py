from pyleecan.Methods.Converter.ConvertMC.convert_mot_to_dict import convert_mot_dict
from pyleecan.Methods.Converter.ConvertMC.Rules.add_rule_machine_type import (
    add_rule_machine_type,
)
from pyleecan.Methods.Converter.ConvertMC.Rules.add_rule_machine_dimension import (
    add_rule_machine_dimension,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_BPM_rules import (
    selection_BPM_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_IM_rules import (
    selection_IM_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_SRM_rules import (
    selection_SRM_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_BPMO_rules import (
    selection_BPMO_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_PMDC_rules import (
    selection_PMDC_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_BPMO_rules import (
    selection_BPMO_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_SYNC_rules import (
    selection_SYNC_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_CLAW_rules import (
    selection_CLAW_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_IM1PH_rules import (
    selection_IM1PH_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_WFC_rules import (
    selection_WFC_rules,
)


def selection_machine_type(self):
    motor_type = self.other_dict["[Calc_Options]"]["Motor_Type"]

    # self.rules_list = self.add_rules(self.mot_dict, self.rules_list)

    self.rules_list = add_rule_machine_type(self.rules_list)
    # selecion motor_type
    if motor_type == "BPM":
        self.rules_list = add_rule_machine_dimension(self.rules_list)
        selection_BPM_rules(self)

    elif motor_type == "IM":
        self.rules_list = add_rule_machine_dimension(self.rules_list)
        selection_IM_rules(self)

    elif motor_type == "SRM":
        selection_SRM_rules(self)

    elif motor_type == "BPMO":
        selection_BPMO_rules(self)

    elif motor_type == "PMDC":
        selection_PMDC_rules(self)

    elif motor_type == "SYNC":
        selection_SYNC_rules(self)

    elif motor_type == "CLAW":
        selection_CLAW_rules(self)

    elif motor_type == "IM1PH":
        selection_IM1PH_rules(self)

    elif motor_type == "WFC":
        selection_WFC_rules(self)

    # machine = rule_convert(self.rules_list, other_dict, None, self.machine)
    return self.machine
