# -*- coding: utf-8 -*-


from numpy import exp, linspace
from numpy import max as np_max
from numpy import min as np_min
from numpy import pi, real

from ....definitions import config_dict
from ....Functions.Plot.Pyvista.configure_plot import configure_plot
from ....Functions.Plot.Pyvista.plot_mesh_field import plot_mesh_field

COLOR_MAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]
FONT_FAMILY_PYVISTA = config_dict["PLOT"]["FONT_FAMILY_PYVISTA"]


def plot_contour(
    self,
    *args,
    label=None,
    indices=None,
    is_surf=False,
    is_radial=False,
    is_center=False,
    clim=None,
    field_name=None,
    save_path=None,
    is_show_fig=True,
    win_title=None,
    is_animated=False,
    title="",
    pv_plotter=None,
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
    save_path : str
        path to save the figure
    is_show_fig : bool
        To call show at the end of the method
    win_title : str
        Name of the window
    is_animated : bool
        True to animate magnetic flux density
    title : str
        Name of the figure
    pv_plotter : pyvista.BasePlotter
        Pyvista plotter
    colormap : str
        Name of the colormap to use (default is from config_dict)

    Returns
    -------

    """

    # Init figure
    if pv_plotter is None:
        if title != "" and win_title == "":
            win_title = title
        elif win_title != "" and title == "":
            title = win_title

        pv_plotter, sargs = configure_plot(pv_plotter=pv_plotter, win_title=win_title)

        pv_plotter.add_text(
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
        pv_plotter,
        sargs,
        field_name,
        clim=clim,
        mesh_pv=mesh_pv,
        field=field,
        colormap=colormap,
    )

    if self.dimension:
        # 2D view
        pv_plotter.view_xy()

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
                pv_plotter,
                sargs,
                field_name_B,
                clim=clim,
                mesh_pv=mesh_pv_B,
                field=field,
                phase=phase,
            )

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
            pv_plotter.show(interactive=False, screenshot=save_path)
    ############################################

    # if save_path is None and is_show_fig:
    #     pv_plotter.show()
    # elif save_path is not None:
    #     pv_plotter.show(interactive=False, screenshot=save_path)
