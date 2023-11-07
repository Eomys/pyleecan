from pyleecan.Methods.Converter.ConvertMC.Step.selection_slot_rules import (
    selection_slot_rules,
)
from pyleecan.Methods.Converter.ConvertMC.Step.selection_lamination_rules import (
    selection_lamination_rules,
)
from pyleecan.Methods.Converter.ConvertMC.Step.selection_winding_rules import (
    selection_winding_rules,
)
from pyleecan.Methods.Converter.ConvertMC.Step.selection_conductor_rules import (
    selection_conductor_rules,
)
from pyleecan.Methods.Converter.ConvertMC.Step.selection_slot_rotor_rules import (
    selection_slot_rotor_rules,
)
from pyleecan.Methods.Converter.ConvertMC.Step.selection_bar_rules import (
    selection_bar_rules,
)
from pyleecan.Methods.Converter.ConvertMC.Step.selection_skew_rules import (
    selection_skew_rules,
)

from pyleecan.Classes.MachineIPMSM import MachineIPMSM


def selection_IM_rules(self):
    self.machine = MachineIPMSM()
    is_stator = True
    selection_slot_rules(self, is_stator)
    selection_lamination_rules(self, is_stator)
    selection_winding_rules(self, is_stator)
    selection_conductor_rules(self, is_stator)
    is_stator = False
    selection_slot_rotor_rules(self, is_stator)
    selection_bar_rules(self, is_stator)
    selection_lamination_rules(self, is_stator)
    selection_skew_rules(self, is_stator)
