# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Mesh/MeshMat.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Mesh import Mesh

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.MeshMat.get_points import get_points
except ImportError as error:
    get_points = error

try:
    from ..Methods.Mesh.MeshMat.get_cells import get_cells
except ImportError as error:
    get_cells = error

try:
    from ..Methods.Mesh.MeshMat.get_normals import get_normals
except ImportError as error:
    get_normals = error

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
    from ..Methods.Mesh.MeshMat.get_all_node_coord import get_all_node_coord
except ImportError as error:
    get_all_node_coord = error

try:
    from ..Methods.Mesh.MeshMat.add_element import add_element
except ImportError as error:
    add_element = error

try:
    from ..Methods.Mesh.MeshMat.get_all_connectivity import get_all_connectivity
except ImportError as error:
    get_all_connectivity = error

try:
    from ..Methods.Mesh.MeshMat.get_connectivity import get_connectivity
except ImportError as error:
    get_connectivity = error

try:
    from ..Methods.Mesh.MeshMat.get_new_tag import get_new_tag
except ImportError as error:
    get_new_tag = error

try:
    from ..Methods.Mesh.MeshMat.interface import interface
except ImportError as error:
    interface = error

try:
    from ..Methods.Mesh.MeshMat.get_node_tags import get_node_tags
except ImportError as error:
    get_node_tags = error

try:
    from ..Methods.Mesh.MeshMat.get_vertice import get_vertice
except ImportError as error:
    get_vertice = error

try:
    from ..Methods.Mesh.MeshMat.plot_mesh import plot_mesh
except ImportError as error:
    plot_mesh = error

try:
    from ..Methods.Mesh.MeshMat.plot_contour import plot_contour
except ImportError as error:
    plot_contour = error

try:
    from ..Methods.Mesh.MeshMat.plot_glyph import plot_glyph
except ImportError as error:
    plot_glyph = error

try:
    from ..Methods.Mesh.MeshMat.plot_deformation import plot_deformation
except ImportError as error:
    plot_deformation = error

try:
    from ..Methods.Mesh.MeshMat.plot_deformation_animated import (
        plot_deformation_animated,
    )
except ImportError as error:
    plot_deformation_animated = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .CellMat import CellMat
from .PointMat import PointMat
from .Mesh import Mesh


class MeshMat(Mesh):
    """Gather the mesh storage format"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.MeshMat.get_points
    if isinstance(get_points, ImportError):
        get_points = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_points: " + str(get_points))
            )
        )
    else:
        get_points = get_points
    # cf Methods.Mesh.MeshMat.get_cells
    if isinstance(get_cells, ImportError):
        get_cells = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_cells: " + str(get_cells))
            )
        )
    else:
        get_cells = get_cells
    # cf Methods.Mesh.MeshMat.get_normals
    if isinstance(get_normals, ImportError):
        get_normals = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_normals: " + str(get_normals))
            )
        )
    else:
        get_normals = get_normals
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
    # cf Methods.Mesh.MeshMat.get_all_node_coord
    if isinstance(get_all_node_coord, ImportError):
        get_all_node_coord = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method get_all_node_coord: "
                    + str(get_all_node_coord)
                )
            )
        )
    else:
        get_all_node_coord = get_all_node_coord
    # cf Methods.Mesh.MeshMat.add_element
    if isinstance(add_element, ImportError):
        add_element = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method add_element: " + str(add_element))
            )
        )
    else:
        add_element = add_element
    # cf Methods.Mesh.MeshMat.get_all_connectivity
    if isinstance(get_all_connectivity, ImportError):
        get_all_connectivity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method get_all_connectivity: "
                    + str(get_all_connectivity)
                )
            )
        )
    else:
        get_all_connectivity = get_all_connectivity
    # cf Methods.Mesh.MeshMat.get_connectivity
    if isinstance(get_connectivity, ImportError):
        get_connectivity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method get_connectivity: "
                    + str(get_connectivity)
                )
            )
        )
    else:
        get_connectivity = get_connectivity
    # cf Methods.Mesh.MeshMat.get_new_tag
    if isinstance(get_new_tag, ImportError):
        get_new_tag = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method get_new_tag: " + str(get_new_tag))
            )
        )
    else:
        get_new_tag = get_new_tag
    # cf Methods.Mesh.MeshMat.interface
    if isinstance(interface, ImportError):
        interface = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method interface: " + str(interface))
            )
        )
    else:
        interface = interface
    # cf Methods.Mesh.MeshMat.get_node_tags
    if isinstance(get_node_tags, ImportError):
        get_node_tags = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method get_node_tags: " + str(get_node_tags)
                )
            )
        )
    else:
        get_node_tags = get_node_tags
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
    # cf Methods.Mesh.MeshMat.plot_contour
    if isinstance(plot_contour, ImportError):
        plot_contour = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method plot_contour: " + str(plot_contour)
                )
            )
        )
    else:
        plot_contour = plot_contour
    # cf Methods.Mesh.MeshMat.plot_glyph
    if isinstance(plot_glyph, ImportError):
        plot_glyph = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshMat method plot_glyph: " + str(plot_glyph))
            )
        )
    else:
        plot_glyph = plot_glyph
    # cf Methods.Mesh.MeshMat.plot_deformation
    if isinstance(plot_deformation, ImportError):
        plot_deformation = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method plot_deformation: "
                    + str(plot_deformation)
                )
            )
        )
    else:
        plot_deformation = plot_deformation
    # cf Methods.Mesh.MeshMat.plot_deformation_animated
    if isinstance(plot_deformation_animated, ImportError):
        plot_deformation_animated = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshMat method plot_deformation_animated: "
                    + str(plot_deformation_animated)
                )
            )
        )
    else:
        plot_deformation_animated = plot_deformation_animated
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
        group=None,
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
        # group can be None, a ndarray or a list
        set_array(self, "group", group)
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
        MeshMat_str += (
            "group = "
            + linesep
            + str(self.group).replace(linesep, linesep + "\t")
            + linesep
            + linesep
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
        if not array_equal(other.group, self.group):
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
        if self.group is None:
            MeshMat_dict["group"] = None
        else:
            MeshMat_dict["group"] = self.group.tolist()
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
        self.group = None
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
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("group", value, "ndarray")
        self._group = value

    # Contain all possible group numbers
    # Type : ndarray
    group = property(
        fget=_get_group, fset=_set_group, doc=u"""Contain all possible group numbers"""
    )
