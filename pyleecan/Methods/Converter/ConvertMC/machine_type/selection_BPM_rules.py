from pyleecan.Methods.Converter.ConvertMC.Step.selection_slot_rules import (
    selection_slot_rules,
)
from pyleecan.Methods.Converter.ConvertMC.Step.selection_slot_rotor_rules import (
    selection_slot_rotor_rules,
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
from pyleecan.Methods.Converter.ConvertMC.Step.selection_magnet_rules import (
    selection_magnet_rules,
)
from pyleecan.Methods.Converter.ConvertMC.Step.selection_skew_rules import (
    selection_skew_rules,
)
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM


def selection_BPM_rules(self):
    self.machine = MachineSIPMSM()
    is_stator = True
    self.rules = selection_slot_rules(self, is_stator)
    self.rules = selection_lamination_rules(self, is_stator)
    self.rules = selection_winding_rules(self, is_stator)
    self.rules = selection_conductor_rules(self, is_stator)
    self.is_stator = False
    self.rules = selection_slot_rotor_rules(self, is_stator)
    # self.rules = get_magnet(self, is_stator=False)
    self.rules = selection_lamination_rules(self, is_stator)
    self.rules = selection_skew_rules(self, is_stator)

    return self.rules
