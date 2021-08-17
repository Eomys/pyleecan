# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/InputVoltage.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/InputVoltage
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
    from ..Methods.Simulation.InputVoltage.gen_input import gen_input
except ImportError as error:
    gen_input = error

try:
    from ..Methods.Simulation.InputVoltage.set_OP_from_array import set_OP_from_array
except ImportError as error:
    set_OP_from_array = error

try:
    from ..Methods.Simulation.InputVoltage.comp_felec import comp_felec
except ImportError as error:
    comp_felec = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .Import import Import
from .ImportMatrix import ImportMatrix


class InputVoltage(Input):
    """Input to start the electrical module with voltage input"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.InputVoltage.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputVoltage method gen_input: " + str(gen_input)
                )
            )
        )
    else:
        gen_input = gen_input
    # cf Methods.Simulation.InputVoltage.set_OP_from_array
    if isinstance(set_OP_from_array, ImportError):
        set_OP_from_array = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputVoltage method set_OP_from_array: "
                    + str(set_OP_from_array)
                )
            )
        )
    else:
        set_OP_from_array = set_OP_from_array
    # cf Methods.Simulation.InputVoltage.comp_felec
    if isinstance(comp_felec, ImportError):
        comp_felec = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputVoltage method comp_felec: " + str(comp_felec)
                )
            )
        )
    else:
        comp_felec = comp_felec
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        angle_rotor=None,
        rot_dir=None,
        angle_rotor_initial=0,
        Tem_av_ref=None,
        Ud_ref=None,
        Uq_ref=None,
        felec=None,
        slip_ref=0,
        U0_ref=None,
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
            if "angle_rotor" in list(init_dict.keys()):
                angle_rotor = init_dict["angle_rotor"]
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
            if "Tem_av_ref" in list(init_dict.keys()):
                Tem_av_ref = init_dict["Tem_av_ref"]
            if "Ud_ref" in list(init_dict.keys()):
                Ud_ref = init_dict["Ud_ref"]
            if "Uq_ref" in list(init_dict.keys()):
                Uq_ref = init_dict["Uq_ref"]
            if "felec" in list(init_dict.keys()):
                felec = init_dict["felec"]
            if "slip_ref" in list(init_dict.keys()):
                slip_ref = init_dict["slip_ref"]
            if "U0_ref" in list(init_dict.keys()):
                U0_ref = init_dict["U0_ref"]
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
        self.angle_rotor = angle_rotor
        self.rot_dir = rot_dir
        self.angle_rotor_initial = angle_rotor_initial
        self.Tem_av_ref = Tem_av_ref
        self.Ud_ref = Ud_ref
        self.Uq_ref = Uq_ref
        self.felec = felec
        self.slip_ref = slip_ref
        self.U0_ref = U0_ref
        # Call Input init
        super(InputVoltage, self).__init__(
            time=time, angle=angle, Nt_tot=Nt_tot, Nrev=Nrev, Na_tot=Na_tot, N0=N0
        )
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        InputVoltage_str = ""
        # Get the properties inherited from Input
        InputVoltage_str += super(InputVoltage, self).__str__()
        if self.angle_rotor is not None:
            tmp = (
                self.angle_rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            InputVoltage_str += "angle_rotor = " + tmp
        else:
            InputVoltage_str += "angle_rotor = None" + linesep + linesep
        InputVoltage_str += "rot_dir = " + str(self.rot_dir) + linesep
        InputVoltage_str += (
            "angle_rotor_initial = " + str(self.angle_rotor_initial) + linesep
        )
        InputVoltage_str += "Tem_av_ref = " + str(self.Tem_av_ref) + linesep
        InputVoltage_str += "Ud_ref = " + str(self.Ud_ref) + linesep
        InputVoltage_str += "Uq_ref = " + str(self.Uq_ref) + linesep
        InputVoltage_str += "felec = " + str(self.felec) + linesep
        InputVoltage_str += "slip_ref = " + str(self.slip_ref) + linesep
        InputVoltage_str += "U0_ref = " + str(self.U0_ref) + linesep
        return InputVoltage_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InputVoltage, self).__eq__(other):
            return False
        if other.angle_rotor != self.angle_rotor:
            return False
        if other.rot_dir != self.rot_dir:
            return False
        if other.angle_rotor_initial != self.angle_rotor_initial:
            return False
        if other.Tem_av_ref != self.Tem_av_ref:
            return False
        if other.Ud_ref != self.Ud_ref:
            return False
        if other.Uq_ref != self.Uq_ref:
            return False
        if other.felec != self.felec:
            return False
        if other.slip_ref != self.slip_ref:
            return False
        if other.U0_ref != self.U0_ref:
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
        diff_list.extend(super(InputVoltage, self).compare(other, name=name))
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
        if other._Ud_ref != self._Ud_ref:
            diff_list.append(name + ".Ud_ref")
        if other._Uq_ref != self._Uq_ref:
            diff_list.append(name + ".Uq_ref")
        if other._felec != self._felec:
            diff_list.append(name + ".felec")
        if other._slip_ref != self._slip_ref:
            diff_list.append(name + ".slip_ref")
        if other._U0_ref != self._U0_ref:
            diff_list.append(name + ".U0_ref")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Input
        S += super(InputVoltage, self).__sizeof__()
        S += getsizeof(self.angle_rotor)
        S += getsizeof(self.rot_dir)
        S += getsizeof(self.angle_rotor_initial)
        S += getsizeof(self.Tem_av_ref)
        S += getsizeof(self.Ud_ref)
        S += getsizeof(self.Uq_ref)
        S += getsizeof(self.felec)
        S += getsizeof(self.slip_ref)
        S += getsizeof(self.U0_ref)
        return S

    def as_dict(self, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from Input
        InputVoltage_dict = super(InputVoltage, self).as_dict(**kwargs)
        if self.angle_rotor is None:
            InputVoltage_dict["angle_rotor"] = None
        else:
            InputVoltage_dict["angle_rotor"] = self.angle_rotor.as_dict(**kwargs)
        InputVoltage_dict["rot_dir"] = self.rot_dir
        InputVoltage_dict["angle_rotor_initial"] = self.angle_rotor_initial
        InputVoltage_dict["Tem_av_ref"] = self.Tem_av_ref
        InputVoltage_dict["Ud_ref"] = self.Ud_ref
        InputVoltage_dict["Uq_ref"] = self.Uq_ref
        InputVoltage_dict["felec"] = self.felec
        InputVoltage_dict["slip_ref"] = self.slip_ref
        InputVoltage_dict["U0_ref"] = self.U0_ref
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        InputVoltage_dict["__class__"] = "InputVoltage"
        return InputVoltage_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.angle_rotor is not None:
            self.angle_rotor._set_None()
        self.rot_dir = None
        self.angle_rotor_initial = None
        self.Tem_av_ref = None
        self.Ud_ref = None
        self.Uq_ref = None
        self.felec = None
        self.slip_ref = None
        self.U0_ref = None
        # Set to None the properties inherited from Input
        super(InputVoltage, self)._set_None()

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

    def _get_Ud_ref(self):
        """getter of Ud_ref"""
        return self._Ud_ref

    def _set_Ud_ref(self, value):
        """setter of Ud_ref"""
        check_var("Ud_ref", value, "float")
        self._Ud_ref = value

    Ud_ref = property(
        fget=_get_Ud_ref,
        fset=_set_Ud_ref,
        doc=u"""d-axis current RMS magnitude  (phase to neutral)

        :Type: float
        """,
    )

    def _get_Uq_ref(self):
        """getter of Uq_ref"""
        return self._Uq_ref

    def _set_Uq_ref(self, value):
        """setter of Uq_ref"""
        check_var("Uq_ref", value, "float")
        self._Uq_ref = value

    Uq_ref = property(
        fget=_get_Uq_ref,
        fset=_set_Uq_ref,
        doc=u"""q-axis current RMS magnitude  (phase to neutral)

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

    def _get_slip_ref(self):
        """getter of slip_ref"""
        return self._slip_ref

    def _set_slip_ref(self, value):
        """setter of slip_ref"""
        check_var("slip_ref", value, "float")
        self._slip_ref = value

    slip_ref = property(
        fget=_get_slip_ref,
        fset=_set_slip_ref,
        doc=u"""Rotor mechanical slip

        :Type: float
        """,
    )

    def _get_U0_ref(self):
        """getter of U0_ref"""
        return self._U0_ref

    def _set_U0_ref(self, value):
        """setter of U0_ref"""
        check_var("U0_ref", value, "float")
        self._U0_ref = value

    U0_ref = property(
        fget=_get_U0_ref,
        fset=_set_U0_ref,
        doc=u"""stator voltage (phase to neutral)

        :Type: float
        """,
    )
