# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/FluxLinkFEMM.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .FluxLink import FluxLink

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.FluxLinkFEMM.comp_fluxlinkage import comp_fluxlinkage
except ImportError as error:
    comp_fluxlinkage = error

try:
    from ..Methods.Simulation.FluxLinkFEMM.solve_FEMM import solve_FEMM
except ImportError as error:
    solve_FEMM = error


from ._check import InitUnKnowClassError


class FluxLinkFEMM(FluxLink):
    """Electric module: Flux Linkage with FEMM"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.FluxLinkFEMM.comp_fluxlinkage
    if isinstance(comp_fluxlinkage, ImportError):
        comp_fluxlinkage = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use FluxLinkFEMM method comp_fluxlinkage: "
                    + str(comp_fluxlinkage)
                )
            )
        )
    else:
        comp_fluxlinkage = comp_fluxlinkage
    # cf Methods.Simulation.FluxLinkFEMM.solve_FEMM
    if isinstance(solve_FEMM, ImportError):
        solve_FEMM = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use FluxLinkFEMM method solve_FEMM: " + str(solve_FEMM)
                )
            )
        )
    else:
        solve_FEMM = solve_FEMM
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
        FEMM_dict={},
        type_calc_leakage=0,
        is_sliding_band=True,
        is_symmetry_a=False,
        sym_a=1,
        is_antiper_a=False,
        is_mmfs=True,
        is_mmfr=True,
        Nt_tot=20,
        a=0,
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

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            FEMM_dict = obj.FEMM_dict
            type_calc_leakage = obj.type_calc_leakage
            is_sliding_band = obj.is_sliding_band
            is_symmetry_a = obj.is_symmetry_a
            sym_a = obj.sym_a
            is_antiper_a = obj.is_antiper_a
            is_mmfs = obj.is_mmfs
            is_mmfr = obj.is_mmfr
            Nt_tot = obj.Nt_tot
            a = obj.a
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "FEMM_dict" in list(init_dict.keys()):
                FEMM_dict = init_dict["FEMM_dict"]
            if "type_calc_leakage" in list(init_dict.keys()):
                type_calc_leakage = init_dict["type_calc_leakage"]
            if "is_sliding_band" in list(init_dict.keys()):
                is_sliding_band = init_dict["is_sliding_band"]
            if "is_symmetry_a" in list(init_dict.keys()):
                is_symmetry_a = init_dict["is_symmetry_a"]
            if "sym_a" in list(init_dict.keys()):
                sym_a = init_dict["sym_a"]
            if "is_antiper_a" in list(init_dict.keys()):
                is_antiper_a = init_dict["is_antiper_a"]
            if "is_mmfs" in list(init_dict.keys()):
                is_mmfs = init_dict["is_mmfs"]
            if "is_mmfr" in list(init_dict.keys()):
                is_mmfr = init_dict["is_mmfr"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "a" in list(init_dict.keys()):
                a = init_dict["a"]
        # Initialisation by argument
        self.FEMM_dict = FEMM_dict
        self.type_calc_leakage = type_calc_leakage
        self.is_sliding_band = is_sliding_band
        self.is_symmetry_a = is_symmetry_a
        self.sym_a = sym_a
        self.is_antiper_a = is_antiper_a
        self.is_mmfs = is_mmfs
        self.is_mmfr = is_mmfr
        self.Nt_tot = Nt_tot
        # Call FluxLink init
        super(FluxLinkFEMM, self).__init__(a=a)
        # The class is frozen (in FluxLink init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        FluxLinkFEMM_str = ""
        # Get the properties inherited from FluxLink
        FluxLinkFEMM_str += super(FluxLinkFEMM, self).__str__()
        FluxLinkFEMM_str += "FEMM_dict = " + str(self.FEMM_dict) + linesep
        FluxLinkFEMM_str += (
            "type_calc_leakage = " + str(self.type_calc_leakage) + linesep
        )
        FluxLinkFEMM_str += "is_sliding_band = " + str(self.is_sliding_band) + linesep
        FluxLinkFEMM_str += "is_symmetry_a = " + str(self.is_symmetry_a) + linesep
        FluxLinkFEMM_str += "sym_a = " + str(self.sym_a) + linesep
        FluxLinkFEMM_str += "is_antiper_a = " + str(self.is_antiper_a) + linesep
        FluxLinkFEMM_str += "is_mmfs = " + str(self.is_mmfs) + linesep
        FluxLinkFEMM_str += "is_mmfr = " + str(self.is_mmfr) + linesep
        FluxLinkFEMM_str += "Nt_tot = " + str(self.Nt_tot) + linesep
        return FluxLinkFEMM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from FluxLink
        if not super(FluxLinkFEMM, self).__eq__(other):
            return False
        if other.FEMM_dict != self.FEMM_dict:
            return False
        if other.type_calc_leakage != self.type_calc_leakage:
            return False
        if other.is_sliding_band != self.is_sliding_band:
            return False
        if other.is_symmetry_a != self.is_symmetry_a:
            return False
        if other.sym_a != self.sym_a:
            return False
        if other.is_antiper_a != self.is_antiper_a:
            return False
        if other.is_mmfs != self.is_mmfs:
            return False
        if other.is_mmfr != self.is_mmfr:
            return False
        if other.Nt_tot != self.Nt_tot:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from FluxLink
        FluxLinkFEMM_dict = super(FluxLinkFEMM, self).as_dict()
        FluxLinkFEMM_dict["FEMM_dict"] = self.FEMM_dict
        FluxLinkFEMM_dict["type_calc_leakage"] = self.type_calc_leakage
        FluxLinkFEMM_dict["is_sliding_band"] = self.is_sliding_band
        FluxLinkFEMM_dict["is_symmetry_a"] = self.is_symmetry_a
        FluxLinkFEMM_dict["sym_a"] = self.sym_a
        FluxLinkFEMM_dict["is_antiper_a"] = self.is_antiper_a
        FluxLinkFEMM_dict["is_mmfs"] = self.is_mmfs
        FluxLinkFEMM_dict["is_mmfr"] = self.is_mmfr
        FluxLinkFEMM_dict["Nt_tot"] = self.Nt_tot
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        FluxLinkFEMM_dict["__class__"] = "FluxLinkFEMM"
        return FluxLinkFEMM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.FEMM_dict = None
        self.type_calc_leakage = None
        self.is_sliding_band = None
        self.is_symmetry_a = None
        self.sym_a = None
        self.is_antiper_a = None
        self.is_mmfs = None
        self.is_mmfr = None
        self.Nt_tot = None
        # Set to None the properties inherited from FluxLink
        super(FluxLinkFEMM, self)._set_None()

    def _get_FEMM_dict(self):
        """getter of FEMM_dict"""
        return self._FEMM_dict

    def _set_FEMM_dict(self, value):
        """setter of FEMM_dict"""
        check_var("FEMM_dict", value, "dict")
        self._FEMM_dict = value

    # To enforce user-defined values for FEMM main parameters
    # Type : dict
    FEMM_dict = property(
        fget=_get_FEMM_dict,
        fset=_set_FEMM_dict,
        doc=u"""To enforce user-defined values for FEMM main parameters """,
    )

    def _get_type_calc_leakage(self):
        """getter of type_calc_leakage"""
        return self._type_calc_leakage

    def _set_type_calc_leakage(self, value):
        """setter of type_calc_leakage"""
        check_var("type_calc_leakage", value, "int", Vmin=0, Vmax=1)
        self._type_calc_leakage = value

    # 0 no leakage calculation /  1 calculation using single slot
    # Type : int, min = 0, max = 1
    type_calc_leakage = property(
        fget=_get_type_calc_leakage,
        fset=_set_type_calc_leakage,
        doc=u"""0 no leakage calculation /  1 calculation using single slot """,
    )

    def _get_is_sliding_band(self):
        """getter of is_sliding_band"""
        return self._is_sliding_band

    def _set_is_sliding_band(self, value):
        """setter of is_sliding_band"""
        check_var("is_sliding_band", value, "bool")
        self._is_sliding_band = value

    # 0 to desactivate the sliding band
    # Type : bool
    is_sliding_band = property(
        fget=_get_is_sliding_band,
        fset=_set_is_sliding_band,
        doc=u"""0 to desactivate the sliding band""",
    )

    def _get_is_symmetry_a(self):
        """getter of is_symmetry_a"""
        return self._is_symmetry_a

    def _set_is_symmetry_a(self, value):
        """setter of is_symmetry_a"""
        check_var("is_symmetry_a", value, "bool")
        self._is_symmetry_a = value

    # 0 Compute on the complete machine, 1 compute according to sym_a and is_antiper_a
    # Type : bool
    is_symmetry_a = property(
        fget=_get_is_symmetry_a,
        fset=_set_is_symmetry_a,
        doc=u"""0 Compute on the complete machine, 1 compute according to sym_a and is_antiper_a""",
    )

    def _get_sym_a(self):
        """getter of sym_a"""
        return self._sym_a

    def _set_sym_a(self, value):
        """setter of sym_a"""
        check_var("sym_a", value, "int", Vmin=1)
        self._sym_a = value

    # Number of symmetry for the angle vector
    # Type : int, min = 1
    sym_a = property(
        fget=_get_sym_a,
        fset=_set_sym_a,
        doc=u"""Number of symmetry for the angle vector""",
    )

    def _get_is_antiper_a(self):
        """getter of is_antiper_a"""
        return self._is_antiper_a

    def _set_is_antiper_a(self, value):
        """setter of is_antiper_a"""
        check_var("is_antiper_a", value, "bool")
        self._is_antiper_a = value

    # To add an antiperiodicity to the angle vector
    # Type : bool
    is_antiper_a = property(
        fget=_get_is_antiper_a,
        fset=_set_is_antiper_a,
        doc=u"""To add an antiperiodicity to the angle vector""",
    )

    def _get_is_mmfs(self):
        """getter of is_mmfs"""
        return self._is_mmfs

    def _set_is_mmfs(self, value):
        """setter of is_mmfs"""
        check_var("is_mmfs", value, "bool")
        self._is_mmfs = value

    # 1 to compute the stator magnetomotive force / stator armature magnetic field
    # Type : bool
    is_mmfs = property(
        fget=_get_is_mmfs,
        fset=_set_is_mmfs,
        doc=u"""1 to compute the stator magnetomotive force / stator armature magnetic field""",
    )

    def _get_is_mmfr(self):
        """getter of is_mmfr"""
        return self._is_mmfr

    def _set_is_mmfr(self, value):
        """setter of is_mmfr"""
        check_var("is_mmfr", value, "bool")
        self._is_mmfr = value

    # 1 to compute the rotor magnetomotive force / rotor magnetic field
    # Type : bool
    is_mmfr = property(
        fget=_get_is_mmfr,
        fset=_set_is_mmfr,
        doc=u"""1 to compute the rotor magnetomotive force / rotor magnetic field""",
    )

    def _get_Nt_tot(self):
        """getter of Nt_tot"""
        return self._Nt_tot

    def _set_Nt_tot(self, value):
        """setter of Nt_tot"""
        check_var("Nt_tot", value, "int")
        self._Nt_tot = value

    # Number of time steps for the FEMM simulation
    # Type : int
    Nt_tot = property(
        fget=_get_Nt_tot,
        fset=_set_Nt_tot,
        doc=u"""Number of time steps for the FEMM simulation""",
    )
