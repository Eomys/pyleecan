# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutLossMinimal.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutLossMinimal
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
from .OutLoss import OutLoss

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.OutLossMinimal.get_loss import get_loss
except ImportError as error:
    get_loss = error

try:
    from ..Methods.Output.OutLossMinimal.get_loss_dist import get_loss_dist
except ImportError as error:
    get_loss_dist = error

try:
    from ..Methods.Output.OutLossMinimal.get_loss_group import get_loss_group
except ImportError as error:
    get_loss_group = error

try:
    from ..Methods.Output.OutLossMinimal.get_loss_overall import get_loss_overall
except ImportError as error:
    get_loss_overall = error

try:
    from ..Methods.Output.OutLossMinimal.store import store
except ImportError as error:
    store = error


from numpy import isnan
from ._check import InitUnKnowClassError


class OutLossMinimal(OutLoss):
    """Gather the loss module outputs"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.OutLossMinimal.get_loss
    if isinstance(get_loss, ImportError):
        get_loss = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLossMinimal method get_loss: " + str(get_loss)
                )
            )
        )
    else:
        get_loss = get_loss
    # cf Methods.Output.OutLossMinimal.get_loss_dist
    if isinstance(get_loss_dist, ImportError):
        get_loss_dist = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLossMinimal method get_loss_dist: "
                    + str(get_loss_dist)
                )
            )
        )
    else:
        get_loss_dist = get_loss_dist
    # cf Methods.Output.OutLossMinimal.get_loss_group
    if isinstance(get_loss_group, ImportError):
        get_loss_group = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLossMinimal method get_loss_group: "
                    + str(get_loss_group)
                )
            )
        )
    else:
        get_loss_group = get_loss_group
    # cf Methods.Output.OutLossMinimal.get_loss_overall
    if isinstance(get_loss_overall, ImportError):
        get_loss_overall = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLossMinimal method get_loss_overall: "
                    + str(get_loss_overall)
                )
            )
        )
    else:
        get_loss_overall = get_loss_overall
    # cf Methods.Output.OutLossMinimal.store
    if isinstance(store, ImportError):
        store = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutLossMinimal method store: " + str(store))
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
        Pstator=None,
        Protor=None,
        Pmagnet=None,
        Pprox=None,
        Pjoule=None,
        coeff_dict=-1,
        axes_dict=None,
        loss_list=-1,
        logger_name="Pyleecan.Loss",
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
            if "axes_dict" in list(init_dict.keys()):
                axes_dict = init_dict["axes_dict"]
            if "loss_list" in list(init_dict.keys()):
                loss_list = init_dict["loss_list"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.loss_list = loss_list
        self.meshsol_list = meshsol_list
        self.loss_index = loss_index
        self.Pstator = Pstator
        self.Protor = Protor
        self.Pmagnet = Pmagnet
        self.Pprox = Pprox
        self.Pjoule = Pjoule
        self.coeff_dict = coeff_dict
        # Call OutLoss init
        super(OutLossMinimal, self).__init__(
            axes_dict=axes_dict, loss_list=loss_list, logger_name=logger_name
        )
        # The class is frozen (in OutLoss init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutLossMinimal_str = ""
        # Get the properties inherited from OutLoss
        OutLossMinimal_str += super(OutLossMinimal, self).__str__()
        OutLossMinimal_str += "loss_list = " + str(self.loss_list) + linesep + linesep
        if len(self.meshsol_list) == 0:
            OutLossMinimal_str += "meshsol_list = []" + linesep
        for ii in range(len(self.meshsol_list)):
            tmp = (
                self.meshsol_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            OutLossMinimal_str += (
                "meshsol_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        OutLossMinimal_str += "loss_index = " + str(self.loss_index) + linesep
        OutLossMinimal_str += "Pstator = " + str(self.Pstator) + linesep
        OutLossMinimal_str += "Protor = " + str(self.Protor) + linesep
        OutLossMinimal_str += "Pmagnet = " + str(self.Pmagnet) + linesep
        OutLossMinimal_str += "Pprox = " + str(self.Pprox) + linesep
        OutLossMinimal_str += "Pjoule = " + str(self.Pjoule) + linesep
        OutLossMinimal_str += "coeff_dict = " + str(self.coeff_dict) + linesep
        return OutLossMinimal_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OutLoss
        if not super(OutLossMinimal, self).__eq__(other):
            return False
        if other.loss_list != self.loss_list:
            return False
        if other.meshsol_list != self.meshsol_list:
            return False
        if other.loss_index != self.loss_index:
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

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from OutLoss
        diff_list.extend(
            super(OutLossMinimal, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
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
                        other.loss_list[ii],
                        name=name + ".loss_list[" + str(ii) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
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
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
        if other._loss_index != self._loss_index:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._loss_index)
                    + ", other="
                    + str(other._loss_index)
                    + ")"
                )
                diff_list.append(name + ".loss_index" + val_str)
            else:
                diff_list.append(name + ".loss_index")
        if (
            other._Pstator is not None
            and self._Pstator is not None
            and isnan(other._Pstator)
            and isnan(self._Pstator)
        ):
            pass
        elif other._Pstator != self._Pstator:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Pstator)
                    + ", other="
                    + str(other._Pstator)
                    + ")"
                )
                diff_list.append(name + ".Pstator" + val_str)
            else:
                diff_list.append(name + ".Pstator")
        if (
            other._Protor is not None
            and self._Protor is not None
            and isnan(other._Protor)
            and isnan(self._Protor)
        ):
            pass
        elif other._Protor != self._Protor:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Protor)
                    + ", other="
                    + str(other._Protor)
                    + ")"
                )
                diff_list.append(name + ".Protor" + val_str)
            else:
                diff_list.append(name + ".Protor")
        if (
            other._Pmagnet is not None
            and self._Pmagnet is not None
            and isnan(other._Pmagnet)
            and isnan(self._Pmagnet)
        ):
            pass
        elif other._Pmagnet != self._Pmagnet:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Pmagnet)
                    + ", other="
                    + str(other._Pmagnet)
                    + ")"
                )
                diff_list.append(name + ".Pmagnet" + val_str)
            else:
                diff_list.append(name + ".Pmagnet")
        if (
            other._Pprox is not None
            and self._Pprox is not None
            and isnan(other._Pprox)
            and isnan(self._Pprox)
        ):
            pass
        elif other._Pprox != self._Pprox:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Pprox) + ", other=" + str(other._Pprox) + ")"
                )
                diff_list.append(name + ".Pprox" + val_str)
            else:
                diff_list.append(name + ".Pprox")
        if (
            other._Pjoule is not None
            and self._Pjoule is not None
            and isnan(other._Pjoule)
            and isnan(self._Pjoule)
        ):
            pass
        elif other._Pjoule != self._Pjoule:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Pjoule)
                    + ", other="
                    + str(other._Pjoule)
                    + ")"
                )
                diff_list.append(name + ".Pjoule" + val_str)
            else:
                diff_list.append(name + ".Pjoule")
        if other._coeff_dict != self._coeff_dict:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._coeff_dict)
                    + ", other="
                    + str(other._coeff_dict)
                    + ")"
                )
                diff_list.append(name + ".coeff_dict" + val_str)
            else:
                diff_list.append(name + ".coeff_dict")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from OutLoss
        S += super(OutLossMinimal, self).__sizeof__()
        if self.loss_list is not None:
            for value in self.loss_list:
                S += getsizeof(value)
        if self.meshsol_list is not None:
            for value in self.meshsol_list:
                S += getsizeof(value)
        if self.loss_index is not None:
            for key, value in self.loss_index.items():
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

        # Get the properties inherited from OutLoss
        OutLossMinimal_dict = super(OutLossMinimal, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.loss_list is None:
            OutLossMinimal_dict["loss_list"] = None
        else:
            OutLossMinimal_dict["loss_list"] = list()
            for obj in self.loss_list:
                if obj is not None:
                    OutLossMinimal_dict["loss_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    OutLossMinimal_dict["loss_list"].append(None)
        if self.meshsol_list is None:
            OutLossMinimal_dict["meshsol_list"] = None
        else:
            OutLossMinimal_dict["meshsol_list"] = list()
            for obj in self.meshsol_list:
                if obj is not None:
                    OutLossMinimal_dict["meshsol_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    OutLossMinimal_dict["meshsol_list"].append(None)
        OutLossMinimal_dict["loss_index"] = (
            self.loss_index.copy() if self.loss_index is not None else None
        )
        OutLossMinimal_dict["Pstator"] = self.Pstator
        OutLossMinimal_dict["Protor"] = self.Protor
        OutLossMinimal_dict["Pmagnet"] = self.Pmagnet
        OutLossMinimal_dict["Pprox"] = self.Pprox
        OutLossMinimal_dict["Pjoule"] = self.Pjoule
        OutLossMinimal_dict["coeff_dict"] = (
            self.coeff_dict.copy() if self.coeff_dict is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OutLossMinimal_dict["__class__"] = "OutLossMinimal"
        return OutLossMinimal_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.loss_list = None
        self.meshsol_list = None
        self.loss_index = None
        self.Pstator = None
        self.Protor = None
        self.Pmagnet = None
        self.Pprox = None
        self.Pjoule = None
        self.coeff_dict = None
        # Set to None the properties inherited from OutLoss
        super(OutLossMinimal, self)._set_None()

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
        doc=u"""Stator core losses due to hysteresis and eddy currents [W]

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
        doc=u"""Rotor core losses due to hysteresis and eddy currents [W]

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
        doc=u"""Magnet eddy current losses [W]

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
        doc=u"""Stator core losses [W]

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
        doc=u"""Stator core losses [W]

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
