# -*- coding: utf-8 -*-

from ....Functions.Structural.conversions import pol2cart


def get_shape_xyz(self):
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

    if self.shape_xyz is not None and self.shape_xyz.size != 0:
        return self.shape_xyz
    else:
        shape_pol = self.shape_pol
        points = self.parent.mesh.get_points()
        return pol2cart(shape_pol, points)
