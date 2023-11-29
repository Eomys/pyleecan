from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM57 import HoleM57
from pyleecan.Classes.HoleM60 import HoleM60
from pyleecan.Classes.HoleM61 import HoleM61
from pyleecan.Classes.HoleM62 import HoleM62
from pyleecan.Classes.HoleM63 import HoleM63
from pyleecan.Functions.Converter.Utils.NotImplemented import NotImplemented


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

    number_hole = self.other_dict["[Dimensions]"]["Magnet_Layers"]

    # initialisation to set the hole in rotor
    self.machine.rotor = LamHole()
    self.machine.rotor.is_stator = False
    self.machine.rotor.is_internal = True

    for hole_id in range(number_hole):
        # set the hole in obj machine, and add particularity to hole
        if hole_type == "Embedded_Parallel":
            self.machine.rotor.hole.append(HoleM62())
            self.machine.rotor.hole[hole_id].W0_is_rad = False

        elif hole_type == "Embedded_Radial":
            self.machine.rotor.hole.append(HoleM62())
            self.machine.rotor.hole[hole_id].W0_is_rad = True

        elif hole_type == "Embedded_Breadleaof":
            self.machine.rotor.hole.append(HoleM63())
            self.machine.rotor.hole[hole_id].top_flat = False

        elif hole_type == "Interior_FlatSimple":
            self.machine.rotor.hole.append(HoleM63())
            self.machine.rotor.hole[hole_id].top_flat = True

        elif hole_type == "Interior_FlatWeb":
            self.machine.rotor.hole.append(HoleM52())
            self.machine.rotor.hole[hole_id].H2 = 0

        elif hole_type == "Interior_VSimple":
            self.machine.rotor.hole.append(HoleM60())

        elif hole_type == "Interior_VWeb":
            self.machine.rotor.hole.append(HoleM57())

        elif hole_type == "Interior_UShape":
            self.machine.rotor.hole.append(HoleM61())

        else:
            raise NotImplemented(
                "Type of hole has not equivalent in pyleecan or has not implement"
            )

    self.get_logger().info(
        f"Conversion {hole_type} into {type(self.machine.rotor.hole[0]).__name__}"
    )

    # writing exception/approximation for Hole
    if type(self.machine.rotor.hole[0]).__name__ == "HoleM60":
        self.get_logger().warning(f"Approximation for W3, Magnet_Post")
