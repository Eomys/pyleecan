# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Optimization/OptiObjFunc.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from pyleecan.Classes._check import check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes._frozen import FrozenClass

from inspect import getsource
from cloudpickle import dumps, loads
from pyleecan.Classes._check import CheckTypeError
from pyleecan.Classes._check import InitUnKnowClassError


class OptiObjFunc(FrozenClass):
    """Optimization"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, description="'", func=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "description" in list(init_dict.keys()):
                description = init_dict["description"]
            if "func" in list(init_dict.keys()):
                func = init_dict["func"]
        # Initialisation by argument
        self.parent = None
        self.description = description
        self.func = func

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OptiObjFunc_str = ""
        if self.parent is None:
            OptiObjFunc_str += "parent = None " + linesep
        else:
            OptiObjFunc_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        OptiObjFunc_str += 'description = "' + str(self.description) + '"' + linesep
        if self._func[1] is None:
            OptiObjFunc_str += "func = " + str(self._func[1])
        else:
            OptiObjFunc_str += (
                "func = " + linesep + str(self._func[1]) + linesep + linesep
            )
        return OptiObjFunc_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.description != self.description:
            return False
        if other.func != self.func:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OptiObjFunc_dict = dict()
        OptiObjFunc_dict["description"] = self.description
        if self.func is None:
            OptiObjFunc_dict["func"] = None
        else:
            OptiObjFunc_dict["func"] = [
                dumps(self._func[0]).decode("ISO-8859-2"),
                self._func[1],
            ]
        # The class name is added to the dict fordeserialisation purpose
        OptiObjFunc_dict["__class__"] = "OptiObjFunc"
        return OptiObjFunc_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.description = None
        self.func = None

    def get_logger(self):
        """getter of the logger"""
        if hasattr(self, "logger_name"):
            return getLogger(self.logger_name)
        elif self.parent != None:
            return self.parent.get_logger()
        else:
            return getLogger("Pyleecan")

    def _get_description(self):
        """getter of description"""
        return self._description

    def _set_description(self, value):
        """setter of description"""
        check_var("description", value, "str")
        self._description = value

    # Description of the objective
    # Type : str
    description = property(
        fget=_get_description,
        fset=_set_description,
        doc=u"""Description of the objective""",
    )

    def _get_func(self):
        """getter of func"""
        return self._func[0]

    def _set_func(self, value):
        """setter of func"""
        try:
            check_var("func", value, "list")
        except CheckTypeError:
            check_var("func", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._func = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._func = [None, None]
        elif callable(value):
            self._func = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    # Function to minimize
    # Type : function
    func = property(fget=_get_func, fset=_set_func, doc=u"""Function to minimize""")
