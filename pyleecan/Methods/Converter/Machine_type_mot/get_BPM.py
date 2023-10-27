from pyleecan.Methods.Converter.Rules_selections.get_slot import get_slot
from pyleecan.Methods.Converter.Rules_selections.get_lamination import get_lamination
from pyleecan.Methods.Converter.Rules_selections.get_winding import get_winding
from pyleecan.Methods.Converter.Rules_selections.get_conductor import get_conductor
from pyleecan.Methods.Converter.Rules_selections.get_magnet import get_magnet
from pyleecan.Methods.Converter.Rules_selections.get_skew import get_skew


def get_BPM(self):
    self.rules = get_slot(self, is_stator=True)
    self.rules = get_lamination(self, is_stator=True)
    self.rules = get_winding(self, is_stator=True)
    self.rules = get_conductor(self, is_stator=True)
    self.rules = get_magnet(self, is_stator=False)
    self.rules = get_lamination(self, is_stator=False)
    self.rules = get_skew(self, is_stator=False)

    return self.rules
