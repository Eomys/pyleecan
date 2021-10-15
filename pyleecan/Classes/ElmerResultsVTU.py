# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Elmer/ElmerResultsVTU.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Elmer/ElmerResultsVTU
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
    from ..Methods.Elmer.ElmerResultsVTU.build_meshsolution import build_meshsolution
except ImportError as error:
    build_meshsolution = error


from ._check import InitUnKnowClassError


class ElmerResultsVTU(Elmer):
    """Class to get Elmer simulation results from a VTU file"""

    VERSION = 1

    # cf Methods.Elmer.ElmerResultsVTU.build_meshsolution
    if isinstance(build_meshsolution, ImportError):
        build_meshsolution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ElmerResultsVTU method build_meshsolution: "
                    + str(build_meshsolution)
                )
            )
        )
    else:
        build_meshsolution = build_meshsolution
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        label="ElmerResults",
        file_path="",
        store_dict=-1,
        logger_name="Pyleecan.Elmer",
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
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
            if "file_path" in list(init_dict.keys()):
                file_path = init_dict["file_path"]
            if "store_dict" in list(init_dict.keys()):
                store_dict = init_dict["store_dict"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.label = label
        self.file_path = file_path
        self.store_dict = store_dict
        # Call Elmer init
        super(ElmerResultsVTU, self).__init__(logger_name=logger_name)
        # The class is frozen (in Elmer init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ElmerResultsVTU_str = ""
        # Get the properties inherited from Elmer
        ElmerResultsVTU_str += super(ElmerResultsVTU, self).__str__()
        ElmerResultsVTU_str += 'label = "' + str(self.label) + '"' + linesep
        ElmerResultsVTU_str += 'file_path = "' + str(self.file_path) + '"' + linesep
        ElmerResultsVTU_str += "store_dict = " + str(self.store_dict) + linesep
        return ElmerResultsVTU_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Elmer
        if not super(ElmerResultsVTU, self).__eq__(other):
            return False
        if other.label != self.label:
            return False
        if other.file_path != self.file_path:
            return False
        if other.store_dict != self.store_dict:
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
        diff_list.extend(super(ElmerResultsVTU, self).compare(other, name=name))
        if other._label != self._label:
            diff_list.append(name + ".label")
        if other._file_path != self._file_path:
            diff_list.append(name + ".file_path")
        if other._store_dict != self._store_dict:
            diff_list.append(name + ".store_dict")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Elmer
        S += super(ElmerResultsVTU, self).__sizeof__()
        S += getsizeof(self.label)
        S += getsizeof(self.file_path)
        if self.store_dict is not None:
            for key, value in self.store_dict.items():
                S += getsizeof(value) + getsizeof(key)
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
        ElmerResultsVTU_dict = super(ElmerResultsVTU, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        ElmerResultsVTU_dict["label"] = self.label
        ElmerResultsVTU_dict["file_path"] = self.file_path
        ElmerResultsVTU_dict["store_dict"] = (
            self.store_dict.copy() if self.store_dict is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ElmerResultsVTU_dict["__class__"] = "ElmerResultsVTU"
        return ElmerResultsVTU_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.label = None
        self.file_path = None
        self.store_dict = None
        # Set to None the properties inherited from Elmer
        super(ElmerResultsVTU, self)._set_None()

    def _get_label(self):
        """getter of label"""
        return self._label

    def _set_label(self, value):
        """setter of label"""
        check_var("label", value, "str")
        self._label = value

    label = property(
        fget=_get_label,
        fset=_set_label,
        doc=u"""Label of the resulting meshsolution

        :Type: str
        """,
    )

    def _get_file_path(self):
        """getter of file_path"""
        return self._file_path

    def _set_file_path(self, value):
        """setter of file_path"""
        check_var("file_path", value, "str")
        self._file_path = value

    file_path = property(
        fget=_get_file_path,
        fset=_set_file_path,
        doc=u"""Filename of the results VTU data file

        :Type: str
        """,
    )

    def _get_store_dict(self):
        """getter of store_dict"""
        return self._store_dict

    def _set_store_dict(self, value):
        """setter of store_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("store_dict", value, "dict")
        self._store_dict = value

    store_dict = property(
        fget=_get_store_dict,
        fset=_set_store_dict,
        doc=u"""Dict containing the data names to store

        :Type: dict
        """,
    )
