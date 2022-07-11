from ....Methods.Slot.Slot import SlotCheckError
from numpy import pi, exp

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Methods.Slot.SlotW60 import S60_WindError
from ....Functions.labels import WIND_LAB


def build_geometry_active(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW60
        A SlotW60 object
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

    Raises
    -------
    S60_WindError
        Slot 60 can use only for winding with Nrad=1 and Ntan 2

    """

    if Nrad != 1 or Ntan != 2:
        raise S60_WindError(
            "Slot 60 can use only for winding with Nrad=1 " + "and Ntan 2"
        )
    self.check()

    # get the name of the lamination
    lam_label = self.parent.get_label()


    point_dict = self._comp_point_coordinate()
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Zw1 = point_dict["Zw1"]
    Zw2 = point_dict["Zw2"]
    Zw3 = point_dict["Zw3"]
    Zw4 = point_dict["Zw4"]
    Zw1s = point_dict["Zw1s"]
    Zw2s = point_dict["Zw2s"]
    Zw3s = point_dict["Zw3s"]
    Zw4s = point_dict["Zw4s"]
    
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
        SurfLine(
            line_list=wind1,
            label=lam_label + "_" + WIND_LAB + "_R0-T0-S0",
            point_ref=Ref1,
        )
    )
    surf_list.append(
        SurfLine(
            line_list=wind2,
            label=lam_label + "_" + WIND_LAB + "_R0-T1-S0",
            point_ref=Ref2,
        )
    )

    # Rotate and translate the surfaces
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
