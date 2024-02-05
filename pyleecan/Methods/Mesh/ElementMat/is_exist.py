# -*- coding: utf-8 -*-

import numpy as np


def is_exist(self, connectivity: np.ndarray) -> bool:
    """Check the existence of a element defined by a connectivity (vector of points indices).
    The order of points indices does not matter.

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    connectivity : ndarray
        an array of node tags

    Returns
    -------
        bool
            True if the element already exist
    """
    if self.nb_node_per_element > 3:
        self.get_logger().warning(
            "ElementMat.is_exist doesn't take into account quad node permutations."
        )

    # Check if the element connectivity provided has the good size
    if self.nb_node_per_element != len(connectivity):
        return False

    # Get the element index for each node of the connectivity
    node_element = np.concatenate(
        [self.get_node2element(node_index) for node_index in connectivity],
    )

    # Count how many nodes of each element are present in the connectivity
    _, unique_counts = np.unique(node_element, return_counts=True)

    # The element already exist if all its node are present in the given connectivity
    result = np.any(unique_counts == self.nb_node_per_element)

    return result
