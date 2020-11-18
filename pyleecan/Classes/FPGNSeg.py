# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/Interpolation/FPGNSeg.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/FPGNSeg
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .GaussPoint import GaussPoint

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.FPGNSeg.get_gauss_points import get_gauss_points
except ImportError as error:
    get_gauss_points = error


from ._check import InitUnKnowClassError


class FPGNSeg(GaussPoint):
    """Compute N gauss point for segment elements"""

    VERSION = 1

    # cf Methods.Mesh.FPGNSeg.get_gauss_points
    if isinstance(get_gauss_points, ImportError):
        get_gauss_points = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use FPGNSeg method get_gauss_points: " + str(get_gauss_points)
                )
            )
        )
    else:
        get_gauss_points = get_gauss_points
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, nb_gauss_point=4, init_dict = None, init_str = None):
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
            if "nb_gauss_point" in list(init_dict.keys()):
                nb_gauss_point = init_dict["nb_gauss_point"]
        # Set the properties (value check and convertion are done in setter)
        self.nb_gauss_point = nb_gauss_point
        # Call GaussPoint init
        super(FPGNSeg, self).__init__()
        # The class is frozen (in GaussPoint init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        FPGNSeg_str = ""
        # Get the properties inherited from GaussPoint
        FPGNSeg_str += super(FPGNSeg, self).__str__()
        FPGNSeg_str += "nb_gauss_point = " + str(self.nb_gauss_point) + linesep
        return FPGNSeg_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from GaussPoint
        if not super(FPGNSeg, self).__eq__(other):
            return False
        if other.nb_gauss_point != self.nb_gauss_point:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from GaussPoint
        FPGNSeg_dict = super(FPGNSeg, self).as_dict()
        FPGNSeg_dict["nb_gauss_point"] = self.nb_gauss_point
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        FPGNSeg_dict["__class__"] = "FPGNSeg"
        return FPGNSeg_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.nb_gauss_point = None
        # Set to None the properties inherited from GaussPoint
        super(FPGNSeg, self)._set_None()

    def _get_nb_gauss_point(self):
        """getter of nb_gauss_point"""
        return self._nb_gauss_point

    def _set_nb_gauss_point(self, value):
        """setter of nb_gauss_point"""
        check_var("nb_gauss_point", value, "int")
        self._nb_gauss_point = value

    nb_gauss_point = property(
        fget=_get_nb_gauss_point,
        fset=_set_nb_gauss_point,
        doc=u"""Nb of gauss point to be used

        :Type: int
        """,
    )
