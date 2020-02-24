# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Simulation/InForce.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Input import Input

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Simulation.InForce.gen_input import gen_input
except ImportError as error:
    gen_input = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.Import import Import


class InForce(Input):
    """Input to start with the structural one """

    VERSION = 1

    # cf Methods.Simulation.InForce.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError("Can't use InForce method gen_input: " + str(gen_input))
            )
        )
    else:
        gen_input = gen_input
    # save method is available in all object
    save = save

    def __init__(self, time=None, angle=None, Prad=None, Ptan=None, init_dict=None):
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
        if Prad == -1:
            Prad = Import()
        if Ptan == -1:
            Ptan = Import()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["time", "angle", "Prad", "Ptan"])
            # Overwrite default value with init_dict content
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Prad" in list(init_dict.keys()):
                Prad = init_dict["Prad"]
            if "Ptan" in list(init_dict.keys()):
                Ptan = init_dict["Ptan"]
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
        # Prad can be None, a Import object or a dict
        if isinstance(Prad, dict):
            # Check that the type is correct (including daughter)
            class_name = Prad.get("__class__")
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
                    "Unknow class name " + class_name + " in init_dict for Prad"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.Prad = class_obj(init_dict=Prad)
        else:
            self.Prad = Prad
        # Ptan can be None, a Import object or a dict
        if isinstance(Ptan, dict):
            # Check that the type is correct (including daughter)
            class_name = Ptan.get("__class__")
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
                    "Unknow class name " + class_name + " in init_dict for Ptan"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.Ptan = class_obj(init_dict=Ptan)
        else:
            self.Ptan = Ptan
        # Call Input init
        super(InForce, self).__init__()
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        InForce_str = ""
        # Get the properties inherited from Input
        InForce_str += super(InForce, self).__str__()
        if self.time is not None:
            tmp = self.time.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InForce_str += "time = " + tmp
        else:
            InForce_str += "time = None" + linesep + linesep
        if self.angle is not None:
            tmp = self.angle.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InForce_str += "angle = " + tmp
        else:
            InForce_str += "angle = None" + linesep + linesep
        if self.Prad is not None:
            tmp = self.Prad.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InForce_str += "Prad = " + tmp
        else:
            InForce_str += "Prad = None" + linesep + linesep
        if self.Ptan is not None:
            tmp = self.Ptan.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InForce_str += "Ptan = " + tmp
        else:
            InForce_str += "Ptan = None" + linesep + linesep
        return InForce_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InForce, self).__eq__(other):
            return False
        if other.time != self.time:
            return False
        if other.angle != self.angle:
            return False
        if other.Prad != self.Prad:
            return False
        if other.Ptan != self.Ptan:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Input
        InForce_dict = super(InForce, self).as_dict()
        if self.time is None:
            InForce_dict["time"] = None
        else:
            InForce_dict["time"] = self.time.as_dict()
        if self.angle is None:
            InForce_dict["angle"] = None
        else:
            InForce_dict["angle"] = self.angle.as_dict()
        if self.Prad is None:
            InForce_dict["Prad"] = None
        else:
            InForce_dict["Prad"] = self.Prad.as_dict()
        if self.Ptan is None:
            InForce_dict["Ptan"] = None
        else:
            InForce_dict["Ptan"] = self.Ptan.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        InForce_dict["__class__"] = "InForce"
        return InForce_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.time is not None:
            self.time._set_None()
        if self.angle is not None:
            self.angle._set_None()
        if self.Prad is not None:
            self.Prad._set_None()
        if self.Ptan is not None:
            self.Ptan._set_None()
        # Set to None the properties inherited from Input
        super(InForce, self)._set_None()

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

    def _get_Prad(self):
        """getter of Prad"""
        return self._Prad

    def _set_Prad(self, value):
        """setter of Prad"""
        check_var("Prad", value, "Import")
        self._Prad = value

        if self._Prad is not None:
            self._Prad.parent = self

    # Radial magnetic air-gap surface force
    # Type : Import
    Prad = property(
        fget=_get_Prad, fset=_set_Prad, doc=u"""Radial magnetic air-gap surface force"""
    )

    def _get_Ptan(self):
        """getter of Ptan"""
        return self._Ptan

    def _set_Ptan(self, value):
        """setter of Ptan"""
        check_var("Ptan", value, "Import")
        self._Ptan = value

        if self._Ptan is not None:
            self._Ptan.parent = self

    # Tangential magnetic air-gap surface force
    # Type : Import
    Ptan = property(
        fget=_get_Ptan,
        fset=_set_Ptan,
        doc=u"""Tangential magnetic air-gap surface force""",
    )
