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
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
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

try:
    from ..Methods.Simulation.ElecLUTdq.solve_power import solve_power
except ImportError as error:
    solve_power = error

try:
    from ..Methods.Simulation.ElecLUTdq.solve_MTPA import solve_MTPA
except ImportError as error:
    solve_MTPA = error


from numpy import isnan
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
    # cf Methods.Simulation.ElecLUTdq.solve_power
    if isinstance(solve_power, ImportError):
        solve_power = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElecLUTdq method solve_power: " + str(solve_power)
                )
            )
        )
    else:
        solve_power = solve_power
    # cf Methods.Simulation.ElecLUTdq.solve_MTPA
    if isinstance(solve_MTPA, ImportError):
        solve_MTPA = property(
            fget=lambda x: raise_(
                ImportError("Can't use ElecLUTdq method solve_MTPA: " + str(solve_MTPA))
            )
        )
    else:
        solve_MTPA = solve_MTPA
    # generic save method is available in all object
    save = save
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
        is_grid_dq=True,
        Urms_max=None,
        Jrms_max=None,
        Irms_max=None,
        load_rate=1,
        eec=None,
        logger_name="Pyleecan.Electrical",
        freq_max=40000,
        LUT_enforced=None,
        Tsta=20,
        Trot=20,
        type_skin_effect=1,
        is_skin_effect_inductance=True,
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
            if "is_grid_dq" in list(init_dict.keys()):
                is_grid_dq = init_dict["is_grid_dq"]
            if "Urms_max" in list(init_dict.keys()):
                Urms_max = init_dict["Urms_max"]
            if "Jrms_max" in list(init_dict.keys()):
                Jrms_max = init_dict["Jrms_max"]
            if "Irms_max" in list(init_dict.keys()):
                Irms_max = init_dict["Irms_max"]
            if "load_rate" in list(init_dict.keys()):
                load_rate = init_dict["load_rate"]
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
            if "type_skin_effect" in list(init_dict.keys()):
                type_skin_effect = init_dict["type_skin_effect"]
            if "is_skin_effect_inductance" in list(init_dict.keys()):
                is_skin_effect_inductance = init_dict["is_skin_effect_inductance"]
        # Set the properties (value check and convertion are done in setter)
        self.n_interp = n_interp
        self.Id_min = Id_min
        self.Id_max = Id_max
        self.Iq_min = Iq_min
        self.Iq_max = Iq_max
        self.n_Id = n_Id
        self.n_Iq = n_Iq
        self.LUT_simu = LUT_simu
        self.is_grid_dq = is_grid_dq
        self.Urms_max = Urms_max
        self.Jrms_max = Jrms_max
        self.Irms_max = Irms_max
        self.load_rate = load_rate
        # Call Electrical init
        super(ElecLUTdq, self).__init__(
            eec=eec,
            logger_name=logger_name,
            freq_max=freq_max,
            LUT_enforced=LUT_enforced,
            Tsta=Tsta,
            Trot=Trot,
            type_skin_effect=type_skin_effect,
            is_skin_effect_inductance=is_skin_effect_inductance,
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
        ElecLUTdq_str += "is_grid_dq = " + str(self.is_grid_dq) + linesep
        ElecLUTdq_str += "Urms_max = " + str(self.Urms_max) + linesep
        ElecLUTdq_str += "Jrms_max = " + str(self.Jrms_max) + linesep
        ElecLUTdq_str += "Irms_max = " + str(self.Irms_max) + linesep
        ElecLUTdq_str += "load_rate = " + str(self.load_rate) + linesep
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
        if other.is_grid_dq != self.is_grid_dq:
            return False
        if other.Urms_max != self.Urms_max:
            return False
        if other.Jrms_max != self.Jrms_max:
            return False
        if other.Irms_max != self.Irms_max:
            return False
        if other.load_rate != self.load_rate:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Electrical
        diff_list.extend(
            super(ElecLUTdq, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._n_interp != self._n_interp:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._n_interp)
                    + ", other="
                    + str(other._n_interp)
                    + ")"
                )
                diff_list.append(name + ".n_interp" + val_str)
            else:
                diff_list.append(name + ".n_interp")
        if (
            other._Id_min is not None
            and self._Id_min is not None
            and isnan(other._Id_min)
            and isnan(self._Id_min)
        ):
            pass
        elif other._Id_min != self._Id_min:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Id_min)
                    + ", other="
                    + str(other._Id_min)
                    + ")"
                )
                diff_list.append(name + ".Id_min" + val_str)
            else:
                diff_list.append(name + ".Id_min")
        if (
            other._Id_max is not None
            and self._Id_max is not None
            and isnan(other._Id_max)
            and isnan(self._Id_max)
        ):
            pass
        elif other._Id_max != self._Id_max:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Id_max)
                    + ", other="
                    + str(other._Id_max)
                    + ")"
                )
                diff_list.append(name + ".Id_max" + val_str)
            else:
                diff_list.append(name + ".Id_max")
        if (
            other._Iq_min is not None
            and self._Iq_min is not None
            and isnan(other._Iq_min)
            and isnan(self._Iq_min)
        ):
            pass
        elif other._Iq_min != self._Iq_min:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Iq_min)
                    + ", other="
                    + str(other._Iq_min)
                    + ")"
                )
                diff_list.append(name + ".Iq_min" + val_str)
            else:
                diff_list.append(name + ".Iq_min")
        if (
            other._Iq_max is not None
            and self._Iq_max is not None
            and isnan(other._Iq_max)
            and isnan(self._Iq_max)
        ):
            pass
        elif other._Iq_max != self._Iq_max:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Iq_max)
                    + ", other="
                    + str(other._Iq_max)
                    + ")"
                )
                diff_list.append(name + ".Iq_max" + val_str)
            else:
                diff_list.append(name + ".Iq_max")
        if other._n_Id != self._n_Id:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._n_Id) + ", other=" + str(other._n_Id) + ")"
                )
                diff_list.append(name + ".n_Id" + val_str)
            else:
                diff_list.append(name + ".n_Id")
        if other._n_Iq != self._n_Iq:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._n_Iq) + ", other=" + str(other._n_Iq) + ")"
                )
                diff_list.append(name + ".n_Iq" + val_str)
            else:
                diff_list.append(name + ".n_Iq")
        if (other.LUT_simu is None and self.LUT_simu is not None) or (
            other.LUT_simu is not None and self.LUT_simu is None
        ):
            diff_list.append(name + ".LUT_simu None mismatch")
        elif self.LUT_simu is not None:
            diff_list.extend(
                self.LUT_simu.compare(
                    other.LUT_simu,
                    name=name + ".LUT_simu",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other._is_grid_dq != self._is_grid_dq:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_grid_dq)
                    + ", other="
                    + str(other._is_grid_dq)
                    + ")"
                )
                diff_list.append(name + ".is_grid_dq" + val_str)
            else:
                diff_list.append(name + ".is_grid_dq")
        if (
            other._Urms_max is not None
            and self._Urms_max is not None
            and isnan(other._Urms_max)
            and isnan(self._Urms_max)
        ):
            pass
        elif other._Urms_max != self._Urms_max:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Urms_max)
                    + ", other="
                    + str(other._Urms_max)
                    + ")"
                )
                diff_list.append(name + ".Urms_max" + val_str)
            else:
                diff_list.append(name + ".Urms_max")
        if (
            other._Jrms_max is not None
            and self._Jrms_max is not None
            and isnan(other._Jrms_max)
            and isnan(self._Jrms_max)
        ):
            pass
        elif other._Jrms_max != self._Jrms_max:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Jrms_max)
                    + ", other="
                    + str(other._Jrms_max)
                    + ")"
                )
                diff_list.append(name + ".Jrms_max" + val_str)
            else:
                diff_list.append(name + ".Jrms_max")
        if (
            other._Irms_max is not None
            and self._Irms_max is not None
            and isnan(other._Irms_max)
            and isnan(self._Irms_max)
        ):
            pass
        elif other._Irms_max != self._Irms_max:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Irms_max)
                    + ", other="
                    + str(other._Irms_max)
                    + ")"
                )
                diff_list.append(name + ".Irms_max" + val_str)
            else:
                diff_list.append(name + ".Irms_max")
        if (
            other._load_rate is not None
            and self._load_rate is not None
            and isnan(other._load_rate)
            and isnan(self._load_rate)
        ):
            pass
        elif other._load_rate != self._load_rate:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._load_rate)
                    + ", other="
                    + str(other._load_rate)
                    + ")"
                )
                diff_list.append(name + ".load_rate" + val_str)
            else:
                diff_list.append(name + ".load_rate")
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
        S += getsizeof(self.is_grid_dq)
        S += getsizeof(self.Urms_max)
        S += getsizeof(self.Jrms_max)
        S += getsizeof(self.Irms_max)
        S += getsizeof(self.load_rate)
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
        ElecLUTdq_dict["is_grid_dq"] = self.is_grid_dq
        ElecLUTdq_dict["Urms_max"] = self.Urms_max
        ElecLUTdq_dict["Jrms_max"] = self.Jrms_max
        ElecLUTdq_dict["Irms_max"] = self.Irms_max
        ElecLUTdq_dict["load_rate"] = self.load_rate
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ElecLUTdq_dict["__class__"] = "ElecLUTdq"
        return ElecLUTdq_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        n_interp_val = self.n_interp
        Id_min_val = self.Id_min
        Id_max_val = self.Id_max
        Iq_min_val = self.Iq_min
        Iq_max_val = self.Iq_max
        n_Id_val = self.n_Id
        n_Iq_val = self.n_Iq
        if self.LUT_simu is None:
            LUT_simu_val = None
        else:
            LUT_simu_val = self.LUT_simu.copy()
        is_grid_dq_val = self.is_grid_dq
        Urms_max_val = self.Urms_max
        Jrms_max_val = self.Jrms_max
        Irms_max_val = self.Irms_max
        load_rate_val = self.load_rate
        if self.eec is None:
            eec_val = None
        else:
            eec_val = self.eec.copy()
        logger_name_val = self.logger_name
        freq_max_val = self.freq_max
        if self.LUT_enforced is None:
            LUT_enforced_val = None
        else:
            LUT_enforced_val = self.LUT_enforced.copy()
        Tsta_val = self.Tsta
        Trot_val = self.Trot
        type_skin_effect_val = self.type_skin_effect
        is_skin_effect_inductance_val = self.is_skin_effect_inductance
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            n_interp=n_interp_val,
            Id_min=Id_min_val,
            Id_max=Id_max_val,
            Iq_min=Iq_min_val,
            Iq_max=Iq_max_val,
            n_Id=n_Id_val,
            n_Iq=n_Iq_val,
            LUT_simu=LUT_simu_val,
            is_grid_dq=is_grid_dq_val,
            Urms_max=Urms_max_val,
            Jrms_max=Jrms_max_val,
            Irms_max=Irms_max_val,
            load_rate=load_rate_val,
            eec=eec_val,
            logger_name=logger_name_val,
            freq_max=freq_max_val,
            LUT_enforced=LUT_enforced_val,
            Tsta=Tsta_val,
            Trot=Trot_val,
            type_skin_effect=type_skin_effect_val,
            is_skin_effect_inductance=is_skin_effect_inductance_val,
        )
        return obj_copy

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
        self.is_grid_dq = None
        self.Urms_max = None
        self.Jrms_max = None
        self.Irms_max = None
        self.load_rate = None
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

    def _get_is_grid_dq(self):
        """getter of is_grid_dq"""
        return self._is_grid_dq

    def _set_is_grid_dq(self, value):
        """setter of is_grid_dq"""
        check_var("is_grid_dq", value, "bool")
        self._is_grid_dq = value

    is_grid_dq = property(
        fget=_get_is_grid_dq,
        fset=_set_is_grid_dq,
        doc=u"""True to build a n_Id*n_Iq grid, otherwise calculate n_Id+n_Iq simulations and extrapolate to the dq plane

        :Type: bool
        """,
    )

    def _get_Urms_max(self):
        """getter of Urms_max"""
        return self._Urms_max

    def _set_Urms_max(self, value):
        """setter of Urms_max"""
        check_var("Urms_max", value, "float", Vmin=0)
        self._Urms_max = value

    Urms_max = property(
        fget=_get_Urms_max,
        fset=_set_Urms_max,
        doc=u"""Maximum rms phase voltage

        :Type: float
        :min: 0
        """,
    )

    def _get_Jrms_max(self):
        """getter of Jrms_max"""
        return self._Jrms_max

    def _set_Jrms_max(self, value):
        """setter of Jrms_max"""
        check_var("Jrms_max", value, "float", Vmin=0)
        self._Jrms_max = value

    Jrms_max = property(
        fget=_get_Jrms_max,
        fset=_set_Jrms_max,
        doc=u"""Maximum rms current density in slot

        :Type: float
        :min: 0
        """,
    )

    def _get_Irms_max(self):
        """getter of Irms_max"""
        return self._Irms_max

    def _set_Irms_max(self, value):
        """setter of Irms_max"""
        check_var("Irms_max", value, "float", Vmin=0)
        self._Irms_max = value

    Irms_max = property(
        fget=_get_Irms_max,
        fset=_set_Irms_max,
        doc=u"""Maximum rms phase current

        :Type: float
        :min: 0
        """,
    )

    def _get_load_rate(self):
        """getter of load_rate"""
        return self._load_rate

    def _set_load_rate(self, value):
        """setter of load_rate"""
        check_var("load_rate", value, "float", Vmin=0, Vmax=1)
        self._load_rate = value

    load_rate = property(
        fget=_get_load_rate,
        fset=_set_load_rate,
        doc=u"""Load rate between 0 (no-load) and 1 (full-load) for MTPA calculation

        :Type: float
        :min: 0
        :max: 1
        """,
    )
