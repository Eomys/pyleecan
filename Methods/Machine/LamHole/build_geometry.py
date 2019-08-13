# -*- coding: utf-8 -*-
"""@package build_geometry
@date Created on juil. 10 10:31 2018
@author franco_i
"""
from numpy import pi, exp

from pyleecan.Classes.Circle import Circle
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment


def build_geometry(self, sym=1, alpha=0, delta=0, is_simplified=False):
    """Build the geometry of the LamHole object

    Parameters
    ----------
    self : LamHole
        The LamHole to build in surface
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_simplified: bool
        True to avoid line superposition

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the lamination

    """

    # Lamination label
    if self.is_stator:
        label = "Stator"
    else:
        label = "Rotor"

    if self.is_internal:
        ls = "_Bore_"  # label for the bore
        ly = "_Yoke_"  # label for the yoke
    else:
        ls = "_Yoke_"
        ly = "_Bore_"

    ref_point = self.comp_radius_mid_yoke() * exp(1j * pi / sym)

    surf_list = list()
    # Lamination surface(s)
    if sym == 1:  # Complete lamination
        surf_list.append(
            Circle(
                radius=self.Rext,
                label="Lamination_" + label + ls + "Ext",
                point_ref=ref_point,
                center=0,
                line_label=label + ls + "Radius",
            )
        )
        if self.Rint > 0:
            surf_list.append(
                Circle(
                    radius=self.Rint,
                    label="Lamination_" + label + ly + "Int",
                    point_ref=0,
                    center=0,
                    line_label=label + ly + "Radius",
                )
            )
    else:  # Symmetry lamination
        begin = self.Rext
        end = self.Rext * exp(1j * 2 * pi / sym)
        Z_begin = self.Rint
        Z_end = self.Rint * exp(1j * 2 * pi / sym)
        line_list = [
            Segment(Z_begin, begin, label=label + "_Yoke_Side"),
            Arc1(begin, end, self.Rext, label=label + ls + "Radius"),
            Segment(end, Z_end, label=label + "_Yoke_Side"),
        ]
        if self.Rint > 0:
            line_list.append(
                Arc1(Z_end, Z_begin, -self.Rint, label=label + ly + "Radius")
            )
        surf_list.append(
            SurfLine(
                line_list=line_list,
                label="Lamination_" + label + ls + "Ext",
                point_ref=ref_point,
            )
        )

    # Holes surface(s)
    for hole in self.hole:
        Zh = hole.Zh
        assert (Zh % sym) == 0  # For now only
        angle = 2 * pi / Zh
        # Create the first hole surface(s)
        surf_hole = hole.build_geometry(alpha=pi / Zh)

        # Copy the hole for Zh / sym
        for ii in range(Zh // sym):
            for surf in surf_hole:
                new_surf = type(surf)(init_dict=surf.as_dict())
                if "Magnet" in surf.label and ii % 2 != 0:  # if the surf is Magnet
                    # Changing the pole of the magnet (before reference number )
                    new_surf.label = new_surf.label[:-10] + "S" + new_surf.label[-9:]
                if "Hole" in surf.label:
                    # changing the hole or magnet reference number
                    new_surf.label = new_surf.label[:-1] + str(ii)
                new_surf.rotate(ii * angle)
                surf_list.append(new_surf)

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    # Adding the ventilation surfaces
    for vent in self.axial_vent:
        surf_list += vent.build_geometry(
            sym=sym, alpha=alpha, delta=delta, is_stator=self.is_stator
        )

    return surf_list
