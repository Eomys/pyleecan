# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Import/ImportGenPWM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Import/ImportGenPWM
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
    from ..Methods.Import.ImportGenPWM.get_data import get_data
except ImportError as error:
    get_data = error


from ._check import InitUnKnowClassError


class ImportGenPWM(ImportMatrix):
    """To generate a PWM voltage matrix"""

    VERSION = 1

    # cf Methods.Import.ImportGenPWM.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError("Can't use ImportGenPWM method get_data: " + str(get_data))
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
        fs=96000,
        duration=10,
        f=50,
        fmax=0,
        fmode=0,
        fswimode=0,
        fswi=1000,
        fswi_max=3000,
        typePWM=8,
        Vdc1=2,
        U0=1,
        type_carrier=0,
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
            if "fs" in list(init_dict.keys()):
                fs = init_dict["fs"]
            if "duration" in list(init_dict.keys()):
                duration = init_dict["duration"]
            if "f" in list(init_dict.keys()):
                f = init_dict["f"]
            if "fmax" in list(init_dict.keys()):
                fmax = init_dict["fmax"]
            if "fmode" in list(init_dict.keys()):
                fmode = init_dict["fmode"]
            if "fswimode" in list(init_dict.keys()):
                fswimode = init_dict["fswimode"]
            if "fswi" in list(init_dict.keys()):
                fswi = init_dict["fswi"]
            if "fswi_max" in list(init_dict.keys()):
                fswi_max = init_dict["fswi_max"]
            if "typePWM" in list(init_dict.keys()):
                typePWM = init_dict["typePWM"]
            if "Vdc1" in list(init_dict.keys()):
                Vdc1 = init_dict["Vdc1"]
            if "U0" in list(init_dict.keys()):
                U0 = init_dict["U0"]
            if "type_carrier" in list(init_dict.keys()):
                type_carrier = init_dict["type_carrier"]
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Set the properties (value check and convertion are done in setter)
        self.fs = fs
        self.duration = duration
        self.f = f
        self.fmax = fmax
        self.fmode = fmode
        self.fswimode = fswimode
        self.fswi = fswi
        self.fswi_max = fswi_max
        self.typePWM = typePWM
        self.Vdc1 = Vdc1
        self.U0 = U0
        self.type_carrier = type_carrier
        # Call ImportMatrix init
        super(ImportGenPWM, self).__init__(is_transpose=is_transpose)
        # The class is frozen (in ImportMatrix init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ImportGenPWM_str = ""
        # Get the properties inherited from ImportMatrix
        ImportGenPWM_str += super(ImportGenPWM, self).__str__()
        ImportGenPWM_str += "fs = " + str(self.fs) + linesep
        ImportGenPWM_str += "duration = " + str(self.duration) + linesep
        ImportGenPWM_str += "f = " + str(self.f) + linesep
        ImportGenPWM_str += "fmax = " + str(self.fmax) + linesep
        ImportGenPWM_str += "fmode = " + str(self.fmode) + linesep
        ImportGenPWM_str += "fswimode = " + str(self.fswimode) + linesep
        ImportGenPWM_str += "fswi = " + str(self.fswi) + linesep
        ImportGenPWM_str += "fswi_max = " + str(self.fswi_max) + linesep
        ImportGenPWM_str += "typePWM = " + str(self.typePWM) + linesep
        ImportGenPWM_str += "Vdc1 = " + str(self.Vdc1) + linesep
        ImportGenPWM_str += "U0 = " + str(self.U0) + linesep
        ImportGenPWM_str += "type_carrier = " + str(self.type_carrier) + linesep
        return ImportGenPWM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ImportMatrix
        if not super(ImportGenPWM, self).__eq__(other):
            return False
        if other.fs != self.fs:
            return False
        if other.duration != self.duration:
            return False
        if other.f != self.f:
            return False
        if other.fmax != self.fmax:
            return False
        if other.fmode != self.fmode:
            return False
        if other.fswimode != self.fswimode:
            return False
        if other.fswi != self.fswi:
            return False
        if other.fswi_max != self.fswi_max:
            return False
        if other.typePWM != self.typePWM:
            return False
        if other.Vdc1 != self.Vdc1:
            return False
        if other.U0 != self.U0:
            return False
        if other.type_carrier != self.type_carrier:
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
        diff_list.extend(super(ImportGenPWM, self).compare(other, name=name))
        if other._fs != self._fs:
            diff_list.append(name + ".fs")
        if other._duration != self._duration:
            diff_list.append(name + ".duration")
        if other._f != self._f:
            diff_list.append(name + ".f")
        if other._fmax != self._fmax:
            diff_list.append(name + ".fmax")
        if other._fmode != self._fmode:
            diff_list.append(name + ".fmode")
        if other._fswimode != self._fswimode:
            diff_list.append(name + ".fswimode")
        if other._fswi != self._fswi:
            diff_list.append(name + ".fswi")
        if other._fswi_max != self._fswi_max:
            diff_list.append(name + ".fswi_max")
        if other._typePWM != self._typePWM:
            diff_list.append(name + ".typePWM")
        if other._Vdc1 != self._Vdc1:
            diff_list.append(name + ".Vdc1")
        if other._U0 != self._U0:
            diff_list.append(name + ".U0")
        if other._type_carrier != self._type_carrier:
            diff_list.append(name + ".type_carrier")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ImportMatrix
        S += super(ImportGenPWM, self).__sizeof__()
        S += getsizeof(self.fs)
        S += getsizeof(self.duration)
        S += getsizeof(self.f)
        S += getsizeof(self.fmax)
        S += getsizeof(self.fmode)
        S += getsizeof(self.fswimode)
        S += getsizeof(self.fswi)
        S += getsizeof(self.fswi_max)
        S += getsizeof(self.typePWM)
        S += getsizeof(self.Vdc1)
        S += getsizeof(self.U0)
        S += getsizeof(self.type_carrier)
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
        ImportGenPWM_dict = super(ImportGenPWM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ImportGenPWM_dict["fs"] = self.fs
        ImportGenPWM_dict["duration"] = self.duration
        ImportGenPWM_dict["f"] = self.f
        ImportGenPWM_dict["fmax"] = self.fmax
        ImportGenPWM_dict["fmode"] = self.fmode
        ImportGenPWM_dict["fswimode"] = self.fswimode
        ImportGenPWM_dict["fswi"] = self.fswi
        ImportGenPWM_dict["fswi_max"] = self.fswi_max
        ImportGenPWM_dict["typePWM"] = self.typePWM
        ImportGenPWM_dict["Vdc1"] = self.Vdc1
        ImportGenPWM_dict["U0"] = self.U0
        ImportGenPWM_dict["type_carrier"] = self.type_carrier
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ImportGenPWM_dict["__class__"] = "ImportGenPWM"
        return ImportGenPWM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.fs = None
        self.duration = None
        self.f = None
        self.fmax = None
        self.fmode = None
        self.fswimode = None
        self.fswi = None
        self.fswi_max = None
        self.typePWM = None
        self.Vdc1 = None
        self.U0 = None
        self.type_carrier = None
        # Set to None the properties inherited from ImportMatrix
        super(ImportGenPWM, self)._set_None()

    def _get_fs(self):
        """getter of fs"""
        return self._fs

    def _set_fs(self, value):
        """setter of fs"""
        check_var("fs", value, "float", Vmin=0)
        self._fs = value

    fs = property(
        fget=_get_fs,
        fset=_set_fs,
        doc=u"""sample frequency

        :Type: float
        :min: 0
        """,
    )

    def _get_duration(self):
        """getter of duration"""
        return self._duration

    def _set_duration(self, value):
        """setter of duration"""
        check_var("duration", value, "int", Vmin=0)
        self._duration = value

    duration = property(
        fget=_get_duration,
        fset=_set_duration,
        doc=u"""duration

        :Type: int
        :min: 0
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
        doc=u"""fundamental frequency

        :Type: float
        :min: 0
        """,
    )

    def _get_fmax(self):
        """getter of fmax"""
        return self._fmax

    def _set_fmax(self, value):
        """setter of fmax"""
        check_var("fmax", value, "float", Vmin=0)
        self._fmax = value

    fmax = property(
        fget=_get_fmax,
        fset=_set_fmax,
        doc=u"""maximal fundamental frequency

        :Type: float
        :min: 0
        """,
    )

    def _get_fmode(self):
        """getter of fmode"""
        return self._fmode

    def _set_fmode(self, value):
        """setter of fmode"""
        check_var("fmode", value, "int", Vmin=0)
        self._fmode = value

    fmode = property(
        fget=_get_fmode,
        fset=_set_fmode,
        doc=u"""speed mode: 0: Fixed speed, 1: Variable speed

        :Type: int
        :min: 0
        """,
    )

    def _get_fswimode(self):
        """getter of fswimode"""
        return self._fswimode

    def _set_fswimode(self, value):
        """setter of fswimode"""
        check_var("fswimode", value, "int")
        self._fswimode = value

    fswimode = property(
        fget=_get_fswimode,
        fset=_set_fswimode,
        doc=u"""switch mode: 0:Fixed fswi, 1:Variable fswi

        :Type: int
        """,
    )

    def _get_fswi(self):
        """getter of fswi"""
        return self._fswi

    def _set_fswi(self, value):
        """setter of fswi"""
        check_var("fswi", value, "float")
        self._fswi = value

    fswi = property(
        fget=_get_fswi,
        fset=_set_fswi,
        doc=u"""switching frequency

        :Type: float
        """,
    )

    def _get_fswi_max(self):
        """getter of fswi_max"""
        return self._fswi_max

    def _set_fswi_max(self, value):
        """setter of fswi_max"""
        check_var("fswi_max", value, "int")
        self._fswi_max = value

    fswi_max = property(
        fget=_get_fswi_max,
        fset=_set_fswi_max,
        doc=u"""maximal switching frequency

        :Type: int
        """,
    )

    def _get_typePWM(self):
        """getter of typePWM"""
        return self._typePWM

    def _set_typePWM(self, value):
        """setter of typePWM"""
        check_var("typePWM", value, "int")
        self._typePWM = value

    typePWM = property(
        fget=_get_typePWM,
        fset=_set_typePWM,
        doc=u"""0: GDPWM 1: DPWMMIN 2: DPWMMAX 3: DPWM0 4: DPWM1 5: DPWM2 6: DPWM3 7: SVPWM 8: SPWM

        :Type: int
        """,
    )

    def _get_Vdc1(self):
        """getter of Vdc1"""
        return self._Vdc1

    def _set_Vdc1(self, value):
        """setter of Vdc1"""
        check_var("Vdc1", value, "float")
        self._Vdc1 = value

    Vdc1 = property(
        fget=_get_Vdc1,
        fset=_set_Vdc1,
        doc=u"""DC BUS voltage

        :Type: float
        """,
    )

    def _get_U0(self):
        """getter of U0"""
        return self._U0

    def _set_U0(self, value):
        """setter of U0"""
        check_var("U0", value, "float")
        self._U0 = value

    U0 = property(
        fget=_get_U0,
        fset=_set_U0,
        doc=u"""reference voltage

        :Type: float
        """,
    )

    def _get_type_carrier(self):
        """getter of type_carrier"""
        return self._type_carrier

    def _set_type_carrier(self, value):
        """setter of type_carrier"""
        check_var("type_carrier", value, "int")
        self._type_carrier = value

    type_carrier = property(
        fget=_get_type_carrier,
        fset=_set_type_carrier,
        doc=u"""1: forward toothsaw carrier 2: backwards toothsaw carrier 3: toothsaw carrier else: symetrical toothsaw carrier

        :Type: int
        """,
    )
