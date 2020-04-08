# -*- coding: utf-8 -*-
from ....Classes.Circle import Circle
from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Classes.SurfRing import SurfRing
from numpy import pi, exp


def build_geometry(self, sym=1, alpha=0, delta=0):
    """Build the geometry of the Lamination

    Parameters
    ----------
    self : Lamination
        Lamination Object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation

    Returns
    surf_list : list
        list of surfaces needed to draw the lamination

    """
    # Lamination label
    if self.is_stator:
        label = "Lamination_Stator"
    else:
        label = "Lamination_Rotor"

    if self.is_internal:
        ls = "_Bore_"  # label for the bore
        ly = "_Yoke_"  # label for the yoke
    else:
        ls = "_Yoke_"
        ly = "_Bore_"

    surf_list = list()
    if sym == 1:  # Complete lamination
        out_surf = Circle(
            radius=self.Rext,
            label=label + ly + "Ext",
            center=0,
            point_ref=self.Rint + (self.Rext - self.Rint) / 2,
        )
        in_surf = Circle(
            radius=self.Rint, label=label + ls + "Int", center=0, point_ref=0
        )
        if self.Rint > 0:
            surf_list.append(
                SurfRing(
                    out_surf=out_surf,
                    in_surf=in_surf,
                    label=label,
                    point_ref=self.Rint + (self.Rext - self.Rint) / 2,
                )
            )
        else:
            surf_list.append(out_surf)
    else:  # Part of the lamination by symmetry
        Z0 = self.Rint
        Z1 = self.Rext
        Z3 = Z0 * exp(1j * 2 * pi / sym)
        Z2 = Z1 * exp(1j * 2 * pi / sym)
        curve_list = list()
        curve_list.append(Segment(Z0, Z1))
        curve_list.append(
            Arc1(begin=Z1, end=Z2, radius=self.Rext, is_trigo_direction=True)
        )
        curve_list.append(Segment(Z2, Z3))
        if self.Rint > 0:
            curve_list.append(
                Arc1(begin=Z3, end=Z0, radius=self.Rint, is_trigo_direction=False)
            )
        surf_yoke = SurfLine(
            line_list=curve_list,
            label=label + "_Ext",
            point_ref=self.Rint + (self.Rext - self.Rint) / 2,
        )
        surf_list.append(surf_yoke)

    # Add the ventilation ducts if there is any
    for vent in self.axial_vent:
        surf_list.extend(vent.build_geometry(sym=sym, is_stator=self.is_stator))

    # apply the transformation
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
