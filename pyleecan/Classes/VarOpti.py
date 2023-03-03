# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/VarOpti.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/VarOpti
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
from .VarParam import VarParam

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.VarOpti.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Simulation.VarOpti.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Simulation.VarOpti.get_full_solver import get_full_solver
except ImportError as error:
    get_full_solver = error


from numpy import isnan
from ._check import InitUnKnowClassError


class VarOpti(VarParam):
    """Handle Optimization multisimulation by varying parameters"""

    VERSION = 1
    NAME = "Optimization"

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.VarOpti.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use VarOpti method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Simulation.VarOpti.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use VarOpti method run: " + str(run))
            )
        )
    else:
        run = run
    # cf Methods.Simulation.VarOpti.get_full_solver
    if isinstance(get_full_solver, ImportError):
        get_full_solver = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarOpti method get_full_solver: " + str(get_full_solver)
                )
            )
        )
    else:
        get_full_solver = get_full_solver
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        objective_list=-1,
        constraint_list=-1,
        solver=None,
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
            if "objective_list" in list(init_dict.keys()):
                objective_list = init_dict["objective_list"]
            if "constraint_list" in list(init_dict.keys()):
                constraint_list = init_dict["constraint_list"]
            if "solver" in list(init_dict.keys()):
                solver = init_dict["solver"]
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
            if "is_reuse_LUT" in list(init_dict.keys()):
                is_reuse_LUT = init_dict["is_reuse_LUT"]
        # Set the properties (value check and convertion are done in setter)
        self.objective_list = objective_list
        self.constraint_list = constraint_list
        self.solver = solver
        # Call VarParam init
        super(VarOpti, self).__init__(
            paramexplorer_list=paramexplorer_list,
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
        # The class is frozen (in VarParam init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        VarOpti_str = ""
        # Get the properties inherited from VarParam
        VarOpti_str += super(VarOpti, self).__str__()
        if len(self.objective_list) == 0:
            VarOpti_str += "objective_list = []" + linesep
        for ii in range(len(self.objective_list)):
            tmp = (
                self.objective_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            VarOpti_str += "objective_list[" + str(ii) + "] =" + tmp + linesep + linesep
        if len(self.constraint_list) == 0:
            VarOpti_str += "constraint_list = []" + linesep
        for ii in range(len(self.constraint_list)):
            tmp = (
                self.constraint_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            VarOpti_str += (
                "constraint_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        if self.solver is not None:
            tmp = self.solver.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            VarOpti_str += "solver = " + tmp
        else:
            VarOpti_str += "solver = None" + linesep + linesep
        return VarOpti_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from VarParam
        if not super(VarOpti, self).__eq__(other):
            return False
        if other.objective_list != self.objective_list:
            return False
        if other.constraint_list != self.constraint_list:
            return False
        if other.solver != self.solver:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from VarParam
        diff_list.extend(
            super(VarOpti, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.objective_list is None and self.objective_list is not None) or (
            other.objective_list is not None and self.objective_list is None
        ):
            diff_list.append(name + ".objective_list None mismatch")
        elif self.objective_list is None:
            pass
        elif len(other.objective_list) != len(self.objective_list):
            diff_list.append("len(" + name + ".objective_list)")
        else:
            for ii in range(len(other.objective_list)):
                diff_list.extend(
                    self.objective_list[ii].compare(
                        other.objective_list[ii],
                        name=name + ".objective_list[" + str(ii) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
        if (other.constraint_list is None and self.constraint_list is not None) or (
            other.constraint_list is not None and self.constraint_list is None
        ):
            diff_list.append(name + ".constraint_list None mismatch")
        elif self.constraint_list is None:
            pass
        elif len(other.constraint_list) != len(self.constraint_list):
            diff_list.append("len(" + name + ".constraint_list)")
        else:
            for ii in range(len(other.constraint_list)):
                diff_list.extend(
                    self.constraint_list[ii].compare(
                        other.constraint_list[ii],
                        name=name + ".constraint_list[" + str(ii) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
        if (other.solver is None and self.solver is not None) or (
            other.solver is not None and self.solver is None
        ):
            diff_list.append(name + ".solver None mismatch")
        elif self.solver is not None:
            diff_list.extend(
                self.solver.compare(
                    other.solver,
                    name=name + ".solver",
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

        # Get size of the properties inherited from VarParam
        S += super(VarOpti, self).__sizeof__()
        if self.objective_list is not None:
            for value in self.objective_list:
                S += getsizeof(value)
        if self.constraint_list is not None:
            for value in self.constraint_list:
                S += getsizeof(value)
        S += getsizeof(self.solver)
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

        # Get the properties inherited from VarParam
        VarOpti_dict = super(VarOpti, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.objective_list is None:
            VarOpti_dict["objective_list"] = None
        else:
            VarOpti_dict["objective_list"] = list()
            for obj in self.objective_list:
                if obj is not None:
                    VarOpti_dict["objective_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    VarOpti_dict["objective_list"].append(None)
        if self.constraint_list is None:
            VarOpti_dict["constraint_list"] = None
        else:
            VarOpti_dict["constraint_list"] = list()
            for obj in self.constraint_list:
                if obj is not None:
                    VarOpti_dict["constraint_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    VarOpti_dict["constraint_list"].append(None)
        if self.solver is None:
            VarOpti_dict["solver"] = None
        else:
            VarOpti_dict["solver"] = self.solver.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        VarOpti_dict["__class__"] = "VarOpti"
        return VarOpti_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.objective_list is None:
            objective_list_val = None
        else:
            objective_list_val = list()
            for obj in self.objective_list:
                objective_list_val.append(obj.copy())
        if self.constraint_list is None:
            constraint_list_val = None
        else:
            constraint_list_val = list()
            for obj in self.constraint_list:
                constraint_list_val.append(obj.copy())
        if self.solver is None:
            solver_val = None
        else:
            solver_val = self.solver.copy()
        if self.paramexplorer_list is None:
            paramexplorer_list_val = None
        else:
            paramexplorer_list_val = list()
            for obj in self.paramexplorer_list:
                paramexplorer_list_val.append(obj.copy())
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
            objective_list=objective_list_val,
            constraint_list=constraint_list_val,
            solver=solver_val,
            paramexplorer_list=paramexplorer_list_val,
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

        self.objective_list = None
        self.constraint_list = None
        if self.solver is not None:
            self.solver._set_None()
        # Set to None the properties inherited from VarParam
        super(VarOpti, self)._set_None()

    def _get_objective_list(self):
        """getter of objective_list"""
        if self._objective_list is not None:
            for obj in self._objective_list:
                if obj is not None:
                    obj.parent = self
        return self._objective_list

    def _set_objective_list(self, value):
        """setter of objective_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "objective_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("objective_list", value, "[OptiObjective]")
        self._objective_list = value

    objective_list = property(
        fget=_get_objective_list,
        fset=_set_objective_list,
        doc=u"""List containing OptiObjective objects

        :Type: [OptiObjective]
        """,
    )

    def _get_constraint_list(self):
        """getter of constraint_list"""
        if self._constraint_list is not None:
            for obj in self._constraint_list:
                if obj is not None:
                    obj.parent = self
        return self._constraint_list

    def _set_constraint_list(self, value):
        """setter of constraint_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "constraint_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("constraint_list", value, "[OptiConstraint]")
        self._constraint_list = value

    constraint_list = property(
        fget=_get_constraint_list,
        fset=_set_constraint_list,
        doc=u"""List containing OptiConstraint objects

        :Type: [OptiConstraint]
        """,
    )

    def _get_solver(self):
        """getter of solver"""
        return self._solver

    def _set_solver(self, value):
        """setter of solver"""
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
                "pyleecan.Classes", value.get("__class__"), "solver"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            OptiSolver = import_class("pyleecan.Classes", "OptiSolver", "solver")
            value = OptiSolver()
        check_var("solver", value, "OptiSolver")
        self._solver = value

        if self._solver is not None:
            self._solver.parent = self

    solver = property(
        fget=_get_solver,
        fset=_set_solver,
        doc=u"""Object that solve an OptiProblem

        :Type: OptiSolver
        """,
    )
