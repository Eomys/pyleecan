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
                    label=label_lam,
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
            curve_list.append(
                Segment(Z0, Z1, prop_dict={BOUNDARY_PROP_LAB: label + "_" + YSR_LAB})
            )
        else:
            curve_list.append(
                Segment(Z3, Z2, prop_dict={BOUNDARY_PROP_LAB: label + "_" + YSL_LAB})
            )
        curve_list.extend(ext_line)
        if self.is_internal:
            curve_list.append(
                Segment(Z2, Z3, prop_dict={BOUNDARY_PROP_LAB: label + "_" + YSL_LAB})
            )
        else:
            curve_list.append(
                Segment(Z1, Z0, prop_dict={BOUNDARY_PROP_LAB: label + "_" + YSR_LAB})
            )
        if self.Rint > 0:
            curve_list.extend(int_line)

        surf_yoke = SurfLine(
            line_list=curve_list,
            label=label_lam,
            point_ref=point_ref,
        )
        surf_list.append(surf_yoke)

    # Add the ventilation ducts if there is any
    for vent in self.axial_vent:
        surf_list.extend(vent.build_geometry(sym=sym))

    # apply the transformation
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
