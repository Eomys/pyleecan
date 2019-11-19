# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Mesh import Mesh

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Mesh.MeshMat.get_submesh import get_submesh
except ImportError as error:
    get_submesh = error

try:
    from pyleecan.Methods.Mesh.MeshMat.get_group import get_group
except ImportError as error:
    get_group = error

try:
    from pyleecan.Methods.Mesh.MeshMat.get_node import get_node
except ImportError as error:
    get_node = error

try:
    from pyleecan.Methods.Mesh.MeshMat.get_element import get_element
except ImportError as error:
    get_element = error

try:
    from pyleecan.Methods.Mesh.MeshMat.get_node2element import get_node2element
except ImportError as error:
    get_node2element = error


from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.SubMesh import SubMesh


class MeshMat(Mesh):
    """Gather the parameters of a mesh under matricial format containing one type of element. """

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.MeshMat.get_submesh
    if isinstance(get_submesh, ImportError):
        get_submesh = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_submesh: " + str(get_submesh))
            )
        )
    else:
        get_submesh = get_submesh
    # cf Methods.Mesh.MeshMat.get_group
    if isinstance(get_group, ImportError):
        get_group = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_group: " + str(get_group))
            )
        )
    else:
        get_group = get_group
    # cf Methods.Mesh.MeshMat.get_node
    if isinstance(get_node, ImportError):
        get_node = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_node: " + str(get_node))
            )
        )
    else:
        get_node = get_node
    # cf Methods.Mesh.MeshMat.get_element
    if isinstance(get_element, ImportError):
        get_element = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_element: " + str(get_element))
            )
        )
    else:
        get_element = get_element
    # cf Methods.Mesh.MeshMat.get_node2element
    if isinstance(get_node2element, ImportError):
        get_node2element = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method get_node2element: "
                    + str(get_node2element)
                )
            )
        )
    else:
        get_node2element = get_node2element
    # save method is available in all object
    save = save

    def __init__(
        self,
        element=None,
        node=None,
        group=None,
        nb_elem=None,
        nb_node=None,
        submesh=list(),
        nb_node_per_element=None,
        name=None,
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
                    "element",
                    "node",
                    "group",
                    "nb_elem",
                    "nb_node",
                    "submesh",
                    "nb_node_per_element",
                    "name",
                ],
            )
            # Overwrite default value with init_dict content
            if "element" in list(init_dict.keys()):
                element = init_dict["element"]
            if "node" in list(init_dict.keys()):
                node = init_dict["node"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
            if "nb_elem" in list(init_dict.keys()):
                nb_elem = init_dict["nb_elem"]
            if "nb_node" in list(init_dict.keys()):
                nb_node = init_dict["nb_node"]
            if "submesh" in list(init_dict.keys()):
                submesh = init_dict["submesh"]
            if "nb_node_per_element" in list(init_dict.keys()):
                nb_node_per_element = init_dict["nb_node_per_element"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
        # Initialisation by argument
        # element can be None, a ndarray or a list
        set_array(self, "element", element)
        # node can be None, a ndarray or a list
        set_array(self, "node", node)
        # group can be None, a ndarray or a list
        set_array(self, "group", group)
        self.nb_elem = nb_elem
        self.nb_node = nb_node
        # submesh can be None or a list of SubMesh object
        self.submesh = list()
        if type(submesh) is list:
            for obj in submesh:
                if obj is None:  # Default value
                    self.submesh.append(SubMesh())
                elif isinstance(obj, dict):
                    self.submesh.append(SubMesh(init_dict=obj))
                else:
                    self.submesh.append(obj)
        elif submesh is None:
            self.submesh = list()
        else:
            self.submesh = submesh
        self.nb_node_per_element = nb_node_per_element
        # Call Mesh init
        super(MeshMat, self).__init__(name=name)
        # The class is frozen (in Mesh init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MeshMat_str = ""
        # Get the properties inherited from Mesh
        MeshMat_str += super(MeshMat, self).__str__() + linesep
        MeshMat_str += "element = " + linesep + str(self.element) + linesep + linesep
        MeshMat_str += "node = " + linesep + str(self.node) + linesep + linesep
        MeshMat_str += "group = " + linesep + str(self.group) + linesep + linesep
        MeshMat_str += "nb_elem = " + str(self.nb_elem) + linesep
        MeshMat_str += "nb_node = " + str(self.nb_node) + linesep
        if len(self.submesh) == 0:
            MeshMat_str += "submesh = []"
        for ii in range(len(self.submesh)):
            MeshMat_str += (
                "submesh["
                + str(ii)
                + "] = "
                + str(self.submesh[ii].as_dict())
                + "\n"
                + linesep
                + linesep
            )
        MeshMat_str += "nb_node_per_element = " + str(self.nb_node_per_element)
        return MeshMat_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Mesh
        if not super(MeshMat, self).__eq__(other):
            return False
        if not array_equal(other.element, self.element):
            return False
        if not array_equal(other.node, self.node):
            return False
        if not array_equal(other.group, self.group):
            return False
        if other.nb_elem != self.nb_elem:
            return False
        if other.nb_node != self.nb_node:
            return False
        if other.submesh != self.submesh:
            return False
        if other.nb_node_per_element != self.nb_node_per_element:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Mesh
        MeshMat_dict = super(MeshMat, self).as_dict()
        if self.element is None:
            MeshMat_dict["element"] = None
        else:
            MeshMat_dict["element"] = self.element.tolist()
        if self.node is None:
            MeshMat_dict["node"] = None
        else:
            MeshMat_dict["node"] = self.node.tolist()
        if self.group is None:
            MeshMat_dict["group"] = None
        else:
            MeshMat_dict["group"] = self.group.tolist()
        MeshMat_dict["nb_elem"] = self.nb_elem
        MeshMat_dict["nb_node"] = self.nb_node
        MeshMat_dict["submesh"] = list()
        for obj in self.submesh:
            MeshMat_dict["submesh"].append(obj.as_dict())
        MeshMat_dict["nb_node_per_element"] = self.nb_node_per_element
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MeshMat_dict["__class__"] = "MeshMat"
        return MeshMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.element = None
        self.node = None
        self.group = None
        self.nb_elem = None
        self.nb_node = None
        for obj in self.submesh:
            obj._set_None()
        self.nb_node_per_element = None
        # Set to None the properties inherited from Mesh
        super(MeshMat, self)._set_None()

    def _get_element(self):
        """getter of element"""
        return self._element

    def _set_element(self, value):
        """setter of element"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("element", value, "ndarray")
        self._element = value

    # Matrix of connectivity for one element type
    # Type : ndarray
    element = property(
        fget=_get_element,
        fset=_set_element,
        doc=u"""Matrix of connectivity for one element type""",
    )

    def _get_node(self):
        """getter of node"""
        return self._node

    def _set_node(self, value):
        """setter of node"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("node", value, "ndarray")
        self._node = value

    # Containing nodes coordinates
    # Type : ndarray
    node = property(
        fget=_get_node, fset=_set_node, doc=u"""Containing nodes coordinates"""
    )

    def _get_group(self):
        """getter of group"""
        return self._group

    def _set_group(self, value):
        """setter of group"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("group", value, "ndarray")
        self._group = value

    # Attribute a number to each subpart of the machine
    # Type : ndarray
    group = property(
        fget=_get_group,
        fset=_set_group,
        doc=u"""Attribute a number to each subpart of the machine""",
    )

    def _get_nb_elem(self):
        """getter of nb_elem"""
        return self._nb_elem

    def _set_nb_elem(self, value):
        """setter of nb_elem"""
        check_var("nb_elem", value, "int")
        self._nb_elem = value

    # Total number of elements
    # Type : int
    nb_elem = property(
        fget=_get_nb_elem, fset=_set_nb_elem, doc=u"""Total number of elements"""
    )

    def _get_nb_node(self):
        """getter of nb_node"""
        return self._nb_node

    def _set_nb_node(self, value):
        """setter of nb_node"""
        check_var("nb_node", value, "int")
        self._nb_node = value

    # Total number of nodes
    # Type : int
    nb_node = property(
        fget=_get_nb_node, fset=_set_nb_node, doc=u"""Total number of nodes"""
    )

    def _get_submesh(self):
        """getter of submesh"""
        for obj in self._submesh:
            if obj is not None:
                obj.parent = self
        return self._submesh

    def _set_submesh(self, value):
        """setter of submesh"""
        check_var("submesh", value, "[SubMesh]")
        self._submesh = value

        for obj in self._submesh:
            if obj is not None:
                obj.parent = self

    # List of submesh
    # Type : [SubMesh]
    submesh = property(fget=_get_submesh, fset=_set_submesh, doc=u"""List of submesh""")

    def _get_nb_node_per_element(self):
        """getter of nb_node_per_element"""
        return self._nb_node_per_element

    def _set_nb_node_per_element(self, value):
        """setter of nb_node_per_element"""
        check_var("nb_node_per_element", value, "int")
        self._nb_node_per_element = value

    # Define the number of node per element
    # Type : int
    nb_node_per_element = property(
        fget=_get_nb_node_per_element,
        fset=_set_nb_node_per_element,
        doc=u"""Define the number of node per element""",
    )
