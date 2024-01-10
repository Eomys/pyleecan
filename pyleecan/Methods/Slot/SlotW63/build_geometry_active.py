from ....Classes.SurfLine import SurfLine
from ....Methods.Slot.SlotW63 import S63_WindError
from ....Functions.labels import WIND_LAB


def build_geometry_active(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW63
        A SlotW63 object
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
        raise S63_WindError("Slot 63 can use only for winding with Nrad=1 and Ntan=2")
    self.check()

    # get the name of the lamination
    lam_label = self.parent.get_label()

    line_dict = self._comp_line_dict()

    if self.W2 != 0:
        Ref1 = (line_dict["w1-2"].get_begin() + line_dict["4-w2"].get_begin()) / 2
        Ref2 = (line_dict["w1s-w2s"].get_begin() + line_dict["5-6"].get_begin()) / 2

        # Create the surfaces
        wind1_lines = [
            line_dict["w1-2"],
            line_dict["2-3"],
            line_dict["3-4"],
            line_dict["4-w2"],
            line_dict["w2-w1"],
        ]

        wind2_lines = [
            line_dict["w1s-w2s"],
            line_dict["w2s-5"],
            line_dict["5-6"],
            line_dict["6-7"],
            line_dict["7-w1s"],
        ]

        surf_list = list()
        surf_list.append(
            SurfLine(
                line_list=wind1_lines,
                label=f"{lam_label}_{WIND_LAB}_R0-T0-S0",
                point_ref=Ref1,
            )
        )
        surf_list.append(
            SurfLine(
                line_list=wind2_lines,
                label=f"{lam_label}_{WIND_LAB}_R0-T1-S0",
                point_ref=Ref2,
            )
        )

    else:
        Ref1 = (line_dict["7-2"].get_begin() + line_dict["4-5"].get_begin()) / 2

        # Create the surfaces
        wind1_lines = [
            line_dict["7-2"],
            line_dict["2-3"],
            line_dict["3-4"],
            line_dict["4-5"],
            line_dict["5-6"],
            line_dict["6-7"],
        ]

        surf_list = list()
        surf_list.append(
            SurfLine(
                line_list=wind1_lines,
                label=f"{lam_label}_{WIND_LAB}_R0-T0-S0",
                point_ref=Ref1,
            )
        )

    # Rotate and translate the surfaces
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
