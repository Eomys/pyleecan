# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Geometry/SurfRing.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Surface import Surface

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Geometry.SurfRing.get_lines import get_lines
except ImportError as error:
    get_lines = error

try:
    from pyleecan.Methods.Geometry.SurfRing.rotate import rotate
except ImportError as error:
    rotate = error

try:
    from pyleecan.Methods.Geometry.SurfRing.translate import translate
except ImportError as error:
    translate = error

try:
    from pyleecan.Methods.Geometry.SurfRing.check import check
except ImportError as error:
    check = error

try:
    from pyleecan.Methods.Geometry.SurfRing.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from pyleecan.Methods.Geometry.SurfRing.get_patches import get_patches
except ImportError as error:
    get_patches = error

try:
    from pyleecan.Methods.Geometry.SurfRing.discretize import discretize
except ImportError as error:
    discretize = error

try:
    from pyleecan.Methods.Geometry.SurfRing.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from pyleecan.Methods.Geometry.SurfRing.plot_lines import plot_lines
except ImportError as error:
    plot_lines = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.Surface import Surface


class SurfRing(Surface):
    """SurfRing is a surface between two closed surfaces (lamination surfaces for instance)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Geometry.SurfRing.get_lines
    if isinstance(get_lines, ImportError):
        get_lines = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfRing method get_lines: " + str(get_lines))
            )
        )
    else:
        get_lines = get_lines
    # cf Methods.Geometry.SurfRing.rotate
    if isinstance(rotate, ImportError):
        rotate = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfRing method rotate: " + str(rotate))
            )
        )
    else:
        rotate = rotate
    # cf Methods.Geometry.SurfRing.translate
    if isinstance(translate, ImportError):
        translate = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfRing method translate: " + str(translate))
            )
        )
    else:
        translate = translate
    # cf Methods.Geometry.SurfRing.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfRing method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Geometry.SurfRing.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SurfRing method comp_length: " + str(comp_length)
                )
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Geometry.SurfRing.get_patches
    if isinstance(get_patches, ImportError):
        get_patches = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SurfRing method get_patches: " + str(get_patches)
                )
            )
        )
    else:
        get_patches = get_patches
    # cf Methods.Geometry.SurfRing.discretize
    if isinstance(discretize, ImportError):
        discretize = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfRing method discretize: " + str(discretize))
            )
        )
    else:
        discretize = discretize
    # cf Methods.Geometry.SurfRing.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SurfRing method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Geometry.SurfRing.plot_lines
    if isinstance(plot_lines, ImportError):
        plot_lines = property(
            fget=lambda x: raise_(
                ImportError("Can't use SurfRing method plot_lines: " + str(plot_lines))
            )
        )
    else:
        plot_lines = plot_lines
    # save method is available in all object
    save = save

    def __init__(self, out_surf=-1, in_surf=-1, point_ref=0, label="", init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if out_surf == -1:
            out_surf = Surface()
        if in_surf == -1:
            in_surf = Surface()
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "out_surf" in list(init_dict.keys()):
                out_surf = init_dict["out_surf"]
            if "in_surf" in list(init_dict.keys()):
                in_surf = init_dict["in_surf"]
            if "point_ref" in list(init_dict.keys()):
                point_ref = init_dict["point_ref"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
        # Initialisation by argument
        # out_surf can be None, a Surface object or a dict
        if isinstance(out_surf, dict):
            # Check that the type is correct (including daughter)
            class_name = out_surf.get("__class__")
            if class_name not in [
                "Surface",
                "Circle",
                "PolarArc",
                "SurfLine",
                "SurfRing",
                "Trapeze",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for out_surf"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.out_surf = class_obj(init_dict=out_surf)
        else:
            self.out_surf = out_surf
        # in_surf can be None, a Surface object or a dict
        if isinstance(in_surf, dict):
            # Check that the type is correct (including daughter)
            class_name = in_surf.get("__class__")
            if class_name not in [
                "Surface",
                "Circle",
                "PolarArc",
                "SurfLine",
                "SurfRing",
                "Trapeze",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for in_surf"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.in_surf = class_obj(init_dict=in_surf)
        else:
            self.in_surf = in_surf
        # Call Surface init
        super(SurfRing, self).__init__(point_ref=point_ref, label=label)
        # The class is frozen (in Surface init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SurfRing_str = ""
        # Get the properties inherited from Surface
        SurfRing_str += super(SurfRing, self).__str__()
        if self.out_surf is not None:
            tmp = self.out_surf.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            SurfRing_str += "out_surf = " + tmp
        else:
            SurfRing_str += "out_surf = None" + linesep + linesep
        if self.in_surf is not None:
            tmp = self.in_surf.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            SurfRing_str += "in_surf = " + tmp
        else:
            SurfRing_str += "in_surf = None" + linesep + linesep
        return SurfRing_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Surface
        if not super(SurfRing, self).__eq__(other):
            return False
        if other.out_surf != self.out_surf:
            return False
        if other.in_surf != self.in_surf:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Surface
        SurfRing_dict = super(SurfRing, self).as_dict()
        if self.out_surf is None:
            SurfRing_dict["out_surf"] = None
        else:
            SurfRing_dict["out_surf"] = self.out_surf.as_dict()
        if self.in_surf is None:
            SurfRing_dict["in_surf"] = None
        else:
            SurfRing_dict["in_surf"] = self.in_surf.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SurfRing_dict["__class__"] = "SurfRing"
        return SurfRing_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.out_surf is not None:
            self.out_surf._set_None()
        if self.in_surf is not None:
            self.in_surf._set_None()
        # Set to None the properties inherited from Surface
        super(SurfRing, self)._set_None()

    def _get_out_surf(self):
        """getter of out_surf"""
        return self._out_surf

    def _set_out_surf(self, value):
        """setter of out_surf"""
        check_var("out_surf", value, "Surface")
        self._out_surf = value

        if self._out_surf is not None:
            self._out_surf.parent = self

    # Outter surface
    # Type : Surface
    out_surf = property(
        fget=_get_out_surf, fset=_set_out_surf, doc=u"""Outter surface"""
    )

    def _get_in_surf(self):
        """getter of in_surf"""
        return self._in_surf

    def _set_in_surf(self, value):
        """setter of in_surf"""
        check_var("in_surf", value, "Surface")
        self._in_surf = value

        if self._in_surf is not None:
            self._in_surf.parent = self

    # Inner surface
    # Type : Surface
    in_surf = property(fget=_get_in_surf, fset=_set_in_surf, doc=u"""Inner surface""")
