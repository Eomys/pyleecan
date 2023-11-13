from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM57 import HoleM57
from pyleecan.Classes.HoleM60 import HoleM60
from pyleecan.Classes.HoleM61 import HoleM61
from pyleecan.Classes.HoleM62 import HoleM62
from pyleecan.Classes.HoleM63 import HoleM63


def convert_hole_type_P(self):
    """Selection correct hole and implementation in obj machine or in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    hole_type = self.other_dict["[Design_Options]"]["BPM_Rotor"]

    # initialisation to set the hole in rotor
    dict_machine = self.machine.rotor.as_dict()
    self.machine.rotor = LamHole(init_dict=dict_machine)
    self.machine.rotor.is_stator = False
    self.machine.rotor.is_internal = True

    if hole_type == "Embedded_Parallel":
        # set the hole in obj machine, and add particularity to hole
        self.machine.rotor.hole.append(HoleM62())
        self.machine.rotor.hole[0].W0_is_rad = False

    elif hole_type == "Embedded_Radial":
        # set the hole in obj machine, and add particularity to hole
        self.machine.rotor.hole.append(HoleM62())
        self.machine.rotor.hole[0].W0_is_rad = True

    elif hole_type == "Embedded_Breadleaof":
        # set the hole in obj machine, and add particularity to hole
        self.machine.rotor.hole.append(HoleM63())
        self.machine.rotor.hole[0].top_flat = False

    elif hole_type == "Interior_Flat(simple)":
        # set the hole in obj machine, and add particularity to hole
        self.machine.rotor.hole.append(HoleM63())
        self.machine.rotor.hole[0].top_flat = True

    elif hole_type == "Interior_Flat(web)":
        # set the hole in obj machine, and add particularity to hole
        self.machine.rotor.hole.append(HoleM52())

    elif hole_type == "Interior_V(simple)":
        # set the hole in obj machine, and add particularity to hole
        self.machine.rotor.hole.append(HoleM60())

    elif hole_type == "Interior_V(web)":
        # set the hole in obj machine, and add particularity to hole
        self.machine.rotor.hole.append(HoleM57())

    elif hole_type == "Interior_UShape":
        # set the hole in obj machine, and add particularity to hole
        self.machine.rotor.hole.append(HoleM61())

    else:
        raise Exception("Conversion of machine doesn't exist")

    return self.other_dict["[Dimensions]"]["Magnet_Layers"]
