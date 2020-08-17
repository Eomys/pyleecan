# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Electrical.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Electrical
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
    from ..Methods.Simulation.Electrical.run import run
except ImportError as error:
    run = error


from ._check import InitUnKnowClassError
from .EEC import EEC


class Electrical(FrozenClass):
    """Electric module abstract object"""

    VERSION = 1

    # cf Methods.Simulation.Electrical.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use Electrical method run: " + str(run))
            )
        )
    else:
        run = run
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, eec=None, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if eec == -1:
            eec = EEC()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            eec = obj.eec
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "eec" in list(init_dict.keys()):
                eec = init_dict["eec"]
        # Initialisation by argument
        self.parent = None
        # eec can be None, a EEC object or a dict
        if isinstance(eec, dict):
            # Check that the type is correct (including daughter)
            class_name = eec.get("__class__")
            if class_name not in ["EEC", "EEC_PMSM"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for eec"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.eec = class_obj(init_dict=eec)
        elif isinstance(eec, str):
            from ..Functions.load import load

            eec = load(eec)
            # Check that the type is correct (including daughter)
            class_name = eec.__class__.__name__
            if class_name not in ["EEC", "EEC_PMSM"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for eec"
                )
            self.eec = eec
        else:
            self.eec = eec

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Electrical_str = ""
        if self.parent is None:
            Electrical_str += "parent = None " + linesep
        else:
            Electrical_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.eec is not None:
            tmp = self.eec.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Electrical_str += "eec = " + tmp
        else:
            Electrical_str += "eec = None" + linesep + linesep
        return Electrical_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.eec != self.eec:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Electrical_dict = dict()
        if self.eec is None:
            Electrical_dict["eec"] = None
        else:
            Electrical_dict["eec"] = self.eec.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        Electrical_dict["__class__"] = "Electrical"
        return Electrical_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.eec is not None:
            self.eec._set_None()

    def _get_eec(self):
        """getter of eec"""
        return self._eec

    def _set_eec(self, value):
        """setter of eec"""
        check_var("eec", value, "EEC")
        self._eec = value

        if self._eec is not None:
            self._eec.parent = self

    eec = property(
        fget=_get_eec,
        fset=_set_eec,
        doc=u"""Electrical Equivalent Circuit

        :Type: EEC
        """,
    )
