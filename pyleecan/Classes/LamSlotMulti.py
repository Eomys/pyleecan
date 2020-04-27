# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Machine/LamSlotMulti.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Lamination import Lamination

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.LamSlotMulti.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.LamSlotMulti.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.LamSlotMulti.comp_radius_mec import comp_radius_mec
except ImportError as error:
    comp_radius_mec = error

try:
    from ..Methods.Machine.LamSlotMulti.comp_surfaces import comp_surfaces
except ImportError as error:
    comp_surfaces = error

try:
    from ..Methods.Machine.LamSlotMulti.get_pole_pair_number import get_pole_pair_number
except ImportError as error:
    get_pole_pair_number = error

try:
    from ..Methods.Machine.LamSlotMulti.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.LamSlotMulti.comp_height_yoke import comp_height_yoke
except ImportError as error:
    comp_height_yoke = error

try:
    from ..Methods.Machine.LamSlotMulti.get_Zs import get_Zs
except ImportError as error:
    get_Zs = error

try:
    from ..Methods.Machine.LamSlotMulti.get_bore_desc import get_bore_desc
except ImportError as error:
    get_bore_desc = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .Slot import Slot
from .Material import Material
from .Hole import Hole
from .Notch import Notch


class LamSlotMulti(Lamination):
    """Lamination with list of Slot"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamSlotMulti.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMulti method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.LamSlotMulti.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotMulti method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.LamSlotMulti.comp_radius_mec
    if isinstance(comp_radius_mec, ImportError):
        comp_radius_mec = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMulti method comp_radius_mec: "
                    + str(comp_radius_mec)
                )
            )
        )
    else:
        comp_radius_mec = comp_radius_mec
    # cf Methods.Machine.LamSlotMulti.comp_surfaces
    if isinstance(comp_surfaces, ImportError):
        comp_surfaces = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMulti method comp_surfaces: " + str(comp_surfaces)
                )
            )
        )
    else:
        comp_surfaces = comp_surfaces
    # cf Methods.Machine.LamSlotMulti.get_pole_pair_number
    if isinstance(get_pole_pair_number, ImportError):
        get_pole_pair_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMulti method get_pole_pair_number: "
                    + str(get_pole_pair_number)
                )
            )
        )
    else:
        get_pole_pair_number = get_pole_pair_number
    # cf Methods.Machine.LamSlotMulti.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotMulti method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.LamSlotMulti.comp_height_yoke
    if isinstance(comp_height_yoke, ImportError):
        comp_height_yoke = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMulti method comp_height_yoke: "
                    + str(comp_height_yoke)
                )
            )
        )
    else:
        comp_height_yoke = comp_height_yoke
    # cf Methods.Machine.LamSlotMulti.get_Zs
    if isinstance(get_Zs, ImportError):
        get_Zs = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotMulti method get_Zs: " + str(get_Zs))
            )
        )
    else:
        get_Zs = get_Zs
    # cf Methods.Machine.LamSlotMulti.get_bore_desc
    if isinstance(get_bore_desc, ImportError):
        get_bore_desc = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMulti method get_bore_desc: " + str(get_bore_desc)
                )
            )
        )
    else:
        get_bore_desc = get_bore_desc
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        slot_list=list(),
        alpha=None,
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
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object
        - __init__ (init_str = s) s must be a string
        s is the file path to load """

        if mat_type == -1:
            mat_type = Material()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            slot_list = obj.slot_list
            alpha = obj.alpha
            L1 = obj.L1
            mat_type = obj.mat_type
            Nrvd = obj.Nrvd
            Wrvd = obj.Wrvd
            Kf1 = obj.Kf1
            is_internal = obj.is_internal
            Rint = obj.Rint
            Rext = obj.Rext
            is_stator = obj.is_stator
            axial_vent = obj.axial_vent
            notch = obj.notch
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "slot_list" in list(init_dict.keys()):
                slot_list = init_dict["slot_list"]
            if "alpha" in list(init_dict.keys()):
                alpha = init_dict["alpha"]
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
        # slot_list can be None or a list of Slot object
        self.slot_list = list()
        if type(slot_list) is list:
            for obj in slot_list:
                if obj is None:  # Default value
                    self.slot_list.append(Slot())
                elif isinstance(obj, dict):
                    # Check that the type is correct (including daughter)
                    class_name = obj.get("__class__")
                    if class_name not in [
                        "Slot",
                        "Slot19",
                        "SlotMFlat",
                        "SlotMPolar",
                        "SlotMag",
                        "SlotUD",
                        "SlotW10",
                        "SlotW11",
                        "SlotW12",
                        "SlotW13",
                        "SlotW14",
                        "SlotW15",
                        "SlotW16",
                        "SlotW21",
                        "SlotW22",
                        "SlotW23",
                        "SlotW24",
                        "SlotW25",
                        "SlotW26",
                        "SlotW27",
                        "SlotW28",
                        "SlotW29",
                        "SlotW60",
                        "SlotW61",
                        "SlotWind",
                    ]:
                        raise InitUnKnowClassError(
                            "Unknow class name "
                            + class_name
                            + " in init_dict for slot_list"
                        )
                    # Dynamic import to call the correct constructor
                    module = __import__(
                        "pyleecan.Classes." + class_name, fromlist=[class_name]
                    )
                    class_obj = getattr(module, class_name)
                    self.slot_list.append(class_obj(init_dict=obj))
                else:
                    self.slot_list.append(obj)
        elif slot_list is None:
            self.slot_list = list()
        else:
            self.slot_list = slot_list
        # alpha can be None, a ndarray or a list
        set_array(self, "alpha", alpha)
        # Call Lamination init
        super(LamSlotMulti, self).__init__(
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

        LamSlotMulti_str = ""
        # Get the properties inherited from Lamination
        LamSlotMulti_str += super(LamSlotMulti, self).__str__()
        if len(self.slot_list) == 0:
            LamSlotMulti_str += "slot_list = []" + linesep
        for ii in range(len(self.slot_list)):
            tmp = (
                self.slot_list[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            LamSlotMulti_str += "slot_list[" + str(ii) + "] =" + tmp + linesep + linesep
        LamSlotMulti_str += (
            "alpha = "
            + linesep
            + str(self.alpha).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return LamSlotMulti_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Lamination
        if not super(LamSlotMulti, self).__eq__(other):
            return False
        if other.slot_list != self.slot_list:
            return False
        if not array_equal(other.alpha, self.alpha):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Lamination
        LamSlotMulti_dict = super(LamSlotMulti, self).as_dict()
        LamSlotMulti_dict["slot_list"] = list()
        for obj in self.slot_list:
            LamSlotMulti_dict["slot_list"].append(obj.as_dict())
        if self.alpha is None:
            LamSlotMulti_dict["alpha"] = None
        else:
            LamSlotMulti_dict["alpha"] = self.alpha.tolist()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        LamSlotMulti_dict["__class__"] = "LamSlotMulti"
        return LamSlotMulti_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.slot_list:
            obj._set_None()
        self.alpha = None
        # Set to None the properties inherited from Lamination
        super(LamSlotMulti, self)._set_None()

    def _get_slot_list(self):
        """getter of slot_list"""
        for obj in self._slot_list:
            if obj is not None:
                obj.parent = self
        return self._slot_list

    def _set_slot_list(self, value):
        """setter of slot_list"""
        check_var("slot_list", value, "[Slot]")
        self._slot_list = value

        for obj in self._slot_list:
            if obj is not None:
                obj.parent = self

    # List of lamination Slot
    # Type : [Slot]
    slot_list = property(
        fget=_get_slot_list, fset=_set_slot_list, doc=u"""List of lamination Slot"""
    )

    def _get_alpha(self):
        """getter of alpha"""
        return self._alpha

    def _set_alpha(self, value):
        """setter of alpha"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("alpha", value, "ndarray")
        self._alpha = value

    # Angular position of the Slots
    # Type : ndarray
    alpha = property(
        fget=_get_alpha, fset=_set_alpha, doc=u"""Angular position of the Slots"""
    )
