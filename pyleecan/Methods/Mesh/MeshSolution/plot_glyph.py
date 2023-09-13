# -*- coding: utf-8 -*-

from ....Functions.Plot.Pyvista.plot_glyph_pv import plot_glyph_pv
from ....Functions.Plot.Pyvista.configure_plot import configure_plot
from numpy import (
    pi,
    max as np_max,
    abs as np_abs,
    linspace,
    exp,
)

from ....Classes.MeshMat import MeshMat
from ....definitions import config_dict

FONT_FAMILY_PYVISTA = config_dict["PLOT"]["FONT_FAMILY_PYVISTA"]


def plot_glyph(
    self,
    *args,
    label=None,
    index=None,
    indices=None,
    clim=None,
    factor=None,
    field_name=None,
    save_path=None,
    is_point_arrow=False,
    group_names=None,
    is_show_fig=True,
    p=None,
    enforced_mesh=None,
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
        a label
    index : int
        an index
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
    group_names : [str]
        plot is restricted to the group(s) corresponding to this list of group names.
    p : pyvista
        a pyvista object
    enforced_mesh : Mesh
        enforced Mesh object


    Returns
    -------
    """
    if group_names is not None:
        meshsol_grp = self.get_group(group_names)
        meshsol_grp.plot_glyph(
            *args,
            label=label,
            index=index,
            indices=indices,
            clim=clim,
            factor=factor,
            field_name=field_name,
            save_path=save_path,
            is_point_arrow=is_point_arrow,
            group_names=None,
            p=p,
            enforced_mesh=enforced_mesh,
        )
    else:
        # Init figure
        if p is None:
            if title != "" and win_title == "":
                win_title = title
            elif win_title != "" and title == "":
                title = win_title

            p, _ = configure_plot(p=p, win_title=win_title, save_path=save_path)

            p.add_text(
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
            index=index,
            indices=indices,
            field_name=field_name,
        )

        # Compute factor
        if factor is None:
            factor = 0.2 * np_max(np_abs(mesh_pv.bounds)) / np_max(np_abs(vect_field))

        # field_name += (
        #     " \n(x " + format(factor, ".3g") + " [" + self.solution[0].unit + "])"
        # )

        # Plot mesh
        p.add_mesh(
            mesh_pv, color="grey", opacity=0.7, show_edges=True, edge_color="white"
        )

        # Add field to mesh
        plot_glyph_pv(
            p=p,
            mesh_pv=mesh_pv,
            vect_field=vect_field,
            is_point_arrow=is_point_arrow,
            factor=factor,
            phase=phase,
        )

        if is_2D:
            p.view_xy()

        # Internal animation (cannot be combined with other plots)
        if is_animated:
            p.add_text(
                'Adjust 3D view and press "Q"',
                position="lower_edge",
                color="gray",
                font_size=10,
                font=FONT_FAMILY_PYVISTA,
            )
            p.show(auto_close=False)

            nframe = 25
            p.open_gif(save_path)
            p.clear()
            for t in linspace(0.0, 1.0, nframe + 1)[:nframe]:
                phase = exp(1j * 2 * pi * t)

                p.add_mesh(
                    mesh_pv,
                    color="grey",
                    opacity=0.7,
                    show_edges=True,
                    edge_color="white",
                )

                # Compute pyvista object
                plot_glyph_pv(
                    p=p,
                    mesh_pv=mesh_pv,
                    vect_field=vect_field,
                    is_point_arrow=is_point_arrow,
                    factor=factor,
                    phase=phase,
                )

                p.add_text(
                    title,
                    position="upper_edge",
                    color="black",
                    font_size=10,
                    font=FONT_FAMILY_PYVISTA,
                )
                p.write_frame()
                p.clear()

            p.close()
        else:
            if save_path is None and is_show_fig:
                p.show()
            elif save_path is not None:
                p.show(interactive=False, screenshot=save_path)

        if is_return_plot_args:
            return p, mesh_pv, vect_field, is_point_arrow, factor, phase
        else:
            return p
