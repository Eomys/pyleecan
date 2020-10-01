# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/Interpolation/RefSegmentP1.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/RefSegmentP1
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .RefCell import RefCell

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.RefSegmentP1.shape_function import shape_function
except ImportError as error:
    shape_function = error

try:
    from ..Methods.Mesh.RefSegmentP1.jacobian import jacobian
except ImportError as error:
    jacobian = error

try:
    from ..Methods.Mesh.RefSegmentP1.grad_shape_function import grad_shape_function
except ImportError as error:
    grad_shape_function = error

try:
    from ..Methods.Mesh.RefSegmentP1.get_real_point import get_real_point
except ImportError as error:
    get_real_point = error

try:
    from ..Methods.Mesh.RefSegmentP1.get_ref_point import get_ref_point
except ImportError as error:
    get_ref_point = error


from ._check import InitUnKnowClassError


class RefSegmentP1(RefCell):
    """Store triangle elements for 2D mesh"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.RefSegmentP1.shape_function
    if isinstance(shape_function, ImportError):
        shape_function = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RefSegmentP1 method shape_function: "
                    + str(shape_function)
                )
            )
        )
    else:
        shape_function = shape_function
    # cf Methods.Mesh.RefSegmentP1.jacobian
    if isinstance(jacobian, ImportError):
        jacobian = property(
            fget=lambda x: raise_(
                ImportError("Can't use RefSegmentP1 method jacobian: " + str(jacobian))
            )
        )
    else:
        jacobian = jacobian
    # cf Methods.Mesh.RefSegmentP1.grad_shape_function
    if isinstance(grad_shape_function, ImportError):
        grad_shape_function = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RefSegmentP1 method grad_shape_function: "
                    + str(grad_shape_function)
                )
            )
        )
    else:
        grad_shape_function = grad_shape_function
    # cf Methods.Mesh.RefSegmentP1.get_real_point
    if isinstance(get_real_point, ImportError):
        get_real_point = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RefSegmentP1 method get_real_point: "
                    + str(get_real_point)
                )
            )
        )
    else:
        get_real_point = get_real_point
    # cf Methods.Mesh.RefSegmentP1.get_ref_point
    if isinstance(get_ref_point, ImportError):
        get_ref_point = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RefSegmentP1 method get_ref_point: " + str(get_ref_point)
                )
            )
        )
    else:
        get_ref_point = get_ref_point
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, epsilon=0.05, init_dict=None, init_str=None):
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
            if "epsilon" in list(init_dict.keys()):
                epsilon = init_dict["epsilon"]
        # Set the properties (value check and convertion are done in setter)
        # Call RefCell init
        super(RefSegmentP1, self).__init__(epsilon=epsilon)
        # The class is frozen (in RefCell init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        RefSegmentP1_str = ""
        # Get the properties inherited from RefCell
        RefSegmentP1_str += super(RefSegmentP1, self).__str__()
        return RefSegmentP1_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from RefCell
        if not super(RefSegmentP1, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from RefCell
        RefSegmentP1_dict = super(RefSegmentP1, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        RefSegmentP1_dict["__class__"] = "RefSegmentP1"
        return RefSegmentP1_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from RefCell
        super(RefSegmentP1, self)._set_None()
