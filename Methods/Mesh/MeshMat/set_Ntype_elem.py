# -*- coding: utf-8 -*-

def set_Ntype_elem(self):
    """Compute the number of different element type in the stored mesh

    Parameters
    ----------
    self : Mesh
        an Mesh object

    Returns
    -------
    Ntype_elem: int
        Number of different element types

    """

    elements = self.elements
    Ntype_elem = len(elements)
    self.Ntype_elem = Ntype_elem

    return Ntype_elem

