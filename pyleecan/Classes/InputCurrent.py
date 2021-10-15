# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/InputCurrent.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/InputCurrent
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
from .Input import Input

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.InputCurrent.gen_input import gen_input
except ImportError as error:
    gen_input = error

try:
    from ..Methods.Simulation.InputCurrent.set_Id_Iq import set_Id_Iq
except ImportError as error:
    set_Id_Iq = error

try:
    from ..Methods.Simulation.InputCurrent.set_OP_from_array import set_OP_from_array
except ImportError as error:
    set_OP_from_array = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .ImportMatrix import ImportMatrix
from .Import import Import


class InputCurrent(Input):
    """Input to skip the electrical module and start with the magnetic one"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.InputCurrent.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputCurrent method gen_input: " + str(gen_input)
                )
            )
        )
    else:
        gen_input = gen_input
    # cf Methods.Simulation.InputCurrent.set_Id_Iq
    if isinstance(set_Id_Iq, ImportError):
        set_Id_Iq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputCurrent method set_Id_Iq: " + str(set_Id_Iq)
                )
            )
        )
    else:
        set_Id_Iq = set_Id_Iq
    # cf Methods.Simulation.InputCurrent.set_OP_from_array
    if isinstance(set_OP_from_array, ImportError):
        set_OP_from_array = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputCurrent method set_OP_from_array: "
                    + str(set_OP_from_array)
                )
            )
        )
    else:
        set_OP_from_array = set_OP_from_array
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Is=None,
        Ir=None,
        angle_rotor=None,
        rot_dir=None,
        angle_rotor_initial=0,
        Tem_av_ref=None,
        Id_ref=None,
        Iq_ref=None,
        felec=None,
        Pem_av_ref=None,
        time=None,
        angle=None,
        Nt_tot=2048,
        Nrev=1,
        Na_tot=2048,
        N0=None,
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
            if "Is" in list(init_dict.keys()):
                Is = init_dict["Is"]
            if "Ir" in list(init_dict.keys()):
                Ir = init_dict["Ir"]
            if "angle_rotor" in list(init_dict.keys()):
                angle_rotor = init_dict["angle_rotor"]
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
            if "Tem_av_ref" in list(init_dict.keys()):
                Tem_av_ref = init_dict["Tem_av_ref"]
            if "Id_ref" in list(init_dict.keys()):
                Id_ref = init_dict["Id_ref"]
            if "Iq_ref" in list(init_dict.keys()):
                Iq_ref = init_dict["Iq_ref"]
            if "felec" in list(init_dict.keys()):
                felec = init_dict["felec"]
            if "Pem_av_ref" in list(init_dict.keys()):
                Pem_av_ref = init_dict["Pem_av_ref"]
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
            if "N0" in list(init_dict.keys()):
                N0 = init_dict["N0"]
        # Set the properties (value check and convertion are done in setter)
        self.Is = Is
        self.Ir = Ir
        self.angle_rotor = angle_rotor
        self.rot_dir = rot_dir
        self.angle_rotor_initial = angle_rotor_initial
        self.Tem_av_ref = Tem_av_ref
        self.Id_ref = Id_ref
        self.Iq_ref = Iq_ref
        self.felec = felec
        self.Pem_av_ref = Pem_av_ref
        # Call Input init
        super(InputCurrent, self).__init__(
            time=time, angle=angle, Nt_tot=Nt_tot, Nrev=Nrev, Na_tot=Na_tot, N0=N0
        )
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        InputCurrent_str = ""
        # Get the properties inherited from Input
        InputCurrent_str += super(InputCurrent, self).__str__()
        if self.Is is not None:
            tmp = self.Is.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputCurrent_str += "Is = " + tmp
        else:
            InputCurrent_str += "Is = None" + linesep + linesep
        if self.Ir is not None:
            tmp = self.Ir.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputCurrent_str += "Ir = " + tmp
        else:
            InputCurrent_str += "Ir = None" + linesep + linesep
        if self.angle_rotor is not None:
            tmp = (
                self.angle_rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            InputCurrent_str += "angle_rotor = " + tmp
        else:
            InputCurrent_str += "angle_rotor = None" + linesep + linesep
        InputCurrent_str += "rot_dir = " + str(self.rot_dir) + linesep
        InputCurrent_str += (
            "angle_rotor_initial = " + str(self.angle_rotor_initial) + linesep
        )
        InputCurrent_str += "Tem_av_ref = " + str(self.Tem_av_ref) + linesep
        InputCurrent_str += "Id_ref = " + str(self.Id_ref) + linesep
        InputCurrent_str += "Iq_ref = " + str(self.Iq_ref) + linesep
        InputCurrent_str += "felec = " + str(self.felec) + linesep
        InputCurrent_str += "Pem_av_ref = " + str(self.Pem_av_ref) + linesep
        return InputCurrent_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InputCurrent, self).__eq__(other):
            return False
        if other.Is != self.Is:
            return False
        if other.Ir != self.Ir:
            return False
        if other.angle_rotor != self.angle_rotor:
            return False
        if other.rot_dir != self.rot_dir:
            return False
        if other.angle_rotor_initial != self.angle_rotor_initial:
            return False
        if other.Tem_av_ref != self.Tem_av_ref:
            return False
        if other.Id_ref != self.Id_ref:
            return False
        if other.Iq_ref != self.Iq_ref:
            return False
        if other.felec != self.felec:
            return False
        if other.Pem_av_ref != self.Pem_av_ref:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Input
        diff_list.extend(super(InputCurrent, self).compare(other, name=name))
        if (other.Is is None and self.Is is not None) or (
            other.Is is not None and self.Is is None
        ):
            diff_list.append(name + ".Is None mismatch")
        elif self.Is is not None:
            diff_list.extend(self.Is.compare(other.Is, name=name + ".Is"))
        if (other.Ir is None and self.Ir is not None) or (
            other.Ir is not None and self.Ir is None
        ):
            diff_list.append(name + ".Ir None mismatch")
        elif self.Ir is not None:
            diff_list.extend(self.Ir.compare(other.Ir, name=name + ".Ir"))
        if (other.angle_rotor is None and self.angle_rotor is not None) or (
            other.angle_rotor is not None and self.angle_rotor is None
        ):
            diff_list.append(name + ".angle_rotor None mismatch")
        elif self.angle_rotor is not None:
            diff_list.extend(
                self.angle_rotor.compare(other.angle_rotor, name=name + ".angle_rotor")
            )
        if other._rot_dir != self._rot_dir:
            diff_list.append(name + ".rot_dir")
        if other._angle_rotor_initial != self._angle_rotor_initial:
            diff_list.append(name + ".angle_rotor_initial")
        if other._Tem_av_ref != self._Tem_av_ref:
            diff_list.append(name + ".Tem_av_ref")
        if other._Id_ref != self._Id_ref:
            diff_list.append(name + ".Id_ref")
        if other._Iq_ref != self._Iq_ref:
            diff_list.append(name + ".Iq_ref")
        if other._felec != self._felec:
            diff_list.append(name + ".felec")
        if other._Pem_av_ref != self._Pem_av_ref:
            diff_list.append(name + ".Pem_av_ref")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Input
        S += super(InputCurrent, self).__sizeof__()
        S += getsizeof(self.Is)
        S += getsizeof(self.Ir)
        S += getsizeof(self.angle_rotor)
        S += getsizeof(self.rot_dir)
        S += getsizeof(self.angle_rotor_initial)
        S += getsizeof(self.Tem_av_ref)
        S += getsizeof(self.Id_ref)
        S += getsizeof(self.Iq_ref)
        S += getsizeof(self.felec)
        S += getsizeof(self.Pem_av_ref)
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
        InputCurrent_dict = super(InputCurrent, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.Is is None:
            InputCurrent_dict["Is"] = None
        else:
            InputCurrent_dict["Is"] = self.Is.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.Ir is None:
            InputCurrent_dict["Ir"] = None
        else:
            InputCurrent_dict["Ir"] = self.Ir.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.angle_rotor is None:
            InputCurrent_dict["angle_rotor"] = None
        else:
            InputCurrent_dict["angle_rotor"] = self.angle_rotor.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        InputCurrent_dict["rot_dir"] = self.rot_dir
        InputCurrent_dict["angle_rotor_initial"] = self.angle_rotor_initial
        InputCurrent_dict["Tem_av_ref"] = self.Tem_av_ref
        InputCurrent_dict["Id_ref"] = self.Id_ref
        InputCurrent_dict["Iq_ref"] = self.Iq_ref
        InputCurrent_dict["felec"] = self.felec
        InputCurrent_dict["Pem_av_ref"] = self.Pem_av_ref
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        InputCurrent_dict["__class__"] = "InputCurrent"
        return InputCurrent_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.Is is not None:
            self.Is._set_None()
        if self.Ir is not None:
            self.Ir._set_None()
        if self.angle_rotor is not None:
            self.angle_rotor._set_None()
        self.rot_dir = None
        self.angle_rotor_initial = None
        self.Tem_av_ref = None
        self.Id_ref = None
        self.Iq_ref = None
        self.felec = None
        self.Pem_av_ref = None
        # Set to None the properties inherited from Input
        super(InputCurrent, self)._set_None()

    def _get_Is(self):
        """getter of Is"""
        return self._Is

    def _set_Is(self, value):
        """setter of Is"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, ndarray):
            value = ImportMatrixVal(value=value)
        elif isinstance(value, list):
            value = ImportMatrixVal(value=array(value))
        elif value == -1:
            value = ImportMatrix()
        elif isinstance(value, dict):
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "Is")
            value = class_obj(init_dict=value)
        check_var("Is", value, "ImportMatrix")
        self._Is = value

        if self._Is is not None:
            self._Is.parent = self

    Is = property(
        fget=_get_Is,
        fset=_set_Is,
        doc=u"""Stator currents as a function of time (each column correspond to one phase) to import

        :Type: ImportMatrix
        """,
    )

    def _get_Ir(self):
        """getter of Ir"""
        return self._Ir

    def _set_Ir(self, value):
        """setter of Ir"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, ndarray):
            value = ImportMatrixVal(value=value)
        elif isinstance(value, list):
            value = ImportMatrixVal(value=array(value))
        elif value == -1:
            value = ImportMatrix()
        elif isinstance(value, dict):
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "Ir")
            value = class_obj(init_dict=value)
        check_var("Ir", value, "ImportMatrix")
        self._Ir = value

        if self._Ir is not None:
            self._Ir.parent = self

    Ir = property(
        fget=_get_Ir,
        fset=_set_Ir,
        doc=u"""Rotor currents as a function of time (each column correspond to one phase) to import

        :Type: ImportMatrix
        """,
    )

    def _get_angle_rotor(self):
        """getter of angle_rotor"""
        return self._angle_rotor

    def _set_angle_rotor(self, value):
        """setter of angle_rotor"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "angle_rotor"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Import()
        check_var("angle_rotor", value, "Import")
        self._angle_rotor = value

        if self._angle_rotor is not None:
            self._angle_rotor.parent = self

    angle_rotor = property(
        fget=_get_angle_rotor,
        fset=_set_angle_rotor,
        doc=u"""Rotor angular position as a function of time (if None computed according to Nr) to import

        :Type: Import
        """,
    )

    def _get_rot_dir(self):
        """getter of rot_dir"""
        return self._rot_dir

    def _set_rot_dir(self, value):
        """setter of rot_dir"""
        check_var("rot_dir", value, "float", Vmin=-1, Vmax=1)
        self._rot_dir = value

    rot_dir = property(
        fget=_get_rot_dir,
        fset=_set_rot_dir,
        doc=u"""Rotation direction of the rotor 1 trigo, -1 clockwise

        :Type: float
        :min: -1
        :max: 1
        """,
    )

    def _get_angle_rotor_initial(self):
        """getter of angle_rotor_initial"""
        return self._angle_rotor_initial

    def _set_angle_rotor_initial(self, value):
        """setter of angle_rotor_initial"""
        check_var("angle_rotor_initial", value, "float")
        self._angle_rotor_initial = value

    angle_rotor_initial = property(
        fget=_get_angle_rotor_initial,
        fset=_set_angle_rotor_initial,
        doc=u"""Initial angular position of the rotor at t=0

        :Type: float
        """,
    )

    def _get_Tem_av_ref(self):
        """getter of Tem_av_ref"""
        return self._Tem_av_ref

    def _set_Tem_av_ref(self, value):
        """setter of Tem_av_ref"""
        check_var("Tem_av_ref", value, "float")
        self._Tem_av_ref = value

    Tem_av_ref = property(
        fget=_get_Tem_av_ref,
        fset=_set_Tem_av_ref,
        doc=u"""Theorical Average Electromagnetic torque

        :Type: float
        """,
    )

    def _get_Id_ref(self):
        """getter of Id_ref"""
        return self._Id_ref

    def _set_Id_ref(self, value):
        """setter of Id_ref"""
        check_var("Id_ref", value, "float")
        self._Id_ref = value

    Id_ref = property(
        fget=_get_Id_ref,
        fset=_set_Id_ref,
        doc=u"""d-axis current RMS magnitude

        :Type: float
        """,
    )

    def _get_Iq_ref(self):
        """getter of Iq_ref"""
        return self._Iq_ref

    def _set_Iq_ref(self, value):
        """setter of Iq_ref"""
        check_var("Iq_ref", value, "float")
        self._Iq_ref = value

    Iq_ref = property(
        fget=_get_Iq_ref,
        fset=_set_Iq_ref,
        doc=u"""q-axis current RMS magnitude

        :Type: float
        """,
    )

    def _get_felec(self):
        """getter of felec"""
        return self._felec

    def _set_felec(self, value):
        """setter of felec"""
        check_var("felec", value, "float")
        self._felec = value

    felec = property(
        fget=_get_felec,
        fset=_set_felec,
        doc=u"""electrical frequency

        :Type: float
        """,
    )

    def _get_Pem_av_ref(self):
        """getter of Pem_av_ref"""
        return self._Pem_av_ref

    def _set_Pem_av_ref(self, value):
        """setter of Pem_av_ref"""
        check_var("Pem_av_ref", value, "float")
        self._Pem_av_ref = value

    Pem_av_ref = property(
        fget=_get_Pem_av_ref,
        fset=_set_Pem_av_ref,
        doc=u"""Theorical Average Electromagnetic Power

        :Type: float
        """,
    )
