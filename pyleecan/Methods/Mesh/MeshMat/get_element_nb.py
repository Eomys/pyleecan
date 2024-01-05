# -*- coding: utf-8 -*-
def get_element_nb(self) -> int:
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

    nb_element = sum([element.nb_element for element in self.element_dict.values()])

    return nb_element
