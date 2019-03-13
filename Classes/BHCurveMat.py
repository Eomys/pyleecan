# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.BHCurve import BHCurve

from pyleecan.Methods.Material.BHCurveMat.comp_B import comp_B

from numpy import array
from pyleecan.Classes.check import InitUnKnowClassError


class BHCurveMat(BHCurve):
    """B(H) curve defined by a matrix"""

    VERSION = 1

    # cf Methods.Material.BHCurveMat.comp_B
    comp_B = comp_B
    # save method is available in all object
    save = save

    def __init__(self, matrix=None, f=None, H=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["matrix", "f", "H"])
            # Overwrite default value with init_dict content
            if "matrix" in list(init_dict.keys()):
                matrix = init_dict["matrix"]
            if "f" in list(init_dict.keys()):
                f = init_dict["f"]
            if "H" in list(init_dict.keys()):
                H = init_dict["H"]
        # Initialisation by argument
        # matrix can be None, a ndarray or a list
        set_array(self, "matrix", matrix)
        # f can be None, a ndarray or a list
        set_array(self, "f", f)
        # H can be None, a ndarray or a list
        set_array(self, "H", H)
        # Call BHCurve init
        super(BHCurveMat, self).__init__()
        # The class is frozen (in BHCurve init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        BHCurveMat_str = ""
        # Get the properties inherited from BHCurve
        BHCurveMat_str += super(BHCurveMat, self).__str__() + linesep
        BHCurveMat_str += "matrix = " + linesep + str(self.matrix) + linesep + linesep
        BHCurveMat_str += "f = " + linesep + str(self.f) + linesep + linesep
        BHCurveMat_str += "H = " + linesep + str(self.H)
        return BHCurveMat_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from BHCurve
        if not super(BHCurveMat, self).__eq__(other):
            return False
        if other.matrix != self.matrix:
            return False
        if other.f != self.f:
            return False
        if other.H != self.H:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from BHCurve
        BHCurveMat_dict = super(BHCurveMat, self).as_dict()
        if self.matrix is None:
            BHCurveMat_dict["matrix"] = None
        else:
            BHCurveMat_dict["matrix"] = self.matrix.tolist()
        if self.f is None:
            BHCurveMat_dict["f"] = None
        else:
            BHCurveMat_dict["f"] = self.f.tolist()
        if self.H is None:
            BHCurveMat_dict["H"] = None
        else:
            BHCurveMat_dict["H"] = self.H.tolist()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        BHCurveMat_dict["__class__"] = "BHCurveMat"
        return BHCurveMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.matrix = None
        self.f = None
        self.H = None
        # Set to None the properties inherited from BHCurve
        super(BHCurveMat, self)._set_None()

    def _get_matrix(self):
        """getter of matrix"""
        return self._matrix

    def _set_matrix(self, value):
        """setter of matrix"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("matrix", value, "ndarray")
        self._matrix = value

    # B(H) matrix value. Every column are B(H) value for a specify frequency
    # Type : ndarray
    matrix = property(
        fget=_get_matrix,
        fset=_set_matrix,
        doc=u"""B(H) matrix value. Every column are B(H) value for a specify frequency""",
    )

    def _get_f(self):
        """getter of f"""
        return self._f

    def _set_f(self, value):
        """setter of f"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("f", value, "ndarray")
        self._f = value

    # f value for each column of the matrix
    # Type : ndarray
    f = property(
        fget=_get_f, fset=_set_f, doc=u"""f value for each column of the matrix"""
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

    # H value for each row of the matrix
    # Type : ndarray
    H = property(
        fget=_get_H, fset=_set_H, doc=u"""H value for each row of the matrix"""
    )
