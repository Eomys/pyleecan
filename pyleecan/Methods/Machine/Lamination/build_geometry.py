# -*- coding: utf-8 -*-
from numpy import pi, exp

from ....Classes.Arc1 import Arc1
from ....Classes.Circle import Circle
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Classes.SurfRing import SurfRing
from ....Functions.labels import (
    LAM_LAB,
    BORE_LAB,
    YOKE_LAB,
    RADIUS_PROP_LAB,
    BOUNDARY_PROP_LAB,
    YSR_LAB,
    YSL_LAB,
)
from ....Functions.Geometry.transform_hole_surf import transform_hole_surf


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
    # Label setup
    label = self.get_label()
    label_lam = label + "_" + LAM_LAB
    label_bore = label + "_" + LAM_LAB + BORE_LAB
    label_yoke = label + "_" + LAM_LAB + YOKE_LAB
    if self.is_internal:
        label_ext = label_bore
        label_int = label_yoke
    else:
        label_ext = label_yoke
        label_int = label_bore

    # Get Radius lines
    if self.is_internal:
        if self.Rint > 0:
            _, int_line = self.get_yoke_desc(
                sym=sym,
                is_reversed=True,
                prop_dict={RADIUS_PROP_LAB: YOKE_LAB, BOUNDARY_PROP_LAB: label_yoke},
            )
        else:
            int_line = []
        _, ext_line = self.get_bore_desc(sym=sym, prop_dict={RADIUS_PROP_LAB: BORE_LAB})
    else:
        _, ext_line = self.get_yoke_desc(
            sym=sym,
            is_reversed=True,
            prop_dict={RADIUS_PROP_LAB: YOKE_LAB, BOUNDARY_PROP_LAB: label_yoke},
        )
        _, int_line = self.get_bore_desc(sym=sym, prop_dict={RADIUS_PROP_LAB: BORE_LAB})

    # Add the ventilation ducts if there is any
    surf_list = list()
    vent_surf_list = list()
    if self.axial_vent not in [None, []]:
        for vent in self.axial_vent:
            vent_list = vent.build_geometry(alpha=0, delta=0)
            vent_surf_list.extend(
                transform_hole_surf(
                    hole_surf_list=vent_list,
                    Zh=vent.Zh,
                    sym=sym,
                    alpha=0,
                    delta=0,
                    is_split=True,
                )
            )
    surf_list.extend(vent_surf_list)

    # Create the Lamination surfaces
    point_ref = self.comp_point_ref(sym=sym)
    if sym == 1:  # Complete lamination
        ext_surf = SurfLine(label=label_ext, line_list=ext_line, point_ref=point_ref,)
        int_surf = SurfLine(label=label_int, line_list=int_line, point_ref=0)
        if self.Rint > 0 and len(ext_line) > 0:
            surf_list.append(
                SurfRing(
                    out_surf=ext_surf,
                    in_surf=int_surf,
                    label=label_lam,
                    point_ref=point_ref,
                )
            )
        elif self.Rint == 0 and len(ext_line) > 0:
            surf_list.append(ext_surf)
        else:
            pass  # No surface to draw (SlotM17)

    elif sym != 1 and len(ext_line) > 0:  # Part of the lamination by symmetry
        right_list, left_list = self.get_yoke_side_line(
            sym=sym, vent_surf_list=vent_surf_list
        )
        # Create lines
        curve_list = list()
        if self.is_internal:
            curve_list.extend(right_list)
        else:
            curve_list.extend(left_list)
        curve_list.extend(ext_line)
        if self.is_internal:
            curve_list.extend(left_list)
        else:
            curve_list.extend(right_list)
        if self.Rint > 0:
            curve_list.extend(int_line)

        surf_yoke = SurfLine(
            line_list=curve_list, label=label_lam, point_ref=point_ref,
        )
        surf_list.append(surf_yoke)

    # apply the transformation
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
