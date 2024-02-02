from ....Classes.ElementMat import ElementMat
from ....Classes.MeshMat import MeshMat
from ....Classes.NodeMat import NodeMat


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
    mesh_mat_node = mesh_mat.get_node_coordinate()
    mesh_mat_element = mesh_mat.get_element()

    # swap axis
    mesh_mat_node = mesh_mat_node.T[perm_coord_list].T

    # create new object
    # 1. create NodeMat
    nb_node = len(mesh_mat_node)
    nodemat = NodeMat(coordinate=mesh_mat_node, nb_node=nb_node)

    # 2. create ElementMat
    elementMatDict = dict()

    for key in mesh_mat_element[0]:
        element_mat = ElementMat(
            connectivity=mesh_mat_element[0][key],
            nb_element=len(mesh_mat_element[0][key]),
        )
        elementMatDict[key] = element_mat

    # 3. create MeshMat
    meshmat = MeshMat(element_dict=elementMatDict, node=nodemat)

    # convert and save into vtk
    mesh_pv = meshmat.get_mesh_pv()
    if path_meshVTK is not None:
        mesh_pv.save(path_meshVTK)
    elif self.path is not None:
        mesh_pv.save(self.path + "/" + self.name + ".vtk")

    self.mesh = mesh_pv

    return self
