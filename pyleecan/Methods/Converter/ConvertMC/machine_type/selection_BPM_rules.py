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
from pyleecan.Methods.Converter.ConvertMC.Step.selection_magnet_rules import (
    selection_magnet_rules,
)

from pyleecan.Methods.Converter.ConvertMC.Step.selection_skew_rules import (
    selection_skew_rules,
)
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM


def selection_BPM_rules(self):
    # check the direction of conversion to define type machine
    if self.is_P_to_other:
        if "[Calc_Options]" not in self.other_dict:
            self.other_dict["[Calc_Options]"] = {}
        temp_dict = self.other_dict["[Calc_Options]"]

        temp_dict["Motor_Type"] = "BPM"

    else:
        self.machine = MachineSIPMSM()

    # step for stator
    is_stator = True
    selection_slot_rules(self, is_stator)
    selection_lamination_rules(self, is_stator)
    selection_winding_rules(self, is_stator)
    selection_conductor_rules(self, is_stator)

    # step for rotor
    is_stator = False
    selection_magnet_rules(self, is_stator)
    selection_lamination_rules(self, is_stator)
    selection_skew_rules(self, is_stator)
