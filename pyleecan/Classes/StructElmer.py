# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/StructElmer.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/StructElmer
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
    from ..Methods.Simulation.StructElmer.gen_mesh import gen_mesh
except ImportError as error:
    gen_mesh = error

try:
    from ..Methods.Simulation.StructElmer.gen_case import gen_case
except ImportError as error:
    gen_case = error

try:
    from ..Methods.Simulation.StructElmer.process_mesh import process_mesh
except ImportError as error:
    process_mesh = error


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
    # cf Methods.Simulation.StructElmer.gen_mesh
    if isinstance(gen_mesh, ImportError):
        gen_mesh = property(
            fget=lambda x: raise_(
                ImportError("Can't use StructElmer method gen_mesh: " + str(gen_mesh))
            )
        )
    else:
        gen_mesh = gen_mesh
    # cf Methods.Simulation.StructElmer.gen_case
    if isinstance(gen_case, ImportError):
        gen_case = property(
            fget=lambda x: raise_(
                ImportError("Can't use StructElmer method gen_case: " + str(gen_case))
            )
        )
    else:
        gen_case = gen_case
    # cf Methods.Simulation.StructElmer.process_mesh
    if isinstance(process_mesh, ImportError):
        process_mesh = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use StructElmer method process_mesh: " + str(process_mesh)
                )
            )
        )
    else:
        process_mesh = process_mesh
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Kmesh_fineness=1,
        path_name="",
        FEA_dict_enforced=-1,
        is_get_mesh=False,
        is_save_FEA=True,
        transform_list=-1,
        include_magnets=True,
        logger_name="Pyleecan.Structural",
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
            if "path_name" in list(init_dict.keys()):
                path_name = init_dict["path_name"]
            if "FEA_dict_enforced" in list(init_dict.keys()):
                FEA_dict_enforced = init_dict["FEA_dict_enforced"]
            if "is_get_mesh" in list(init_dict.keys()):
                is_get_mesh = init_dict["is_get_mesh"]
            if "is_save_FEA" in list(init_dict.keys()):
                is_save_FEA = init_dict["is_save_FEA"]
            if "transform_list" in list(init_dict.keys()):
                transform_list = init_dict["transform_list"]
            if "include_magnets" in list(init_dict.keys()):
                include_magnets = init_dict["include_magnets"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.Kmesh_fineness = Kmesh_fineness
        self.path_name = path_name
        self.FEA_dict_enforced = FEA_dict_enforced
        self.is_get_mesh = is_get_mesh
        self.is_save_FEA = is_save_FEA
        self.transform_list = transform_list
        self.include_magnets = include_magnets
        # Call Structural init
        super(StructElmer, self).__init__(logger_name=logger_name)
        # The class is frozen (in Structural init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        StructElmer_str = ""
        # Get the properties inherited from Structural
        StructElmer_str += super(StructElmer, self).__str__()
        StructElmer_str += "Kmesh_fineness = " + str(self.Kmesh_fineness) + linesep
        StructElmer_str += 'path_name = "' + str(self.path_name) + '"' + linesep
        StructElmer_str += (
            "FEA_dict_enforced = " + str(self.FEA_dict_enforced) + linesep
        )
        StructElmer_str += "is_get_mesh = " + str(self.is_get_mesh) + linesep
        StructElmer_str += "is_save_FEA = " + str(self.is_save_FEA) + linesep
        StructElmer_str += (
            "transform_list = "
            + linesep
            + str(self.transform_list).replace(linesep, linesep + "\t")
            + linesep
        )
        StructElmer_str += "include_magnets = " + str(self.include_magnets) + linesep
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
        if other.path_name != self.path_name:
            return False
        if other.FEA_dict_enforced != self.FEA_dict_enforced:
            return False
        if other.is_get_mesh != self.is_get_mesh:
            return False
        if other.is_save_FEA != self.is_save_FEA:
            return False
        if other.transform_list != self.transform_list:
            return False
        if other.include_magnets != self.include_magnets:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Structural
        diff_list.extend(super(StructElmer, self).compare(other, name=name))
        if other._Kmesh_fineness != self._Kmesh_fineness:
            diff_list.append(name + ".Kmesh_fineness")
        if other._path_name != self._path_name:
            diff_list.append(name + ".path_name")
        if other._FEA_dict_enforced != self._FEA_dict_enforced:
            diff_list.append(name + ".FEA_dict_enforced")
        if other._is_get_mesh != self._is_get_mesh:
            diff_list.append(name + ".is_get_mesh")
        if other._is_save_FEA != self._is_save_FEA:
            diff_list.append(name + ".is_save_FEA")
        if other._transform_list != self._transform_list:
            diff_list.append(name + ".transform_list")
        if other._include_magnets != self._include_magnets:
            diff_list.append(name + ".include_magnets")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Structural
        S += super(StructElmer, self).__sizeof__()
        S += getsizeof(self.Kmesh_fineness)
        S += getsizeof(self.path_name)
        if self.FEA_dict_enforced is not None:
            for key, value in self.FEA_dict_enforced.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.is_get_mesh)
        S += getsizeof(self.is_save_FEA)
        if self.transform_list is not None:
            for value in self.transform_list:
                S += getsizeof(value)
        S += getsizeof(self.include_magnets)
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

        # Get the properties inherited from Structural
        StructElmer_dict = super(StructElmer, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        StructElmer_dict["Kmesh_fineness"] = self.Kmesh_fineness
        StructElmer_dict["path_name"] = self.path_name
        StructElmer_dict["FEA_dict_enforced"] = (
            self.FEA_dict_enforced.copy()
            if self.FEA_dict_enforced is not None
            else None
        )
        StructElmer_dict["is_get_mesh"] = self.is_get_mesh
        StructElmer_dict["is_save_FEA"] = self.is_save_FEA
        StructElmer_dict["transform_list"] = (
            self.transform_list.copy() if self.transform_list is not None else None
        )
        StructElmer_dict["include_magnets"] = self.include_magnets
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        StructElmer_dict["__class__"] = "StructElmer"
        return StructElmer_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Kmesh_fineness = None
        self.path_name = None
        self.FEA_dict_enforced = None
        self.is_get_mesh = None
        self.is_save_FEA = None
        self.transform_list = None
        self.include_magnets = None
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

    def _get_path_name(self):
        """getter of path_name"""
        return self._path_name

    def _set_path_name(self, value):
        """setter of path_name"""
        check_var("path_name", value, "str")
        self._path_name = value

    path_name = property(
        fget=_get_path_name,
        fset=_set_path_name,
        doc=u"""Name of the path to save the FEA model

        :Type: str
        """,
    )

    def _get_FEA_dict_enforced(self):
        """getter of FEA_dict_enforced"""
        return self._FEA_dict_enforced

    def _set_FEA_dict_enforced(self, value):
        """setter of FEA_dict_enforced"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("FEA_dict_enforced", value, "dict")
        self._FEA_dict_enforced = value

    FEA_dict_enforced = property(
        fget=_get_FEA_dict_enforced,
        fset=_set_FEA_dict_enforced,
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
        doc=u"""To save FEA mesh for latter post-procesing (only possible with is_save_FEA set to True)

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
        doc=u"""List of dictionary to apply transformation on the machine surfaces. Key: label (to select the surface), type (rotate or translate), value (alpha or delta)

        :Type: list
        """,
    )

    def _get_include_magnets(self):
        """getter of include_magnets"""
        return self._include_magnets

    def _set_include_magnets(self, value):
        """setter of include_magnets"""
        check_var("include_magnets", value, "bool")
        self._include_magnets = value

    include_magnets = property(
        fget=_get_include_magnets,
        fset=_set_include_magnets,
        doc=u"""Switch to include magents in the structural simulation

        :Type: bool
        """,
    )
