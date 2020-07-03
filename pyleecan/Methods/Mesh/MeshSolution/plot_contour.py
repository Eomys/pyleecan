# -*- coding: utf-8 -*-

try:
    import pyvistaqt as pv
    is_pyvistaqt = True
except:
    import pyvista as pv
    is_pyvistaqt = False
from numpy import min as np_min, max as np_max

from ....Classes.MeshMat import MeshMat
from ....definitions import config_dict

COLOR_MAP = config_dict["color_dict"]["COLOR_MAP"]


def plot_contour(
    self,
    label=None,
    index=None,
    indices=None,
    is_surf=False,
    is_radial=False,
    is_center=False,
    clim=None,
    field_name=None,
):
    """Plot the contour of a field on a mesh using pyvista plotter.

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

    Returns
    -------
    """

    # Get the mesh
    mesh = self.get_mesh(label=label, index=index)
    if isinstance(mesh, MeshMat):
        mesh_pv = mesh.get_mesh_pv(indices=indices)
    else:
        mesh_pv = mesh.get_mesh(indices=indices)

    # Get the field
    field = self.get_field(
        label=label,
        index=index,
        indices=indices,
        is_surf=is_surf,
        is_radial=is_radial,
        is_center=is_center,
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
        clim = [np_min(field), np_max(field)]

    # Add field to mesh
    if is_surf:
        surf = mesh_pv.get_surf(indices=indices)
        surf[field_name] = field
        mesh_field = surf
    else:
        mesh_pv[field_name] = field
        mesh_field = mesh_pv

    # Configure plot
    if is_pyvistaqt:
        p = pv.BackgroundPlotter()
        p.set_background("white")
    else:
        pv.set_plot_theme("document")
        p = pv.Plotter(notebook=False)
    sargs = dict(
        interactive=True,
        title_font_size=20,
        label_font_size=16,
        font_family="arial",
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
    p.show()
