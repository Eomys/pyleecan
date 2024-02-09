import os
from ....Functions.GUI.log_error import log_error


def save_vtk(self, save_path):
    """Save mesh to a .vtk file

    Parameters
    ----------
    self : Mesh
        an Mesh object
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None

    """
    # Check if extension file is .vtk
    save_path_L = save_path.split(".")
    if len(save_path_L) == 1:
        save_path = f"{save_path_L[0]}.vtk"
    else:
        if save_path_L[-1] != "vtk":
            err_msg = f"Error save path extension is not .vtk"
            log_error(
                self,
                err_msg,
                self.get_logger(),
                is_popup=False,
                is_warning=False,
            )

    # Check if save_path exist
    save_path_2 = os.path.dirname(save_path)

    if not os.path.isdir(save_path_2):
        raise Exception(
            f"Error while saving mesh to vtk, save path doesn't exist: {save_path}"
        )
    self.get_mesh_pv().save(save_path)
