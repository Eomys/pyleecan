# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Elmer/SolverInputFile.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Elmer/SolverInputFile
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
from .Elmer import Elmer

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Elmer.SolverInputFile.write import write
except ImportError as error:
    write = error


from ._check import InitUnKnowClassError


class SolverInputFile(Elmer):
    """Class to setup the Elmer Solver Input File"""

    VERSION = 1

    # cf Methods.Elmer.SolverInputFile.write
    if isinstance(write, ImportError):
        write = property(
            fget=lambda x: raise_(
                ImportError("Can't use SolverInputFile method write: " + str(write))
            )
        )
    else:
        write = write
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, sections=-1, logger_name="Pyleecan.Elmer", init_dict=None, init_str=None
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
            if "sections" in list(init_dict.keys()):
                sections = init_dict["sections"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.sections = sections
        # Call Elmer init
        super(SolverInputFile, self).__init__(logger_name=logger_name)
        # The class is frozen (in Elmer init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SolverInputFile_str = ""
        # Get the properties inherited from Elmer
        SolverInputFile_str += super(SolverInputFile, self).__str__()
        SolverInputFile_str += (
            "sections = "
            + linesep
            + str(self.sections).replace(linesep, linesep + "\t")
            + linesep
        )
        return SolverInputFile_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Elmer
        if not super(SolverInputFile, self).__eq__(other):
            return False
        if other.sections != self.sections:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Elmer
        diff_list.extend(super(SolverInputFile, self).compare(other, name=name))
        if other._sections != self._sections:
            diff_list.append(name + ".sections")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Elmer
        S += super(SolverInputFile, self).__sizeof__()
        if self.sections is not None:
            for value in self.sections:
                S += getsizeof(value)
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

        # Get the properties inherited from Elmer
        SolverInputFile_dict = super(SolverInputFile, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        SolverInputFile_dict["sections"] = (
            self.sections.copy() if self.sections is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SolverInputFile_dict["__class__"] = "SolverInputFile"
        return SolverInputFile_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.sections = None
        # Set to None the properties inherited from Elmer
        super(SolverInputFile, self)._set_None()

    def _get_sections(self):
        """getter of sections"""
        return self._sections

    def _set_sections(self, value):
        """setter of sections"""
        if type(value) is int and value == -1:
            value = list()
        check_var("sections", value, "list")
        self._sections = value

    sections = property(
        fget=_get_sections,
        fset=_set_sections,
        doc=u"""List of SIF sections

        :Type: list
        """,
    )
