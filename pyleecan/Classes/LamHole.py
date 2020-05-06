# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Machine/LamHole.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Lamination import Lamination

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.LamHole.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.LamHole.comp_height_yoke import comp_height_yoke
except ImportError as error:
    comp_height_yoke = error

try:
    from ..Methods.Machine.LamHole.comp_masses import comp_masses
except ImportError as error:
    comp_masses = error

try:
    from ..Methods.Machine.LamHole.comp_surfaces import comp_surfaces
except ImportError as error:
    comp_surfaces = error

try:
    from ..Methods.Machine.LamHole.comp_volumes import comp_volumes
except ImportError as error:
    comp_volumes = error

try:
    from ..Methods.Machine.LamHole.get_pole_pair_number import get_pole_pair_number
except ImportError as error:
    get_pole_pair_number = error

try:
    from ..Methods.Machine.LamHole.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.LamHole.comp_radius_mid_yoke import comp_radius_mid_yoke
except ImportError as error:
    comp_radius_mid_yoke = error


from ._check import InitUnKnowClassError
from .Hole import Hole
from .Bore import Bore
from .Material import Material
from .Notch import Notch


class LamHole(Lamination):
    """Lamination with Hole with or without magnet or winding"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamHole.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHole method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.LamHole.comp_height_yoke
    if isinstance(comp_height_yoke, ImportError):
        comp_height_yoke = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHole method comp_height_yoke: "
                    + str(comp_height_yoke)
                )
            )
        )
    else:
        comp_height_yoke = comp_height_yoke
    # cf Methods.Machine.LamHole.comp_masses
    if isinstance(comp_masses, ImportError):
        comp_masses = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamHole method comp_masses: " + str(comp_masses))
            )
        )
    else:
        comp_masses = comp_masses
    # cf Methods.Machine.LamHole.comp_surfaces
    if isinstance(comp_surfaces, ImportError):
        comp_surfaces = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHole method comp_surfaces: " + str(comp_surfaces)
                )
            )
        )
    else:
        comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamHole.comp_volumes
    if isinstance(comp_volumes, ImportError):
        comp_volumes = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHole method comp_volumes: " + str(comp_volumes)
                )
            )
        )
    else:
        comp_volumes = comp_volumes
    # cf Methods.Machine.LamHole.get_pole_pair_number
    if isinstance(get_pole_pair_number, ImportError):
        get_pole_pair_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHole method get_pole_pair_number: "
                    + str(get_pole_pair_number)
                )
            )
        )
    else:
        get_pole_pair_number = get_pole_pair_number
    # cf Methods.Machine.LamHole.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamHole method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.LamHole.comp_radius_mid_yoke
    if isinstance(comp_radius_mid_yoke, ImportError):
        comp_radius_mid_yoke = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamHole method comp_radius_mid_yoke: "
                    + str(comp_radius_mid_yoke)
                )
            )
        )
    else:
        comp_radius_mid_yoke = comp_radius_mid_yoke
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        hole=list(),
        bore=None,
        L1=0.35,
        mat_type=-1,
        Nrvd=0,
        Wrvd=0,
        Kf1=0.95,
        is_internal=True,
        Rint=0,
        Rext=1,
        is_stator=True,
        axial_vent=list(),
        notch=list(),
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if bore == -1:
            bore = Bore()
        if mat_type == -1:
            mat_type = Material()
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "hole" in list(init_dict.keys()):
                hole = init_dict["hole"]
            if "bore" in list(init_dict.keys()):
                bore = init_dict["bore"]
            if "L1" in list(init_dict.keys()):
                L1 = init_dict["L1"]
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
            if "Nrvd" in list(init_dict.keys()):
                Nrvd = init_dict["Nrvd"]
            if "Wrvd" in list(init_dict.keys()):
                Wrvd = init_dict["Wrvd"]
            if "Kf1" in list(init_dict.keys()):
                Kf1 = init_dict["Kf1"]
            if "is_internal" in list(init_dict.keys()):
                is_internal = init_dict["is_internal"]
            if "Rint" in list(init_dict.keys()):
                Rint = init_dict["Rint"]
            if "Rext" in list(init_dict.keys()):
                Rext = init_dict["Rext"]
            if "is_stator" in list(init_dict.keys()):
                is_stator = init_dict["is_stator"]
            if "axial_vent" in list(init_dict.keys()):
                axial_vent = init_dict["axial_vent"]
            if "notch" in list(init_dict.keys()):
                notch = init_dict["notch"]
        # Initialisation by argument
        # hole can be None or a list of Hole object
        self.hole = list()
        if type(hole) is list:
            for obj in hole:
                if obj is None:  # Default value
                    self.hole.append(Hole())
                elif isinstance(obj, dict):
                    # Check that the type is correct (including daughter)
                    class_name = obj.get("__class__")
                    if class_name not in [
                        "Hole",
                        "HoleM50",
                        "HoleM51",
                        "HoleM52",
                        "HoleM53",
                        "HoleM54",
                        "HoleM58",
                        "HoleMag",
                        "VentilationCirc",
                        "VentilationPolar",
                        "VentilationTrap",
                    ]:
                        raise InitUnKnowClassError(
                            "Unknow class name " + class_name + " in init_dict for hole"
                        )
                    # Dynamic import to call the correct constructor
                    module = __import__(
                        "pyleecan.Classes." + class_name, fromlist=[class_name]
                    )
                    class_obj = getattr(module, class_name)
                    self.hole.append(class_obj(init_dict=obj))
                else:
                    self.hole.append(obj)
        elif hole is None:
            self.hole = list()
        else:
            self.hole = hole
        # bore can be None, a Bore object or a dict
        if isinstance(bore, dict):
            # Check that the type is correct (including daughter)
            class_name = bore.get("__class__")
            if class_name not in ["Bore", "BoreFlower"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for bore"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.bore = class_obj(init_dict=bore)
        else:
            self.bore = bore
        # Call Lamination init
        super(LamHole, self).__init__(
            L1=L1,
            mat_type=mat_type,
            Nrvd=Nrvd,
            Wrvd=Wrvd,
            Kf1=Kf1,
            is_internal=is_internal,
            Rint=Rint,
            Rext=Rext,
            is_stator=is_stator,
            axial_vent=axial_vent,
            notch=notch,
        )
        # The class is frozen (in Lamination init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        LamHole_str = ""
        # Get the properties inherited from Lamination
        LamHole_str += super(LamHole, self).__str__()
        if len(self.hole) == 0:
            LamHole_str += "hole = []" + linesep
        for ii in range(len(self.hole)):
            tmp = self.hole[ii].__str__().replace(linesep, linesep + "\t") + linesep
            LamHole_str += "hole[" + str(ii) + "] =" + tmp + linesep + linesep
        if self.bore is not None:
            tmp = self.bore.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            LamHole_str += "bore = " + tmp
        else:
            LamHole_str += "bore = None" + linesep + linesep
        return LamHole_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Lamination
        if not super(LamHole, self).__eq__(other):
            return False
        if other.hole != self.hole:
            return False
        if other.bore != self.bore:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Lamination
        LamHole_dict = super(LamHole, self).as_dict()
        LamHole_dict["hole"] = list()
        for obj in self.hole:
            LamHole_dict["hole"].append(obj.as_dict())
        if self.bore is None:
            LamHole_dict["bore"] = None
        else:
            LamHole_dict["bore"] = self.bore.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        LamHole_dict["__class__"] = "LamHole"
        return LamHole_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.hole:
            obj._set_None()
        if self.bore is not None:
            self.bore._set_None()
        # Set to None the properties inherited from Lamination
        super(LamHole, self)._set_None()

    def _get_hole(self):
        """getter of hole"""
        for obj in self._hole:
            if obj is not None:
                obj.parent = self
        return self._hole

    def _set_hole(self, value):
        """setter of hole"""
        check_var("hole", value, "[Hole]")
        self._hole = value

        for obj in self._hole:
            if obj is not None:
                obj.parent = self

    # lamination Hole
    # Type : [Hole]
    hole = property(fget=_get_hole, fset=_set_hole, doc=u"""lamination Hole""")

    def _get_bore(self):
        """getter of bore"""
        return self._bore

    def _set_bore(self, value):
        """setter of bore"""
        check_var("bore", value, "Bore")
        self._bore = value

        if self._bore is not None:
            self._bore.parent = self

    # Bore Shape
    # Type : Bore
    bore = property(fget=_get_bore, fset=_set_bore, doc=u"""Bore Shape""")
