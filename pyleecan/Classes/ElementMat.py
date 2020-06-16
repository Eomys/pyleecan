# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Mesh/ElementMat.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Element import Element

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.ElementMat.add_element import add_element
except ImportError as error:
    add_element = error

try:
    from ..Methods.Mesh.ElementMat.get_all_connectivity import get_all_connectivity
except ImportError as error:
    get_all_connectivity = error

try:
    from ..Methods.Mesh.ElementMat.get_all_node_tags import get_all_node_tags
except ImportError as error:
    get_all_node_tags = error

try:
    from ..Methods.Mesh.ElementMat.get_connectivity import get_connectivity
except ImportError as error:
    get_connectivity = error

try:
    from ..Methods.Mesh.ElementMat.get_group import get_group
except ImportError as error:
    get_group = error

try:
    from ..Methods.Mesh.ElementMat.get_node2element import get_node2element
except ImportError as error:
    get_node2element = error

try:
    from ..Methods.Mesh.ElementMat.is_exist import is_exist
except ImportError as error:
    is_exist = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class ElementMat(Element):
    """Define the connectivity under matricial format containing one type of element (example: only triangles with 3 nodes). """

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.ElementMat.add_element
    if isinstance(add_element, ImportError):
        add_element = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElementMat method add_element: " + str(add_element)
                )
            )
        )
    else:
        add_element = add_element
    # cf Methods.Mesh.ElementMat.get_all_connectivity
    if isinstance(get_all_connectivity, ImportError):
        get_all_connectivity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElementMat method get_all_connectivity: "
                    + str(get_all_connectivity)
                )
            )
        )
    else:
        get_all_connectivity = get_all_connectivity
    # cf Methods.Mesh.ElementMat.get_all_node_tags
    if isinstance(get_all_node_tags, ImportError):
        get_all_node_tags = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElementMat method get_all_node_tags: "
                    + str(get_all_node_tags)
                )
            )
        )
    else:
        get_all_node_tags = get_all_node_tags
    # cf Methods.Mesh.ElementMat.get_connectivity
    if isinstance(get_connectivity, ImportError):
        get_connectivity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElementMat method get_connectivity: "
                    + str(get_connectivity)
                )
            )
        )
    else:
        get_connectivity = get_connectivity
    # cf Methods.Mesh.ElementMat.get_group
    if isinstance(get_group, ImportError):
        get_group = property(
            fget=lambda x: raise_(
                ImportError("Can't use ElementMat method get_group: " + str(get_group))
            )
        )
    else:
        get_group = get_group
    # cf Methods.Mesh.ElementMat.get_node2element
    if isinstance(get_node2element, ImportError):
        get_node2element = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElementMat method get_node2element: "
                    + str(get_node2element)
                )
            )
        )
    else:
        get_node2element = get_node2element
    # cf Methods.Mesh.ElementMat.is_exist
    if isinstance(is_exist, ImportError):
        is_exist = property(
            fget=lambda x: raise_(
                ImportError("Can't use ElementMat method is_exist: " + str(is_exist))
            )
        )
    else:
        is_exist = is_exist
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
        connectivity=None,
        nb_elem=0,
        nb_node_per_element=0,
        group=None,
        tag=None,
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

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            connectivity = obj.connectivity
            nb_elem = obj.nb_elem
            nb_node_per_element = obj.nb_node_per_element
            group = obj.group
            tag = obj.tag
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "connectivity" in list(init_dict.keys()):
                connectivity = init_dict["connectivity"]
            if "nb_elem" in list(init_dict.keys()):
                nb_elem = init_dict["nb_elem"]
            if "nb_node_per_element" in list(init_dict.keys()):
                nb_node_per_element = init_dict["nb_node_per_element"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
            if "tag" in list(init_dict.keys()):
                tag = init_dict["tag"]
        # Initialisation by argument
        # connectivity can be None, a ndarray or a list
        set_array(self, "connectivity", connectivity)
        self.nb_elem = nb_elem
        self.nb_node_per_element = nb_node_per_element
        # group can be None, a ndarray or a list
        set_array(self, "group", group)
        # tag can be None, a ndarray or a list
        set_array(self, "tag", tag)
        # Call Element init
        super(ElementMat, self).__init__()
        # The class is frozen (in Element init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ElementMat_str = ""
        # Get the properties inherited from Element
        ElementMat_str += super(ElementMat, self).__str__()
        ElementMat_str += (
            "connectivity = "
            + linesep
            + str(self.connectivity).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        ElementMat_str += "nb_elem = " + str(self.nb_elem) + linesep
        ElementMat_str += (
            "nb_node_per_element = " + str(self.nb_node_per_element) + linesep
        )
        ElementMat_str += (
            "group = "
            + linesep
            + str(self.group).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        ElementMat_str += (
            "tag = "
            + linesep
            + str(self.tag).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return ElementMat_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Element
        if not super(ElementMat, self).__eq__(other):
            return False
        if not array_equal(other.connectivity, self.connectivity):
            return False
        if other.nb_elem != self.nb_elem:
            return False
        if other.nb_node_per_element != self.nb_node_per_element:
            return False
        if not array_equal(other.group, self.group):
            return False
        if not array_equal(other.tag, self.tag):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Element
        ElementMat_dict = super(ElementMat, self).as_dict()
        if self.connectivity is None:
            ElementMat_dict["connectivity"] = None
        else:
            ElementMat_dict["connectivity"] = self.connectivity.tolist()
        ElementMat_dict["nb_elem"] = self.nb_elem
        ElementMat_dict["nb_node_per_element"] = self.nb_node_per_element
        if self.group is None:
            ElementMat_dict["group"] = None
        else:
            ElementMat_dict["group"] = self.group.tolist()
        if self.tag is None:
            ElementMat_dict["tag"] = None
        else:
            ElementMat_dict["tag"] = self.tag.tolist()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ElementMat_dict["__class__"] = "ElementMat"
        return ElementMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.connectivity = None
        self.nb_elem = None
        self.nb_node_per_element = None
        self.group = None
        self.tag = None
        # Set to None the properties inherited from Element
        super(ElementMat, self)._set_None()

    def _get_connectivity(self):
        """getter of connectivity"""
        return self._connectivity

    def _set_connectivity(self, value):
        """setter of connectivity"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("connectivity", value, "ndarray")
        self._connectivity = value

    # Matrix of connectivity for one element type
    # Type : ndarray
    connectivity = property(
        fget=_get_connectivity,
        fset=_set_connectivity,
        doc=u"""Matrix of connectivity for one element type""",
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

    # Attribute a group number (int) to each element . This group number should correspond to a subpart of the machine.
    # Type : ndarray
    group = property(
        fget=_get_group,
        fset=_set_group,
        doc=u"""Attribute a group number (int) to each element . This group number should correspond to a subpart of the machine.""",
    )

    def _get_tag(self):
        """getter of tag"""
        return self._tag

    def _set_tag(self, value):
        """setter of tag"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("tag", value, "ndarray")
        self._tag = value

    # Element tags
    # Type : ndarray
    tag = property(fget=_get_tag, fset=_set_tag, doc=u"""Element tags""")
