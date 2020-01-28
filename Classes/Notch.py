# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Machine/Notch.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
import numpy
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.Notch.get_Rbo import get_Rbo
except ImportError as error:
    get_Rbo = error

try:
    from pyleecan.Methods.Machine.Notch.is_outwards import is_outwards
except ImportError as error:
    is_outwards = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.Slot import Slot


class Notch(FrozenClass):
    """Abstract class for notches"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Notch.get_Rbo
    if isinstance(get_Rbo, ImportError):
        get_Rbo = property(
            fget=lambda x: raise_(
                ImportError("Can't use Notch method get_Rbo: " + str(get_Rbo))
            )
        )
    else:
        get_Rbo = get_Rbo
    # cf Methods.Machine.Notch.is_outwards
    if isinstance(is_outwards, ImportError):
        is_outwards = property(
            fget=lambda x: raise_(
                ImportError("Can't use Notch method is_outwards: " + str(is_outwards))
            )
        )
    else:
        is_outwards = is_outwards
    # save method is available in all object
    save = save

    def __init__(self, notch_shape=list(), init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["notch_shape"])
            # Overwrite default value with init_dict content
            if "notch_shape" in list(init_dict.keys()):
                notch_shape = init_dict["notch_shape"]
        # Initialisation by argument
        self.parent = None
        # notch_shape can be None or a list of Slot object
        self.notch_shape = list()
        if type(notch_shape) is list:
            for obj in notch_shape:
                if obj is None:  # Default value
                    self.notch_shape.append(Slot())
                elif isinstance(obj, dict):
                    # Check that the type is correct (including daughter)
                    class_name = obj.get("__class__")
                    if class_name not in [
                        "Slot",
                        "Slot19",
                        "SlotMFlat",
                        "SlotMPolar",
                        "SlotMag",
                        "SlotUD",
                        "SlotW10",
                        "SlotW11",
                        "SlotW12",
                        "SlotW13",
                        "SlotW14",
                        "SlotW15",
                        "SlotW16",
                        "SlotW21",
                        "SlotW22",
                        "SlotW23",
                        "SlotW24",
                        "SlotW25",
                        "SlotW26",
                        "SlotW27",
                        "SlotW28",
                        "SlotW29",
                        "SlotW60",
                        "SlotW61",
                        "SlotWind",
                    ]:
                        raise InitUnKnowClassError(
                            "Unknow class name "
                            + class_name
                            + " in init_dict for notch_shape"
                        )
                    # Dynamic import to call the correct constructor
                    module = __import__(
                        "pyleecan.Classes." + class_name, fromlist=[class_name]
                    )
                    class_obj = getattr(module, class_name)
                    self.notch_shape.append(class_obj(init_dict=obj))
                else:
                    self.notch_shape.append(obj)
        elif notch_shape is None:
            self.notch_shape = list()
        else:
            self.notch_shape = notch_shape

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Notch_str = ""
        if self.parent is None:
            Notch_str += "parent = None " + linesep
        else:
            Notch_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if len(self.notch_shape) == 0:
            Notch_str += "notch_shape = []"
        for ii in range(len(self.notch_shape)):
            Notch_str += (
                "notch_shape["
                + str(ii)
                + "] = "
                + str(self.notch_shape[ii].as_dict())
                + "\n"
            )
        return Notch_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.notch_shape != self.notch_shape:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Notch_dict = dict()
        Notch_dict["notch_shape"] = list()
        for obj in self.notch_shape:
            Notch_dict["notch_shape"].append(obj.as_dict())
        # The class name is added to the dict fordeserialisation purpose
        Notch_dict["__class__"] = "Notch"
        return Notch_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.notch_shape:
            obj._set_None()

    def _get_notch_shape(self):
        """getter of notch_shape"""
        for obj in self._notch_shape:
            if obj is not None:
                obj.parent = self
        return self._notch_shape

    def _set_notch_shape(self, value):
        """setter of notch_shape"""
        check_var("notch_shape", value, "[Slot]")
        self._notch_shape = value

        for obj in self._notch_shape:
            if obj is not None:
                obj.parent = self

    # Shape of Notch
    # Type : [Slot]
    notch_shape = property(
        fget=_get_notch_shape, fset=_set_notch_shape, doc=u"""Shape of Notch"""
    )
