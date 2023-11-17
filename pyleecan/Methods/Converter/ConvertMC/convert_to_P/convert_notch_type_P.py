from pyleecan.Classes.Notch import Notch
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.SlotM19 import SlotM19


def convert_notch_type_P(self, is_stator):
    if is_stator == False:
        try:
            Notch_depth = self.other_dict["[Dimensions]"]["PoleNotchDepth"]
        except:
            Notch_depth = 0

        if Notch_depth != 0:
            self.machine.rotor.notch.append(Notch())
            self.machine.rotor.notch[0] = NotchEvenDist()
            self.machine.rotor.notch[0].notch_shape = SlotM19()
            self.add_rule_notch(is_stator)

            self.get_logger().info("add notch for rotor")
            self.get_logger().info("approximation of notch for slotM19")

    else:
        self.get_logger().info("Motor-CAD have not possibility to add notch in stator")
