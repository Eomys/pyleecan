from pyleecan.Methods.Converter.ConvertMC.Step.selection_slot_rules import get_slot
from pyleecan.Methods.Converter.ConvertMC.Step.selection_slot_rotor_rules import (
    get_slot_rotor,
)
from pyleecan.Methods.Converter.ConvertMC.Step.selection_lamination_rules import (
    get_lamination,
)
from pyleecan.Methods.Converter.ConvertMC.Step.selection_winding_rules import (
    get_winding,
)
from pyleecan.Methods.Converter.ConvertMC.Step.selection_conductor_rules import (
    get_conductor,
)
from pyleecan.Methods.Converter.ConvertMC.Step.selection_magnet_rules import get_magnet
from pyleecan.Methods.Converter.ConvertMC.Step.selection_skew_rules import get_skew
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM


def selection_BPM_rules(self):
    self.machine = MachineSIPMSM()
    self.is_stator = True
    self.rules = get_slot(self)
    self.rules = get_lamination(self)
    self.rules = get_winding(self)
    self.rules = get_conductor(self)
    self.is_stator = False
    self.rules = get_slot_rotor(self)
    # self.rules = get_magnet(self, is_stator=False)
    self.rules = get_lamination(self)
    self.rules = get_skew(self)

    return self.rules
