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
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Mesh import Mesh

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.MeshMat.get_node import get_node
except ImportError as error:
    get_node = error

try:
    from ..Methods.Mesh.MeshMat.get_node_indice import get_node_indice
except ImportError as error:
    get_node_indice = error

try:
    from ..Methods.Mesh.MeshMat.get_cell import get_cell
except ImportError as error:
    get_cell = error

try:
    from ..Methods.Mesh.MeshMat.get_mesh_pv import get_mesh_pv
except ImportError as error:
    get_mesh_pv = error

try:
    from ..Methods.Mesh.MeshMat.get_cell_area import get_cell_area
except ImportError as error:
    get_cell_area = error

try:
    from ..Methods.Mesh.MeshMat.get_vertice import get_vertice
except ImportError as error:
    get_vertice = error

try:
    from ..Methods.Mesh.MeshMat.get_node2cell import get_node2cell
except ImportError as error:
    get_node2cell = error

try:
    from ..Methods.Mesh.MeshMat.add_cell import add_cell
except ImportError as error:
    add_cell = error

try:
    from ..Methods.Mesh.MeshMat.renum import renum
except ImportError as error:
    renum = error

try:
    from ..Methods.Mesh.MeshMat.find_cell import find_cell
except ImportError as error:
    find_cell = error

try:
    from ..Methods.Mesh.MeshMat.interface import interface
except ImportError as error:
    interface = error

try:
    from ..Methods.Mesh.MeshMat.clear_node import clear_node
except ImportError as error:
    clear_node = error

try:
    from ..Methods.Mesh.MeshMat.clear_cell import clear_cell
except ImportError as error:
    clear_cell = error


from ._check import InitUnKnowClassError
from .CellMat import CellMat
from .NodeMat import NodeMat


class MeshMat(Mesh):
    """Gather the mesh storage format"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.MeshMat.get_node
    if isinstance(get_node, ImportError):
        get_node = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_node: " + str(get_node))
            )
        )
    else:
        get_node = get_node
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
    # cf Methods.Mesh.MeshMat.get_cell
    if isinstance(get_cell, ImportError):
        get_cell = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_cell: " + str(get_cell))
            )
        )
    else:
        get_cell = get_cell
    # cf Methods.Mesh.MeshMat.get_mesh_pv
    if isinstance(get_mesh_pv, ImportError):
        get_mesh_pv = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_mesh_pv: " + str(get_mesh_pv))
            )
        )
    else:
        get_mesh_pv = get_mesh_pv
    # cf Methods.Mesh.MeshMat.get_cell_area
    if isinstance(get_cell_area, ImportError):
        get_cell_area = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method get_cell_area: " + str(get_cell_area)
                )
            )
        )
    else:
        get_cell_area = get_cell_area
    # cf Methods.Mesh.MeshMat.get_vertice
    if isinstance(get_vertice, ImportError):
        get_vertice = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_vertice: " + str(get_vertice))
            )
        )
    else:
        get_vertice = get_vertice
    # cf Methods.Mesh.MeshMat.get_node2cell
    if isinstance(get_node2cell, ImportError):
        get_node2cell = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method get_node2cell: " + str(get_node2cell)
                )
            )
        )
    else:
        get_node2cell = get_node2cell
    # cf Methods.Mesh.MeshMat.add_cell
    if isinstance(add_cell, ImportError):
        add_cell = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method add_cell: " + str(add_cell))
            )
        )
    else:
        add_cell = add_cell
    # cf Methods.Mesh.MeshMat.renum
    if isinstance(renum, ImportError):
        renum = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method renum: " + str(renum))
            )
        )
    else:
        renum = renum
    # cf Methods.Mesh.MeshMat.find_cell
    if isinstance(find_cell, ImportError):
        find_cell = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method find_cell: " + str(find_cell))
            )
        )
    else:
        find_cell = find_cell
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
    # cf Methods.Mesh.MeshMat.clear_cell
    if isinstance(clear_cell, ImportError):
        clear_cell = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method clear_cell: " + str(clear_cell))
            )
        )
    else:
        clear_cell = clear_cell
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        cell=-1,
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
            if "cell" in list(init_dict.keys()):
                cell = init_dict["cell"]
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
        self.cell = cell
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
        if len(self.cell) == 0:
            MeshMat_str += "cell = dict()" + linesep
        for key, obj in self.cell.items():
            tmp = self.cell[key].__str__().replace(linesep, linesep + "\t") + linesep
            MeshMat_str += "cell[" + key + "] =" + tmp + linesep + linesep
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
        if other.cell != self.cell:
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

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Mesh
        diff_list.extend(super(MeshMat, self).compare(other, name=name))
        if (other.cell is None and self.cell is not None) or (
            other.cell is not None and self.cell is None
        ):
            diff_list.append(name + ".cell None mismatch")
        elif self.cell is None:
            pass
        elif len(other.cell) != len(self.cell):
            diff_list.append("len(" + name + "cell)")
        else:
            for key in self.cell:
                diff_list.extend(
                    self.cell[key].compare(other.cell[key], name=name + ".cell")
                )
        if (other.node is None and self.node is not None) or (
            other.node is not None and self.node is None
        ):
            diff_list.append(name + ".node None mismatch")
        elif self.node is not None:
            diff_list.extend(self.node.compare(other.node, name=name + ".node"))
        if other.__is_renum != self.__is_renum:
            diff_list.append(name + "._is_renum")
        if other._sym != self._sym:
            diff_list.append(name + ".sym")
        if other._is_antiper_a != self._is_antiper_a:
            diff_list.append(name + ".is_antiper_a")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Mesh
        S += super(MeshMat, self).__sizeof__()
        if self.cell is not None:
            for key, value in self.cell.items():
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
        if self.cell is None:
            MeshMat_dict["cell"] = None
        else:
            MeshMat_dict["cell"] = dict()
            for key, obj in self.cell.items():
                if obj is not None:
                    MeshMat_dict["cell"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    MeshMat_dict["cell"][key] = None
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

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.cell = None
        if self.node is not None:
            self.node._set_None()
        self._is_renum = None
        self.sym = None
        self.is_antiper_a = None
        # Set to None the properties inherited from Mesh
        super(MeshMat, self)._set_None()

    def _get_cell(self):
        """getter of cell"""
        if self._cell is not None:
            for key, obj in self._cell.items():
                if obj is not None:
                    obj.parent = self
        return self._cell

    def _set_cell(self, value):
        """setter of cell"""
        if type(value) is dict:
            for key, obj in value.items():
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "cell"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("cell", value, "{CellMat}")
        self._cell = value

    cell = property(
        fget=_get_cell,
        fset=_set_cell,
        doc=u"""Storing connectivity

        :Type: {CellMat}
        """,
    )

    def _get_node(self):
        """getter of node"""
        return self._node

    def _set_node(self, value):
        """setter of node"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "node")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
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
        doc=u"""True if renumering the nodes and cells is useful when renum method is called (saving calculation time)

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
