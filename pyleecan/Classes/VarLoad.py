# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/VarLoad.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/VarLoad
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
from .VarSimu import VarSimu

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.VarLoad.get_elec_datakeeper import get_elec_datakeeper
except ImportError as error:
    get_elec_datakeeper = error

try:
    from ..Methods.Simulation.VarLoad.get_mag_datakeeper import get_mag_datakeeper
except ImportError as error:
    get_mag_datakeeper = error

try:
    from ..Methods.Simulation.VarLoad.get_force_datakeeper import get_force_datakeeper
except ImportError as error:
    get_force_datakeeper = error


from ._check import InitUnKnowClassError
from .DataKeeper import DataKeeper
from .VarSimu import VarSimu
from .Post import Post


class VarLoad(VarSimu):
    """Abstract class to generate multi-simulation by changing the operating point"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.VarLoad.get_elec_datakeeper
    if isinstance(get_elec_datakeeper, ImportError):
        get_elec_datakeeper = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarLoad method get_elec_datakeeper: "
                    + str(get_elec_datakeeper)
                )
            )
        )
    else:
        get_elec_datakeeper = get_elec_datakeeper
    # cf Methods.Simulation.VarLoad.get_mag_datakeeper
    if isinstance(get_mag_datakeeper, ImportError):
        get_mag_datakeeper = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarLoad method get_mag_datakeeper: "
                    + str(get_mag_datakeeper)
                )
            )
        )
    else:
        get_mag_datakeeper = get_mag_datakeeper
    # cf Methods.Simulation.VarLoad.get_force_datakeeper
    if isinstance(get_force_datakeeper, ImportError):
        get_force_datakeeper = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarLoad method get_force_datakeeper: "
                    + str(get_force_datakeeper)
                )
            )
        )
    else:
        get_force_datakeeper = get_force_datakeeper
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name="",
        desc="",
        datakeeper_list=-1,
        is_keep_all_output=False,
        stop_if_error=False,
        var_simu=None,
        ref_simu_index=None,
        nb_simu=0,
        is_reuse_femm_file=True,
        postproc_list=-1,
        pre_keeper_postproc_list=None,
        post_keeper_postproc_list=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "datakeeper_list" in list(init_dict.keys()):
                datakeeper_list = init_dict["datakeeper_list"]
            if "is_keep_all_output" in list(init_dict.keys()):
                is_keep_all_output = init_dict["is_keep_all_output"]
            if "stop_if_error" in list(init_dict.keys()):
                stop_if_error = init_dict["stop_if_error"]
            if "var_simu" in list(init_dict.keys()):
                var_simu = init_dict["var_simu"]
            if "ref_simu_index" in list(init_dict.keys()):
                ref_simu_index = init_dict["ref_simu_index"]
            if "nb_simu" in list(init_dict.keys()):
                nb_simu = init_dict["nb_simu"]
            if "is_reuse_femm_file" in list(init_dict.keys()):
                is_reuse_femm_file = init_dict["is_reuse_femm_file"]
            if "postproc_list" in list(init_dict.keys()):
                postproc_list = init_dict["postproc_list"]
            if "pre_keeper_postproc_list" in list(init_dict.keys()):
                pre_keeper_postproc_list = init_dict["pre_keeper_postproc_list"]
            if "post_keeper_postproc_list" in list(init_dict.keys()):
                post_keeper_postproc_list = init_dict["post_keeper_postproc_list"]
        # Set the properties (value check and convertion are done in setter)
        # Call VarSimu init
        super(VarLoad, self).__init__(
            name=name,
            desc=desc,
            datakeeper_list=datakeeper_list,
            is_keep_all_output=is_keep_all_output,
            stop_if_error=stop_if_error,
            var_simu=var_simu,
            ref_simu_index=ref_simu_index,
            nb_simu=nb_simu,
            is_reuse_femm_file=is_reuse_femm_file,
            postproc_list=postproc_list,
            pre_keeper_postproc_list=pre_keeper_postproc_list,
            post_keeper_postproc_list=post_keeper_postproc_list,
        )
        # The class is frozen (in VarSimu init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        VarLoad_str = ""
        # Get the properties inherited from VarSimu
        VarLoad_str += super(VarLoad, self).__str__()
        return VarLoad_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from VarSimu
        if not super(VarLoad, self).__eq__(other):
            return False
        return True

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from VarSimu
        S += super(VarLoad, self).__sizeof__()
        return S

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from VarSimu
        VarLoad_dict = super(VarLoad, self).as_dict()
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        VarLoad_dict["__class__"] = "VarLoad"
        return VarLoad_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from VarSimu
        super(VarLoad, self)._set_None()
