# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/VarSimu.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/VarSimu
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
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.VarSimu.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Simulation.VarSimu.set_reused_data import set_reused_data
except ImportError as error:
    set_reused_data = error

try:
    from ..Methods.Simulation.VarSimu.check_param import check_param
except ImportError as error:
    check_param = error

try:
    from ..Methods.Simulation.VarSimu.generate_simulation_list import (
        generate_simulation_list,
    )
except ImportError as error:
    generate_simulation_list = error

try:
    from ..Methods.Simulation.VarSimu.gen_datakeeper_list import gen_datakeeper_list
except ImportError as error:
    gen_datakeeper_list = error

try:
    from ..Methods.Simulation.VarSimu.get_elec_datakeeper import get_elec_datakeeper
except ImportError as error:
    get_elec_datakeeper = error

try:
    from ..Methods.Simulation.VarSimu.get_mag_datakeeper import get_mag_datakeeper
except ImportError as error:
    get_mag_datakeeper = error

try:
    from ..Methods.Simulation.VarSimu.get_force_datakeeper import get_force_datakeeper
except ImportError as error:
    get_force_datakeeper = error

try:
    from ..Methods.Simulation.VarSimu.get_ref_simu_index import get_ref_simu_index
except ImportError as error:
    get_ref_simu_index = error


from ._check import InitUnKnowClassError
from .DataKeeper import DataKeeper
from .Post import Post


class VarSimu(FrozenClass):
    """Abstract class for the multi-simulation"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.VarSimu.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use VarSimu method run: " + str(run))
            )
        )
    else:
        run = run
    # cf Methods.Simulation.VarSimu.set_reused_data
    if isinstance(set_reused_data, ImportError):
        set_reused_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarSimu method set_reused_data: " + str(set_reused_data)
                )
            )
        )
    else:
        set_reused_data = set_reused_data
    # cf Methods.Simulation.VarSimu.check_param
    if isinstance(check_param, ImportError):
        check_param = property(
            fget=lambda x: raise_(
                ImportError("Can't use VarSimu method check_param: " + str(check_param))
            )
        )
    else:
        check_param = check_param
    # cf Methods.Simulation.VarSimu.generate_simulation_list
    if isinstance(generate_simulation_list, ImportError):
        generate_simulation_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarSimu method generate_simulation_list: "
                    + str(generate_simulation_list)
                )
            )
        )
    else:
        generate_simulation_list = generate_simulation_list
    # cf Methods.Simulation.VarSimu.gen_datakeeper_list
    if isinstance(gen_datakeeper_list, ImportError):
        gen_datakeeper_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarSimu method gen_datakeeper_list: "
                    + str(gen_datakeeper_list)
                )
            )
        )
    else:
        gen_datakeeper_list = gen_datakeeper_list
    # cf Methods.Simulation.VarSimu.get_elec_datakeeper
    if isinstance(get_elec_datakeeper, ImportError):
        get_elec_datakeeper = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarSimu method get_elec_datakeeper: "
                    + str(get_elec_datakeeper)
                )
            )
        )
    else:
        get_elec_datakeeper = get_elec_datakeeper
    # cf Methods.Simulation.VarSimu.get_mag_datakeeper
    if isinstance(get_mag_datakeeper, ImportError):
        get_mag_datakeeper = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarSimu method get_mag_datakeeper: "
                    + str(get_mag_datakeeper)
                )
            )
        )
    else:
        get_mag_datakeeper = get_mag_datakeeper
    # cf Methods.Simulation.VarSimu.get_force_datakeeper
    if isinstance(get_force_datakeeper, ImportError):
        get_force_datakeeper = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarSimu method get_force_datakeeper: "
                    + str(get_force_datakeeper)
                )
            )
        )
    else:
        get_force_datakeeper = get_force_datakeeper
    # cf Methods.Simulation.VarSimu.get_ref_simu_index
    if isinstance(get_ref_simu_index, ImportError):
        get_ref_simu_index = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarSimu method get_ref_simu_index: "
                    + str(get_ref_simu_index)
                )
            )
        )
    else:
        get_ref_simu_index = get_ref_simu_index
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
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
        self.parent = None
        self.name = name
        self.desc = desc
        self.datakeeper_list = datakeeper_list
        self.is_keep_all_output = is_keep_all_output
        self.stop_if_error = stop_if_error
        self.var_simu = var_simu
        self.nb_simu = nb_simu
        self.is_reuse_femm_file = is_reuse_femm_file
        self.postproc_list = postproc_list
        self.pre_keeper_postproc_list = pre_keeper_postproc_list
        self.post_keeper_postproc_list = post_keeper_postproc_list

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        VarSimu_str = ""
        if self.parent is None:
            VarSimu_str += "parent = None " + linesep
        else:
            VarSimu_str += "parent = " + str(type(self.parent)) + " object" + linesep
        VarSimu_str += 'name = "' + str(self.name) + '"' + linesep
        VarSimu_str += 'desc = "' + str(self.desc) + '"' + linesep
        if len(self.datakeeper_list) == 0:
            VarSimu_str += "datakeeper_list = []" + linesep
        for ii in range(len(self.datakeeper_list)):
            tmp = (
                self.datakeeper_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            VarSimu_str += (
                "datakeeper_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        VarSimu_str += "is_keep_all_output = " + str(self.is_keep_all_output) + linesep
        VarSimu_str += "stop_if_error = " + str(self.stop_if_error) + linesep
        if self.var_simu is not None:
            tmp = self.var_simu.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            VarSimu_str += "var_simu = " + tmp
        else:
            VarSimu_str += "var_simu = None" + linesep + linesep
        VarSimu_str += "nb_simu = " + str(self.nb_simu) + linesep
        VarSimu_str += "is_reuse_femm_file = " + str(self.is_reuse_femm_file) + linesep
        if len(self.postproc_list) == 0:
            VarSimu_str += "postproc_list = []" + linesep
        for ii in range(len(self.postproc_list)):
            tmp = (
                self.postproc_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            VarSimu_str += "postproc_list[" + str(ii) + "] =" + tmp + linesep + linesep
        if len(self.pre_keeper_postproc_list) == 0:
            VarSimu_str += "pre_keeper_postproc_list = []" + linesep
        for ii in range(len(self.pre_keeper_postproc_list)):
            tmp = (
                self.pre_keeper_postproc_list[ii]
                .__str__()
                .replace(linesep, linesep + "\t")
                + linesep
            )
            VarSimu_str += (
                "pre_keeper_postproc_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        if len(self.post_keeper_postproc_list) == 0:
            VarSimu_str += "post_keeper_postproc_list = []" + linesep
        for ii in range(len(self.post_keeper_postproc_list)):
            tmp = (
                self.post_keeper_postproc_list[ii]
                .__str__()
                .replace(linesep, linesep + "\t")
                + linesep
            )
            VarSimu_str += (
                "post_keeper_postproc_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        return VarSimu_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        if other.desc != self.desc:
            return False
        if other.datakeeper_list != self.datakeeper_list:
            return False
        if other.is_keep_all_output != self.is_keep_all_output:
            return False
        if other.stop_if_error != self.stop_if_error:
            return False
        if other.var_simu != self.var_simu:
            return False
        if other.nb_simu != self.nb_simu:
            return False
        if other.is_reuse_femm_file != self.is_reuse_femm_file:
            return False
        if other.postproc_list != self.postproc_list:
            return False
        if other.pre_keeper_postproc_list != self.pre_keeper_postproc_list:
            return False
        if other.post_keeper_postproc_list != self.post_keeper_postproc_list:
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
        if other._desc != self._desc:
            diff_list.append(name + ".desc")
        if (other.datakeeper_list is None and self.datakeeper_list is not None) or (
            other.datakeeper_list is not None and self.datakeeper_list is None
        ):
            diff_list.append(name + ".datakeeper_list None mismatch")
        elif self.datakeeper_list is None:
            pass
        elif len(other.datakeeper_list) != len(self.datakeeper_list):
            diff_list.append("len(" + name + ".datakeeper_list)")
        else:
            for ii in range(len(other.datakeeper_list)):
                diff_list.extend(
                    self.datakeeper_list[ii].compare(
                        other.datakeeper_list[ii],
                        name=name + ".datakeeper_list[" + str(ii) + "]",
                    )
                )
        if other._is_keep_all_output != self._is_keep_all_output:
            diff_list.append(name + ".is_keep_all_output")
        if other._stop_if_error != self._stop_if_error:
            diff_list.append(name + ".stop_if_error")
        if (other.var_simu is None and self.var_simu is not None) or (
            other.var_simu is not None and self.var_simu is None
        ):
            diff_list.append(name + ".var_simu None mismatch")
        elif self.var_simu is not None:
            diff_list.extend(
                self.var_simu.compare(other.var_simu, name=name + ".var_simu")
            )
        if other._nb_simu != self._nb_simu:
            diff_list.append(name + ".nb_simu")
        if other._is_reuse_femm_file != self._is_reuse_femm_file:
            diff_list.append(name + ".is_reuse_femm_file")
        if (other.postproc_list is None and self.postproc_list is not None) or (
            other.postproc_list is not None and self.postproc_list is None
        ):
            diff_list.append(name + ".postproc_list None mismatch")
        elif self.postproc_list is None:
            pass
        elif len(other.postproc_list) != len(self.postproc_list):
            diff_list.append("len(" + name + ".postproc_list)")
        else:
            for ii in range(len(other.postproc_list)):
                diff_list.extend(
                    self.postproc_list[ii].compare(
                        other.postproc_list[ii],
                        name=name + ".postproc_list[" + str(ii) + "]",
                    )
                )
        if (
            other.pre_keeper_postproc_list is None
            and self.pre_keeper_postproc_list is not None
        ) or (
            other.pre_keeper_postproc_list is not None
            and self.pre_keeper_postproc_list is None
        ):
            diff_list.append(name + ".pre_keeper_postproc_list None mismatch")
        elif self.pre_keeper_postproc_list is None:
            pass
        elif len(other.pre_keeper_postproc_list) != len(self.pre_keeper_postproc_list):
            diff_list.append("len(" + name + ".pre_keeper_postproc_list)")
        else:
            for ii in range(len(other.pre_keeper_postproc_list)):
                diff_list.extend(
                    self.pre_keeper_postproc_list[ii].compare(
                        other.pre_keeper_postproc_list[ii],
                        name=name + ".pre_keeper_postproc_list[" + str(ii) + "]",
                    )
                )
        if (
            other.post_keeper_postproc_list is None
            and self.post_keeper_postproc_list is not None
        ) or (
            other.post_keeper_postproc_list is not None
            and self.post_keeper_postproc_list is None
        ):
            diff_list.append(name + ".post_keeper_postproc_list None mismatch")
        elif self.post_keeper_postproc_list is None:
            pass
        elif len(other.post_keeper_postproc_list) != len(
            self.post_keeper_postproc_list
        ):
            diff_list.append("len(" + name + ".post_keeper_postproc_list)")
        else:
            for ii in range(len(other.post_keeper_postproc_list)):
                diff_list.extend(
                    self.post_keeper_postproc_list[ii].compare(
                        other.post_keeper_postproc_list[ii],
                        name=name + ".post_keeper_postproc_list[" + str(ii) + "]",
                    )
                )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.name)
        S += getsizeof(self.desc)
        if self.datakeeper_list is not None:
            for value in self.datakeeper_list:
                S += getsizeof(value)
        S += getsizeof(self.is_keep_all_output)
        S += getsizeof(self.stop_if_error)
        S += getsizeof(self.var_simu)
        S += getsizeof(self.nb_simu)
        S += getsizeof(self.is_reuse_femm_file)
        if self.postproc_list is not None:
            for value in self.postproc_list:
                S += getsizeof(value)
        if self.pre_keeper_postproc_list is not None:
            for value in self.pre_keeper_postproc_list:
                S += getsizeof(value)
        if self.post_keeper_postproc_list is not None:
            for value in self.post_keeper_postproc_list:
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

        VarSimu_dict = dict()
        VarSimu_dict["name"] = self.name
        VarSimu_dict["desc"] = self.desc
        if self.datakeeper_list is None:
            VarSimu_dict["datakeeper_list"] = None
        else:
            VarSimu_dict["datakeeper_list"] = list()
            for obj in self.datakeeper_list:
                if obj is not None:
                    VarSimu_dict["datakeeper_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    VarSimu_dict["datakeeper_list"].append(None)
        VarSimu_dict["is_keep_all_output"] = self.is_keep_all_output
        VarSimu_dict["stop_if_error"] = self.stop_if_error
        if self.var_simu is None:
            VarSimu_dict["var_simu"] = None
        else:
            VarSimu_dict["var_simu"] = self.var_simu.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        VarSimu_dict["nb_simu"] = self.nb_simu
        VarSimu_dict["is_reuse_femm_file"] = self.is_reuse_femm_file
        if self.postproc_list is None:
            VarSimu_dict["postproc_list"] = None
        else:
            VarSimu_dict["postproc_list"] = list()
            for obj in self.postproc_list:
                if obj is not None:
                    VarSimu_dict["postproc_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    VarSimu_dict["postproc_list"].append(None)
        if self.pre_keeper_postproc_list is None:
            VarSimu_dict["pre_keeper_postproc_list"] = None
        else:
            VarSimu_dict["pre_keeper_postproc_list"] = list()
            for obj in self.pre_keeper_postproc_list:
                if obj is not None:
                    VarSimu_dict["pre_keeper_postproc_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    VarSimu_dict["pre_keeper_postproc_list"].append(None)
        if self.post_keeper_postproc_list is None:
            VarSimu_dict["post_keeper_postproc_list"] = None
        else:
            VarSimu_dict["post_keeper_postproc_list"] = list()
            for obj in self.post_keeper_postproc_list:
                if obj is not None:
                    VarSimu_dict["post_keeper_postproc_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    VarSimu_dict["post_keeper_postproc_list"].append(None)
        # The class name is added to the dict for deserialisation purpose
        VarSimu_dict["__class__"] = "VarSimu"
        return VarSimu_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.desc = None
        self.datakeeper_list = None
        self.is_keep_all_output = None
        self.stop_if_error = None
        if self.var_simu is not None:
            self.var_simu._set_None()
        self.nb_simu = None
        self.is_reuse_femm_file = None
        self.postproc_list = None
        self.pre_keeper_postproc_list = None
        self.post_keeper_postproc_list = None

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
        doc=u"""Name of the multi-simulation

        :Type: str
        """,
    )

    def _get_desc(self):
        """getter of desc"""
        return self._desc

    def _set_desc(self, value):
        """setter of desc"""
        check_var("desc", value, "str")
        self._desc = value

    desc = property(
        fget=_get_desc,
        fset=_set_desc,
        doc=u"""Multi-simulation description

        :Type: str
        """,
    )

    def _get_datakeeper_list(self):
        """getter of datakeeper_list"""
        if self._datakeeper_list is not None:
            for obj in self._datakeeper_list:
                if obj is not None:
                    obj.parent = self
        return self._datakeeper_list

    def _set_datakeeper_list(self, value):
        """setter of datakeeper_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "datakeeper_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("datakeeper_list", value, "[DataKeeper]")
        self._datakeeper_list = value

    datakeeper_list = property(
        fget=_get_datakeeper_list,
        fset=_set_datakeeper_list,
        doc=u"""List containing DataKeepers to extract VarSimu results 

        :Type: [DataKeeper]
        """,
    )

    def _get_is_keep_all_output(self):
        """getter of is_keep_all_output"""
        return self._is_keep_all_output

    def _set_is_keep_all_output(self, value):
        """setter of is_keep_all_output"""
        check_var("is_keep_all_output", value, "bool")
        self._is_keep_all_output = value

    is_keep_all_output = property(
        fget=_get_is_keep_all_output,
        fset=_set_is_keep_all_output,
        doc=u"""True to store every output in a list

        :Type: bool
        """,
    )

    def _get_stop_if_error(self):
        """getter of stop_if_error"""
        return self._stop_if_error

    def _set_stop_if_error(self, value):
        """setter of stop_if_error"""
        check_var("stop_if_error", value, "bool")
        self._stop_if_error = value

    stop_if_error = property(
        fget=_get_stop_if_error,
        fset=_set_stop_if_error,
        doc=u"""Stop the multi-simulation if a simulation fails 

        :Type: bool
        """,
    )

    def _get_var_simu(self):
        """getter of var_simu"""
        return self._var_simu

    def _set_var_simu(self, value):
        """setter of var_simu"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "var_simu"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = VarSimu()
        check_var("var_simu", value, "VarSimu")
        self._var_simu = value

        if self._var_simu is not None:
            self._var_simu.parent = self

    var_simu = property(
        fget=_get_var_simu,
        fset=_set_var_simu,
        doc=u"""Multi-simulation of a Multi-simulation definition

        :Type: VarSimu
        """,
    )

    def _get_nb_simu(self):
        """getter of nb_simu"""
        return self._nb_simu

    def _set_nb_simu(self, value):
        """setter of nb_simu"""
        check_var("nb_simu", value, "int")
        self._nb_simu = value

    nb_simu = property(
        fget=_get_nb_simu,
        fset=_set_nb_simu,
        doc=u"""Number of simulations

        :Type: int
        """,
    )

    def _get_is_reuse_femm_file(self):
        """getter of is_reuse_femm_file"""
        return self._is_reuse_femm_file

    def _set_is_reuse_femm_file(self, value):
        """setter of is_reuse_femm_file"""
        check_var("is_reuse_femm_file", value, "bool")
        self._is_reuse_femm_file = value

    is_reuse_femm_file = property(
        fget=_get_is_reuse_femm_file,
        fset=_set_is_reuse_femm_file,
        doc=u"""True to reuse the femm file for each simulation (draw the machine only once, MagFEMM only)

        :Type: bool
        """,
    )

    def _get_postproc_list(self):
        """getter of postproc_list"""
        if self._postproc_list is not None:
            for obj in self._postproc_list:
                if obj is not None:
                    obj.parent = self
        return self._postproc_list

    def _set_postproc_list(self, value):
        """setter of postproc_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "postproc_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("postproc_list", value, "[Post]")
        self._postproc_list = value

    postproc_list = property(
        fget=_get_postproc_list,
        fset=_set_postproc_list,
        doc=u"""List of post-processing to run on XOutput after the multisimulation

        :Type: [Post]
        """,
    )

    def _get_pre_keeper_postproc_list(self):
        """getter of pre_keeper_postproc_list"""
        if self._pre_keeper_postproc_list is not None:
            for obj in self._pre_keeper_postproc_list:
                if obj is not None:
                    obj.parent = self
        return self._pre_keeper_postproc_list

    def _set_pre_keeper_postproc_list(self, value):
        """setter of pre_keeper_postproc_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes",
                        obj.get("__class__"),
                        "pre_keeper_postproc_list",
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("pre_keeper_postproc_list", value, "[Post]")
        self._pre_keeper_postproc_list = value

    pre_keeper_postproc_list = property(
        fget=_get_pre_keeper_postproc_list,
        fset=_set_pre_keeper_postproc_list,
        doc=u"""If not None, replace the reference simulation postproc_list in each generated simulation (run before datakeeper)

        :Type: [Post]
        """,
    )

    def _get_post_keeper_postproc_list(self):
        """getter of post_keeper_postproc_list"""
        if self._post_keeper_postproc_list is not None:
            for obj in self._post_keeper_postproc_list:
                if obj is not None:
                    obj.parent = self
        return self._post_keeper_postproc_list

    def _set_post_keeper_postproc_list(self, value):
        """setter of post_keeper_postproc_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes",
                        obj.get("__class__"),
                        "post_keeper_postproc_list",
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("post_keeper_postproc_list", value, "[Post]")
        self._post_keeper_postproc_list = value

    post_keeper_postproc_list = property(
        fget=_get_post_keeper_postproc_list,
        fset=_set_post_keeper_postproc_list,
        doc=u"""List of post-processing to run on output after each simulation (except reference one) after the datakeeper.

        :Type: [Post]
        """,
    )
