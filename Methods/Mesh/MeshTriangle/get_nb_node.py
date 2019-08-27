# -*- coding: utf-8 -*-

from pyleecan.Methods.Output.Output.getter import GetOutError


def get_nb_node(self):
    """Return the total number of elements in the stored mesh

    Parameters
    ----------
    self : Mesh
        an Mesh object

    Returns
    -------
    Nb_nodes_tot: int
        Total number of nodes in the mesh

    """

    # Already available => Return
    if self.Nb_nodes_tot is not None:
        return self.Nb_nodes_tot

    # Check if possible to get the BH curve
    if (
        self is None
    ):
        raise GetOutError(
            "Mesh is not Set, can't get the number of nodes"
        )

    # Compute and store the number of elements
    Nb_nodes_tot = self.set_Nb_nodes_tot()

    return Nb_nodes_tot

