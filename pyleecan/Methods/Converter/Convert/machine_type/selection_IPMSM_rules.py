from pyleecan.Methods.Converter.Convert.Step.selection_lamination_rules import (
    selection_lamination_rules,
)
from pyleecan.Methods.Converter.Convert.Step.selection_slot_rotor_rules import (
    selection_slot_rotor_rules,
)
from pyleecan.Methods.Converter.Convert.Step.selection_bar_rules import (
    selection_bar_rules,
)
from pyleecan.Methods.Converter.Convert.Step.selection_skew_rules import (
    selection_skew_rules,
)
from pyleecan.Methods.Converter.Convert.selection_LamSlotWind_rules import (
    selection_LamSlotWind_rules,
)

from pyleecan.Classes.MachineIPMSM import MachineIPMSM


def selection_IPMSM_rules(self):
    """selection step to have rules for motor IPMSM

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object

    """
    # step for stator
    selection_LamSlotWind_rules(self)

    is_stator = False
    selection_slot_rotor_rules(self, is_stator)
    selection_bar_rules(self, is_stator)
    selection_lamination_rules(self, is_stator)
    selection_skew_rules(self, is_stator)
