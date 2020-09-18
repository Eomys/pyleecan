# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/NotchEvenDist.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/NotchEvenDist
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Notch import Notch

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.NotchEvenDist.get_notch_list import get_notch_list
except ImportError as error:
    get_notch_list = error


from ._check import InitUnKnowClassError
from .Slot import Slot


class NotchEvenDist(Notch):
    """Class for evenly distributed notches (according to Zs)"""

    VERSION = 1

    # cf Methods.Machine.NotchEvenDist.get_notch_list
    if isinstance(get_notch_list, ImportError):
        get_notch_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use NotchEvenDist method get_notch_list: "
                    + str(get_notch_list)
                )
            )
        )
    else:
        get_notch_list = get_notch_list
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, alpha=0, notch_shape=-1, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if notch_shape == -1:
            notch_shape = Slot()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            alpha = obj.alpha
            notch_shape = obj.notch_shape
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "alpha" in list(init_dict.keys()):
                alpha = init_dict["alpha"]
            if "notch_shape" in list(init_dict.keys()):
                notch_shape = init_dict["notch_shape"]
        # Initialisation by argument
        self.alpha = alpha
        # notch_shape can be None, a Slot object or a dict
        if isinstance(notch_shape, dict):
            # Check that the type is correct (including daughter)
            class_name = notch_shape.get("__class__")
            if class_name not in [
                "Slot",
                "Slot19",
                "SlotCirc",
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
                    "Unknow class name " + class_name + " in init_dict for notch_shape"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.notch_shape = class_obj(init_dict=notch_shape)
        elif isinstance(notch_shape, str):
            from ..Functions.load import load

            notch_shape = load(notch_shape)
            # Check that the type is correct (including daughter)
            class_name = notch_shape.__class__.__name__
            if class_name not in [
                "Slot",
                "Slot19",
                "SlotCirc",
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
                    "Unknow class name " + class_name + " in init_dict for notch_shape"
                )
            self.notch_shape = notch_shape
        else:
            self.notch_shape = notch_shape
        # Call Notch init
        super(NotchEvenDist, self).__init__()
        # The class is frozen (in Notch init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        NotchEvenDist_str = ""
        # Get the properties inherited from Notch
        NotchEvenDist_str += super(NotchEvenDist, self).__str__()
        NotchEvenDist_str += "alpha = " + str(self.alpha) + linesep
        if self.notch_shape is not None:
            tmp = (
                self.notch_shape.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            NotchEvenDist_str += "notch_shape = " + tmp
        else:
            NotchEvenDist_str += "notch_shape = None" + linesep + linesep
        return NotchEvenDist_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Notch
        if not super(NotchEvenDist, self).__eq__(other):
            return False
        if other.alpha != self.alpha:
            return False
        if other.notch_shape != self.notch_shape:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from Notch
        NotchEvenDist_dict = super(NotchEvenDist, self).as_dict()
        NotchEvenDist_dict["alpha"] = self.alpha
        if self.notch_shape is None:
            NotchEvenDist_dict["notch_shape"] = None
        else:
            NotchEvenDist_dict["notch_shape"] = self.notch_shape.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        NotchEvenDist_dict["__class__"] = "NotchEvenDist"
        return NotchEvenDist_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.alpha = None
        if self.notch_shape is not None:
            self.notch_shape._set_None()
        # Set to None the properties inherited from Notch
        super(NotchEvenDist, self)._set_None()

    def _get_alpha(self):
        """getter of alpha"""
        return self._alpha

    def _set_alpha(self, value):
        """setter of alpha"""
        check_var("alpha", value, "float")
        self._alpha = value

    alpha = property(
        fget=_get_alpha,
        fset=_set_alpha,
        doc=u"""angular positon of the first notch

        :Type: float
        """,
    )

    def _get_notch_shape(self):
        """getter of notch_shape"""
        return self._notch_shape

    def _set_notch_shape(self, value):
        """setter of notch_shape"""
        check_var("notch_shape", value, "Slot")
        self._notch_shape = value

        if self._notch_shape is not None:
            self._notch_shape.parent = self

    notch_shape = property(
        fget=_get_notch_shape,
        fset=_set_notch_shape,
        doc=u"""Shape of the Notch

        :Type: Slot
        """,
    )
