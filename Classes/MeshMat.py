# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Mesh import Mesh

from pyleecan.Methods.Mesh.MeshMat.comp_projection_mesh2mesh import comp_projection_mesh2mesh
from pyleecan.Methods.Mesh.MeshMat.get_Ntype_elem import get_Ntype_elem
from pyleecan.Methods.Mesh.MeshMat.set_Ntype_elem import set_Ntype_elem
from pyleecan.Methods.Mesh.MeshMat.get_nodes2elements import get_nodes2elements
from pyleecan.Methods.Mesh.MeshMat.set_nodes2elements import set_nodes2elements

from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Elements import Elements



class MeshMat(Mesh):
    """Gather the parameters of mesh under matricial format"""

    VERSION = 1

    # cf Methods.Mesh.MeshMat.comp_projection_mesh2mesh
    comp_projection_mesh2mesh = comp_projection_mesh2mesh
    # cf Methods.Mesh.MeshMat.get_Ntype_elem
    get_Ntype_elem = get_Ntype_elem
    # cf Methods.Mesh.MeshMat.set_Ntype_elem
    set_Ntype_elem = set_Ntype_elem
    # cf Methods.Mesh.MeshMat.get_nodes2elements
    get_nodes2elements = get_nodes2elements
    # cf Methods.Mesh.MeshMat.set_nodes2elements
    set_nodes2elements = set_nodes2elements
    # save method is available in all object
    save = save

    def __init__(self, elements=list(), nodes=None, submeshes=None, nodes_to_elements=None, Ntype_elem=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["elements", "nodes", "submeshes", "nodes_to_elements", "Ntype_elem"])
            # Overwrite default value with init_dict content
            if "elements" in list(init_dict.keys()):
                elements = init_dict["elements"]
            if "nodes" in list(init_dict.keys()):
                nodes = init_dict["nodes"]
            if "submeshes" in list(init_dict.keys()):
                submeshes = init_dict["submeshes"]
            if "nodes_to_elements" in list(init_dict.keys()):
                nodes_to_elements = init_dict["nodes_to_elements"]
            if "Ntype_elem" in list(init_dict.keys()):
                Ntype_elem = init_dict["Ntype_elem"]
        # Initialisation by argument
        # elements can be None or a list of Elements object
        self.elements = list()
        if type(elements) is list:
            for obj in elements:
                if obj is None:  # Default value
                    self.elements.append(Elements())
                elif isinstance(obj, dict):
                    self.elements.append(Elements(init_dict=obj))
                else:
                    self.elements.append(obj)
        elif elements is None:
            self.elements = list()
        else:
            self.elements = elements
        # nodes can be None, a ndarray or a list
        set_array(self, "nodes", nodes)
        self.submeshes = submeshes
        self.nodes_to_elements = nodes_to_elements
        self.Ntype_elem = Ntype_elem
        # Call Mesh init
        super(MeshMat, self).__init__()
        # The class is frozen (in Mesh init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MeshMat_str = ""
        # Get the properties inherited from Mesh
        MeshMat_str += super(MeshMat, self).__str__() + linesep
        if len(self.elements) == 0:
            MeshMat_str += "elements = []"
        for ii in range(len(self.elements)):
            MeshMat_str += "elements["+str(ii)+"] = "+str(self.elements[ii].as_dict())+"\n" + linesep + linesep
        MeshMat_str += "nodes = " + linesep + str(self.nodes) + linesep + linesep
        MeshMat_str += "submeshes = " + str(self.submeshes) + linesep
        MeshMat_str += "nodes_to_elements = " + str(self.nodes_to_elements) + linesep
        MeshMat_str += "Ntype_elem = " + str(self.Ntype_elem)
        return MeshMat_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Mesh
        if not super(MeshMat, self).__eq__(other):
            return False
        if other.elements != self.elements:
            return False
        if not array_equal(other.nodes, self.nodes):
            return False
        if other.submeshes != self.submeshes:
            return False
        if other.nodes_to_elements != self.nodes_to_elements:
            return False
        if other.Ntype_elem != self.Ntype_elem:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Mesh
        MeshMat_dict = super(MeshMat, self).as_dict()
        MeshMat_dict["elements"] = list()
        for obj in self.elements:
            MeshMat_dict["elements"].append(obj.as_dict())
        if self.nodes is None:
            MeshMat_dict["nodes"] = None
        else:
            MeshMat_dict["nodes"] = self.nodes.tolist()
        MeshMat_dict["submeshes"] = self.submeshes
        MeshMat_dict["nodes_to_elements"] = self.nodes_to_elements
        MeshMat_dict["Ntype_elem"] = self.Ntype_elem
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MeshMat_dict["__class__"] = "MeshMat"
        return MeshMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.elements:
            obj._set_None()
        self.nodes = None
        self.submeshes = None
        self.nodes_to_elements = None
        self.Ntype_elem = None
        # Set to None the properties inherited from Mesh
        super(MeshMat, self)._set_None()

    def _get_elements(self):
        """getter of elements"""
        for obj in self._elements:
            if obj is not None:
                obj.parent = self
        return self._elements

    def _set_elements(self, value):
        """setter of elements"""
        check_var("elements", value, "[Elements]")
        self._elements = value

        for obj in self._elements:
            if obj is not None:
                obj.parent = self
    # Containing one list of connectivity per type element type
    # Type : [Elements]
    elements = property(fget=_get_elements, fset=_set_elements,
                        doc=u"""Containing one list of connectivity per type element type""")

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

    # Containing nodes coordinates
    # Type : ndarray
    nodes = property(fget=_get_nodes, fset=_set_nodes,
                     doc=u"""Containing nodes coordinates""")

    def _get_submeshes(self):
        """getter of submeshes"""
        return self._submeshes

    def _set_submeshes(self, value):
        """setter of submeshes"""
        check_var("submeshes", value, "dict")
        self._submeshes = value

    # Containing  lists of elements number from the same part of the machine (stator, rotor, airgap …)
    # Type : dict
    submeshes = property(fget=_get_submeshes, fset=_set_submeshes,
                         doc=u"""Containing  lists of elements number from the same part of the machine (stator, rotor, airgap …)""")

    def _get_nodes_to_elements(self):
        """getter of nodes_to_elements"""
        return self._nodes_to_elements

    def _set_nodes_to_elements(self, value):
        """setter of nodes_to_elements"""
        check_var("nodes_to_elements", value, "dict")
        self._nodes_to_elements = value

    # Containing list of element connected to each nodes
    # Type : dict
    nodes_to_elements = property(fget=_get_nodes_to_elements, fset=_set_nodes_to_elements,
                                 doc=u"""Containing list of element connected to each nodes""")

    def _get_Ntype_elem(self):
        """getter of Ntype_elem"""
        return self._Ntype_elem

    def _set_Ntype_elem(self, value):
        """setter of Ntype_elem"""
        check_var("Ntype_elem", value, "int")
        self._Ntype_elem = value

    # Total number of different type of element
    # Type : int
    Ntype_elem = property(fget=_get_Ntype_elem, fset=_set_Ntype_elem,
                          doc=u"""Total number of different type of element""")
