from .....Classes.HoleM52 import HoleM52
from .....Classes.HoleM57 import HoleM57
from .....Classes.HoleM60 import HoleM60
from .....Classes.HoleM61 import HoleM61
from .....Classes.HoleM62 import HoleM62
from .....Classes.HoleM63 import HoleM63


def convert_hole_to_other(self):
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
    hole = self.machine.rotor.hole[0]
    hole_type = type(hole).__name__

    # Check that every set of hole have the same type
    for current_hole in self.machine.rotor.hole:
        if isinstance(current_hole, hole.__class__):
            self.get_logger().error(
                "In motor-cad, we have just the possibility to set the same type of hole, so we select the first hole"
            )

    # selection type of Slot
    if isinstance(hole, HoleM52):
        name_hole = "Interior_Flat(web)"

    elif isinstance(hole, HoleM57):
        name_hole = "Interior_V(web)"

    elif isinstance(hole, HoleM60):
        name_hole = "Interior_V(simple)"
        self.get_logger().warning(f"Approximation for W3, Magnet_Post")

    elif isinstance(hole, HoleM61):
        name_hole = "Interior_U-Shape"

    elif isinstance(hole, HoleM62):
        if self.machine.rotor.hole.W0_is_rad == False:
            name_hole = "Embedded_Parallel"
        else:
            name_hole = "Embedded_Radial"

    elif isinstance(hole, HoleM63):
        if hole.top_flat == False:
            name_hole = "Embedded_Breadleaof"
        else:
            name_hole = "Interior_Flat(simple)"

    else:
        raise NotImplementedError(
            f"Type of hole {hole_type} has not equivalent or has not been implementated"
        )

    # writting in dict
    if "[Design_Options]" not in self.other_dict:
        self.other_dict["[Design_Options]"] = {"BPM_Rotor": name_hole}
    else:
        self.other_dict["[Design_Options]"]["BPM_Rotor"] = name_hole

    self.get_logger().info(f"Conversion {hole_type} into {name_hole}")
