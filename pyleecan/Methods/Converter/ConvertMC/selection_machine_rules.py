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

from pyleecan.Methods.Converter.Convert.convert_machine_type import convert_machine_type


def selection_machine_rules(self):
    convert_machine_type(self)
    motor_type = type(self.machine).__name__
    # add rule present in all machine
    add_rule_machine_type(self)

    # selecion motor_type

    if motor_type == "MachineSIPMSM":
        add_rule_machine_dimension(self)
        # particularity for BPM with airgap, changemen rule machine dimension
        self.selection_BPM_rules()

    elif motor_type == "MachineIPMSM":
        add_rule_machine_dimension(self)
        selection_IM_rules(self)
