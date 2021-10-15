# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/ForceMT.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/ForceMT
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
from .Force import Force

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.ForceMT.comp_force import comp_force
except ImportError as error:
    comp_force = error

try:
    from ..Methods.Simulation.ForceMT.comp_force_nodal import comp_force_nodal
except ImportError as error:
    comp_force_nodal = error


from ._check import InitUnKnowClassError


class ForceMT(Force):
    """Force Maxwell tensor model for radial flux machines"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.ForceMT.comp_force
    if isinstance(comp_force, ImportError):
        comp_force = property(
            fget=lambda x: raise_(
                ImportError("Can't use ForceMT method comp_force: " + str(comp_force))
            )
        )
    else:
        comp_force = comp_force
    # cf Methods.Simulation.ForceMT.comp_force_nodal
    if isinstance(comp_force_nodal, ImportError):
        comp_force_nodal = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ForceMT method comp_force_nodal: "
                    + str(comp_force_nodal)
                )
            )
        )
    else:
        comp_force_nodal = comp_force_nodal
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        is_periodicity_t=None,
        is_periodicity_a=None,
        is_agsf_transfer=False,
        max_wavenumber_transfer=None,
        Rsbo_enforced_transfer=None,
        logger_name="Pyleecan.Force",
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
            if "is_periodicity_t" in list(init_dict.keys()):
                is_periodicity_t = init_dict["is_periodicity_t"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
            if "is_agsf_transfer" in list(init_dict.keys()):
                is_agsf_transfer = init_dict["is_agsf_transfer"]
            if "max_wavenumber_transfer" in list(init_dict.keys()):
                max_wavenumber_transfer = init_dict["max_wavenumber_transfer"]
            if "Rsbo_enforced_transfer" in list(init_dict.keys()):
                Rsbo_enforced_transfer = init_dict["Rsbo_enforced_transfer"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        # Call Force init
        super(ForceMT, self).__init__(
            is_periodicity_t=is_periodicity_t,
            is_periodicity_a=is_periodicity_a,
            is_agsf_transfer=is_agsf_transfer,
            max_wavenumber_transfer=max_wavenumber_transfer,
            Rsbo_enforced_transfer=Rsbo_enforced_transfer,
            logger_name=logger_name,
        )
        # The class is frozen (in Force init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ForceMT_str = ""
        # Get the properties inherited from Force
        ForceMT_str += super(ForceMT, self).__str__()
        return ForceMT_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Force
        if not super(ForceMT, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Force
        diff_list.extend(super(ForceMT, self).compare(other, name=name))
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Force
        S += super(ForceMT, self).__sizeof__()
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

        # Get the properties inherited from Force
        ForceMT_dict = super(ForceMT, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ForceMT_dict["__class__"] = "ForceMT"
        return ForceMT_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Force
        super(ForceMT, self)._set_None()
