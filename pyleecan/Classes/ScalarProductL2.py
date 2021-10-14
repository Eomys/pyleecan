# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/Interpolation/ScalarProductL2.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/ScalarProductL2
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
from .ScalarProduct import ScalarProduct

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.ScalarProductL2.scalar_product import scalar_product
except ImportError as error:
    scalar_product = error


from ._check import InitUnKnowClassError


class ScalarProductL2(ScalarProduct):
    """Store shape functions definition in the reference element"""

    VERSION = 1

    # cf Methods.Mesh.ScalarProductL2.scalar_product
    if isinstance(scalar_product, ImportError):
        scalar_product = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ScalarProductL2 method scalar_product: "
                    + str(scalar_product)
                )
            )
        )
    else:
        scalar_product = scalar_product
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, init_dict=None, init_str=None):
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
        # Set the properties (value check and convertion are done in setter)
        # Call ScalarProduct init
        super(ScalarProductL2, self).__init__()
        # The class is frozen (in ScalarProduct init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ScalarProductL2_str = ""
        # Get the properties inherited from ScalarProduct
        ScalarProductL2_str += super(ScalarProductL2, self).__str__()
        return ScalarProductL2_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ScalarProduct
        if not super(ScalarProductL2, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from ScalarProduct
        diff_list.extend(super(ScalarProductL2, self).compare(other, name=name))
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from ScalarProduct
        S += super(ScalarProductL2, self).__sizeof__()
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

        # Get the properties inherited from ScalarProduct
        ScalarProductL2_dict = super(ScalarProductL2, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ScalarProductL2_dict["__class__"] = "ScalarProductL2"
        return ScalarProductL2_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from ScalarProduct
        super(ScalarProductL2, self)._set_None()
