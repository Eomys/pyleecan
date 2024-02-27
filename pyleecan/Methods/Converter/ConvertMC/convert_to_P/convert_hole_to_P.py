from .....Classes.LamHole import LamHole
from .....Classes.HoleM52 import HoleM52
from .....Classes.HoleM57 import HoleM57
from .....Classes.HoleM60 import HoleM60
from .....Classes.HoleM61 import HoleM61
from .....Classes.HoleM62 import HoleM62
from .....Classes.HoleM63 import HoleM63


def convert_hole_to_P(self):
    """Selects correct hole and implements it in obj machine

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object

    Returns
    ---------
    len_hole : int
        The number of hole
    """

    hole_type = self.other_dict["[Design_Options]"]["BPM_Rotor"]

    # Motor-CAD cannot have 2 different types of holes
    # initialisation to set the hole in rotor
    self.machine.rotor = LamHole()
    self.machine.rotor.is_stator = False
    self.machine.rotor.is_internal = True

    # set the hole in obj machine, and add particularity to hole
    if hole_type == "Embedded_Parallel":
        self.machine.rotor.hole.append(HoleM62())
        self.machine.rotor.hole[0].W0_is_rad = False

    elif hole_type == "Embedded_Radial":
        self.machine.rotor.hole.append(HoleM62())
        self.machine.rotor.hole[0].W0_is_rad = True

    elif hole_type == "Embedded_Breadloaf":
        self.machine.rotor.hole.append(HoleM63())
        self.machine.rotor.hole[0].top_flat = False

    elif hole_type == "Interior_Flat_Simple":
        self.machine.rotor.hole.append(HoleM63())
        self.machine.rotor.hole[0].top_flat = True
        self.get_logger().warning(
            f"HoleM63 : Approximation for H1, Pole Arc isn't present in Pyleecan"
        )

    elif hole_type == "Interior_Flat_Web":
        self.machine.rotor.hole.append(HoleM52())
        self.machine.rotor.hole[0].H2 = 0

    # possibility to have many set for the same Hole
    elif hole_type == "Interior_VSimple":
        number_hole = self.other_dict["[Dimensions]"]["VMagnet_Layers"]
        for hole_id in range(number_hole):
            self.machine.rotor.hole.append(HoleM60())

    elif hole_type == "Interior_VShape":
        number_hole = self.other_dict["[Dimensions]"]["VMagnet_Layers"]
        for hole_id in range(number_hole):
            self.machine.rotor.hole.append(HoleM57())
            self.get_logger().warning(
                "HoleM57 : Approximation check the settings for HoleM57"
            )

    elif hole_type == "Interior_UShape":
        number_hole = self.other_dict["[Dimensions]"]["Magnet_Layers"]
        for hole_id in range(number_hole):
            self.machine.rotor.hole.append(HoleM61())

    else:
        raise NotImplementedError(
            f"Type of hole {hole_type} has not equivalent in pyleecan or has not been implementated"
        )

    # writing exception/approximation for Hole
    if isinstance(self.machine.rotor.hole[0], HoleM60):
        self.get_logger().warning(f"HoleM60 : Approximation for W3, Magnet_Post")

    if isinstance(self.machine.rotor.hole[0], HoleM63):
        self.get_logger().warning(f"HoleM63 : Approximation for W0")

    if isinstance(self.machine.rotor.hole[0], HoleM57):
        self.get_logger().warning(
            f"HoleM57 : Approximation Pole Arc has not equivalent in pyleecan "
        )

    self.get_logger().info(
        f"Conversion {hole_type} into {type(self.machine.rotor.hole[0]).__name__}"
    )
