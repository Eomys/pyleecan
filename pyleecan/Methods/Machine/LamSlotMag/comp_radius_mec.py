# -*- coding: utf-8 -*-

from numpy import array


def comp_radius_mec(self):
    """Compute the mechanical radius of the Lamination [m]

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object

    Returns
    -------
    Rmec: float
        Mechanical radius [m]

    """

    surf_list = list()
    for magnet in self.slot.magnet:
        surf_list.extend(magnet.build_geometry())

    # Numerical computation
    point_list = list()
    for surf in surf_list:
        point_list.extend(surf.discretize(50))
    magnet_points = array(point_list)

    if self.is_internal:  # inward Slot
        # Top radius of the magnet
        Rmec = max(self.Rext, max(abs(magnet_points)))
    else:
        Rmec = min(self.Rint, min(abs(magnet_points)))

    return Rmec
