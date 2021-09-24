# -*- coding: utf-8 -*-
from ....Classes.Frame import Frame


def build_geometry(self, sym=1, alpha=0, delta=0):
    """Build the geometry of the Frame with structural Bars

    Parameters
    ----------
    self : FrameBar
        FrameBar Object
    sym : int
        symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation

    Returns
    -------
    surf_list : list
        list of surface

    """

    # Build Frame Geometry
    surf_list_frame = Frame.build_geometry(self, sym, alpha, delta)
    # Build Bar Geometry
    surf_list_bar = self.build_geometry_bar(sym, alpha, delta)

    surf_list = surf_list_frame + surf_list_bar
    return surf_list
