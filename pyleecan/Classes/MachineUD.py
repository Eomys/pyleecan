# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/MachineUD.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/MachineUD
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Machine import Machine

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.MachineUD.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.MachineUD.get_lam_list import get_lam_list
except ImportError as error:
    get_lam_list = error

try:
    from ..Methods.Machine.MachineUD.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.MachineUD.is_synchronous import is_synchronous
except ImportError as error:
    is_synchronous = error


from ._check import InitUnKnowClassError
from .Lamination import Lamination
from .Frame import Frame
from .Shaft import Shaft


class MachineUD(Machine):
    """User defined Machine with multiple Laminations"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.MachineUD.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineUD method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.MachineUD.get_lam_list
    if isinstance(get_lam_list, ImportError):
        get_lam_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineUD method get_lam_list: " + str(get_lam_list)
                )
            )
        )
    else:
        get_lam_list = get_lam_list
    # cf Methods.Machine.MachineUD.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use MachineUD method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.MachineUD.is_synchronous
    if isinstance(is_synchronous, ImportError):
        is_synchronous = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineUD method is_synchronous: " + str(is_synchronous)
                )
            )
        )
    else:
        is_synchronous = is_synchronous
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        lam_list=list(),
        is_sync=True,
        frame=-1,
        shaft=-1,
        name="default_machine",
        desc="",
        type_machine=1,
        logger_name="Pyleecan.Machine",
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

        if frame == -1:
            frame = Frame()
        if shaft == -1:
            shaft = Shaft()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            lam_list = obj.lam_list
            is_sync = obj.is_sync
            frame = obj.frame
            shaft = obj.shaft
            name = obj.name
            desc = obj.desc
            type_machine = obj.type_machine
            logger_name = obj.logger_name
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "lam_list" in list(init_dict.keys()):
                lam_list = init_dict["lam_list"]
            if "is_sync" in list(init_dict.keys()):
                is_sync = init_dict["is_sync"]
            if "frame" in list(init_dict.keys()):
                frame = init_dict["frame"]
            if "shaft" in list(init_dict.keys()):
                shaft = init_dict["shaft"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "type_machine" in list(init_dict.keys()):
                type_machine = init_dict["type_machine"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Initialisation by argument
        # lam_list can be None or a list of Lamination object
        self.lam_list = list()
        if type(lam_list) is list:
            for obj in lam_list:
                if obj is None:  # Default value
                    self.lam_list.append(Lamination())
                elif isinstance(obj, dict):
                    # Check that the type is correct (including daughter)
                    class_name = obj.get("__class__")
                    if class_name not in [
                        "Lamination",
                        "LamHole",
                        "LamSlot",
                        "LamSlotMag",
                        "LamSlotMulti",
                        "LamSlotWind",
                        "LamSquirrelCage",
                    ]:
                        raise InitUnKnowClassError(
                            "Unknow class name "
                            + class_name
                            + " in init_dict for lam_list"
                        )
                    # Dynamic import to call the correct constructor
                    module = __import__(
                        "pyleecan.Classes." + class_name, fromlist=[class_name]
                    )
                    class_obj = getattr(module, class_name)
                    self.lam_list.append(class_obj(init_dict=obj))
                else:
                    self.lam_list.append(obj)
        elif lam_list is None:
            self.lam_list = list()
        else:
            self.lam_list = lam_list
        self.is_sync = is_sync
        # Call Machine init
        super(MachineUD, self).__init__(
            frame=frame,
            shaft=shaft,
            name=name,
            desc=desc,
            type_machine=type_machine,
            logger_name=logger_name,
        )
        # The class is frozen (in Machine init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MachineUD_str = ""
        # Get the properties inherited from Machine
        MachineUD_str += super(MachineUD, self).__str__()
        if len(self.lam_list) == 0:
            MachineUD_str += "lam_list = []" + linesep
        for ii in range(len(self.lam_list)):
            tmp = self.lam_list[ii].__str__().replace(linesep, linesep + "\t") + linesep
            MachineUD_str += "lam_list[" + str(ii) + "] =" + tmp + linesep + linesep
        MachineUD_str += "is_sync = " + str(self.is_sync) + linesep
        return MachineUD_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Machine
        if not super(MachineUD, self).__eq__(other):
            return False
        if other.lam_list != self.lam_list:
            return False
        if other.is_sync != self.is_sync:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from Machine
        MachineUD_dict = super(MachineUD, self).as_dict()
        MachineUD_dict["lam_list"] = list()
        for obj in self.lam_list:
            MachineUD_dict["lam_list"].append(obj.as_dict())
        MachineUD_dict["is_sync"] = self.is_sync
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MachineUD_dict["__class__"] = "MachineUD"
        return MachineUD_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.lam_list:
            obj._set_None()
        self.is_sync = None
        # Set to None the properties inherited from Machine
        super(MachineUD, self)._set_None()

    def _get_lam_list(self):
        """getter of lam_list"""
        for obj in self._lam_list:
            if obj is not None:
                obj.parent = self
        return self._lam_list

    def _set_lam_list(self, value):
        """setter of lam_list"""
        check_var("lam_list", value, "[Lamination]")
        self._lam_list = value

        for obj in self._lam_list:
            if obj is not None:
                obj.parent = self

    lam_list = property(
        fget=_get_lam_list,
        fset=_set_lam_list,
        doc=u"""List of Lamination

        :Type: [Lamination]
        """,
    )

    def _get_is_sync(self):
        """getter of is_sync"""
        return self._is_sync

    def _set_is_sync(self, value):
        """setter of is_sync"""
        check_var("is_sync", value, "bool")
        self._is_sync = value

    is_sync = property(
        fget=_get_is_sync,
        fset=_set_is_sync,
        doc=u"""True if the machine should be handled as a Synchronous machine

        :Type: bool
        """,
    )
