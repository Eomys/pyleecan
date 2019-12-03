# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Element import Element

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Mesh.ElementDict.get_group import get_group
except ImportError as error:
    get_group = error

try:
    from pyleecan.Methods.Mesh.ElementDict.get_node_tags import get_node_tags
except ImportError as error:
    get_node_tags = error

try:
    from pyleecan.Methods.Mesh.ElementDict.get_node2element import get_node2element
except ImportError as error:
    get_node2element = error

try:
    from pyleecan.Methods.Mesh.ElementDict.convert_element import convert_element
except ImportError as error:
    convert_element = error

try:
    from pyleecan.Methods.Mesh.ElementDict.add_element import add_element
except ImportError as error:
    add_element = error

try:
    from pyleecan.Methods.Mesh.ElementDict.get_connectivity import get_connectivity
except ImportError as error:
    get_connectivity = error

try:
    from pyleecan.Methods.Mesh.ElementDict.get_new_tag import get_new_tag
except ImportError as error:
    get_new_tag = error

try:
    from pyleecan.Methods.Mesh.ElementDict.is_exist import is_exist
except ImportError as error:
    is_exist = error


from pyleecan.Classes.check import InitUnKnowClassError


class ElementDict(Element):
    """Define the connectivity with a dict, sorting element by types. """

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.ElementDict.get_group
    if isinstance(get_group, ImportError):
        get_group = property(
            fget=lambda x: raise_(
                ImportError("Can't use ElementDict method get_group: " + str(get_group))
            )
        )
    else:
        get_group = get_group
    # cf Methods.Mesh.ElementDict.get_node_tags
    if isinstance(get_node_tags, ImportError):
        get_node_tags = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElementDict method get_node_tags: " + str(get_node_tags)
                )
            )
        )
    else:
        get_node_tags = get_node_tags
    # cf Methods.Mesh.ElementDict.get_node2element
    if isinstance(get_node2element, ImportError):
        get_node2element = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElementDict method get_node2element: "
                    + str(get_node2element)
                )
            )
        )
    else:
        get_node2element = get_node2element
    # cf Methods.Mesh.ElementDict.convert_element
    if isinstance(convert_element, ImportError):
        convert_element = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElementDict method convert_element: "
                    + str(convert_element)
                )
            )
        )
    else:
        convert_element = convert_element
    # cf Methods.Mesh.ElementDict.add_element
    if isinstance(add_element, ImportError):
        add_element = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElementDict method add_element: " + str(add_element)
                )
            )
        )
    else:
        add_element = add_element
    # cf Methods.Mesh.ElementDict.get_connectivity
    if isinstance(get_connectivity, ImportError):
        get_connectivity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElementDict method get_connectivity: "
                    + str(get_connectivity)
                )
            )
        )
    else:
        get_connectivity = get_connectivity
    # cf Methods.Mesh.ElementDict.get_new_tag
    if isinstance(get_new_tag, ImportError):
        get_new_tag = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElementDict method get_new_tag: " + str(get_new_tag)
                )
            )
        )
    else:
        get_new_tag = get_new_tag
    # cf Methods.Mesh.ElementDict.is_exist
    if isinstance(is_exist, ImportError):
        is_exist = property(
            fget=lambda x: raise_(
                ImportError("Can't use ElementDict method is_exist: " + str(is_exist))
            )
        )
    else:
        is_exist = is_exist
    # save method is available in all object
    save = save

    def __init__(
        self,
        connectivity=None,
        nb_elem=None,
        nb_node_per_element=None,
        tag=None,
        group=None,
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
                ["connectivity", "nb_elem", "nb_node_per_element", "tag", "group"],
            )
            # Overwrite default value with init_dict content
            if "connectivity" in list(init_dict.keys()):
                connectivity = init_dict["connectivity"]
            if "nb_elem" in list(init_dict.keys()):
                nb_elem = init_dict["nb_elem"]
            if "nb_node_per_element" in list(init_dict.keys()):
                nb_node_per_element = init_dict["nb_node_per_element"]
            if "tag" in list(init_dict.keys()):
                tag = init_dict["tag"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
        # Initialisation by argument
        self.connectivity = connectivity
        self.nb_elem = nb_elem
        self.nb_node_per_element = nb_node_per_element
        self.tag = tag
        self.group = group
        # Call Element init
        super(ElementDict, self).__init__()
        # The class is frozen (in Element init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ElementDict_str = ""
        # Get the properties inherited from Element
        ElementDict_str += super(ElementDict, self).__str__() + linesep
        ElementDict_str += "connectivity = " + str(self.connectivity) + linesep
        ElementDict_str += "nb_elem = " + str(self.nb_elem) + linesep
        ElementDict_str += (
            "nb_node_per_element = " + str(self.nb_node_per_element) + linesep
        )
        ElementDict_str += "tag = " + str(self.tag) + linesep
        ElementDict_str += "group = " + str(self.group)
        return ElementDict_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Element
        if not super(ElementDict, self).__eq__(other):
            return False
        if other.connectivity != self.connectivity:
            return False
        if other.nb_elem != self.nb_elem:
            return False
        if other.nb_node_per_element != self.nb_node_per_element:
            return False
        if other.tag != self.tag:
            return False
        if other.group != self.group:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Element
        ElementDict_dict = super(ElementDict, self).as_dict()
        ElementDict_dict["connectivity"] = self.connectivity
        ElementDict_dict["nb_elem"] = self.nb_elem
        ElementDict_dict["nb_node_per_element"] = self.nb_node_per_element
        ElementDict_dict["tag"] = self.tag
        ElementDict_dict["group"] = self.group
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ElementDict_dict["__class__"] = "ElementDict"
        return ElementDict_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.connectivity = None
        self.nb_elem = None
        self.nb_node_per_element = None
        self.tag = None
        self.group = None
        # Set to None the properties inherited from Element
        super(ElementDict, self)._set_None()

    def _get_connectivity(self):
        """getter of connectivity"""
        return self._connectivity

    def _set_connectivity(self, value):
        """setter of connectivity"""
        check_var("connectivity", value, "dict")
        self._connectivity = value

    # Dict containing connectivity strored per element type in a ndarray: element = {"Triangle": np.array([nd1, nd2, nd3 ]), "Quadrangle": np.array([nd1, nd2, nd3, nd4 ])}.
    # Type : dict
    connectivity = property(
        fget=_get_connectivity,
        fset=_set_connectivity,
        doc=u"""Dict containing connectivity strored per element type in a ndarray: element = {"Triangle": np.array([nd1, nd2, nd3 ]), "Quadrangle": np.array([nd1, nd2, nd3, nd4 ])}.""",
    )

    def _get_nb_elem(self):
        """getter of nb_elem"""
        return self._nb_elem

    def _set_nb_elem(self, value):
        """setter of nb_elem"""
        check_var("nb_elem", value, "dict")
        self._nb_elem = value

    # Number of elements per element type and total: nb_elem = {"Total": nb_elem_total (int), "Triangle": nb_elem_triangle (int)  … }.
    # Type : dict
    nb_elem = property(
        fget=_get_nb_elem,
        fset=_set_nb_elem,
        doc=u"""Number of elements per element type and total: nb_elem = {"Total": nb_elem_total (int), "Triangle": nb_elem_triangle (int)  … }.""",
    )

    def _get_nb_node_per_element(self):
        """getter of nb_node_per_element"""
        return self._nb_node_per_element

    def _set_nb_node_per_element(self, value):
        """setter of nb_node_per_element"""
        check_var("nb_node_per_element", value, "dict")
        self._nb_node_per_element = value

    # Define the number of node per element
    # Type : dict
    nb_node_per_element = property(
        fget=_get_nb_node_per_element,
        fset=_set_nb_node_per_element,
        doc=u"""Define the number of node per element""",
    )

    def _get_tag(self):
        """getter of tag"""
        return self._tag

    def _set_tag(self, value):
        """setter of tag"""
        check_var("tag", value, "dict")
        self._tag = value

    # Dict containing tags stored per element type
    # Type : dict
    tag = property(
        fget=_get_tag,
        fset=_set_tag,
        doc=u"""Dict containing tags stored per element type""",
    )

    def _get_group(self):
        """getter of group"""
        return self._group

    def _set_group(self, value):
        """setter of group"""
        check_var("group", value, "dict")
        self._group = value

    # Attribute a group number (int) to each element . This group number should correspond to a subpart of the machine.
    # Type : dict
    group = property(
        fget=_get_group,
        fset=_set_group,
        doc=u"""Attribute a group number (int) to each element . This group number should correspond to a subpart of the machine.""",
    )
