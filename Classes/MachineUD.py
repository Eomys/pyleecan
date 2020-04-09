# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Machine/MachineUD.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from pyleecan.Classes._check import check_var, raise_
from pyleecan.Functions.get_logger import get_logger
from pyleecan.Functions.save import save
from pyleecan.Classes.Machine import Machine

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.MachineUD.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from pyleecan.Methods.Machine.MachineUD.plot import plot
except ImportError as error:
    plot = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.Shaft import Shaft


class MachineUD(Machine):
    """Doubly Fed Induction Machine"""

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
    # cf Methods.Machine.MachineUD.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use MachineUD method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # save method is available in all object
    save = save

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        lam_list=list(),
        frame=-1,
        shaft=-1,
        name="default_machine",
        desc="",
        type_machine=1,
        logger_name="Pyleecan.Machine",
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if frame == -1:
            frame = Frame()
        if shaft == -1:
            shaft = Shaft()
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "lam_list" in list(init_dict.keys()):
                lam_list = init_dict["lam_list"]
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
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Machine
        MachineUD_dict = super(MachineUD, self).as_dict()
        MachineUD_dict["lam_list"] = list()
        for obj in self.lam_list:
            MachineUD_dict["lam_list"].append(obj.as_dict())
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MachineUD_dict["__class__"] = "MachineUD"
        return MachineUD_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.lam_list:
            obj._set_None()
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

    # List of Lamination
    # Type : [Lamination]
    lam_list = property(
        fget=_get_lam_list, fset=_set_lam_list, doc=u"""List of Lamination"""
    )
