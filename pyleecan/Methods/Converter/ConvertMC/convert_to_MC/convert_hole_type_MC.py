def convert_hole_type_MC(self):
    """Selects correct hole and implements it in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object

    Returns
    ---------
    len_hole : int
        The number of hole
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

    # selection type of Slot
    if hole_type == "HoleM62" and self.machine.rotor.hole.W0_is_rad == False:
        name_hole = "Embedded_Parallel"

    elif hole_type == "HoleM62":
        name_hole = "Embedded_Radial"

    elif hole_type == "HoleM63":
        name_hole = "Embedded_Breadleaof"

    elif hole_type == "HoleM63":
        name_hole = "Interior_Flat(simple)"

    elif hole_type == "HoleM52":
        name_hole = "Interior_Flat(web)"

    elif hole_type == "HoleM60":
        name_hole = "Interior_V(simple)"
        self.get_logger().warning(f"Approximation for W3, Magnet_Post")

    elif hole_type == "HoleM57":
        name_hole = "Interior_V(web)"

    elif hole_type == "HoleM61":
        name_hole = "Interior_U-Shape"

    else:
        raise Exception("Conversion of machine doesn't exist")

    # writting in dict
    if "[Design_Options]" not in self.other_dict:
        self.other_dict["[Design_Options]"] = {"BPM_Rotor": name_hole}
    else:
        self.other_dict["[Design_Options]"]["BPM_Rotor"] = name_hole

    self.get_logger().info(f"Conversion {hole_type} into {name_hole}")

    return len_hole
