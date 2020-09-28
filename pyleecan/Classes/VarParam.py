# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/VarParam.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/VarParam
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .VarSimu import VarSimu

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.VarParam.check_param import check_param
except ImportError as error:
    check_param = error

try:
    from ..Methods.Simulation.VarParam.get_simulations import get_simulations
except ImportError as error:
    get_simulations = error


from ._check import InitUnKnowClassError
from .ParamExplorer import ParamExplorer
from .DataKeeper import DataKeeper
from .Post import Post


class VarParam(VarSimu):
    """Handle multisimulation by varying parameters"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.VarParam.check_param
    if isinstance(check_param, ImportError):
        check_param = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarParam method check_param: " + str(check_param)
                )
            )
        )
    else:
        check_param = check_param
    # cf Methods.Simulation.VarParam.get_simulations
    if isinstance(get_simulations, ImportError):
        get_simulations = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VarParam method get_simulations: " + str(get_simulations)
                )
            )
        )
    else:
        get_simulations = get_simulations
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        paramexplorer_list=list(),
        name="",
        desc="",
        datakeeper_list=list(),
        is_keep_all_output=False,
        stop_if_error=False,
        ref_simu_index=None,
        nb_simu=0,
        is_reuse_femm_file=True,
        postproc_list=list(),
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            paramexplorer_list = obj.paramexplorer_list
            name = obj.name
            desc = obj.desc
            datakeeper_list = obj.datakeeper_list
            is_keep_all_output = obj.is_keep_all_output
            stop_if_error = obj.stop_if_error
            ref_simu_index = obj.ref_simu_index
            nb_simu = obj.nb_simu
            is_reuse_femm_file = obj.is_reuse_femm_file
            postproc_list = obj.postproc_list
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "paramexplorer_list" in list(init_dict.keys()):
                paramexplorer_list = init_dict["paramexplorer_list"]
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
            if "ref_simu_index" in list(init_dict.keys()):
                ref_simu_index = init_dict["ref_simu_index"]
            if "nb_simu" in list(init_dict.keys()):
                nb_simu = init_dict["nb_simu"]
            if "is_reuse_femm_file" in list(init_dict.keys()):
                is_reuse_femm_file = init_dict["is_reuse_femm_file"]
            if "postproc_list" in list(init_dict.keys()):
                postproc_list = init_dict["postproc_list"]
        # Initialisation by argument
        # paramexplorer_list can be None or a list of ParamExplorer object or a list of dict
        if type(paramexplorer_list) is list:
            # Check if the list is only composed of ParamExplorer
            if len(paramexplorer_list) > 0 and all(
                isinstance(obj, ParamExplorer) for obj in paramexplorer_list
            ):
                # set the list to keep pointer reference
                self.paramexplorer_list = paramexplorer_list
            else:
                self.paramexplorer_list = list()
                for obj in paramexplorer_list:
                    if not isinstance(obj, dict):  # Default value
                        self.paramexplorer_list.append(obj)
                    elif isinstance(obj, dict):
                        # Check that the type is correct (including daughter)
                        class_name = obj.get("__class__")
                        if class_name not in [
                            "ParamExplorer",
                            "OptiDesignVar",
                            "ParamExplorerSet",
                        ]:
                            raise InitUnKnowClassError(
                                "Unknow class name "
                                + class_name
                                + " in init_dict for paramexplorer_list"
                            )
                        # Dynamic import to call the correct constructor
                        module = __import__(
                            "pyleecan.Classes." + class_name, fromlist=[class_name]
                        )
                        class_obj = getattr(module, class_name)
                        self.paramexplorer_list.append(class_obj(init_dict=obj))

        elif paramexplorer_list is None:
            self.paramexplorer_list = list()
        else:
            self.paramexplorer_list = paramexplorer_list
        # Call VarSimu init
        super(VarParam, self).__init__(
            name=name,
            desc=desc,
            datakeeper_list=datakeeper_list,
            is_keep_all_output=is_keep_all_output,
            stop_if_error=stop_if_error,
            ref_simu_index=ref_simu_index,
            nb_simu=nb_simu,
            is_reuse_femm_file=is_reuse_femm_file,
            postproc_list=postproc_list,
        )
        # The class is frozen (in VarSimu init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        VarParam_str = ""
        # Get the properties inherited from VarSimu
        VarParam_str += super(VarParam, self).__str__()
        if len(self.paramexplorer_list) == 0:
            VarParam_str += "paramexplorer_list = []" + linesep
        for ii in range(len(self.paramexplorer_list)):
            tmp = (
                self.paramexplorer_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            VarParam_str += (
                "paramexplorer_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        return VarParam_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from VarSimu
        if not super(VarParam, self).__eq__(other):
            return False
        if other.paramexplorer_list != self.paramexplorer_list:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from VarSimu
        VarParam_dict = super(VarParam, self).as_dict()
        VarParam_dict["paramexplorer_list"] = list()
        for obj in self.paramexplorer_list:
            VarParam_dict["paramexplorer_list"].append(obj.as_dict())
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        VarParam_dict["__class__"] = "VarParam"
        return VarParam_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.paramexplorer_list:
            obj._set_None()
        # Set to None the properties inherited from VarSimu
        super(VarParam, self)._set_None()

    def _get_paramexplorer_list(self):
        """getter of paramexplorer_list"""
        for obj in self._paramexplorer_list:
            if obj is not None:
                obj.parent = self
        return self._paramexplorer_list

    def _set_paramexplorer_list(self, value):
        """setter of paramexplorer_list"""
        check_var("paramexplorer_list", value, "[ParamExplorer]")
        self._paramexplorer_list = value

        for obj in self._paramexplorer_list:
            if obj is not None:
                obj.parent = self

    paramexplorer_list = property(
        fget=_get_paramexplorer_list,
        fset=_set_paramexplorer_list,
        doc=u"""List containing ParamSetter to define every simulation

        :Type: [ParamExplorer]
        """,
    )
