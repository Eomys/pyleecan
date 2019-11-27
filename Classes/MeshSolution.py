# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.Solution import Solution


class MeshSolution(FrozenClass):
    """To associate a Mesh with one or several solutions"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, name=None, mesh=None, solution=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if mesh == -1:
            mesh = Mesh()
        if solution == -1:
            solution = Solution()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["name", "mesh", "solution"])
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "mesh" in list(init_dict.keys()):
                mesh = init_dict["mesh"]
            if "solution" in list(init_dict.keys()):
                solution = init_dict["solution"]
        # Initialisation by argument
        self.parent = None
        self.name = name
        # mesh can be None, a Mesh object or a dict
        if isinstance(mesh, dict):
            self.mesh = Mesh(init_dict=mesh)
        else:
            self.mesh = mesh
        # solution can be None, a Solution object or a dict
        if isinstance(solution, dict):
            # Check that the type is correct (including daughter)
            class_name = solution.get("__class__")
            if class_name not in ["Solution", "SolutionFEMM"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for solution"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.solution = class_obj(init_dict=solution)
        else:
            self.solution = solution

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
        MeshSolution_str += "mesh = " + str(self.mesh.as_dict()) + linesep + linesep
        MeshSolution_str += "solution = " + str(self.solution.as_dict())
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
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        MeshSolution_dict = dict()
        MeshSolution_dict["name"] = self.name
        if self.mesh is None:
            MeshSolution_dict["mesh"] = None
        else:
            MeshSolution_dict["mesh"] = self.mesh.as_dict()
        if self.solution is None:
            MeshSolution_dict["solution"] = None
        else:
            MeshSolution_dict["solution"] = self.solution.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        MeshSolution_dict["__class__"] = "MeshSolution"
        return MeshSolution_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.name = None
        if self.mesh is not None:
            self.mesh._set_None()
        if self.solution is not None:
            self.solution._set_None()

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
        return self._mesh

    def _set_mesh(self, value):
        """setter of mesh"""
        check_var("mesh", value, "Mesh")
        self._mesh = value

        if self._mesh is not None:
            self._mesh.parent = self

    # A Mesh object.
    # Type : Mesh
    mesh = property(fget=_get_mesh, fset=_set_mesh, doc=u"""A Mesh object. """)

    def _get_solution(self):
        """getter of solution"""
        return self._solution

    def _set_solution(self, value):
        """setter of solution"""
        check_var("solution", value, "Solution")
        self._solution = value

        if self._solution is not None:
            self._solution.parent = self

    # A Solution object which are defined with respect to the mesh attribute.
    # Type : Solution
    solution = property(
        fget=_get_solution,
        fset=_set_solution,
        doc=u"""A Solution object which are defined with respect to the mesh attribute.""",
    )
