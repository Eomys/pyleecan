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
                ([int(x) for x in dataset["node_nums"]], dataset["x"], dataset["y"], dataset["z"])
            ).T

        # If element dataset
        elif dataset["type"] == 2412:
            # Look for the different types of elements stored in the dataset
            elements_type = list(set(dataset["num_nodes"]))
            element_type_dict = {"3": "triangle", "4": "quad"}
            # Store connectivities
            elements = dict()
            for element_type in elements_type:
                ind = where(np_array(dataset["num_nodes"]) == element_type)[0]
                elements[element_type_dict[str(element_type)]] = vstack(
                    (dataset["element_nums"], np_array(dataset["nodes_nums"])[ind].T)
                ).T

    return nodes, elements
