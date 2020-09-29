# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/MeshSolution.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/MeshSolution
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
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

try:
    from ..Methods.Mesh.MeshSolution.get_field import get_field
except ImportError as error:
    get_field = error

try:
    from ..Methods.Mesh.MeshSolution.plot_mesh import plot_mesh
except ImportError as error:
    plot_mesh = error

try:
    from ..Methods.Mesh.MeshSolution.plot_contour import plot_contour
except ImportError as error:
    plot_contour = error

try:
    from ..Methods.Mesh.MeshSolution.plot_deflection import plot_deflection
except ImportError as error:
    plot_deflection = error

try:
    from ..Methods.Mesh.MeshSolution.plot_deflection_animated import (
        plot_deflection_animated,
    )
except ImportError as error:
    plot_deflection_animated = error

try:
    from ..Methods.Mesh.MeshSolution.plot_glyph import plot_glyph
except ImportError as error:
    plot_glyph = error

try:
    from ..Methods.Mesh.MeshSolution.get_group import get_group
except ImportError as error:
    get_group = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .Mesh import Mesh
from .Solution import Solution


class MeshSolution(FrozenClass):
    """Abstract class to associate a mesh with one or several solutions"""

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
    # cf Methods.Mesh.MeshSolution.get_field
    if isinstance(get_field, ImportError):
        get_field = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method get_field: " + str(get_field)
                )
            )
        )
    else:
        get_field = get_field
    # cf Methods.Mesh.MeshSolution.plot_mesh
    if isinstance(plot_mesh, ImportError):
        plot_mesh = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method plot_mesh: " + str(plot_mesh)
                )
            )
        )
    else:
        plot_mesh = plot_mesh
    # cf Methods.Mesh.MeshSolution.plot_contour
    if isinstance(plot_contour, ImportError):
        plot_contour = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method plot_contour: " + str(plot_contour)
                )
            )
        )
    else:
        plot_contour = plot_contour
    # cf Methods.Mesh.MeshSolution.plot_deflection
    if isinstance(plot_deflection, ImportError):
        plot_deflection = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method plot_deflection: "
                    + str(plot_deflection)
                )
            )
        )
    else:
        plot_deflection = plot_deflection
    # cf Methods.Mesh.MeshSolution.plot_deflection_animated
    if isinstance(plot_deflection_animated, ImportError):
        plot_deflection_animated = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method plot_deflection_animated: "
                    + str(plot_deflection_animated)
                )
            )
        )
    else:
        plot_deflection_animated = plot_deflection_animated
    # cf Methods.Mesh.MeshSolution.plot_glyph
    if isinstance(plot_glyph, ImportError):
        plot_glyph = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method plot_glyph: " + str(plot_glyph)
                )
            )
        )
    else:
        plot_glyph = plot_glyph
    # cf Methods.Mesh.MeshSolution.get_group
    if isinstance(get_group, ImportError):
        get_group = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method get_group: " + str(get_group)
                )
            )
        )
    else:
        get_group = get_group
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
        label=None,
        mesh=-1,
        is_same_mesh=True,
        solution=-1,
        group=-1,
        dimension=2,
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
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
            if "mesh" in list(init_dict.keys()):
                mesh = init_dict["mesh"]
            if "is_same_mesh" in list(init_dict.keys()):
                is_same_mesh = init_dict["is_same_mesh"]
            if "solution" in list(init_dict.keys()):
                solution = init_dict["solution"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
            if "dimension" in list(init_dict.keys()):
                dimension = init_dict["dimension"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.label = label
        self.mesh = mesh
        self.is_same_mesh = is_same_mesh
        self.solution = solution
        self.group = group
        self.dimension = dimension

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MeshSolution_str = ""
        if self.parent is None:
            MeshSolution_str += "parent = None " + linesep
        else:
            MeshSolution_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        MeshSolution_str += 'label = "' + str(self.label) + '"' + linesep
        if len(self.mesh) == 0:
            MeshSolution_str += "mesh = []" + linesep
        for ii in range(len(self.mesh)):
            tmp = self.mesh[ii].__str__().replace(linesep, linesep + "\t") + linesep
            MeshSolution_str += "mesh[" + str(ii) + "] =" + tmp + linesep + linesep
        MeshSolution_str += "is_same_mesh = " + str(self.is_same_mesh) + linesep
        if len(self.solution) == 0:
            MeshSolution_str += "solution = []" + linesep
        for ii in range(len(self.solution)):
            tmp = self.solution[ii].__str__().replace(linesep, linesep + "\t") + linesep
            MeshSolution_str += "solution[" + str(ii) + "] =" + tmp + linesep + linesep
        if len(self.group) == 0:
            MeshSolution_str += "group = dict()"
        for key, obj in self.group.items():
            MeshSolution_str += (
                "group[" + key + "] = " + str(self.group[key]) + linesep + linesep
            )
        MeshSolution_str += "dimension = " + str(self.dimension) + linesep
        return MeshSolution_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.label != self.label:
            return False
        if other.mesh != self.mesh:
            return False
        if other.is_same_mesh != self.is_same_mesh:
            return False
        if other.solution != self.solution:
            return False
        if other.group is None and self.group is not None:
            return False
        elif len(other.group) != len(self.group):
            return False
        else:
            for key in other.group:
                if key not in self.group or not array_equal(
                    other.group[key], self.group[key]
                ):
                    return False
        if other.dimension != self.dimension:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)
        """

        MeshSolution_dict = dict()
        MeshSolution_dict["label"] = self.label
        if self.mesh is None:
            MeshSolution_dict["mesh"] = None
        else:
            MeshSolution_dict["mesh"] = list()
            for obj in self.mesh:
                MeshSolution_dict["mesh"].append(obj.as_dict())
        MeshSolution_dict["is_same_mesh"] = self.is_same_mesh
        if self.solution is None:
            MeshSolution_dict["solution"] = None
        else:
            MeshSolution_dict["solution"] = list()
            for obj in self.solution:
                MeshSolution_dict["solution"].append(obj.as_dict())
        if self.group is None:
            MeshSolution_dict["group"] = None
        else:
            MeshSolution_dict["group"] = dict()
            for key, obj in self.group.items():
                MeshSolution_dict["group"][key] = obj.tolist()
        MeshSolution_dict["dimension"] = self.dimension
        # The class name is added to the dict fordeserialisation purpose
        MeshSolution_dict["__class__"] = "MeshSolution"
        return MeshSolution_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.label = None
        for obj in self.mesh:
            obj._set_None()
        self.is_same_mesh = None
        for obj in self.solution:
            obj._set_None()
        self.group = None
        self.dimension = None

    def _get_label(self):
        """getter of label"""
        return self._label

    def _set_label(self, value):
        """setter of label"""
        check_var("label", value, "str")
        self._label = value

    label = property(
        fget=_get_label,
        fset=_set_label,
        doc=u"""(Optional) Descriptive name of the mesh

        :Type: str
        """,
    )

    def _get_mesh(self):
        """getter of mesh"""
        if self._mesh is not None:
            for obj in self._mesh:
                if obj is not None:
                    obj.parent = self
        return self._mesh

    def _set_mesh(self, value):
        """setter of mesh"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "mesh"
                    )
                    value[ii] = class_obj(init_dict=obj)
        if value is -1:
            value = list()
        check_var("mesh", value, "[Mesh]")
        self._mesh = value

    mesh = property(
        fget=_get_mesh,
        fset=_set_mesh,
        doc=u"""A list of Mesh objects. 

        :Type: [Mesh]
        """,
    )

    def _get_is_same_mesh(self):
        """getter of is_same_mesh"""
        return self._is_same_mesh

    def _set_is_same_mesh(self, value):
        """setter of is_same_mesh"""
        check_var("is_same_mesh", value, "bool")
        self._is_same_mesh = value

    is_same_mesh = property(
        fget=_get_is_same_mesh,
        fset=_set_is_same_mesh,
        doc=u"""1 if the mesh is the same at each step (time, mode etc.)

        :Type: bool
        """,
    )

    def _get_solution(self):
        """getter of solution"""
        if self._solution is not None:
            for obj in self._solution:
                if obj is not None:
                    obj.parent = self
        return self._solution

    def _set_solution(self, value):
        """setter of solution"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "solution"
                    )
                    value[ii] = class_obj(init_dict=obj)
        if value is -1:
            value = list()
        check_var("solution", value, "[Solution]")
        self._solution = value

    solution = property(
        fget=_get_solution,
        fset=_set_solution,
        doc=u"""A list of Solution objects

        :Type: [Solution]
        """,
    )

    def _get_group(self):
        """getter of group"""
        return self._group

    def _set_group(self, value):
        """setter of group"""
        if type(value) is dict:
            for key, obj in value.items():
                if type(obj) is list:
                    try:
                        value[key] = array(obj)
                    except:
                        pass
        if value is -1:
            value = dict()
        check_var("group", value, "{ndarray}")
        self._group = value

    group = property(
        fget=_get_group,
        fset=_set_group,
        doc=u"""Dict sorted by groups name with cells indices. 

        :Type: {ndarray}
        """,
    )

    def _get_dimension(self):
        """getter of dimension"""
        return self._dimension

    def _set_dimension(self, value):
        """setter of dimension"""
        check_var("dimension", value, "int", Vmin=1, Vmax=3)
        self._dimension = value

    dimension = property(
        fget=_get_dimension,
        fset=_set_dimension,
        doc=u"""Dimension of the physical problem

        :Type: int
        :min: 1
        :max: 3
        """,
    )
