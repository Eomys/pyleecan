# -*- coding: utf-8 -*-

from ....Methods.Slot.Slot.check import SlotCheckError
from numpy import pi, exp
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine


def build_geometry_wind(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW61
        A SlotW61 object
    Nrad : int
        Number of radial layer
    Ntan : int
        Number of tangentiel layer
    is_simplified : bool
        boolean to specify if the coincident lines are considered as one
         or different lines (Default value = False)
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : complex
        complex for translation (Default value = 0)

    Returns
    -------
    surf_list: list
        List of surface delimiting the winding zone

    """

    if Nrad != 1 or Ntan != 2:
        raise S61_WindError(
            "Slot 61 can use only for winding with Nrad=1 " + "and Ntan 2"
        )
    self.check()

    # get the name of the lamination
    st = self.get_name_lam()

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10] = self._comp_point_coordinate()

    # Compute the point in the tooth ref
    hsp = pi / self.Zs
    Z4t = Z4 * exp(1j * hsp)
    Z5t = Z5 * exp(1j * hsp)
    Zw1t = Z4t - self.H3
    Zw2t = Z5t + self.H4
    Zw3t = Zw2t + 1j * ((self.W1 - self.W2) / 2 - self.W3)
    Zw4t = Zw1t + 1j * ((self.W1 - self.W2) / 2 - self.W3)

    # Go back to slot ref
    Zw1 = Zw1t * exp(1j * -hsp)
    Zw2 = Zw2t * exp(1j * -hsp)
    Zw3 = Zw3t * exp(1j * -hsp)
    Zw4 = Zw4t * exp(1j * -hsp)
    Zw1s = Zw1.conjugate()
    Zw2s = Zw2.conjugate()
    Zw3s = Zw3.conjugate()
    Zw4s = Zw4.conjugate()
    Ref1 = (Zw1 + Zw2 + Zw3 + Zw4) / 4
    Ref2 = (Zw1s + Zw2s + Zw3s + Zw4s) / 4

    # Create the surfaces
    surf_list = list()
    wind1 = [Segment(Zw3, Zw4)]
    wind2 = [Segment(Zw3s, Zw4s)]
    if (is_simplified and self.W3 > 0) or not is_simplified:
        wind1.append(Segment(Zw4, Zw1))
        wind2.append(Segment(Zw4s, Zw1s))
    if not is_simplified:
        wind1.append(Segment(Zw1, Zw2))
        wind2.append(Segment(Zw1s, Zw2s))
    if (is_simplified and self.W4 > 0) or not is_simplified:
        wind1.append(Segment(Zw2, Zw3))
        wind2.append(Segment(Zw2s, Zw3s))

    surf_list.append(
        SurfLine(line_list=wind1, label="Wind" + st + "_R0_T0_S0", point_ref=Ref1)
    )
    surf_list.append(
        SurfLine(line_list=wind2, label="Wind" + st + "_R0_T1_S0", point_ref=Ref2)
    )

    # Rotate and translate the surfaces
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list


class S61_WindError(SlotCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    winding


    """

    pass
