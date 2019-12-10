# -*- coding: utf-8 -*-

import numpy as np


def add_element(self, node_tags):
    """Add a new element defined by a vector of node tags

    Parameters
    ----------
    self : ElementDict
        an ElementDict object
    node_tags : array
        an array of node tags

    Returns
    -------
        bool
            False if the element already exist
    """
    # Check the existence of the element
    if self.is_exist(node_tags):
        return False

    # if self.connectivity is not None:
    #     #     e = np.array([], dtype=int)
    #     #     for i in node_tags:
    #     #         e = np.concatenate((e, self.get_node2element(i)))
    #     #
    #     #     unique, unique_counts = np.unique(e, return_counts=True)
    #     #     for ie in range(len(unique)):
    #     #         if unique_counts[ie] == len(self.get_node_tags(unique[ie])):
    #     #             # If this condition is valid, the element already exist
    #     #             return False

    # Create the new element
    if len(node_tags) == 2:
        if self.connectivity is None:  # Create the dict
            self.connectivity = dict()
            self.connectivity = {"Segment": node_tags}
            self.tag = {"Segment": np.array([self.get_new_tag()])}
            self.nb_node_per_element = {"Segment": 2}

        else:
            if "Segment" in self.connectivity:  # Add new line
                self.connectivity["Segment"] = np.vstack(
                    [self.connectivity["Segment"], node_tags]
                )
                self.tag["Segment"] = np.concatenate(
                    [self.tag["Segment"], np.array([self.get_new_tag()])]
                )
            else:
                self.connectivity["Segment"] = node_tags  # Create new key
                self.tag["Segment"] = np.array([self.get_new_tag()])

    # Create the new element
    if len(node_tags) == 3:
        if self.connectivity is None:
            self.connectivity = dict()
            self.connectivity = {"Triangle": node_tags}
            self.tag = {"Triangle": self.get_new_tag()}
            self.nb_node_per_element = {"Triangle": 3}

        else:
            if "Triangle" in self.connectivity:
                self.connectivity["Triangle"] = np.vstack(
                    [self.connectivity["Triangle"], node_tags]
                )
                self.tag["Triangle"] = np.concatenate(
                    [self.tag["Triangle"], np.array([self.get_new_tag()])]
                )
            else:
                self.connectivity["Triangle"] = node_tags
                self.tag["Triangle"] = np.array([self.get_new_tag()])

    return True
