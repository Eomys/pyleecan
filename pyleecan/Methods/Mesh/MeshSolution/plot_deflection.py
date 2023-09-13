# -*- coding: utf-8 -*-

from numpy import (
    pi,
    real,
    min as np_min,
    max as np_max,
    abs as np_abs,
    linspace,
    exp,
)

from ....Classes.MeshVTK import MeshVTK

from ....definitions import config_dict
from pyleecan.Functions.Plot.Pyvista.configure_plot import configure_plot
from pyleecan.Functions.Plot.Pyvista.plot_surf_deflection import plot_surf_deflection

COLOR_MAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]
FONT_FAMILY_PYVISTA = config_dict["PLOT"]["FONT_FAMILY_PYVISTA"]


def plot_deflection(
    self,
    *args,
    label=None,
    index=None,
    indices=None,
    clim=None,
    factor=None,
    field_name=None,
    group_names=None,
    save_path=None,
    title="",
    win_title="",
    is_surf=True,
    is_show_fig=True,
    p=None,
    sargs=None,
    is_animated=False,
    phase=1,
    is_return_plot_args=False,
):
    """Plot the operational deflection shape using pyvista plotter.

    Parameters
    ----------
    self : MeshSolution
        a MeshSolution object
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
    is_show_fig : bool
        To call show at the end of the method
    p=None,
    meshsol_list=[],
    plot_list=[],

    Returns
    -------
    """
    if group_names is not None:
        meshsol_grp = self.get_group(group_names)

        meshsol_grp.plot_deflection(
            *args,
            label=label,
            index=index,
            indices=indices,
            clim=clim,
            factor=factor,
            field_name=field_name,
            save_path=save_path,
            title=title,
            win_title=win_title,
            is_surf=is_surf,
            is_show_fig=is_show_fig,
            group_names=None,
            p=p,
        )
    else:
        # Init figure
        if p is None:
            if title != "" and win_title == "":
                win_title = title
            elif win_title != "" and title == "":
                title = win_title

            p, sargs = configure_plot(p=p, win_title=win_title, save_path=save_path)

            p.add_text(
                title,
                position="upper_edge",
                color="black",
                font_size=10,
                font=FONT_FAMILY_PYVISTA,
            )

        # Get deflection
        vect_field, field_normal_amp, field_name, mesh_pv = self.get_deflection(
            *args,
            label=label,
            index=index,
            indices=indices,
            field_name=field_name,
        )

        # Compute colorbar boundaries
        if clim is None:
            clim = [np_min(real(field_normal_amp)), np_max(real(field_normal_amp))]
            if (clim[1] - clim[0]) / clim[1] < 0.01:
                clim[0] = -abs(clim[1])
                clim[1] = abs(clim[1])

        # Compute deformation factor
        if factor is None:
            factor = 0.2 * np_max(np_abs(mesh_pv.bounds)) / np_max(np_abs(vect_field))

        field_name += (
            " \n(x " + format(factor, ".3g") + " [" + self.solution[0].unit + "])"
        )

        # # Plot mesh only
        # p.add_mesh(
        #     mesh_pv, color="grey", opacity=0.7, show_edges=True, edge_color="white"
        # )

        # Extract surface
        mesh = MeshVTK(mesh=mesh_pv, is_pyvista_mesh=True)
        if is_surf:
            surf_pv = mesh.get_surf()
        else:
            surf_pv = mesh.get_mesh_pv()

        # Plot deflection surface
        plot_surf_deflection(
            surf_pv=surf_pv,
            vect_field=vect_field,
            field=field_normal_amp,
            field_name=field_name,
            p=p,
            sargs=sargs,
            clim=clim,
            factor=factor,
            phase=phase,
        )

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

                # Compute pyvista object
                plot_surf_deflection(
                    surf_pv=surf_pv,
                    vect_field=vect_field,
                    field=field_normal_amp,
                    field_name=field_name,
                    p=p,
                    sargs=sargs,
                    clim=clim,
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
            # Save figure
            if save_path is None and is_show_fig:
                p.show()
            elif save_path is not None:
                p.show(interactive=False, screenshot=save_path)

        if is_return_plot_args:
            return (
                p,
                sargs,
                surf_pv,
                vect_field,
                field_normal_amp,
                field_name,
                clim,
                factor,
                phase,
            )
        else:
            return p
