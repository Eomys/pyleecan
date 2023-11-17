from pyleecan.Classes.SlotM19 import SlotM19


def convert_notch_type_MC(self, is_stator):
    if is_stator == False:
        len_nocth = len(self.machine.rotor.notch)

        if len_nocth > 1:
            self.get_logger().info("Motor-CAD have just the possibility to add 1 notch")
            self.get_logger().info("We try to add the first notch")

        if len_nocth > 0:
            if self.machine.rotor.notch[0].notch_shape == SlotM19():
                self.add_rule_notch(is_stator)
                self.get_logger().info("approximation of notch for slotM19")

            else:
                self.get_logger().info(
                    "just the slotM19 has the possibility to have a conversion"
                )

    else:
        self.get_logger().info("Motor-CAD have not possibility to add notch in stator")
