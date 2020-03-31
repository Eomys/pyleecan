# -*- coding: utf-8 -*-
"""@package build_geometry
@date Created on juin 20 11:12 2018
@author franco_i
"""
from numpy import pi, angle, exp

from pyleecan.Classes.Circle import Circle
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfRing import SurfRing
from pyleecan.Methods.Machine.Lamination.build_geometry import (
    build_geometry as build_geo,
)


def build_geometry(self, sym=1, alpha=0, delta=0):
    """Build the geometry of the LamSlot object

    Parameters
    ----------
    self : LamSlot
        a LamSlot object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the lamination

    """

    if self.is_stator:
        ll = "Stator"  # Label lamination
    else:
        ll = "Rotor"
    if self.is_internal:
        ls = "Ext"  # label for the slot
        ly = "Int"  # label for the yoke
    else:
        ls = "Int"
        ly = "Ext"

    Ryoke = self.get_Ryoke()
    H_yoke = self.comp_height_yoke()

    if self.slot is not None and self.slot.Zs != 0:
        # getting Number of Slot
        Zs = self.slot.Zs

        # Check for symmetry
        assert (Zs % sym) == 0

        bore_desc = self.get_bore_desc(sym=sym)
        bore_list = list()
        for bore in bore_desc:
            if type(bore["obj"]) is Arc1:
                bore_list.append(bore["obj"])
            elif "lines" in bore:  # Duplicated slot
                for line in bore["lines"]:
                    bore_list.append(type(line)(init_dict=line.as_dict()))
                    bore_list[-1].rotate((bore["begin_angle"] + bore["end_angle"]) / 2)
            else:  # Notches
                lines = bore["obj"].build_geometry()
                for line in lines:
                    line.rotate((bore["begin_angle"] + bore["end_angle"]) / 2)
                bore_list.extend(lines)
    else:  # No slot
        return build_geo(self, sym=sym, alpha=alpha, delta=delta)

    # Create the lamination surface(s)
    surf_list = list()
    if sym == 1:  # Complete lamination
        if self.is_internal:
            point_ref = Ryoke + (H_yoke / 2)
        else:
            point_ref = Ryoke - (H_yoke / 2)
        # Create Slot surface
        surf_slot = SurfLine(
            line_list=bore_list,
            label="Lamination_" + ll + "_Bore_" + ls,
            point_ref=point_ref,
        )
        # Create yoke circle surface
        surf_yoke = Circle(
            radius=Ryoke,
            label="Lamination_" + ll + "_Yoke_" + ly,
            line_label=ll + "_Yoke_Radius",
            center=0,
        )
        if self.Rint == 0:
            surf_list = [surf_slot]
        elif self.is_internal:
            surf_list.append(
                SurfRing(
                    out_surf=surf_slot,
                    in_surf=surf_yoke,
                    label="Lamination_" + ll,
                    point_ref=point_ref,
                )
            )
        else:
            surf_list.append(
                SurfRing(
                    out_surf=surf_yoke,
                    in_surf=surf_slot,
                    label="Lamination_" + ll,
                    point_ref=point_ref,
                )
            )
    else:  # Only one surface
        # Add the Yoke part
        Zy1 = Ryoke
        Zy2 = Ryoke * exp(1j * 2 * pi / sym)
        bore_list.append(Segment(bore_list[-1].get_end(), Zy2, label=ll + "_Yoke_Side"))
        if Ryoke > 0:  # For internal lamination
            bore_list.append(
                Arc1(
                    begin=Zy2,
                    end=Zy1,
                    radius=-Ryoke,
                    is_trigo_direction=False,
                    label=ll + "_Yoke_Radius",
                )
            )
        bore_list.append(
            Segment(Zy1, bore_list[0].get_begin(), label=ll + "_Yoke_Side")
        )
        # Create a Surface for the slot
        if self.is_internal:
            point_ref = (Ryoke + H_yoke / 2) * exp(1j * pi / sym)
        else:
            point_ref = (Ryoke - H_yoke / 2) * exp(1j * pi / sym)
        surf_slot = SurfLine(
            line_list=bore_list,
            label="Lamination_" + ll + "_Bore_" + ls,
            point_ref=point_ref,
        )
        surf_list.append(surf_slot)

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
