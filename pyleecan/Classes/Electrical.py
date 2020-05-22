# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/Electrical.csv
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
    from ..Methods.Simulation.Electrical.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Simulation.Electrical.comp_fluxlinkage import comp_fluxlinkage
except ImportError as error:
    comp_fluxlinkage = error

try:
    from ..Methods.Simulation.Electrical.comp_inductance import comp_inductance
except ImportError as error:
    comp_inductance = error


from ._check import InitUnKnowClassError
from .FluxLink import FluxLink
from .IndMag import IndMag


class Electrical(FrozenClass):
    """Electric module abstract object"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Electrical.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use Electrical method run: " + str(run))
            )
        )
    else:
        run = run
    # cf Methods.Simulation.Electrical.comp_fluxlinkage
    if isinstance(comp_fluxlinkage, ImportError):
        comp_fluxlinkage = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Electrical method comp_fluxlinkage: "
                    + str(comp_fluxlinkage)
                )
            )
        )
    else:
        comp_fluxlinkage = comp_fluxlinkage
    # cf Methods.Simulation.Electrical.comp_inductance
    if isinstance(comp_inductance, ImportError):
        comp_inductance = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Electrical method comp_inductance: "
                    + str(comp_inductance)
                )
            )
        )
    else:
        comp_inductance = comp_inductance
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, fluxlink=-1, indmag=-1, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if fluxlink == -1:
            fluxlink = FluxLink()
        if indmag == -1:
            indmag = IndMag()
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "fluxlink" in list(init_dict.keys()):
                fluxlink = init_dict["fluxlink"]
            if "indmag" in list(init_dict.keys()):
                indmag = init_dict["indmag"]
        # Initialisation by argument
        self.parent = None
        # fluxlink can be None, a FluxLink object or a dict
        if isinstance(fluxlink, dict):
            # Check that the type is correct (including daughter)
            class_name = fluxlink.get("__class__")
            if class_name not in ["FluxLink", "FluxLinkFEMM"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for fluxlink"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.fluxlink = class_obj(init_dict=fluxlink)
        else:
            self.fluxlink = fluxlink
        # indmag can be None, a IndMag object or a dict
        if isinstance(indmag, dict):
            # Check that the type is correct (including daughter)
            class_name = indmag.get("__class__")
            if class_name not in ["IndMag", "IndMagFEMM"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for indmag"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.indmag = class_obj(init_dict=indmag)
        else:
            self.indmag = indmag

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Electrical_str = ""
        if self.parent is None:
            Electrical_str += "parent = None " + linesep
        else:
            Electrical_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.fluxlink is not None:
            tmp = self.fluxlink.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Electrical_str += "fluxlink = " + tmp
        else:
            Electrical_str += "fluxlink = None" + linesep + linesep
        if self.indmag is not None:
            tmp = self.indmag.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Electrical_str += "indmag = " + tmp
        else:
            Electrical_str += "indmag = None" + linesep + linesep
        return Electrical_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.fluxlink != self.fluxlink:
            return False
        if other.indmag != self.indmag:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Electrical_dict = dict()
        if self.fluxlink is None:
            Electrical_dict["fluxlink"] = None
        else:
            Electrical_dict["fluxlink"] = self.fluxlink.as_dict()
        if self.indmag is None:
            Electrical_dict["indmag"] = None
        else:
            Electrical_dict["indmag"] = self.indmag.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        Electrical_dict["__class__"] = "Electrical"
        return Electrical_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.fluxlink is not None:
            self.fluxlink._set_None()
        if self.indmag is not None:
            self.indmag._set_None()

    def _get_fluxlink(self):
        """getter of fluxlink"""
        return self._fluxlink

    def _set_fluxlink(self, value):
        """setter of fluxlink"""
        check_var("fluxlink", value, "FluxLink")
        self._fluxlink = value

        if self._fluxlink is not None:
            self._fluxlink.parent = self

    # Flux Linkage
    # Type : FluxLink
    fluxlink = property(fget=_get_fluxlink, fset=_set_fluxlink, doc=u"""Flux Linkage""")

    def _get_indmag(self):
        """getter of indmag"""
        return self._indmag

    def _set_indmag(self, value):
        """setter of indmag"""
        check_var("indmag", value, "IndMag")
        self._indmag = value

        if self._indmag is not None:
            self._indmag.parent = self

    # Magnetic Inductance
    # Type : IndMag
    indmag = property(
        fget=_get_indmag, fset=_set_indmag, doc=u"""Magnetic Inductance"""
    )
