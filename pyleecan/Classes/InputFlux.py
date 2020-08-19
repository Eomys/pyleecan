# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/InputFlux.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/InputFlux
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
    from ..Methods.Simulation.InputFlux.gen_input import gen_input
except ImportError as error:
    gen_input = error


from ._check import InitUnKnowClassError
from .ImportVectorField import ImportVectorField
from .Input import Input
from .Import import Import


class InputFlux(Input):
    """Input to skip the magnetic module and start with the structural one"""

    VERSION = 1

    # cf Methods.Simulation.InputFlux.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError("Can't use InputFlux method gen_input: " + str(gen_input))
            )
        )
    else:
        gen_input = gen_input
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        B=None,
        OP=None,
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

        if B == -1:
            B = ImportVectorField()
        if OP == -1:
            OP = Input()
        if time == -1:
            time = Import()
        if angle == -1:
            angle = Import()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            B = obj.B
            OP = obj.OP
            time = obj.time
            angle = obj.angle
            Nt_tot = obj.Nt_tot
            Nrev = obj.Nrev
            Na_tot = obj.Na_tot
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "B" in list(init_dict.keys()):
                B = init_dict["B"]
            if "OP" in list(init_dict.keys()):
                OP = init_dict["OP"]
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
        # B can be None, a ImportVectorField object or a dict
        if isinstance(B, dict):
            self.B = ImportVectorField(init_dict=B)
        elif isinstance(B, str):
            from ..Functions.load import load

            self.B = load(B)
        else:
            self.B = B
        # OP can be None, a Input object or a dict
        if isinstance(OP, dict):
            # Check that the type is correct (including daughter)
            class_name = OP.get("__class__")
            if class_name not in [
                "Input",
                "InputCurrent",
                "InputElec",
                "InputFlux",
                "InputForce",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for OP"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.OP = class_obj(init_dict=OP)
        elif isinstance(OP, str):
            from ..Functions.load import load

            OP = load(OP)
            # Check that the type is correct (including daughter)
            class_name = OP.__class__.__name__
            if class_name not in [
                "Input",
                "InputCurrent",
                "InputElec",
                "InputFlux",
                "InputForce",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for OP"
                )
            self.OP = OP
        else:
            self.OP = OP
        # Call Input init
        super(InputFlux, self).__init__(
            time=time, angle=angle, Nt_tot=Nt_tot, Nrev=Nrev, Na_tot=Na_tot
        )
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        InputFlux_str = ""
        # Get the properties inherited from Input
        InputFlux_str += super(InputFlux, self).__str__()
        if self.B is not None:
            tmp = self.B.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputFlux_str += "B = " + tmp
        else:
            InputFlux_str += "B = None" + linesep + linesep
        if self.OP is not None:
            tmp = self.OP.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputFlux_str += "OP = " + tmp
        else:
            InputFlux_str += "OP = None" + linesep + linesep
        return InputFlux_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InputFlux, self).__eq__(other):
            return False
        if other.B != self.B:
            return False
        if other.OP != self.OP:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Input
        InputFlux_dict = super(InputFlux, self).as_dict()
        if self.B is None:
            InputFlux_dict["B"] = None
        else:
            InputFlux_dict["B"] = self.B.as_dict()
        if self.OP is None:
            InputFlux_dict["OP"] = None
        else:
            InputFlux_dict["OP"] = self.OP.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        InputFlux_dict["__class__"] = "InputFlux"
        return InputFlux_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.B is not None:
            self.B._set_None()
        if self.OP is not None:
            self.OP._set_None()
        # Set to None the properties inherited from Input
        super(InputFlux, self)._set_None()

    def _get_B(self):
        """getter of B"""
        return self._B

    def _set_B(self, value):
        """setter of B"""
        check_var("B", value, "ImportVectorField")
        self._B = value

        if self._B is not None:
            self._B.parent = self

    B = property(
        fget=_get_B,
        fset=_set_B,
        doc=u"""Airgap flux density

        :Type: ImportVectorField
        """,
    )

    def _get_OP(self):
        """getter of OP"""
        return self._OP

    def _set_OP(self, value):
        """setter of OP"""
        check_var("OP", value, "Input")
        self._OP = value

        if self._OP is not None:
            self._OP.parent = self

    OP = property(
        fget=_get_OP,
        fset=_set_OP,
        doc=u"""InputCurrent to define Operating Point (not mandatory)

        :Type: Input
        """,
    )
