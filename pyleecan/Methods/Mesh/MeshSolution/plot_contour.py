# -*- coding: utf-8 -*-

from numpy import real, min as np_min, max as np_max
from numpy.linalg import norm

from ....Classes.MeshMat import MeshMat
from ....definitions import config_dict

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
    is_show_fig : bool
        To call show at the end of the method

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
        )
    else:
        if save_path is None:
            try:
                import pyvistaqt as pv

                is_pyvistaqt = True
            except:
                import pyvista as pv

                is_pyvistaqt = False
        else:
            import pyvista as pv

            is_pyvistaqt = False

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
        if is_surf:
            surf = mesh_pv.get_surf(indices=indices)
            surf[field_name] = real(field)
            mesh_field = surf
        else:
            mesh_pv[field_name] = real(field)
            mesh_field = mesh_pv

        # Configure plot
        if is_pyvistaqt:
            p = pv.BackgroundPlotter(title=win_title)
            p.set_background("white")
        else:
            pv.set_plot_theme("document")
            p = pv.Plotter(notebook=False, title=win_title)
        sargs = dict(
            interactive=True,
            title_font_size=20,
            label_font_size=16,
            font_family=FONT_FAMILY_PYVISTA,
            color="black",
        )
        p.add_mesh(
            mesh_field,
            scalars=field_name,
            show_edges=False,
            cmap=COLOR_MAP,
            clim=clim,
            scalar_bar_args=sargs,
        )
        p.add_axes(color="k", x_color="#da3061", y_color="#0069a1", z_color="#bbcf1c")
        if self.dimension == 2:
            # 2D view
            p.view_xy()
        else:
            # isometric view with z towards left
            p.view_isometric()
            p.camera_position = [
                p.camera_position[0],
                (
                    p.camera_position[1][0],
                    p.camera_position[1][2],
                    p.camera_position[1][0],
                ),
                (
                    p.camera_position[2][1],
                    p.camera_position[2][2],
                    p.camera_position[2][0],
                ),
            ]
        if save_path is None and is_show_fig:
            p.show()
        elif save_path is not None:
            p.show(interactive=False, screenshot=save_path)
