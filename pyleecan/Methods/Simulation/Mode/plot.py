# -*- coding: utf-8 -*-

from numpy import max as np_max, min as np_min


def plot(self, i):
    """Return the pyvista mesh object.

    Parameters
    ----------
    self : Mode
        a Mode object
    i : int
        index of the mode to plot

    Returns
    -------
    mesh : pyvista.core.pointset.StructuredGrid
        a pyvista StructuredGrid object
    """

    radial_shape = self.get_shape_pol()[:, 0]
    clim = [np_min(radial_shape), np_max(radial_shape)]
    self.parent.mesh.plot_contour(
        radial_shape, field_name="Radial displacement", clim=clim
    )
