# -*- coding: utf-8 -*-
from scipy.io import savemat
import os
from ....Functions.GUI.log_error import log_error


def export_to_mat(self, save_path):
    """Save mesh and all solutions to a .mat file

    Parameters
    ----------
    self : MeshSolution
        an MeshSolution object
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None

    """
    # Check if extension file is .mat
    save_path_L = save_path.split(".")
    if len(save_path_L) == 1:
        save_path = f"{save_path_L[0]}.mat"
    else:
        if save_path_L[-1] != "mat":
            err_msg = f"Error save path extension is not .mat"
            log_error(
                self,
                err_msg,
                self.mesh.get_logger(),
                is_popup=False,
                is_warning=False,
            )

    # Check if save_path exist
    save_path_2 = os.path.dirname(save_path)

    if not os.path.isdir(save_path_2):
        raise Exception(
            f"Error while saving mesh solution, save path doesn't exist: {save_path}"
        )

    # dict to save
    mesh_dict = dict()
    mesh_dict["mesh"] = {}
    mesh_dict["mesh"]["points_coordinates"] = self.mesh.get_mesh_pv().points
    mesh_dict["mesh"]["cells_connectivity"] = self.mesh.get_mesh_pv().cells

    mesh_dict["solution"] = {}
    for key in self.solution_dict:
        mesh_dict["solution"][key] = self.solution_dict[f"{key}"].as_dict()

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
