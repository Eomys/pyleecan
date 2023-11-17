from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.Notch import Notch
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.SlotM19 import SlotM19


def selection_lamination_rules(self, is_stator):
    """selection step to add rules for lamination

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    # selection of number and type layers
    if not self.is_P_to_other:
        self.convert_duct_type_P(is_stator)
        self.convert_notch_type_P(is_stator)

    else:
        self.convert_duct_type_MC(is_stator)
        self.convert_notch_type_MC(is_stator)
