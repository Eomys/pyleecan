# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/ElecLUTdq.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/ElecLUTdq
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
from .Electrical import Electrical

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.ElecLUTdq.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Simulation.ElecLUTdq.comp_LUTdq import comp_LUTdq
except ImportError as error:
    comp_LUTdq = error


from ._check import InitUnKnowClassError


class ElecLUTdq(Electrical):
    """Electric module object for electrical equivalent circuit simulation"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.ElecLUTdq.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use ElecLUTdq method run: " + str(run))
            )
        )
    else:
        run = run
    # cf Methods.Simulation.ElecLUTdq.comp_LUTdq
    if isinstance(comp_LUTdq, ImportError):
        comp_LUTdq = property(
            fget=lambda x: raise_(
                ImportError("Can't use ElecLUTdq method comp_LUTdq: " + str(comp_LUTdq))
            )
        )
    else:
        comp_LUTdq = comp_LUTdq
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        n_interp=10,
        Id_min=None,
        Id_max=None,
        Iq_min=None,
        Iq_max=None,
        n_Id=1,
        n_Iq=1,
        LUT_simu=None,
        eec=None,
        logger_name="Pyleecan.Electrical",
        freq_max=40000,
        LUT_enforced=None,
        Tsta=20,
        Trot=20,
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
            if "n_interp" in list(init_dict.keys()):
                n_interp = init_dict["n_interp"]
            if "Id_min" in list(init_dict.keys()):
                Id_min = init_dict["Id_min"]
            if "Id_max" in list(init_dict.keys()):
                Id_max = init_dict["Id_max"]
            if "Iq_min" in list(init_dict.keys()):
                Iq_min = init_dict["Iq_min"]
            if "Iq_max" in list(init_dict.keys()):
                Iq_max = init_dict["Iq_max"]
            if "n_Id" in list(init_dict.keys()):
                n_Id = init_dict["n_Id"]
            if "n_Iq" in list(init_dict.keys()):
                n_Iq = init_dict["n_Iq"]
            if "LUT_simu" in list(init_dict.keys()):
                LUT_simu = init_dict["LUT_simu"]
            if "eec" in list(init_dict.keys()):
                eec = init_dict["eec"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "freq_max" in list(init_dict.keys()):
                freq_max = init_dict["freq_max"]
            if "LUT_enforced" in list(init_dict.keys()):
                LUT_enforced = init_dict["LUT_enforced"]
            if "Tsta" in list(init_dict.keys()):
                Tsta = init_dict["Tsta"]
            if "Trot" in list(init_dict.keys()):
                Trot = init_dict["Trot"]
        # Set the properties (value check and convertion are done in setter)
        self.n_interp = n_interp
        self.Id_min = Id_min
        self.Id_max = Id_max
        self.Iq_min = Iq_min
        self.Iq_max = Iq_max
        self.n_Id = n_Id
        self.n_Iq = n_Iq
        self.LUT_simu = LUT_simu
        # Call Electrical init
        super(ElecLUTdq, self).__init__(
            eec=eec,
            logger_name=logger_name,
            freq_max=freq_max,
            LUT_enforced=LUT_enforced,
            Tsta=Tsta,
            Trot=Trot,
        )
        # The class is frozen (in Electrical init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ElecLUTdq_str = ""
        # Get the properties inherited from Electrical
        ElecLUTdq_str += super(ElecLUTdq, self).__str__()
        ElecLUTdq_str += "n_interp = " + str(self.n_interp) + linesep
        ElecLUTdq_str += "Id_min = " + str(self.Id_min) + linesep
        ElecLUTdq_str += "Id_max = " + str(self.Id_max) + linesep
        ElecLUTdq_str += "Iq_min = " + str(self.Iq_min) + linesep
        ElecLUTdq_str += "Iq_max = " + str(self.Iq_max) + linesep
        ElecLUTdq_str += "n_Id = " + str(self.n_Id) + linesep
        ElecLUTdq_str += "n_Iq = " + str(self.n_Iq) + linesep
        if self.LUT_simu is not None:
            tmp = self.LUT_simu.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            ElecLUTdq_str += "LUT_simu = " + tmp
        else:
            ElecLUTdq_str += "LUT_simu = None" + linesep + linesep
        return ElecLUTdq_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Electrical
        if not super(ElecLUTdq, self).__eq__(other):
            return False
        if other.n_interp != self.n_interp:
            return False
        if other.Id_min != self.Id_min:
            return False
        if other.Id_max != self.Id_max:
            return False
        if other.Iq_min != self.Iq_min:
            return False
        if other.Iq_max != self.Iq_max:
            return False
        if other.n_Id != self.n_Id:
            return False
        if other.n_Iq != self.n_Iq:
            return False
        if other.LUT_simu != self.LUT_simu:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Electrical
        diff_list.extend(super(ElecLUTdq, self).compare(other, name=name))
        if other._n_interp != self._n_interp:
            diff_list.append(name + ".n_interp")
        if other._Id_min != self._Id_min:
            diff_list.append(name + ".Id_min")
        if other._Id_max != self._Id_max:
            diff_list.append(name + ".Id_max")
        if other._Iq_min != self._Iq_min:
            diff_list.append(name + ".Iq_min")
        if other._Iq_max != self._Iq_max:
            diff_list.append(name + ".Iq_max")
        if other._n_Id != self._n_Id:
            diff_list.append(name + ".n_Id")
        if other._n_Iq != self._n_Iq:
            diff_list.append(name + ".n_Iq")
        if (other.LUT_simu is None and self.LUT_simu is not None) or (
            other.LUT_simu is not None and self.LUT_simu is None
        ):
            diff_list.append(name + ".LUT_simu None mismatch")
        elif self.LUT_simu is not None:
            diff_list.extend(
                self.LUT_simu.compare(other.LUT_simu, name=name + ".LUT_simu")
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Electrical
        S += super(ElecLUTdq, self).__sizeof__()
        S += getsizeof(self.n_interp)
        S += getsizeof(self.Id_min)
        S += getsizeof(self.Id_max)
        S += getsizeof(self.Iq_min)
        S += getsizeof(self.Iq_max)
        S += getsizeof(self.n_Id)
        S += getsizeof(self.n_Iq)
        S += getsizeof(self.LUT_simu)
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

        # Get the properties inherited from Electrical
        ElecLUTdq_dict = super(ElecLUTdq, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ElecLUTdq_dict["n_interp"] = self.n_interp
        ElecLUTdq_dict["Id_min"] = self.Id_min
        ElecLUTdq_dict["Id_max"] = self.Id_max
        ElecLUTdq_dict["Iq_min"] = self.Iq_min
        ElecLUTdq_dict["Iq_max"] = self.Iq_max
        ElecLUTdq_dict["n_Id"] = self.n_Id
        ElecLUTdq_dict["n_Iq"] = self.n_Iq
        if self.LUT_simu is None:
            ElecLUTdq_dict["LUT_simu"] = None
        else:
            ElecLUTdq_dict["LUT_simu"] = self.LUT_simu.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ElecLUTdq_dict["__class__"] = "ElecLUTdq"
        return ElecLUTdq_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.n_interp = None
        self.Id_min = None
        self.Id_max = None
        self.Iq_min = None
        self.Iq_max = None
        self.n_Id = None
        self.n_Iq = None
        if self.LUT_simu is not None:
            self.LUT_simu._set_None()
        # Set to None the properties inherited from Electrical
        super(ElecLUTdq, self)._set_None()

    def _get_n_interp(self):
        """getter of n_interp"""
        return self._n_interp

    def _set_n_interp(self, value):
        """setter of n_interp"""
        check_var("n_interp", value, "int", Vmin=1)
        self._n_interp = value

    n_interp = property(
        fget=_get_n_interp,
        fset=_set_n_interp,
        doc=u"""Number of id values used for interpolation

        :Type: int
        :min: 1
        """,
    )

    def _get_Id_min(self):
        """getter of Id_min"""
        return self._Id_min

    def _set_Id_min(self, value):
        """setter of Id_min"""
        check_var("Id_min", value, "float")
        self._Id_min = value

    Id_min = property(
        fget=_get_Id_min,
        fset=_set_Id_min,
        doc=u"""Minimum Id for LUT calculation

        :Type: float
        """,
    )

    def _get_Id_max(self):
        """getter of Id_max"""
        return self._Id_max

    def _set_Id_max(self, value):
        """setter of Id_max"""
        check_var("Id_max", value, "float")
        self._Id_max = value

    Id_max = property(
        fget=_get_Id_max,
        fset=_set_Id_max,
        doc=u"""Maximum Id for LUT calculation

        :Type: float
        """,
    )

    def _get_Iq_min(self):
        """getter of Iq_min"""
        return self._Iq_min

    def _set_Iq_min(self, value):
        """setter of Iq_min"""
        check_var("Iq_min", value, "float")
        self._Iq_min = value

    Iq_min = property(
        fget=_get_Iq_min,
        fset=_set_Iq_min,
        doc=u"""Minimum Iq for LUT calculation

        :Type: float
        """,
    )

    def _get_Iq_max(self):
        """getter of Iq_max"""
        return self._Iq_max

    def _set_Iq_max(self, value):
        """setter of Iq_max"""
        check_var("Iq_max", value, "float")
        self._Iq_max = value

    Iq_max = property(
        fget=_get_Iq_max,
        fset=_set_Iq_max,
        doc=u"""Maximum Iq for LUT calculation

        :Type: float
        """,
    )

    def _get_n_Id(self):
        """getter of n_Id"""
        return self._n_Id

    def _set_n_Id(self, value):
        """setter of n_Id"""
        check_var("n_Id", value, "int")
        self._n_Id = value

    n_Id = property(
        fget=_get_n_Id,
        fset=_set_n_Id,
        doc=u"""Number of Id for LUT calculation

        :Type: int
        """,
    )

    def _get_n_Iq(self):
        """getter of n_Iq"""
        return self._n_Iq

    def _set_n_Iq(self, value):
        """setter of n_Iq"""
        check_var("n_Iq", value, "int")
        self._n_Iq = value

    n_Iq = property(
        fget=_get_n_Iq,
        fset=_set_n_Iq,
        doc=u"""Number of Iq for LUT calculation

        :Type: int
        """,
    )

    def _get_LUT_simu(self):
        """getter of LUT_simu"""
        return self._LUT_simu

    def _set_LUT_simu(self, value):
        """setter of LUT_simu"""
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
                "pyleecan.Classes", value.get("__class__"), "LUT_simu"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Simulation = import_class("pyleecan.Classes", "Simulation", "LUT_simu")
            value = Simulation()
        check_var("LUT_simu", value, "Simulation")
        self._LUT_simu = value

        if self._LUT_simu is not None:
            self._LUT_simu.parent = self

    LUT_simu = property(
        fget=_get_LUT_simu,
        fset=_set_LUT_simu,
        doc=u"""Simulation object to run for LUT calculation

        :Type: Simulation
        """,
    )
