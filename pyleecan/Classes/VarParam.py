# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/VarParam.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/VarParam
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
from .VarSimu import VarSimu

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.VarParam.check_param import check_param
except ImportError as error:
    check_param = error

try:
    from ..Methods.Simulation.VarParam.generate_simulation_list import (
        generate_simulation_list,
    )
except ImportError as error:
    generate_simulation_list = error

try:
    from ..Methods.Simulation.VarParam.get_simu_number import get_simu_number
except ImportError as error:
    get_simu_number = error


from ._check import InitUnKnowClassError
from .ParamExplorer import ParamExplorer
from .DataKeeper import DataKeeper
from .VarSimu import VarSimu
from .Post import Post


class VarParam(VarSimu):
    """Handle multisimulation by varying parameters"""

    VERSION = 1
    NAME = "Parameter Sweep"

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.VarParam.check_param
    if isinstance(check_param, ImportError):
        check_param = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarParam method check_param: " + str(check_param)
                )
            )
        )
    else:
        check_param = check_param
    # cf Methods.Simulation.VarParam.generate_simulation_list
    if isinstance(generate_simulation_list, ImportError):
        generate_simulation_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarParam method generate_simulation_list: "
                    + str(generate_simulation_list)
                )
            )
        )
    else:
        generate_simulation_list = generate_simulation_list
    # cf Methods.Simulation.VarParam.get_simu_number
    if isinstance(get_simu_number, ImportError):
        get_simu_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarParam method get_simu_number: " + str(get_simu_number)
                )
            )
        )
    else:
        get_simu_number = get_simu_number
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        paramexplorer_list=-1,
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
            if "paramexplorer_list" in list(init_dict.keys()):
                paramexplorer_list = init_dict["paramexplorer_list"]
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
        # Set the properties (value check and convertion are done in setter)
        self.paramexplorer_list = paramexplorer_list
        # Call VarSimu init
        super(VarParam, self).__init__(
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
        )
        # The class is frozen (in VarSimu init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        VarParam_str = ""
        # Get the properties inherited from VarSimu
        VarParam_str += super(VarParam, self).__str__()
        if len(self.paramexplorer_list) == 0:
            VarParam_str += "paramexplorer_list = []" + linesep
        for ii in range(len(self.paramexplorer_list)):
            tmp = (
                self.paramexplorer_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            VarParam_str += (
                "paramexplorer_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        return VarParam_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from VarSimu
        if not super(VarParam, self).__eq__(other):
            return False
        if other.paramexplorer_list != self.paramexplorer_list:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from VarSimu
        diff_list.extend(super(VarParam, self).compare(other, name=name))
        if (
            other.paramexplorer_list is None and self.paramexplorer_list is not None
        ) or (other.paramexplorer_list is not None and self.paramexplorer_list is None):
            diff_list.append(name + ".paramexplorer_list None mismatch")
        elif self.paramexplorer_list is None:
            pass
        elif len(other.paramexplorer_list) != len(self.paramexplorer_list):
            diff_list.append("len(" + name + ".paramexplorer_list)")
        else:
            for ii in range(len(other.paramexplorer_list)):
                diff_list.extend(
                    self.paramexplorer_list[ii].compare(
                        other.paramexplorer_list[ii],
                        name=name + ".paramexplorer_list[" + str(ii) + "]",
                    )
                )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from VarSimu
        S += super(VarParam, self).__sizeof__()
        if self.paramexplorer_list is not None:
            for value in self.paramexplorer_list:
                S += getsizeof(value)
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
        VarParam_dict = super(VarParam, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.paramexplorer_list is None:
            VarParam_dict["paramexplorer_list"] = None
        else:
            VarParam_dict["paramexplorer_list"] = list()
            for obj in self.paramexplorer_list:
                if obj is not None:
                    VarParam_dict["paramexplorer_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    VarParam_dict["paramexplorer_list"].append(None)
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        VarParam_dict["__class__"] = "VarParam"
        return VarParam_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.paramexplorer_list = None
        # Set to None the properties inherited from VarSimu
        super(VarParam, self)._set_None()

    def _get_paramexplorer_list(self):
        """getter of paramexplorer_list"""
        if self._paramexplorer_list is not None:
            for obj in self._paramexplorer_list:
                if obj is not None:
                    obj.parent = self
        return self._paramexplorer_list

    def _set_paramexplorer_list(self, value):
        """setter of paramexplorer_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "paramexplorer_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("paramexplorer_list", value, "[ParamExplorer]")
        self._paramexplorer_list = value

    paramexplorer_list = property(
        fget=_get_paramexplorer_list,
        fset=_set_paramexplorer_list,
        doc=u"""List containing ParamSetter to define every simulation

        :Type: [ParamExplorer]
        """,
    )
