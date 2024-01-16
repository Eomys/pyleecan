# -*- coding: utf-8 -*-

import numpy as np
import pyuff
from numpy import array as np_array
from numpy import hstack, newaxis, stack, vstack


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
            nodes = stack(
                (
                    np_array(dataset["node_nums"], np.int32),
                    dataset["x"],
                    dataset["y"],
                    dataset["z"],
                ),
                axis=1,
            )

        # If element dataset
        elif dataset["type"] == 2412:
            # Store connectivities
            elements = dict()
            for elt_type, elt_dict in dataset.items():
                if (
                    elt_type != "type"
                    and isinstance(elt_type, str)
                    and isinstance(elt_dict, dict)
                ):
                    elements[elt_type] = hstack(
                        (
                            np_array(elt_dict["element_nums"])[:, newaxis],
                            elt_dict["nodes_nums"],
                        )
                    )

        elif dataset["type"] == 82:
            # Store connectivities
            elements = dict()
            nodes_nums = dataset["nodes"]
            ind = np.where(nodes_nums == 0.0)  ##identify zeros
            nodes_nums = np.delete(nodes_nums, ind)  # delete zeros
            indices = list()  ##indices of duplicated node numbers
            for i in range(1, len(nodes_nums)):
                if nodes_nums[i] == nodes_nums[i - 1]:
                    indices.append(i)
            nodes_nums = np.delete(nodes_nums, indices)

            indices_node1 = np.arange(
                4, len(nodes_nums), 5
            )  ##indices of first node of previous element

            nodes_nums = np.delete(nodes_nums, indices_node1)

            ##assuming quad elements 4 nodes per element
            n = int(len(nodes_nums) / 4)
            nodes_nums = np.reshape(nodes_nums, (n, 4))
            element_nums = np.arange(len(nodes_nums))
            elements["quad"] = vstack((element_nums, nodes_nums.T)).T

    return nodes, elements
