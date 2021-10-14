# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Import/ImportGenVectSin.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Import/ImportGenVectSin
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
    from ..Methods.Import.ImportGenVectSin.get_data import get_data
except ImportError as error:
    get_data = error


from ._check import InitUnKnowClassError


class ImportGenVectSin(ImportMatrix):
    """To generate a Sinus vector"""

    VERSION = 1

    # cf Methods.Import.ImportGenVectSin.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportGenVectSin method get_data: " + str(get_data)
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
        f=100,
        A=1,
        Phi=0,
        N=1024,
        Tf=1,
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
            if "f" in list(init_dict.keys()):
                f = init_dict["f"]
            if "A" in list(init_dict.keys()):
                A = init_dict["A"]
            if "Phi" in list(init_dict.keys()):
                Phi = init_dict["Phi"]
            if "N" in list(init_dict.keys()):
                N = init_dict["N"]
            if "Tf" in list(init_dict.keys()):
                Tf = init_dict["Tf"]
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Set the properties (value check and convertion are done in setter)
        self.f = f
        self.A = A
        self.Phi = Phi
        self.N = N
        self.Tf = Tf
        # Call ImportMatrix init
        super(ImportGenVectSin, self).__init__(is_transpose=is_transpose)
        # The class is frozen (in ImportMatrix init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ImportGenVectSin_str = ""
        # Get the properties inherited from ImportMatrix
        ImportGenVectSin_str += super(ImportGenVectSin, self).__str__()
        ImportGenVectSin_str += "f = " + str(self.f) + linesep
        ImportGenVectSin_str += "A = " + str(self.A) + linesep
        ImportGenVectSin_str += "Phi = " + str(self.Phi) + linesep
        ImportGenVectSin_str += "N = " + str(self.N) + linesep
        ImportGenVectSin_str += "Tf = " + str(self.Tf) + linesep
        return ImportGenVectSin_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ImportMatrix
        if not super(ImportGenVectSin, self).__eq__(other):
            return False
        if other.f != self.f:
            return False
        if other.A != self.A:
            return False
        if other.Phi != self.Phi:
            return False
        if other.N != self.N:
            return False
        if other.Tf != self.Tf:
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
        diff_list.extend(super(ImportGenVectSin, self).compare(other, name=name))
        if other._f != self._f:
            diff_list.append(name + ".f")
        if other._A != self._A:
            diff_list.append(name + ".A")
        if other._Phi != self._Phi:
            diff_list.append(name + ".Phi")
        if other._N != self._N:
            diff_list.append(name + ".N")
        if other._Tf != self._Tf:
            diff_list.append(name + ".Tf")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ImportMatrix
        S += super(ImportGenVectSin, self).__sizeof__()
        S += getsizeof(self.f)
        S += getsizeof(self.A)
        S += getsizeof(self.Phi)
        S += getsizeof(self.N)
        S += getsizeof(self.Tf)
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
        ImportGenVectSin_dict = super(ImportGenVectSin, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ImportGenVectSin_dict["f"] = self.f
        ImportGenVectSin_dict["A"] = self.A
        ImportGenVectSin_dict["Phi"] = self.Phi
        ImportGenVectSin_dict["N"] = self.N
        ImportGenVectSin_dict["Tf"] = self.Tf
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ImportGenVectSin_dict["__class__"] = "ImportGenVectSin"
        return ImportGenVectSin_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.f = None
        self.A = None
        self.Phi = None
        self.N = None
        self.Tf = None
        # Set to None the properties inherited from ImportMatrix
        super(ImportGenVectSin, self)._set_None()

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
        doc=u"""Frequency of the sinus to generate

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
        doc=u"""Amplitude of the sinus to generate

        :Type: float
        """,
    )

    def _get_Phi(self):
        """getter of Phi"""
        return self._Phi

    def _set_Phi(self, value):
        """setter of Phi"""
        check_var("Phi", value, "float", Vmin=-6.29, Vmax=6.29)
        self._Phi = value

    Phi = property(
        fget=_get_Phi,
        fset=_set_Phi,
        doc=u"""Phase of the sinus to generate

        :Type: float
        :min: -6.29
        :max: 6.29
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
        doc=u"""Length of the vector to generate

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
        doc=u"""End time of the sinus generation

        :Type: float
        :min: 0
        """,
    )
