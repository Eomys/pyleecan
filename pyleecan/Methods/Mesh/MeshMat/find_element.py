# -*- coding: utf-8 -*-

import numpy as np


def find_element(self, points, nb_pt, normal_t=None):
    """Return the elements containing the target point(s)

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
    element_list: list
        A list of selected elements

    """
    # nmax_search = 3
    elements_list = list()
    element_prop = list()

    nodes = self.node
    point_coord = nodes.coordinate
    nb_tot_pt = nodes.nb_node

    for ii in range(nb_pt):
        if nb_pt == 1:
            pt = points
        else:
            pt = points[ii, :]
        for key in self.element:
            elements = self.element[key]
            ref_element = elements.interpolation.ref_element
            connect = elements.connectivity
            nb_node_per_element = elements.nb_node_per_element
            # vertice0 = point_coord[connect[0]]
            # dist_ref = np.sqrt(
            #     np.square(vertice0[0, 0] - vertice0[1, 0])
            #     + np.square(vertice0[0, 1] - vertice0[1, 1])
            # )

            # compute the distance of all nodes to the current point 'pt'
            point_rep = np.tile(pt, (nb_tot_pt, 1))

            if self.dimension == 3:
                dist_node = np.reshape(
                    np.sqrt(
                        np.square(point_coord[:, 0] - point_rep[:, 0])
                        + np.square(point_coord[:, 1] - point_rep[:, 1])
                        + np.square(point_coord[:, 2] - point_rep[:, 2])
                    ),
                    (nb_tot_pt, 1),
                )
            else:
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

            # while inode < nmax_search and inode < nb_tot_pt and dontstop:

            # get elements that contain the closest node and test if point is inside
            closest_elements = np.where(connect == Imin_node[inode])[0]
            nb_closest_elem = len(closest_elements)
            a, b = np.zeros(nb_closest_elem), np.zeros(nb_closest_elem)
            element_prop = list()
            for ielt in range(nb_closest_elem):
                vert = self.get_vertice(closest_elements[ielt])[key]
                (is_inside, a[ielt], b[ielt]) = ref_element.is_inside(
                    vert, pt, normal_t
                )
                if is_inside:
                    # dontstop = False
                    element_prop.append(key)
                    element_prop.append(closest_elements[ielt])

                # inode = inode + 1
                # break

            # if no element was found, give it a second try
            # TODO first check if outside mesh
            if len(element_prop) == 0:
                # test all elements (sorted by center, i.e. mean of vertices)
                vert_cent = np.zeros(pt.shape)
                for ielement in range(nb_node_per_element):
                    vert_cent = (
                        vert_cent
                        + point_coord[connect[:, ielement]] / nb_node_per_element
                    )

                if self.dimension == 3:
                    dist_vert_cent = np.reshape(
                        np.sqrt(
                            (vert_cent[:, 0] - pt[0]) ** 2
                            + (vert_cent[:, 1] - pt[1]) ** 2
                            + (vert_cent[:, 2] - pt[2]) ** 2
                        ),
                        (elements.nb_element, 1),
                    )
                else:
                    dist_vert_cent = np.reshape(
                        np.sqrt(
                            (vert_cent[:, 0] - pt[0]) ** 2
                            + (vert_cent[:, 1] - pt[1]) ** 2
                        ),
                        (elements.nb_element, 1),
                    )

                Imin_vert_cent = np.argsort(dist_vert_cent, axis=0)[:, 0]
                i = 0
                is_inside = False
                while i < elements.nb_element and not is_inside:
                    vert = self.get_vertice(Imin_vert_cent[i])[key]
                    (is_inside, a, b) = ref_element.is_inside(vert, pt, normal_t)
                    if is_inside:
                        # dontstop = False
                        element_prop = [key, Imin_vert_cent[i]]
                    i += 1

            # No element contain the point atleast (only possible if point is outside mesh)
            if len(element_prop) == 0:
                elements_list.append(None)
            # one element found
            elif len(element_prop) == 2:
                elements_list.append(element_prop)
            # more than one elements found
            elif len(element_prop) > 2:
                ind = np.where(np.min(a) == a)[0][0]
                elements_list.append(element_prop[2 * ind : 2 * ind + 2])

    return elements_list
