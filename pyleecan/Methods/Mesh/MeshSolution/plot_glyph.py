# -*- coding: utf-8 -*-

from numpy import real, max as np_max

from ....Classes.MeshMat import MeshMat


def plot_glyph(
    self,
    label=None,
    index=None,
    indices=None,
    clim=None,
    factor=None,
    field_name=None,
    ifreq=0,
    is_2d=False,
    save_path=None,
):
    """Plot the vector field as a glyph (or quiver) over the mesh.

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
    ifreq : int
        index of the frequency to use for plot (if exists)

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

    # Get the mesh
    mesh = self.get_mesh(label=label, index=index)
    if isinstance(mesh, MeshMat):
        mesh_pv = mesh.get_mesh_pv(indices=indices)
    else:
        mesh_pv = mesh.get_mesh(indices=indices)

    # Get the vector field
    vect_field = real(self.get_field(label=label, index=index, indices=indices))
    if len(vect_field.shape) == 3:
        # Third dimension is frequencies
        vect_field = vect_field[:, :, ifreq]

    # Compute factor
    if factor is None:
        factor = 1 / (100 * np_max(vect_field))

    # Add field to mesh
    mesh_pv["field"] = vect_field
    mesh_cell = mesh_pv.point_data_to_cell_data()
    surf = mesh_cell.extract_geometry()
    centers2 = surf.cell_centers()
    centers2.vectors = surf["field"] * factor

    # Configure plot
    if is_pyvistaqt:
        p = pv.BackgroundPlotter()
        p.set_background("white")
    else:
        pv.set_plot_theme("document")
        p = pv.Plotter(notebook=False)
    p.add_mesh(
        mesh_pv, color="grey", opacity=0.7, show_edges=True, edge_color="white",
    )
    p.add_mesh(centers2.arrows, color="white")
    if is_2d:
        p.view_xy()
    if save_path is None:
        p.show()
    else:
        p.show(interactive=False, screenshot=save_path)
