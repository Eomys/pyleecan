# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/HoleUD.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/HoleUD
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .HoleMag import HoleMag

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.HoleUD.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.HoleUD.comp_surface_magnet_id import comp_surface_magnet_id
except ImportError as error:
    comp_surface_magnet_id = error

try:
    from ..Methods.Slot.HoleUD.has_magnet import has_magnet
except ImportError as error:
    has_magnet = error

try:
    from ..Methods.Slot.HoleUD.remove_magnet import remove_magnet
except ImportError as error:
    remove_magnet = error


from ._check import InitUnKnowClassError
from .Surface import Surface
from .Material import Material


class HoleUD(HoleMag):
    """User defined hole from list of surface"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.HoleUD.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleUD method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.HoleUD.comp_surface_magnet_id
    if isinstance(comp_surface_magnet_id, ImportError):
        comp_surface_magnet_id = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleUD method comp_surface_magnet_id: "
                    + str(comp_surface_magnet_id)
                )
            )
        )
    else:
        comp_surface_magnet_id = comp_surface_magnet_id
    # cf Methods.Slot.HoleUD.has_magnet
    if isinstance(has_magnet, ImportError):
        has_magnet = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleUD method has_magnet: " + str(has_magnet))
            )
        )
    else:
        has_magnet = has_magnet
    # cf Methods.Slot.HoleUD.remove_magnet
    if isinstance(remove_magnet, ImportError):
        remove_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleUD method remove_magnet: " + str(remove_magnet)
                )
            )
        )
    else:
        remove_magnet = remove_magnet
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, surf_list=list(), magnet_dict={}, Zh=36, mat_void=-1, init_dict = None, init_str = None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if mat_void == -1:
            mat_void = Material()
        if init_str is not None :  # Initialisation by str
            from ..Functions.load import load
            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            surf_list = obj.surf_list
            magnet_dict = obj.magnet_dict
            Zh = obj.Zh
            mat_void = obj.mat_void
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "surf_list" in list(init_dict.keys()):
                surf_list = init_dict["surf_list"]
            if "magnet_dict" in list(init_dict.keys()):
                magnet_dict = init_dict["magnet_dict"]
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
        # Initialisation by argument
        # surf_list can be None or a list of Surface object or a list of dict
        if type(surf_list) is list:
            # Check if the list is only composed of Surface
            if len(surf_list) > 0 and all(isinstance(obj, Surface) for obj in surf_list):
                # set the list to keep pointer reference
                self.surf_list = surf_list
            else:
                self.surf_list = list()
                for obj in surf_list:
                    if not isinstance(obj, dict):  # Default value
                        self.surf_list.append(obj)
                    elif isinstance(obj, dict):
                        # Check that the type is correct (including daughter)
                        class_name = obj.get("__class__")
                        if class_name not in ['Surface', 'Circle', 'PolarArc', 'SurfLine', 'SurfRing', 'Trapeze']:
                            raise InitUnKnowClassError(
                                "Unknow class name "
                                + class_name
                                + " in init_dict for surf_list"
                            )
                        # Dynamic import to call the correct constructor
                        module = __import__(
                            "pyleecan.Classes." + class_name, fromlist=[class_name]
                        )
                        class_obj = getattr(module, class_name)
                        self.surf_list.append(class_obj(init_dict=obj))
    
        elif surf_list is None:
            self.surf_list = list()
        else:
            self.surf_list = surf_list
        self.magnet_dict = magnet_dict
        # Call HoleMag init
        super(HoleUD, self).__init__(Zh=Zh, mat_void=mat_void)
        # The class is frozen (in HoleMag init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        HoleUD_str = ""
        # Get the properties inherited from HoleMag
        HoleUD_str += super(HoleUD, self).__str__()
        if len(self.surf_list) == 0:
            HoleUD_str += "surf_list = []" + linesep
        for ii in range(len(self.surf_list)):
            tmp = self.surf_list[ii].__str__().replace(linesep, linesep + "\t") + linesep
            HoleUD_str += "surf_list["+str(ii)+"] ="+ tmp + linesep + linesep
        HoleUD_str += "magnet_dict = " + str(self.magnet_dict) + linesep
        return HoleUD_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from HoleMag
        if not super(HoleUD, self).__eq__(other):
            return False
        if other.surf_list != self.surf_list:
            return False
        if other.magnet_dict != self.magnet_dict:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from HoleMag
        HoleUD_dict = super(HoleUD, self).as_dict()
        HoleUD_dict["surf_list"] = list()
        for obj in self.surf_list:
            HoleUD_dict["surf_list"].append(obj.as_dict())
        HoleUD_dict["magnet_dict"] = self.magnet_dict
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        HoleUD_dict["__class__"] = "HoleUD"
        return HoleUD_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.surf_list:
            obj._set_None()
        self.magnet_dict = None
        # Set to None the properties inherited from HoleMag
        super(HoleUD, self)._set_None()

    def _get_surf_list(self):
        """getter of surf_list"""
        for obj in self._surf_list:
            if obj is not None:
                obj.parent = self
        return self._surf_list

    def _set_surf_list(self, value):
        """setter of surf_list"""
        check_var("surf_list", value, "[Surface]")
        self._surf_list = value

        for obj in self._surf_list:
            if obj is not None:
                obj.parent = self

    surf_list = property(
        fget=_get_surf_list,
        fset=_set_surf_list,
        doc=u"""List of surface to draw the Hole. Surfaces must be ordered in trigo order, label must contain HoleMagnet for Magnet and Hole for holes

        :Type: [Surface]
        """,
    )

    def _get_magnet_dict(self):
        """getter of magnet_dict"""
        return self._magnet_dict

    def _set_magnet_dict(self, value):
        """setter of magnet_dict"""
        check_var("magnet_dict", value, "dict")
        self._magnet_dict = value

    magnet_dict = property(
        fget=_get_magnet_dict,
        fset=_set_magnet_dict,
        doc=u"""dictionnary with the magnet for the Hole (None to remove magnet, key should be magnet_X)

        :Type: dict
        """,
    )
