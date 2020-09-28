# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/InputForce.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/InputForce
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Input import Input

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.InputForce.gen_input import gen_input
except ImportError as error:
    gen_input = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .ImportVectorField import ImportVectorField
from .ImportMatrix import ImportMatrix


class InputForce(Input):
    """Input to start with the structural one """

    VERSION = 1

    # cf Methods.Simulation.InputForce.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError("Can't use InputForce method gen_input: " + str(gen_input))
            )
        )
    else:
        gen_input = gen_input
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        P=None,
        time=None,
        angle=None,
        Nt_tot=2048,
        Nrev=1,
        Na_tot=2048,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if P == -1:
            P = ImportVectorField()
        if time == -1:
            time = ImportMatrix()
        if angle == -1:
            angle = ImportMatrix()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            P = obj.P
            time = obj.time
            angle = obj.angle
            Nt_tot = obj.Nt_tot
            Nrev = obj.Nrev
            Na_tot = obj.Na_tot
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "P" in list(init_dict.keys()):
                P = init_dict["P"]
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Nrev" in list(init_dict.keys()):
                Nrev = init_dict["Nrev"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
        # Initialisation by argument
        # P can be None, a ImportVectorField object or a dict
        if isinstance(P, dict):
            self.P = ImportVectorField(init_dict=P)
        elif isinstance(P, str):
            from ..Functions.load import load

            self.P = load(P)
        else:
            self.P = P
        # Call Input init
        super(InputForce, self).__init__(
            time=time, angle=angle, Nt_tot=Nt_tot, Nrev=Nrev, Na_tot=Na_tot
        )
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        InputForce_str = ""
        # Get the properties inherited from Input
        InputForce_str += super(InputForce, self).__str__()
        if self.P is not None:
            tmp = self.P.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputForce_str += "P = " + tmp
        else:
            InputForce_str += "P = None" + linesep + linesep
        return InputForce_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InputForce, self).__eq__(other):
            return False
        if other.P != self.P:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from Input
        InputForce_dict = super(InputForce, self).as_dict()
        if self.P is None:
            InputForce_dict["P"] = None
        else:
            InputForce_dict["P"] = self.P.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        InputForce_dict["__class__"] = "InputForce"
        return InputForce_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.P is not None:
            self.P._set_None()
        # Set to None the properties inherited from Input
        super(InputForce, self)._set_None()

    def _get_P(self):
        """getter of P"""
        return self._P

    def _set_P(self, value):
        """setter of P"""
        check_var("P", value, "ImportVectorField")
        self._P = value

        if self._P is not None:
            self._P.parent = self

    P = property(
        fget=_get_P,
        fset=_set_P,
        doc=u"""Magnetic air-gap surface force

        :Type: ImportVectorField
        """,
    )
