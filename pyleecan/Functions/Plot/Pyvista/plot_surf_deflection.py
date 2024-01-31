# -*- coding: utf-8 -*-

from numpy import abs as np_abs
from numpy import max as np_max
from numpy import min as np_min
from numpy import real

from ....definitions import config_dict

COLOR_MAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]


def plot_surf_deflection(
    pv_plotter,
    sargs,
    surf_pv,
    vect_field,
    field,
    field_name,
    clim=None,
    factor=None,
    phase=1,
):
    """Plot a vector field as arrow (or glyph) using pyvista plotter.

    Parameters
    ----------
    pv_plotter : pyvista.Plotter
        a pyvista plotting object
    *sargs: list of strings
        List of arguments for the scalar bar
    surf_pv : UnstructuredGrid
        a pyvista surface mesh object
    vect_field : ndaray
        field to plot
    field : ndarray
        a vector field to plot as glyph
    field_name : str
        name of the field
    clim : list
        a list of 2 elements for the limits of the colorbar
    factor : float
        amplitude factor for vector field
    phase : complex
        coefficient to change the phase of the plot

    Returns
    -------
    """

    # Compute colorbar boundaries
    if clim is None:
        clim = [np_min(real(field)), np_max(real(field))]
        if (clim[1] - clim[0]) / clim[1] < 0.01:
            clim[0] = -abs(clim[1])
            clim[1] = abs(clim[1])

    # Compute deformation factor
    if factor is None:
        factor = 0.2 * np_max(np_abs(surf_pv.bounds)) / np_max(np_abs(vect_field))

    # Compute pyvista object
    # Add field to surf
    surf_pv.point_data[field_name] = real(vect_field * phase) * factor
    surf_pv.active_vectors_name = field_name

    # Warp by vectors
    surf_warp = surf_pv.warp_by_vector()

    # Add normal field amplitude for colormap
    surf_warp[field_name] = real(field * phase)

    # Plot mesh
    pv_plotter.add_mesh(
        surf_pv, color="grey", opacity=0.7, show_edges=True, edge_color="white"
    )

    # Plot deflection
    pv_plotter.add_mesh(
        surf_warp,
        scalars=field_name,
        opacity=1,
        show_edges=False,
        cmap=COLOR_MAP,
        clim=clim,
        scalar_bar_args=sargs,
    )
