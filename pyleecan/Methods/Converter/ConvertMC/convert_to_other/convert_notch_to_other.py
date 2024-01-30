from .....Classes.SlotM19 import SlotM19


def convert_notch_to_other(self, is_stator):
    """selection step to add rules for notch

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor
    """

    if is_stator:
        len_nocth = len(self.machine.stator.notch)
    else:
        len_nocth = len(self.machine.rotor.notch)

    # If there is any notch, then do nothing
    if len_nocth == 0:
        return

    if not is_stator:
        # A MC machine has the possibility to have a single notch set
        if len_nocth > 1:
            self.get_logger().info("A Motor-cad machine can only have one notch set")
            self.get_logger().info("Only the first notch set will be added")

        if isinstance(self.machine.rotor.notch[0].notch_shape, SlotM19):
            self.add_rule_notch(is_stator)
            self.get_logger().warning(
                "Approximation: top of slot is flat in Pyleecan contrary to MC top is rounded"
            )

        else:
            self.get_logger().error("Only the slotM19 can be converted")

    else:
        self.get_logger().error("Motor-CAD machine can't have stator notch")
