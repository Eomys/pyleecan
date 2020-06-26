# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/Loss1.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Loss import Loss

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Loss1.run import run
except ImportError as error:
    run = error


from ._check import InitUnKnowClassError
from .LossModel import LossModel


class Loss1(Loss):
    """Gather loss modules loss calculation models"""

    VERSION = 1

    # cf Methods.Simulation.Loss1.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use Loss1 method run: " + str(run))
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

    def __init__(
        self,
        lam_stator=None,
        lam_rotor=None,
        wind_stator=None,
        wind_rotor=None,
        mag_stator=None,
        mag_rotor=None,
        windage=None,
        bearing=None,
        shaft=None,
        frame=None,
        additional=None,
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

        if lam_stator == -1:
            lam_stator = LossModel()
        if lam_rotor == -1:
            lam_rotor = LossModel()
        if wind_stator == -1:
            wind_stator = LossModel()
        if wind_rotor == -1:
            wind_rotor = LossModel()
        if mag_stator == -1:
            mag_stator = LossModel()
        if mag_rotor == -1:
            mag_rotor = LossModel()
        if windage == -1:
            windage = LossModel()
        if bearing == -1:
            bearing = LossModel()
        if shaft == -1:
            shaft = LossModel()
        if frame == -1:
            frame = LossModel()
        if additional == -1:
            additional = LossModel()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            lam_stator = obj.lam_stator
            lam_rotor = obj.lam_rotor
            wind_stator = obj.wind_stator
            wind_rotor = obj.wind_rotor
            mag_stator = obj.mag_stator
            mag_rotor = obj.mag_rotor
            windage = obj.windage
            bearing = obj.bearing
            shaft = obj.shaft
            frame = obj.frame
            additional = obj.additional
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "lam_stator" in list(init_dict.keys()):
                lam_stator = init_dict["lam_stator"]
            if "lam_rotor" in list(init_dict.keys()):
                lam_rotor = init_dict["lam_rotor"]
            if "wind_stator" in list(init_dict.keys()):
                wind_stator = init_dict["wind_stator"]
            if "wind_rotor" in list(init_dict.keys()):
                wind_rotor = init_dict["wind_rotor"]
            if "mag_stator" in list(init_dict.keys()):
                mag_stator = init_dict["mag_stator"]
            if "mag_rotor" in list(init_dict.keys()):
                mag_rotor = init_dict["mag_rotor"]
            if "windage" in list(init_dict.keys()):
                windage = init_dict["windage"]
            if "bearing" in list(init_dict.keys()):
                bearing = init_dict["bearing"]
            if "shaft" in list(init_dict.keys()):
                shaft = init_dict["shaft"]
            if "frame" in list(init_dict.keys()):
                frame = init_dict["frame"]
            if "additional" in list(init_dict.keys()):
                additional = init_dict["additional"]
        # Initialisation by argument
        # lam_stator can be None, a LossModel object or a dict
        if isinstance(lam_stator, dict):
            self.lam_stator = LossModel(init_dict=lam_stator)
        elif isinstance(lam_stator, str):
            from ..Functions.load import load

            self.lam_stator = load(lam_stator)
        else:
            self.lam_stator = lam_stator
        # lam_rotor can be None, a LossModel object or a dict
        if isinstance(lam_rotor, dict):
            self.lam_rotor = LossModel(init_dict=lam_rotor)
        elif isinstance(lam_rotor, str):
            from ..Functions.load import load

            self.lam_rotor = load(lam_rotor)
        else:
            self.lam_rotor = lam_rotor
        # wind_stator can be None, a LossModel object or a dict
        if isinstance(wind_stator, dict):
            self.wind_stator = LossModel(init_dict=wind_stator)
        elif isinstance(wind_stator, str):
            from ..Functions.load import load

            self.wind_stator = load(wind_stator)
        else:
            self.wind_stator = wind_stator
        # wind_rotor can be None, a LossModel object or a dict
        if isinstance(wind_rotor, dict):
            self.wind_rotor = LossModel(init_dict=wind_rotor)
        elif isinstance(wind_rotor, str):
            from ..Functions.load import load

            self.wind_rotor = load(wind_rotor)
        else:
            self.wind_rotor = wind_rotor
        # mag_stator can be None, a LossModel object or a dict
        if isinstance(mag_stator, dict):
            self.mag_stator = LossModel(init_dict=mag_stator)
        elif isinstance(mag_stator, str):
            from ..Functions.load import load

            self.mag_stator = load(mag_stator)
        else:
            self.mag_stator = mag_stator
        # mag_rotor can be None, a LossModel object or a dict
        if isinstance(mag_rotor, dict):
            self.mag_rotor = LossModel(init_dict=mag_rotor)
        elif isinstance(mag_rotor, str):
            from ..Functions.load import load

            self.mag_rotor = load(mag_rotor)
        else:
            self.mag_rotor = mag_rotor
        # windage can be None, a LossModel object or a dict
        if isinstance(windage, dict):
            self.windage = LossModel(init_dict=windage)
        elif isinstance(windage, str):
            from ..Functions.load import load

            self.windage = load(windage)
        else:
            self.windage = windage
        # bearing can be None, a LossModel object or a dict
        if isinstance(bearing, dict):
            self.bearing = LossModel(init_dict=bearing)
        elif isinstance(bearing, str):
            from ..Functions.load import load

            self.bearing = load(bearing)
        else:
            self.bearing = bearing
        # shaft can be None, a LossModel object or a dict
        if isinstance(shaft, dict):
            self.shaft = LossModel(init_dict=shaft)
        elif isinstance(shaft, str):
            from ..Functions.load import load

            self.shaft = load(shaft)
        else:
            self.shaft = shaft
        # frame can be None, a LossModel object or a dict
        if isinstance(frame, dict):
            self.frame = LossModel(init_dict=frame)
        elif isinstance(frame, str):
            from ..Functions.load import load

            self.frame = load(frame)
        else:
            self.frame = frame
        # additional can be None, a LossModel object or a dict
        if isinstance(additional, dict):
            self.additional = LossModel(init_dict=additional)
        elif isinstance(additional, str):
            from ..Functions.load import load

            self.additional = load(additional)
        else:
            self.additional = additional
        # Call Loss init
        super(Loss1, self).__init__()
        # The class is frozen (in Loss init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Loss1_str = ""
        # Get the properties inherited from Loss
        Loss1_str += super(Loss1, self).__str__()
        if self.lam_stator is not None:
            tmp = (
                self.lam_stator.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            Loss1_str += "lam_stator = " + tmp
        else:
            Loss1_str += "lam_stator = None" + linesep + linesep
        if self.lam_rotor is not None:
            tmp = self.lam_rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Loss1_str += "lam_rotor = " + tmp
        else:
            Loss1_str += "lam_rotor = None" + linesep + linesep
        if self.wind_stator is not None:
            tmp = (
                self.wind_stator.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            Loss1_str += "wind_stator = " + tmp
        else:
            Loss1_str += "wind_stator = None" + linesep + linesep
        if self.wind_rotor is not None:
            tmp = (
                self.wind_rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            Loss1_str += "wind_rotor = " + tmp
        else:
            Loss1_str += "wind_rotor = None" + linesep + linesep
        if self.mag_stator is not None:
            tmp = (
                self.mag_stator.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            Loss1_str += "mag_stator = " + tmp
        else:
            Loss1_str += "mag_stator = None" + linesep + linesep
        if self.mag_rotor is not None:
            tmp = self.mag_rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Loss1_str += "mag_rotor = " + tmp
        else:
            Loss1_str += "mag_rotor = None" + linesep + linesep
        if self.windage is not None:
            tmp = self.windage.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Loss1_str += "windage = " + tmp
        else:
            Loss1_str += "windage = None" + linesep + linesep
        if self.bearing is not None:
            tmp = self.bearing.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Loss1_str += "bearing = " + tmp
        else:
            Loss1_str += "bearing = None" + linesep + linesep
        if self.shaft is not None:
            tmp = self.shaft.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Loss1_str += "shaft = " + tmp
        else:
            Loss1_str += "shaft = None" + linesep + linesep
        if self.frame is not None:
            tmp = self.frame.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Loss1_str += "frame = " + tmp
        else:
            Loss1_str += "frame = None" + linesep + linesep
        if self.additional is not None:
            tmp = (
                self.additional.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            Loss1_str += "additional = " + tmp
        else:
            Loss1_str += "additional = None" + linesep + linesep
        return Loss1_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Loss
        if not super(Loss1, self).__eq__(other):
            return False
        if other.lam_stator != self.lam_stator:
            return False
        if other.lam_rotor != self.lam_rotor:
            return False
        if other.wind_stator != self.wind_stator:
            return False
        if other.wind_rotor != self.wind_rotor:
            return False
        if other.mag_stator != self.mag_stator:
            return False
        if other.mag_rotor != self.mag_rotor:
            return False
        if other.windage != self.windage:
            return False
        if other.bearing != self.bearing:
            return False
        if other.shaft != self.shaft:
            return False
        if other.frame != self.frame:
            return False
        if other.additional != self.additional:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Loss
        Loss1_dict = super(Loss1, self).as_dict()
        if self.lam_stator is None:
            Loss1_dict["lam_stator"] = None
        else:
            Loss1_dict["lam_stator"] = self.lam_stator.as_dict()
        if self.lam_rotor is None:
            Loss1_dict["lam_rotor"] = None
        else:
            Loss1_dict["lam_rotor"] = self.lam_rotor.as_dict()
        if self.wind_stator is None:
            Loss1_dict["wind_stator"] = None
        else:
            Loss1_dict["wind_stator"] = self.wind_stator.as_dict()
        if self.wind_rotor is None:
            Loss1_dict["wind_rotor"] = None
        else:
            Loss1_dict["wind_rotor"] = self.wind_rotor.as_dict()
        if self.mag_stator is None:
            Loss1_dict["mag_stator"] = None
        else:
            Loss1_dict["mag_stator"] = self.mag_stator.as_dict()
        if self.mag_rotor is None:
            Loss1_dict["mag_rotor"] = None
        else:
            Loss1_dict["mag_rotor"] = self.mag_rotor.as_dict()
        if self.windage is None:
            Loss1_dict["windage"] = None
        else:
            Loss1_dict["windage"] = self.windage.as_dict()
        if self.bearing is None:
            Loss1_dict["bearing"] = None
        else:
            Loss1_dict["bearing"] = self.bearing.as_dict()
        if self.shaft is None:
            Loss1_dict["shaft"] = None
        else:
            Loss1_dict["shaft"] = self.shaft.as_dict()
        if self.frame is None:
            Loss1_dict["frame"] = None
        else:
            Loss1_dict["frame"] = self.frame.as_dict()
        if self.additional is None:
            Loss1_dict["additional"] = None
        else:
            Loss1_dict["additional"] = self.additional.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        Loss1_dict["__class__"] = "Loss1"
        return Loss1_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.lam_stator is not None:
            self.lam_stator._set_None()
        if self.lam_rotor is not None:
            self.lam_rotor._set_None()
        if self.wind_stator is not None:
            self.wind_stator._set_None()
        if self.wind_rotor is not None:
            self.wind_rotor._set_None()
        if self.mag_stator is not None:
            self.mag_stator._set_None()
        if self.mag_rotor is not None:
            self.mag_rotor._set_None()
        if self.windage is not None:
            self.windage._set_None()
        if self.bearing is not None:
            self.bearing._set_None()
        if self.shaft is not None:
            self.shaft._set_None()
        if self.frame is not None:
            self.frame._set_None()
        if self.additional is not None:
            self.additional._set_None()
        # Set to None the properties inherited from Loss
        super(Loss1, self)._set_None()

    def _get_lam_stator(self):
        """getter of lam_stator"""
        return self._lam_stator

    def _set_lam_stator(self, value):
        """setter of lam_stator"""
        check_var("lam_stator", value, "LossModel")
        self._lam_stator = value

        if self._lam_stator is not None:
            self._lam_stator.parent = self

    # Stator Lamination Loss Model
    # Type : LossModel
    lam_stator = property(
        fget=_get_lam_stator,
        fset=_set_lam_stator,
        doc=u"""Stator Lamination Loss Model""",
    )

    def _get_lam_rotor(self):
        """getter of lam_rotor"""
        return self._lam_rotor

    def _set_lam_rotor(self, value):
        """setter of lam_rotor"""
        check_var("lam_rotor", value, "LossModel")
        self._lam_rotor = value

        if self._lam_rotor is not None:
            self._lam_rotor.parent = self

    # Rotor Lamination Loss Model
    # Type : LossModel
    lam_rotor = property(
        fget=_get_lam_rotor, fset=_set_lam_rotor, doc=u"""Rotor Lamination Loss Model"""
    )

    def _get_wind_stator(self):
        """getter of wind_stator"""
        return self._wind_stator

    def _set_wind_stator(self, value):
        """setter of wind_stator"""
        check_var("wind_stator", value, "LossModel")
        self._wind_stator = value

        if self._wind_stator is not None:
            self._wind_stator.parent = self

    # Stator Winding Loss Model
    # Type : LossModel
    wind_stator = property(
        fget=_get_wind_stator,
        fset=_set_wind_stator,
        doc=u"""Stator Winding Loss Model""",
    )

    def _get_wind_rotor(self):
        """getter of wind_rotor"""
        return self._wind_rotor

    def _set_wind_rotor(self, value):
        """setter of wind_rotor"""
        check_var("wind_rotor", value, "LossModel")
        self._wind_rotor = value

        if self._wind_rotor is not None:
            self._wind_rotor.parent = self

    # Rotor Winding Loss Model
    # Type : LossModel
    wind_rotor = property(
        fget=_get_wind_rotor, fset=_set_wind_rotor, doc=u"""Rotor Winding Loss Model"""
    )

    def _get_mag_stator(self):
        """getter of mag_stator"""
        return self._mag_stator

    def _set_mag_stator(self, value):
        """setter of mag_stator"""
        check_var("mag_stator", value, "LossModel")
        self._mag_stator = value

        if self._mag_stator is not None:
            self._mag_stator.parent = self

    # Stator Magnet Loss Model
    # Type : LossModel
    mag_stator = property(
        fget=_get_mag_stator, fset=_set_mag_stator, doc=u"""Stator Magnet Loss Model"""
    )

    def _get_mag_rotor(self):
        """getter of mag_rotor"""
        return self._mag_rotor

    def _set_mag_rotor(self, value):
        """setter of mag_rotor"""
        check_var("mag_rotor", value, "LossModel")
        self._mag_rotor = value

        if self._mag_rotor is not None:
            self._mag_rotor.parent = self

    # Rotor Magnet Loss Model
    # Type : LossModel
    mag_rotor = property(
        fget=_get_mag_rotor, fset=_set_mag_rotor, doc=u"""Rotor Magnet Loss Model"""
    )

    def _get_windage(self):
        """getter of windage"""
        return self._windage

    def _set_windage(self, value):
        """setter of windage"""
        check_var("windage", value, "LossModel")
        self._windage = value

        if self._windage is not None:
            self._windage.parent = self

    # Windage Loss Model
    # Type : LossModel
    windage = property(
        fget=_get_windage, fset=_set_windage, doc=u"""Windage Loss Model"""
    )

    def _get_bearing(self):
        """getter of bearing"""
        return self._bearing

    def _set_bearing(self, value):
        """setter of bearing"""
        check_var("bearing", value, "LossModel")
        self._bearing = value

        if self._bearing is not None:
            self._bearing.parent = self

    # Bearing Loss Model
    # Type : LossModel
    bearing = property(
        fget=_get_bearing, fset=_set_bearing, doc=u"""Bearing Loss Model"""
    )

    def _get_shaft(self):
        """getter of shaft"""
        return self._shaft

    def _set_shaft(self, value):
        """setter of shaft"""
        check_var("shaft", value, "LossModel")
        self._shaft = value

        if self._shaft is not None:
            self._shaft.parent = self

    # Shaft Loss Model
    # Type : LossModel
    shaft = property(fget=_get_shaft, fset=_set_shaft, doc=u"""Shaft Loss Model""")

    def _get_frame(self):
        """getter of frame"""
        return self._frame

    def _set_frame(self, value):
        """setter of frame"""
        check_var("frame", value, "LossModel")
        self._frame = value

        if self._frame is not None:
            self._frame.parent = self

    # Frame Loss Model
    # Type : LossModel
    frame = property(fget=_get_frame, fset=_set_frame, doc=u"""Frame Loss Model""")

    def _get_additional(self):
        """getter of additional"""
        return self._additional

    def _set_additional(self, value):
        """setter of additional"""
        check_var("additional", value, "LossModel")
        self._additional = value

        if self._additional is not None:
            self._additional.parent = self

    # Loss moduale
    # Type : LossModel
    additional = property(
        fget=_get_additional, fset=_set_additional, doc=u"""Loss moduale"""
    )
