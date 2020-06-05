# -*- coding: utf-8 -*-

import numpy as np


def get_mesh(self, j_t0=0):
    """Return the mesh corresponding to a time step.

    Parameters
    ----------
    self : MeshSolution
        an MeshSolution object
    j_t0 : int
        a time step

    Returns
    -------
    mesh: Mesh
        a Mesh object

    """

    if self.is_same_mesh:
        return self.mesh[0]
    else:
        return self.mesh[j_t0]
