# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/VarSimu.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/VarSimu
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.VarSimu.run import run
except ImportError as error:
    run = error


from ._check import InitUnKnowClassError
from .DataKeeper import DataKeeper


class VarSimu(FrozenClass):
    """Abstract class for the multi-simulation"""

    VERSION = 1

    # cf Methods.Simulation.VarSimu.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use VarSimu method run: " + str(run))
            )
        )
    else:
        run = run
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name="",
        desc="",
        datakeeper_list=list(),
        nb_proc=1,
        is_keep_all_output=False,
        stop_if_error=False,
        ref_simu_index=None,
        nb_simu=0,
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
            name = obj.name
            desc = obj.desc
            datakeeper_list = obj.datakeeper_list
            nb_proc = obj.nb_proc
            is_keep_all_output = obj.is_keep_all_output
            stop_if_error = obj.stop_if_error
            ref_simu_index = obj.ref_simu_index
            nb_simu = obj.nb_simu
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "datakeeper_list" in list(init_dict.keys()):
                datakeeper_list = init_dict["datakeeper_list"]
            if "nb_proc" in list(init_dict.keys()):
                nb_proc = init_dict["nb_proc"]
            if "is_keep_all_output" in list(init_dict.keys()):
                is_keep_all_output = init_dict["is_keep_all_output"]
            if "stop_if_error" in list(init_dict.keys()):
                stop_if_error = init_dict["stop_if_error"]
            if "ref_simu_index" in list(init_dict.keys()):
                ref_simu_index = init_dict["ref_simu_index"]
            if "nb_simu" in list(init_dict.keys()):
                nb_simu = init_dict["nb_simu"]
        # Initialisation by argument
        self.parent = None
        self.name = name
        self.desc = desc
        # datakeeper_list can be None or a list of DataKeeper object
        self.datakeeper_list = list()
        if type(datakeeper_list) is list:
            for obj in datakeeper_list:
                if obj is None:  # Default value
                    self.datakeeper_list.append(DataKeeper())
                elif isinstance(obj, dict):
                    self.datakeeper_list.append(DataKeeper(init_dict=obj))
                else:
                    self.datakeeper_list.append(obj)
        elif datakeeper_list is None:
            self.datakeeper_list = list()
        else:
            self.datakeeper_list = datakeeper_list
        self.nb_proc = nb_proc
        self.is_keep_all_output = is_keep_all_output
        self.stop_if_error = stop_if_error
        self.ref_simu_index = ref_simu_index
        self.nb_simu = nb_simu

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        VarSimu_str = ""
        if self.parent is None:
            VarSimu_str += "parent = None " + linesep
        else:
            VarSimu_str += "parent = " + str(type(self.parent)) + " object" + linesep
        VarSimu_str += 'name = "' + str(self.name) + '"' + linesep
        VarSimu_str += 'desc = "' + str(self.desc) + '"' + linesep
        if len(self.datakeeper_list) == 0:
            VarSimu_str += "datakeeper_list = []" + linesep
        for ii in range(len(self.datakeeper_list)):
            tmp = (
                self.datakeeper_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            VarSimu_str += (
                "datakeeper_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        VarSimu_str += "nb_proc = " + str(self.nb_proc) + linesep
        VarSimu_str += "is_keep_all_output = " + str(self.is_keep_all_output) + linesep
        VarSimu_str += "stop_if_error = " + str(self.stop_if_error) + linesep
        VarSimu_str += "ref_simu_index = " + str(self.ref_simu_index) + linesep
        VarSimu_str += "nb_simu = " + str(self.nb_simu) + linesep
        return VarSimu_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        if other.desc != self.desc:
            return False
        if other.datakeeper_list != self.datakeeper_list:
            return False
        if other.nb_proc != self.nb_proc:
            return False
        if other.is_keep_all_output != self.is_keep_all_output:
            return False
        if other.stop_if_error != self.stop_if_error:
            return False
        if other.ref_simu_index != self.ref_simu_index:
            return False
        if other.nb_simu != self.nb_simu:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        VarSimu_dict = dict()
        VarSimu_dict["name"] = self.name
        VarSimu_dict["desc"] = self.desc
        VarSimu_dict["datakeeper_list"] = list()
        for obj in self.datakeeper_list:
            VarSimu_dict["datakeeper_list"].append(obj.as_dict())
        VarSimu_dict["nb_proc"] = self.nb_proc
        VarSimu_dict["is_keep_all_output"] = self.is_keep_all_output
        VarSimu_dict["stop_if_error"] = self.stop_if_error
        VarSimu_dict["ref_simu_index"] = self.ref_simu_index
        VarSimu_dict["nb_simu"] = self.nb_simu
        # The class name is added to the dict fordeserialisation purpose
        VarSimu_dict["__class__"] = "VarSimu"
        return VarSimu_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.desc = None
        for obj in self.datakeeper_list:
            obj._set_None()
        self.nb_proc = None
        self.is_keep_all_output = None
        self.stop_if_error = None
        self.ref_simu_index = None
        self.nb_simu = None

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""Name of the multi-simulation

        :Type: str
        """,
    )

    def _get_desc(self):
        """getter of desc"""
        return self._desc

    def _set_desc(self, value):
        """setter of desc"""
        check_var("desc", value, "str")
        self._desc = value

    desc = property(
        fget=_get_desc,
        fset=_set_desc,
        doc=u"""Multi-simulation description

        :Type: str
        """,
    )

    def _get_datakeeper_list(self):
        """getter of datakeeper_list"""
        for obj in self._datakeeper_list:
            if obj is not None:
                obj.parent = self
        return self._datakeeper_list

    def _set_datakeeper_list(self, value):
        """setter of datakeeper_list"""
        check_var("datakeeper_list", value, "[DataKeeper]")
        self._datakeeper_list = value

        for obj in self._datakeeper_list:
            if obj is not None:
                obj.parent = self

    datakeeper_list = property(
        fget=_get_datakeeper_list,
        fset=_set_datakeeper_list,
        doc=u"""List containing DataKeepers to extract VarSimu results 

        :Type: [DataKeeper]
        """,
    )

    def _get_nb_proc(self):
        """getter of nb_proc"""
        return self._nb_proc

    def _set_nb_proc(self, value):
        """setter of nb_proc"""
        check_var("nb_proc", value, "int", Vmin=1)
        self._nb_proc = value

    nb_proc = property(
        fget=_get_nb_proc,
        fset=_set_nb_proc,
        doc=u"""Number of processors used to run the simulations

        :Type: int
        :min: 1
        """,
    )

    def _get_is_keep_all_output(self):
        """getter of is_keep_all_output"""
        return self._is_keep_all_output

    def _set_is_keep_all_output(self, value):
        """setter of is_keep_all_output"""
        check_var("is_keep_all_output", value, "bool")
        self._is_keep_all_output = value

    is_keep_all_output = property(
        fget=_get_is_keep_all_output,
        fset=_set_is_keep_all_output,
        doc=u"""True to store every output in a list

        :Type: bool
        """,
    )

    def _get_stop_if_error(self):
        """getter of stop_if_error"""
        return self._stop_if_error

    def _set_stop_if_error(self, value):
        """setter of stop_if_error"""
        check_var("stop_if_error", value, "bool")
        self._stop_if_error = value

    stop_if_error = property(
        fget=_get_stop_if_error,
        fset=_set_stop_if_error,
        doc=u"""Stop the multi-simulation if a simulation fails 

        :Type: bool
        """,
    )

    def _get_ref_simu_index(self):
        """getter of ref_simu_index"""
        return self._ref_simu_index

    def _set_ref_simu_index(self, value):
        """setter of ref_simu_index"""
        check_var("ref_simu_index", value, "int", Vmin=0)
        self._ref_simu_index = value

    ref_simu_index = property(
        fget=_get_ref_simu_index,
        fset=_set_ref_simu_index,
        doc=u"""Index of the reference simulation, if None the reference simulation is not in the multi-simulation

        :Type: int
        :min: 0
        """,
    )

    def _get_nb_simu(self):
        """getter of nb_simu"""
        return self._nb_simu

    def _set_nb_simu(self, value):
        """setter of nb_simu"""
        check_var("nb_simu", value, "int")
        self._nb_simu = value

    nb_simu = property(
        fget=_get_nb_simu,
        fset=_set_nb_simu,
        doc=u"""Number of simulations

        :Type: int
        """,
    )
