# -*- coding: utf-8 -*-


def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
    """
    Convert this object in a json serializable dict (can be use in __init__).
    type_handle_ndarray: int
        How to handle ndarray (0: tolist, 1: copy, 2: nothing)
    keep_function : bool
        True to keep the function object, else return str
    Optional keyword input parameter is for internal use only
    and may prevent json serializability.
    """

    # Get the properties inherited from Mesh
    MeshVTK_dict = super(type(self), self).as_dict(
        type_handle_ndarray=type_handle_ndarray, keep_function=keep_function, **kwargs
    )
    MeshVTK_dict["mesh"] = None
    MeshVTK_dict["is_pyvista_mesh"] = self.is_pyvista_mesh
    MeshVTK_dict["format"] = self.format
    MeshVTK_dict["path"] = self.path
    MeshVTK_dict["name"] = self.name
    MeshVTK_dict["surf"] = None
    MeshVTK_dict["is_vtk_surf"] = self.is_vtk_surf
    MeshVTK_dict["surf_path"] = self.surf_path
    MeshVTK_dict["surf_name"] = self.surf_name
    if self.node_normals is None:
        MeshVTK_dict["node_normals"] = None
    else:
        if type_handle_ndarray == 0:
            MeshVTK_dict["node_normals"] = self.node_normals.tolist()
        elif type_handle_ndarray == 1:
            MeshVTK_dict["node_normals"] = self.node_normals.copy()
        elif type_handle_ndarray == 2:
            MeshVTK_dict["node_normals"] = self.node_normals
        else:
            raise Exception("Unknown type_handle_ndarray: " + str(type_handle_ndarray))

    # The class name is added to the dict for deserialisation purpose
    # Overwrite the mother class name
    MeshVTK_dict["__class__"] = "MeshVTK"
    return MeshVTK_dict
