# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/StructElmer.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/StructElmer
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Structural import Structural

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.StructElmer.run import run
except ImportError as error:
    run = error

try:
    from ..Methods.Simulation.StructElmer.get_meshsolution import get_meshsolution
except ImportError as error:
    get_meshsolution = error

try:
    from ..Methods.Simulation.StructElmer.get_path_save_fea import get_path_save_fea
except ImportError as error:
    get_path_save_fea = error

try:
    from ..Methods.Simulation.StructElmer.solve_FEA import solve_FEA
except ImportError as error:
    solve_FEA = error

try:
    from ..Methods.Simulation.StructElmer.init_model import init_model
except ImportError as error:
    init_model = error


from ._check import InitUnKnowClassError


class StructElmer(Structural):
    """Structural module: FEA model with Elmer"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.StructElmer.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use StructElmer method run: " + str(run))
            )
        )
    else:
        run = run
    # cf Methods.Simulation.StructElmer.get_meshsolution
    if isinstance(get_meshsolution, ImportError):
        get_meshsolution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use StructElmer method get_meshsolution: "
                    + str(get_meshsolution)
                )
            )
        )
    else:
        get_meshsolution = get_meshsolution
    # cf Methods.Simulation.StructElmer.get_path_save_fea
    if isinstance(get_path_save_fea, ImportError):
        get_path_save_fea = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use StructElmer method get_path_save_fea: "
                    + str(get_path_save_fea)
                )
            )
        )
    else:
        get_path_save_fea = get_path_save_fea
    # cf Methods.Simulation.StructElmer.solve_FEA
    if isinstance(solve_FEA, ImportError):
        solve_FEA = property(
            fget=lambda x: raise_(
                ImportError("Can't use StructElmer method solve_FEA: " + str(solve_FEA))
            )
        )
    else:
        solve_FEA = solve_FEA
    # cf Methods.Simulation.StructElmer.init_model
    if isinstance(init_model, ImportError):
        init_model = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use StructElmer method init_model: " + str(init_model)
                )
            )
        )
    else:
        init_model = init_model
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Kmesh_fineness=1,
        file_name="",
        FEMM_dict_enforced=-1,
        is_get_mesh=False,
        is_save_FEA=False,
        transform_list=-1,
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
            if "Kmesh_fineness" in list(init_dict.keys()):
                Kmesh_fineness = init_dict["Kmesh_fineness"]
            if "file_name" in list(init_dict.keys()):
                file_name = init_dict["file_name"]
            if "FEMM_dict_enforced" in list(init_dict.keys()):
                FEMM_dict_enforced = init_dict["FEMM_dict_enforced"]
            if "is_get_mesh" in list(init_dict.keys()):
                is_get_mesh = init_dict["is_get_mesh"]
            if "is_save_FEA" in list(init_dict.keys()):
                is_save_FEA = init_dict["is_save_FEA"]
            if "transform_list" in list(init_dict.keys()):
                transform_list = init_dict["transform_list"]
        # Set the properties (value check and convertion are done in setter)
        self.Kmesh_fineness = Kmesh_fineness
        self.file_name = file_name
        self.FEMM_dict_enforced = FEMM_dict_enforced
        self.is_get_mesh = is_get_mesh
        self.is_save_FEA = is_save_FEA
        self.transform_list = transform_list
        # Call Structural init
        super(StructElmer, self).__init__()
        # The class is frozen (in Structural init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        StructElmer_str = ""
        # Get the properties inherited from Structural
        StructElmer_str += super(StructElmer, self).__str__()
        StructElmer_str += "Kmesh_fineness = " + str(self.Kmesh_fineness) + linesep
        StructElmer_str += 'file_name = "' + str(self.file_name) + '"' + linesep
        StructElmer_str += (
            "FEMM_dict_enforced = " + str(self.FEMM_dict_enforced) + linesep
        )
        StructElmer_str += "is_get_mesh = " + str(self.is_get_mesh) + linesep
        StructElmer_str += "is_save_FEA = " + str(self.is_save_FEA) + linesep
        StructElmer_str += (
            "transform_list = "
            + linesep
            + str(self.transform_list).replace(linesep, linesep + "\t")
            + linesep
        )
        return StructElmer_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Structural
        if not super(StructElmer, self).__eq__(other):
            return False
        if other.Kmesh_fineness != self.Kmesh_fineness:
            return False
        if other.file_name != self.file_name:
            return False
        if other.FEMM_dict_enforced != self.FEMM_dict_enforced:
            return False
        if other.is_get_mesh != self.is_get_mesh:
            return False
        if other.is_save_FEA != self.is_save_FEA:
            return False
        if other.transform_list != self.transform_list:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from Structural
        StructElmer_dict = super(StructElmer, self).as_dict()
        StructElmer_dict["Kmesh_fineness"] = self.Kmesh_fineness
        StructElmer_dict["file_name"] = self.file_name
        StructElmer_dict["FEMM_dict_enforced"] = (
            self.FEMM_dict_enforced.copy()
            if self.FEMM_dict_enforced is not None
            else None
        )
        StructElmer_dict["is_get_mesh"] = self.is_get_mesh
        StructElmer_dict["is_save_FEA"] = self.is_save_FEA
        StructElmer_dict["transform_list"] = (
            self.transform_list.copy() if self.transform_list is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        StructElmer_dict["__class__"] = "StructElmer"
        return StructElmer_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Kmesh_fineness = None
        self.file_name = None
        self.FEMM_dict_enforced = None
        self.is_get_mesh = None
        self.is_save_FEA = None
        self.transform_list = None
        # Set to None the properties inherited from Structural
        super(StructElmer, self)._set_None()

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
        doc=u"""Name of the file to save the FEA model

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
        doc=u"""To enforce user-defined values for FEA main parameters 

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
        doc=u"""To save FEA mesh and solution in .vtu file

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
        doc=u"""List of dictionnary to apply transformation on the machine surfaces. Key: label (to select the surface), type (rotate or translate), value (alpha or delta)

        :Type: list
        """,
    )
