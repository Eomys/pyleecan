# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Post/PostFunction.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Post/PostFunction
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
from .Post import Post

from ntpath import basename
from os.path import isfile
from ._check import CheckTypeError
import numpy as np
import random
from ._check import InitUnKnowClassError


class PostFunction(Post):
    """Post-processing from a user-defined function"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, run=None, init_dict=None, init_str=None):
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
            if "run" in list(init_dict.keys()):
                run = init_dict["run"]
        # Set the properties (value check and convertion are done in setter)
        self.run = run
        # Call Post init
        super(PostFunction, self).__init__()
        # The class is frozen (in Post init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        PostFunction_str = ""
        # Get the properties inherited from Post
        PostFunction_str += super(PostFunction, self).__str__()
        if self._run_str is not None:
            PostFunction_str += "run = " + self._run_str + linesep
        elif self._run_func is not None:
            PostFunction_str += "run = " + str(self._run_func) + linesep
        else:
            PostFunction_str += "run = None" + linesep + linesep
        return PostFunction_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Post
        if not super(PostFunction, self).__eq__(other):
            return False
        if other._run_str != self._run_str:
            return False
        return True

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Post
        S += super(PostFunction, self).__sizeof__()
        S += getsizeof(self._run_str)
        return S

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from Post
        PostFunction_dict = super(PostFunction, self).as_dict()
        if self._run_str is not None:
            PostFunction_dict["run"] = self._run_str
        else:
            PostFunction_dict["run"] = None
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        PostFunction_dict["__class__"] = "PostFunction"
        return PostFunction_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.run = None
        # Set to None the properties inherited from Post
        super(PostFunction, self)._set_None()

    def _get_run(self):
        """getter of run"""
        return self._run_func

    def _set_run(self, value):
        """setter of run"""
        if value is None:
            self._run_str = None
            self._run_func = None
        elif isinstance(value, str) and "lambda" in value:
            self._run_str = value
            self._run_func = eval(value)
        elif isinstance(value, str) and isfile(value) and value[-3:] == ".py":
            self._run_str = value
            f = open(value, "r")
            exec(f.read(), globals())
            self._run_func = eval(basename(value[:-3]))
        elif callable(value):
            self._run_str = None
            self._run_func = value
        else:
            raise CheckTypeError(
                "For property run Expected function or str (path to python file or lambda), got: "
                + str(type(value))
            )

    run = property(
        fget=_get_run,
        fset=_set_run,
        doc=u"""Post-processing that takes an output in argument

        :Type: function
        """,
    )
