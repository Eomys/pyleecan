# -*- coding: utf-8 -*-
from numpy import pi, exp

from ....Classes.Lamination import Lamination
from ....Classes.Circle import Circle
from ....Classes.SurfLine import SurfLine
from ....Classes.SurfRing import SurfRing
from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment


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

    # Lamination label
    if self.is_stator:
        label = "Lamination_Stator"
    else:
        label = "Lamination_Rotor"

    # getting the Lamination surface
    surf_list = Lamination.build_geometry(self, sym=sym, alpha=alpha, delta=delta)

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

    return surf_list
