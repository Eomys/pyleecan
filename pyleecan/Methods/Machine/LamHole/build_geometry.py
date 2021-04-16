# -*- coding: utf-8 -*-
from numpy import pi, exp

from ....Classes.Circle import Circle
from ....Classes.SurfLine import SurfLine
from ....Classes.SurfRing import SurfRing
from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Functions.labels import LAM_LAB, BORE_LAB, YOKE_LAB


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

    # Label setup
    label = self.get_label()
    label_lam = label + "_" + LAM_LAB
    label_bore = label + "_" + BORE_LAB
    label_yoke = label + "_" + YOKE_LAB

    if self.is_internal:
        Ryoke = self.Rint
        Rbo = self.Rext
    else:
        Ryoke = self.Rext
        Rbo = self.Rint

    ref_point = self.comp_radius_mid_yoke() * exp(1j * pi / sym)

    surf_list = list()
    # Lamination surface(s)
    if sym == 1:  # Complete lamination
        if self.bore is None:
            bore_surf = SurfLine(
                line_list=self.get_bore_line(0, 2 * pi, label=label_bore),
                label=label_bore,
                point_ref=ref_point,
            )
        else:
            bore_surf = SurfLine(
                line_list=self.bore.get_bore_line(label=label_bore),
                label=label_bore,
                point_ref=ref_point,
            )
        yoke_surf = Circle(
            radius=Ryoke, label=label_yoke, point_ref=0, center=0, line_label=label_yoke
        )
        if Ryoke > 0:
            if self.is_internal:
                surf_list.append(
                    SurfRing(
                        out_surf=bore_surf,
                        in_surf=yoke_surf,
                        label=label_lam,
                        point_ref=ref_point,
                    )
                )
            else:
                surf_list.append(
                    SurfRing(
                        out_surf=yoke_surf,
                        in_surf=bore_surf,
                        label=label_lam,
                        point_ref=ref_point,
                    )
                )
        else:
            bore_surf.label = label_lam
            surf_list.append(bore_surf)

    else:  # Symmetry lamination
        alpha_begin = 0
        alpha_end = 2 * pi / sym
        begin = Rbo * exp(1j * alpha_begin)
        end = Rbo * exp(1j * alpha_end)
        Z_begin = Ryoke * exp(1j * alpha_begin)
        Z_end = Ryoke * exp(1j * alpha_end)
        line_list = [Segment(Z_begin, begin, label=label + "_Yoke_Side_Right")]
        bore_line = self.get_bore_line(alpha_begin, alpha_end, label=label_bore)
        for line in bore_line:
            line_list.append(line)
        line_list.append(Segment(end, Z_end, label=label + "_Yoke_Side_Left"))
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
            SurfLine(line_list=line_list, label=label_lam, point_ref=ref_point)
        )

    # Holes surface(s)
    for hole in self.hole:
        Zh = hole.Zh
        assert (Zh % sym) == 0, (
            "ERROR, Wrong symmetry for "
            + label
            + " "
            + str(Zh)
            + " holes and sym="
            + str(sym)
        )  # For now only
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
