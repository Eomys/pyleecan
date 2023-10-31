# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/MeshMat.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/MeshMat
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .Mesh import Mesh

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.MeshMat.get_node_coordinate import get_node_coordinate
except ImportError as error:
    get_node_coordinate = error

try:
    from ..Methods.Mesh.MeshMat.get_node_indice import get_node_indice
except ImportError as error:
    get_node_indice = error

try:
    from ..Methods.Mesh.MeshMat.get_element import get_element
except ImportError as error:
    get_element = error

try:
    from ..Methods.Mesh.MeshMat.get_mesh_pv import get_mesh_pv
except ImportError as error:
    get_mesh_pv = error

try:
    from ..Methods.Mesh.MeshMat.get_element_area import get_element_area
except ImportError as error:
    get_element_area = error

try:
    from ..Methods.Mesh.MeshMat.get_vertice import get_vertice
except ImportError as error:
    get_vertice = error

try:
    from ..Methods.Mesh.MeshMat.get_node2element import get_node2element
except ImportError as error:
    get_node2element = error

try:
    from ..Methods.Mesh.MeshMat.add_element import add_element
except ImportError as error:
    add_element = error

try:
    from ..Methods.Mesh.MeshMat.renum import renum
except ImportError as error:
    renum = error

try:
    from ..Methods.Mesh.MeshMat.find_element import find_element
except ImportError as error:
    find_element = error

try:
    from ..Methods.Mesh.MeshMat.interface import interface
except ImportError as error:
    interface = error

try:
    from ..Methods.Mesh.MeshMat.clear_node import clear_node
except ImportError as error:
    clear_node = error

try:
    from ..Methods.Mesh.MeshMat.clear_element import clear_element
except ImportError as error:
    clear_element = error

try:
    from ..Methods.Mesh.MeshMat.get_element_nb import get_element_nb
except ImportError as error:
    get_element_nb = error


from numpy import isnan
from ._check import InitUnKnowClassError


class MeshMat(Mesh):
    """Gather the mesh storage format"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.MeshMat.get_node_coordinate
    if isinstance(get_node_coordinate, ImportError):
        get_node_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method get_node_coordinate: "
                    + str(get_node_coordinate)
                )
            )
        )
    else:
        get_node_coordinate = get_node_coordinate
    # cf Methods.Mesh.MeshMat.get_node_indice
    if isinstance(get_node_indice, ImportError):
        get_node_indice = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method get_node_indice: " + str(get_node_indice)
                )
            )
        )
    else:
        get_node_indice = get_node_indice
    # cf Methods.Mesh.MeshMat.get_element
    if isinstance(get_element, ImportError):
        get_element = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_element: " + str(get_element))
            )
        )
    else:
        get_element = get_element
    # cf Methods.Mesh.MeshMat.get_mesh_pv
    if isinstance(get_mesh_pv, ImportError):
        get_mesh_pv = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_mesh_pv: " + str(get_mesh_pv))
            )
        )
    else:
        get_mesh_pv = get_mesh_pv
    # cf Methods.Mesh.MeshMat.get_element_area
    if isinstance(get_element_area, ImportError):
        get_element_area = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method get_element_area: "
                    + str(get_element_area)
                )
            )
        )
    else:
        get_element_area = get_element_area
    # cf Methods.Mesh.MeshMat.get_vertice
    if isinstance(get_vertice, ImportError):
        get_vertice = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_vertice: " + str(get_vertice))
            )
        )
    else:
        get_vertice = get_vertice
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
    # cf Methods.Mesh.MeshMat.add_element
    if isinstance(add_element, ImportError):
        add_element = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method add_element: " + str(add_element))
            )
        )
    else:
        add_element = add_element
    # cf Methods.Mesh.MeshMat.renum
    if isinstance(renum, ImportError):
        renum = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method renum: " + str(renum))
            )
        )
    else:
        renum = renum
    # cf Methods.Mesh.MeshMat.find_element
    if isinstance(find_element, ImportError):
        find_element = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method find_element: " + str(find_element)
                )
            )
        )
    else:
        find_element = find_element
    # cf Methods.Mesh.MeshMat.interface
    if isinstance(interface, ImportError):
        interface = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method interface: " + str(interface))
            )
        )
    else:
        interface = interface
    # cf Methods.Mesh.MeshMat.clear_node
    if isinstance(clear_node, ImportError):
        clear_node = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method clear_node: " + str(clear_node))
            )
        )
    else:
        clear_node = clear_node
    # cf Methods.Mesh.MeshMat.clear_element
    if isinstance(clear_element, ImportError):
        clear_element = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method clear_element: " + str(clear_element)
                )
            )
        )
    else:
        clear_element = clear_element
    # cf Methods.Mesh.MeshMat.get_element_nb
    if isinstance(get_element_nb, ImportError):
        get_element_nb = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method get_element_nb: " + str(get_element_nb)
                )
            )
        )
    else:
        get_element_nb = get_element_nb
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        element=-1,
        node=-1,
        _is_renum=False,
        sym=1,
        is_antiper_a=False,
        label=None,
        dimension=2,
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
            if "element" in list(init_dict.keys()):
                element = init_dict["element"]
            if "node" in list(init_dict.keys()):
                node = init_dict["node"]
            if "_is_renum" in list(init_dict.keys()):
                _is_renum = init_dict["_is_renum"]
            if "sym" in list(init_dict.keys()):
                sym = init_dict["sym"]
            if "is_antiper_a" in list(init_dict.keys()):
                is_antiper_a = init_dict["is_antiper_a"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
            if "dimension" in list(init_dict.keys()):
                dimension = init_dict["dimension"]
        # Set the properties (value check and convertion are done in setter)
        self.element = element
        self.node = node
        self._is_renum = _is_renum
        self.sym = sym
        self.is_antiper_a = is_antiper_a
        # Call Mesh init
        super(MeshMat, self).__init__(label=label, dimension=dimension)
        # The class is frozen (in Mesh init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MeshMat_str = ""
        # Get the properties inherited from Mesh
        MeshMat_str += super(MeshMat, self).__str__()
        if len(self.element) == 0:
            MeshMat_str += "element = dict()" + linesep
        for key, obj in self.element.items():
            tmp = self.element[key].__str__().replace(linesep, linesep + "\t") + linesep
            MeshMat_str += "element[" + key + "] =" + tmp + linesep + linesep
        if self.node is not None:
            tmp = self.node.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MeshMat_str += "node = " + tmp
        else:
            MeshMat_str += "node = None" + linesep + linesep
        MeshMat_str += "_is_renum = " + str(self._is_renum) + linesep
        MeshMat_str += "sym = " + str(self.sym) + linesep
        MeshMat_str += "is_antiper_a = " + str(self.is_antiper_a) + linesep
        return MeshMat_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Mesh
        if not super(MeshMat, self).__eq__(other):
            return False
        if other.element != self.element:
            return False
        if other.node != self.node:
            return False
        if other._is_renum != self._is_renum:
            return False
        if other.sym != self.sym:
            return False
        if other.is_antiper_a != self.is_antiper_a:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Mesh
        diff_list.extend(
            super(MeshMat, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.element is None and self.element is not None) or (
            other.element is not None and self.element is None
        ):
            diff_list.append(name + ".element None mismatch")
        elif self.element is None:
            pass
        elif len(other.element) != len(self.element):
            diff_list.append("len(" + name + "element)")
        else:
            for key in self.element:
                diff_list.extend(
                    self.element[key].compare(
                        other.element[key],
                        name=name + ".element[" + str(key) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
        if (other.node is None and self.node is not None) or (
            other.node is not None and self.node is None
        ):
            diff_list.append(name + ".node None mismatch")
        elif self.node is not None:
            diff_list.extend(
                self.node.compare(
                    other.node,
                    name=name + ".node",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other.__is_renum != self.__is_renum:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self.__is_renum)
                    + ", other="
                    + str(other.__is_renum)
                    + ")"
                )
                diff_list.append(name + "._is_renum" + val_str)
            else:
                diff_list.append(name + "._is_renum")
        if other._sym != self._sym:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._sym) + ", other=" + str(other._sym) + ")"
                )
                diff_list.append(name + ".sym" + val_str)
            else:
                diff_list.append(name + ".sym")
        if other._is_antiper_a != self._is_antiper_a:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_antiper_a)
                    + ", other="
                    + str(other._is_antiper_a)
                    + ")"
                )
                diff_list.append(name + ".is_antiper_a" + val_str)
            else:
                diff_list.append(name + ".is_antiper_a")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Mesh
        S += super(MeshMat, self).__sizeof__()
        if self.element is not None:
            for key, value in self.element.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.node)
        S += getsizeof(self._is_renum)
        S += getsizeof(self.sym)
        S += getsizeof(self.is_antiper_a)
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

        # Get the properties inherited from Mesh
        MeshMat_dict = super(MeshMat, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.element is None:
            MeshMat_dict["element"] = None
        else:
            MeshMat_dict["element"] = dict()
            for key, obj in self.element.items():
                if obj is not None:
                    MeshMat_dict["element"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    MeshMat_dict["element"][key] = None
        if self.node is None:
            MeshMat_dict["node"] = None
        else:
            MeshMat_dict["node"] = self.node.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        MeshMat_dict["_is_renum"] = self._is_renum
        MeshMat_dict["sym"] = self.sym
        MeshMat_dict["is_antiper_a"] = self.is_antiper_a
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        MeshMat_dict["__class__"] = "MeshMat"
        return MeshMat_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.element is None:
            element_val = None
        else:
            element_val = dict()
            for key, obj in self.element.items():
                element_val[key] = obj.copy()
        if self.node is None:
            node_val = None
        else:
            node_val = self.node.copy()
        _is_renum_val = self._is_renum
        sym_val = self.sym
        is_antiper_a_val = self.is_antiper_a
        label_val = self.label
        dimension_val = self.dimension
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            element=element_val,
            node=node_val,
            _is_renum=_is_renum_val,
            sym=sym_val,
            is_antiper_a=is_antiper_a_val,
            label=label_val,
            dimension=dimension_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.element = None
        if self.node is not None:
            self.node._set_None()
        self._is_renum = None
        self.sym = None
        self.is_antiper_a = None
        # Set to None the properties inherited from Mesh
        super(MeshMat, self)._set_None()

    def _get_element(self):
        """getter of element"""
        if self._element is not None:
            for key, obj in self._element.items():
                if obj is not None:
                    obj.parent = self
        return self._element

    def _set_element(self, value):
        """setter of element"""
        if type(value) is dict:
            for key, obj in value.items():
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[key] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "element"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("element", value, "{ElementMat}")
        self._element = value

    element = property(
        fget=_get_element,
        fset=_set_element,
        doc=u"""Storing connectivity

        :Type: {ElementMat}
        """,
    )

    def _get_node(self):
        """getter of node"""
        return self._node

    def _set_node(self, value):
        """setter of node"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "node")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            NodeMat = import_class("pyleecan.Classes", "NodeMat", "node")
            value = NodeMat()
        check_var("node", value, "NodeMat")
        self._node = value

        if self._node is not None:
            self._node.parent = self

    node = property(
        fget=_get_node,
        fset=_set_node,
        doc=u"""Storing nodes

        :Type: NodeMat
        """,
    )

    def _get__is_renum(self):
        """getter of _is_renum"""
        return self.__is_renum

    def _set__is_renum(self, value):
        """setter of _is_renum"""
        check_var("_is_renum", value, "bool")
        self.__is_renum = value

    _is_renum = property(
        fget=_get__is_renum,
        fset=_set__is_renum,
        doc=u"""True if renumering the nodes and elements is useful when renum method is called (saving calculation time)

        :Type: bool
        """,
    )

    def _get_sym(self):
        """getter of sym"""
        return self._sym

    def _set_sym(self, value):
        """setter of sym"""
        check_var("sym", value, "int")
        self._sym = value

    sym = property(
        fget=_get_sym,
        fset=_set_sym,
        doc=u"""Spatial symmetry factor

        :Type: int
        """,
    )

    def _get_is_antiper_a(self):
        """getter of is_antiper_a"""
        return self._is_antiper_a

    def _set_is_antiper_a(self, value):
        """setter of is_antiper_a"""
        check_var("is_antiper_a", value, "bool")
        self._is_antiper_a = value

    is_antiper_a = property(
        fget=_get_is_antiper_a,
        fset=_set_is_antiper_a,
        doc=u"""True if there is a spatial antiperiod

        :Type: bool
        """,
    )
