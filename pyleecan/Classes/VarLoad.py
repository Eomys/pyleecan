# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/VarLoad.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/VarLoad
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
from .VarSimu import VarSimu

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.VarLoad.get_ref_simu_index import get_ref_simu_index
except ImportError as error:
    get_ref_simu_index = error

try:
    from ..Methods.Simulation.VarLoad.get_OP_array import get_OP_array
except ImportError as error:
    get_OP_array = error

try:
    from ..Methods.Simulation.VarLoad.set_OP_array import set_OP_array
except ImportError as error:
    set_OP_array = error

try:
    from ..Methods.Simulation.VarLoad._set_OP_matrix import _set_OP_matrix
except ImportError as error:
    _set_OP_matrix = error


from numpy import isnan
from ._check import InitUnKnowClassError


class VarLoad(VarSimu):
    """Abstract class to generate multi-simulation by changing the operating point"""

    VERSION = 1
    NAME = "Variable Load"

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.VarLoad.get_ref_simu_index
    if isinstance(get_ref_simu_index, ImportError):
        get_ref_simu_index = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarLoad method get_ref_simu_index: "
                    + str(get_ref_simu_index)
                )
            )
        )
    else:
        get_ref_simu_index = get_ref_simu_index
    # cf Methods.Simulation.VarLoad.get_OP_array
    if isinstance(get_OP_array, ImportError):
        get_OP_array = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarLoad method get_OP_array: " + str(get_OP_array)
                )
            )
        )
    else:
        get_OP_array = get_OP_array
    # cf Methods.Simulation.VarLoad.set_OP_array
    if isinstance(set_OP_array, ImportError):
        set_OP_array = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarLoad method set_OP_array: " + str(set_OP_array)
                )
            )
        )
    else:
        set_OP_array = set_OP_array
    # cf Methods.Simulation.VarLoad._set_OP_matrix
    if isinstance(_set_OP_matrix, ImportError):
        _set_OP_matrix = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarLoad method _set_OP_matrix: " + str(_set_OP_matrix)
                )
            )
        )
    else:
        _set_OP_matrix = _set_OP_matrix
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        OP_matrix=None,
        name="",
        desc="",
        datakeeper_list=-1,
        is_keep_all_output=False,
        stop_if_error=False,
        var_simu=None,
        nb_simu=0,
        is_reuse_femm_file=True,
        postproc_list=-1,
        pre_keeper_postproc_list=None,
        post_keeper_postproc_list=None,
        is_reuse_LUT=True,
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
            if "OP_matrix" in list(init_dict.keys()):
                OP_matrix = init_dict["OP_matrix"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "datakeeper_list" in list(init_dict.keys()):
                datakeeper_list = init_dict["datakeeper_list"]
            if "is_keep_all_output" in list(init_dict.keys()):
                is_keep_all_output = init_dict["is_keep_all_output"]
            if "stop_if_error" in list(init_dict.keys()):
                stop_if_error = init_dict["stop_if_error"]
            if "var_simu" in list(init_dict.keys()):
                var_simu = init_dict["var_simu"]
            if "nb_simu" in list(init_dict.keys()):
                nb_simu = init_dict["nb_simu"]
            if "is_reuse_femm_file" in list(init_dict.keys()):
                is_reuse_femm_file = init_dict["is_reuse_femm_file"]
            if "postproc_list" in list(init_dict.keys()):
                postproc_list = init_dict["postproc_list"]
            if "pre_keeper_postproc_list" in list(init_dict.keys()):
                pre_keeper_postproc_list = init_dict["pre_keeper_postproc_list"]
            if "post_keeper_postproc_list" in list(init_dict.keys()):
                post_keeper_postproc_list = init_dict["post_keeper_postproc_list"]
            if "is_reuse_LUT" in list(init_dict.keys()):
                is_reuse_LUT = init_dict["is_reuse_LUT"]
        # Set the properties (value check and convertion are done in setter)
        self.OP_matrix = OP_matrix
        # Call VarSimu init
        super(VarLoad, self).__init__(
            name=name,
            desc=desc,
            datakeeper_list=datakeeper_list,
            is_keep_all_output=is_keep_all_output,
            stop_if_error=stop_if_error,
            var_simu=var_simu,
            nb_simu=nb_simu,
            is_reuse_femm_file=is_reuse_femm_file,
            postproc_list=postproc_list,
            pre_keeper_postproc_list=pre_keeper_postproc_list,
            post_keeper_postproc_list=post_keeper_postproc_list,
            is_reuse_LUT=is_reuse_LUT,
        )
        # The class is frozen (in VarSimu init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        VarLoad_str = ""
        # Get the properties inherited from VarSimu
        VarLoad_str += super(VarLoad, self).__str__()
        if self.OP_matrix is not None:
            tmp = self.OP_matrix.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            VarLoad_str += "OP_matrix = " + tmp
        else:
            VarLoad_str += "OP_matrix = None" + linesep + linesep
        return VarLoad_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from VarSimu
        if not super(VarLoad, self).__eq__(other):
            return False
        if other.OP_matrix != self.OP_matrix:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from VarSimu
        diff_list.extend(
            super(VarLoad, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.OP_matrix is None and self.OP_matrix is not None) or (
            other.OP_matrix is not None and self.OP_matrix is None
        ):
            diff_list.append(name + ".OP_matrix None mismatch")
        elif self.OP_matrix is not None:
            diff_list.extend(
                self.OP_matrix.compare(
                    other.OP_matrix,
                    name=name + ".OP_matrix",
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

        # Get size of the properties inherited from VarSimu
        S += super(VarLoad, self).__sizeof__()
        S += getsizeof(self.OP_matrix)
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

        # Get the properties inherited from VarSimu
        VarLoad_dict = super(VarLoad, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.OP_matrix is None:
            VarLoad_dict["OP_matrix"] = None
        else:
            VarLoad_dict["OP_matrix"] = self.OP_matrix.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        VarLoad_dict["__class__"] = "VarLoad"
        return VarLoad_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.OP_matrix is None:
            OP_matrix_val = None
        else:
            OP_matrix_val = self.OP_matrix.copy()
        name_val = self.name
        desc_val = self.desc
        if self.datakeeper_list is None:
            datakeeper_list_val = None
        else:
            datakeeper_list_val = list()
            for obj in self.datakeeper_list:
                datakeeper_list_val.append(obj.copy())
        is_keep_all_output_val = self.is_keep_all_output
        stop_if_error_val = self.stop_if_error
        if self.var_simu is None:
            var_simu_val = None
        else:
            var_simu_val = self.var_simu.copy()
        nb_simu_val = self.nb_simu
        is_reuse_femm_file_val = self.is_reuse_femm_file
        if self.postproc_list is None:
            postproc_list_val = None
        else:
            postproc_list_val = list()
            for obj in self.postproc_list:
                postproc_list_val.append(obj.copy())
        if self.pre_keeper_postproc_list is None:
            pre_keeper_postproc_list_val = None
        else:
            pre_keeper_postproc_list_val = list()
            for obj in self.pre_keeper_postproc_list:
                pre_keeper_postproc_list_val.append(obj.copy())
        if self.post_keeper_postproc_list is None:
            post_keeper_postproc_list_val = None
        else:
            post_keeper_postproc_list_val = list()
            for obj in self.post_keeper_postproc_list:
                post_keeper_postproc_list_val.append(obj.copy())
        is_reuse_LUT_val = self.is_reuse_LUT
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            OP_matrix=OP_matrix_val,
            name=name_val,
            desc=desc_val,
            datakeeper_list=datakeeper_list_val,
            is_keep_all_output=is_keep_all_output_val,
            stop_if_error=stop_if_error_val,
            var_simu=var_simu_val,
            nb_simu=nb_simu_val,
            is_reuse_femm_file=is_reuse_femm_file_val,
            postproc_list=postproc_list_val,
            pre_keeper_postproc_list=pre_keeper_postproc_list_val,
            post_keeper_postproc_list=post_keeper_postproc_list_val,
            is_reuse_LUT=is_reuse_LUT_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.OP_matrix is not None:
            self.OP_matrix._set_None()
        # Set to None the properties inherited from VarSimu
        super(VarLoad, self)._set_None()

    def _get_OP_matrix(self):
        """getter of OP_matrix"""
        return self._OP_matrix

    OP_matrix = property(
        fget=_get_OP_matrix,
        fset=_set_OP_matrix,
        doc=u"""Operating point matrix object

        :Type: OPMatrix
        """,
    )
