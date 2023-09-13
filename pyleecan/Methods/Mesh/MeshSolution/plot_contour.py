# -*- coding: utf-8 -*-

from numpy import real, min as np_min, max as np_max
from numpy.linalg import norm

from ....Classes.MeshMat import MeshMat
from ....definitions import config_dict

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

from pyleecan.Functions.Plot.Pyvista.configure_plot import configure_plot
from pyleecan.Functions.Plot.Pyvista.plot_surf_deflection import plot_surf_deflection
from pyleecan.Functions.Plot.Pyvista.plot_mesh_field import plot_mesh_field

COLOR_MAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]
FONT_FAMILY_PYVISTA = config_dict["PLOT"]["FONT_FAMILY_PYVISTA"]


def plot_contour(
    self,
    *args,
    label=None,
    index=None,
    indices=None,
    is_surf=False,
    is_radial=False,
    is_center=False,
    clim=None,
    field_name=None,
    group_names=None,
    save_path=None,
    itimefreq=0,
    is_show_fig=True,
    win_title=None,
    factor=None,
    is_animated=False,
    title="",
    p=None,
    colormap=COLOR_MAP
):
    """Plot the contour of a field on a mesh using pyvista plotter.

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
    is_surf : bool
        field over outer surface
    is_radial : bool
        radial component only
    is_center : bool
        field at cell-centers
    clim : list
        a list of 2 elements for the limits of the colorbar
    field_name : str
        title of the field to display on plot
    group_names : list
        a list of str corresponding to group name(s)
    save_path : str
        path to save the figure
    itimefreq : int
        if the field depends has a time/freqs axis, return the timefreq-th slice.
    is_show_fig : bool
        To call show at the end of the method
    win_title : str
        Name of the window
    factor : float
        Normalization factor
    is_animated : bool
        True to animate magnetic flux density
    title : str
        Name of the figure
    p : ?
        Pyvista plotter
    colormap : str
        Name of the colormap to use (default is from config_dict)

    Returns
    -------

    """
    if group_names is not None:
        meshsol_grp = self.get_group(group_names)
        meshsol_grp.plot_contour(
            *args,
            label=label,
            index=index,
            indices=indices,
            is_surf=is_surf,
            is_radial=is_radial,
            is_center=is_center,
            clim=clim,
            field_name=field_name,
            group_names=None,
            save_path=save_path,
            itimefreq=itimefreq,
            is_animated=is_animated,
            title=title,
            colormap=colormap,
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

        # Get the mesh_pv and field
        mesh_pv, field, field_name = self.get_mesh_field_pv(
            *args,
            label=label,
            index=index,
            indices=indices,
            is_surf=is_surf,
            is_radial=is_radial,
            is_center=is_center,
            field_name=field_name,
        )

        # Add field to mesh
        # if is_surf:
        #     surf = mesh_pv.get_surf(indices=indices)
        #     surf[field_name] = real(field)
        #     mesh_field = surf
        # else:
        #     mesh_pv[field_name] = real(field)
        #     mesh_field = mesh_pv
        if clim is None:
            clim = [np_min(real(field)), np_max(real(field))]
            if abs((clim[1] - clim[0]) / clim[1]) < 0.01:
                clim[0] = -abs(clim[1])
                clim[1] = abs(clim[1])

        plot_mesh_field(
            p,
            sargs,
            field_name,
            clim=clim,
            mesh_pv=mesh_pv,
            field=field,
            colormap=colormap,
        )

        ###########
        # Internal animation (cannot be combined with other plots)
        if is_animated:
            p.add_text(
                'Adjust 3D view and press "Q"',
                position="lower_edge",
                color="gray",
                font_size=10,
                font="arial",
            )
            p.show(auto_close=False)

            p.open_gif(save_path)
            p.clear()

            if len(args) == 0 or "time" in args:
                mesh_pv_B, field_B, field_name_B = self.get_mesh_field_pv("time")
                nframe = len(field_B)
                is_time = True
            else:
                nframe = 25
                mesh_pv_B, field_B, field_name_B = self.get_mesh_field_pv(args)
                is_time = False
                t = linspace(0.0, 1.0, nframe + 1)[:nframe]

            for i in range(nframe):
                # Compute colorbar boundaries

                if is_time:
                    field = field_B[i, :]
                    phase = 1
                else:
                    field = field_B
                    phase = exp(1j * 2 * pi * t[i])
                # Compute pyvista object
                plot_mesh_field(
                    p,
                    sargs,
                    field_name_B,
                    clim=clim,
                    mesh_pv=mesh_pv_B,
                    field=field,
                    phase=phase,
                )

                p.add_text(
                    title,
                    position="upper_edge",
                    color="black",
                    font_size=10,
                    font="arial",
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
    ############################################

    # if save_path is None and is_show_fig:
    #     p.show()
    # elif save_path is not None:
    #     p.show(interactive=False, screenshot=save_path)
