# -*- coding: utf-8 -*-
from ....Classes.PointMat import PointMat
from ....Classes.CellMat import CellMat
from ....definitions import PACKAGE_NAME
from collections import Counter
import numpy as np
from itertools import combinations

def interface(self, other_mesh):
    """Define a MeshMat object corresponding to the exact intersection between two meshes (points must be in both meshes).

    Parameters
    ----------
    self : MeshMat
        a Mesh object
    other_mesh : Mesh
        an other Mesh object

        Returns
    -------
    """

    # Dynamic import
    new_mesh = self.copy()
    # new_mesh.point = PointMat()
    new_mesh.cell = dict()

    for key in self.cell:

        # Developer info: IDK if this code works with other than triangle cells. To be checked.
        if self.cell[key].nb_pt_per_cell == 3:  # Triangle case

            new_mesh.cell["line"] = CellMat(nb_pt_per_cell=2)

            connect = self.cell[key].get_connectivity()
            connect2 = other_mesh.cell[key].get_connectivity()

            points_tags = np.unique(connect)
            other_points_tags = np.unique(connect2)

            # Find the points on the interface (they are in both in and out)
            interface_points_tags = np.intersect1d(points_tags, other_points_tags)
            nb_interf_points = len(interface_points_tags)

            comb = combinations(range(self.cell[key].nb_pt_per_cell), 2)

            for duo in list(comb):
                col1i = np.mod(duo[0], 3)
                col2i = np.mod(duo[1], 3)
                col1 = connect[:, col1i]
                col2 = connect[:, col2i]

                col1_bin = np.zeros(len(col1))
                col2_bin = np.zeros(len(col1))

                for pt in interface_points_tags:
                    Icol1i = np.where(col1 == pt)[0]
                    Icol2i = np.where(col2 == pt)[0]
                    col1_bin[Icol1i] = 1
                    col2_bin[Icol2i] = 1

                # Position in vector where 2 nodes of the same element are on the interface (potential line element)
                I_target = np.where(col1_bin + col2_bin== 2)[0]

                comb2 = combinations(range(other_mesh.cell[key].nb_pt_per_cell), 2)
                for duo2 in list(comb2):
                    col1j = np.mod(duo2[0], 3)
                    col2j = np.mod(duo2[1], 3)
                    col12 = connect2[:, col1j]
                    col22 = connect2[:, col2j]

                    col12_bin = np.zeros(len(col12))
                    col22_bin = np.zeros(len(col12))

                    for pt in interface_points_tags:
                        Icol1i = np.where(col12 == pt)[0]
                        Icol2i = np.where(col22 == pt)[0]
                        col12_bin[Icol1i] = 1
                        col22_bin[Icol2i] = 1

                    # Same but in the second mesh
                    I_target2 = np.where(col12_bin + col22_bin== 2)[0]

                    for itag in I_target2:
                        e_tag1 = col12[itag]
                        e_tag2 = col22[itag]
                        Iline = np.where(((col1[I_target] == e_tag1) & (col2[I_target] == e_tag2)) | ((col2[I_target] == e_tag1) & (col1[I_target] == e_tag2)))[0]
                        if Iline.size != 0:
                            new_mesh.add_cell([e_tag1, e_tag2], "line")

    return new_mesh
    # TODO : Extend the code to higher dimension (3 points triangles for tetrahedra interfaces ...)

    # import matplotlib.pyplot as plt
    # fig, ax = plt.subplots()
    # x = mesh_group.point[:,0]
    # y = mesh_group.point[:,1]
    # ax.scatter(x, y)
    # for ieleme in range(mesh_group.nb_elem):
    #     x = mesh_group.point[interface_elem[ieleme,:],0]
    #     y = mesh_group.point[interface_elem[ieleme,:],1]
    #     ax.plot(x, y)
    #
    # fig, ax = plt.subplots()
    # x = points_in[:, 0]
    # y = points_in[:, 1]
    # ax.scatter(x, y)
    # x = points_out[:, 0]
    # y = points_out[:, 1]
    # ax.scatter(x, y)
    # x = points_parent[interface_points_id, 0]
    # y = points_parent[interface_points_id, 1]
    # ax.scatter(x, y, marker='x')
