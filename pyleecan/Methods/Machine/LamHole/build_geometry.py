# -*- coding: utf-8 -*-
from numpy import pi, exp

from ....Classes.Lamination import Lamination
from ....Classes.Circle import Circle
from ....Classes.SurfLine import SurfLine
from ....Classes.SurfRing import SurfRing
from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Functions.labels import update_RTS_index
from ....Functions.Geometry.transform_hole_surf import transform_hole_surf


def build_geometry(self, sym=1, alpha=0, delta=0, is_circular_radius=False):
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
    is_circular_radius : bool
        True to add surfaces to "close" the Lamination radii

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the lamination

    """

    # getting the Lamination surface
    surf_list = Lamination.build_geometry(
        self, sym=sym, alpha=alpha, delta=delta, is_circular_radius=is_circular_radius
    )

    # Holes surface(s)
    for hole in self.hole:
        # Create the first hole surface(s)
        surf_hole = hole.build_geometry(alpha=pi / hole.Zh)
        surf_list.extend(
            transform_hole_surf(
                hole_surf_list=surf_hole, Zh=hole.Zh, sym=sym, alpha=0, delta=0
            )
        )

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
