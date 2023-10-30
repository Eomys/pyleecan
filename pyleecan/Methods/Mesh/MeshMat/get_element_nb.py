# -*- coding: utf-8 -*-
def get_element_nb(self):
    """Return the total number of element of all kind

    Parameters
    ----------
    self : MeshMat
        A MeshMat object

    Returns
    -------
    nb_element : int
        total number of element of all kind
    """

    nb_element = 0
    for key in self.element:
        if self.element[key].nb_element is not None:
            nb_element += self.element[key].nb_element

    return nb_element
