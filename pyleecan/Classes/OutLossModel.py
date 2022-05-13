# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutLossModel.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutLossModel
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.OutLossModel.get_mesh_solution import get_mesh_solution
except ImportError as error:
    get_mesh_solution = error

try:
    from ..Methods.Output.OutLossModel.get_loss_scalar import get_loss_scalar
except ImportError as error:
    get_loss_scalar = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class OutLossModel(FrozenClass):
    """Gather the loss module outputs"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.OutLossModel.get_mesh_solution
    if isinstance(get_mesh_solution, ImportError):
        get_mesh_solution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLossModel method get_mesh_solution: "
                    + str(get_mesh_solution)
                )
            )
        )
    else:
        get_mesh_solution = get_mesh_solution
    # cf Methods.Output.OutLossModel.get_loss_scalar
    if isinstance(get_loss_scalar, ImportError):
        get_loss_scalar = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLossModel method get_loss_scalar: "
                    + str(get_loss_scalar)
                )
            )
        )
    else:
        get_loss_scalar = get_loss_scalar
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name="",
        loss_density=None,
        coeff_dict=None,
        freqs=None,
        scalar_value=None,
        group=None,
        f=None,
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
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "loss_density" in list(init_dict.keys()):
                loss_density = init_dict["loss_density"]
            if "coeff_dict" in list(init_dict.keys()):
                coeff_dict = init_dict["coeff_dict"]
            if "freqs" in list(init_dict.keys()):
                freqs = init_dict["freqs"]
            if "scalar_value" in list(init_dict.keys()):
                scalar_value = init_dict["scalar_value"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
            if "f" in list(init_dict.keys()):
                f = init_dict["f"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.name = name
        self.loss_density = loss_density
        self.coeff_dict = coeff_dict
        self.freqs = freqs
        self.scalar_value = scalar_value
        self.group = group
        self.f = f

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutLossModel_str = ""
        if self.parent is None:
            OutLossModel_str += "parent = None " + linesep
        else:
            OutLossModel_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        OutLossModel_str += 'name = "' + str(self.name) + '"' + linesep
        OutLossModel_str += (
            "loss_density = "
            + linesep
            + str(self.loss_density).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLossModel_str += "coeff_dict = " + str(self.coeff_dict) + linesep
        OutLossModel_str += (
            "freqs = "
            + linesep
            + str(self.freqs).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        OutLossModel_str += "scalar_value = " + str(self.scalar_value) + linesep
        OutLossModel_str += 'group = "' + str(self.group) + '"' + linesep
        OutLossModel_str += "f = " + str(self.f) + linesep
        return OutLossModel_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        if not array_equal(other.loss_density, self.loss_density):
            return False
        if other.coeff_dict != self.coeff_dict:
            return False
        if not array_equal(other.freqs, self.freqs):
            return False
        if other.scalar_value != self.scalar_value:
            return False
        if other.group != self.group:
            return False
        if other.f != self.f:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._name != self._name:
            diff_list.append(name + ".name")
        if not array_equal(other.loss_density, self.loss_density):
            diff_list.append(name + ".loss_density")
        if other._coeff_dict != self._coeff_dict:
            diff_list.append(name + ".coeff_dict")
        if not array_equal(other.freqs, self.freqs):
            diff_list.append(name + ".freqs")
        if other._scalar_value != self._scalar_value:
            diff_list.append(name + ".scalar_value")
        if other._group != self._group:
            diff_list.append(name + ".group")
        if other._f != self._f:
            diff_list.append(name + ".f")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.name)
        S += getsizeof(self.loss_density)
        if self.coeff_dict is not None:
            for key, value in self.coeff_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.freqs)
        S += getsizeof(self.scalar_value)
        S += getsizeof(self.group)
        S += getsizeof(self.f)
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

        OutLossModel_dict = dict()
        OutLossModel_dict["name"] = self.name
        if self.loss_density is None:
            OutLossModel_dict["loss_density"] = None
        else:
            if type_handle_ndarray == 0:
                OutLossModel_dict["loss_density"] = self.loss_density.tolist()
            elif type_handle_ndarray == 1:
                OutLossModel_dict["loss_density"] = self.loss_density.copy()
            elif type_handle_ndarray == 2:
                OutLossModel_dict["loss_density"] = self.loss_density
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        OutLossModel_dict["coeff_dict"] = (
            self.coeff_dict.copy() if self.coeff_dict is not None else None
        )
        if self.freqs is None:
            OutLossModel_dict["freqs"] = None
        else:
            if type_handle_ndarray == 0:
                OutLossModel_dict["freqs"] = self.freqs.tolist()
            elif type_handle_ndarray == 1:
                OutLossModel_dict["freqs"] = self.freqs.copy()
            elif type_handle_ndarray == 2:
                OutLossModel_dict["freqs"] = self.freqs
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        OutLossModel_dict["scalar_value"] = self.scalar_value
        OutLossModel_dict["group"] = self.group
        OutLossModel_dict["f"] = self.f
        # The class name is added to the dict for deserialisation purpose
        OutLossModel_dict["__class__"] = "OutLossModel"
        return OutLossModel_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.loss_density = None
        self.coeff_dict = None
        self.freqs = None
        self.scalar_value = None
        self.group = None
        self.f = None

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""Name of the loss

        :Type: str
        """,
    )

    def _get_loss_density(self):
        """getter of loss_density"""
        return self._loss_density

    def _set_loss_density(self, value):
        """setter of loss_density"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("loss_density", value, "ndarray")
        self._loss_density = value

    loss_density = property(
        fget=_get_loss_density,
        fset=_set_loss_density,
        doc=u"""Loss density 

        :Type: ndarray
        """,
    )

    def _get_coeff_dict(self):
        """getter of coeff_dict"""
        return self._coeff_dict

    def _set_coeff_dict(self, value):
        """setter of coeff_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("coeff_dict", value, "dict")
        self._coeff_dict = value

    coeff_dict = property(
        fget=_get_coeff_dict,
        fset=_set_coeff_dict,
        doc=u"""dict of coefficients to compute the scalar value with respcet to frequency

        :Type: dict
        """,
    )

    def _get_freqs(self):
        """getter of freqs"""
        return self._freqs

    def _set_freqs(self, value):
        """setter of freqs"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("freqs", value, "ndarray")
        self._freqs = value

    freqs = property(
        fget=_get_freqs,
        fset=_set_freqs,
        doc=u"""array of frequency to sum the losses of each one

        :Type: ndarray
        """,
    )

    def _get_scalar_value(self):
        """getter of scalar_value"""
        return self._scalar_value

    def _set_scalar_value(self, value):
        """setter of scalar_value"""
        check_var("scalar_value", value, "float")
        self._scalar_value = value

    scalar_value = property(
        fget=_get_scalar_value,
        fset=_set_scalar_value,
        doc=u"""Scalar value of the loss got by integrating the loss density over the machine

        :Type: float
        """,
    )

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
        doc=u"""group to which the loss applies

        :Type: str
        """,
    )

    def _get_f(self):
        """getter of f"""
        return self._f

    def _set_f(self, value):
        """setter of f"""
        check_var("f", value, "float")
        self._f = value

    f = property(
        fget=_get_f,
        fset=_set_f,
        doc=u"""Base electrical frequency of the simulation

        :Type: float
        """,
    )
