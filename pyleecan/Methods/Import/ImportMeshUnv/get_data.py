# -*- coding: utf-8 -*-

from numpy import array as np_array, where, vstack, hstack

import pyuff


def get_data(self):
    """Return mesh data (nodes and elements) from a .unv file

    Parameters
    ----------
    self : ImportData
        An ImportData object

    Returns
    -------
    nodes: ndarray
        The nodes id and coordinates (one line = id, 3 coordinates)
    elements: dict
        The elements id and connectivity per element type (one line = id, n node ids)

    """

    # Import data from .unv file
    uff_ascii = pyuff.UFF(self.file_path)
    datasets = uff_ascii.read_sets()

    # Scan datasets
    for dataset in datasets:
        # If nodes dataset
        if dataset["type"] == 15:
            nodes = vstack(
                (
                    [int(x) for x in dataset["node_nums"]],
                    dataset["x"],
                    dataset["y"],
                    dataset["z"],
                )
            ).T

        # If element dataset
        elif dataset["type"] == 2412:
            # Store connectivities
            elements = dict()
            for elt_type, elt_dict in dataset.items():
                if elt_type != "type":
                    elements[elt_type] = vstack(
                        (elt_dict["element_nums"], np_array(elt_dict["nodes_nums"]).T)
                    ).T

    return nodes, elements
