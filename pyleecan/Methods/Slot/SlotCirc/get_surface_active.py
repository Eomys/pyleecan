from ....Classes.SurfLine import SurfLine
from ....Functions.labels import WIND_LAB, DRAW_PROP_LAB


def get_surface_active(self, alpha=0, delta=0):
    """Return the full active surface

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_wind: Surface
        Surface corresponding to the Active Area
    """

    # Create curve list
    line_dict = self._comp_line_dict()
    curve_list = [
        line_dict["1-M"],
        line_dict["M-2"],
        line_dict["2-1"],
    ]
    curve_list = [line for line in curve_list if line is not None]

    # Only the closing arc (2-1) needs to be drawn (in FEMM)
    for curve in curve_list[:-1]:
        if curve.prop_dict is None:
            curve.prop_dict = dict()
        curve.prop_dict.update({DRAW_PROP_LAB: False})

    # Create surface
    ZM = line_dict["M-2"].get_begin()
    Zmid = (self.get_Rbo() + ZM) / 2
    label = self.parent.get_label() + "_" + WIND_LAB + "_R0-T0-S0"
    surface = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return surface
