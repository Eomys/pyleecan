from ....Classes.SurfLine import SurfLine
from ....Functions.labels import SOP_LAB, DRAW_PROP_LAB


def get_surface_opening(self, alpha=0, delta=0):
    """Return the list of surfaces defining the opening area of the Slot

    Parameters
    ----------
    self : SlotW29
        A SlotW29 object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_list : list
        list of surfaces objects
    """

    # H0=H1=0 no opening
    if self.H0 == 0 and self.H1 == 0:
        return []

    # Create curve list
    line_dict = self._comp_line_dict()
    # Selection type Wedge
    if self.wedge_type == 0:
        # Create curve list

        curve_list = [
            line_dict["1-2"],
            line_dict["2-3"],
            line_dict["3-4"],
            line_dict["4-9"],
            line_dict["9-10"],
            line_dict["10-11"],
            line_dict["11-12"],
            line_dict["12-1"],
        ]
        # Create surface
        if self.is_outwards():
            Zmid = self.get_Rbo() + (self.H0 + self.H1) / 2
        else:
            Zmid = self.get_Rbo() - (self.H0 + self.H1) / 2

    else:
        # Create curve list
        curve_list = [
            line_dict["1-2"],
            line_dict["2-11"],
            line_dict["11-12"],
            line_dict["12-1"],
        ]
        # Create surface
        if self.is_outwards():
            Zmid = self.get_Rbo() + self.H0 / 2
        else:
            Zmid = self.get_Rbo() - self.H0 / 2

    curve_list = [line for line in curve_list if line is not None]

    # Only the closing arc (12-1) needs to be drawn (in FEMM)
    for curve in curve_list[:-1]:
        if curve.prop_dict is None:
            curve.prop_dict = dict()
        curve.prop_dict.update({DRAW_PROP_LAB: False})

    # Create surface
    label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S0"
    surface = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return [surface]
