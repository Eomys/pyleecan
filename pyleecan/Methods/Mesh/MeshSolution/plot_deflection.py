# -*- coding: utf-8 -*-

from numpy import real, min as np_min, max as np_max, zeros, hstack

from ....Classes.MeshMat import MeshMat
from ....Classes.MeshVTK import MeshVTK
from ....definitions import config_dict

COLOR_MAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]


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
    win_title=None,
    is_surf=True,
    is_show_fig=True,
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

        if title != "" and win_title == "":
            win_title = title
        elif win_title != "" and title == "":
            title = win_title

        # Get mesh and field
        mesh_pv, field, field_name = self.get_mesh_field_pv(
            *args,
            label=label,
            index=index,
            indices=indices,
            field_name=field_name,
            is_radial=True,
        )
        mesh = MeshVTK(mesh=mesh_pv, is_pyvista_mesh=True)
        _, vect_field, _ = self.get_mesh_field_pv(
            *args,
            label=label,
            index=index,
            indices=indices,
            field_name=field_name,
            is_radial=False,
        )

        if field_name is None:
            if label is not None:
                field_name = label
            elif self.get_solution(index=index).label is not None:
                field_name = self.get_solution(index=index).label
            else:
                field_name = "Field"

        # Compute colorbar boundaries
        if clim is None:
            clim = [np_min(real(field)), np_max(real(field))]
            if (clim[1] - clim[0]) / clim[1] < 0.01:
                clim[0] = -abs(clim[1])
                clim[1] = abs(clim[1])

        # Compute deformation factor
        if factor is None:
            # factor = 1 / (100 * clim[1])
            factor = 1 / clim[1] * 10

        # Add third dimension if needed
        solution = self.get_solution(
            label=label,
            index=index,
        )
        if solution.dimension == 2:
            vect_field = hstack((vect_field, zeros((vect_field.shape[0], 1))))

        # Extract surface
        if is_surf:
            surf = mesh.get_surf(indices=indices)
        else:
            surf = mesh.get_mesh_pv(indices=indices)

        # Add field to surf
        surf.vectors = real(vect_field) * factor

        # Warp by vectors
        surf_warp = surf.warp_by_vector()

        # Add radial field
        surf_warp[field_name] = real(field)

        # Configure plot
        if is_pyvistaqt:
            p = pv.BackgroundPlotter()
            p.set_background("white")
        else:
            pv.set_plot_theme("document")
            p = pv.Plotter(notebook=False, title=win_title)
        sargs = dict(
            interactive=True,
            title_font_size=20,
            label_font_size=16,
            font_family="arial",
            color="black",
        )
        p.add_mesh(
            mesh_pv, color="grey", opacity=1, show_edges=True, edge_color="white"
        )
        p.set_position((0.2, 0.2, 0.5))
        p.reset_camera()
        p.clear()
        p.add_mesh(
            surf_warp,
            scalars=field_name,
            opacity=1,
            show_edges=False,
            cmap=COLOR_MAP,
            clim=clim,
            scalar_bar_args=sargs,
        )
        p.add_text(title, position="upper_edge")
        p.add_axes()
        if self.dimension == 2:
            p.view_xy()
        if save_path is None and is_show_fig:
            p.show()
        elif save_path is not None:
            p.show(interactive=False, screenshot=save_path)
