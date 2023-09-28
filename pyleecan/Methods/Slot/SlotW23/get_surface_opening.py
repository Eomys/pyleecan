from ....Classes.SurfLine import SurfLine
from ....Functions.labels import SOP_LAB, DRAW_PROP_LAB


def get_surface_opening(self, alpha=0, delta=0):
    """Return the list of surfaces defining the opening area of the Slot

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object
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
    if self.H0 == 0 and self.get_H1() == 0:
        return []

    # Create curve list
    line_dict = self._comp_line_dict()
    curve_list = [
        line_dict["1-2"],
        line_dict["2-3"],
        line_dict["3-6"],
        line_dict["6-7"],
        line_dict["7-8"],
        line_dict["8-1"],
    ]
    curve_list = [line for line in curve_list if line is not None]

    # Only the closing arc (8-1) needs to be drawn (in FEMM)
    for curve in curve_list[:-1]:
        if curve.prop_dict is None:
            curve.prop_dict = dict()
        curve.prop_dict.update({DRAW_PROP_LAB: False})

    # Create surface
    if self.is_outwards():
        Zmid = self.get_Rbo() + self.H0 / 2
    else:
        Zmid = self.get_Rbo() - self.H0 / 2
    label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S0"
    surface = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return [surface]
