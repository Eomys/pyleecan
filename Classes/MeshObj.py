# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Mesh import Mesh

from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Element import Element



class MeshObj(Mesh):
    """Gather the parameters of mesh under object format"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, elements=list(), nodes=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["elements", "nodes"])
            # Overwrite default value with init_dict content
            if "elements" in list(init_dict.keys()):
                elements = init_dict["elements"]
            if "nodes" in list(init_dict.keys()):
                nodes = init_dict["nodes"]
        # Initialisation by argument
        # elements can be None or a list of Element object
        self.elements = list()
        if type(elements) is list:
            for obj in elements:
                if obj is None:  # Default value
                    self.elements.append(Element())
                elif isinstance(obj, dict):
                    self.elements.append(Element(init_dict=obj))
                else:
                    self.elements.append(obj)
        elif elements is None:
            self.elements = list()
        else:
            self.elements = elements
        # nodes can be None, a ndarray or a list
        set_array(self, "nodes", nodes)
        # Call Mesh init
        super(MeshObj, self).__init__()
        # The class is frozen (in Mesh init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MeshObj_str = ""
        # Get the properties inherited from Mesh
        MeshObj_str += super(MeshObj, self).__str__() + linesep
        if len(self.elements) == 0:
            MeshObj_str += "elements = []"
        for ii in range(len(self.elements)):
            MeshObj_str += "elements["+str(ii)+"] = "+str(self.elements[ii].as_dict())+"\n" + linesep + linesep
        MeshObj_str += "nodes = " + linesep + str(self.nodes)
        return MeshObj_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Mesh
        if not super(MeshObj, self).__eq__(other):
            return False
        if other.elements != self.elements:
            return False
        if not array_equal(other.nodes, self.nodes):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Mesh
        MeshObj_dict = super(MeshObj, self).as_dict()
        MeshObj_dict["elements"] = list()
        for obj in self.elements:
            MeshObj_dict["elements"].append(obj.as_dict())
        if self.nodes is None:
            MeshObj_dict["nodes"] = None
        else:
            MeshObj_dict["nodes"] = self.nodes.tolist()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MeshObj_dict["__class__"] = "MeshObj"
        return MeshObj_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.elements:
            obj._set_None()
        self.nodes = None
        # Set to None the properties inherited from Mesh
        super(MeshObj, self)._set_None()

    def _get_elements(self):
        """getter of elements"""
        for obj in self._elements:
            if obj is not None:
                obj.parent = self
        return self._elements

    def _set_elements(self, value):
        """setter of elements"""
        check_var("elements", value, "[Element]")
        self._elements = value

        for obj in self._elements:
            if obj is not None:
                obj.parent = self
    # Containing all different elements 
    # Type : [Element]
    elements = property(fget=_get_elements, fset=_set_elements,
                        doc=u"""Containing all different elements """)

    def _get_nodes(self):
        """getter of nodes"""
        return self._nodes

    def _set_nodes(self, value):
        """setter of nodes"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("nodes", value, "ndarray")
        self._nodes = value

    # Containing all nodes 
    # Type : ndarray
    nodes = property(fget=_get_nodes, fset=_set_nodes,
                     doc=u"""Containing all nodes """)
