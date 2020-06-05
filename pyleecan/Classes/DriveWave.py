# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/DriveWave.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.DriveWave.get_wave import get_wave
except ImportError as error:
    get_wave = error


from ._check import InitUnKnowClassError
from .Import import Import


class DriveWave(FrozenClass):
    """Drive to generate a wave according to an Import object"""

    VERSION = 1

    # cf Methods.Simulation.DriveWave.get_wave
    if isinstance(get_wave, ImportError):
        get_wave = property(
            fget=lambda x: raise_(
                ImportError("Can't use DriveWave method get_wave: " + str(get_wave))
            )
        )
    else:
        get_wave = get_wave
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, wave=-1, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if wave == -1:
            wave = Import()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            wave = obj.wave
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "wave" in list(init_dict.keys()):
                wave = init_dict["wave"]
        # Initialisation by argument
        self.parent = None
        # wave can be None, a Import object or a dict
        if isinstance(wave, dict):
            # Check that the type is correct (including daughter)
            class_name = wave.get("__class__")
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for wave"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.wave = class_obj(init_dict=wave)
        elif isinstance(wave, str):
            self.wave = Import(init_str=wave)
        else:
            self.wave = wave

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        DriveWave_str = ""
        if self.parent is None:
            DriveWave_str += "parent = None " + linesep
        else:
            DriveWave_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.wave is not None:
            tmp = self.wave.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            DriveWave_str += "wave = " + tmp
        else:
            DriveWave_str += "wave = None" + linesep + linesep
        return DriveWave_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.wave != self.wave:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        DriveWave_dict = dict()
        if self.wave is None:
            DriveWave_dict["wave"] = None
        else:
            DriveWave_dict["wave"] = self.wave.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        DriveWave_dict["__class__"] = "DriveWave"
        return DriveWave_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.wave is not None:
            self.wave._set_None()

    def _get_wave(self):
        """getter of wave"""
        return self._wave

    def _set_wave(self, value):
        """setter of wave"""
        check_var("wave", value, "Import")
        self._wave = value

        if self._wave is not None:
            self._wave.parent = self

    # Wave generator
    # Type : Import
    wave = property(fget=_get_wave, fset=_set_wave, doc=u"""Wave generator""")
