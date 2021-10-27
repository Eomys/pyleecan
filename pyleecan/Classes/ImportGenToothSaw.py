# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Import/ImportGenToothSaw.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Import/ImportGenToothSaw
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
from .ImportMatrix import ImportMatrix

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Import.ImportGenToothSaw.get_data import get_data
except ImportError as error:
    get_data = error


from ._check import InitUnKnowClassError


class ImportGenToothSaw(ImportMatrix):
    """To generate a toothsaw vector"""

    VERSION = 1

    # cf Methods.Import.ImportGenToothSaw.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportGenToothSaw method get_data: " + str(get_data)
                )
            )
        )
    else:
        get_data = get_data
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        type_signal=0,
        f=100,
        A=1,
        N=1024,
        Tf=1,
        Dt=0,
        is_transpose=False,
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
            if "type_signal" in list(init_dict.keys()):
                type_signal = init_dict["type_signal"]
            if "f" in list(init_dict.keys()):
                f = init_dict["f"]
            if "A" in list(init_dict.keys()):
                A = init_dict["A"]
            if "N" in list(init_dict.keys()):
                N = init_dict["N"]
            if "Tf" in list(init_dict.keys()):
                Tf = init_dict["Tf"]
            if "Dt" in list(init_dict.keys()):
                Dt = init_dict["Dt"]
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Set the properties (value check and convertion are done in setter)
        self.type_signal = type_signal
        self.f = f
        self.A = A
        self.N = N
        self.Tf = Tf
        self.Dt = Dt
        # Call ImportMatrix init
        super(ImportGenToothSaw, self).__init__(is_transpose=is_transpose)
        # The class is frozen (in ImportMatrix init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ImportGenToothSaw_str = ""
        # Get the properties inherited from ImportMatrix
        ImportGenToothSaw_str += super(ImportGenToothSaw, self).__str__()
        ImportGenToothSaw_str += "type_signal = " + str(self.type_signal) + linesep
        ImportGenToothSaw_str += "f = " + str(self.f) + linesep
        ImportGenToothSaw_str += "A = " + str(self.A) + linesep
        ImportGenToothSaw_str += "N = " + str(self.N) + linesep
        ImportGenToothSaw_str += "Tf = " + str(self.Tf) + linesep
        ImportGenToothSaw_str += "Dt = " + str(self.Dt) + linesep
        return ImportGenToothSaw_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ImportMatrix
        if not super(ImportGenToothSaw, self).__eq__(other):
            return False
        if other.type_signal != self.type_signal:
            return False
        if other.f != self.f:
            return False
        if other.A != self.A:
            return False
        if other.N != self.N:
            return False
        if other.Tf != self.Tf:
            return False
        if other.Dt != self.Dt:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from ImportMatrix
        diff_list.extend(super(ImportGenToothSaw, self).compare(other, name=name))
        if other._type_signal != self._type_signal:
            diff_list.append(name + ".type_signal")
        if other._f != self._f:
            diff_list.append(name + ".f")
        if other._A != self._A:
            diff_list.append(name + ".A")
        if other._N != self._N:
            diff_list.append(name + ".N")
        if other._Tf != self._Tf:
            diff_list.append(name + ".Tf")
        if other._Dt != self._Dt:
            diff_list.append(name + ".Dt")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ImportMatrix
        S += super(ImportGenToothSaw, self).__sizeof__()
        S += getsizeof(self.type_signal)
        S += getsizeof(self.f)
        S += getsizeof(self.A)
        S += getsizeof(self.N)
        S += getsizeof(self.Tf)
        S += getsizeof(self.Dt)
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

        # Get the properties inherited from ImportMatrix
        ImportGenToothSaw_dict = super(ImportGenToothSaw, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ImportGenToothSaw_dict["type_signal"] = self.type_signal
        ImportGenToothSaw_dict["f"] = self.f
        ImportGenToothSaw_dict["A"] = self.A
        ImportGenToothSaw_dict["N"] = self.N
        ImportGenToothSaw_dict["Tf"] = self.Tf
        ImportGenToothSaw_dict["Dt"] = self.Dt
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ImportGenToothSaw_dict["__class__"] = "ImportGenToothSaw"
        return ImportGenToothSaw_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.type_signal = None
        self.f = None
        self.A = None
        self.N = None
        self.Tf = None
        self.Dt = None
        # Set to None the properties inherited from ImportMatrix
        super(ImportGenToothSaw, self)._set_None()

    def _get_type_signal(self):
        """getter of type_signal"""
        return self._type_signal

    def _set_type_signal(self, value):
        """setter of type_signal"""
        check_var("type_signal", value, "int", Vmin=0, Vmax=2)
        self._type_signal = value

    type_signal = property(
        fget=_get_type_signal,
        fset=_set_type_signal,
        doc=u"""0: Forward toothsaw, 1: Backwards toothsaw, 2: symmetrical toothsaw

        :Type: int
        :min: 0
        :max: 2
        """,
    )

    def _get_f(self):
        """getter of f"""
        return self._f

    def _set_f(self, value):
        """setter of f"""
        check_var("f", value, "float", Vmin=0)
        self._f = value

    f = property(
        fget=_get_f,
        fset=_set_f,
        doc=u"""Frequency of the signal to generate

        :Type: float
        :min: 0
        """,
    )

    def _get_A(self):
        """getter of A"""
        return self._A

    def _set_A(self, value):
        """setter of A"""
        check_var("A", value, "float")
        self._A = value

    A = property(
        fget=_get_A,
        fset=_set_A,
        doc=u"""Amplitude of the signal to generate

        :Type: float
        """,
    )

    def _get_N(self):
        """getter of N"""
        return self._N

    def _set_N(self, value):
        """setter of N"""
        check_var("N", value, "int", Vmin=0)
        self._N = value

    N = property(
        fget=_get_N,
        fset=_set_N,
        doc=u"""Length of the signal to generate

        :Type: int
        :min: 0
        """,
    )

    def _get_Tf(self):
        """getter of Tf"""
        return self._Tf

    def _set_Tf(self, value):
        """setter of Tf"""
        check_var("Tf", value, "float", Vmin=0)
        self._Tf = value

    Tf = property(
        fget=_get_Tf,
        fset=_set_Tf,
        doc=u"""End time of the signal generation

        :Type: float
        :min: 0
        """,
    )

    def _get_Dt(self):
        """getter of Dt"""
        return self._Dt

    def _set_Dt(self, value):
        """setter of Dt"""
        check_var("Dt", value, "float")
        self._Dt = value

    Dt = property(
        fget=_get_Dt,
        fset=_set_Dt,
        doc=u"""Time offset

        :Type: float
        """,
    )
