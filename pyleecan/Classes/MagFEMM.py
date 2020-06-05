# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/MagFEMM.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Magnetics import Magnetics

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.MagFEMM.comp_flux_airgap import comp_flux_airgap
except ImportError as error:
    comp_flux_airgap = error

try:
    from ..Methods.Simulation.MagFEMM.get_path_save import get_path_save
except ImportError as error:
    get_path_save = error

try:
    from ..Methods.Simulation.MagFEMM.solve_FEMM import solve_FEMM
except ImportError as error:
    solve_FEMM = error

try:
    from ..Methods.Simulation.MagFEMM.get_meshsolution import get_meshsolution
except ImportError as error:
    get_meshsolution = error

try:
    from ..Methods.Simulation.MagFEMM.get_path_save_fem import get_path_save_fem
except ImportError as error:
    get_path_save_fem = error


from ._check import InitUnKnowClassError


class MagFEMM(Magnetics):
    """Magnetic module: Finite Element model with FEMM"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.MagFEMM.comp_flux_airgap
    if isinstance(comp_flux_airgap, ImportError):
        comp_flux_airgap = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagFEMM method comp_flux_airgap: "
                    + str(comp_flux_airgap)
                )
            )
        )
    else:
        comp_flux_airgap = comp_flux_airgap
    # cf Methods.Simulation.MagFEMM.get_path_save
    if isinstance(get_path_save, ImportError):
        get_path_save = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagFEMM method get_path_save: " + str(get_path_save)
                )
            )
        )
    else:
        get_path_save = get_path_save
    # cf Methods.Simulation.MagFEMM.solve_FEMM
    if isinstance(solve_FEMM, ImportError):
        solve_FEMM = property(
            fget=lambda x: raise_(
                ImportError("Can't use MagFEMM method solve_FEMM: " + str(solve_FEMM))
            )
        )
    else:
        solve_FEMM = solve_FEMM
    # cf Methods.Simulation.MagFEMM.get_meshsolution
    if isinstance(get_meshsolution, ImportError):
        get_meshsolution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagFEMM method get_meshsolution: "
                    + str(get_meshsolution)
                )
            )
        )
    else:
        get_meshsolution = get_meshsolution
    # cf Methods.Simulation.MagFEMM.get_path_save_fem
    if isinstance(get_path_save_fem, ImportError):
        get_path_save_fem = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagFEMM method get_path_save_fem: "
                    + str(get_path_save_fem)
                )
            )
        )
    else:
        get_path_save_fem = get_path_save_fem
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Kmesh_fineness=1,
        Kgeo_fineness=1,
        type_calc_leakage=0,
        file_name="",
        FEMM_dict={},
        angle_stator=0,
        is_get_mesh=False,
        is_save_FEA=False,
        is_sliding_band=True,
        transform_list=[],
        is_remove_slotS=False,
        is_remove_slotR=False,
        is_remove_vent=False,
        is_mmfs=True,
        is_mmfr=True,
        type_BH_stator=0,
        type_BH_rotor=0,
        is_symmetry_t=False,
        sym_t=1,
        is_antiper_t=False,
        is_symmetry_a=False,
        sym_a=1,
        is_antiper_a=False,
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Kmesh_fineness" in list(init_dict.keys()):
                Kmesh_fineness = init_dict["Kmesh_fineness"]
            if "Kgeo_fineness" in list(init_dict.keys()):
                Kgeo_fineness = init_dict["Kgeo_fineness"]
            if "type_calc_leakage" in list(init_dict.keys()):
                type_calc_leakage = init_dict["type_calc_leakage"]
            if "file_name" in list(init_dict.keys()):
                file_name = init_dict["file_name"]
            if "FEMM_dict" in list(init_dict.keys()):
                FEMM_dict = init_dict["FEMM_dict"]
            if "angle_stator" in list(init_dict.keys()):
                angle_stator = init_dict["angle_stator"]
            if "is_get_mesh" in list(init_dict.keys()):
                is_get_mesh = init_dict["is_get_mesh"]
            if "is_save_FEA" in list(init_dict.keys()):
                is_save_FEA = init_dict["is_save_FEA"]
            if "is_sliding_band" in list(init_dict.keys()):
                is_sliding_band = init_dict["is_sliding_band"]
            if "transform_list" in list(init_dict.keys()):
                transform_list = init_dict["transform_list"]
            if "is_remove_slotS" in list(init_dict.keys()):
                is_remove_slotS = init_dict["is_remove_slotS"]
            if "is_remove_slotR" in list(init_dict.keys()):
                is_remove_slotR = init_dict["is_remove_slotR"]
            if "is_remove_vent" in list(init_dict.keys()):
                is_remove_vent = init_dict["is_remove_vent"]
            if "is_mmfs" in list(init_dict.keys()):
                is_mmfs = init_dict["is_mmfs"]
            if "is_mmfr" in list(init_dict.keys()):
                is_mmfr = init_dict["is_mmfr"]
            if "type_BH_stator" in list(init_dict.keys()):
                type_BH_stator = init_dict["type_BH_stator"]
            if "type_BH_rotor" in list(init_dict.keys()):
                type_BH_rotor = init_dict["type_BH_rotor"]
            if "is_symmetry_t" in list(init_dict.keys()):
                is_symmetry_t = init_dict["is_symmetry_t"]
            if "sym_t" in list(init_dict.keys()):
                sym_t = init_dict["sym_t"]
            if "is_antiper_t" in list(init_dict.keys()):
                is_antiper_t = init_dict["is_antiper_t"]
            if "is_symmetry_a" in list(init_dict.keys()):
                is_symmetry_a = init_dict["is_symmetry_a"]
            if "sym_a" in list(init_dict.keys()):
                sym_a = init_dict["sym_a"]
            if "is_antiper_a" in list(init_dict.keys()):
                is_antiper_a = init_dict["is_antiper_a"]
        # Initialisation by argument
        self.Kmesh_fineness = Kmesh_fineness
        self.Kgeo_fineness = Kgeo_fineness
        self.type_calc_leakage = type_calc_leakage
        self.file_name = file_name
        self.FEMM_dict = FEMM_dict
        self.angle_stator = angle_stator
        self.is_get_mesh = is_get_mesh
        self.is_save_FEA = is_save_FEA
        self.is_sliding_band = is_sliding_band
        self.transform_list = transform_list
        # Call Magnetics init
        super(MagFEMM, self).__init__(
            is_remove_slotS=is_remove_slotS,
            is_remove_slotR=is_remove_slotR,
            is_remove_vent=is_remove_vent,
            is_mmfs=is_mmfs,
            is_mmfr=is_mmfr,
            type_BH_stator=type_BH_stator,
            type_BH_rotor=type_BH_rotor,
            is_symmetry_t=is_symmetry_t,
            sym_t=sym_t,
            is_antiper_t=is_antiper_t,
            is_symmetry_a=is_symmetry_a,
            sym_a=sym_a,
            is_antiper_a=is_antiper_a,
        )
        # The class is frozen (in Magnetics init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MagFEMM_str = ""
        # Get the properties inherited from Magnetics
        MagFEMM_str += super(MagFEMM, self).__str__()
        MagFEMM_str += "Kmesh_fineness = " + str(self.Kmesh_fineness) + linesep
        MagFEMM_str += "Kgeo_fineness = " + str(self.Kgeo_fineness) + linesep
        MagFEMM_str += "type_calc_leakage = " + str(self.type_calc_leakage) + linesep
        MagFEMM_str += 'file_name = "' + str(self.file_name) + '"' + linesep
        MagFEMM_str += "FEMM_dict = " + str(self.FEMM_dict) + linesep
        MagFEMM_str += "angle_stator = " + str(self.angle_stator) + linesep
        MagFEMM_str += "is_get_mesh = " + str(self.is_get_mesh) + linesep
        MagFEMM_str += "is_save_FEA = " + str(self.is_save_FEA) + linesep
        MagFEMM_str += "is_sliding_band = " + str(self.is_sliding_band) + linesep
        MagFEMM_str += (
            "transform_list = "
            + linesep
            + str(self.transform_list).replace(linesep, linesep + "\t")
            + linesep
        )
        return MagFEMM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Magnetics
        if not super(MagFEMM, self).__eq__(other):
            return False
        if other.Kmesh_fineness != self.Kmesh_fineness:
            return False
        if other.Kgeo_fineness != self.Kgeo_fineness:
            return False
        if other.type_calc_leakage != self.type_calc_leakage:
            return False
        if other.file_name != self.file_name:
            return False
        if other.FEMM_dict != self.FEMM_dict:
            return False
        if other.angle_stator != self.angle_stator:
            return False
        if other.is_get_mesh != self.is_get_mesh:
            return False
        if other.is_save_FEA != self.is_save_FEA:
            return False
        if other.is_sliding_band != self.is_sliding_band:
            return False
        if other.transform_list != self.transform_list:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Magnetics
        MagFEMM_dict = super(MagFEMM, self).as_dict()
        MagFEMM_dict["Kmesh_fineness"] = self.Kmesh_fineness
        MagFEMM_dict["Kgeo_fineness"] = self.Kgeo_fineness
        MagFEMM_dict["type_calc_leakage"] = self.type_calc_leakage
        MagFEMM_dict["file_name"] = self.file_name
        MagFEMM_dict["FEMM_dict"] = self.FEMM_dict
        MagFEMM_dict["angle_stator"] = self.angle_stator
        MagFEMM_dict["is_get_mesh"] = self.is_get_mesh
        MagFEMM_dict["is_save_FEA"] = self.is_save_FEA
        MagFEMM_dict["is_sliding_band"] = self.is_sliding_band
        MagFEMM_dict["transform_list"] = self.transform_list
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MagFEMM_dict["__class__"] = "MagFEMM"
        return MagFEMM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Kmesh_fineness = None
        self.Kgeo_fineness = None
        self.type_calc_leakage = None
        self.file_name = None
        self.FEMM_dict = None
        self.angle_stator = None
        self.is_get_mesh = None
        self.is_save_FEA = None
        self.is_sliding_band = None
        self.transform_list = None
        # Set to None the properties inherited from Magnetics
        super(MagFEMM, self)._set_None()

    def _get_Kmesh_fineness(self):
        """getter of Kmesh_fineness"""
        return self._Kmesh_fineness

    def _set_Kmesh_fineness(self, value):
        """setter of Kmesh_fineness"""
        check_var("Kmesh_fineness", value, "float")
        self._Kmesh_fineness = value

    # global coefficient to adjust mesh fineness in FEMM (1 : default , > 1 : finner , < 1 : less fine)
    # Type : float
    Kmesh_fineness = property(
        fget=_get_Kmesh_fineness,
        fset=_set_Kmesh_fineness,
        doc=u"""global coefficient to adjust mesh fineness in FEMM (1 : default , > 1 : finner , < 1 : less fine)""",
    )

    def _get_Kgeo_fineness(self):
        """getter of Kgeo_fineness"""
        return self._Kgeo_fineness

    def _set_Kgeo_fineness(self, value):
        """setter of Kgeo_fineness"""
        check_var("Kgeo_fineness", value, "float")
        self._Kgeo_fineness = value

    # global coefficient to adjust geometry fineness in FEMM (1 : default , > 1 : finner , < 1 : less fine)
    # Type : float
    Kgeo_fineness = property(
        fget=_get_Kgeo_fineness,
        fset=_set_Kgeo_fineness,
        doc=u"""global coefficient to adjust geometry fineness in FEMM (1 : default , > 1 : finner , < 1 : less fine)""",
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

    def _get_file_name(self):
        """getter of file_name"""
        return self._file_name

    def _set_file_name(self, value):
        """setter of file_name"""
        check_var("file_name", value, "str")
        self._file_name = value

    # Name of the file to save the FEMM model
    # Type : str
    file_name = property(
        fget=_get_file_name,
        fset=_set_file_name,
        doc=u"""Name of the file to save the FEMM model""",
    )

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

    def _get_angle_stator(self):
        """getter of angle_stator"""
        return self._angle_stator

    def _set_angle_stator(self, value):
        """setter of angle_stator"""
        check_var("angle_stator", value, "float")
        self._angle_stator = value

    # Angular position shift of the stator
    # Type : float
    angle_stator = property(
        fget=_get_angle_stator,
        fset=_set_angle_stator,
        doc=u"""Angular position shift of the stator""",
    )

    def _get_is_get_mesh(self):
        """getter of is_get_mesh"""
        return self._is_get_mesh

    def _set_is_get_mesh(self, value):
        """setter of is_get_mesh"""
        check_var("is_get_mesh", value, "bool")
        self._is_get_mesh = value

    # To save FEA mesh for latter post-procesing
    # Type : bool
    is_get_mesh = property(
        fget=_get_is_get_mesh,
        fset=_set_is_get_mesh,
        doc=u"""To save FEA mesh for latter post-procesing """,
    )

    def _get_is_save_FEA(self):
        """getter of is_save_FEA"""
        return self._is_save_FEA

    def _set_is_save_FEA(self, value):
        """setter of is_save_FEA"""
        check_var("is_save_FEA", value, "bool")
        self._is_save_FEA = value

    # To save FEA mesh and solution in .dat file
    # Type : bool
    is_save_FEA = property(
        fget=_get_is_save_FEA,
        fset=_set_is_save_FEA,
        doc=u"""To save FEA mesh and solution in .dat file""",
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

    def _get_transform_list(self):
        """getter of transform_list"""
        return self._transform_list

    def _set_transform_list(self, value):
        """setter of transform_list"""
        check_var("transform_list", value, "list")
        self._transform_list = value

    # List of dictionnary to apply transformation on the machine surfaces. Key: label (to select the surface), type (rotate or translate), value (alpha or delta)
    # Type : list
    transform_list = property(
        fget=_get_transform_list,
        fset=_set_transform_list,
        doc=u"""List of dictionnary to apply transformation on the machine surfaces. Key: label (to select the surface), type (rotate or translate), value (alpha or delta)""",
    )
