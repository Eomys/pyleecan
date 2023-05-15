# -*- coding: utf-8 -*-


def get_mesh(self, label=None, index=None):
    """Return the mesh corresponding to label or an index.

    Parameters
    ----------
    self : MeshSolution
        an MeshSolution object
    label : str
        Label of the mesh to return
    index : int
        Index of the mesh to return

    Returns
    -------
    mesh: Mesh
        a Mesh object

    """

    if self.is_same_mesh:
        tmpmesh = self.mesh[0]
    else:
        if index is None:
            index = 0
            if label is not None:
                for i, mesh in enumerate(self.mesh):
                    if mesh.label == label:
                        index = i
        tmpmesh = self.mesh[index]

    return tmpmesh
