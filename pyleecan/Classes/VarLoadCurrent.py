# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/VarLoadCurrent.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/VarLoadCurrent
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
from .VarLoad import VarLoad

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.VarLoadCurrent.get_input_list import get_input_list
except ImportError as error:
    get_input_list = error

try:
    from ..Methods.Simulation.VarLoadCurrent.generate_simulation_list import (
        generate_simulation_list,
    )
except ImportError as error:
    generate_simulation_list = error

try:
    from ..Methods.Simulation.VarLoadCurrent.check_param import check_param
except ImportError as error:
    check_param = error

try:
    from ..Methods.Simulation.VarLoadCurrent.get_elec_datakeeper import (
        get_elec_datakeeper,
    )
except ImportError as error:
    get_elec_datakeeper = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .DataKeeper import DataKeeper
from .VarSimu import VarSimu
from .Post import Post


class VarLoadCurrent(VarLoad):
    """Generate a multisimulation with InputCurrent at variable operating point"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.VarLoadCurrent.get_input_list
    if isinstance(get_input_list, ImportError):
        get_input_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarLoadCurrent method get_input_list: "
                    + str(get_input_list)
                )
            )
        )
    else:
        get_input_list = get_input_list
    # cf Methods.Simulation.VarLoadCurrent.generate_simulation_list
    if isinstance(generate_simulation_list, ImportError):
        generate_simulation_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarLoadCurrent method generate_simulation_list: "
                    + str(generate_simulation_list)
                )
            )
        )
    else:
        generate_simulation_list = generate_simulation_list
    # cf Methods.Simulation.VarLoadCurrent.check_param
    if isinstance(check_param, ImportError):
        check_param = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarLoadCurrent method check_param: " + str(check_param)
                )
            )
        )
    else:
        check_param = check_param
    # cf Methods.Simulation.VarLoadCurrent.get_elec_datakeeper
    if isinstance(get_elec_datakeeper, ImportError):
        get_elec_datakeeper = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarLoadCurrent method get_elec_datakeeper: "
                    + str(get_elec_datakeeper)
                )
            )
        )
    else:
        get_elec_datakeeper = get_elec_datakeeper
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        OP_matrix=None,
        type_OP_matrix=0,
        is_torque=False,
        is_power=False,
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
            if "OP_matrix" in list(init_dict.keys()):
                OP_matrix = init_dict["OP_matrix"]
            if "type_OP_matrix" in list(init_dict.keys()):
                type_OP_matrix = init_dict["type_OP_matrix"]
            if "is_torque" in list(init_dict.keys()):
                is_torque = init_dict["is_torque"]
            if "is_power" in list(init_dict.keys()):
                is_power = init_dict["is_power"]
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
        self.OP_matrix = OP_matrix
        self.type_OP_matrix = type_OP_matrix
        self.is_torque = is_torque
        self.is_power = is_power
        # Call VarLoad init
        super(VarLoadCurrent, self).__init__(
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
        # The class is frozen (in VarLoad init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        VarLoadCurrent_str = ""
        # Get the properties inherited from VarLoad
        VarLoadCurrent_str += super(VarLoadCurrent, self).__str__()
        VarLoadCurrent_str += (
            "OP_matrix = "
            + linesep
            + str(self.OP_matrix).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        VarLoadCurrent_str += "type_OP_matrix = " + str(self.type_OP_matrix) + linesep
        VarLoadCurrent_str += "is_torque = " + str(self.is_torque) + linesep
        VarLoadCurrent_str += "is_power = " + str(self.is_power) + linesep
        return VarLoadCurrent_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from VarLoad
        if not super(VarLoadCurrent, self).__eq__(other):
            return False
        if not array_equal(other.OP_matrix, self.OP_matrix):
            return False
        if other.type_OP_matrix != self.type_OP_matrix:
            return False
        if other.is_torque != self.is_torque:
            return False
        if other.is_power != self.is_power:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from VarLoad
        diff_list.extend(super(VarLoadCurrent, self).compare(other, name=name))
        if not array_equal(other.OP_matrix, self.OP_matrix):
            diff_list.append(name + ".OP_matrix")
        if other._type_OP_matrix != self._type_OP_matrix:
            diff_list.append(name + ".type_OP_matrix")
        if other._is_torque != self._is_torque:
            diff_list.append(name + ".is_torque")
        if other._is_power != self._is_power:
            diff_list.append(name + ".is_power")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from VarLoad
        S += super(VarLoadCurrent, self).__sizeof__()
        S += getsizeof(self.OP_matrix)
        S += getsizeof(self.type_OP_matrix)
        S += getsizeof(self.is_torque)
        S += getsizeof(self.is_power)
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

        # Get the properties inherited from VarLoad
        VarLoadCurrent_dict = super(VarLoadCurrent, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.OP_matrix is None:
            VarLoadCurrent_dict["OP_matrix"] = None
        else:
            if type_handle_ndarray == 0:
                VarLoadCurrent_dict["OP_matrix"] = self.OP_matrix.tolist()
            elif type_handle_ndarray == 1:
                VarLoadCurrent_dict["OP_matrix"] = self.OP_matrix.copy()
            elif type_handle_ndarray == 2:
                VarLoadCurrent_dict["OP_matrix"] = self.OP_matrix
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        VarLoadCurrent_dict["type_OP_matrix"] = self.type_OP_matrix
        VarLoadCurrent_dict["is_torque"] = self.is_torque
        VarLoadCurrent_dict["is_power"] = self.is_power
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        VarLoadCurrent_dict["__class__"] = "VarLoadCurrent"
        return VarLoadCurrent_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.OP_matrix = None
        self.type_OP_matrix = None
        self.is_torque = None
        self.is_power = None
        # Set to None the properties inherited from VarLoad
        super(VarLoadCurrent, self)._set_None()

    def _get_OP_matrix(self):
        """getter of OP_matrix"""
        return self._OP_matrix

    def _set_OP_matrix(self, value):
        """setter of OP_matrix"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("OP_matrix", value, "ndarray")
        self._OP_matrix = value

    OP_matrix = property(
        fget=_get_OP_matrix,
        fset=_set_OP_matrix,
        doc=u"""Operating point matrix (N0,I0,Phi0,T,P) or (N0,Id,Iq,T,P) 

        :Type: ndarray
        """,
    )

    def _get_type_OP_matrix(self):
        """getter of type_OP_matrix"""
        return self._type_OP_matrix

    def _set_type_OP_matrix(self, value):
        """setter of type_OP_matrix"""
        check_var("type_OP_matrix", value, "int", Vmin=0, Vmax=1)
        self._type_OP_matrix = value

    type_OP_matrix = property(
        fget=_get_type_OP_matrix,
        fset=_set_type_OP_matrix,
        doc=u"""Select which kind of OP_matrix is used 0: (N0,I0,Phi0,T,P), 1:(N0,Id,Iq,T,P) 

        :Type: int
        :min: 0
        :max: 1
        """,
    )

    def _get_is_torque(self):
        """getter of is_torque"""
        return self._is_torque

    def _set_is_torque(self, value):
        """setter of is_torque"""
        check_var("is_torque", value, "bool")
        self._is_torque = value

    is_torque = property(
        fget=_get_is_torque,
        fset=_set_is_torque,
        doc=u"""True if the Torque is defined in OP_matrix

        :Type: bool
        """,
    )

    def _get_is_power(self):
        """getter of is_power"""
        return self._is_power

    def _set_is_power(self, value):
        """setter of is_power"""
        check_var("is_power", value, "bool")
        self._is_power = value

    is_power = property(
        fget=_get_is_power,
        fset=_set_is_power,
        doc=u"""True if the Power is defined in OP_matrix

        :Type: bool
        """,
    )
