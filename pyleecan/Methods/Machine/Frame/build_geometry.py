# -*- coding: utf-8 -*-
from ....Classes.Circle import Circle
from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Classes.SurfRing import SurfRing
from numpy import exp, pi


def build_geometry(self, sym=1, alpha=0, delta=0):
    """Build the geometry of the Frame

    Parameters
    ----------
    self : Frame
        Frame Object
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
    surf_list = list()
    # If there is a frame...
    if self.comp_height_eq() != 0:
        if sym == 1:  # No symmetry / full frame
            out_surf = Circle(
                radius=self.Rext,
                label="Frame_Outter",
                center=0,
                point_ref=self.Rint + (self.Rext - self.Rint) / 2,
            )
            in_surf = Circle(
                radius=self.Rint, label="Frame_Inner", center=0, point_ref=0
            )
            surf_list = [
                SurfRing(
                    out_surf=out_surf,
                    in_surf=in_surf,
                    label="Frame",
                    point_ref=self.Rint + (self.Rext - self.Rint) / 2,
                )
            ]
        else:  # Part of the frame
            Z0 = self.Rint
            Z3 = Z0 * exp(1j * 2 * pi / sym)
            Z1 = self.Rext
            Z2 = Z1 * exp(1j * 2 * pi / sym)
            curve_list = list()
            curve_list.append(Segment(Z0, Z1))
            curve_list.append(Arc1(Z1, Z2, self.Rext))
            curve_list.append(Segment(Z2, Z3))
            curve_list.append(Arc1(Z3, Z0, -self.Rint, is_trigo_direction=False))
            surf_frame = SurfLine(
                line_list=curve_list,
                label="Frame",
                point_ref=self.Rint + (self.Rext - self.Rint) / 2,
            )
            surf_list.append(surf_frame)

        # Apply the transformations
        for surf in surf_list:
            surf.rotate(alpha)
            surf.translate(delta)

    return surf_list
