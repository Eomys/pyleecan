# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Mesh/SolutionFEMM.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import set_array, check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Solution import Solution

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Mesh.SolutionFEMM.get_field import get_field
except ImportError as error:
    get_field = error


from numpy import array, array_equal
from pyleecan.Classes._check import InitUnKnowClassError


class SolutionFEMM(Solution):
    """Gather the electromagnetic solution from FEMM (only 2D triangles)"""

    VERSION = 1

    # cf Methods.Mesh.SolutionFEMM.get_field
    if isinstance(get_field, ImportError):
        get_field = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SolutionFEMM method get_field: " + str(get_field)
                )
            )
        )
    else:
        get_field = get_field
    # save method is available in all object
    save = save

    def __init__(self, B=None, H=None, mu=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["B", "H", "mu"])
            # Overwrite default value with init_dict content
            if "B" in list(init_dict.keys()):
                B = init_dict["B"]
            if "H" in list(init_dict.keys()):
                H = init_dict["H"]
            if "mu" in list(init_dict.keys()):
                mu = init_dict["mu"]
        # Initialisation by argument
        # B can be None, a ndarray or a list
        set_array(self, "B", B)
        # H can be None, a ndarray or a list
        set_array(self, "H", H)
        # mu can be None, a ndarray or a list
        set_array(self, "mu", mu)
        # Call Solution init
        super(SolutionFEMM, self).__init__()
        # The class is frozen (in Solution init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SolutionFEMM_str = ""
        # Get the properties inherited from Solution
        SolutionFEMM_str += super(SolutionFEMM, self).__str__() + linesep
        SolutionFEMM_str += "B = " + linesep + str(self.B) + linesep + linesep
        SolutionFEMM_str += "H = " + linesep + str(self.H) + linesep + linesep
        SolutionFEMM_str += "mu = " + linesep + str(self.mu)
        return SolutionFEMM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Solution
        if not super(SolutionFEMM, self).__eq__(other):
            return False
        if not array_equal(other.B, self.B):
            return False
        if not array_equal(other.H, self.H):
            return False
        if not array_equal(other.mu, self.mu):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Solution
        SolutionFEMM_dict = super(SolutionFEMM, self).as_dict()
        if self.B is None:
            SolutionFEMM_dict["B"] = None
        else:
            SolutionFEMM_dict["B"] = self.B.tolist()
        if self.H is None:
            SolutionFEMM_dict["H"] = None
        else:
            SolutionFEMM_dict["H"] = self.H.tolist()
        if self.mu is None:
            SolutionFEMM_dict["mu"] = None
        else:
            SolutionFEMM_dict["mu"] = self.mu.tolist()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SolutionFEMM_dict["__class__"] = "SolutionFEMM"
        return SolutionFEMM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.B = None
        self.H = None
        self.mu = None
        # Set to None the properties inherited from Solution
        super(SolutionFEMM, self)._set_None()

    def _get_B(self):
        """getter of B"""
        return self._B

    def _set_B(self, value):
        """setter of B"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("B", value, "ndarray")
        self._B = value

    # Magnetic flux per element (Bx, By)
    # Type : ndarray
    B = property(
        fget=_get_B, fset=_set_B, doc=u"""Magnetic flux per element (Bx, By)"""
    )

    def _get_H(self):
        """getter of H"""
        return self._H

    def _set_H(self, value):
        """setter of H"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("H", value, "ndarray")
        self._H = value

    # Magnetic field per element (Hx, Hy)
    # Type : ndarray
    H = property(
        fget=_get_H, fset=_set_H, doc=u"""Magnetic field per element (Hx, Hy)"""
    )

    def _get_mu(self):
        """getter of mu"""
        return self._mu

    def _set_mu(self, value):
        """setter of mu"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("mu", value, "ndarray")
        self._mu = value

    # Pemreability per element
    # Type : ndarray
    mu = property(fget=_get_mu, fset=_set_mu, doc=u"""Pemreability per element""")
