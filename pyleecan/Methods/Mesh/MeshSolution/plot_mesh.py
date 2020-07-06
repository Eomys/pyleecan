# -*- coding: utf-8 -*-

from ....Classes.MeshMat import MeshMat


def plot_mesh(self, label=None, index=None, indices=None, is_2d=False, save_path=None):
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

    Returns
    -------
    """

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
        mesh = mesh_obj.get_mesh_pv(indices=indices)
    else:
        mesh = mesh_obj.get_mesh(indices=indices)

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
    if is_2d:
        p.view_xy()
    if save_path is None:
        p.show()
    else:
        p.show(interactive=False, screenshot=save_path)
