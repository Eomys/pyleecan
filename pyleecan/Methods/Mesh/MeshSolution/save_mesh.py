# -*- coding: utf-8 -*-
from scipy.io import savemat


def save_mesh(self, save_path):
    """Save mesh to a .mat file

    Parameters
    ----------
    self : MeshSolution
        an MeshSolution object
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None

    """

    # dict to save
    mesh_dict = dict()

    for nb_mesh in range(self.mesh):
        mesh_dict[f"{self.mesh[nb_mesh].label}"] = self.mesh[nb_mesh].node.coordinate

    # Save result
    savemat(save_path, mesh_dict)
