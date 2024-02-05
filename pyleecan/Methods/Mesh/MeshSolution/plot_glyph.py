# -*- coding: utf-8 -*-

from numpy import abs as np_abs
from numpy import exp, linspace
from numpy import max as np_max
from numpy import pi

from ....definitions import config_dict
from ....Functions.Plot.Pyvista.configure_plot import configure_plot
from ....Functions.Plot.Pyvista.plot_glyph_pv import plot_glyph_pv

FONT_FAMILY_PYVISTA = config_dict["PLOT"]["FONT_FAMILY_PYVISTA"]


def plot_glyph(
    self,
    *args,
    label=None,
    indices=None,
    factor=None,
    field_name=None,
    save_path=None,
    is_point_arrow=False,
    is_show_fig=True,
    pv_plotter=None,
    win_title="",
    title="",
    is_animated=False,
    phase=1,
    is_return_plot_args=False,
):
    """Plot the vector field as a glyph (or quiver) over the mesh.

    Parameters
    ----------
    self : MeshSolution
        a MeshSolution object
    *args: list of strings
        List of axes requested by the user, their units and values (optional)
    label : str
        label of the solution to plot
    indices : list
        list of the points to extract (optional)
    clim : list
        a list of 2 elements for the limits of the colorbar
    factor : float
        factor to multiply vector field
    field_name : str
        title of the field to display on plot
    save_path : str
        path to save the plot into an image
    is_point_arrow : bool
        to plot a nodal field (point-wise solution required)
    pv_plotter : pyvista
        a pyvista object
    enforced_mesh : Mesh
        enforced Mesh object


    Returns
    -------
    """
    # Init figure
    if pv_plotter is None:
        if title != "" and win_title == "":
            win_title = title
        elif win_title != "" and title == "":
            title = win_title

        pv_plotter, _ = configure_plot(pv_plotter=pv_plotter, win_title=win_title)

        pv_plotter.add_text(
            title,
            position="upper_edge",
            color="black",
            font_size=10,
            font=FONT_FAMILY_PYVISTA,
        )

    # Get glyph field
    vect_field, field_name, mesh_pv, is_2D = self.get_glyph(
        *args,
        label=label,
        indices=indices,
        field_name=field_name,
    )

    # Compute factor
    if factor is None:
        factor = 0.2 * np_max(np_abs(mesh_pv.bounds)) / np_max(np_abs(vect_field))

    # Plot mesh
    pv_plotter.add_mesh(
        mesh_pv, color="grey", opacity=0.7, show_edges=True, edge_color="white"
    )

    # Add field to mesh
    plot_glyph_pv(
        pv_plotter=pv_plotter,
        mesh_pv=mesh_pv,
        vect_field=vect_field,
        is_point_arrow=is_point_arrow,
        factor=factor,
        phase=phase,
    )

    if is_2D:
        pv_plotter.view_xy()

    # Internal animation (cannot be combined with other plots)
    if is_animated:
        pv_plotter.add_text(
            'Adjust 3D view and press "Q"',
            position="lower_edge",
            color="gray",
            font_size=10,
            font=FONT_FAMILY_PYVISTA,
        )
        pv_plotter.show(auto_close=False)

        nframe = 25
        pv_plotter.open_gif(save_path)
        pv_plotter.clear()
        for t in linspace(0.0, 1.0, nframe, endpoint=False):
            phase = exp(1j * 2 * pi * t)

            pv_plotter.add_mesh(
                mesh_pv,
                color="grey",
                opacity=0.7,
                show_edges=True,
                edge_color="white",
            )

            # Compute pyvista object
            plot_glyph_pv(
                pv_plotter=pv_plotter,
                mesh_pv=mesh_pv,
                vect_field=vect_field,
                is_point_arrow=is_point_arrow,
                factor=factor,
                phase=phase,
            )

            pv_plotter.add_text(
                title,
                position="upper_edge",
                color="black",
                font_size=10,
                font=FONT_FAMILY_PYVISTA,
            )
            pv_plotter.write_frame()
            pv_plotter.clear()

        pv_plotter.close()
    else:
        if save_path is None and is_show_fig:
            pv_plotter.show()
        elif save_path is not None:
            pv_plotter.show(interactive=False, screenshot=save_path)

    if is_return_plot_args:
        return pv_plotter, mesh_pv, vect_field, is_point_arrow, factor, phase
    else:
        return pv_plotter
