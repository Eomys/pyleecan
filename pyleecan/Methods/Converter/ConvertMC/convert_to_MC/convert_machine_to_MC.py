def convert_machine_to_MC(self):  # conversion to MotorCAD
    """Update other_dict with the correct machine type

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # check the direction of conversion
    motor_type = type(self.machine).__name__

    # selection type of machine
    if motor_type == "MachineSIPMSM":
        name_machine = "BPM"

    elif motor_type == "MachineIPMSM":
        name_machine = "BPM"

    elif motor_type == "MachineSCIM":
        name_machine = "IM"

    else:
        raise NotImplementedError(
            f"Machine {motor_type} has not equivalent or has not implement"
        )

    self.get_logger().info(f"Conversion {motor_type} into {name_machine}")

    # writting in dict
    if "[Calc_Options]" not in self.other_dict:
        self.other_dict["[Calc_Options]"] = {"Motor_Type": name_machine}
    else:
        self.other_dict["[Calc_Options]"]["Motor_Type"] = name_machine
