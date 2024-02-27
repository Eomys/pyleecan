from ....Classes.SurfLine import SurfLine
from ....Functions.labels import SOP_LAB, DRAW_PROP_LAB


def get_surface_opening(self, alpha=0, delta=0):
    """Return the list of surfaces defining the opening area of the Slot

    Parameters
    ----------
    self : SlotW63
        A SlotW63 object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_list : list
        list of surfaces objects
    """

    # Create curve list
    line_dict = self._comp_line_dict()
    if self.W2 != 0:
        if self.H2 != 0:
            curve_list = [
                line_dict["1-2"],
                line_dict["2-w1"],
                line_dict["w1-w2"],
                line_dict["w2-w2s"],
                line_dict["w2s-w1s"],
                line_dict["w1s-7"],
                line_dict["7-8"],
                line_dict["8-1"],
            ]

        else:
            curve_list = [
                line_dict["2-w1"],
                line_dict["w1-w2"],
                line_dict["w2-w2s"],
                line_dict["w2s-w1s"],
                line_dict["w1s-7"],
                line_dict["7-2"],
            ]
    else:
        if self.H2 != 0:
            curve_list = [
                line_dict["1-2"],
                line_dict["2-7"],
                line_dict["7-8"],
                line_dict["8-1"],
            ]

        else:
            curve_list = [
                line_dict["2-7"],
                line_dict["7w-2w"],
            ]

    curve_list = [line for line in curve_list if line is not None]

    # Only the closing arc (10-1) needs to be drawn (in FEMM)
    for curve in curve_list[:-1]:
        if curve.prop_dict is None:
            curve.prop_dict = dict()
        curve.prop_dict.update({DRAW_PROP_LAB: False})

    # Create surface
    point_dict = self._comp_point_coordinate()
    Z2 = point_dict["Z2"]
    Z8 = point_dict["Z8"]

    Zmid = (Z8 + Z2) / 2
    label = f"{self.parent.get_label()}_{SOP_LAB}_R0-T0-S0"
    surface = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # Apply transformation
    if alpha != 0:
        surface.rotate(alpha)
    if delta != 0:
        surface.translate(delta)

    return [surface]
