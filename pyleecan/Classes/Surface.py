# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Geometry/Surface.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Geometry/Surface
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
    from ..Methods.Geometry.Surface.comp_mesh_dict import comp_mesh_dict
except ImportError as error:
    comp_mesh_dict = error

try:
    from ..Methods.Geometry.Surface.draw_FEMM import draw_FEMM
except ImportError as error:
    draw_FEMM = error

try:
    from ..Methods.Geometry.Surface.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Geometry.Surface.split_line import split_line
except ImportError as error:
    split_line = error


from ._check import InitUnKnowClassError


class Surface(FrozenClass):
    """SurfLine define by list of lines that delimit it, label and point reference."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Geometry.Surface.comp_mesh_dict
    if isinstance(comp_mesh_dict, ImportError):
        comp_mesh_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Surface method comp_mesh_dict: " + str(comp_mesh_dict)
                )
            )
        )
    else:
        comp_mesh_dict = comp_mesh_dict
    # cf Methods.Geometry.Surface.draw_FEMM
    if isinstance(draw_FEMM, ImportError):
        draw_FEMM = property(
            fget=lambda x: raise_(
                ImportError("Can't use Surface method draw_FEMM: " + str(draw_FEMM))
            )
        )
    else:
        draw_FEMM = draw_FEMM
    # cf Methods.Geometry.Surface.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Surface method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Geometry.Surface.split_line
    if isinstance(split_line, ImportError):
        split_line = property(
            fget=lambda x: raise_(
                ImportError("Can't use Surface method split_line: " + str(split_line))
            )
        )
    else:
        split_line = split_line
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, point_ref=0, label="", init_dict=None, init_str=None):
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
            if "point_ref" in list(init_dict.keys()):
                point_ref = init_dict["point_ref"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.point_ref = point_ref
        self.label = label

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Surface_str = ""
        if self.parent is None:
            Surface_str += "parent = None " + linesep
        else:
            Surface_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Surface_str += "point_ref = " + str(self.point_ref) + linesep
        Surface_str += 'label = "' + str(self.label) + '"' + linesep
        return Surface_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.point_ref != self.point_ref:
            return False
        if other.label != self.label:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        Surface_dict = dict()
        Surface_dict["point_ref"] = self.point_ref
        Surface_dict["label"] = self.label
        # The class name is added to the dict fordeserialisation purpose
        Surface_dict["__class__"] = "Surface"
        return Surface_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.point_ref = None
        self.label = None

    def _get_point_ref(self):
        """getter of point_ref"""
        return self._point_ref

    def _set_point_ref(self, value):
        """setter of point_ref"""
        check_var("point_ref", value, "complex")
        self._point_ref = value

    point_ref = property(
        fget=_get_point_ref,
        fset=_set_point_ref,
        doc=u"""Center of symmetry

        :Type: complex
        """,
    )

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
        doc=u"""Label of the surface

        :Type: str
        """,
    )
