from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import SOP_LAB


def get_surface_opening(self, alpha=0, delta=0):
    """Return the list of surfaces defining the opening area of the Slot

    Parameters
    ----------
    self : SlotUD
        A SlotUD object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_list : list
        list of surfaces objects
    """

    # get curve_list
    line_list = self.build_geometry()
    curve_list_start = line_list[: self.wind_begin_index]
    curve_list_end = line_list[self.wind_end_index :]
    # Active Line
    Zb = curve_list_start[-1].get_end()
    Ze = curve_list_end[0].get_begin()
    if self.type_line_wind == 0:
        act_line = Segment(begin=Zb, end=Ze)
    else:
        act_line = Arc1(
            begin=Zb,
            end=Ze,
            radius=abs(Zb),
            is_trigo_direction=True,
        )
    bot_line = Arc1(
        curve_list_end[-1].get_end(),
        curve_list_start[0].get_begin(),
        -self.get_Rbo(),
        is_trigo_direction=False,
    )

    curve_list = curve_list_start + [act_line] + curve_list_end + [bot_line]
    label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S0"
    surface = SurfLine(line_list=curve_list, label=label)
    surface.comp_point_ref(is_set=True)

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return [surface]
