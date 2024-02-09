# -*- coding: utf-8 -*-

from numpy import abs as np_abs
from numpy import exp, linspace
from numpy import max as np_max
from numpy import min as np_min
from numpy import pi, real
from numpy.linalg import norm

from pyleecan.definitions import config_dict
from pyleecan.Functions.Plot.Pyvista.configure_plot import configure_plot
from pyleecan.Functions.Plot.Pyvista.plot_mesh_field import plot_mesh_field

COLOR_MAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]
FONT_FAMILY_PYVISTA = config_dict["PLOT"]["FONT_FAMILY_PYVISTA"]


def plot_B_mesh(
    self,
    *args,
    indices=None,
    is_surf=False,
    is_radial=False,
    is_center=False,
    clim=None,
    field_name=None,
    group_names=None,
    save_path=None,
    is_show_fig=True,
    win_title=None,
    is_animated=False,
    title="",
    pv_plotter=None,
    is_contour=True,
    is_2D=False
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
        field at element-centers
    clim : list
        a list of 2 elements for the limits of the colorbar
    field_name : str
        title of the field to display on plot
    group_names : list
        a list of str corresponding to group name(s)
    save_path : str
        path to save the figure
    is_show_fig : bool
        To call show at the end of the method
    is_animated : True to animate magnetic flux density
    is_2D : bool
        True plot in 2 dimensions (view on XY)

    Returns
    -------

    """
    MS_B = self.mag.meshsolution

    if group_names is not None:
        MS_B_plot = MS_B.get_group(group_names)
    else:
        MS_B_plot = MS_B

    # Init figure
    if pv_plotter is None:
        if title != "" and win_title == "":
            win_title = title
        elif win_title != "" and title == "":
            title = win_title

        pv_plotter, sargs = configure_plot(
            pv_plotter=pv_plotter,
            win_title=win_title,
        )

        pv_plotter.add_text(
            title,
            position="upper_edge",
            color="black",
            font_size=10,
            font=FONT_FAMILY_PYVISTA,
        )

    # Get the mesh_pv and field
    mesh_pv, field, field_name = MS_B_plot.get_mesh_field_pv(
        *args,
        label="B",
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
        if (clim[1] - clim[0]) / clim[1] < 0.01:
            clim[0] = -abs(clim[1])
            clim[1] = abs(clim[1])

    if is_2D:
        # 2D view
        pv_plotter.view_xy()

    plot_mesh_field(
        pv_plotter,
        sargs,
        field_name,
        clim=clim,
        mesh_pv=mesh_pv,
        field=field,
    )

    if is_contour:
        if MS_B_plot["A_z"].type_element != "node":
            raise Exception(
                "Cannot field lines if A_z calculated on nodes is not in meshsolution"
            )
        mesh_pv_Az, field_A, field_name_A = MS_B_plot.get_mesh_field_pv(
            *args,
            label="A_z",
            indices=indices,
            is_surf=is_surf,
            is_radial=is_radial,
            is_center=is_center,
            field_name=field_name,
        )
        mesh_pv_Az[field_name_A] = field_A
        contours = mesh_pv_Az.contour()
        pv_plotter.add_mesh(contours, color="black", line_width=5)

    ###########
    # Internal animation (cannot be combined with other plots)
    if is_animated:
        pv_plotter.add_text(
            'Adjust 3D view and press "Q"',
            position="lower_edge",
            color="gray",
            font_size=10,
            font="arial",
        )
        pv_plotter.show(auto_close=False)

        pv_plotter.open_gif(save_path)
        pv_plotter.clear()

        if len(args) == 0 or "time" in args:
            mesh_pv_B, field_B, field_name_B = MS_B_plot.get_mesh_field_pv(
                "time",
                label="B",
                indices=indices,
            )
            nframe = len(field_B)
            is_time = True

            if is_contour:
                mesh_pv_Az, field_A, field_name_A = MS_B_plot.get_mesh_field_pv(
                    "time",
                    label="A_z",
                    indices=indices,
                )
        else:
            nframe = 25
            mesh_pv_B, field_B, field_name_B = MS_B_plot.get_mesh_field_pv(args)
            is_time = False
            t = linspace(0.0, 1.0, nframe + 1)[:nframe]

        for i in range(nframe):
            # Compute colorbar boundaries

            if is_time:
                field = field_B[i, :]
                phase = 1
                if is_contour:
                    field_At = field_A[i, :]
            else:
                field = field_B
                phase = exp(1j * 2 * pi * t[i])

                if is_contour:
                    field_At = field_A
            # Compute pyvista object
            plot_mesh_field(
                pv_plotter,
                sargs,
                field_name_B,
                clim=clim,
                mesh_pv=mesh_pv_B,
                field=field,
                phase=phase,
            )

            if is_contour:
                mesh_pv_Az[field_name_A] = real(field_At * phase)
                contours = mesh_pv_Az.contour()
                pv_plotter.add_mesh(contours, color="black", line_width=5)

            pv_plotter.add_text(
                title,
                position="upper_edge",
                color="black",
                font_size=10,
                font="arial",
            )
            pv_plotter.write_frame()
            pv_plotter.clear()
        pv_plotter.close()

    else:
        # Save figure
        if save_path is None and is_show_fig:
            pv_plotter.show()
        elif save_path is not None:
            pv_plotter.reset_camera()
            pv_plotter.show(interactive=False, screenshot=save_path)
