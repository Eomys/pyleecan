# -*- coding: utf-8 -*-


from numpy import (
    real,
    min as np_min,
    max as np_max,
    abs as np_abs,
)


from ....definitions import config_dict

COLOR_MAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]


def plot_surf_deflection(
    p,
    sargs,
    surf_pv,
    vect_field,
    field,
    field_name,
    clim=None,
    factor=None,
    phase=1,
):
    """Plot the operational deflection shape using pyvista plotter. Made to be called from plot_pyvista.

    Parameters
    ----------

    clim : list
        a list of 2 elements for the limits of the colorbar
    factor : float
        factor to multiply vector field
    field_name : str
        title of the field to display on plot
    is_show_fig : bool
        To call show at the end of the method
    p=None,
    meshsol_list=[],
    plot_list=[],

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
    surf_pv.vectors = real(vect_field * phase) * factor

    # Warp by vectors
    surf_warp = surf_pv.warp_by_vector()

    # Add normal field amplitude for colormap
    surf_warp[field_name] = real(field * phase)

    # Plot mesh
    p.add_mesh(surf_pv, color="grey", opacity=0.7, show_edges=True, edge_color="white")

    # Plot deflection
    p.add_mesh(
        surf_warp,
        scalars=field_name,
        opacity=1,
        show_edges=False,
        cmap=COLOR_MAP,
        clim=clim,
        scalar_bar_args=sargs,
    )
