# -*- coding: utf-8 -*-

import numpy as np


def find_element(self, points, normal_t=None):
    """Return the elements containing the target point(s)

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    points : ndarray
        2darray containing the coordinates of the target point(s)
    normal_t TODO identify what it is

    Returns
    -------
    element_list: list
        A list of selected elements

    """

    if points.ndim != 2:
        raise ValueError(
            "points must have two dimensions, namely the number of points and the points coordinates."
        )

    # nmax_search = 3
    elements_list = []
    element_prop = []

    nodes = self.node
    point_coord = nodes.coordinate
    nb_mesh_point = nodes.nb_node

    for point in points:
        # Find the closest node to the given point
        point_rep = np.tile(point, (nb_mesh_point, 1))
        dist_node = np.linalg.norm(point_coord - point_rep, axis=1, keepdims=True)
        idx_closest_node = dist_node.argmin(axis=0)

        for key in self.element:
            elements = self.element[key]
            ref_element = elements.interpolation.ref_element
            connect = elements.connectivity
            nb_node_per_element = elements.nb_node_per_element

            # All selected nodes from the closest to the farthest are tested
            # get elements that contain the closest node and test if point is inside
            idx_closest_elements = np.where(connect == idx_closest_node)[0]
            nb_closest_elem = len(idx_closest_elements)
            a, b = np.zeros(nb_closest_elem), np.zeros(nb_closest_elem)
            element_prop = list()
            for k, idx_closest_elem in enumerate(idx_closest_elements):
                vert = self.get_vertice(idx_closest_elem)[key]
                (is_inside, a[k], b[k]) = ref_element.is_inside(vert, point, normal_t)
                if is_inside:
                    # dontstop = False
                    element_prop.append(key)
                    element_prop.append(idx_closest_elem)

                # inode = inode + 1
                # break<

            # if no element was found, give it a second try
            # TODO first check if outside mesh
            if len(element_prop) == 0:
                # test all elements (sorted by center, i.e. mean of vertices)
                element_center = point_coord[connect].mean(axis=1)

                dist_element_cent = np.linalg.norm(
                    element_center - point[np.newaxis], axis=1, keepdims=True
                )

                idx_sorted_dist = np.argsort(dist_element_cent, axis=0)[:, 0]
                for i in range(elements.nb_element):
                    vert = self.get_vertice(idx_sorted_dist[i])[key]
                    (is_inside, a, b) = ref_element.is_inside(vert, point, normal_t)
                    if is_inside:
                        element_prop = [key, idx_sorted_dist[i]]
                        break

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
