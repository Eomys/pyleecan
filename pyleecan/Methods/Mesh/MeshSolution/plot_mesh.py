# -*- coding: utf-8 -*-

from ....Classes.MeshMat import MeshMat


def plot_mesh(
    self,
    p=None,
    label=None,
    index=None,
    indices=None,
    save_path=None,
    group_names=None,
    node_label=None,
    is_show_axes=False,
    is_show_fig=True,
    is_show_grid=False,
    win_title=None,
):
    """Plot the mesh using pyvista plotter.

    Parameters
    ----------
    self : MeshSolution
        a MeshSolution object
    p : a pyvista(qt) object, optional
        a pyvista object which will be used for the plot
    label : str
        a label
    index : int
        an index
    indices : list
        list of the points to extract (optional)
    is_show_axes : bool
        True to show axes
    is_show_fig : bool
        To call show at the end of the method
    is_show_grid : bool
        True to show grid

    Returns
    -------
    """

    if group_names is not None:
        meshsol_grp = self.get_group(group_names)
        meshsol_grp.plot_mesh(
            label=label,
            index=index,
            indices=indices,
            save_path=save_path,
            group_names=None,
        )
    else:
        if p is None:
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

            print(save_path)

            # Configure plot
            if is_pyvistaqt:
                p = pv.BackgroundPlotter(title=win_title)
                p.set_background("white")
            else:
                pv.set_plot_theme("document")
                p = pv.Plotter(notebook=False, title=win_title)
        else:
            is_show_fig = False
        # Get the mesh
        mesh_obj = self.get_mesh(label=label, index=index)
        if isinstance(mesh_obj, MeshMat):
            new_mesh = mesh_obj.copy()
            new_mesh.renum()
            mesh = new_mesh.get_mesh_pv(indices=indices)
        else:
            mesh = mesh_obj.get_mesh_pv(indices=indices)

        p.add_mesh(
            mesh,
            color="grey",
            opacity=1,
            show_edges=True,
            edge_color="white",
            line_width=1,
        )
        if is_show_axes:
            p.add_axes(
                color="k", x_color="#da3061", y_color="#0069a1", z_color="#bbcf1c"
            )
        if is_show_grid:
            p.show_grid()
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
        elif save_path is not None:  # and is_show_fig:
            p.show(interactive=False, screenshot=save_path)

    return p
