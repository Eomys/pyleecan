# -*- coding: utf-8 -*-

from ....Classes.MeshMat import MeshMat
from ....Functions.Plot.Pyvista.configure_plot import configure_plot


def plot_mesh(
    self,
    pv_plotter=None,
    indices=None,
    save_path=None,
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
    pv_plotter : a pyvista(qt) object, optional
        a pyvista object which will be used for the plot
    indices : list
        list of the nodes to extract (optional)
    save_path : str
        Path to a file where to save the figure
    is_show_axes : bool
        True to show axes
    is_show_fig : bool
        To call show at the end of the method
    is_show_grid : bool
        True to show grid
    win_title : str
        To set the name of the plot window

    Returns
    -------
    """

    if pv_plotter is None:
        pv_plotter, _ = configure_plot(
            pv_plotter=pv_plotter, win_title=win_title, is_show_axes=is_show_axes
        )
    else:
        is_show_fig = False

    # Get the mesh
    mesh_obj = self.mesh
    if isinstance(mesh_obj, MeshMat):
        new_mesh = mesh_obj.copy()
        new_mesh.renum()
        mesh = new_mesh.get_mesh_pv(indices=indices)
    else:
        mesh = mesh_obj.get_mesh_pv(indices=indices)

    pv_plotter.add_mesh(
        mesh,
        color="grey",
        opacity=1,
        show_edges=True,
        edge_color="white",
        line_width=1,
    )

    if is_show_grid:
        pv_plotter.show_grid()
    if self.dimension == 2:
        # 2D view
        pv_plotter.view_xy()
    else:
        # isometric view with z towards left
        pv_plotter.view_isometric()
        pv_plotter.camera_position = [
            pv_plotter.camera_position[0],
            (
                pv_plotter.camera_position[1][0],
                pv_plotter.camera_position[1][2],
                pv_plotter.camera_position[1][0],
            ),
            (
                pv_plotter.camera_position[2][1],
                pv_plotter.camera_position[2][2],
                pv_plotter.camera_position[2][0],
            ),
        ]
    if save_path is None and is_show_fig:
        pv_plotter.show()
    elif save_path is not None:  # and is_show_fig:
        pv_plotter.show(interactive=False, screenshot=save_path)

    return pv_plotter
