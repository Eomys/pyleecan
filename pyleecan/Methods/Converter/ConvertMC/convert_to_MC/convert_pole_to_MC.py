def convert_pole_to_MC(self):
    """Selects correct pole and implements it in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object

    Returns
    ---------

    """
    # conversion to motor-cad
    hole_type = type(self.machine.rotor.hole[0]).__name__
    len_hole = len(self.machine.rotor.hole)

    for hole_id in range(len_hole):
        if hole_type != type(self.machine.rotor.hole[hole_id]).__name__:
            self.get_logger().error(
                "In motor-cad, we have just the possibility to set the same type of hole, so we select the first hole"
            )
            len_hole = 1

    # selection type of pole
    if hole_type == "SlotW61":
        name_hole = "Sync_Salient_Pole"

    elif hole_type == "SlotW62":
        name_hole = "Sync_Parallel_Tooth"

    elif hole_type == "SlotW29":
        name_hole = "Sync_Parallel_Slot"

    else:
        raise NotImplementedError(
            f"Type of hole {hole_type} has not equivalent or has not implement"
        )

    # writting in dict
    if "[Design_Options]" not in self.other_dict:
        self.other_dict["[Design_Options]"] = {"Sync_Rotor": name_hole}
    else:
        self.other_dict["[Design_Options]"]["Sync_Rotor"] = name_hole

    self.get_logger().info(f"Conversion {hole_type} into {name_hole}")
