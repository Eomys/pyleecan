# -*- coding: utf-8 -*-


def get_surf(self, indices=None):
    """Return the surf object if it was already extracted, or extracts it from the mesh.

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    surf : pyvista.core.pointset.PolyData
        a pyvista polydata object
    """

    # Already available => Return
    if self.surf is not None:
        # Extract subsurface
        if indices is not None:
            surf = self.surf.extract_points(indices)
        return surf

    # Extract the outer surface of the mesh
    else:
        mesh = self.get_mesh(indices=indices)
        surf = mesh.extract_surface()

        if self.is_vtk_surf:
            surf.save(self.path_surf + "/" + self.name + ".vtk")
        else:
            self.surf = surf

        return surf
