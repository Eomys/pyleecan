# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Input import Input

from pyleecan.Methods.Simulation.InFlux.gen_input import gen_input

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Import import Import


class InFlux(Input):
    """Input to skip the magnetic module and start with the structural one"""

    VERSION = 1

    # cf Methods.Simulation.InFlux.gen_input
    gen_input = gen_input
    # save method is available in all object
    save = save

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
            check_init_dict(init_dict, ["time", "angle", "Br", "Bt"])
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
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
                "ImportGenVectSin",
                "ImportGenMatrixSin",
                "ImportGenVectLin",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for " + prop_name
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
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
                "ImportGenVectSin",
                "ImportGenMatrixSin",
                "ImportGenVectLin",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for " + prop_name
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
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
                "ImportGenVectSin",
                "ImportGenMatrixSin",
                "ImportGenVectLin",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for " + prop_name
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
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "Import",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
                "ImportGenVectSin",
                "ImportGenMatrixSin",
                "ImportGenVectLin",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for " + prop_name
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.Bt = class_obj(init_dict=Bt)
        else:
            self.Bt = Bt
        # Call Input init
        super(InFlux, self).__init__()
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        InFlux_str = ""
        # Get the properties inherited from Input
        InFlux_str += super(InFlux, self).__str__() + linesep
        InFlux_str += "time = " + str(self.time.as_dict()) + linesep + linesep
        InFlux_str += "angle = " + str(self.angle.as_dict()) + linesep + linesep
        InFlux_str += "Br = " + str(self.Br.as_dict()) + linesep + linesep
        InFlux_str += "Bt = " + str(self.Bt.as_dict())
        return InFlux_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InFlux, self).__eq__(other):
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
        InFlux_dict = super(InFlux, self).as_dict()
        if self.time is None:
            InFlux_dict["time"] = None
        else:
            InFlux_dict["time"] = self.time.as_dict()
        if self.angle is None:
            InFlux_dict["angle"] = None
        else:
            InFlux_dict["angle"] = self.angle.as_dict()
        if self.Br is None:
            InFlux_dict["Br"] = None
        else:
            InFlux_dict["Br"] = self.Br.as_dict()
        if self.Bt is None:
            InFlux_dict["Bt"] = None
        else:
            InFlux_dict["Bt"] = self.Bt.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        InFlux_dict["__class__"] = "InFlux"
        return InFlux_dict

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
        super(InFlux, self)._set_None()

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
