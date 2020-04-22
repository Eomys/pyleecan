# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/InputFlux.csv
WARNING! All changes made in this file will be lost!
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

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, time=None, angle=None, Br=None, Bt=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if time == -1:
            time = Import()
        if angle == -1:
            angle = Import()
        if Br == -1:
            Br = Import()
        if Bt == -1:
            Bt = Import()
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Br" in list(init_dict.keys()):
                Br = init_dict["Br"]
            if "Bt" in list(init_dict.keys()):
                Bt = init_dict["Bt"]
        # Initialisation by argument
        # time can be None, a Import object or a dict
        if isinstance(time, dict):
            # Check that the type is correct (including daughter)
            class_name = time.get("__class__")
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for time"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.time = class_obj(init_dict=time)
        else:
            self.time = time
        # angle can be None, a Import object or a dict
        if isinstance(angle, dict):
            # Check that the type is correct (including daughter)
            class_name = angle.get("__class__")
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for angle"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.angle = class_obj(init_dict=angle)
        else:
            self.angle = angle
        # Br can be None, a Import object or a dict
        if isinstance(Br, dict):
            # Check that the type is correct (including daughter)
            class_name = Br.get("__class__")
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for Br"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.Br = class_obj(init_dict=Br)
        else:
            self.Br = Br
        # Bt can be None, a Import object or a dict
        if isinstance(Bt, dict):
            # Check that the type is correct (including daughter)
            class_name = Bt.get("__class__")
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for Bt"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.Bt = class_obj(init_dict=Bt)
        else:
            self.Bt = Bt
        # Call Input init
        super(InputFlux, self).__init__()
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        InputFlux_str = ""
        # Get the properties inherited from Input
        InputFlux_str += super(InputFlux, self).__str__()
        if self.time is not None:
            tmp = self.time.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputFlux_str += "time = " + tmp
        else:
            InputFlux_str += "time = None" + linesep + linesep
        if self.angle is not None:
            tmp = self.angle.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputFlux_str += "angle = " + tmp
        else:
            InputFlux_str += "angle = None" + linesep + linesep
        if self.Br is not None:
            tmp = self.Br.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputFlux_str += "Br = " + tmp
        else:
            InputFlux_str += "Br = None" + linesep + linesep
        if self.Bt is not None:
            tmp = self.Bt.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputFlux_str += "Bt = " + tmp
        else:
            InputFlux_str += "Bt = None" + linesep + linesep
        return InputFlux_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InputFlux, self).__eq__(other):
            return False
        if other.time != self.time:
            return False
        if other.angle != self.angle:
            return False
        if other.Br != self.Br:
            return False
        if other.Bt != self.Bt:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Input
        InputFlux_dict = super(InputFlux, self).as_dict()
        if self.time is None:
            InputFlux_dict["time"] = None
        else:
            InputFlux_dict["time"] = self.time.as_dict()
        if self.angle is None:
            InputFlux_dict["angle"] = None
        else:
            InputFlux_dict["angle"] = self.angle.as_dict()
        if self.Br is None:
            InputFlux_dict["Br"] = None
        else:
            InputFlux_dict["Br"] = self.Br.as_dict()
        if self.Bt is None:
            InputFlux_dict["Bt"] = None
        else:
            InputFlux_dict["Bt"] = self.Bt.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        InputFlux_dict["__class__"] = "InputFlux"
        return InputFlux_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.time is not None:
            self.time._set_None()
        if self.angle is not None:
            self.angle._set_None()
        if self.Br is not None:
            self.Br._set_None()
        if self.Bt is not None:
            self.Bt._set_None()
        # Set to None the properties inherited from Input
        super(InputFlux, self)._set_None()

    def _get_time(self):
        """getter of time"""
        return self._time

    def _set_time(self, value):
        """setter of time"""
        check_var("time", value, "Import")
        self._time = value

        if self._time is not None:
            self._time.parent = self

    # Electrical time vector (no symmetry) to import
    # Type : Import
    time = property(
        fget=_get_time,
        fset=_set_time,
        doc=u"""Electrical time vector (no symmetry) to import""",
    )

    def _get_angle(self):
        """getter of angle"""
        return self._angle

    def _set_angle(self, value):
        """setter of angle"""
        check_var("angle", value, "Import")
        self._angle = value

        if self._angle is not None:
            self._angle.parent = self

    # Electrical position vector (no symmetry) to import
    # Type : Import
    angle = property(
        fget=_get_angle,
        fset=_set_angle,
        doc=u"""Electrical position vector (no symmetry) to import""",
    )

    def _get_Br(self):
        """getter of Br"""
        return self._Br

    def _set_Br(self, value):
        """setter of Br"""
        check_var("Br", value, "Import")
        self._Br = value

        if self._Br is not None:
            self._Br.parent = self

    # Radial airgap flux density
    # Type : Import
    Br = property(fget=_get_Br, fset=_set_Br, doc=u"""Radial airgap flux density""")

    def _get_Bt(self):
        """getter of Bt"""
        return self._Bt

    def _set_Bt(self, value):
        """setter of Bt"""
        check_var("Bt", value, "Import")
        self._Bt = value

        if self._Bt is not None:
            self._Bt.parent = self

    # Tangential airgap flux density
    # Type : Import
    Bt = property(fget=_get_Bt, fset=_set_Bt, doc=u"""Tangential airgap flux density""")
