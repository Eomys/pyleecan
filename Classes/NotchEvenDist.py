# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Machine/NotchEvenDist.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import set_array, check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Notch import Notch

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.NotchEvenDist.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error


from numpy import array, array_equal
from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.Slot import Slot


class NotchEvenDist(Notch):
    """Class for evenly distributed notches"""

    VERSION = 1

    # cf Methods.Machine.NotchEvenDist.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use NotchEvenDist method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # save method is available in all object
    save = save

    def __init__(self, alpha=None, notch_shape=list(), init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["alpha", "notch_shape"])
            # Overwrite default value with init_dict content
            if "alpha" in list(init_dict.keys()):
                alpha = init_dict["alpha"]
            if "notch_shape" in list(init_dict.keys()):
                notch_shape = init_dict["notch_shape"]
        # Initialisation by argument
        # alpha can be None, a ndarray or a list
        set_array(self, "alpha", alpha)
        # Call Notch init
        super(NotchEvenDist, self).__init__(notch_shape=notch_shape)
        # The class is frozen (in Notch init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        NotchEvenDist_str = ""
        # Get the properties inherited from Notch
        NotchEvenDist_str += super(NotchEvenDist, self).__str__()
        NotchEvenDist_str += (
            "alpha = "
            + linesep
            + str(self.alpha).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return NotchEvenDist_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Notch
        if not super(NotchEvenDist, self).__eq__(other):
            return False
        if not array_equal(other.alpha, self.alpha):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Notch
        NotchEvenDist_dict = super(NotchEvenDist, self).as_dict()
        if self.alpha is None:
            NotchEvenDist_dict["alpha"] = None
        else:
            NotchEvenDist_dict["alpha"] = self.alpha.tolist()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        NotchEvenDist_dict["__class__"] = "NotchEvenDist"
        return NotchEvenDist_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.alpha = None
        # Set to None the properties inherited from Notch
        super(NotchEvenDist, self)._set_None()

    def _get_alpha(self):
        """getter of alpha"""
        return self._alpha

    def _set_alpha(self, value):
        """setter of alpha"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("alpha", value, "ndarray")
        self._alpha = value

    # angular positon of the first notch
    # Type : ndarray
    alpha = property(
        fget=_get_alpha, fset=_set_alpha, doc=u"""angular positon of the first notch"""
    )
