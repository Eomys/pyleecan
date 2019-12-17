# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Import/ImportGenVectSin.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.ImportMatrix import ImportMatrix

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Import.ImportGenVectSin.get_data import get_data
except ImportError as error:
    get_data = error


from pyleecan.Classes.check import InitUnKnowClassError


class ImportGenVectSin(ImportMatrix):
    """To generate a Sinus vector"""

    VERSION = 1

    # cf Methods.Import.ImportGenVectSin.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportGenVectSin method get_data: " + str(get_data)
                )
            )
        )
    else:
        get_data = get_data
    # save method is available in all object
    save = save

    def __init__(
        self, f=100, A=1, Phi=0, N=1024, Tf=1, is_transpose=False, init_dict=None
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["f", "A", "Phi", "N", "Tf", "is_transpose"])
            # Overwrite default value with init_dict content
            if "f" in list(init_dict.keys()):
                f = init_dict["f"]
            if "A" in list(init_dict.keys()):
                A = init_dict["A"]
            if "Phi" in list(init_dict.keys()):
                Phi = init_dict["Phi"]
            if "N" in list(init_dict.keys()):
                N = init_dict["N"]
            if "Tf" in list(init_dict.keys()):
                Tf = init_dict["Tf"]
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Initialisation by argument
        self.f = f
        self.A = A
        self.Phi = Phi
        self.N = N
        self.Tf = Tf
        # Call ImportMatrix init
        super(ImportGenVectSin, self).__init__(is_transpose=is_transpose)
        # The class is frozen (in ImportMatrix init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ImportGenVectSin_str = ""
        # Get the properties inherited from ImportMatrix
        ImportGenVectSin_str += super(ImportGenVectSin, self).__str__() + linesep
        ImportGenVectSin_str += "f = " + str(self.f) + linesep
        ImportGenVectSin_str += "A = " + str(self.A) + linesep
        ImportGenVectSin_str += "Phi = " + str(self.Phi) + linesep
        ImportGenVectSin_str += "N = " + str(self.N) + linesep
        ImportGenVectSin_str += "Tf = " + str(self.Tf)
        return ImportGenVectSin_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ImportMatrix
        if not super(ImportGenVectSin, self).__eq__(other):
            return False
        if other.f != self.f:
            return False
        if other.A != self.A:
            return False
        if other.Phi != self.Phi:
            return False
        if other.N != self.N:
            return False
        if other.Tf != self.Tf:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from ImportMatrix
        ImportGenVectSin_dict = super(ImportGenVectSin, self).as_dict()
        ImportGenVectSin_dict["f"] = self.f
        ImportGenVectSin_dict["A"] = self.A
        ImportGenVectSin_dict["Phi"] = self.Phi
        ImportGenVectSin_dict["N"] = self.N
        ImportGenVectSin_dict["Tf"] = self.Tf
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ImportGenVectSin_dict["__class__"] = "ImportGenVectSin"
        return ImportGenVectSin_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.f = None
        self.A = None
        self.Phi = None
        self.N = None
        self.Tf = None
        # Set to None the properties inherited from ImportMatrix
        super(ImportGenVectSin, self)._set_None()

    def _get_f(self):
        """getter of f"""
        return self._f

    def _set_f(self, value):
        """setter of f"""
        check_var("f", value, "float", Vmin=0)
        self._f = value

    # Frequency of the sinus to generate
    # Type : float, min = 0
    f = property(
        fget=_get_f, fset=_set_f, doc=u"""Frequency of the sinus to generate"""
    )

    def _get_A(self):
        """getter of A"""
        return self._A

    def _set_A(self, value):
        """setter of A"""
        check_var("A", value, "float")
        self._A = value

    # Amplitude of the sinus to generate
    # Type : float
    A = property(
        fget=_get_A, fset=_set_A, doc=u"""Amplitude of the sinus to generate"""
    )

    def _get_Phi(self):
        """getter of Phi"""
        return self._Phi

    def _set_Phi(self, value):
        """setter of Phi"""
        check_var("Phi", value, "float", Vmin=-6.29, Vmax=6.29)
        self._Phi = value

    # Phase of the sinus to generate
    # Type : float, min = -6.29, max = 6.29
    Phi = property(
        fget=_get_Phi, fset=_set_Phi, doc=u"""Phase of the sinus to generate"""
    )

    def _get_N(self):
        """getter of N"""
        return self._N

    def _set_N(self, value):
        """setter of N"""
        check_var("N", value, "int", Vmin=0)
        self._N = value

    # Length of the vector to generate
    # Type : int, min = 0
    N = property(fget=_get_N, fset=_set_N, doc=u"""Length of the vector to generate""")

    def _get_Tf(self):
        """getter of Tf"""
        return self._Tf

    def _set_Tf(self, value):
        """setter of Tf"""
        check_var("Tf", value, "float", Vmin=0)
        self._Tf = value

    # End time of the sinus generation
    # Type : float, min = 0
    Tf = property(
        fget=_get_Tf, fset=_set_Tf, doc=u"""End time of the sinus generation"""
    )
