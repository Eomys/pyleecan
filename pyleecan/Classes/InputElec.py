# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/InputElec.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/InputElec
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Input import Input

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.InputElec.gen_input import gen_input
except ImportError as error:
    gen_input = error

try:
    from ..Methods.Simulation.InputElec.comp_felec import comp_felec
except ImportError as error:
    comp_felec = error

try:
    from ..Methods.Simulation.InputElec.set_Id_Iq import set_Id_Iq
except ImportError as error:
    set_Id_Iq = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .ImportMatrix import ImportMatrix


class InputElec(Input):
    """Input to skip the electrical module and start with the magnetic one"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.InputElec.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError("Can't use InputElec method gen_input: " + str(gen_input))
            )
        )
    else:
        gen_input = gen_input
    # cf Methods.Simulation.InputElec.comp_felec
    if isinstance(comp_felec, ImportError):
        comp_felec = property(
            fget=lambda x: raise_(
                ImportError("Can't use InputElec method comp_felec: " + str(comp_felec))
            )
        )
    else:
        comp_felec = comp_felec
    # cf Methods.Simulation.InputElec.set_Id_Iq
    if isinstance(set_Id_Iq, ImportError):
        set_Id_Iq = property(
            fget=lambda x: raise_(
                ImportError("Can't use InputElec method set_Id_Iq: " + str(set_Id_Iq))
            )
        )
    else:
        set_Id_Iq = set_Id_Iq
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        N0=None,
        rot_dir=-1,
        Id_ref=None,
        Iq_ref=None,
        Ud_ref=None,
        Uq_ref=None,
        time=None,
        angle=None,
        Nt_tot=2048,
        Nrev=1,
        Na_tot=2048,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "N0" in list(init_dict.keys()):
                N0 = init_dict["N0"]
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
            if "Id_ref" in list(init_dict.keys()):
                Id_ref = init_dict["Id_ref"]
            if "Iq_ref" in list(init_dict.keys()):
                Iq_ref = init_dict["Iq_ref"]
            if "Ud_ref" in list(init_dict.keys()):
                Ud_ref = init_dict["Ud_ref"]
            if "Uq_ref" in list(init_dict.keys()):
                Uq_ref = init_dict["Uq_ref"]
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Nrev" in list(init_dict.keys()):
                Nrev = init_dict["Nrev"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
        # Set the properties (value check and convertion are done in setter)
        self.N0 = N0
        self.rot_dir = rot_dir
        self.Id_ref = Id_ref
        self.Iq_ref = Iq_ref
        self.Ud_ref = Ud_ref
        self.Uq_ref = Uq_ref
        # Call Input init
        super(InputElec, self).__init__(
            time=time, angle=angle, Nt_tot=Nt_tot, Nrev=Nrev, Na_tot=Na_tot
        )
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        InputElec_str = ""
        # Get the properties inherited from Input
        InputElec_str += super(InputElec, self).__str__()
        InputElec_str += "N0 = " + str(self.N0) + linesep
        InputElec_str += "rot_dir = " + str(self.rot_dir) + linesep
        InputElec_str += "Id_ref = " + str(self.Id_ref) + linesep
        InputElec_str += "Iq_ref = " + str(self.Iq_ref) + linesep
        InputElec_str += "Ud_ref = " + str(self.Ud_ref) + linesep
        InputElec_str += "Uq_ref = " + str(self.Uq_ref) + linesep
        return InputElec_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InputElec, self).__eq__(other):
            return False
        if other.N0 != self.N0:
            return False
        if other.rot_dir != self.rot_dir:
            return False
        if other.Id_ref != self.Id_ref:
            return False
        if other.Iq_ref != self.Iq_ref:
            return False
        if other.Ud_ref != self.Ud_ref:
            return False
        if other.Uq_ref != self.Uq_ref:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from Input
        InputElec_dict = super(InputElec, self).as_dict()
        InputElec_dict["N0"] = self.N0
        InputElec_dict["rot_dir"] = self.rot_dir
        InputElec_dict["Id_ref"] = self.Id_ref
        InputElec_dict["Iq_ref"] = self.Iq_ref
        InputElec_dict["Ud_ref"] = self.Ud_ref
        InputElec_dict["Uq_ref"] = self.Uq_ref
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        InputElec_dict["__class__"] = "InputElec"
        return InputElec_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.N0 = None
        self.rot_dir = None
        self.Id_ref = None
        self.Iq_ref = None
        self.Ud_ref = None
        self.Uq_ref = None
        # Set to None the properties inherited from Input
        super(InputElec, self)._set_None()

    def _get_N0(self):
        """getter of N0"""
        return self._N0

    def _set_N0(self, value):
        """setter of N0"""
        check_var("N0", value, "float")
        self._N0 = value

    N0 = property(
        fget=_get_N0,
        fset=_set_N0,
        doc=u"""Rotor speed

        :Type: float
        """,
    )

    def _get_rot_dir(self):
        """getter of rot_dir"""
        return self._rot_dir

    def _set_rot_dir(self, value):
        """setter of rot_dir"""
        check_var("rot_dir", value, "float", Vmin=-1, Vmax=1)
        self._rot_dir = value

    rot_dir = property(
        fget=_get_rot_dir,
        fset=_set_rot_dir,
        doc=u"""Rotation direction of the rotor 1 trigo, -1 clockwise

        :Type: float
        :min: -1
        :max: 1
        """,
    )

    def _get_Id_ref(self):
        """getter of Id_ref"""
        return self._Id_ref

    def _set_Id_ref(self, value):
        """setter of Id_ref"""
        check_var("Id_ref", value, "float")
        self._Id_ref = value

    Id_ref = property(
        fget=_get_Id_ref,
        fset=_set_Id_ref,
        doc=u"""d-axis current magnitude

        :Type: float
        """,
    )

    def _get_Iq_ref(self):
        """getter of Iq_ref"""
        return self._Iq_ref

    def _set_Iq_ref(self, value):
        """setter of Iq_ref"""
        check_var("Iq_ref", value, "float")
        self._Iq_ref = value

    Iq_ref = property(
        fget=_get_Iq_ref,
        fset=_set_Iq_ref,
        doc=u"""q-axis current magnitude

        :Type: float
        """,
    )

    def _get_Ud_ref(self):
        """getter of Ud_ref"""
        return self._Ud_ref

    def _set_Ud_ref(self, value):
        """setter of Ud_ref"""
        check_var("Ud_ref", value, "float")
        self._Ud_ref = value

    Ud_ref = property(
        fget=_get_Ud_ref,
        fset=_set_Ud_ref,
        doc=u"""d-axis voltage magnitude

        :Type: float
        """,
    )

    def _get_Uq_ref(self):
        """getter of Uq_ref"""
        return self._Uq_ref

    def _set_Uq_ref(self, value):
        """setter of Uq_ref"""
        check_var("Uq_ref", value, "float")
        self._Uq_ref = value

    Uq_ref = property(
        fget=_get_Uq_ref,
        fset=_set_Uq_ref,
        doc=u"""q-axis voltage magnitude

        :Type: float
        """,
    )
