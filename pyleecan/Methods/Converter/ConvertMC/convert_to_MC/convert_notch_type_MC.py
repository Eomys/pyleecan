def convert_notch_type_MC(self, is_stator):
    """selection step to add rules for notch

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor
    """

    if is_stator == False:
        len_nocth = len(self.machine.rotor.notch)

        if len_nocth > 1:
            self.get_logger().info("Motor-CAD have just the possibility to add 1 notch")
            self.get_logger().info("We try to add the first notch")

        if len_nocth > 0:
            if type(self.machine.rotor.notch[0].notch_shape).__name__ == "SlotM19":
                self.add_rule_notch(is_stator)
                self.get_logger().warning("Approximation of notch for slotM19")

            else:
                self.get_logger().error(
                    "just the slotM19 has the possibility to have a conversion"
                )

    else:
        if len(self.machine.stator.notch) > 0:
            self.get_logger().error(
                "Motor-CAD have not possibility to add notch in stator"
            )
