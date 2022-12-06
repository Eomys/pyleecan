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
        Slot 60 can use only for winding with Nrad=1 and Ntan=2

    """

    if Nrad != 1 or Ntan != 2:
        raise S60_WindError("Slot 60 can use only for winding with Nrad=1 and Ntan=2")
    self.check()

    # get the name of the lamination
    lam_label = self.parent.get_label()

    line_dict = self._comp_line_dict()

    Ref1 = (line_dict["w3-w4"].get_begin() + line_dict["w1-w2"].get_begin()) / 2
    Ref2 = (line_dict["w3s-w4s"].get_begin() + line_dict["w1s-w2s"].get_begin()) / 2

    # Create the surfaces
    wind1_lines = [
        line_dict["w3-w4"],
        line_dict["w4-w1"],
        line_dict["w1-w2"],
        line_dict["w2-w3"],
    ]

    wind2_lines = [
        line_dict["w3s-w4s"],
        line_dict["w4s-w1s"],
        line_dict["w1s-w2s"],
        line_dict["w2s-w3s"],
    ]

    surf_list = list()
    surf_list.append(
        SurfLine(
            line_list=wind1_lines,
            label=lam_label + "_" + WIND_LAB + "_R0-T0-S0",
            point_ref=Ref1,
        )
    )
    surf_list.append(
        SurfLine(
            line_list=wind2_lines,
            label=lam_label + "_" + WIND_LAB + "_R0-T1-S0",
            point_ref=Ref2,
        )
    )

    # Rotate and translate the surfaces
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
