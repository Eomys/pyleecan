from numpy import arcsin, exp

from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1
from ....Classes.SurfLine import SurfLine


def get_surface_active(self, alpha=0, delta=0):
    """Return the full winding surface

    Parameters
    ----------
    self : SlotUD2
        A SlotUD2 object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_wind: Surface
        Surface corresponding to the Winding Area
    """
    st = self.get_name_lam()
    surface = self.active_surf.copy()

    surface.label = "Wind_" + st + "_R0_T0_S0"

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return surface
