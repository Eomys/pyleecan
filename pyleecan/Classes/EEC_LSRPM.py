# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/EEC_LSRPM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/EEC_LSRPM
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
from .EEC import EEC

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.EEC_LSRPM.comp_parameters import comp_parameters
except ImportError as error:
    comp_parameters = error

try:
    from ..Methods.Simulation.EEC_LSRPM.solve import solve
except ImportError as error:
    solve = error

try:
    from ..Methods.Simulation.EEC_LSRPM.comp_joule_losses import comp_joule_losses
except ImportError as error:
    comp_joule_losses = error


from ._check import InitUnKnowClassError


class EEC_LSRPM(EEC):
    """Electrical Equivalent Circuit for LSRPM"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.EEC_LSRPM.comp_parameters
    if isinstance(comp_parameters, ImportError):
        comp_parameters = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_LSRPM method comp_parameters: "
                    + str(comp_parameters)
                )
            )
        )
    else:
        comp_parameters = comp_parameters
    # cf Methods.Simulation.EEC_LSRPM.solve
    if isinstance(solve, ImportError):
        solve = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_LSRPM method solve: " + str(solve))
            )
        )
    else:
        solve = solve
    # cf Methods.Simulation.EEC_LSRPM.comp_joule_losses
    if isinstance(comp_joule_losses, ImportError):
        comp_joule_losses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_LSRPM method comp_joule_losses: "
                    + str(comp_joule_losses)
                )
            )
        )
    else:
        comp_joule_losses = comp_joule_losses
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        type_skin_effect=1,
        OP=None,
        Tsta=20,
        Trot=20,
        Xkr_skinS=1,
        Xke_skinS=1,
        Xkr_skinR=1,
        Xke_skinR=1,
        R1=None,
        fluxlink=None,
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
            if "type_skin_effect" in list(init_dict.keys()):
                type_skin_effect = init_dict["type_skin_effect"]
            if "OP" in list(init_dict.keys()):
                OP = init_dict["OP"]
            if "Tsta" in list(init_dict.keys()):
                Tsta = init_dict["Tsta"]
            if "Trot" in list(init_dict.keys()):
                Trot = init_dict["Trot"]
            if "Xkr_skinS" in list(init_dict.keys()):
                Xkr_skinS = init_dict["Xkr_skinS"]
            if "Xke_skinS" in list(init_dict.keys()):
                Xke_skinS = init_dict["Xke_skinS"]
            if "Xkr_skinR" in list(init_dict.keys()):
                Xkr_skinR = init_dict["Xkr_skinR"]
            if "Xke_skinR" in list(init_dict.keys()):
                Xke_skinR = init_dict["Xke_skinR"]
            if "R1" in list(init_dict.keys()):
                R1 = init_dict["R1"]
            if "fluxlink" in list(init_dict.keys()):
                fluxlink = init_dict["fluxlink"]
        # Set the properties (value check and convertion are done in setter)
        # Call EEC init
        super(EEC_LSRPM, self).__init__(
            type_skin_effect=type_skin_effect,
            OP=OP,
            Tsta=Tsta,
            Trot=Trot,
            Xkr_skinS=Xkr_skinS,
            Xke_skinS=Xke_skinS,
            Xkr_skinR=Xkr_skinR,
            Xke_skinR=Xke_skinR,
            R1=R1,
            fluxlink=fluxlink,
        )
        # The class is frozen (in EEC init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        EEC_LSRPM_str = ""
        # Get the properties inherited from EEC
        EEC_LSRPM_str += super(EEC_LSRPM, self).__str__()
        return EEC_LSRPM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from EEC
        if not super(EEC_LSRPM, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from EEC
        diff_list.extend(super(EEC_LSRPM, self).compare(other, name=name))
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from EEC
        S += super(EEC_LSRPM, self).__sizeof__()
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

        # Get the properties inherited from EEC
        EEC_LSRPM_dict = super(EEC_LSRPM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        EEC_LSRPM_dict["__class__"] = "EEC_LSRPM"
        return EEC_LSRPM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from EEC
        super(EEC_LSRPM, self)._set_None()
