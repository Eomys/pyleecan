# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Mesh/MeshSolution.csv
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
    from ..Methods.Mesh.MeshSolution.get_mesh import get_mesh
except ImportError as error:
    get_mesh = error

try:
    from ..Methods.Mesh.MeshSolution.get_solution import get_solution
except ImportError as error:
    get_solution = error


from ._check import InitUnKnowClassError
from .Mesh import Mesh


class MeshSolution(FrozenClass):
    """To associate a Mesh with one or several solutions"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.MeshSolution.get_mesh
    if isinstance(get_mesh, ImportError):
        get_mesh = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshSolution method get_mesh: " + str(get_mesh))
            )
        )
    else:
        get_mesh = get_mesh
    # cf Methods.Mesh.MeshSolution.get_solution
    if isinstance(get_solution, ImportError):
        get_solution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method get_solution: " + str(get_solution)
                )
            )
        )
    else:
        get_solution = get_solution
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
        name="",
        mesh=list(),
        soldict={},
        is_same_mesh=True,
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
            name = obj.name
            mesh = obj.mesh
            soldict = obj.soldict
            is_same_mesh = obj.is_same_mesh
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "mesh" in list(init_dict.keys()):
                mesh = init_dict["mesh"]
            if "soldict" in list(init_dict.keys()):
                soldict = init_dict["soldict"]
            if "is_same_mesh" in list(init_dict.keys()):
                is_same_mesh = init_dict["is_same_mesh"]
        # Initialisation by argument
        self.parent = None
        self.name = name
        # mesh can be None or a list of Mesh object
        self.mesh = list()
        if type(mesh) is list:
            for obj in mesh:
                if obj is None:  # Default value
                    self.mesh.append(Mesh())
                elif isinstance(obj, dict):
                    # Check that the type is correct (including daughter)
                    class_name = obj.get("__class__")
                    if class_name not in ["Mesh", "MeshVTK"]:
                        raise InitUnKnowClassError(
                            "Unknow class name " + class_name + " in init_dict for mesh"
                        )
                    # Dynamic import to call the correct constructor
                    module = __import__(
                        "pyleecan.Classes." + class_name, fromlist=[class_name]
                    )
                    class_obj = getattr(module, class_name)
                    self.mesh.append(class_obj(init_dict=obj))
                else:
                    self.mesh.append(obj)
        elif mesh is None:
            self.mesh = list()
        else:
            self.mesh = mesh
        self.soldict = soldict
        self.is_same_mesh = is_same_mesh

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MeshSolution_str = ""
        if self.parent is None:
            MeshSolution_str += "parent = None " + linesep
        else:
            MeshSolution_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        MeshSolution_str += 'name = "' + str(self.name) + '"' + linesep
        if len(self.mesh) == 0:
            MeshSolution_str += "mesh = []" + linesep
        for ii in range(len(self.mesh)):
            tmp = self.mesh[ii].__str__().replace(linesep, linesep + "\t") + linesep
            MeshSolution_str += "mesh[" + str(ii) + "] =" + tmp + linesep + linesep
        MeshSolution_str += "soldict = " + str(self.soldict) + linesep
        MeshSolution_str += "is_same_mesh = " + str(self.is_same_mesh) + linesep
        return MeshSolution_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        if other.mesh != self.mesh:
            return False
        if other.soldict != self.soldict:
            return False
        if other.is_same_mesh != self.is_same_mesh:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        MeshSolution_dict = dict()
        MeshSolution_dict["name"] = self.name
        MeshSolution_dict["mesh"] = list()
        for obj in self.mesh:
            MeshSolution_dict["mesh"].append(obj.as_dict())
        MeshSolution_dict["soldict"] = self.soldict
        MeshSolution_dict["is_same_mesh"] = self.is_same_mesh
        # The class name is added to the dict fordeserialisation purpose
        MeshSolution_dict["__class__"] = "MeshSolution"
        return MeshSolution_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        for obj in self.mesh:
            obj._set_None()
        self.soldict = None
        self.is_same_mesh = None

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    # (Optional) Descriptive name of the mesh
    # Type : str
    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""(Optional) Descriptive name of the mesh""",
    )

    def _get_mesh(self):
        """getter of mesh"""
        for obj in self._mesh:
            if obj is not None:
                obj.parent = self
        return self._mesh

    def _set_mesh(self, value):
        """setter of mesh"""
        check_var("mesh", value, "[Mesh]")
        self._mesh = value

        for obj in self._mesh:
            if obj is not None:
                obj.parent = self

    # A list of Mesh objects.
    # Type : [Mesh]
    mesh = property(fget=_get_mesh, fset=_set_mesh, doc=u"""A list of Mesh objects. """)

    def _get_soldict(self):
        """getter of soldict"""
        return self._soldict

    def _set_soldict(self, value):
        """setter of soldict"""
        check_var("soldict", value, "dict")
        self._soldict = value

    # A list of dict containing Solution objects which are defined with respect to the mesh attribute.
    # Type : dict
    soldict = property(
        fget=_get_soldict,
        fset=_set_soldict,
        doc=u"""A list of dict containing Solution objects which are defined with respect to the mesh attribute.""",
    )

    def _get_is_same_mesh(self):
        """getter of is_same_mesh"""
        return self._is_same_mesh

    def _set_is_same_mesh(self, value):
        """setter of is_same_mesh"""
        check_var("is_same_mesh", value, "bool")
        self._is_same_mesh = value

    # 1 if the mesh is the same at each time step
    # Type : bool
    is_same_mesh = property(
        fget=_get_is_same_mesh,
        fset=_set_is_same_mesh,
        doc=u"""1 if the mesh is the same at each time step""",
    )
