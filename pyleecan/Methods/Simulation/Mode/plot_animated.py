# -*- coding: utf-8 -*-

from numpy import max as np_max, min as np_min


def plot_animated(self, i):
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
    shape_xyz = self.get_shape_xyz()
    clim = [np_min(radial_shape), np_max(radial_shape)]
    self.parent.mesh.plot_deformation_animated(
        shape_xyz,
        radial_shape,
        factor=0.05,
        field_name="Radial displacement",
        clim=clim,
    )
