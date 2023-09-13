# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/MagFEMM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/MagFEMM
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
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

try:
    from ..Methods.Simulation.MagFEMM.solve_FEMM_parallel import solve_FEMM_parallel
except ImportError as error:
    solve_FEMM_parallel = error

try:
    from ..Methods.Simulation.MagFEMM.build_MS_sliced import build_MS_sliced
except ImportError as error:
    build_MS_sliced = error


from numpy import isnan
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
    # cf Methods.Simulation.MagFEMM.solve_FEMM_parallel
    if isinstance(solve_FEMM_parallel, ImportError):
        solve_FEMM_parallel = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagFEMM method solve_FEMM_parallel: "
                    + str(solve_FEMM_parallel)
                )
            )
        )
    else:
        solve_FEMM_parallel = solve_FEMM_parallel
    # cf Methods.Simulation.MagFEMM.build_MS_sliced
    if isinstance(build_MS_sliced, ImportError):
        build_MS_sliced = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagFEMM method build_MS_sliced: " + str(build_MS_sliced)
                )
            )
        )
    else:
        build_MS_sliced = build_MS_sliced
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Kmesh_fineness=1,
        Kgeo_fineness=1,
        type_calc_leakage=0,
        file_name="",
        FEMM_dict_enforced=-1,
        is_get_meshsolution=False,
        is_save_meshsolution_as_file=False,
        is_sliding_band=True,
        transform_list=-1,
        rotor_dxf=None,
        stator_dxf=None,
        import_file=None,
        is_close_femm=True,
        nb_worker=1,
        Rag_enforced=None,
        is_set_previous=True,
        is_fast_draw=True,
        is_calc_torque_energy=True,
        is_remove_slotS=False,
        is_remove_slotR=False,
        is_remove_ventS=False,
        is_remove_ventR=False,
        is_mmfs=True,
        is_mmfr=True,
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_t=False,
        is_periodicity_a=False,
        angle_stator_shift=0,
        angle_rotor_shift=0,
        logger_name="Pyleecan.Magnetics",
        Slice_enforced=None,
        Nslices_enforced=None,
        type_distribution_enforced=None,
        is_current_harm=True,
        T_mag=20,
        is_periodicity_rotor=False,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
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
            if "FEMM_dict_enforced" in list(init_dict.keys()):
                FEMM_dict_enforced = init_dict["FEMM_dict_enforced"]
            if "is_get_meshsolution" in list(init_dict.keys()):
                is_get_meshsolution = init_dict["is_get_meshsolution"]
            if "is_save_meshsolution_as_file" in list(init_dict.keys()):
                is_save_meshsolution_as_file = init_dict["is_save_meshsolution_as_file"]
            if "is_sliding_band" in list(init_dict.keys()):
                is_sliding_band = init_dict["is_sliding_band"]
            if "transform_list" in list(init_dict.keys()):
                transform_list = init_dict["transform_list"]
            if "rotor_dxf" in list(init_dict.keys()):
                rotor_dxf = init_dict["rotor_dxf"]
            if "stator_dxf" in list(init_dict.keys()):
                stator_dxf = init_dict["stator_dxf"]
            if "import_file" in list(init_dict.keys()):
                import_file = init_dict["import_file"]
            if "is_close_femm" in list(init_dict.keys()):
                is_close_femm = init_dict["is_close_femm"]
            if "nb_worker" in list(init_dict.keys()):
                nb_worker = init_dict["nb_worker"]
            if "Rag_enforced" in list(init_dict.keys()):
                Rag_enforced = init_dict["Rag_enforced"]
            if "is_set_previous" in list(init_dict.keys()):
                is_set_previous = init_dict["is_set_previous"]
            if "is_fast_draw" in list(init_dict.keys()):
                is_fast_draw = init_dict["is_fast_draw"]
            if "is_calc_torque_energy" in list(init_dict.keys()):
                is_calc_torque_energy = init_dict["is_calc_torque_energy"]
            if "is_remove_slotS" in list(init_dict.keys()):
                is_remove_slotS = init_dict["is_remove_slotS"]
            if "is_remove_slotR" in list(init_dict.keys()):
                is_remove_slotR = init_dict["is_remove_slotR"]
            if "is_remove_ventS" in list(init_dict.keys()):
                is_remove_ventS = init_dict["is_remove_ventS"]
            if "is_remove_ventR" in list(init_dict.keys()):
                is_remove_ventR = init_dict["is_remove_ventR"]
            if "is_mmfs" in list(init_dict.keys()):
                is_mmfs = init_dict["is_mmfs"]
            if "is_mmfr" in list(init_dict.keys()):
                is_mmfr = init_dict["is_mmfr"]
            if "type_BH_stator" in list(init_dict.keys()):
                type_BH_stator = init_dict["type_BH_stator"]
            if "type_BH_rotor" in list(init_dict.keys()):
                type_BH_rotor = init_dict["type_BH_rotor"]
            if "is_periodicity_t" in list(init_dict.keys()):
                is_periodicity_t = init_dict["is_periodicity_t"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
            if "angle_stator_shift" in list(init_dict.keys()):
                angle_stator_shift = init_dict["angle_stator_shift"]
            if "angle_rotor_shift" in list(init_dict.keys()):
                angle_rotor_shift = init_dict["angle_rotor_shift"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "Slice_enforced" in list(init_dict.keys()):
                Slice_enforced = init_dict["Slice_enforced"]
            if "Nslices_enforced" in list(init_dict.keys()):
                Nslices_enforced = init_dict["Nslices_enforced"]
            if "type_distribution_enforced" in list(init_dict.keys()):
                type_distribution_enforced = init_dict["type_distribution_enforced"]
            if "is_current_harm" in list(init_dict.keys()):
                is_current_harm = init_dict["is_current_harm"]
            if "T_mag" in list(init_dict.keys()):
                T_mag = init_dict["T_mag"]
            if "is_periodicity_rotor" in list(init_dict.keys()):
                is_periodicity_rotor = init_dict["is_periodicity_rotor"]
        # Set the properties (value check and convertion are done in setter)
        self.Kmesh_fineness = Kmesh_fineness
        self.Kgeo_fineness = Kgeo_fineness
        self.type_calc_leakage = type_calc_leakage
        self.file_name = file_name
        self.FEMM_dict_enforced = FEMM_dict_enforced
        self.is_get_meshsolution = is_get_meshsolution
        self.is_save_meshsolution_as_file = is_save_meshsolution_as_file
        self.is_sliding_band = is_sliding_band
        self.transform_list = transform_list
        self.rotor_dxf = rotor_dxf
        self.stator_dxf = stator_dxf
        self.import_file = import_file
        self.is_close_femm = is_close_femm
        self.nb_worker = nb_worker
        self.Rag_enforced = Rag_enforced
        self.is_set_previous = is_set_previous
        self.is_fast_draw = is_fast_draw
        self.is_calc_torque_energy = is_calc_torque_energy
        # Call Magnetics init
        super(MagFEMM, self).__init__(
            is_remove_slotS=is_remove_slotS,
            is_remove_slotR=is_remove_slotR,
            is_remove_ventS=is_remove_ventS,
            is_remove_ventR=is_remove_ventR,
            is_mmfs=is_mmfs,
            is_mmfr=is_mmfr,
            type_BH_stator=type_BH_stator,
            type_BH_rotor=type_BH_rotor,
            is_periodicity_t=is_periodicity_t,
            is_periodicity_a=is_periodicity_a,
            angle_stator_shift=angle_stator_shift,
            angle_rotor_shift=angle_rotor_shift,
            logger_name=logger_name,
            Slice_enforced=Slice_enforced,
            Nslices_enforced=Nslices_enforced,
            type_distribution_enforced=type_distribution_enforced,
            is_current_harm=is_current_harm,
            T_mag=T_mag,
            is_periodicity_rotor=is_periodicity_rotor,
        )
        # The class is frozen (in Magnetics init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MagFEMM_str = ""
        # Get the properties inherited from Magnetics
        MagFEMM_str += super(MagFEMM, self).__str__()
        MagFEMM_str += "Kmesh_fineness = " + str(self.Kmesh_fineness) + linesep
        MagFEMM_str += "Kgeo_fineness = " + str(self.Kgeo_fineness) + linesep
        MagFEMM_str += "type_calc_leakage = " + str(self.type_calc_leakage) + linesep
        MagFEMM_str += 'file_name = "' + str(self.file_name) + '"' + linesep
        MagFEMM_str += "FEMM_dict_enforced = " + str(self.FEMM_dict_enforced) + linesep
        MagFEMM_str += (
            "is_get_meshsolution = " + str(self.is_get_meshsolution) + linesep
        )
        MagFEMM_str += (
            "is_save_meshsolution_as_file = "
            + str(self.is_save_meshsolution_as_file)
            + linesep
        )
        MagFEMM_str += "is_sliding_band = " + str(self.is_sliding_band) + linesep
        MagFEMM_str += (
            "transform_list = "
            + linesep
            + str(self.transform_list).replace(linesep, linesep + "\t")
            + linesep
        )
        if self.rotor_dxf is not None:
            tmp = self.rotor_dxf.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MagFEMM_str += "rotor_dxf = " + tmp
        else:
            MagFEMM_str += "rotor_dxf = None" + linesep + linesep
        if self.stator_dxf is not None:
            tmp = (
                self.stator_dxf.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            MagFEMM_str += "stator_dxf = " + tmp
        else:
            MagFEMM_str += "stator_dxf = None" + linesep + linesep
        MagFEMM_str += 'import_file = "' + str(self.import_file) + '"' + linesep
        MagFEMM_str += "is_close_femm = " + str(self.is_close_femm) + linesep
        MagFEMM_str += "nb_worker = " + str(self.nb_worker) + linesep
        MagFEMM_str += "Rag_enforced = " + str(self.Rag_enforced) + linesep
        MagFEMM_str += "is_set_previous = " + str(self.is_set_previous) + linesep
        MagFEMM_str += "is_fast_draw = " + str(self.is_fast_draw) + linesep
        MagFEMM_str += (
            "is_calc_torque_energy = " + str(self.is_calc_torque_energy) + linesep
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
        if other.FEMM_dict_enforced != self.FEMM_dict_enforced:
            return False
        if other.is_get_meshsolution != self.is_get_meshsolution:
            return False
        if other.is_save_meshsolution_as_file != self.is_save_meshsolution_as_file:
            return False
        if other.is_sliding_band != self.is_sliding_band:
            return False
        if other.transform_list != self.transform_list:
            return False
        if other.rotor_dxf != self.rotor_dxf:
            return False
        if other.stator_dxf != self.stator_dxf:
            return False
        if other.import_file != self.import_file:
            return False
        if other.is_close_femm != self.is_close_femm:
            return False
        if other.nb_worker != self.nb_worker:
            return False
        if other.Rag_enforced != self.Rag_enforced:
            return False
        if other.is_set_previous != self.is_set_previous:
            return False
        if other.is_fast_draw != self.is_fast_draw:
            return False
        if other.is_calc_torque_energy != self.is_calc_torque_energy:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Magnetics
        diff_list.extend(
            super(MagFEMM, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._Kmesh_fineness is not None
            and self._Kmesh_fineness is not None
            and isnan(other._Kmesh_fineness)
            and isnan(self._Kmesh_fineness)
        ):
            pass
        elif other._Kmesh_fineness != self._Kmesh_fineness:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Kmesh_fineness)
                    + ", other="
                    + str(other._Kmesh_fineness)
                    + ")"
                )
                diff_list.append(name + ".Kmesh_fineness" + val_str)
            else:
                diff_list.append(name + ".Kmesh_fineness")
        if (
            other._Kgeo_fineness is not None
            and self._Kgeo_fineness is not None
            and isnan(other._Kgeo_fineness)
            and isnan(self._Kgeo_fineness)
        ):
            pass
        elif other._Kgeo_fineness != self._Kgeo_fineness:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Kgeo_fineness)
                    + ", other="
                    + str(other._Kgeo_fineness)
                    + ")"
                )
                diff_list.append(name + ".Kgeo_fineness" + val_str)
            else:
                diff_list.append(name + ".Kgeo_fineness")
        if other._type_calc_leakage != self._type_calc_leakage:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._type_calc_leakage)
                    + ", other="
                    + str(other._type_calc_leakage)
                    + ")"
                )
                diff_list.append(name + ".type_calc_leakage" + val_str)
            else:
                diff_list.append(name + ".type_calc_leakage")
        if other._file_name != self._file_name:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._file_name)
                    + ", other="
                    + str(other._file_name)
                    + ")"
                )
                diff_list.append(name + ".file_name" + val_str)
            else:
                diff_list.append(name + ".file_name")
        if other._FEMM_dict_enforced != self._FEMM_dict_enforced:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._FEMM_dict_enforced)
                    + ", other="
                    + str(other._FEMM_dict_enforced)
                    + ")"
                )
                diff_list.append(name + ".FEMM_dict_enforced" + val_str)
            else:
                diff_list.append(name + ".FEMM_dict_enforced")
        if other._is_get_meshsolution != self._is_get_meshsolution:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_get_meshsolution)
                    + ", other="
                    + str(other._is_get_meshsolution)
                    + ")"
                )
                diff_list.append(name + ".is_get_meshsolution" + val_str)
            else:
                diff_list.append(name + ".is_get_meshsolution")
        if other._is_save_meshsolution_as_file != self._is_save_meshsolution_as_file:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_save_meshsolution_as_file)
                    + ", other="
                    + str(other._is_save_meshsolution_as_file)
                    + ")"
                )
                diff_list.append(name + ".is_save_meshsolution_as_file" + val_str)
            else:
                diff_list.append(name + ".is_save_meshsolution_as_file")
        if other._is_sliding_band != self._is_sliding_band:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_sliding_band)
                    + ", other="
                    + str(other._is_sliding_band)
                    + ")"
                )
                diff_list.append(name + ".is_sliding_band" + val_str)
            else:
                diff_list.append(name + ".is_sliding_band")
        if other._transform_list != self._transform_list:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._transform_list)
                    + ", other="
                    + str(other._transform_list)
                    + ")"
                )
                diff_list.append(name + ".transform_list" + val_str)
            else:
                diff_list.append(name + ".transform_list")
        if (other.rotor_dxf is None and self.rotor_dxf is not None) or (
            other.rotor_dxf is not None and self.rotor_dxf is None
        ):
            diff_list.append(name + ".rotor_dxf None mismatch")
        elif self.rotor_dxf is not None:
            diff_list.extend(
                self.rotor_dxf.compare(
                    other.rotor_dxf,
                    name=name + ".rotor_dxf",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.stator_dxf is None and self.stator_dxf is not None) or (
            other.stator_dxf is not None and self.stator_dxf is None
        ):
            diff_list.append(name + ".stator_dxf None mismatch")
        elif self.stator_dxf is not None:
            diff_list.extend(
                self.stator_dxf.compare(
                    other.stator_dxf,
                    name=name + ".stator_dxf",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other._import_file != self._import_file:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._import_file)
                    + ", other="
                    + str(other._import_file)
                    + ")"
                )
                diff_list.append(name + ".import_file" + val_str)
            else:
                diff_list.append(name + ".import_file")
        if other._is_close_femm != self._is_close_femm:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_close_femm)
                    + ", other="
                    + str(other._is_close_femm)
                    + ")"
                )
                diff_list.append(name + ".is_close_femm" + val_str)
            else:
                diff_list.append(name + ".is_close_femm")
        if other._nb_worker != self._nb_worker:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._nb_worker)
                    + ", other="
                    + str(other._nb_worker)
                    + ")"
                )
                diff_list.append(name + ".nb_worker" + val_str)
            else:
                diff_list.append(name + ".nb_worker")
        if (
            other._Rag_enforced is not None
            and self._Rag_enforced is not None
            and isnan(other._Rag_enforced)
            and isnan(self._Rag_enforced)
        ):
            pass
        elif other._Rag_enforced != self._Rag_enforced:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Rag_enforced)
                    + ", other="
                    + str(other._Rag_enforced)
                    + ")"
                )
                diff_list.append(name + ".Rag_enforced" + val_str)
            else:
                diff_list.append(name + ".Rag_enforced")
        if other._is_set_previous != self._is_set_previous:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_set_previous)
                    + ", other="
                    + str(other._is_set_previous)
                    + ")"
                )
                diff_list.append(name + ".is_set_previous" + val_str)
            else:
                diff_list.append(name + ".is_set_previous")
        if other._is_fast_draw != self._is_fast_draw:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_fast_draw)
                    + ", other="
                    + str(other._is_fast_draw)
                    + ")"
                )
                diff_list.append(name + ".is_fast_draw" + val_str)
            else:
                diff_list.append(name + ".is_fast_draw")
        if other._is_calc_torque_energy != self._is_calc_torque_energy:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_calc_torque_energy)
                    + ", other="
                    + str(other._is_calc_torque_energy)
                    + ")"
                )
                diff_list.append(name + ".is_calc_torque_energy" + val_str)
            else:
                diff_list.append(name + ".is_calc_torque_energy")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Magnetics
        S += super(MagFEMM, self).__sizeof__()
        S += getsizeof(self.Kmesh_fineness)
        S += getsizeof(self.Kgeo_fineness)
        S += getsizeof(self.type_calc_leakage)
        S += getsizeof(self.file_name)
        if self.FEMM_dict_enforced is not None:
            for key, value in self.FEMM_dict_enforced.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.is_get_meshsolution)
        S += getsizeof(self.is_save_meshsolution_as_file)
        S += getsizeof(self.is_sliding_band)
        if self.transform_list is not None:
            for value in self.transform_list:
                S += getsizeof(value)
        S += getsizeof(self.rotor_dxf)
        S += getsizeof(self.stator_dxf)
        S += getsizeof(self.import_file)
        S += getsizeof(self.is_close_femm)
        S += getsizeof(self.nb_worker)
        S += getsizeof(self.Rag_enforced)
        S += getsizeof(self.is_set_previous)
        S += getsizeof(self.is_fast_draw)
        S += getsizeof(self.is_calc_torque_energy)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from Magnetics
        MagFEMM_dict = super(MagFEMM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        MagFEMM_dict["Kmesh_fineness"] = self.Kmesh_fineness
        MagFEMM_dict["Kgeo_fineness"] = self.Kgeo_fineness
        MagFEMM_dict["type_calc_leakage"] = self.type_calc_leakage
        MagFEMM_dict["file_name"] = self.file_name
        MagFEMM_dict["FEMM_dict_enforced"] = (
            self.FEMM_dict_enforced.copy()
            if self.FEMM_dict_enforced is not None
            else None
        )
        MagFEMM_dict["is_get_meshsolution"] = self.is_get_meshsolution
        MagFEMM_dict["is_save_meshsolution_as_file"] = self.is_save_meshsolution_as_file
        MagFEMM_dict["is_sliding_band"] = self.is_sliding_band
        MagFEMM_dict["transform_list"] = (
            self.transform_list.copy() if self.transform_list is not None else None
        )
        if self.rotor_dxf is None:
            MagFEMM_dict["rotor_dxf"] = None
        else:
            MagFEMM_dict["rotor_dxf"] = self.rotor_dxf.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.stator_dxf is None:
            MagFEMM_dict["stator_dxf"] = None
        else:
            MagFEMM_dict["stator_dxf"] = self.stator_dxf.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        MagFEMM_dict["import_file"] = self.import_file
        MagFEMM_dict["is_close_femm"] = self.is_close_femm
        MagFEMM_dict["nb_worker"] = self.nb_worker
        MagFEMM_dict["Rag_enforced"] = self.Rag_enforced
        MagFEMM_dict["is_set_previous"] = self.is_set_previous
        MagFEMM_dict["is_fast_draw"] = self.is_fast_draw
        MagFEMM_dict["is_calc_torque_energy"] = self.is_calc_torque_energy
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        MagFEMM_dict["__class__"] = "MagFEMM"
        return MagFEMM_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        Kmesh_fineness_val = self.Kmesh_fineness
        Kgeo_fineness_val = self.Kgeo_fineness
        type_calc_leakage_val = self.type_calc_leakage
        file_name_val = self.file_name
        if self.FEMM_dict_enforced is None:
            FEMM_dict_enforced_val = None
        else:
            FEMM_dict_enforced_val = self.FEMM_dict_enforced.copy()
        is_get_meshsolution_val = self.is_get_meshsolution
        is_save_meshsolution_as_file_val = self.is_save_meshsolution_as_file
        is_sliding_band_val = self.is_sliding_band
        if self.transform_list is None:
            transform_list_val = None
        else:
            transform_list_val = self.transform_list.copy()
        if self.rotor_dxf is None:
            rotor_dxf_val = None
        else:
            rotor_dxf_val = self.rotor_dxf.copy()
        if self.stator_dxf is None:
            stator_dxf_val = None
        else:
            stator_dxf_val = self.stator_dxf.copy()
        import_file_val = self.import_file
        is_close_femm_val = self.is_close_femm
        nb_worker_val = self.nb_worker
        Rag_enforced_val = self.Rag_enforced
        is_set_previous_val = self.is_set_previous
        is_fast_draw_val = self.is_fast_draw
        is_calc_torque_energy_val = self.is_calc_torque_energy
        is_remove_slotS_val = self.is_remove_slotS
        is_remove_slotR_val = self.is_remove_slotR
        is_remove_ventS_val = self.is_remove_ventS
        is_remove_ventR_val = self.is_remove_ventR
        is_mmfs_val = self.is_mmfs
        is_mmfr_val = self.is_mmfr
        type_BH_stator_val = self.type_BH_stator
        type_BH_rotor_val = self.type_BH_rotor
        is_periodicity_t_val = self.is_periodicity_t
        is_periodicity_a_val = self.is_periodicity_a
        angle_stator_shift_val = self.angle_stator_shift
        angle_rotor_shift_val = self.angle_rotor_shift
        logger_name_val = self.logger_name
        if self.Slice_enforced is None:
            Slice_enforced_val = None
        else:
            Slice_enforced_val = self.Slice_enforced.copy()
        Nslices_enforced_val = self.Nslices_enforced
        type_distribution_enforced_val = self.type_distribution_enforced
        is_current_harm_val = self.is_current_harm
        T_mag_val = self.T_mag
        is_periodicity_rotor_val = self.is_periodicity_rotor
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            Kmesh_fineness=Kmesh_fineness_val,
            Kgeo_fineness=Kgeo_fineness_val,
            type_calc_leakage=type_calc_leakage_val,
            file_name=file_name_val,
            FEMM_dict_enforced=FEMM_dict_enforced_val,
            is_get_meshsolution=is_get_meshsolution_val,
            is_save_meshsolution_as_file=is_save_meshsolution_as_file_val,
            is_sliding_band=is_sliding_band_val,
            transform_list=transform_list_val,
            rotor_dxf=rotor_dxf_val,
            stator_dxf=stator_dxf_val,
            import_file=import_file_val,
            is_close_femm=is_close_femm_val,
            nb_worker=nb_worker_val,
            Rag_enforced=Rag_enforced_val,
            is_set_previous=is_set_previous_val,
            is_fast_draw=is_fast_draw_val,
            is_calc_torque_energy=is_calc_torque_energy_val,
            is_remove_slotS=is_remove_slotS_val,
            is_remove_slotR=is_remove_slotR_val,
            is_remove_ventS=is_remove_ventS_val,
            is_remove_ventR=is_remove_ventR_val,
            is_mmfs=is_mmfs_val,
            is_mmfr=is_mmfr_val,
            type_BH_stator=type_BH_stator_val,
            type_BH_rotor=type_BH_rotor_val,
            is_periodicity_t=is_periodicity_t_val,
            is_periodicity_a=is_periodicity_a_val,
            angle_stator_shift=angle_stator_shift_val,
            angle_rotor_shift=angle_rotor_shift_val,
            logger_name=logger_name_val,
            Slice_enforced=Slice_enforced_val,
            Nslices_enforced=Nslices_enforced_val,
            type_distribution_enforced=type_distribution_enforced_val,
            is_current_harm=is_current_harm_val,
            T_mag=T_mag_val,
            is_periodicity_rotor=is_periodicity_rotor_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Kmesh_fineness = None
        self.Kgeo_fineness = None
        self.type_calc_leakage = None
        self.file_name = None
        self.FEMM_dict_enforced = None
        self.is_get_meshsolution = None
        self.is_save_meshsolution_as_file = None
        self.is_sliding_band = None
        self.transform_list = None
        if self.rotor_dxf is not None:
            self.rotor_dxf._set_None()
        if self.stator_dxf is not None:
            self.stator_dxf._set_None()
        self.import_file = None
        self.is_close_femm = None
        self.nb_worker = None
        self.Rag_enforced = None
        self.is_set_previous = None
        self.is_fast_draw = None
        self.is_calc_torque_energy = None
        # Set to None the properties inherited from Magnetics
        super(MagFEMM, self)._set_None()

    def _get_Kmesh_fineness(self):
        """getter of Kmesh_fineness"""
        return self._Kmesh_fineness

    def _set_Kmesh_fineness(self, value):
        """setter of Kmesh_fineness"""
        check_var("Kmesh_fineness", value, "float")
        self._Kmesh_fineness = value

    Kmesh_fineness = property(
        fget=_get_Kmesh_fineness,
        fset=_set_Kmesh_fineness,
        doc=u"""global coefficient to adjust mesh fineness in FEMM (1 : default , > 1 : finner , < 1 : less fine)

        :Type: float
        """,
    )

    def _get_Kgeo_fineness(self):
        """getter of Kgeo_fineness"""
        return self._Kgeo_fineness

    def _set_Kgeo_fineness(self, value):
        """setter of Kgeo_fineness"""
        check_var("Kgeo_fineness", value, "float")
        self._Kgeo_fineness = value

    Kgeo_fineness = property(
        fget=_get_Kgeo_fineness,
        fset=_set_Kgeo_fineness,
        doc=u"""global coefficient to adjust geometry fineness in FEMM (1 : default , > 1 : finner , < 1 : less fine)

        :Type: float
        """,
    )

    def _get_type_calc_leakage(self):
        """getter of type_calc_leakage"""
        return self._type_calc_leakage

    def _set_type_calc_leakage(self, value):
        """setter of type_calc_leakage"""
        check_var("type_calc_leakage", value, "int", Vmin=0, Vmax=1)
        self._type_calc_leakage = value

    type_calc_leakage = property(
        fget=_get_type_calc_leakage,
        fset=_set_type_calc_leakage,
        doc=u"""0 no leakage calculation /  1 calculation using single slot 

        :Type: int
        :min: 0
        :max: 1
        """,
    )

    def _get_file_name(self):
        """getter of file_name"""
        return self._file_name

    def _set_file_name(self, value):
        """setter of file_name"""
        check_var("file_name", value, "str")
        self._file_name = value

    file_name = property(
        fget=_get_file_name,
        fset=_set_file_name,
        doc=u"""Name of the file to save the FEMM model

        :Type: str
        """,
    )

    def _get_FEMM_dict_enforced(self):
        """getter of FEMM_dict_enforced"""
        return self._FEMM_dict_enforced

    def _set_FEMM_dict_enforced(self, value):
        """setter of FEMM_dict_enforced"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("FEMM_dict_enforced", value, "dict")
        self._FEMM_dict_enforced = value

    FEMM_dict_enforced = property(
        fget=_get_FEMM_dict_enforced,
        fset=_set_FEMM_dict_enforced,
        doc=u"""To enforce user-defined values for FEMM main parameters 

        :Type: dict
        """,
    )

    def _get_is_get_meshsolution(self):
        """getter of is_get_meshsolution"""
        return self._is_get_meshsolution

    def _set_is_get_meshsolution(self, value):
        """setter of is_get_meshsolution"""
        check_var("is_get_meshsolution", value, "bool")
        self._is_get_meshsolution = value

    is_get_meshsolution = property(
        fget=_get_is_get_meshsolution,
        fset=_set_is_get_meshsolution,
        doc=u"""To save FEA and mesh for latter post-procesing 

        :Type: bool
        """,
    )

    def _get_is_save_meshsolution_as_file(self):
        """getter of is_save_meshsolution_as_file"""
        return self._is_save_meshsolution_as_file

    def _set_is_save_meshsolution_as_file(self, value):
        """setter of is_save_meshsolution_as_file"""
        check_var("is_save_meshsolution_as_file", value, "bool")
        self._is_save_meshsolution_as_file = value

    is_save_meshsolution_as_file = property(
        fget=_get_is_save_meshsolution_as_file,
        fset=_set_is_save_meshsolution_as_file,
        doc=u"""To save FEA and mesh as h5 files to save memory

        :Type: bool
        """,
    )

    def _get_is_sliding_band(self):
        """getter of is_sliding_band"""
        return self._is_sliding_band

    def _set_is_sliding_band(self, value):
        """setter of is_sliding_band"""
        check_var("is_sliding_band", value, "bool")
        self._is_sliding_band = value

    is_sliding_band = property(
        fget=_get_is_sliding_band,
        fset=_set_is_sliding_band,
        doc=u"""0 to desactivate the sliding band

        :Type: bool
        """,
    )

    def _get_transform_list(self):
        """getter of transform_list"""
        return self._transform_list

    def _set_transform_list(self, value):
        """setter of transform_list"""
        if type(value) is int and value == -1:
            value = list()
        check_var("transform_list", value, "list")
        self._transform_list = value

    transform_list = property(
        fget=_get_transform_list,
        fset=_set_transform_list,
        doc=u"""List of dictionary to apply transformation on the machine surfaces. Key: label (to select the surface), type (rotate or translate), value (alpha or delta)

        :Type: list
        """,
    )

    def _get_rotor_dxf(self):
        """getter of rotor_dxf"""
        return self._rotor_dxf

    def _set_rotor_dxf(self, value):
        """setter of rotor_dxf"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "rotor_dxf"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            DXFImport = import_class("pyleecan.Classes", "DXFImport", "rotor_dxf")
            value = DXFImport()
        check_var("rotor_dxf", value, "DXFImport")
        self._rotor_dxf = value

        if self._rotor_dxf is not None:
            self._rotor_dxf.parent = self

    rotor_dxf = property(
        fget=_get_rotor_dxf,
        fset=_set_rotor_dxf,
        doc=u"""To use a dxf version of the rotor instead of build_geometry

        :Type: DXFImport
        """,
    )

    def _get_stator_dxf(self):
        """getter of stator_dxf"""
        return self._stator_dxf

    def _set_stator_dxf(self, value):
        """setter of stator_dxf"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "stator_dxf"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            DXFImport = import_class("pyleecan.Classes", "DXFImport", "stator_dxf")
            value = DXFImport()
        check_var("stator_dxf", value, "DXFImport")
        self._stator_dxf = value

        if self._stator_dxf is not None:
            self._stator_dxf.parent = self

    stator_dxf = property(
        fget=_get_stator_dxf,
        fset=_set_stator_dxf,
        doc=u"""To use a dxf version of the rotor instead of build_geometry

        :Type: DXFImport
        """,
    )

    def _get_import_file(self):
        """getter of import_file"""
        return self._import_file

    def _set_import_file(self, value):
        """setter of import_file"""
        check_var("import_file", value, "str")
        self._import_file = value

    import_file = property(
        fget=_get_import_file,
        fset=_set_import_file,
        doc=u"""To import an existing femm file

        :Type: str
        """,
    )

    def _get_is_close_femm(self):
        """getter of is_close_femm"""
        return self._is_close_femm

    def _set_is_close_femm(self, value):
        """setter of is_close_femm"""
        check_var("is_close_femm", value, "bool")
        self._is_close_femm = value

    is_close_femm = property(
        fget=_get_is_close_femm,
        fset=_set_is_close_femm,
        doc=u"""To close femm automatically after the simulation

        :Type: bool
        """,
    )

    def _get_nb_worker(self):
        """getter of nb_worker"""
        return self._nb_worker

    def _set_nb_worker(self, value):
        """setter of nb_worker"""
        check_var("nb_worker", value, "int")
        self._nb_worker = value

    nb_worker = property(
        fget=_get_nb_worker,
        fset=_set_nb_worker,
        doc=u"""To run FEMM in parallel (the parallelization is on the time loop)

        :Type: int
        """,
    )

    def _get_Rag_enforced(self):
        """getter of Rag_enforced"""
        return self._Rag_enforced

    def _set_Rag_enforced(self, value):
        """setter of Rag_enforced"""
        check_var("Rag_enforced", value, "float")
        self._Rag_enforced = value

    Rag_enforced = property(
        fget=_get_Rag_enforced,
        fset=_set_Rag_enforced,
        doc=u"""To enforce a different radius value for air-gap outputs

        :Type: float
        """,
    )

    def _get_is_set_previous(self):
        """getter of is_set_previous"""
        return self._is_set_previous

    def _set_is_set_previous(self, value):
        """setter of is_set_previous"""
        check_var("is_set_previous", value, "bool")
        self._is_set_previous = value

    is_set_previous = property(
        fget=_get_is_set_previous,
        fset=_set_is_set_previous,
        doc=u"""True set previous .ans result file in current .fem to use it as initialization and speed up calculation time

        :Type: bool
        """,
    )

    def _get_is_fast_draw(self):
        """getter of is_fast_draw"""
        return self._is_fast_draw

    def _set_is_fast_draw(self, value):
        """setter of is_fast_draw"""
        check_var("is_fast_draw", value, "bool")
        self._is_fast_draw = value

    is_fast_draw = property(
        fget=_get_is_fast_draw,
        fset=_set_is_fast_draw,
        doc=u"""True to use the symetry of the lamination to draw the machine faster

        :Type: bool
        """,
    )

    def _get_is_calc_torque_energy(self):
        """getter of is_calc_torque_energy"""
        return self._is_calc_torque_energy

    def _set_is_calc_torque_energy(self, value):
        """setter of is_calc_torque_energy"""
        check_var("is_calc_torque_energy", value, "bool")
        self._is_calc_torque_energy = value

    is_calc_torque_energy = property(
        fget=_get_is_calc_torque_energy,
        fset=_set_is_calc_torque_energy,
        doc=u"""True to calculate torque from integration of energy derivate over rotor elements

        :Type: bool
        """,
    )
