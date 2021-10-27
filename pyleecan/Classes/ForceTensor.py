# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/ForceTensor.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/ForceTensor
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
from .Force import Force

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.ForceTensor.comp_force import comp_force
except ImportError as error:
    comp_force = error

try:
    from ..Methods.Simulation.ForceTensor.comp_force_nodal import comp_force_nodal
except ImportError as error:
    comp_force_nodal = error

try:
    from ..Methods.Simulation.ForceTensor.comp_magnetostrictive_tensor import (
        comp_magnetostrictive_tensor,
    )
except ImportError as error:
    comp_magnetostrictive_tensor = error

try:
    from ..Methods.Simulation.ForceTensor.element_loop import element_loop
except ImportError as error:
    element_loop = error


from ._check import InitUnKnowClassError


class ForceTensor(Force):
    """Force various tensors (Maxwell, magnetostrictive) model for radial flux machines"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.ForceTensor.comp_force
    if isinstance(comp_force, ImportError):
        comp_force = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ForceTensor method comp_force: " + str(comp_force)
                )
            )
        )
    else:
        comp_force = comp_force
    # cf Methods.Simulation.ForceTensor.comp_force_nodal
    if isinstance(comp_force_nodal, ImportError):
        comp_force_nodal = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ForceTensor method comp_force_nodal: "
                    + str(comp_force_nodal)
                )
            )
        )
    else:
        comp_force_nodal = comp_force_nodal
    # cf Methods.Simulation.ForceTensor.comp_magnetostrictive_tensor
    if isinstance(comp_magnetostrictive_tensor, ImportError):
        comp_magnetostrictive_tensor = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ForceTensor method comp_magnetostrictive_tensor: "
                    + str(comp_magnetostrictive_tensor)
                )
            )
        )
    else:
        comp_magnetostrictive_tensor = comp_magnetostrictive_tensor
    # cf Methods.Simulation.ForceTensor.element_loop
    if isinstance(element_loop, ImportError):
        element_loop = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ForceTensor method element_loop: " + str(element_loop)
                )
            )
        )
    else:
        element_loop = element_loop
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        group="stator core",
        tensor=None,
        is_periodicity_t=None,
        is_periodicity_a=None,
        is_agsf_transfer=False,
        max_wavenumber_transfer=None,
        Rsbo_enforced_transfer=None,
        logger_name="Pyleecan.Force",
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
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
            if "tensor" in list(init_dict.keys()):
                tensor = init_dict["tensor"]
            if "is_periodicity_t" in list(init_dict.keys()):
                is_periodicity_t = init_dict["is_periodicity_t"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
            if "is_agsf_transfer" in list(init_dict.keys()):
                is_agsf_transfer = init_dict["is_agsf_transfer"]
            if "max_wavenumber_transfer" in list(init_dict.keys()):
                max_wavenumber_transfer = init_dict["max_wavenumber_transfer"]
            if "Rsbo_enforced_transfer" in list(init_dict.keys()):
                Rsbo_enforced_transfer = init_dict["Rsbo_enforced_transfer"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.group = group
        self.tensor = tensor
        # Call Force init
        super(ForceTensor, self).__init__(
            is_periodicity_t=is_periodicity_t,
            is_periodicity_a=is_periodicity_a,
            is_agsf_transfer=is_agsf_transfer,
            max_wavenumber_transfer=max_wavenumber_transfer,
            Rsbo_enforced_transfer=Rsbo_enforced_transfer,
            logger_name=logger_name,
        )
        # The class is frozen (in Force init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ForceTensor_str = ""
        # Get the properties inherited from Force
        ForceTensor_str += super(ForceTensor, self).__str__()
        ForceTensor_str += 'group = "' + str(self.group) + '"' + linesep
        ForceTensor_str += "tensor = " + str(self.tensor) + linesep
        return ForceTensor_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Force
        if not super(ForceTensor, self).__eq__(other):
            return False
        if other.group != self.group:
            return False
        if other.tensor != self.tensor:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Force
        diff_list.extend(super(ForceTensor, self).compare(other, name=name))
        if other._group != self._group:
            diff_list.append(name + ".group")
        if other._tensor != self._tensor:
            diff_list.append(name + ".tensor")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Force
        S += super(ForceTensor, self).__sizeof__()
        S += getsizeof(self.group)
        if self.tensor is not None:
            for key, value in self.tensor.items():
                S += getsizeof(value) + getsizeof(key)
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

        # Get the properties inherited from Force
        ForceTensor_dict = super(ForceTensor, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ForceTensor_dict["group"] = self.group
        ForceTensor_dict["tensor"] = (
            self.tensor.copy() if self.tensor is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ForceTensor_dict["__class__"] = "ForceTensor"
        return ForceTensor_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.group = None
        self.tensor = None
        # Set to None the properties inherited from Force
        super(ForceTensor, self)._set_None()

    def _get_group(self):
        """getter of group"""
        return self._group

    def _set_group(self, value):
        """setter of group"""
        check_var("group", value, "str")
        self._group = value

    group = property(
        fget=_get_group,
        fset=_set_group,
        doc=u"""Name of the group selected for magnetic force computation. If None, all the domain is selected.

        :Type: str
        """,
    )

    def _get_tensor(self):
        """getter of tensor"""
        return self._tensor

    def _set_tensor(self, value):
        """setter of tensor"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("tensor", value, "dict")
        self._tensor = value

    tensor = property(
        fget=_get_tensor,
        fset=_set_tensor,
        doc=u"""Force model(s) to be used

        :Type: dict
        """,
    )
