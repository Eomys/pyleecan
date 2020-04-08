# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Machine/BoreFlower.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ..Classes._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Classes.Bore import Bore

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.BoreFlower.get_bore_line import get_bore_line
except ImportError as error:
    get_bore_line = error


from ..Classes._check import InitUnKnowClassError


class BoreFlower(Bore):
    """Class for Bore flower shape"""

    VERSION = 1

    # cf Methods.Machine.BoreFlower.get_bore_line
    if isinstance(get_bore_line, ImportError):
        get_bore_line = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use BoreFlower method get_bore_line: " + str(get_bore_line)
                )
            )
        )
    else:
        get_bore_line = get_bore_line
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, N=8, Rarc=0.01, alpha=0, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "N" in list(init_dict.keys()):
                N = init_dict["N"]
            if "Rarc" in list(init_dict.keys()):
                Rarc = init_dict["Rarc"]
            if "alpha" in list(init_dict.keys()):
                alpha = init_dict["alpha"]
        # Initialisation by argument
        self.N = N
        self.Rarc = Rarc
        self.alpha = alpha
        # Call Bore init
        super(BoreFlower, self).__init__()
        # The class is frozen (in Bore init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        BoreFlower_str = ""
        # Get the properties inherited from Bore
        BoreFlower_str += super(BoreFlower, self).__str__()
        BoreFlower_str += "N = " + str(self.N) + linesep
        BoreFlower_str += "Rarc = " + str(self.Rarc) + linesep
        BoreFlower_str += "alpha = " + str(self.alpha) + linesep
        return BoreFlower_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Bore
        if not super(BoreFlower, self).__eq__(other):
            return False
        if other.N != self.N:
            return False
        if other.Rarc != self.Rarc:
            return False
        if other.alpha != self.alpha:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Bore
        BoreFlower_dict = super(BoreFlower, self).as_dict()
        BoreFlower_dict["N"] = self.N
        BoreFlower_dict["Rarc"] = self.Rarc
        BoreFlower_dict["alpha"] = self.alpha
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        BoreFlower_dict["__class__"] = "BoreFlower"
        return BoreFlower_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.N = None
        self.Rarc = None
        self.alpha = None
        # Set to None the properties inherited from Bore
        super(BoreFlower, self)._set_None()

    def _get_N(self):
        """getter of N"""
        return self._N

    def _set_N(self, value):
        """setter of N"""
        check_var("N", value, "int", Vmin=0)
        self._N = value

    # Number of flower arc
    # Type : int, min = 0
    N = property(fget=_get_N, fset=_set_N, doc=u"""Number of flower arc""")

    def _get_Rarc(self):
        """getter of Rarc"""
        return self._Rarc

    def _set_Rarc(self, value):
        """setter of Rarc"""
        check_var("Rarc", value, "float", Vmin=0)
        self._Rarc = value

    # Radius of the flower arc
    # Type : float, min = 0
    Rarc = property(fget=_get_Rarc, fset=_set_Rarc, doc=u"""Radius of the flower arc""")

    def _get_alpha(self):
        """getter of alpha"""
        return self._alpha

    def _set_alpha(self, value):
        """setter of alpha"""
        check_var("alpha", value, "float")
        self._alpha = value

    # Angular offset for the arc
    # Type : float
    alpha = property(
        fget=_get_alpha, fset=_set_alpha, doc=u"""Angular offset for the arc"""
    )
