# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Mesh/MeshMat.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Mesh import Mesh

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.MeshMat.get_point import get_point
except ImportError as error:
    get_point = error

try:
    from ..Methods.Mesh.MeshMat.get_cell import get_cell
except ImportError as error:
    get_cell = error

try:
    from ..Methods.Mesh.MeshMat.get_mesh_pv import get_mesh_pv
except ImportError as error:
    get_mesh_pv = error

try:
    from ..Methods.Mesh.MeshMat.get_normal import get_normal
except ImportError as error:
    get_normal = error

try:
    from ..Methods.Mesh.MeshMat.get_surf import get_surf
except ImportError as error:
    get_surf = error

try:
    from ..Methods.Mesh.MeshMat.get_cell_area import get_cell_area
except ImportError as error:
    get_cell_area = error

try:
    from ..Methods.Mesh.MeshMat.set_submesh import set_submesh
except ImportError as error:
    set_submesh = error

try:
    from ..Methods.Mesh.MeshMat.add_cell import add_cell
except ImportError as error:
    add_cell = error

try:
    from ..Methods.Mesh.MeshMat.interface import interface
except ImportError as error:
    interface = error

try:
    from ..Methods.Mesh.MeshMat.get_vertice import get_vertice
except ImportError as error:
    get_vertice = error

try:
    from ..Methods.Mesh.MeshMat.plot_mesh import plot_mesh
except ImportError as error:
    plot_mesh = error

try:
    from ..Methods.Mesh.MeshMat.get_group import get_group
except ImportError as error:
    get_group = error


from numpy import array, empty
from ._check import InitUnKnowClassError
from .CellMat import CellMat
from .PointMat import PointMat
from .Mesh import Mesh


class MeshMat(Mesh):
    """Gather the mesh storage format"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.MeshMat.get_point
    if isinstance(get_point, ImportError):
        get_point = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_point: " + str(get_point))
            )
        )
    else:
        get_point = get_point
    # cf Methods.Mesh.MeshMat.get_cell
    if isinstance(get_cell, ImportError):
        get_cell = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_cell: " + str(get_cell))
            )
        )
    else:
        get_cell = get_cell
    # cf Methods.Mesh.MeshMat.get_mesh_pv
    if isinstance(get_mesh_pv, ImportError):
        get_mesh_pv = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_mesh_pv: " + str(get_mesh_pv))
            )
        )
    else:
        get_mesh_pv = get_mesh_pv
    # cf Methods.Mesh.MeshMat.get_normal
    if isinstance(get_normal, ImportError):
        get_normal = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_normal: " + str(get_normal))
            )
        )
    else:
        get_normal = get_normal
    # cf Methods.Mesh.MeshMat.get_surf
    if isinstance(get_surf, ImportError):
        get_surf = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_surf: " + str(get_surf))
            )
        )
    else:
        get_surf = get_surf
    # cf Methods.Mesh.MeshMat.get_cell_area
    if isinstance(get_cell_area, ImportError):
        get_cell_area = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method get_cell_area: " + str(get_cell_area)
                )
            )
        )
    else:
        get_cell_area = get_cell_area
    # cf Methods.Mesh.MeshMat.set_submesh
    if isinstance(set_submesh, ImportError):
        set_submesh = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method set_submesh: " + str(set_submesh))
            )
        )
    else:
        set_submesh = set_submesh
    # cf Methods.Mesh.MeshMat.add_cell
    if isinstance(add_cell, ImportError):
        add_cell = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method add_cell: " + str(add_cell))
            )
        )
    else:
        add_cell = add_cell
    # cf Methods.Mesh.MeshMat.interface
    if isinstance(interface, ImportError):
        interface = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method interface: " + str(interface))
            )
        )
    else:
        interface = interface
    # cf Methods.Mesh.MeshMat.get_vertice
    if isinstance(get_vertice, ImportError):
        get_vertice = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_vertice: " + str(get_vertice))
            )
        )
    else:
        get_vertice = get_vertice
    # cf Methods.Mesh.MeshMat.plot_mesh
    if isinstance(plot_mesh, ImportError):
        plot_mesh = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method plot_mesh: " + str(plot_mesh))
            )
        )
    else:
        plot_mesh = plot_mesh
    # cf Methods.Mesh.MeshMat.get_group
    if isinstance(get_group, ImportError):
        get_group = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_group: " + str(get_group))
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
        cell=dict(),
        point=-1,
        submesh=list(),
        group=dict(),
        label=None,
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

        if point == -1:
            point = PointMat()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            cell = obj.cell
            point = obj.point
            submesh = obj.submesh
            group = obj.group
            label = obj.label
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "cell" in list(init_dict.keys()):
                cell = init_dict["cell"]
            if "point" in list(init_dict.keys()):
                point = init_dict["point"]
            if "submesh" in list(init_dict.keys()):
                submesh = init_dict["submesh"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        # cell can be None or a dict of CellMat object
        self.cell = dict()
        if type(cell) is dict:
            for key, obj in cell.items():
                if isinstance(obj, dict):
                    self.cell[key] = CellMat(init_dict=obj)
                else:
                    self.cell[key] = obj
        elif cell is None:
            self.cell = dict()
        else:
            self.cell = cell  # Should raise an error
        # point can be None, a PointMat object or a dict
        if isinstance(point, dict):
            self.point = PointMat(init_dict=point)
        elif isinstance(point, str):
            from ..Functions.load import load

            self.point = load(point)
        else:
            self.point = point
        # submesh can be None or a list of Mesh object
        self.submesh = list()
        if type(submesh) is list:
            for obj in submesh:
                if obj is None:  # Default value
                    self.submesh.append(Mesh())
                elif isinstance(obj, dict):
                    # Check that the type is correct (including daughter)
                    class_name = obj.get("__class__")
                    if class_name not in ["Mesh", "MeshMat", "MeshVTK"]:
                        raise InitUnKnowClassError(
                            "Unknow class name "
                            + class_name
                            + " in init_dict for submesh"
                        )
                    # Dynamic import to call the correct constructor
                    module = __import__(
                        "pyleecan.Classes." + class_name, fromlist=[class_name]
                    )
                    class_obj = getattr(module, class_name)
                    self.submesh.append(class_obj(init_dict=obj))
                else:
                    self.submesh.append(obj)
        elif submesh is None:
            self.submesh = list()
        else:
            self.submesh = submesh
        # group can be None or a dict of ndarray
        self.group = dict()
        if type(group) is dict:
            for key, obj in group.items():
                if obj is None:  # Default value
                    value = empty(0)
                elif isinstance(obj, list):
                    value = array(obj)
                self.group[key] = value
        elif group is None:
            self.group = dict()
        else:
            self.group = group  # Should raise an error
        # Call Mesh init
        super(MeshMat, self).__init__(label=label)
        # The class is frozen (in Mesh init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MeshMat_str = ""
        # Get the properties inherited from Mesh
        MeshMat_str += super(MeshMat, self).__str__()
        if len(self.cell) == 0:
            MeshMat_str += "cell = dict()" + linesep
        for key, obj in self.cell.items():
            tmp = self.cell[key].__str__().replace(linesep, linesep + "\t") + linesep
            MeshMat_str += "cell[" + key + "] =" + tmp + linesep + linesep
        if self.point is not None:
            tmp = self.point.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MeshMat_str += "point = " + tmp
        else:
            MeshMat_str += "point = None" + linesep + linesep
        if len(self.submesh) == 0:
            MeshMat_str += "submesh = []" + linesep
        for ii in range(len(self.submesh)):
            tmp = self.submesh[ii].__str__().replace(linesep, linesep + "\t") + linesep
            MeshMat_str += "submesh[" + str(ii) + "] =" + tmp + linesep + linesep
        if len(self.group) == 0:
            MeshMat_str += "group = dict()"
        for key, obj in self.group.items():
            MeshMat_str += (
                "group[" + key + "] = " + str(self.group[key]) + linesep + linesep
            )
        return MeshMat_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Mesh
        if not super(MeshMat, self).__eq__(other):
            return False
        if other.cell != self.cell:
            return False
        if other.point != self.point:
            return False
        if other.submesh != self.submesh:
            return False
        if other.group != self.group:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Mesh
        MeshMat_dict = super(MeshMat, self).as_dict()
        MeshMat_dict["cell"] = dict()
        for key, obj in self.cell.items():
            MeshMat_dict["cell"][key] = obj.as_dict()
        if self.point is None:
            MeshMat_dict["point"] = None
        else:
            MeshMat_dict["point"] = self.point.as_dict()
        MeshMat_dict["submesh"] = list()
        for obj in self.submesh:
            MeshMat_dict["submesh"].append(obj.as_dict())
        MeshMat_dict["group"] = dict()
        for key, obj in self.group.items():
            MeshMat_dict["group"][key] = obj.tolist()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MeshMat_dict["__class__"] = "MeshMat"
        return MeshMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for key, obj in self.cell.items():
            obj._set_None()
        if self.point is not None:
            self.point._set_None()
        for obj in self.submesh:
            obj._set_None()
        self.group = dict()
        # Set to None the properties inherited from Mesh
        super(MeshMat, self)._set_None()

    def _get_cell(self):
        """getter of cell"""
        for key, obj in self._cell.items():
            if obj is not None:
                obj.parent = self
        return self._cell

    def _set_cell(self, value):
        """setter of cell"""
        check_var("cell", value, "{CellMat}")
        self._cell = value

    # Storing connectivity
    # Type : {CellMat}
    cell = property(fget=_get_cell, fset=_set_cell, doc=u"""Storing connectivity""")

    def _get_point(self):
        """getter of point"""
        return self._point

    def _set_point(self, value):
        """setter of point"""
        check_var("point", value, "PointMat")
        self._point = value

        if self._point is not None:
            self._point.parent = self

    # Storing nodes
    # Type : PointMat
    point = property(fget=_get_point, fset=_set_point, doc=u"""Storing nodes""")

    def _get_submesh(self):
        """getter of submesh"""
        for obj in self._submesh:
            if obj is not None:
                obj.parent = self
        return self._submesh

    def _set_submesh(self, value):
        """setter of submesh"""
        check_var("submesh", value, "[Mesh]")
        self._submesh = value

        for obj in self._submesh:
            if obj is not None:
                obj.parent = self

    # Storing submeshes. Node and element numbers/tags or group must be the same.
    # Type : [Mesh]
    submesh = property(
        fget=_get_submesh,
        fset=_set_submesh,
        doc=u"""Storing submeshes. Node and element numbers/tags or group must be the same.""",
    )

    def _get_group(self):
        """getter of group"""
        return self._group

    def _set_group(self, value):
        """setter of group"""
        if type(value) is dict:
            for key, obj in value.items():
                if obj is None:
                    obj = array([])
                elif type(obj) is list:
                    try:
                        obj = array(obj)
                    except:
                        pass
        check_var("group", value, "{ndarray}")
        self._group = value

    # Dict sorted by groups name with cells indices.
    # Type : {ndarray}
    group = property(
        fget=_get_group,
        fset=_set_group,
        doc=u"""Dict sorted by groups name with cells indices. """,
    )
