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
    mesh_dict["mesh"] = {}
    mesh_dict["mesh"]["N_points"] = self.mesh.get_mesh_pv().points
    mesh_dict["mesh"]["N_cells"] = self.mesh.get_mesh_pv().cells

    mesh_dict["solution"] = {}
    for value in self.solution_dict:
        mesh_dict["solution"][f"{value}"] = self.solution_dict[f"{value}"].as_dict()

    mesh_dict = del_key_value_None(mesh_dict)
    # Save result
    savemat(save_path, mesh_dict)


def del_key_value_None(mesh_dict):
    for key, value in mesh_dict.items():
        if isinstance(value, dict):
            pass
            # del_key_value_None(mesh_dict[key])

        elif value == None:
            del mesh_dict[key]

    return mesh_dict
