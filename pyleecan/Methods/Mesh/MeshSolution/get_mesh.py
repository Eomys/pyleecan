# -*- coding: utf-8 -*-


def get_mesh(self, label=None, index=None):
    """Return the mesh corresponding to label or an index.

    Parameters
    ----------
    self : MeshSolution
        an MeshSolution object
    label : str
        a label
    index : int
        an index

    Returns
    -------
    mesh: Mesh
        a Mesh object

    """

    if self.is_same_mesh:
        return self.mesh[0]
    else:
        if index is None:
            index = 0
            if label is not None:
                for i, solution in enumerate(self.solution):
                    if solution.label == label:
                        index = i
        return self.mesh[index]
