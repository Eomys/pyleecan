# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/Interpolation/ScalarProductL2.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/ScalarProductL2
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
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
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, init_dict=None, init_str=None):
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
        # Set the properties (value check and convertion are done in setter)
        # Call ScalarProduct init
        super(ScalarProductL2, self).__init__()
        # The class is frozen (in ScalarProduct init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

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

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from ScalarProduct
        ScalarProductL2_dict = super(ScalarProductL2, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ScalarProductL2_dict["__class__"] = "ScalarProductL2"
        return ScalarProductL2_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from ScalarProduct
        super(ScalarProductL2, self)._set_None()
