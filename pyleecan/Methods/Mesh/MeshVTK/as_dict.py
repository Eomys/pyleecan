# -*- coding: utf-8 -*-


def as_dict(self):
    """Convert this object in a json seriable dict (can be use in __init__)"""

    # Get the properties inherited from Mesh
    MeshVTK_dict = super(MeshVTK, self).as_dict()
    MeshVTK_dict["mesh"] = None
    MeshVTK_dict["is_pyvista_mesh"] = self.is_pyvista_mesh
    MeshVTK_dict["format"] = self.format
    MeshVTK_dict["path"] = self.path
    MeshVTK_dict["name"] = self.name
    MeshVTK_dict["surf"] = None
    MeshVTK_dict["is_vtk_surf"] = self.is_vtk_surf
    MeshVTK_dict["surf_path"] = self.surf_path
    MeshVTK_dict["surf_name"] = self.surf_name
    # The class name is added to the dict for deserialisation purpose
    # Overwrite the mother class name
    MeshVTK_dict["__class__"] = "MeshVTK"
    return MeshVTK_dict
