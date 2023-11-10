from pyleecan.Methods.Converter.Convert.Step.selection_slot_rules import (
    selection_slot_rules,
)
from pyleecan.Methods.Converter.Convert.Step.selection_lamination_rules import (
    selection_lamination_rules,
)
from pyleecan.Methods.Converter.Convert.Step.selection_winding_rules import (
    selection_winding_rules,
)
from pyleecan.Methods.Converter.Convert.Step.selection_conductor_rules import (
    selection_conductor_rules,
)
from pyleecan.Methods.Converter.Convert.Step.selection_magnet_rules import (
    selection_magnet_rules,
)

from pyleecan.Methods.Converter.Convert.Step.selection_skew_rules import (
    selection_skew_rules,
)
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Methods.Converter.Convert.selection_LamSlotWind_rules import (
    selection_LamSlotWind_rules,
)


def selection_SIPMSM_rules(self):
    """selection step to have rules for motor SIPMSM

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    # step for stator
    self.selection_LamSlotWind_rules(is_stator=True)

    # step for rotor
    is_stator = False
    self.selection_magnet_rules(is_stator)
    self.selection_lamination_rules(is_stator)
    self.selection_skew_rules(is_stator)
