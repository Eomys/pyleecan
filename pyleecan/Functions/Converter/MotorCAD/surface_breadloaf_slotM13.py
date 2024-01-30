from numpy import sqrt, cos, arcsin, exp


def other_to_P(self, machine, other_dict, other_unit_dict):
    """Converts the surface_breadloaf motor-cad slot into pyleecan slotM13

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    machine : Machine
        A pyleecan machine
    other_dict : dict
        A dict with the conversion obj machine
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)

    Returns
    ---------
    machine : Machine
        A pyleecan machine
    """

    # Magnet arc is equivalent at W1 in ED
    self.unit_type = "ED"
    other_path_list = ["[Dimensions]", "Magnet_Arc_[ED]"]
    W1 = self.get_other(other_dict, other_path_list, other_unit_dict)

    self.unit_type = "m"

    if "MagnetReduction" in other_dict["[Dimensions]"]:
        other_path_list = ["[Dimensions]", "MagnetReduction"]
        Red = self.get_other(other_dict, other_path_list, other_unit_dict)

    else:
        Red = 0

    Rbo = machine.rotor.get_Rbo()

    slot_W1 = sqrt(2 * (Rbo) ** 2 * (1 - cos(W1)))
    machine.rotor.slot.W1 = slot_W1

    # set W0
    machine.rotor.slot.W0 = slot_W1

    # correction value H1 (circular segment)
    c = machine.rotor.slot.W0
    alpha = 2 * arcsin(c / (2 * Rbo))
    H = Rbo * (1 - cos(alpha / 2))
    machine.rotor.slot.H1 = machine.rotor.slot.H1 + H

    # define rtopm at max

    # alpha is the angle to rotate Z0 so ||Z1,Z10|| = W0
    alpha = float(arcsin(slot_W1 / (2 * Rbo)))

    Z1 = Rbo * exp(-1j * alpha)

    machine.rotor.slot.Rtopm = abs(Z1)

    # point selection
    point_dict = machine.rotor.slot._comp_point_coordinate()
    ZM0 = point_dict["ZM0"]
    ZM2 = point_dict["ZM2"]
    ZM3 = point_dict["ZM3"]
    ZM2 = ZM2 - Red
    ZM3 = ZM3 - Red

    x2 = ZM0
    y2 = 0
    x1 = ZM2.real
    y1 = ZM2.imag

    x3 = ZM3.real
    y3 = ZM3.imag

    # equation cercle with 3 points
    # coordonné du centre x
    x = -(
        (x3**2 - x2**2 + y3**2 - y2**2) / (2 * (y3 - y2))
        - (x2**2 - x1**2 + y2**2 - y1**2) / (2 * (y2 - y1))
    ) / (((x2 - x1) / (y2 - y1)) - ((x3 - x2) / (y3 - y2)))

    y = -((x2 - x1) * x / (y2 - y1)) + (
        (x2**2 - x1**2 + y2**2 - y1**2) / (2 * (y2 - y1))
    )

    Rtopm = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)

    machine.rotor.slot.Rtopm = Rtopm

    return machine


def P_to_other(self, machine, other_dict, other_unit_dict=None):
    """conversion obj machine in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    machine : Machine
        A pyleecan machine
    other_dict : dict
        A dict with the conversion obj machine
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)

    Returns
    ---------
    other_dict : dict
        A dict with the conversion obj machine
    """

    return other_dict
