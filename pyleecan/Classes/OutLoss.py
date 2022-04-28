# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutLoss.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutLoss
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
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.OutLoss.get_loss import get_loss
except ImportError as error:
    get_loss = error

try:
    from ..Methods.Output.OutLoss.get_loss_density_ag import get_loss_density_ag
except ImportError as error:
    get_loss_density_ag = error

try:
    from ..Methods.Output.OutLoss.get_loss_dist import get_loss_dist
except ImportError as error:
    get_loss_dist = error

try:
    from ..Methods.Output.OutLoss.get_loss_group import get_loss_group
except ImportError as error:
    get_loss_group = error

try:
    from ..Methods.Output.OutLoss.get_loss_overall import get_loss_overall
except ImportError as error:
    get_loss_overall = error

try:
    from ..Methods.Output.OutLoss.store import store
except ImportError as error:
    store = error


from ._check import InitUnKnowClassError


class OutLoss(FrozenClass):
    """Gather the loss module outputs"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.OutLoss.get_loss
    if isinstance(get_loss, ImportError):
        get_loss = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutLoss method get_loss: " + str(get_loss))
            )
        )
    else:
        get_loss = get_loss
    # cf Methods.Output.OutLoss.get_loss_density_ag
    if isinstance(get_loss_density_ag, ImportError):
        get_loss_density_ag = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLoss method get_loss_density_ag: "
                    + str(get_loss_density_ag)
                )
            )
        )
    else:
        get_loss_density_ag = get_loss_density_ag
    # cf Methods.Output.OutLoss.get_loss_dist
    if isinstance(get_loss_dist, ImportError):
        get_loss_dist = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLoss method get_loss_dist: " + str(get_loss_dist)
                )
            )
        )
    else:
        get_loss_dist = get_loss_dist
    # cf Methods.Output.OutLoss.get_loss_group
    if isinstance(get_loss_group, ImportError):
        get_loss_group = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLoss method get_loss_group: " + str(get_loss_group)
                )
            )
        )
    else:
        get_loss_group = get_loss_group
    # cf Methods.Output.OutLoss.get_loss_overall
    if isinstance(get_loss_overall, ImportError):
        get_loss_overall = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLoss method get_loss_overall: "
                    + str(get_loss_overall)
                )
            )
        )
    else:
        get_loss_overall = get_loss_overall
    # cf Methods.Output.OutLoss.store
    if isinstance(store, ImportError):
        store = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutLoss method store: " + str(store))
            )
        )
    else:
        store = store
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        loss_list=None,
        meshsol_list=None,
        loss_index=-1,
        logger_name="Pyleecan.Loss",
        axes_dict=None,
        Pstator=None,
        Protor=None,
        Pmagnet=None,
        Pprox=None,
        Pjoule=None,
        coeff_dict=-1,
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
            if "loss_list" in list(init_dict.keys()):
                loss_list = init_dict["loss_list"]
            if "meshsol_list" in list(init_dict.keys()):
                meshsol_list = init_dict["meshsol_list"]
            if "loss_index" in list(init_dict.keys()):
                loss_index = init_dict["loss_index"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "axes_dict" in list(init_dict.keys()):
                axes_dict = init_dict["axes_dict"]
            if "Pstator" in list(init_dict.keys()):
                Pstator = init_dict["Pstator"]
            if "Protor" in list(init_dict.keys()):
                Protor = init_dict["Protor"]
            if "Pmagnet" in list(init_dict.keys()):
                Pmagnet = init_dict["Pmagnet"]
            if "Pprox" in list(init_dict.keys()):
                Pprox = init_dict["Pprox"]
            if "Pjoule" in list(init_dict.keys()):
                Pjoule = init_dict["Pjoule"]
            if "coeff_dict" in list(init_dict.keys()):
                coeff_dict = init_dict["coeff_dict"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.loss_list = loss_list
        self.meshsol_list = meshsol_list
        self.loss_index = loss_index
        self.logger_name = logger_name
        self.axes_dict = axes_dict
        self.Pstator = Pstator
        self.Protor = Protor
        self.Pmagnet = Pmagnet
        self.Pprox = Pprox
        self.Pjoule = Pjoule
        self.coeff_dict = coeff_dict

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutLoss_str = ""
        if self.parent is None:
            OutLoss_str += "parent = None " + linesep
        else:
            OutLoss_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutLoss_str += "loss_list = " + str(self.loss_list) + linesep + linesep
        if len(self.meshsol_list) == 0:
            OutLoss_str += "meshsol_list = []" + linesep
        for ii in range(len(self.meshsol_list)):
            tmp = (
                self.meshsol_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            OutLoss_str += "meshsol_list[" + str(ii) + "] =" + tmp + linesep + linesep
        OutLoss_str += "loss_index = " + str(self.loss_index) + linesep
        OutLoss_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        OutLoss_str += "axes_dict = " + str(self.axes_dict) + linesep + linesep
        OutLoss_str += "Pstator = " + str(self.Pstator) + linesep
        OutLoss_str += "Protor = " + str(self.Protor) + linesep
        OutLoss_str += "Pmagnet = " + str(self.Pmagnet) + linesep
        OutLoss_str += "Pprox = " + str(self.Pprox) + linesep
        OutLoss_str += "Pjoule = " + str(self.Pjoule) + linesep
        OutLoss_str += "coeff_dict = " + str(self.coeff_dict) + linesep
        return OutLoss_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.loss_list != self.loss_list:
            return False
        if other.meshsol_list != self.meshsol_list:
            return False
        if other.loss_index != self.loss_index:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.axes_dict != self.axes_dict:
            return False
        if other.Pstator != self.Pstator:
            return False
        if other.Protor != self.Protor:
            return False
        if other.Pmagnet != self.Pmagnet:
            return False
        if other.Pprox != self.Pprox:
            return False
        if other.Pjoule != self.Pjoule:
            return False
        if other.coeff_dict != self.coeff_dict:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.loss_list is None and self.loss_list is not None) or (
            other.loss_list is not None and self.loss_list is None
        ):
            diff_list.append(name + ".loss_list None mismatch")
        elif self.loss_list is None:
            pass
        elif len(other.loss_list) != len(self.loss_list):
            diff_list.append("len(" + name + ".loss_list)")
        else:
            for ii in range(len(other.loss_list)):
                diff_list.extend(
                    self.loss_list[ii].compare(
                        other.loss_list[ii], name=name + ".loss_list[" + str(ii) + "]"
                    )
                )
        if (other.meshsol_list is None and self.meshsol_list is not None) or (
            other.meshsol_list is not None and self.meshsol_list is None
        ):
            diff_list.append(name + ".meshsol_list None mismatch")
        elif self.meshsol_list is None:
            pass
        elif len(other.meshsol_list) != len(self.meshsol_list):
            diff_list.append("len(" + name + ".meshsol_list)")
        else:
            for ii in range(len(other.meshsol_list)):
                diff_list.extend(
                    self.meshsol_list[ii].compare(
                        other.meshsol_list[ii],
                        name=name + ".meshsol_list[" + str(ii) + "]",
                    )
                )
        if other._loss_index != self._loss_index:
            diff_list.append(name + ".loss_index")
        if other._logger_name != self._logger_name:
            diff_list.append(name + ".logger_name")
        if (other.axes_dict is None and self.axes_dict is not None) or (
            other.axes_dict is not None and self.axes_dict is None
        ):
            diff_list.append(name + ".axes_dict None mismatch")
        elif self.axes_dict is None:
            pass
        elif len(other.axes_dict) != len(self.axes_dict):
            diff_list.append("len(" + name + "axes_dict)")
        else:
            for key in self.axes_dict:
                diff_list.extend(
                    self.axes_dict[key].compare(
                        other.axes_dict[key], name=name + ".axes_dict[" + str(key) + "]"
                    )
                )
        if other._Pstator != self._Pstator:
            diff_list.append(name + ".Pstator")
        if other._Protor != self._Protor:
            diff_list.append(name + ".Protor")
        if other._Pmagnet != self._Pmagnet:
            diff_list.append(name + ".Pmagnet")
        if other._Pprox != self._Pprox:
            diff_list.append(name + ".Pprox")
        if other._Pjoule != self._Pjoule:
            diff_list.append(name + ".Pjoule")
        if other._coeff_dict != self._coeff_dict:
            diff_list.append(name + ".coeff_dict")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.loss_list is not None:
            for value in self.loss_list:
                S += getsizeof(value)
        if self.meshsol_list is not None:
            for value in self.meshsol_list:
                S += getsizeof(value)
        if self.loss_index is not None:
            for key, value in self.loss_index.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.logger_name)
        if self.axes_dict is not None:
            for key, value in self.axes_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.Pstator)
        S += getsizeof(self.Protor)
        S += getsizeof(self.Pmagnet)
        S += getsizeof(self.Pprox)
        S += getsizeof(self.Pjoule)
        if self.coeff_dict is not None:
            for key, value in self.coeff_dict.items():
                S += getsizeof(value) + getsizeof(key)
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

        OutLoss_dict = dict()
        if self.loss_list is None:
            OutLoss_dict["loss_list"] = None
        else:
            OutLoss_dict["loss_list"] = list()
            for obj in self.loss_list:
                if obj is not None:
                    OutLoss_dict["loss_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    OutLoss_dict["loss_list"].append(None)
        if self.meshsol_list is None:
            OutLoss_dict["meshsol_list"] = None
        else:
            OutLoss_dict["meshsol_list"] = list()
            for obj in self.meshsol_list:
                if obj is not None:
                    OutLoss_dict["meshsol_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    OutLoss_dict["meshsol_list"].append(None)
        OutLoss_dict["loss_index"] = (
            self.loss_index.copy() if self.loss_index is not None else None
        )
        OutLoss_dict["logger_name"] = self.logger_name
        if self.axes_dict is None:
            OutLoss_dict["axes_dict"] = None
        else:
            OutLoss_dict["axes_dict"] = dict()
            for key, obj in self.axes_dict.items():
                if obj is not None:
                    OutLoss_dict["axes_dict"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    OutLoss_dict["axes_dict"][key] = None
        OutLoss_dict["Pstator"] = self.Pstator
        OutLoss_dict["Protor"] = self.Protor
        OutLoss_dict["Pmagnet"] = self.Pmagnet
        OutLoss_dict["Pprox"] = self.Pprox
        OutLoss_dict["Pjoule"] = self.Pjoule
        OutLoss_dict["coeff_dict"] = (
            self.coeff_dict.copy() if self.coeff_dict is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        OutLoss_dict["__class__"] = "OutLoss"
        return OutLoss_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.loss_list = None
        self.meshsol_list = None
        self.loss_index = None
        self.logger_name = None
        self.axes_dict = None
        self.Pstator = None
        self.Protor = None
        self.Pmagnet = None
        self.Pprox = None
        self.Pjoule = None
        self.coeff_dict = None

    def _get_loss_list(self):
        """getter of loss_list"""
        if self._loss_list is not None:
            for obj in self._loss_list:
                if obj is not None:
                    obj.parent = self
        return self._loss_list

    def _set_loss_list(self, value):
        """setter of loss_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "SciDataTool.Classes", obj.get("__class__"), "loss_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("loss_list", value, "[DataND]")
        self._loss_list = value

    loss_list = property(
        fget=_get_loss_list,
        fset=_set_loss_list,
        doc=u"""Internal list of loss data

        :Type: [SciDataTool.Classes.DataND.DataND]
        """,
    )

    def _get_meshsol_list(self):
        """getter of meshsol_list"""
        if self._meshsol_list is not None:
            for obj in self._meshsol_list:
                if obj is not None:
                    obj.parent = self
        return self._meshsol_list

    def _set_meshsol_list(self, value):
        """setter of meshsol_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "meshsol_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("meshsol_list", value, "[MeshSolution]")
        self._meshsol_list = value

    meshsol_list = property(
        fget=_get_meshsol_list,
        fset=_set_meshsol_list,
        doc=u"""Internal list of loss meshsolutions

        :Type: [MeshSolution]
        """,
    )

    def _get_loss_index(self):
        """getter of loss_index"""
        return self._loss_index

    def _set_loss_index(self, value):
        """setter of loss_index"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("loss_index", value, "dict")
        self._loss_index = value

    loss_index = property(
        fget=_get_loss_index,
        fset=_set_loss_index,
        doc=u"""Internal dict to index losses

        :Type: dict
        """,
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use

        :Type: str
        """,
    )

    def _get_axes_dict(self):
        """getter of axes_dict"""
        if self._axes_dict is not None:
            for key, obj in self._axes_dict.items():
                if obj is not None:
                    obj.parent = self
        return self._axes_dict

    def _set_axes_dict(self, value):
        """setter of axes_dict"""
        if type(value) is dict:
            for key, obj in value.items():
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[key] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "SciDataTool.Classes", obj.get("__class__"), "axes_dict"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("axes_dict", value, "{Data}")
        self._axes_dict = value

    axes_dict = property(
        fget=_get_axes_dict,
        fset=_set_axes_dict,
        doc=u"""Dict containing axes data used for Magnetics

        :Type: {SciDataTool.Classes.DataND.Data}
        """,
    )

    def _get_Pstator(self):
        """getter of Pstator"""
        return self._Pstator

    def _set_Pstator(self, value):
        """setter of Pstator"""
        check_var("Pstator", value, "float")
        self._Pstator = value

    Pstator = property(
        fget=_get_Pstator,
        fset=_set_Pstator,
        doc=u"""Stator core losses due to hysteresis and eddy currents

        :Type: float
        """,
    )

    def _get_Protor(self):
        """getter of Protor"""
        return self._Protor

    def _set_Protor(self, value):
        """setter of Protor"""
        check_var("Protor", value, "float")
        self._Protor = value

    Protor = property(
        fget=_get_Protor,
        fset=_set_Protor,
        doc=u"""Rotor core losses due to hysteresis and eddy currents

        :Type: float
        """,
    )

    def _get_Pmagnet(self):
        """getter of Pmagnet"""
        return self._Pmagnet

    def _set_Pmagnet(self, value):
        """setter of Pmagnet"""
        check_var("Pmagnet", value, "float")
        self._Pmagnet = value

    Pmagnet = property(
        fget=_get_Pmagnet,
        fset=_set_Pmagnet,
        doc=u"""Magnet eddy current losses

        :Type: float
        """,
    )

    def _get_Pprox(self):
        """getter of Pprox"""
        return self._Pprox

    def _set_Pprox(self, value):
        """setter of Pprox"""
        check_var("Pprox", value, "float")
        self._Pprox = value

    Pprox = property(
        fget=_get_Pprox,
        fset=_set_Pprox,
        doc=u"""Stator core losses

        :Type: float
        """,
    )

    def _get_Pjoule(self):
        """getter of Pjoule"""
        return self._Pjoule

    def _set_Pjoule(self, value):
        """setter of Pjoule"""
        check_var("Pjoule", value, "float")
        self._Pjoule = value

    Pjoule = property(
        fget=_get_Pjoule,
        fset=_set_Pjoule,
        doc=u"""Stator core losses

        :Type: float
        """,
    )

    def _get_coeff_dict(self):
        """getter of coeff_dict"""
        return self._coeff_dict

    def _set_coeff_dict(self, value):
        """setter of coeff_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("coeff_dict", value, "dict")
        self._coeff_dict = value

    coeff_dict = property(
        fget=_get_coeff_dict,
        fset=_set_coeff_dict,
        doc=u"""Dict containing coefficients to rebuild loss polynom function of frequency

        :Type: dict
        """,
    )
