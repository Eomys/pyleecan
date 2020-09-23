# -*- coding: utf-8 -*-

import numpy as np


def find_cell(self, points, nb_pt, normal_t=None):
    """Return the cells containing the target point(s)

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    points : ndarray
        coordinates of the target point(s)
    nb_pt : int
        number of target points

    Returns
    -------
    cell_list: list
        A list of  of selected cells

    """
    nmax_search = 3
    cells_list = list()
    cell_prop = list()

    point = self.point
    point_coord = point.coordinate
    nb_tot_pt = point.nb_pt

    for ii in range(nb_pt):
        if nb_pt == 1:
            pt = points
        else:
            pt = points[ii, :]
        for key in self.cell:
            cells = self.cell[key]
            connect = cells.connectivity
            vertice0 = point_coord[connect[0]]
            dist_ref = np.sqrt(
                np.square(vertice0[0, 0] - vertice0[1, 0])
                + np.square(vertice0[0, 1] - vertice0[1, 1])
            )

            point_rep = np.tile(pt, (nb_tot_pt, 1))
            dist_node = np.reshape(
                np.sqrt(
                    np.square(point_coord[:, 0] - point_rep[:, 0])
                    + np.square(point_coord[:, 1] - point_rep[:, 1])
                ),
                (nb_tot_pt, 1),
            )
            # min_dist = np.min(dist_node)
            # min_node = np.where(dist_node == min_dist)[0]
            Imin_node = np.argsort(dist_node, axis=0)
            # Imin_node = Imin_node[0:nmax_search]  #

            # All selected nodes from the closest to the farthest are tested
            inode = 0
            # dontstop = True
            cell_prop = list()
            # while inode < nmax_search and inode < nb_tot_pt and dontstop:
            closest_cells = np.where(connect == Imin_node[inode])[0]
            nb_closest_elem = len(closest_cells)
            a = np.zeros(nb_closest_elem)
            b = np.zeros(nb_closest_elem)
            for ielt in range(nb_closest_elem):
                vert = self.get_vertice(closest_cells[ielt])[key]
                (is_inside, a[ielt], b[ielt]) = cells.interpolation.ref_cell.is_inside(
                    vert, pt, normal_t
                )
                if is_inside:
                    # dontstop = False
                    cell_prop.append(key)
                    cell_prop.append(closest_cells[ielt])

                # inode = inode + 1
                # break
            if len(cell_prop) > 2:
                ind = np.where(np.min(a) == a)[0][0]
                cells_list.append(cell_prop[2 * ind : 2 * ind + 2])
            else:
                if not cell_prop:
                    cells_list.append(None)
                else:
                    cells_list.append(cell_prop)

            # No cell contain the point

    return cells_list
