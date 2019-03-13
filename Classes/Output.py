# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.OutGeo import OutGeo
from pyleecan.Classes.OutElec import OutElec
from pyleecan.Classes.Simulation import Simulation
from pyleecan.Classes.Simu1 import Simu1


class Output(FrozenClass):
    """Main Output object: gather all the outputs of all the modules"""

    VERSION = 1

    def __init__(self, geo=-1, elec=-1, simu=-1, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if geo == -1:
            geo = OutGeo()
        if elec == -1:
            elec = OutElec()
        if simu == -1:
            simu = Simulation()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["geo", "elec", "simu"])
            # Overwrite default value with init_dict content
            if "geo" in list(init_dict.keys()):
                geo = init_dict["geo"]
            if "elec" in list(init_dict.keys()):
                elec = init_dict["elec"]
            if "simu" in list(init_dict.keys()):
                simu = init_dict["simu"]
        # Initialisation by argument
        self.parent = None
        # geo can be None, a OutGeo object or a dict
        if isinstance(geo, dict):
            self.geo = OutGeo(init_dict=geo)
        else:
            self.geo = geo
        # elec can be None, a OutElec object or a dict
        if isinstance(elec, dict):
            self.elec = OutElec(init_dict=elec)
        else:
            self.elec = elec
        # simu can be None, a Simulation object or a dict
        if isinstance(simu, dict):
            # Call the correct constructor according to the dict
            load_dict = {"Simu1": Simu1, "Simulation": Simulation}
            obj_class = simu.get("__class__")
            if obj_class is None:
                self.simu = Simulation(init_dict=simu)
            elif obj_class in list(load_dict.keys()):
                self.simu = load_dict[obj_class](init_dict=simu)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError("Unknow class name in init_dict for simu")
        else:
            self.simu = simu

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Output_str = ""
        if self.parent is None:
            Output_str += "parent = None " + linesep
        else:
            Output_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Output_str += "geo = " + str(self.geo.as_dict()) + linesep + linesep
        Output_str += "elec = " + str(self.elec.as_dict()) + linesep + linesep
        Output_str += "simu = " + str(self.simu.as_dict())
        return Output_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.geo != self.geo:
            return False
        if other.elec != self.elec:
            return False
        if other.simu != self.simu:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Output_dict = dict()
        if self.geo is None:
            Output_dict["geo"] = None
        else:
            Output_dict["geo"] = self.geo.as_dict()
        if self.elec is None:
            Output_dict["elec"] = None
        else:
            Output_dict["elec"] = self.elec.as_dict()
        if self.simu is None:
            Output_dict["simu"] = None
        else:
            Output_dict["simu"] = self.simu.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        Output_dict["__class__"] = "Output"
        return Output_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.geo is not None:
            self.geo._set_None()
        if self.elec is not None:
            self.elec._set_None()
        if self.simu is not None:
            self.simu._set_None()

    def _get_geo(self):
        """getter of geo"""
        return self._geo

    def _set_geo(self, value):
        """setter of geo"""
        check_var("geo", value, "OutGeo")
        self._geo = value

        if self._geo is not None:
            self._geo.parent = self

    # Geometry output
    # Type : OutGeo
    geo = property(fget=_get_geo, fset=_set_geo, doc=u"""Geometry output""")

    def _get_elec(self):
        """getter of elec"""
        return self._elec

    def _set_elec(self, value):
        """setter of elec"""
        check_var("elec", value, "OutElec")
        self._elec = value

        if self._elec is not None:
            self._elec.parent = self

    # Electrical module output
    # Type : OutElec
    elec = property(fget=_get_elec, fset=_set_elec, doc=u"""Electrical module output""")

    def _get_simu(self):
        """getter of simu"""
        return self._simu

    def _set_simu(self, value):
        """setter of simu"""
        check_var("simu", value, "Simulation")
        self._simu = value

        if self._simu is not None:
            self._simu.parent = self

    # Simulation object that generated the Output
    # Type : Simulation
    simu = property(
        fget=_get_simu,
        fset=_set_simu,
        doc=u"""Simulation object that generated the Output""",
    )
