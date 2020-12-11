# -*- coding: utf-8 -*-

from ....Functions.Structural.conversions import cart2pol


def get_shape_pol(self):
    """Return the mode shape in cartesian coordinates.

    Parameters
    ----------
    self : Mode
        a Mode object

    Returns
    -------
    shape : ndarray
        ndarray of the shape (Nnodes*Ndof)
    """

    if self.shape_pol is not None and self.shape_pol.size != 0:
        return self.shape_pol
    else:
        shape_xyz = self.shape_xyz
        points = self.parent.mesh.get_points()
        return cart2pol(shape_xyz, points)
