from .....Classes.NotchEvenDist import NotchEvenDist
from .....Classes.SlotM19 import SlotM19


def convert_notch_to_P(self, is_stator):
    """selects step to add rules for notch

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor
    """
    if not is_stator:
        # In .mot file :
        #   If the machine have notch => PoleNotchDepth > 1
        #   If the machine have any notch => PoleNotchDepth do not exist
        #                                    OR PoleNotchDepth = 0
        if "PoleNotchDepth" in self.other_dict["[Dimensions]"]:
            Notch_depth = self.other_dict["[Dimensions]"]["PoleNotchDepth"]
        else:
            Notch_depth = 0

        if Notch_depth != 0:
            # MC has one set of notch and just equivalent of slotM19
            self.machine.rotor.notch.append(NotchEvenDist())
            self.machine.rotor.notch[0].notch_shape = SlotM19()

            self.get_logger().info("Add notch for rotor")
            self.get_logger().warning(
                "Approximation: top of slot is flat in Pyleecan contrary to MC top is rounded"
            )
    else:
        self.get_logger().error("MC machine can't have notch in stator")
