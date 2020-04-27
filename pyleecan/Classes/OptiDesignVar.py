# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Optimization/OptiDesignVar.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from inspect import getsource
from cloudpickle import dumps, loads
from ._check import CheckTypeError
from ._check import InitUnKnowClassError


class OptiDesignVar(FrozenClass):
    """Optimization"""

    VERSION = 1

    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        name="",
        type_var="interval",
        space=[0, 1],
        function=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object
        - __init__ (init_str = s) s must be a string
        s is the file path to load """

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            name = obj.name
            type_var = obj.type_var
            space = obj.space
            function = obj.function
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "type_var" in list(init_dict.keys()):
                type_var = init_dict["type_var"]
            if "space" in list(init_dict.keys()):
                space = init_dict["space"]
            if "function" in list(init_dict.keys()):
                function = init_dict["function"]
        # Initialisation by argument
        self.parent = None
        self.name = name
        self.type_var = type_var
        self.space = space
        self.function = function

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OptiDesignVar_str = ""
        if self.parent is None:
            OptiDesignVar_str += "parent = None " + linesep
        else:
            OptiDesignVar_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        OptiDesignVar_str += 'name = "' + str(self.name) + '"' + linesep
        OptiDesignVar_str += 'type_var = "' + str(self.type_var) + '"' + linesep
        OptiDesignVar_str += (
            "space = "
            + linesep
            + str(self.space).replace(linesep, linesep + "\t")
            + linesep
        )
        if self._function[1] is None:
            OptiDesignVar_str += "function = " + str(self._function[1])
        else:
            OptiDesignVar_str += (
                "function = " + linesep + str(self._function[1]) + linesep + linesep
            )
        return OptiDesignVar_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        if other.type_var != self.type_var:
            return False
        if other.space != self.space:
            return False
        if other.function != self.function:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OptiDesignVar_dict = dict()
        OptiDesignVar_dict["name"] = self.name
        OptiDesignVar_dict["type_var"] = self.type_var
        OptiDesignVar_dict["space"] = self.space
        if self.function is None:
            OptiDesignVar_dict["function"] = None
        else:
            OptiDesignVar_dict["function"] = [
                dumps(self._function[0]).decode("ISO-8859-2"),
                self._function[1],
            ]
        # The class name is added to the dict fordeserialisation purpose
        OptiDesignVar_dict["__class__"] = "OptiDesignVar"
        return OptiDesignVar_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        self.type_var = None
        self.space = None
        self.function = None

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    # name of the design variable
    # Type : str
    name = property(
        fget=_get_name, fset=_set_name, doc=u"""name of the design variable"""
    )

    def _get_type_var(self):
        """getter of type_var"""
        return self._type_var

    def _set_type_var(self, value):
        """setter of type_var"""
        check_var("type_var", value, "str")
        self._type_var = value

    # Type of the variable interval or set.
    # Type : str
    type_var = property(
        fget=_get_type_var,
        fset=_set_type_var,
        doc=u"""Type of the variable interval or set.""",
    )

    def _get_space(self):
        """getter of space"""
        return self._space

    def _set_space(self, value):
        """setter of space"""
        check_var("space", value, "list")
        self._space = value

    # Space of the variable
    # Type : list
    space = property(fget=_get_space, fset=_set_space, doc=u"""Space of the variable""")

    def _get_function(self):
        """getter of function"""
        return self._function[0]

    def _set_function(self, value):
        """setter of function"""
        try:
            check_var("function", value, "list")
        except CheckTypeError:
            check_var("function", value, "function")
        if isinstance(value, list):  # Load function from saved dict
            self._function = [loads(value[0].encode("ISO-8859-2")), value[1]]
        elif value is None:
            self._function = [None, None]
        elif callable(value):
            self._function = [value, getsource(value)]
        else:
            raise TypeError(
                "Expected function or list from a saved file, got: " + str(type(value))
            )

    # Function of the space to initiate the variable
    # Type : function
    function = property(
        fget=_get_function,
        fset=_set_function,
        doc=u"""Function of the space to initiate the variable""",
    )
