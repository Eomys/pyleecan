# -*- coding: utf-8 -*-
from numpy import pi, angle, exp

from ....Classes.Circle import Circle
from ....Classes.SurfLine import SurfLine
from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment


def build_geometry(self, sym=1, alpha=0, delta=0):
    """Build the geometry of the LamSlotMulti object

    Parameters
    ----------
    self : LamSlotMulti
        a LamSlotMulti object
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

    # getting Number of Slot
    Zs = self.get_Zs()

    # Check for symmetry
    assert (Zs % sym) == 0

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
    Rbo = self.get_Rbo()
    H_yoke = self.comp_height_yoke()

    bore_desc = self.get_bore_desc(sym=sym)
    bore_list = list()
    for bore in bore_desc:
        if type(bore["obj"]) is Arc1:
            bore_list.append(bore["obj"])
        else:
            lines = bore["obj"].build_geometry()
            for line in lines:
                line.rotate((bore["begin_angle"] + bore["end_angle"]) / 2)
            bore_list.extend(lines)

    # Create the lamination surface(s)
    surf_list = list()
    if sym == 1:  # Complete lamination
        # Create Slot surface
        surf_slot = SurfLine(
            line_list=bore_list, label="Lamination_" + ll + "_Bore_" + ls
        )
        if self.is_internal:
            surf_slot.point_ref = Ryoke + (H_yoke / 2)
        else:
            surf_slot.point_ref = Ryoke - (H_yoke / 2)
        # Create yoke circle surface
        if Ryoke > 0:
            surf_yoke = Circle(
                radius=Ryoke,
                label="Lamination_" + ll + "_Yoke_" + ly,
                line_label=ll + "_Yoke_Radius",
                center=0,
            )
        # The order matters when plotting
        if self.is_internal:
            surf_list.append(surf_slot)
            if Ryoke > 0:
                surf_list.append(surf_yoke)
        else:
            surf_yoke.point_ref = None  # No need to set the surface
            surf_list.append(surf_yoke)
            surf_list.append(surf_slot)
    else:  # Only one surface
        # Add the Yoke part
        Zy1 = Ryoke
        Zy2 = Ryoke * exp(1j * 2 * pi / sym)
        bore_list.append(
            Segment(Rbo * exp(1j * (2 * pi / sym)), Zy2, label=ll + "_Yoke_Side")
        )
        if Ryoke > 0:
            # For internal lamination Ryoke can be 0
            bore_list.append(
                Arc1(
                    begin=Zy2,
                    end=Zy1,
                    radius=-Ryoke,
                    is_trigo_direction=False,
                    label=ll + "_Yoke_Radius",
                )
            )
        bore_list.append(Segment(Zy1, Rbo, label=ll + "_Yoke_Side"))
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
