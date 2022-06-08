# -*- coding: utf-8 -*-
from ....Classes.SurfLine import SurfLine
from ....Classes.SurfRing import SurfRing
from ....Functions.labels import (
    LAM_LAB,
    BORE_LAB,
    YOKE_LAB,
    RADIUS_PROP_LAB,
    BOUNDARY_PROP_LAB,
)

from ....Functions.Geometry.transform_hole_surf import transform_hole_surf


def build_geometry(self, sym=1, alpha=0, delta=0, is_circular_radius=False):
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
    is_circular_radius : bool
        True to add surfaces to "close" the Lamination radii

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
    yoke_prop = {RADIUS_PROP_LAB: YOKE_LAB, BOUNDARY_PROP_LAB: label_yoke}
    if self.is_internal:
        if self.Rint > 0:
            int_line = self.build_radius_lines(
                is_bore=False, sym=sym, is_reversed=True, prop_dict=yoke_prop
            )
        else:
            int_line = []
        ext_line = self.build_radius_lines(
            is_bore=True, sym=sym, prop_dict={RADIUS_PROP_LAB: BORE_LAB}
        )
    else:
        ext_line = self.build_radius_lines(
            is_bore=False, sym=sym, is_reversed=True, prop_dict=yoke_prop
        )
        int_line = self.build_radius_lines(
            is_bore=True, sym=sym, prop_dict={RADIUS_PROP_LAB: BORE_LAB}
        )

    # Add the ventilation ducts if there is any
    surf_list = list()
    vent_surf_list = list()
    if self.axial_vent not in [None, []]:
        for vent in self.axial_vent:
            kwargs = dict(alpha=0, delta=0)
            vent_list = vent.build_geometry(**kwargs)
            surf = transform_hole_surf(
                hole_surf_list=vent_list, Zh=vent.Zh, sym=sym, is_split=True, **kwargs
            )
            vent_surf_list.extend(surf)
    surf_list.extend(vent_surf_list)

    # Add the closing surfaces if requested
    if is_circular_radius:
        surf_list.extend(self.get_surfaces_closing(sym=sym))

    # Create the Lamination surfaces
    point_ref = self.comp_point_ref(sym=sym)
    if sym == 1:  # Complete lamination
        ext_surf = SurfLine(label=label_ext, line_list=ext_line, point_ref=point_ref)
        int_surf = SurfLine(label=label_int, line_list=int_line, point_ref=0)
        if self.Rint > 0 and len(ext_line) > 0:
            surf_list.insert(
                0,
                SurfRing(
                    out_surf=ext_surf,
                    in_surf=int_surf,
                    label=label_lam,
                    point_ref=point_ref,
                ),  # First in list for plot
            )
        elif self.Rint == 0 and len(ext_line) > 0:
            surf_list.insert(0, ext_surf)  # First in list for plot
        else:
            pass  # No surface to draw (SlotM17)

    elif sym != 1 and len(ext_line) > 0:  # Part of the lamination by symmetry
        # Get limit point of the yoke side
        if self.is_internal:
            ZTR = ext_line[0].get_begin()  # Top Right
            ZTL = ext_line[-1].get_end()  # Top Left
            if len(int_line) > 0:
                ZBR = int_line[-1].get_end()  # Bot Right
                ZBL = int_line[0].get_begin()  # Bot Left
            else:  # Machine without shaft for instance
                ZBR = None
                ZBL = None
        else:
            ZTR = ext_line[-1].get_end()  # Top Right
            ZTL = ext_line[0].get_begin()  # Top Left
            if len(int_line) > 0:
                ZBL = int_line[-1].get_end()  # Bot Left
                ZBR = int_line[0].get_begin()  # Bot Right
            else:  # Machine without shaft for instance
                ZBR = None
                ZBL = None
        right_list, left_list = self.build_yoke_side_line(
            sym=sym, vent_surf_list=vent_surf_list, ZBR=ZBR, ZTR=ZTR, ZBL=ZBL, ZTL=ZTL
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

        surf_yoke = SurfLine(line_list=curve_list, label=label_lam, point_ref=point_ref)
        surf_list.insert(0, surf_yoke)  # First in list for plot

    # apply the transformation
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
