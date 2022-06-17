# -*- coding: utf-8 -*-
from numpy import pi
from ....Classes.LamSquirrelCage import LamSquirrelCage
from ....Functions.labels import HOLEV_LAB, HOLEM_LAB, update_RTS_index


def build_geometry(self, sym=1, alpha=0, delta=0, is_circular_radius=False):
    """Build geometry of the LamSquirrelCage

    Parameters
    ----------
    self : LamSquirrelCageMag
        A LamSquirrelCageMag Object
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
    surf_list: list
        list of surfaces

    """

    # Lamination label
    if self.is_stator:
        label = "Lamination_Stator"
    else:
        label = "Lamination_Rotor"

    surf_list = LamSquirrelCage.build_geometry(
        self, sym=sym, is_circular_radius=is_circular_radius, alpha=alpha, delta=delta
    )

    # Holes surface(s)
    for hole in self.get_hole_list():
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

        hole_surf_list = list()
        # Copy the hole for Zh / sym
        for ii in range(Zh // sym):
            for surf in surf_hole:
                new_surf = type(surf)(init_dict=surf.as_dict())
                new_surf.label = update_RTS_index(label=new_surf.label, S_id=ii)
                new_surf.rotate(ii * angle)
                hole_surf_list.append(new_surf)

    # Apply the transformations
    for surf in hole_surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    surf_list.extend(hole_surf_list)
    return surf_list
