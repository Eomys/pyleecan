from ....Functions.labels import WIND_LAB
from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1
from ....Classes.SurfLine import SurfLine


def get_surface_active(self, alpha=0, delta=0):
    """Return the full winding surface

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
    surf_wind: Surface
        Surface corresponding to the Winding Area
    """
    # get curve_list
    type_line_wind = self.type_line_wind
    if self.wind_begin_index is None and self.wind_end_index is None:
        # Winding not define, use complete surface
        line_list = self.build_geometry()
        type_line_wind = 1  # Enforce Arc1
    else:
        line_list = self.build_geometry()[self.wind_begin_index : self.wind_end_index]

    # Add closing line
    if type_line_wind == 0:
        line_list.append(
            Segment(begin=line_list[-1].get_end(), end=line_list[0].get_begin())
        )
    else:
        line_list.append(
            Arc1(
                begin=line_list[-1].get_end(),
                end=line_list[0].get_begin(),
                radius=-abs(line_list[-1].get_end()),
                is_trigo_direction=False,
            )
        )

    label = self.parent.get_label() + "_" + WIND_LAB + "_R0-T0-S0"
    surface = SurfLine(line_list=line_list, label=label)
    surface.comp_point_ref(is_set=True)

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return surface
