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

    # To save meshsolution in file .mat, dict mesh_dict must not have value = None and value = {} (empty dict)
    mesh_dict["solution"] = del_value_None(mesh_dict["solution"])
    # Save result
    savemat(save_path, mesh_dict)


def del_value_None(mesh_dict):
    """Delate value set at None in dict

    Parameters
    ----------
    mesh_dict : dict
        dict Mesh Solution

    """
    for key, value in mesh_dict.items():
        if isinstance(value, dict):
            if len(mesh_dict[key]) == 0:
                mesh_dict.pop(key)
                del_value_None(mesh_dict)
                break

            else:
                del_value_None(mesh_dict[key])

        elif isinstance(value, list):
            for ele in value:
                if isinstance(ele, dict):
                    del_value_None(ele)

        elif value == None:
            del mesh_dict[key]
            del_value_None(mesh_dict)
            break

    return mesh_dict
