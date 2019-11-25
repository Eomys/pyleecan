# -*- coding: utf-8 -*-

from pyleecan.Methods.Output.Output.getter import GetOutError


def get_nodes2elements(self):
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
    if self.nodes_to_elements is not None:
        return self.nodes_to_elements

    # Check if possible to get the BH curve
    if (
        self is None
    ):
        raise GetOutError(
            "Mesh is not Set, can't get the list of element connected to each node"
        )

    # Compute and store the number of elements
    nodes_to_elements = self.set_nodes2elements()

    return nodes_to_elements

