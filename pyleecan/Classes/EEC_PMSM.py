# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/EEC_PMSM.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .EEC import EEC

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.EEC_PMSM.comp_parameters import comp_parameters
except ImportError as error:
    comp_parameters = error

try:
    from ..Methods.Simulation.EEC_PMSM.solve_EEC import solve_EEC
except ImportError as error:
    solve_EEC = error

try:
    from ..Methods.Simulation.EEC_PMSM.gen_drive import gen_drive
except ImportError as error:
    gen_drive = error


from ._check import InitUnKnowClassError
from .IndMag import IndMag
from .FluxLink import FluxLink
from .Drive import Drive


class EEC_PMSM(EEC):
    """Electric module: Electrical Equivalent Circuit"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.EEC_PMSM.comp_parameters
    if isinstance(comp_parameters, ImportError):
        comp_parameters = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_PMSM method comp_parameters: " + str(comp_parameters)
                )
            )
        )
    else:
        comp_parameters = comp_parameters
    # cf Methods.Simulation.EEC_PMSM.solve_EEC
    if isinstance(solve_EEC, ImportError):
        solve_EEC = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_PMSM method solve_EEC: " + str(solve_EEC))
            )
        )
    else:
        solve_EEC = solve_EEC
    # cf Methods.Simulation.EEC_PMSM.gen_drive
    if isinstance(gen_drive, ImportError):
        gen_drive = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_PMSM method gen_drive: " + str(gen_drive))
            )
        )
    else:
        gen_drive = gen_drive
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
        indmag=None,
        fluxlink=None,
        parameters={},
        freq0=None,
        drive=None,
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

        if indmag == -1:
            indmag = IndMag()
        if fluxlink == -1:
            fluxlink = FluxLink()
        if drive == -1:
            drive = Drive()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            indmag = obj.indmag
            fluxlink = obj.fluxlink
            parameters = obj.parameters
            freq0 = obj.freq0
            drive = obj.drive
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "indmag" in list(init_dict.keys()):
                indmag = init_dict["indmag"]
            if "fluxlink" in list(init_dict.keys()):
                fluxlink = init_dict["fluxlink"]
            if "parameters" in list(init_dict.keys()):
                parameters = init_dict["parameters"]
            if "freq0" in list(init_dict.keys()):
                freq0 = init_dict["freq0"]
            if "drive" in list(init_dict.keys()):
                drive = init_dict["drive"]
        # Initialisation by argument
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
        elif isinstance(indmag, str):
            from ..Functions.load import load

            indmag = load(indmag)
            # Check that the type is correct (including daughter)
            class_name = indmag.__class__.__name__
            if class_name not in ["IndMag", "IndMagFEMM"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for indmag"
                )
            self.indmag = indmag
        else:
            self.indmag = indmag
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
        elif isinstance(fluxlink, str):
            from ..Functions.load import load

            fluxlink = load(fluxlink)
            # Check that the type is correct (including daughter)
            class_name = fluxlink.__class__.__name__
            if class_name not in ["FluxLink", "FluxLinkFEMM"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for fluxlink"
                )
            self.fluxlink = fluxlink
        else:
            self.fluxlink = fluxlink
        self.parameters = parameters
        self.freq0 = freq0
        # drive can be None, a Drive object or a dict
        if isinstance(drive, dict):
            # Check that the type is correct (including daughter)
            class_name = drive.get("__class__")
            if class_name not in ["Drive", "DriveWave"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for drive"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.drive = class_obj(init_dict=drive)
        elif isinstance(drive, str):
            from ..Functions.load import load

            drive = load(drive)
            # Check that the type is correct (including daughter)
            class_name = drive.__class__.__name__
            if class_name not in ["Drive", "DriveWave"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for drive"
                )
            self.drive = drive
        else:
            self.drive = drive
        # Call EEC init
        super(EEC_PMSM, self).__init__()
        # The class is frozen (in EEC init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        EEC_PMSM_str = ""
        # Get the properties inherited from EEC
        EEC_PMSM_str += super(EEC_PMSM, self).__str__()
        if self.indmag is not None:
            tmp = self.indmag.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            EEC_PMSM_str += "indmag = " + tmp
        else:
            EEC_PMSM_str += "indmag = None" + linesep + linesep
        if self.fluxlink is not None:
            tmp = self.fluxlink.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            EEC_PMSM_str += "fluxlink = " + tmp
        else:
            EEC_PMSM_str += "fluxlink = None" + linesep + linesep
        EEC_PMSM_str += "parameters = " + str(self.parameters) + linesep
        EEC_PMSM_str += "freq0 = " + str(self.freq0) + linesep
        if self.drive is not None:
            tmp = self.drive.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            EEC_PMSM_str += "drive = " + tmp
        else:
            EEC_PMSM_str += "drive = None" + linesep + linesep
        return EEC_PMSM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from EEC
        if not super(EEC_PMSM, self).__eq__(other):
            return False
        if other.indmag != self.indmag:
            return False
        if other.fluxlink != self.fluxlink:
            return False
        if other.parameters != self.parameters:
            return False
        if other.freq0 != self.freq0:
            return False
        if other.drive != self.drive:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from EEC
        EEC_PMSM_dict = super(EEC_PMSM, self).as_dict()
        if self.indmag is None:
            EEC_PMSM_dict["indmag"] = None
        else:
            EEC_PMSM_dict["indmag"] = self.indmag.as_dict()
        if self.fluxlink is None:
            EEC_PMSM_dict["fluxlink"] = None
        else:
            EEC_PMSM_dict["fluxlink"] = self.fluxlink.as_dict()
        EEC_PMSM_dict["parameters"] = self.parameters
        EEC_PMSM_dict["freq0"] = self.freq0
        if self.drive is None:
            EEC_PMSM_dict["drive"] = None
        else:
            EEC_PMSM_dict["drive"] = self.drive.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        EEC_PMSM_dict["__class__"] = "EEC_PMSM"
        return EEC_PMSM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.indmag is not None:
            self.indmag._set_None()
        if self.fluxlink is not None:
            self.fluxlink._set_None()
        self.parameters = None
        self.freq0 = None
        if self.drive is not None:
            self.drive._set_None()
        # Set to None the properties inherited from EEC
        super(EEC_PMSM, self)._set_None()

    def _get_indmag(self):
        """getter of indmag"""
        return self._indmag

    def _set_indmag(self, value):
        """setter of indmag"""
        check_var("indmag", value, "IndMag")
        self._indmag = value

        if self._indmag is not None:
            self._indmag.parent = self

    # Magnetic inductance
    # Type : IndMag
    indmag = property(
        fget=_get_indmag, fset=_set_indmag, doc=u"""Magnetic inductance"""
    )

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

    def _get_parameters(self):
        """getter of parameters"""
        return self._parameters

    def _set_parameters(self, value):
        """setter of parameters"""
        check_var("parameters", value, "dict")
        self._parameters = value

    # Parameters of the EEC: computed if empty, or enforced
    # Type : dict
    parameters = property(
        fget=_get_parameters,
        fset=_set_parameters,
        doc=u"""Parameters of the EEC: computed if empty, or enforced""",
    )

    def _get_freq0(self):
        """getter of freq0"""
        return self._freq0

    def _set_freq0(self, value):
        """setter of freq0"""
        check_var("freq0", value, "float")
        self._freq0 = value

    # Frequency
    # Type : float
    freq0 = property(fget=_get_freq0, fset=_set_freq0, doc=u"""Frequency""")

    def _get_drive(self):
        """getter of drive"""
        return self._drive

    def _set_drive(self, value):
        """setter of drive"""
        check_var("drive", value, "Drive")
        self._drive = value

        if self._drive is not None:
            self._drive.parent = self

    # Drive
    # Type : Drive
    drive = property(fget=_get_drive, fset=_set_drive, doc=u"""Drive""")
