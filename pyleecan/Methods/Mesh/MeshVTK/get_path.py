from os.path import join
from ....definitions import RESULT_DIR


def get_path(self, name=None, file_format="vtk"):
    """return the path to the file to save the mesh

    Parameters
    ----------
    self : MeshVTK
        MeshVTK Object
    name : str
        Name of the file to use (None: use self.name)
    file_format : str
        extension of the file to use

    Returns
    -------
    path : str
        Full path to the mesh file
    """

    if self.path is None:
        self.path = RESULT_DIR

    if name is None:
        filename = self.name + "." + file_format
    else:
        filename = name + "." + file_format

    return join(self.path, filename).replace("\\", "/")
