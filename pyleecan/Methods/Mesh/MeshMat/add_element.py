# -*- coding: utf-8 -*-


def add_element(self, node_indices, element_type):
    """Add a new element defined by node indices and element type.

    Parameters
    ----------
    self : MeshMat
        a MeshMat object
    node_indices : ndarray or list of int
        a ndarray of nodes indices (length must match element.nb_node_per_element)
    element_type : str
        Define the type of element to add (key of self.element dict)

    Returns
    -------
    new_index : int
        indice of the newly created element. None if the element already exists.
    """

    # The element index must be unique for all element type
    new_index = self.get_element_nb()  # index start at 0 (last index = nb-1)

    is_created = self.element[element_type].add_element(node_indices, new_index)

    if is_created:
        return new_index
    else:
        return None
