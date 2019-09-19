# -*- coding: utf-8 -*-
"""@package build_geometry
@date Created on juil. 10 10:31 2018
@author franco_i
@todo: modify side segments for other bore radii (due to notches)
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
        Ryoke = self.Rint
        Rbore = self.Rext
        label1 = "Ext"
        label2 = "Int"
    else:
        Ryoke = self.Rext
        Rbore = self.Rint
        label2 = "Ext"
        label1 = "Int"

    label_bore = label + "_Bore_Radius"
    label_yoke = label + "_Yoke_Radius"

    ref_point = self.comp_radius_mid_yoke() * exp(1j * pi / sym)

    surf_list = list()
    # Lamination surface(s)
    if sym == 1:  # Complete lamination
        surf_list.append(
            SurfLine(
                line_list=self.get_bore_line(0, 2 * pi, label=label_bore),
                label="Lamination_" + label + "_Bore_" + label1,
                point_ref=ref_point,
            )
        )
        if Ryoke > 0:
            surf_list.append(
                Circle(
                    radius=Ryoke,
                    label="Lamination_" + label + "_Yoke_" + label2,
                    point_ref=0,
                    center=0,
                    line_label=label_yoke,
                )
            )
    else:  # Symmetry lamination
        alpha_begin = 0
        alpha_end = 2 * pi / sym
        begin = Rbore * exp(1j * alpha_begin)
        end = Rbore * exp(1j * alpha_end)
        Z_begin = Ryoke * exp(1j * alpha_begin)
        Z_end = Ryoke * exp(1j * alpha_end)
        line_list = [Segment(Z_begin, begin, label=label + "_Yoke_Side")]
        bore_line = self.get_bore_line(alpha_begin, alpha_end, label=label_bore)
        for line in bore_line:
            line_list.append(line)
        line_list.append(Segment(end, Z_end, label=label + "_Yoke_Side"))
        if Ryoke > 0:
            line_list.append(
                Arc1(
                    begin=Z_end,
                    end=Z_begin,
                    radius=-Ryoke,
                    is_trigo_direction=False,
                    label=label_yoke,
                )
            )
        surf_list.append(
            SurfLine(
                line_list=line_list,
                label="Lamination_" + label + "_Bore_" + label1,
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
