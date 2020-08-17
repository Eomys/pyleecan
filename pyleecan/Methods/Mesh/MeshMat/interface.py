# -*- coding: utf-8 -*-
from ....Classes.PointMat import PointMat
from ....Classes.CellMat import CellMat
from ....definitions import PACKAGE_NAME
from collections import Counter
import numpy as np


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
    new_mesh.point = PointMat()
    new_mesh.cell = dict()
    new_mesh.cell["segment"] = CellMat(nb_pt_per_cell=2)

    for key in self.cell:

        # Developer info: IDK if this code works with other than triangle cells. To be checked.
        if self.cell[key].nb_pt_per_cell == 3:  # Triangle case
            points_tags = np.unique(self.cell[key].get_connectivity())
            other_points_tags = np.unique(other_mesh.cell[key].get_connectivity())

            # Find the points on the interface (they are in both in and out)
            interface_points_tags = np.intersect1d(points_tags, other_points_tags)
            nb_interf_points = len(interface_points_tags)

            tmp_cell_tags = np.array([], dtype=int)
            tmp_cell_tags_other = np.array([], dtype=int)
            point2elem_dict = dict()
            point2elem_other_dict = dict()
            # Find the cells in contact with the interface (they contain the interface points)
            for ind in range(nb_interf_points):
                tmp_tag = self.cell[key].get_point2cell(interface_points_tags[ind])
                point2elem_dict[interface_points_tags[ind]] = tmp_tag
                tmp_cell_tags = np.concatenate((tmp_cell_tags, tmp_tag))

                tmp_tag = other_mesh.cell[key].get_point2cell(
                    interface_points_tags[ind]
                )
                point2elem_other_dict[interface_points_tags[ind]] = tmp_tag
                tmp_cell_tags_other = np.concatenate((tmp_cell_tags_other, tmp_tag))

            # Find cell tags in contact and number of points in contact for each cell
            tmp_cell_tags_unique = np.unique(
                tmp_cell_tags
            )  # List of cell tag which are in contact with the interface
            nb_elem_contact = len(tmp_cell_tags_unique)
            nb_cell_tags_unique = np.zeros((nb_elem_contact, 1), dtype=int)
            elem2point_dict = dict()
            for ind in range(nb_elem_contact):
                # Number of point on the interface for each cell from tmp_cell_tags_unique
                Ipos = np.where(tmp_cell_tags_unique[ind] == tmp_cell_tags)[0]
                nb_cell_tags_unique[ind] = len(Ipos)
                # Which points exactly are concerned; store them in elem2point_dict
                cells_tmp = self.get_cell(tmp_cell_tags_unique[ind])[0]
                # for key in cells_tmp:
                points_tmp = np.unique(cells_tmp[key])
                points_tmp_interf = np.array([], dtype=int)
                for ipos in range(len(points_tmp)):
                    if points_tmp[ipos] in interface_points_tags:
                        points_tmp_interf = np.concatenate(
                            (points_tmp_interf, np.array([points_tmp[ipos]], dtype=int))
                        )
                elem2point_dict[tmp_cell_tags_unique[ind]] = points_tmp_interf

            # Build cell
            seg_elem_pos = np.where(nb_cell_tags_unique == 2)[
                0
            ]  # Position in the vector tmp_cell_tags_unique
            seg_elem_tag = tmp_cell_tags_unique[
                seg_elem_pos
            ]  # Vector of cell tags with only 2 points on the interface
            nb_elem_segm = len(seg_elem_tag)
            for i_seg in range(nb_elem_segm):
                tag_two_points = elem2point_dict[seg_elem_tag[i_seg]]
                new_mesh.add_cell(tag_two_points, "segment")

            # The same operation is applied in the other mesh because in the corners, 1 cell will contain 3 points,
            # and it will not be detected by seg_elem_pos. Applying the same process to the other mesh solve the issue
            # if add_cell ignore the already defined cells.
            tmp_cell_tags_other_unique = np.unique(tmp_cell_tags_other)
            nb_point_other_contact = len(tmp_cell_tags_other_unique)
            nb_cell_tags_other_unique = np.zeros((nb_point_other_contact, 1), dtype=int)
            elem2point_other_dict = dict()
            for ind in range(nb_point_other_contact):
                Ipos = np.where(tmp_cell_tags_other_unique[ind] == tmp_cell_tags_other)[
                    0
                ]
                nb_cell_tags_other_unique[ind] = len(Ipos)
                cells_tmp = other_mesh.get_cell(tmp_cell_tags_other_unique[ind])[0]
                points_tmp = np.unique(cells_tmp[key])
                points_tmp_interf = np.array([], dtype=int)
                for ipos in range(len(points_tmp)):
                    if points_tmp[ipos] in interface_points_tags:
                        points_tmp_interf = np.concatenate(
                            (points_tmp_interf, np.array([points_tmp[ipos]], dtype=int))
                        )
                elem2point_other_dict[
                    tmp_cell_tags_other_unique[ind]
                ] = points_tmp_interf

            # Build segment cells in other mesh
            seg_elem_pos = np.where(nb_cell_tags_other_unique == 2)[0]
            seg_elem_tag = tmp_cell_tags_other_unique[seg_elem_pos]
            nb_elem_segm = len(seg_elem_tag)
            for i_seg in range(nb_elem_segm):
                tag_two_points = elem2point_other_dict[seg_elem_tag[i_seg]]
                # It is not really added if it already exist
                # new_tag = new_mesh.get_new_tag()
                new_mesh.add_cell(tag_two_points, "segment")

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
