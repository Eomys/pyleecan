from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.CellMat import CellMat


def perm_coord(
    self,
    perm_coord_list=[0, 1, 2],
    path_meshVTK=None,
):
    """Returns the current MeshVTK object with permuted coordinates

    Parameters
    ----------
    self : MeshVTK
        a MeshVTK object
    perm_coord_list : list
        list of the coordinates to be permuted
    path_meshVTK : str
        full path to the MeshVTK file

    Returns
    -------
    mesh: MeshVTK
        The MeshVTK object with permuted coordinates

    """
    # convert into MeshMat object
    mesh_mat = self.convert(meshtype="MeshMat", scale=1)

    # extract nodes en elements
    mesh_mat_node = mesh_mat.get_node()
    mesh_mat_cell = mesh_mat.get_cell()

    # swap axis
    mesh_mat_node = mesh_mat_node.T[perm_coord_list].T

    # create new object
    # 1. create NodeMat
    nb_node = len(mesh_mat_node)
    nodemat = NodeMat(coordinate=mesh_mat_node, nb_node=nb_node)

    # 2. create CellMat
    cellMat = CellMat()
    CellMatDict = dict()

    for key in mesh_mat_cell[0]:
        cellMat = CellMat(
            connectivity=mesh_mat_cell[0][key],
            nb_cell=len(mesh_mat_cell[0][key]),
        )
        CellMatDict[key] = cellMat

    # 3. create MeshMat
    meshmat = MeshMat(cell=CellMatDict, node=nodemat)

    # convert and save into vtk
    mesh_pv = meshmat.get_mesh_pv()
    if path_meshVTK != None:
        mesh_pv.save(path_meshVTK)
    else:
        mesh_pv.save(self.path + "/" + self.name + ".vtk")

    self.mesh = mesh_pv

    return self
