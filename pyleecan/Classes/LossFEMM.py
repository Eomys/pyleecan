# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/LossFEMM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/LossFEMM
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
from .Loss import Loss

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.LossFEMM.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Simulation.LossFEMM.comp_loss_density_core import (
        comp_loss_density_core,
    )
except ImportError as error:
    comp_loss_density_core = error

try:
    from ..Methods.Simulation.LossFEMM.comp_loss_density_joule import (
        comp_loss_density_joule,
    )
except ImportError as error:
    comp_loss_density_joule = error

try:
    from ..Methods.Simulation.LossFEMM.comp_loss_density_magnet import (
        comp_loss_density_magnet,
    )
except ImportError as error:
    comp_loss_density_magnet = error

try:
    from ..Methods.Simulation.LossFEMM.comp_loss import comp_loss
except ImportError as error:
    comp_loss = error


from numpy import isnan
from ._check import InitUnKnowClassError


class LossFEMM(Loss):
    """Loss module dedicated to FEMM developed in https://www.femm.info/wiki/SPMLoss"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.LossFEMM.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use LossFEMM method run: " + str(run))
            )
        )
    else:
        run = run
    # cf Methods.Simulation.LossFEMM.comp_loss_density_core
    if isinstance(comp_loss_density_core, ImportError):
        comp_loss_density_core = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossFEMM method comp_loss_density_core: "
                    + str(comp_loss_density_core)
                )
            )
        )
    else:
        comp_loss_density_core = comp_loss_density_core
    # cf Methods.Simulation.LossFEMM.comp_loss_density_joule
    if isinstance(comp_loss_density_joule, ImportError):
        comp_loss_density_joule = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossFEMM method comp_loss_density_joule: "
                    + str(comp_loss_density_joule)
                )
            )
        )
    else:
        comp_loss_density_joule = comp_loss_density_joule
    # cf Methods.Simulation.LossFEMM.comp_loss_density_magnet
    if isinstance(comp_loss_density_magnet, ImportError):
        comp_loss_density_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossFEMM method comp_loss_density_magnet: "
                    + str(comp_loss_density_magnet)
                )
            )
        )
    else:
        comp_loss_density_magnet = comp_loss_density_magnet
    # cf Methods.Simulation.LossFEMM.comp_loss
    if isinstance(comp_loss, ImportError):
        comp_loss = property(
            fget=lambda x: raise_(
                ImportError("Can't use LossFEMM method comp_loss: " + str(comp_loss))
            )
        )
    else:
        comp_loss = comp_loss
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        logger_name="Pyleecan.Loss",
        model_dict=None,
        Tsta=20,
        Trot=20,
        is_get_meshsolution=False,
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
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "model_dict" in list(init_dict.keys()):
                model_dict = init_dict["model_dict"]
            if "Tsta" in list(init_dict.keys()):
                Tsta = init_dict["Tsta"]
            if "Trot" in list(init_dict.keys()):
                Trot = init_dict["Trot"]
            if "is_get_meshsolution" in list(init_dict.keys()):
                is_get_meshsolution = init_dict["is_get_meshsolution"]
        # Set the properties (value check and convertion are done in setter)
        # Call Loss init
        super(LossFEMM, self).__init__(
            logger_name=logger_name,
            model_dict=model_dict,
            Tsta=Tsta,
            Trot=Trot,
            is_get_meshsolution=is_get_meshsolution,
        )
        # The class is frozen (in Loss init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LossFEMM_str = ""
        # Get the properties inherited from Loss
        LossFEMM_str += super(LossFEMM, self).__str__()
        return LossFEMM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Loss
        if not super(LossFEMM, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Loss
        diff_list.extend(
            super(LossFEMM, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Loss
        S += super(LossFEMM, self).__sizeof__()
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

        # Get the properties inherited from Loss
        LossFEMM_dict = super(LossFEMM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LossFEMM_dict["__class__"] = "LossFEMM"
        return LossFEMM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Loss
        super(LossFEMM, self)._set_None()
