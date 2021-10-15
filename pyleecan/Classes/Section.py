# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Elmer/Section.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Elmer/Section
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
    from ..Methods.Elmer.Section.__delitem__ import __delitem__
except ImportError as error:
    __delitem__ = error

try:
    from ..Methods.Elmer.Section.__getitem__ import __getitem__
except ImportError as error:
    __getitem__ = error

try:
    from ..Methods.Elmer.Section.__iter__ import __iter__
except ImportError as error:
    __iter__ = error

try:
    from ..Methods.Elmer.Section.__len__ import __len__
except ImportError as error:
    __len__ = error

try:
    from ..Methods.Elmer.Section.__missing__ import __missing__
except ImportError as error:
    __missing__ = error

try:
    from ..Methods.Elmer.Section.__reversed__ import __reversed__
except ImportError as error:
    __reversed__ = error

try:
    from ..Methods.Elmer.Section.__setitem__ import __setitem__
except ImportError as error:
    __setitem__ = error

try:
    from ..Methods.Elmer.Section.pop import pop
except ImportError as error:
    pop = error

try:
    from ..Methods.Elmer.Section.keys import keys
except ImportError as error:
    keys = error

try:
    from ..Methods.Elmer.Section.write import write
except ImportError as error:
    write = error


from ._check import InitUnKnowClassError


class Section(Elmer):
    """Class to setup a section of an Elmer Solver Input File"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Elmer.Section.__delitem__
    if isinstance(__delitem__, ImportError):
        __delitem__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use Section method __delitem__: " + str(__delitem__))
            )
        )
    else:
        __delitem__ = __delitem__
    # cf Methods.Elmer.Section.__getitem__
    if isinstance(__getitem__, ImportError):
        __getitem__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use Section method __getitem__: " + str(__getitem__))
            )
        )
    else:
        __getitem__ = __getitem__
    # cf Methods.Elmer.Section.__iter__
    if isinstance(__iter__, ImportError):
        __iter__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use Section method __iter__: " + str(__iter__))
            )
        )
    else:
        __iter__ = __iter__
    # cf Methods.Elmer.Section.__len__
    if isinstance(__len__, ImportError):
        __len__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use Section method __len__: " + str(__len__))
            )
        )
    else:
        __len__ = __len__
    # cf Methods.Elmer.Section.__missing__
    if isinstance(__missing__, ImportError):
        __missing__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use Section method __missing__: " + str(__missing__))
            )
        )
    else:
        __missing__ = __missing__
    # cf Methods.Elmer.Section.__reversed__
    if isinstance(__reversed__, ImportError):
        __reversed__ = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Section method __reversed__: " + str(__reversed__)
                )
            )
        )
    else:
        __reversed__ = __reversed__
    # cf Methods.Elmer.Section.__setitem__
    if isinstance(__setitem__, ImportError):
        __setitem__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use Section method __setitem__: " + str(__setitem__))
            )
        )
    else:
        __setitem__ = __setitem__
    # cf Methods.Elmer.Section.pop
    if isinstance(pop, ImportError):
        pop = property(
            fget=lambda x: raise_(
                ImportError("Can't use Section method pop: " + str(pop))
            )
        )
    else:
        pop = pop
    # cf Methods.Elmer.Section.keys
    if isinstance(keys, ImportError):
        keys = property(
            fget=lambda x: raise_(
                ImportError("Can't use Section method keys: " + str(keys))
            )
        )
    else:
        keys = keys
    # cf Methods.Elmer.Section.write
    if isinstance(write, ImportError):
        write = property(
            fget=lambda x: raise_(
                ImportError("Can't use Section method write: " + str(write))
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
        self,
        section="",
        id=None,
        comment="",
        _statements=-1,
        _comments=-1,
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
            if "section" in list(init_dict.keys()):
                section = init_dict["section"]
            if "id" in list(init_dict.keys()):
                id = init_dict["id"]
            if "comment" in list(init_dict.keys()):
                comment = init_dict["comment"]
            if "_statements" in list(init_dict.keys()):
                _statements = init_dict["_statements"]
            if "_comments" in list(init_dict.keys()):
                _comments = init_dict["_comments"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.section = section
        self.id = id
        self.comment = comment
        self._statements = _statements
        self._comments = _comments
        # Call Elmer init
        super(Section, self).__init__(logger_name=logger_name)
        # The class is frozen (in Elmer init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Section_str = ""
        # Get the properties inherited from Elmer
        Section_str += super(Section, self).__str__()
        Section_str += 'section = "' + str(self.section) + '"' + linesep
        Section_str += "id = " + str(self.id) + linesep
        Section_str += 'comment = "' + str(self.comment) + '"' + linesep
        Section_str += "_statements = " + str(self._statements) + linesep
        Section_str += "_comments = " + str(self._comments) + linesep
        return Section_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Elmer
        if not super(Section, self).__eq__(other):
            return False
        if other.section != self.section:
            return False
        if other.id != self.id:
            return False
        if other.comment != self.comment:
            return False
        if other._statements != self._statements:
            return False
        if other._comments != self._comments:
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
        diff_list.extend(super(Section, self).compare(other, name=name))
        if other._section != self._section:
            diff_list.append(name + ".section")
        if other._id != self._id:
            diff_list.append(name + ".id")
        if other._comment != self._comment:
            diff_list.append(name + ".comment")
        if other.__statements != self.__statements:
            diff_list.append(name + "._statements")
        if other.__comments != self.__comments:
            diff_list.append(name + "._comments")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Elmer
        S += super(Section, self).__sizeof__()
        S += getsizeof(self.section)
        S += getsizeof(self.id)
        S += getsizeof(self.comment)
        if self._statements is not None:
            for key, value in self._statements.items():
                S += getsizeof(value) + getsizeof(key)
        if self._comments is not None:
            for key, value in self._comments.items():
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
        Section_dict = super(Section, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        Section_dict["section"] = self.section
        Section_dict["id"] = self.id
        Section_dict["comment"] = self.comment
        Section_dict["_statements"] = (
            self._statements.copy() if self._statements is not None else None
        )
        Section_dict["_comments"] = (
            self._comments.copy() if self._comments is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Section_dict["__class__"] = "Section"
        return Section_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.section = None
        self.id = None
        self.comment = None
        self._statements = None
        self._comments = None
        # Set to None the properties inherited from Elmer
        super(Section, self)._set_None()

    def _get_section(self):
        """getter of section"""
        return self._section

    def _set_section(self, value):
        """setter of section"""
        check_var("section", value, "str")
        self._section = value

    section = property(
        fget=_get_section,
        fset=_set_section,
        doc=u"""Name of the section

        :Type: str
        """,
    )

    def _get_id(self):
        """getter of id"""
        return self._id

    def _set_id(self, value):
        """setter of id"""
        check_var("id", value, "int")
        self._id = value

    id = property(
        fget=_get_id,
        fset=_set_id,
        doc=u"""Index of a numbered section

        :Type: int
        """,
    )

    def _get_comment(self):
        """getter of comment"""
        return self._comment

    def _set_comment(self, value):
        """setter of comment"""
        check_var("comment", value, "str")
        self._comment = value

    comment = property(
        fget=_get_comment,
        fset=_set_comment,
        doc=u"""Section global comment

        :Type: str
        """,
    )

    def _get__statements(self):
        """getter of _statements"""
        return self.__statements

    def _set__statements(self, value):
        """setter of _statements"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("_statements", value, "dict")
        self.__statements = value

    _statements = property(
        fget=_get__statements,
        fset=_set__statements,
        doc=u"""internal dict to store the sections statements

        :Type: dict
        """,
    )

    def _get__comments(self):
        """getter of _comments"""
        return self.__comments

    def _set__comments(self, value):
        """setter of _comments"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("_comments", value, "dict")
        self.__comments = value

    _comments = property(
        fget=_get__comments,
        fset=_set__comments,
        doc=u"""internal dict to store comments on single statements

        :Type: dict
        """,
    )
