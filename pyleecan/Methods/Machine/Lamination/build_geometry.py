# -*- coding: utf-8 -*-
from numpy import pi, exp

from ....Classes.Arc1 import Arc1
from ....Classes.Circle import Circle
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Classes.SurfRing import SurfRing


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

    label_bore = label + "_Bore_Radius"
    label_yoke = label + "_Yoke_Radius"

    if self.is_internal:
        label_int = label_yoke + "_Int"  # internal label is yoke
        label_ext = label_bore + "_Ext"  # external label is bore
    else:
        label_int = label_bore + "_Int"  # internal label is bore
        label_ext = label_yoke + "_Ext"  # external label is yoke

    # Get Radius lines
    if self.is_internal:
        if self.Rint > 0:
            _, int_line = self.get_yoke_desc(
                sym=sym, is_reversed=True, line_label=label_int
            )
        else:
            int_line = []
        _, ext_line = self.get_bore_desc(sym=sym, line_label=label_ext)
    else:
        _, ext_line = self.get_yoke_desc(
            sym=sym, is_reversed=True, line_label=label_ext
        )
        _, int_line = self.get_bore_desc(sym=sym, line_label=label_int)

    # Create the surfaces
    point_ref = self.comp_point_ref(sym=sym)
    surf_list = list()
    if sym == 1:  # Complete lamination
        ext_surf = SurfLine(
            label=label_ext,
            line_list=ext_line,
            point_ref=point_ref,
        )
        int_surf = SurfLine(label=label_int, line_list=int_line, point_ref=0)
        if self.Rint > 0 and len(ext_line) > 0:
            surf_list.append(
                SurfRing(
                    out_surf=ext_surf,
                    in_surf=int_surf,
                    label=label,
                    point_ref=point_ref,
                )
            )
        elif self.Rint == 0 and len(ext_line) > 0:
            surf_list.append(ext_surf)
        else:
            pass  # No surface to draw (SlotM17)

    elif sym != 1 and len(ext_line) > 0:  # Part of the lamination by symmetry
        Z0 = self.Rint
        Z1 = self.Rext
        Z3 = Z0 * exp(1j * 2 * pi / sym)
        Z2 = Z1 * exp(1j * 2 * pi / sym)
        # Create lines
        curve_list = list()
        if self.is_internal:
            curve_list.append(Segment(Z0, Z1, label=label + "_Yoke_Side"))
        else:
            curve_list.append(Segment(Z3, Z2, label=label + "_Yoke_Side"))
        curve_list.extend(ext_line)
        if self.is_internal:
            curve_list.append(Segment(Z2, Z3, label=label + "_Yoke_Side"))
        else:
            curve_list.append(Segment(Z1, Z0, label=label + "_Yoke_Side"))
        if self.Rint > 0:
            curve_list.extend(int_line)

        surf_yoke = SurfLine(
            line_list=curve_list,
            label=label + "_Ext",
            point_ref=point_ref,
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
