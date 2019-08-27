# -*- coding: utf-8 -*-

from pyleecan.Methods.Output.Output.getter import GetOutError


def get_Ntype_elem(self):
    """Return the total number of elements in the stored mesh

    Parameters
    ----------
    self : Mesh
        an Mesh object

    Returns
    -------
    Nb_elem_tot: int
        Total number of elements mesh

    """

    # Already available => Return
    if self.Ntype_elem is not None:
        return self.Ntype_elem

    # Check if possible to get the BH curve
    if (
        self is None
    ):
        raise GetOutError(
            "Mesh is not Set, can't get the number of element type"
        )

    # Compute and store the number of elements
    Ntype_elem = self.set_Ntype_elem()

    return Ntype_elem

