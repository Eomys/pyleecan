# -*- coding: utf-8 -*-

import numpy as np


def find_element(self, points, normal_t=None):
    """Return the elements containing the target point(s)

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    points : ndarray
        2D array containing the coordinates of the target point(s)
    normal_t normal direction to the target element

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
    element_list = []
    element_prop_list = []

    nodes = self.node
    point_coord = nodes.coordinate
    nb_mesh_point = nodes.nb_node

    for point in points:
        # Find the closest node to the given point
        point_rep = np.tile(
            point[: self.dimension], (nb_mesh_point, 1)
        )  # /!\ if the mesh is in 2D, exclude z coordinate
        dist_node = np.linalg.norm(point_coord - point_rep, axis=1, keepdims=True)
        idx_closest_node = dist_node.argmin(axis=0)

        for key in self.element_dict:
            elements = self.element_dict[key]
            ref_element = elements.ref_element
            connect = elements.connectivity

            # All selected nodes from the closest to the farthest are tested
            # get elements that contain the closest node and test if point is inside
            idx_closest_elements = np.nonzero(connect == idx_closest_node)[0]
            nb_closest_elem = len(idx_closest_elements)
            a, b = np.zeros(nb_closest_elem), np.zeros(nb_closest_elem)
            element_idx = []
            element_prop = []
            for k, idx_closest_elem in enumerate(idx_closest_elements):
                vert = self.get_element_coordinate(idx_closest_elem, element_name=key)[
                    key
                ]
                (is_inside, a[k], b[k]) = ref_element.is_inside(
                    vert, point[: self.dimension], normal_t
                )
                if is_inside:
                    # dontstop = False
                    element_prop.append(key)
                    element_idx.append(idx_closest_elem)

            # if no element was found, give it a second try
            # TODO first check if outside mesh
            if len(element_prop) == 0:
                # test all elements (sorted by center, i.e. mean of element vertices coordinate)
                element_center = point_coord[connect].mean(axis=1)

                dist_element_cent = np.linalg.norm(
                    element_center - point[np.newaxis], axis=1, keepdims=True
                )

                idx_sorted_dist = np.argsort(dist_element_cent, axis=0)[:, 0]
                for i in range(elements.nb_element):
                    vert = self.get_element_coordinate(idx_sorted_dist[i])[key]
                    is_inside, a, *_ = ref_element.is_inside(
                        vert, point[: self.dimension], normal_t
                    )
                    if is_inside:
                        element_prop = [key]
                        element_idx = [idx_sorted_dist[i]]
                        break

            # No element contain the point atleast (only possible if point is outside mesh)
            if len(element_prop) == 0:
                element_prop_list.append(None)
                element_list.append(None)

            # one element found
            elif len(element_prop) == 1:
                element_prop_list.extend(element_prop)
                element_list.extend(element_idx)
            # more than one elements found -> find the closest element
            elif len(element_prop) > 1:
                index = np.nonzero(np.min(a) == a)[0]
                if len(index > 1):
                    logger = self.get_logger()
                    logger.warning(
                        f"The target point {point} belongs to more than one element, it may be on an edge. The method returns only one element."
                    )

                element_prop_list.append(element_prop[index[0]])
                element_list.append(element_idx[index[0]])

    return element_prop_list, element_list
