# -*- coding: utf-8 -*-
from numpy import pi, angle, exp

from ....Classes.Circle import Circle
from ....Classes.SurfLine import SurfLine
from ....Classes.SurfRing import SurfRing
from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Functions.labels import LAM_LAB, BORE_LAB, YOKE_LAB


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

    # Label setup
    label = self.get_label()
    label_lam = label + "_" + LAM_LAB
    label_bore = label + "_" + BORE_LAB
    label_yoke = label + "_" + YOKE_LAB
    if self.is_internal:
        label_ext = label_bore
        label_int = label_yoke
    else:
        label_ext = label_yoke
        label_int = label_bore

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
        surf_slot = SurfLine(line_list=bore_list, label=label_bore)
        if self.is_internal:
            point_ref = Ryoke + (H_yoke / 2)
        else:
            point_ref = Ryoke - (H_yoke / 2)
        surf_slot.point_ref = point_ref
        # Create yoke circle surface
        surf_yoke = Circle(
            radius=Ryoke, label=label_yoke, line_label=label_yoke, center=0
        )
        if self.Rint == 0 and len(bore_list) > 0:
            surf_slot.label = label_lam
            surf_list = [surf_slot]
        elif self.Rint == 0 and len(bore_list) == 0:
            surf_list = list()
        elif self.is_internal:
            surf_list.append(
                SurfRing(
                    out_surf=surf_slot,
                    in_surf=surf_yoke,
                    label=label_lam,
                    point_ref=point_ref,
                )
            )
        else:
            surf_list.append(
                SurfRing(
                    out_surf=surf_yoke,
                    in_surf=surf_slot,
                    label=label_lam,
                    point_ref=point_ref,
                )
            )
    else:  # Only one surface
        # Add the Yoke part
        Zy1 = Ryoke
        Zy2 = Ryoke * exp(1j * 2 * pi / sym)
        bore_list.append(
            Segment(
                Rbo * exp(1j * (2 * pi / sym)),
                Zy2,
                label=label_lam + "_Yoke_Side_Right",
            )
        )
        if Ryoke > 0:
            # For internal lamination Ryoke can be 0
            bore_list.append(
                Arc1(
                    begin=Zy2,
                    end=Zy1,
                    radius=-Ryoke,
                    is_trigo_direction=False,
                    label=label_lam + "_Yoke_Radius",
                )
            )
        bore_list.append(Segment(Zy1, Rbo, label=label_lam + "_Yoke_Side_Left"))
        # Create a Surface for the slot
        if self.is_internal:
            point_ref = (Ryoke + H_yoke / 2) * exp(1j * pi / sym)
        else:
            point_ref = (Ryoke - H_yoke / 2) * exp(1j * pi / sym)
        surf_slot = SurfLine(
            line_list=bore_list,
            label=label_lam,
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
