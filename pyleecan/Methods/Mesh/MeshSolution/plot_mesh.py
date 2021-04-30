# -*- coding: utf-8 -*-

from ....Classes.MeshMat import MeshMat


def plot_mesh(
    self,
    label=None,
    index=None,
    indices=None,
    save_path=None,
    group_names=None,
    node_label=None,
    is_show_axes=False,
    is_show_fig=True,
):
    """Plot the mesh using pyvista plotter.

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
    is_show_fig : bool
        To call show at the end of the method
    Returns
    -------
    """
    if group_names is not None:
        meshsol_grp = self.get_group(group_names)
        meshsol_grp.plot_mesh(label, index, indices, save_path, None)
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

        print(save_path)

        # Get the mesh
        mesh_obj = self.get_mesh(label=label, index=index)
        if isinstance(mesh_obj, MeshMat):
            new_mesh = mesh_obj.copy()
            new_mesh.renum()
            mesh = new_mesh.get_mesh_pv(indices=indices)
        else:
            mesh = mesh_obj.get_mesh_pv(indices=indices)

        # Configure plot
        if is_pyvistaqt:
            p = pv.BackgroundPlotter()
            p.set_background("white")
        else:
            pv.set_plot_theme("document")
            p = pv.Plotter(notebook=False)
        p.add_mesh(
            mesh,
            color="grey",
            opacity=1,
            show_edges=True,
            edge_color="white",
            line_width=1,
        )
        p.set_position((0.2, 0.2, 0.5))
        p.reset_camera()
        if is_show_axes:
            p.add_axes()
        if self.dimension == 2:
            p.view_xy()
        if save_path is None and is_show_fig:
            p.show()
        elif save_path is not None:
            p.show(interactive=False, screenshot=save_path)
