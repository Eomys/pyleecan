# -*- coding: utf-8 -*-

from numpy import real, min as np_min, max as np_max

from ....Classes.MeshMat import MeshMat
from ....Classes.MeshVTK import MeshVTK
from ....definitions import config_dict

COLOR_MAP = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]


def plot_deflection(
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
        mesh = MeshVTK(mesh=mesh_pv, is_pyvista_mesh=True)

    # Get the field
    field = real(
        self.get_field(
            label=label, index=index, indices=indices, is_surf=True, is_radial=True
        )
    )
    vect_field = real(self.get_field(label=label, index=index, indices=indices))
    if len(field.shape) == 2:
        # Third dimension is frequencies
        field = field[:, ifreq]
        vect_field = vect_field[:, :, ifreq]
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
            clim[0] = -clim[1]

    # Compute deformation factor
    if factor is None:
        factor = 1 / (100 * clim[1])

    # Extract surface
    surf = mesh.get_surf(indices=indices)

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
        p = pv.Plotter(notebook=False)
    sargs = dict(
        interactive=True,
        title_font_size=20,
        label_font_size=16,
        font_family="arial",
        color="black",
    )
    p.add_mesh(
        surf_warp,
        scalars=field_name,
        opacity=1,
        show_edges=False,
        cmap=COLOR_MAP,
        clim=clim,
        scalar_bar_args=sargs,
    )
    if is_2d:
        p.view_xy()
    if save_path is None:
        p.show()
    else:
        p.show(interactive=False, screenshot=save_path)
