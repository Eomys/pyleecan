# -*- coding: utf-8 -*-
from numpy import pi, exp

from ....Classes.Arc1 import Arc1
from ....Classes.Circle import Circle
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Classes.SurfRing import SurfRing
from ....Classes.Lamination import Lamination


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
        label = "Lamination_Stator"  # Label lamination
    else:
        label = "Lamination_Rotor"
    if self.is_internal:
        lb = "Ext"  # label for the bore
        ly = "Int"  # label for the yoke
    else:
        lb = "Int"
        ly = "Ext"
    label_bore = label + "_Bore_Radius_" + lb
    label_yoke = label + "_Yoke_Radius_" + ly

    Ryoke = self.get_Ryoke()
    H_yoke = self.comp_height_yoke()

    if self.slot is not None and self.slot.Zs != 0:
        # getting Number of Slot
        Zs = self.slot.Zs

        # Check for symmetry
        assert (Zs % sym) == 0, (
            "ERROR, Wrong symmetry for "
            + label
            + " "
            + str(Zs)
            + " slots and sym="
            + str(sym)
        )

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
        # Set line label
        for line in bore_list:
            line.label = label_bore
    else:  # No slot
        return Lamination.build_geometry(self, sym=sym, alpha=alpha, delta=delta)

    # Get Yoke lines (including notches)
    if self.yoke_notch is not None and len(self.yoke_notch) > 0:
        yoke_desc = self.get_yoke_desc(sym=sym)
        yoke_list = list()
        for yoke in yoke_desc:
            if type(yoke["obj"]) is Arc1:
                yoke_list.append(yoke["obj"])
            elif "lines" in yoke:  # Duplicated slot
                for line in yoke["lines"]:
                    yoke_list.append(type(line)(init_dict=line.as_dict()))
                    yoke_list[-1].rotate((yoke["begin_angle"] + yoke["end_angle"]) / 2)
            else:  # Notches
                self.is_internal = not self.is_internal
                lines = yoke["obj"].build_geometry()
                self.is_internal = not self.is_internal
                for line in lines:
                    line.rotate((yoke["begin_angle"] + yoke["end_angle"]) / 2)
                yoke_list.extend(lines)
        # Set line label
        for line in yoke_list:
            line.label = label_yoke
        surf_yoke = SurfLine(line_list=yoke_list, label=label_yoke, point_ref=None)
    elif sym == 1:
        surf_yoke = Circle(
            radius=Ryoke, label=label_yoke, line_label=label_yoke, center=0
        )
    elif Ryoke > 0:  # For internal lamination
        yoke_list = [
            Arc1(
                begin=Zy2,
                end=Zy1,
                radius=-Ryoke,
                is_trigo_direction=False,
                label=label_yoke,
            )
        ]
    else:
        yoke_list = list()

    # Create the lamination surface(s)
    surf_list = list()
    if sym == 1:  # Complete lamination
        if self.is_internal:
            point_ref = Ryoke + (H_yoke / 2)
        else:
            point_ref = Ryoke - (H_yoke / 2)
        # Create Slot surface
        surf_slot = SurfLine(line_list=bore_list, label=label_bore, point_ref=point_ref)
        if self.Rint == 0 and len(bore_list) > 0:
            surf_list = [surf_slot]
        elif self.Rint == 0 and len(bore_list) == 0:
            surf_list = list()
        elif self.is_internal:
            surf_list.append(
                SurfRing(
                    out_surf=surf_slot,
                    in_surf=surf_yoke,
                    label=label,
                    point_ref=point_ref,
                )
            )
        else:
            surf_list.append(
                SurfRing(
                    out_surf=surf_yoke,
                    in_surf=surf_slot,
                    label=label,
                    point_ref=point_ref,
                )
            )
    else:  # Only one surface
        # Add the Yoke part
        Zy1 = Ryoke
        Zy2 = Ryoke * exp(1j * 2 * pi / sym)
        bore_list.append(
            Segment(bore_list[-1].get_end(), Zy2, label=label + "_Yoke_Side_Left")
        )
        bore_list.extend(yoke_list)
        bore_list.append(
            Segment(Zy1, bore_list[0].get_begin(), label=label + "_Yoke_Side_Right")
        )
        # Create a Surface for the slot
        if self.is_internal:
            point_ref = (Ryoke + H_yoke / 2) * exp(1j * pi / sym)
        else:
            point_ref = (Ryoke - H_yoke / 2) * exp(1j * pi / sym)
        surf_slot = SurfLine(line_list=bore_list, label=label_bore, point_ref=point_ref)
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
