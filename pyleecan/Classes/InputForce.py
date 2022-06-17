# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/InputForce.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/InputForce
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
from .Input import Input

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.InputForce.gen_input import gen_input
except ImportError as error:
    gen_input = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class InputForce(Input):
    """Input to start with the structural one """

    VERSION = 1

    # cf Methods.Simulation.InputForce.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError("Can't use InputForce method gen_input: " + str(gen_input))
            )
        )
    else:
        gen_input = gen_input
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        P=None,
        time=None,
        angle=None,
        Nt_tot=2048,
        Nrev=None,
        Na_tot=2048,
        OP=None,
        t_final=None,
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
            if "P" in list(init_dict.keys()):
                P = init_dict["P"]
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Nrev" in list(init_dict.keys()):
                Nrev = init_dict["Nrev"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
            if "OP" in list(init_dict.keys()):
                OP = init_dict["OP"]
            if "t_final" in list(init_dict.keys()):
                t_final = init_dict["t_final"]
        # Set the properties (value check and convertion are done in setter)
        self.P = P
        # Call Input init
        super(InputForce, self).__init__(
            time=time,
            angle=angle,
            Nt_tot=Nt_tot,
            Nrev=Nrev,
            Na_tot=Na_tot,
            OP=OP,
            t_final=t_final,
        )
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        InputForce_str = ""
        # Get the properties inherited from Input
        InputForce_str += super(InputForce, self).__str__()
        if self.P is not None:
            tmp = self.P.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputForce_str += "P = " + tmp
        else:
            InputForce_str += "P = None" + linesep + linesep
        return InputForce_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InputForce, self).__eq__(other):
            return False
        if other.P != self.P:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Input
        diff_list.extend(
            super(InputForce, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.P is None and self.P is not None) or (
            other.P is not None and self.P is None
        ):
            diff_list.append(name + ".P None mismatch")
        elif self.P is not None:
            diff_list.extend(
                self.P.compare(
                    other.P,
                    name=name + ".P",
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

        # Get size of the properties inherited from Input
        S += super(InputForce, self).__sizeof__()
        S += getsizeof(self.P)
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

        # Get the properties inherited from Input
        InputForce_dict = super(InputForce, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.P is None:
            InputForce_dict["P"] = None
        else:
            InputForce_dict["P"] = self.P.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        InputForce_dict["__class__"] = "InputForce"
        return InputForce_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.P is None:
            P_val = None
        else:
            P_val = self.P.copy()
        if self.time is None:
            time_val = None
        else:
            time_val = self.time.copy()
        if self.angle is None:
            angle_val = None
        else:
            angle_val = self.angle.copy()
        Nt_tot_val = self.Nt_tot
        Nrev_val = self.Nrev
        Na_tot_val = self.Na_tot
        if self.OP is None:
            OP_val = None
        else:
            OP_val = self.OP.copy()
        t_final_val = self.t_final
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            P=P_val,
            time=time_val,
            angle=angle_val,
            Nt_tot=Nt_tot_val,
            Nrev=Nrev_val,
            Na_tot=Na_tot_val,
            OP=OP_val,
            t_final=t_final_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.P is not None:
            self.P._set_None()
        # Set to None the properties inherited from Input
        super(InputForce, self)._set_None()

    def _get_P(self):
        """getter of P"""
        return self._P

    def _set_P(self, value):
        """setter of P"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "P")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            ImportVectorField = import_class(
                "pyleecan.Classes", "ImportVectorField", "P"
            )
            value = ImportVectorField()
        check_var("P", value, "ImportVectorField")
        self._P = value

        if self._P is not None:
            self._P.parent = self

    P = property(
        fget=_get_P,
        fset=_set_P,
        doc=u"""Magnetic air-gap surface force

        :Type: ImportVectorField
        """,
    )
