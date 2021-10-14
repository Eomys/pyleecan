# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Simu1.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Simu1
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Simulation import Simulation

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Simu1.run_single import run_single
except ImportError as error:
    run_single = error


from ._check import InitUnKnowClassError
from .Electrical import Electrical
from .Magnetics import Magnetics
from .Structural import Structural
from .Force import Force
from .Loss import Loss
from .Machine import Machine
from .Input import Input
from .VarSimu import VarSimu
from .Post import Post


class Simu1(Simulation):
    """Five sequential weak coupling multi physics simulation"""

    VERSION = 1

    # cf Methods.Simulation.Simu1.run_single
    if isinstance(run_single, ImportError):
        run_single = property(
            fget=lambda x: raise_(
                ImportError("Can't use Simu1 method run_single: " + str(run_single))
            )
        )
    else:
        run_single = run_single
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        elec=None,
        mag=None,
        struct=None,
        force=None,
        loss=None,
        name="",
        desc="",
        machine=-1,
        input=-1,
        logger_name="Pyleecan.Simulation",
        var_simu=None,
        postproc_list=-1,
        index=None,
        path_result=None,
        layer=None,
        layer_log_warn=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "elec" in list(init_dict.keys()):
                elec = init_dict["elec"]
            if "mag" in list(init_dict.keys()):
                mag = init_dict["mag"]
            if "struct" in list(init_dict.keys()):
                struct = init_dict["struct"]
            if "force" in list(init_dict.keys()):
                force = init_dict["force"]
            if "loss" in list(init_dict.keys()):
                loss = init_dict["loss"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "machine" in list(init_dict.keys()):
                machine = init_dict["machine"]
            if "input" in list(init_dict.keys()):
                input = init_dict["input"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "var_simu" in list(init_dict.keys()):
                var_simu = init_dict["var_simu"]
            if "postproc_list" in list(init_dict.keys()):
                postproc_list = init_dict["postproc_list"]
            if "index" in list(init_dict.keys()):
                index = init_dict["index"]
            if "path_result" in list(init_dict.keys()):
                path_result = init_dict["path_result"]
            if "layer" in list(init_dict.keys()):
                layer = init_dict["layer"]
            if "layer_log_warn" in list(init_dict.keys()):
                layer_log_warn = init_dict["layer_log_warn"]
        # Set the properties (value check and convertion are done in setter)
        self.elec = elec
        self.mag = mag
        self.struct = struct
        self.force = force
        self.loss = loss
        # Call Simulation init
        super(Simu1, self).__init__(
            name=name,
            desc=desc,
            machine=machine,
            input=input,
            logger_name=logger_name,
            var_simu=var_simu,
            postproc_list=postproc_list,
            index=index,
            path_result=path_result,
            layer=layer,
            layer_log_warn=layer_log_warn,
        )
        # The class is frozen (in Simulation init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Simu1_str = ""
        # Get the properties inherited from Simulation
        Simu1_str += super(Simu1, self).__str__()
        if self.elec is not None:
            tmp = self.elec.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Simu1_str += "elec = " + tmp
        else:
            Simu1_str += "elec = None" + linesep + linesep
        if self.mag is not None:
            tmp = self.mag.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Simu1_str += "mag = " + tmp
        else:
            Simu1_str += "mag = None" + linesep + linesep
        if self.struct is not None:
            tmp = self.struct.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Simu1_str += "struct = " + tmp
        else:
            Simu1_str += "struct = None" + linesep + linesep
        if self.force is not None:
            tmp = self.force.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Simu1_str += "force = " + tmp
        else:
            Simu1_str += "force = None" + linesep + linesep
        if self.loss is not None:
            tmp = self.loss.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Simu1_str += "loss = " + tmp
        else:
            Simu1_str += "loss = None" + linesep + linesep
        return Simu1_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Simulation
        if not super(Simu1, self).__eq__(other):
            return False
        if other.elec != self.elec:
            return False
        if other.mag != self.mag:
            return False
        if other.struct != self.struct:
            return False
        if other.force != self.force:
            return False
        if other.loss != self.loss:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Simulation
        diff_list.extend(super(Simu1, self).compare(other, name=name))
        if (other.elec is None and self.elec is not None) or (
            other.elec is not None and self.elec is None
        ):
            diff_list.append(name + ".elec None mismatch")
        elif self.elec is not None:
            diff_list.extend(self.elec.compare(other.elec, name=name + ".elec"))
        if (other.mag is None and self.mag is not None) or (
            other.mag is not None and self.mag is None
        ):
            diff_list.append(name + ".mag None mismatch")
        elif self.mag is not None:
            diff_list.extend(self.mag.compare(other.mag, name=name + ".mag"))
        if (other.struct is None and self.struct is not None) or (
            other.struct is not None and self.struct is None
        ):
            diff_list.append(name + ".struct None mismatch")
        elif self.struct is not None:
            diff_list.extend(self.struct.compare(other.struct, name=name + ".struct"))
        if (other.force is None and self.force is not None) or (
            other.force is not None and self.force is None
        ):
            diff_list.append(name + ".force None mismatch")
        elif self.force is not None:
            diff_list.extend(self.force.compare(other.force, name=name + ".force"))
        if (other.loss is None and self.loss is not None) or (
            other.loss is not None and self.loss is None
        ):
            diff_list.append(name + ".loss None mismatch")
        elif self.loss is not None:
            diff_list.extend(self.loss.compare(other.loss, name=name + ".loss"))
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Simulation
        S += super(Simu1, self).__sizeof__()
        S += getsizeof(self.elec)
        S += getsizeof(self.mag)
        S += getsizeof(self.struct)
        S += getsizeof(self.force)
        S += getsizeof(self.loss)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from Simulation
        Simu1_dict = super(Simu1, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.elec is None:
            Simu1_dict["elec"] = None
        else:
            Simu1_dict["elec"] = self.elec.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.mag is None:
            Simu1_dict["mag"] = None
        else:
            Simu1_dict["mag"] = self.mag.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.struct is None:
            Simu1_dict["struct"] = None
        else:
            Simu1_dict["struct"] = self.struct.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.force is None:
            Simu1_dict["force"] = None
        else:
            Simu1_dict["force"] = self.force.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.loss is None:
            Simu1_dict["loss"] = None
        else:
            Simu1_dict["loss"] = self.loss.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Simu1_dict["__class__"] = "Simu1"
        return Simu1_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.elec is not None:
            self.elec._set_None()
        if self.mag is not None:
            self.mag._set_None()
        if self.struct is not None:
            self.struct._set_None()
        if self.force is not None:
            self.force._set_None()
        if self.loss is not None:
            self.loss._set_None()
        # Set to None the properties inherited from Simulation
        super(Simu1, self)._set_None()

    def _get_elec(self):
        """getter of elec"""
        return self._elec

    def _set_elec(self, value):
        """setter of elec"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "elec")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Electrical()
        check_var("elec", value, "Electrical")
        self._elec = value

        if self._elec is not None:
            self._elec.parent = self

    elec = property(
        fget=_get_elec,
        fset=_set_elec,
        doc=u"""Electrical module

        :Type: Electrical
        """,
    )

    def _get_mag(self):
        """getter of mag"""
        return self._mag

    def _set_mag(self, value):
        """setter of mag"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "mag")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Magnetics()
        check_var("mag", value, "Magnetics")
        self._mag = value

        if self._mag is not None:
            self._mag.parent = self

    mag = property(
        fget=_get_mag,
        fset=_set_mag,
        doc=u"""Magnetic module

        :Type: Magnetics
        """,
    )

    def _get_struct(self):
        """getter of struct"""
        return self._struct

    def _set_struct(self, value):
        """setter of struct"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "struct"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Structural()
        check_var("struct", value, "Structural")
        self._struct = value

        if self._struct is not None:
            self._struct.parent = self

    struct = property(
        fget=_get_struct,
        fset=_set_struct,
        doc=u"""Structural module

        :Type: Structural
        """,
    )

    def _get_force(self):
        """getter of force"""
        return self._force

    def _set_force(self, value):
        """setter of force"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "force"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Force()
        check_var("force", value, "Force")
        self._force = value

        if self._force is not None:
            self._force.parent = self

    force = property(
        fget=_get_force,
        fset=_set_force,
        doc=u"""Force moduale

        :Type: Force
        """,
    )

    def _get_loss(self):
        """getter of loss"""
        return self._loss

    def _set_loss(self, value):
        """setter of loss"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "loss")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Loss()
        check_var("loss", value, "Loss")
        self._loss = value

        if self._loss is not None:
            self._loss.parent = self

    loss = property(
        fget=_get_loss,
        fset=_set_loss,
        doc=u"""Loss moduale

        :Type: Loss
        """,
    )
