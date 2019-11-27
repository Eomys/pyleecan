# -*- coding: utf-8 -*-

#sfrom pyleecan.Classes.ElementDict import ElementDict
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np
import copy

def convert_element(self, other_element):
    """Define an ElementDict object from any other Element type.

     Parameters
     ----------
     self : ElementDict
         an ElementDict object
     other_element : Element
         an Element object

     Returns
     -------
     """

    self.connectivity = dict()
    self.group = dict()
    self.nb_elem = dict()
    self.nb_node_per_element = dict()
    self.tag = dict()

    if type(other_element) is ElementMat:
        if other_element.nb_node_per_element == 2:
            self.connectivity["Segment"] = other_element.connectivity
            self.group["Segment"] = other_element.group
            self.nb_elem["Segment"] = other_element.nb_elem
            self.nb_node_per_element["Segment"] = other_element.nb_node_per_element
            self.tag["Segment"] = np.linspace(
                0, other_element.nb_elem - 1, other_element.nb_elem
            )

        if other_element.nb_node_per_element == 3:
            self.connectivity["Triangle"] = other_element.connectivity
            self.group["Triangle"] = other_element.group
            self.nb_elem["Triangle"] = other_element.nb_elem
            self.nb_node_per_element["Triangle"] = other_element.nb_node_per_element
            self.tag["Triangle"] = np.linspace(
                0, other_element.nb_elem - 1, other_element.nb_elem
            )

        if other_element.nb_node_per_element == 4:
            self.connectivity["Quadrangle"] = other_element.connectivity
            self.group["Quadrangle"] = other_element.group
            self.nb_elem["Quadrangle"] = other_element.nb_elem
            self.nb_node_per_element["Quadrangle"] = other_element.nb_node_per_element
            self.tag["Quadrangle"] = np.linspace(
                0, other_element.nb_elem - 1, other_element.nb_elem
            )

    else:
        self.connectivity = other_element.connectivity
        self.group = other_element.group
        self.nb_elem = other_element.nb_elem
        self.nb_node_per_element = other_element.nb_node_per_element
        self.tag = other_element.tag
