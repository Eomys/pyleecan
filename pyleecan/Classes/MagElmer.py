# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/MagElmer.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/MagElmer
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Magnetics import Magnetics

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.MagElmer.comp_flux_airgap import comp_flux_airgap
except ImportError as error:
    comp_flux_airgap = error

try:
    from ..Methods.Simulation.MagElmer.solve_FEA import solve_FEA
except ImportError as error:
    solve_FEA = error

try:
    from ..Methods.Simulation.MagElmer.get_meshsolution import get_meshsolution
except ImportError as error:
    get_meshsolution = error

try:
    from ..Methods.Simulation.MagElmer.get_path_save_fea import get_path_save_fea
except ImportError as error:
    get_path_save_fea = error

try:
    from ..Methods.Simulation.MagElmer.get_path_save import get_path_save
except ImportError as error:
    get_path_save = error

try:
    from ..Methods.Simulation.MagElmer.comp_axes import comp_axes
except ImportError as error:
    comp_axes = error

try:
    from ..Methods.Simulation.MagElmer.gen_elmer_mesh import gen_elmer_mesh
except ImportError as error:
    gen_elmer_mesh = error


from ._check import InitUnKnowClassError
from .DXFImport import DXFImport


class MagElmer(Magnetics):
    """Magnetic module: Finite Element model with Elmer"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.MagElmer.comp_flux_airgap
    if isinstance(comp_flux_airgap, ImportError):
        comp_flux_airgap = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagElmer method comp_flux_airgap: "
                    + str(comp_flux_airgap)
                )
            )
        )
    else:
        comp_flux_airgap = comp_flux_airgap
    # cf Methods.Simulation.MagElmer.solve_FEA
    if isinstance(solve_FEA, ImportError):
        solve_FEA = property(
            fget=lambda x: raise_(
                ImportError("Can't use MagElmer method solve_FEA: " + str(solve_FEA))
            )
        )
    else:
        solve_FEA = solve_FEA
    # cf Methods.Simulation.MagElmer.get_meshsolution
    if isinstance(get_meshsolution, ImportError):
        get_meshsolution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagElmer method get_meshsolution: "
                    + str(get_meshsolution)
                )
            )
        )
    else:
        get_meshsolution = get_meshsolution
    # cf Methods.Simulation.MagElmer.get_path_save_fea
    if isinstance(get_path_save_fea, ImportError):
        get_path_save_fea = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagElmer method get_path_save_fea: "
                    + str(get_path_save_fea)
                )
            )
        )
    else:
        get_path_save_fea = get_path_save_fea
    # cf Methods.Simulation.MagElmer.get_path_save
    if isinstance(get_path_save, ImportError):
        get_path_save = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagElmer method get_path_save: " + str(get_path_save)
                )
            )
        )
    else:
        get_path_save = get_path_save
    # cf Methods.Simulation.MagElmer.comp_axes
    if isinstance(comp_axes, ImportError):
        comp_axes = property(
            fget=lambda x: raise_(
                ImportError("Can't use MagElmer method comp_axes: " + str(comp_axes))
            )
        )
    else:
        comp_axes = comp_axes
    # cf Methods.Simulation.MagElmer.gen_elmer_mesh
    if isinstance(gen_elmer_mesh, ImportError):
        gen_elmer_mesh = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagElmer method gen_elmer_mesh: " + str(gen_elmer_mesh)
                )
            )
        )
    else:
        gen_elmer_mesh = gen_elmer_mesh
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Kmesh_fineness=1,
        Kgeo_fineness=1,
        file_name="",
        FEA_dict=-1,
        is_get_mesh=False,
        is_save_FEA=False,
        transform_list=-1,
        rotor_dxf=None,
        stator_dxf=None,
        import_file="",
        nb_worker=1,
        is_remove_slotS=False,
        is_remove_slotR=False,
        is_remove_vent=False,
        is_mmfs=True,
        is_mmfr=True,
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_t=False,
        is_periodicity_a=False,
        angle_stator_shift=0,
        angle_rotor_shift=0,
        logger_name="Pyleecan.Magnetics",
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
            if "file_name" in list(init_dict.keys()):
                file_name = init_dict["file_name"]
            if "FEA_dict" in list(init_dict.keys()):
                FEA_dict = init_dict["FEA_dict"]
            if "is_get_mesh" in list(init_dict.keys()):
                is_get_mesh = init_dict["is_get_mesh"]
            if "is_save_FEA" in list(init_dict.keys()):
                is_save_FEA = init_dict["is_save_FEA"]
            if "transform_list" in list(init_dict.keys()):
                transform_list = init_dict["transform_list"]
            if "rotor_dxf" in list(init_dict.keys()):
                rotor_dxf = init_dict["rotor_dxf"]
            if "stator_dxf" in list(init_dict.keys()):
                stator_dxf = init_dict["stator_dxf"]
            if "import_file" in list(init_dict.keys()):
                import_file = init_dict["import_file"]
            if "nb_worker" in list(init_dict.keys()):
                nb_worker = init_dict["nb_worker"]
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
        # Set the properties (value check and convertion are done in setter)
        self.Kmesh_fineness = Kmesh_fineness
        self.Kgeo_fineness = Kgeo_fineness
        self.file_name = file_name
        self.FEA_dict = FEA_dict
        self.is_get_mesh = is_get_mesh
        self.is_save_FEA = is_save_FEA
        self.transform_list = transform_list
        self.rotor_dxf = rotor_dxf
        self.stator_dxf = stator_dxf
        self.import_file = import_file
        self.nb_worker = nb_worker
        # Call Magnetics init
        super(MagElmer, self).__init__(
            is_remove_slotS=is_remove_slotS,
            is_remove_slotR=is_remove_slotR,
            is_remove_vent=is_remove_vent,
            is_mmfs=is_mmfs,
            is_mmfr=is_mmfr,
            type_BH_stator=type_BH_stator,
            type_BH_rotor=type_BH_rotor,
            is_periodicity_t=is_periodicity_t,
            is_periodicity_a=is_periodicity_a,
            angle_stator_shift=angle_stator_shift,
            angle_rotor_shift=angle_rotor_shift,
            logger_name=logger_name,
        )
        # The class is frozen (in Magnetics init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MagElmer_str = ""
        # Get the properties inherited from Magnetics
        MagElmer_str += super(MagElmer, self).__str__()
        MagElmer_str += "Kmesh_fineness = " + str(self.Kmesh_fineness) + linesep
        MagElmer_str += "Kgeo_fineness = " + str(self.Kgeo_fineness) + linesep
        MagElmer_str += 'file_name = "' + str(self.file_name) + '"' + linesep
        MagElmer_str += "FEA_dict = " + str(self.FEA_dict) + linesep
        MagElmer_str += "is_get_mesh = " + str(self.is_get_mesh) + linesep
        MagElmer_str += "is_save_FEA = " + str(self.is_save_FEA) + linesep
        MagElmer_str += (
            "transform_list = "
            + linesep
            + str(self.transform_list).replace(linesep, linesep + "\t")
            + linesep
        )
        if self.rotor_dxf is not None:
            tmp = self.rotor_dxf.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MagElmer_str += "rotor_dxf = " + tmp
        else:
            MagElmer_str += "rotor_dxf = None" + linesep + linesep
        if self.stator_dxf is not None:
            tmp = (
                self.stator_dxf.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            MagElmer_str += "stator_dxf = " + tmp
        else:
            MagElmer_str += "stator_dxf = None" + linesep + linesep
        MagElmer_str += 'import_file = "' + str(self.import_file) + '"' + linesep
        MagElmer_str += "nb_worker = " + str(self.nb_worker) + linesep
        return MagElmer_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Magnetics
        if not super(MagElmer, self).__eq__(other):
            return False
        if other.Kmesh_fineness != self.Kmesh_fineness:
            return False
        if other.Kgeo_fineness != self.Kgeo_fineness:
            return False
        if other.file_name != self.file_name:
            return False
        if other.FEA_dict != self.FEA_dict:
            return False
        if other.is_get_mesh != self.is_get_mesh:
            return False
        if other.is_save_FEA != self.is_save_FEA:
            return False
        if other.transform_list != self.transform_list:
            return False
        if other.rotor_dxf != self.rotor_dxf:
            return False
        if other.stator_dxf != self.stator_dxf:
            return False
        if other.import_file != self.import_file:
            return False
        if other.nb_worker != self.nb_worker:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Magnetics
        diff_list.extend(super(MagElmer, self).compare(other, name=name))
        if other._Kmesh_fineness != self._Kmesh_fineness:
            diff_list.append(name + ".Kmesh_fineness")
        if other._Kgeo_fineness != self._Kgeo_fineness:
            diff_list.append(name + ".Kgeo_fineness")
        if other._file_name != self._file_name:
            diff_list.append(name + ".file_name")
        if other._FEA_dict != self._FEA_dict:
            diff_list.append(name + ".FEA_dict")
        if other._is_get_mesh != self._is_get_mesh:
            diff_list.append(name + ".is_get_mesh")
        if other._is_save_FEA != self._is_save_FEA:
            diff_list.append(name + ".is_save_FEA")
        if other._transform_list != self._transform_list:
            diff_list.append(name + ".transform_list")
        if (other.rotor_dxf is None and self.rotor_dxf is not None) or (
            other.rotor_dxf is not None and self.rotor_dxf is None
        ):
            diff_list.append(name + ".rotor_dxf None mismatch")
        elif self.rotor_dxf is not None:
            diff_list.extend(
                self.rotor_dxf.compare(other.rotor_dxf, name=name + ".rotor_dxf")
            )
        if (other.stator_dxf is None and self.stator_dxf is not None) or (
            other.stator_dxf is not None and self.stator_dxf is None
        ):
            diff_list.append(name + ".stator_dxf None mismatch")
        elif self.stator_dxf is not None:
            diff_list.extend(
                self.stator_dxf.compare(other.stator_dxf, name=name + ".stator_dxf")
            )
        if other._import_file != self._import_file:
            diff_list.append(name + ".import_file")
        if other._nb_worker != self._nb_worker:
            diff_list.append(name + ".nb_worker")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Magnetics
        S += super(MagElmer, self).__sizeof__()
        S += getsizeof(self.Kmesh_fineness)
        S += getsizeof(self.Kgeo_fineness)
        S += getsizeof(self.file_name)
        if self.FEA_dict is not None:
            for key, value in self.FEA_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.is_get_mesh)
        S += getsizeof(self.is_save_FEA)
        if self.transform_list is not None:
            for value in self.transform_list:
                S += getsizeof(value)
        S += getsizeof(self.rotor_dxf)
        S += getsizeof(self.stator_dxf)
        S += getsizeof(self.import_file)
        S += getsizeof(self.nb_worker)
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
        MagElmer_dict = super(MagElmer, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        MagElmer_dict["Kmesh_fineness"] = self.Kmesh_fineness
        MagElmer_dict["Kgeo_fineness"] = self.Kgeo_fineness
        MagElmer_dict["file_name"] = self.file_name
        MagElmer_dict["FEA_dict"] = (
            self.FEA_dict.copy() if self.FEA_dict is not None else None
        )
        MagElmer_dict["is_get_mesh"] = self.is_get_mesh
        MagElmer_dict["is_save_FEA"] = self.is_save_FEA
        MagElmer_dict["transform_list"] = (
            self.transform_list.copy() if self.transform_list is not None else None
        )
        if self.rotor_dxf is None:
            MagElmer_dict["rotor_dxf"] = None
        else:
            MagElmer_dict["rotor_dxf"] = self.rotor_dxf.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.stator_dxf is None:
            MagElmer_dict["stator_dxf"] = None
        else:
            MagElmer_dict["stator_dxf"] = self.stator_dxf.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        MagElmer_dict["import_file"] = self.import_file
        MagElmer_dict["nb_worker"] = self.nb_worker
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        MagElmer_dict["__class__"] = "MagElmer"
        return MagElmer_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Kmesh_fineness = None
        self.Kgeo_fineness = None
        self.file_name = None
        self.FEA_dict = None
        self.is_get_mesh = None
        self.is_save_FEA = None
        self.transform_list = None
        if self.rotor_dxf is not None:
            self.rotor_dxf._set_None()
        if self.stator_dxf is not None:
            self.stator_dxf._set_None()
        self.import_file = None
        self.nb_worker = None
        # Set to None the properties inherited from Magnetics
        super(MagElmer, self)._set_None()

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
        doc=u"""global coefficient to adjust mesh fineness (1 : default , > 1 : finner , < 1 : less fine)

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
        doc=u"""global coefficient to adjust geometry fineness (1 : default , > 1 : finner , < 1 : less fine)

        :Type: float
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
        doc=u"""Name of the file to save the Elmer model

        :Type: str
        """,
    )

    def _get_FEA_dict(self):
        """getter of FEA_dict"""
        return self._FEA_dict

    def _set_FEA_dict(self, value):
        """setter of FEA_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("FEA_dict", value, "dict")
        self._FEA_dict = value

    FEA_dict = property(
        fget=_get_FEA_dict,
        fset=_set_FEA_dict,
        doc=u"""To enforce user-defined values for Elmer main parameters 

        :Type: dict
        """,
    )

    def _get_is_get_mesh(self):
        """getter of is_get_mesh"""
        return self._is_get_mesh

    def _set_is_get_mesh(self, value):
        """setter of is_get_mesh"""
        check_var("is_get_mesh", value, "bool")
        self._is_get_mesh = value

    is_get_mesh = property(
        fget=_get_is_get_mesh,
        fset=_set_is_get_mesh,
        doc=u"""To save FEA mesh for latter post-procesing 

        :Type: bool
        """,
    )

    def _get_is_save_FEA(self):
        """getter of is_save_FEA"""
        return self._is_save_FEA

    def _set_is_save_FEA(self, value):
        """setter of is_save_FEA"""
        check_var("is_save_FEA", value, "bool")
        self._is_save_FEA = value

    is_save_FEA = property(
        fget=_get_is_save_FEA,
        fset=_set_is_save_FEA,
        doc=u"""To save FEA mesh and solution in a file

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
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "rotor_dxf"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
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
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "stator_dxf"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
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
        doc=u"""To import an existing simulation file

        :Type: str
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
        doc=u"""To run Elmer in parallel (the parallelization is on the time loop)

        :Type: int
        """,
    )
