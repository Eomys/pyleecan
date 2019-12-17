# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Mesh/MeshSolution.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Mesh.MeshSolution.get_mesh import get_mesh
except ImportError as error:
    get_mesh = error

try:
    from pyleecan.Methods.Mesh.MeshSolution.get_solution import get_solution
except ImportError as error:
    get_solution = error


from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.Solution import Solution


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

    def __init__(
        self, name="", mesh=list(), solution=list(), is_same_mesh=True, init_dict=None
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["name", "mesh", "solution", "is_same_mesh"])
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "mesh" in list(init_dict.keys()):
                mesh = init_dict["mesh"]
            if "solution" in list(init_dict.keys()):
                solution = init_dict["solution"]
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
                    self.mesh.append(Mesh(init_dict=obj))
                else:
                    self.mesh.append(obj)
        elif mesh is None:
            self.mesh = list()
        else:
            self.mesh = mesh
        # solution can be None or a list of Solution object
        self.solution = list()
        if type(solution) is list:
            for obj in solution:
                if obj is None:  # Default value
                    self.solution.append(Solution())
                elif isinstance(obj, dict):
                    # Check that the type is correct (including daughter)
                    class_name = obj.get("__class__")
                    if class_name not in ["Solution", "SolutionFEMM"]:
                        raise InitUnKnowClassError(
                            "Unknow class name "
                            + class_name
                            + " in init_dict for solution"
                        )
                    # Dynamic import to call the correct constructor
                    module = __import__(
                        "pyleecan.Classes." + class_name, fromlist=[class_name]
                    )
                    class_obj = getattr(module, class_name)
                    self.solution.append(class_obj(init_dict=obj))
                else:
                    self.solution.append(obj)
        elif solution is None:
            self.solution = list()
        else:
            self.solution = solution
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
            MeshSolution_str += "mesh = []"
        for ii in range(len(self.mesh)):
            MeshSolution_str += (
                "mesh["
                + str(ii)
                + "] = "
                + str(self.mesh[ii].as_dict())
                + "\n"
                + linesep
                + linesep
            )
        if len(self.solution) == 0:
            MeshSolution_str += "solution = []"
        for ii in range(len(self.solution)):
            MeshSolution_str += (
                "solution["
                + str(ii)
                + "] = "
                + str(self.solution[ii].as_dict())
                + "\n"
                + linesep
                + linesep
            )
        MeshSolution_str += "is_same_mesh = " + str(self.is_same_mesh)
        return MeshSolution_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.name != self.name:
            return False
        if other.mesh != self.mesh:
            return False
        if other.solution != self.solution:
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
        MeshSolution_dict["solution"] = list()
        for obj in self.solution:
            MeshSolution_dict["solution"].append(obj.as_dict())
        MeshSolution_dict["is_same_mesh"] = self.is_same_mesh
        # The class name is added to the dict fordeserialisation purpose
        MeshSolution_dict["__class__"] = "MeshSolution"
        return MeshSolution_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        for obj in self.mesh:
            obj._set_None()
        for obj in self.solution:
            obj._set_None()
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

    # A Mesh object.
    # Type : [Mesh]
    mesh = property(fget=_get_mesh, fset=_set_mesh, doc=u"""A Mesh object. """)

    def _get_solution(self):
        """getter of solution"""
        for obj in self._solution:
            if obj is not None:
                obj.parent = self
        return self._solution

    def _set_solution(self, value):
        """setter of solution"""
        check_var("solution", value, "[Solution]")
        self._solution = value

        for obj in self._solution:
            if obj is not None:
                obj.parent = self

    # A Solution object which are defined with respect to the mesh attribute.
    # Type : [Solution]
    solution = property(
        fget=_get_solution,
        fset=_set_solution,
        doc=u"""A Solution object which are defined with respect to the mesh attribute.""",
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
