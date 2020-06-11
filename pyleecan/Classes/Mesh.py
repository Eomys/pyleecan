# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Mesh/Mesh.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.Mesh.set_submesh import set_submesh
except ImportError as error:
    set_submesh = error

try:
    from ..Methods.Mesh.Mesh.get_all_node_coord import get_all_node_coord
except ImportError as error:
    get_all_node_coord = error

try:
    from ..Methods.Mesh.Mesh.add_element import add_element
except ImportError as error:
    add_element = error

try:
    from ..Methods.Mesh.Mesh.get_all_connectivity import get_all_connectivity
except ImportError as error:
    get_all_connectivity = error

try:
    from ..Methods.Mesh.Mesh.get_connectivity import get_connectivity
except ImportError as error:
    get_connectivity = error

try:
    from ..Methods.Mesh.Mesh.get_new_tag import get_new_tag
except ImportError as error:
    get_new_tag = error

try:
    from ..Methods.Mesh.Mesh.interface import interface
except ImportError as error:
    interface = error

try:
    from ..Methods.Mesh.Mesh.get_node_tags import get_node_tags
except ImportError as error:
    get_node_tags = error

try:
    from ..Methods.Mesh.Mesh.get_vertice import get_vertice
except ImportError as error:
    get_vertice = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .Element import Element
from .Node import Node


class Mesh(FrozenClass):
    """Gather the mesh storage format"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.Mesh.set_submesh
    if isinstance(set_submesh, ImportError):
        set_submesh = property(
            fget=lambda x: raise_(
                ImportError("Can't use Mesh method set_submesh: " + str(set_submesh))
            )
        )
    else:
        set_submesh = set_submesh
    # cf Methods.Mesh.Mesh.get_all_node_coord
    if isinstance(get_all_node_coord, ImportError):
        get_all_node_coord = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Mesh method get_all_node_coord: "
                    + str(get_all_node_coord)
                )
            )
        )
    else:
        get_all_node_coord = get_all_node_coord
    # cf Methods.Mesh.Mesh.add_element
    if isinstance(add_element, ImportError):
        add_element = property(
            fget=lambda x: raise_(
                ImportError("Can't use Mesh method add_element: " + str(add_element))
            )
        )
    else:
        add_element = add_element
    # cf Methods.Mesh.Mesh.get_all_connectivity
    if isinstance(get_all_connectivity, ImportError):
        get_all_connectivity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Mesh method get_all_connectivity: "
                    + str(get_all_connectivity)
                )
            )
        )
    else:
        get_all_connectivity = get_all_connectivity
    # cf Methods.Mesh.Mesh.get_connectivity
    if isinstance(get_connectivity, ImportError):
        get_connectivity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Mesh method get_connectivity: " + str(get_connectivity)
                )
            )
        )
    else:
        get_connectivity = get_connectivity
    # cf Methods.Mesh.Mesh.get_new_tag
    if isinstance(get_new_tag, ImportError):
        get_new_tag = property(
            fget=lambda x: raise_(
                ImportError("Can't use Mesh method get_new_tag: " + str(get_new_tag))
            )
        )
    else:
        get_new_tag = get_new_tag
    # cf Methods.Mesh.Mesh.interface
    if isinstance(interface, ImportError):
        interface = property(
            fget=lambda x: raise_(
                ImportError("Can't use Mesh method interface: " + str(interface))
            )
        )
    else:
        interface = interface
    # cf Methods.Mesh.Mesh.get_node_tags
    if isinstance(get_node_tags, ImportError):
        get_node_tags = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Mesh method get_node_tags: " + str(get_node_tags)
                )
            )
        )
    else:
        get_node_tags = get_node_tags
    # cf Methods.Mesh.Mesh.get_vertice
    if isinstance(get_vertice, ImportError):
        get_vertice = property(
            fget=lambda x: raise_(
                ImportError("Can't use Mesh method get_vertice: " + str(get_vertice))
            )
        )
    else:
        get_vertice = get_vertice
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        element=dict(),
        node=-1,
        submesh=list(),
        group=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if node == -1:
            node = Node()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            element = obj.element
            node = obj.node
            submesh = obj.submesh
            group = obj.group
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "element" in list(init_dict.keys()):
                element = init_dict["element"]
            if "node" in list(init_dict.keys()):
                node = init_dict["node"]
            if "submesh" in list(init_dict.keys()):
                submesh = init_dict["submesh"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
        # Initialisation by argument
        self.parent = None
        # element can be None or a dict of Element object
        self.element = dict()
        if type(element) is dict:
            for key, obj in element.items():
                if isinstance(obj, dict):
                    # Check that the type is correct (including daughter)
                    class_name = obj.get("__class__")
                    if class_name not in ["Element", "ElementMat"]:
                        raise InitUnKnowClassError(
                            "Unknow class name "
                            + class_name
                            + " in init_dict for element"
                        )
                    # Dynamic import to call the correct constructor
                    module = __import__(
                        "pyleecan.Classes." + class_name, fromlist=[class_name]
                    )
                    class_obj = getattr(module, class_name)
                    self.element[key] = class_obj(init_dict=obj)
                else:
                    self.element[key] = obj
        elif element is None:
            self.element = dict()
        else:
            self.element = element  # Should raise an error
        # node can be None, a Node object or a dict
        if isinstance(node, dict):
            # Check that the type is correct (including daughter)
            class_name = node.get("__class__")
            if class_name not in ["Node", "NodeMat"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for node"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.node = class_obj(init_dict=node)
        elif isinstance(node, str):
            from ..Functions.load import load

            node = load(node)
            # Check that the type is correct (including daughter)
            class_name = node.__class__.__name__
            if class_name not in ["Node", "NodeMat"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for node"
                )
            self.node = node
        else:
            self.node = node
        # submesh can be None or a list of Mesh object
        self.submesh = list()
        if type(submesh) is list:
            for obj in submesh:
                if obj is None:  # Default value
                    self.submesh.append(Mesh())
                elif isinstance(obj, dict):
                    # Check that the type is correct (including daughter)
                    class_name = obj.get("__class__")
                    if class_name not in ["Mesh", "MeshVTK"]:
                        raise InitUnKnowClassError(
                            "Unknow class name "
                            + class_name
                            + " in init_dict for submesh"
                        )
                    # Dynamic import to call the correct constructor
                    module = __import__(
                        "pyleecan.Classes." + class_name, fromlist=[class_name]
                    )
                    class_obj = getattr(module, class_name)
                    self.submesh.append(class_obj(init_dict=obj))
                else:
                    self.submesh.append(obj)
        elif submesh is None:
            self.submesh = list()
        else:
            self.submesh = submesh
        # group can be None, a ndarray or a list
        set_array(self, "group", group)

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Mesh_str = ""
        if self.parent is None:
            Mesh_str += "parent = None " + linesep
        else:
            Mesh_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if len(self.element) == 0:
            Mesh_str += "element = dict()" + linesep
        for key, obj in self.element.items():
            tmp = self.element[key].__str__().replace(linesep, linesep + "\t") + linesep
            Mesh_str += "element[" + key + "] =" + tmp + linesep + linesep
        if self.node is not None:
            tmp = self.node.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Mesh_str += "node = " + tmp
        else:
            Mesh_str += "node = None" + linesep + linesep
        if len(self.submesh) == 0:
            Mesh_str += "submesh = []" + linesep
        for ii in range(len(self.submesh)):
            tmp = self.submesh[ii].__str__().replace(linesep, linesep + "\t") + linesep
            Mesh_str += "submesh[" + str(ii) + "] =" + tmp + linesep + linesep
        Mesh_str += (
            "group = "
            + linesep
            + str(self.group).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return Mesh_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.element != self.element:
            return False
        if other.node != self.node:
            return False
        if other.submesh != self.submesh:
            return False
        if not array_equal(other.group, self.group):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Mesh_dict = dict()
        Mesh_dict["element"] = dict()
        for key, obj in self.element.items():
            Mesh_dict["element"][key] = obj.as_dict()
        if self.node is None:
            Mesh_dict["node"] = None
        else:
            Mesh_dict["node"] = self.node.as_dict()
        Mesh_dict["submesh"] = list()
        for obj in self.submesh:
            Mesh_dict["submesh"].append(obj.as_dict())
        if self.group is None:
            Mesh_dict["group"] = None
        else:
            Mesh_dict["group"] = self.group.tolist()
        # The class name is added to the dict fordeserialisation purpose
        Mesh_dict["__class__"] = "Mesh"
        return Mesh_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for key, obj in self.element.items():
            obj._set_None()
        if self.node is not None:
            self.node._set_None()
        for obj in self.submesh:
            obj._set_None()
        self.group = None

    def _get_element(self):
        """getter of element"""
        for key, obj in self._element.items():
            if obj is not None:
                obj.parent = self
        return self._element

    def _set_element(self, value):
        """setter of element"""
        check_var("element", value, "{Element}")
        self._element = value

    # Storing connectivity
    # Type : {Element}
    element = property(
        fget=_get_element, fset=_set_element, doc=u"""Storing connectivity"""
    )

    def _get_node(self):
        """getter of node"""
        return self._node

    def _set_node(self, value):
        """setter of node"""
        check_var("node", value, "Node")
        self._node = value

        if self._node is not None:
            self._node.parent = self

    # Storing nodes
    # Type : Node
    node = property(fget=_get_node, fset=_set_node, doc=u"""Storing nodes""")

    def _get_submesh(self):
        """getter of submesh"""
        for obj in self._submesh:
            if obj is not None:
                obj.parent = self
        return self._submesh

    def _set_submesh(self, value):
        """setter of submesh"""
        check_var("submesh", value, "[Mesh]")
        self._submesh = value

        for obj in self._submesh:
            if obj is not None:
                obj.parent = self

    # Storing submeshes. Node and element numbers/tags or group must be the same.
    # Type : [Mesh]
    submesh = property(
        fget=_get_submesh,
        fset=_set_submesh,
        doc=u"""Storing submeshes. Node and element numbers/tags or group must be the same.""",
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

    # Contain all possible group numbers
    # Type : ndarray
    group = property(
        fget=_get_group, fset=_set_group, doc=u"""Contain all possible group numbers"""
    )
