# -*- coding: utf-8 -*-

from pyleecan.Classes.ElementDict import ElementDict
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


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
     elemdict: ElementDict
         an ElementDict which is created from other_element

     """

    elemdict = ElementDict()
    elemdict.connectivity = dict()
    elemdict.group = dict()
    elemdict.nb_elem = dict()
    elemdict.nb_node_per_element = dict()

    if type(other_element) is ElementMat:
        if other_element.nb_node_per_element == 2:
            elemdict.connectivity["Segment"] = other_element.connectivity
            elemdict.group["Segment"] = other_element.group
            elemdict.nb_elem["Segment"] = other_element.nb_elem
            elemdict.nb_node_per_element["Segment"] = other_element.nb_node_per_element

        if other_element.nb_node_per_element == 3:
            elemdict.connectivity["Triangle"] = other_element.connectivity
            elemdict.group["Triangle"] = other_element.group
            elemdict.nb_elem["Triangle"] = other_element.nb_elem
            elemdict.nb_node_per_element["Triangle"] = other_element.nb_node_per_element

        if other_element.nb_node_per_element == 4:
            elemdict.connectivity["Quadrangle"] = other_element.connectivity
            elemdict.group["Quadrangle"] = other_element.group
            elemdict.nb_elem["Quadrangle"] = other_element.nb_elem
            elemdict.nb_node_per_element["Quadrangle"] = other_element.nb_node_per_element

    return elemdict