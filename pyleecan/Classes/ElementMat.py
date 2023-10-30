# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/ElementMat.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/ElementMat
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.ElementMat.add_element import add_element
except ImportError as error:
    add_element = error

try:
    from ..Methods.Mesh.ElementMat.get_connectivity import get_connectivity
except ImportError as error:
    get_connectivity = error

try:
    from ..Methods.Mesh.ElementMat.get_node2element import get_node2element
except ImportError as error:
    get_node2element = error

try:
    from ..Methods.Mesh.ElementMat.is_exist import is_exist
except ImportError as error:
    is_exist = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class ElementMat(FrozenClass):
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
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        connectivity=None,
        nb_element=0,
        nb_node_per_element=0,
        indice=None,
        interpolation=-1,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "connectivity" in list(init_dict.keys()):
                connectivity = init_dict["connectivity"]
            if "nb_element" in list(init_dict.keys()):
                nb_element = init_dict["nb_element"]
            if "nb_node_per_element" in list(init_dict.keys()):
                nb_node_per_element = init_dict["nb_node_per_element"]
            if "indice" in list(init_dict.keys()):
                indice = init_dict["indice"]
            if "interpolation" in list(init_dict.keys()):
                interpolation = init_dict["interpolation"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.connectivity = connectivity
        self.nb_element = nb_element
        self.nb_node_per_element = nb_node_per_element
        self.indice = indice
        self.interpolation = interpolation

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ElementMat_str = ""
        if self.parent is None:
            ElementMat_str += "parent = None " + linesep
        else:
            ElementMat_str += "parent = " + str(type(self.parent)) + " object" + linesep
        ElementMat_str += (
            "connectivity = "
            + linesep
            + str(self.connectivity).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        ElementMat_str += "nb_element = " + str(self.nb_element) + linesep
        ElementMat_str += (
            "nb_node_per_element = " + str(self.nb_node_per_element) + linesep
        )
        ElementMat_str += (
            "indice = "
            + linesep
            + str(self.indice).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        if self.interpolation is not None:
            tmp = (
                self.interpolation.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            ElementMat_str += "interpolation = " + tmp
        else:
            ElementMat_str += "interpolation = None" + linesep + linesep
        return ElementMat_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if not array_equal(other.connectivity, self.connectivity):
            return False
        if other.nb_element != self.nb_element:
            return False
        if other.nb_node_per_element != self.nb_node_per_element:
            return False
        if not array_equal(other.indice, self.indice):
            return False
        if other.interpolation != self.interpolation:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if not array_equal(other.connectivity, self.connectivity):
            diff_list.append(name + ".connectivity")
        if other._nb_element != self._nb_element:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._nb_element)
                    + ", other="
                    + str(other._nb_element)
                    + ")"
                )
                diff_list.append(name + ".nb_element" + val_str)
            else:
                diff_list.append(name + ".nb_element")
        if other._nb_node_per_element != self._nb_node_per_element:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._nb_node_per_element)
                    + ", other="
                    + str(other._nb_node_per_element)
                    + ")"
                )
                diff_list.append(name + ".nb_node_per_element" + val_str)
            else:
                diff_list.append(name + ".nb_node_per_element")
        if not array_equal(other.indice, self.indice):
            diff_list.append(name + ".indice")
        if (other.interpolation is None and self.interpolation is not None) or (
            other.interpolation is not None and self.interpolation is None
        ):
            diff_list.append(name + ".interpolation None mismatch")
        elif self.interpolation is not None:
            diff_list.extend(
                self.interpolation.compare(
                    other.interpolation,
                    name=name + ".interpolation",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.connectivity)
        S += getsizeof(self.nb_element)
        S += getsizeof(self.nb_node_per_element)
        S += getsizeof(self.indice)
        S += getsizeof(self.interpolation)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        ElementMat_dict = dict()
        if self.connectivity is None:
            ElementMat_dict["connectivity"] = None
        else:
            if type_handle_ndarray == 0:
                ElementMat_dict["connectivity"] = self.connectivity.tolist()
            elif type_handle_ndarray == 1:
                ElementMat_dict["connectivity"] = self.connectivity.copy()
            elif type_handle_ndarray == 2:
                ElementMat_dict["connectivity"] = self.connectivity
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        ElementMat_dict["nb_element"] = self.nb_element
        ElementMat_dict["nb_node_per_element"] = self.nb_node_per_element
        if self.indice is None:
            ElementMat_dict["indice"] = None
        else:
            if type_handle_ndarray == 0:
                ElementMat_dict["indice"] = self.indice.tolist()
            elif type_handle_ndarray == 1:
                ElementMat_dict["indice"] = self.indice.copy()
            elif type_handle_ndarray == 2:
                ElementMat_dict["indice"] = self.indice
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.interpolation is None:
            ElementMat_dict["interpolation"] = None
        else:
            ElementMat_dict["interpolation"] = self.interpolation.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        ElementMat_dict["__class__"] = "ElementMat"
        return ElementMat_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.connectivity is None:
            connectivity_val = None
        else:
            connectivity_val = self.connectivity.copy()
        nb_element_val = self.nb_element
        nb_node_per_element_val = self.nb_node_per_element
        if self.indice is None:
            indice_val = None
        else:
            indice_val = self.indice.copy()
        if self.interpolation is None:
            interpolation_val = None
        else:
            interpolation_val = self.interpolation.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            connectivity=connectivity_val,
            nb_element=nb_element_val,
            nb_node_per_element=nb_node_per_element_val,
            indice=indice_val,
            interpolation=interpolation_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.connectivity = None
        self.nb_element = None
        self.nb_node_per_element = None
        self.indice = None
        if self.interpolation is not None:
            self.interpolation._set_None()

    def _get_connectivity(self):
        """getter of connectivity"""
        return self._connectivity

    def _set_connectivity(self, value):
        """setter of connectivity"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("connectivity", value, "ndarray")
        self._connectivity = value

    connectivity = property(
        fget=_get_connectivity,
        fset=_set_connectivity,
        doc=u"""Matrix of connectivity for one element type

        :Type: ndarray
        """,
    )

    def _get_nb_element(self):
        """getter of nb_element"""
        return self._nb_element

    def _set_nb_element(self, value):
        """setter of nb_element"""
        check_var("nb_element", value, "int")
        self._nb_element = value

    nb_element = property(
        fget=_get_nb_element,
        fset=_set_nb_element,
        doc=u"""Total number of elements

        :Type: int
        """,
    )

    def _get_nb_node_per_element(self):
        """getter of nb_node_per_element"""
        return self._nb_node_per_element

    def _set_nb_node_per_element(self, value):
        """setter of nb_node_per_element"""
        check_var("nb_node_per_element", value, "int")
        self._nb_node_per_element = value

    nb_node_per_element = property(
        fget=_get_nb_node_per_element,
        fset=_set_nb_node_per_element,
        doc=u"""Define the number of node per element

        :Type: int
        """,
    )

    def _get_indice(self):
        """getter of indice"""
        return self._indice

    def _set_indice(self, value):
        """setter of indice"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("indice", value, "ndarray")
        self._indice = value

    indice = property(
        fget=_get_indice,
        fset=_set_indice,
        doc=u"""Element indices

        :Type: ndarray
        """,
    )

    def _get_interpolation(self):
        """getter of interpolation"""
        return self._interpolation

    def _set_interpolation(self, value):
        """setter of interpolation"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "interpolation"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Interpolation = import_class(
                "pyleecan.Classes", "Interpolation", "interpolation"
            )
            value = Interpolation()
        check_var("interpolation", value, "Interpolation")
        self._interpolation = value

        if self._interpolation is not None:
            self._interpolation.parent = self

    interpolation = property(
        fget=_get_interpolation,
        fset=_set_interpolation,
        doc=u"""Define FEA interpolation

        :Type: Interpolation
        """,
    )
