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

    bore_list = list()

    # Add first bore line
    if sym > 1:
        op0 = self.slot_list[0].comp_angle_opening()
        # self.get_bore_line(0, self.alpha[0] - op0 / 2)
        bore_list.append(
            Arc1(
                begin=Rbo,
                end=Rbo * exp(self.alpha[0] - op0 / 2),
                radius=Rbo,
                is_trigo_direction=True,
            )
        )

    for ii in range(int(len(self.slot_list) / sym) - 1):
        # Add the slot lines
        slot_line = self.slot_list[ii].build_geometry()
        for line in slot_line:
            line.rotate(angle=self.alpha[ii])
        bore_list.extend(slot_line)
        # Add the bore line up to the next slot
        if sym == 1 or ii != len(self.slot_list) / sym - 1:
            # Skip the last bore line in case of sym
            op1 = self.slot_list[ii].comp_angle_opening()
            op2 = self.slot_list[ii + 1].comp_angle_opening()
            # self.get_bore_line(self.alpha[ii] + op1 / 2, self.alpha[ii + 1] - op2 / 2)
            bore_list.append(
                Arc1(
                    begin=Rbo * exp(1j * (self.alpha[ii] + op1 / 2)),
                    end=Rbo * exp(1j * (self.alpha[ii + 1] - op2 / 2)),
                    radius=Rbo,
                    is_trigo_direction=True,
                )
            )

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
        # Add the last bore line
        bore_list.append(
            Arc1(
                begin=Rbo * exp(1j * (self.alpha[ii] + op1 / 2)),
                end=Rbo * exp(1j * (2 * pi / sym)),
                radius=Rbo,
                is_trigo_direction=True,
            )
        )
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
