from pyleecan.Classes.Notch import Notch
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.SlotM19 import SlotM19


def convert_notch_to_P(self, is_stator):
    """selection step to add rules for notch

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor
    """
    if is_stator == False:
        if "PoleNotchDepth" in self.other_dict["[Dimensions]"]:
            Notch_depth = self.other_dict["[Dimensions]"]["PoleNotchDepth"]
        else:
            Notch_depth = 0

        if Notch_depth != 0:
            # MC has one set of notch and just equivalent of slotM19
            self.machine.rotor.notch.append(Notch())
            self.machine.rotor.notch[0] = NotchEvenDist()
            self.machine.rotor.notch[0].notch_shape = SlotM19()
            self.add_rule_notch(is_stator)

            self.get_logger().info("Add notch for rotor")
            self.get_logger().warning("Approximation of notch for slotM19")
