# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutLossFEMM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutLossFEMM
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
    from ..Methods.Output.OutLossFEMM.get_loss_group import get_loss_group
except ImportError as error:
    get_loss_group = error

try:
    from ..Methods.Output.OutLossFEMM.get_loss_overall import get_loss_overall
except ImportError as error:
    get_loss_overall = error

try:
    from ..Methods.Output.OutLossFEMM.store import store
except ImportError as error:
    store = error


from ._check import InitUnKnowClassError


class OutLossFEMM(OutLoss):
    """Gather the loss module outputs after LossFEMM"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.OutLossFEMM.get_loss_group
    if isinstance(get_loss_group, ImportError):
        get_loss_group = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLossFEMM method get_loss_group: "
                    + str(get_loss_group)
                )
            )
        )
    else:
        get_loss_group = get_loss_group
    # cf Methods.Output.OutLossFEMM.get_loss_overall
    if isinstance(get_loss_overall, ImportError):
        get_loss_overall = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutLossFEMM method get_loss_overall: "
                    + str(get_loss_overall)
                )
            )
        )
    else:
        get_loss_overall = get_loss_overall
    # cf Methods.Output.OutLossFEMM.store
    if isinstance(store, ImportError):
        store = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutLossFEMM method store: " + str(store))
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
        axes_dict=None,
        Pstator=None,
        Protor=None,
        Pmagnet=None,
        Pprox=None,
        Pjoule=None,
        meshsolution=None,
        coeff_dict=-1,
        loss_list=None,
        meshsol_list=-1,
        loss_index=-1,
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
            if "meshsolution" in list(init_dict.keys()):
                meshsolution = init_dict["meshsolution"]
            if "coeff_dict" in list(init_dict.keys()):
                coeff_dict = init_dict["coeff_dict"]
            if "loss_list" in list(init_dict.keys()):
                loss_list = init_dict["loss_list"]
            if "meshsol_list" in list(init_dict.keys()):
                meshsol_list = init_dict["meshsol_list"]
            if "loss_index" in list(init_dict.keys()):
                loss_index = init_dict["loss_index"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.axes_dict = axes_dict
        self.Pstator = Pstator
        self.Protor = Protor
        self.Pmagnet = Pmagnet
        self.Pprox = Pprox
        self.Pjoule = Pjoule
        self.meshsolution = meshsolution
        self.coeff_dict = coeff_dict
        # Call OutLoss init
        super(OutLossFEMM, self).__init__(
            loss_list=loss_list,
            meshsol_list=meshsol_list,
            loss_index=loss_index,
            logger_name=logger_name,
        )
        # The class is frozen (in OutLoss init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutLossFEMM_str = ""
        # Get the properties inherited from OutLoss
        OutLossFEMM_str += super(OutLossFEMM, self).__str__()
        OutLossFEMM_str += "axes_dict = " + str(self.axes_dict) + linesep + linesep
        OutLossFEMM_str += "Pstator = " + str(self.Pstator) + linesep
        OutLossFEMM_str += "Protor = " + str(self.Protor) + linesep
        OutLossFEMM_str += "Pmagnet = " + str(self.Pmagnet) + linesep
        OutLossFEMM_str += "Pprox = " + str(self.Pprox) + linesep
        OutLossFEMM_str += "Pjoule = " + str(self.Pjoule) + linesep
        if self.meshsolution is not None:
            tmp = (
                self.meshsolution.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            OutLossFEMM_str += "meshsolution = " + tmp
        else:
            OutLossFEMM_str += "meshsolution = None" + linesep + linesep
        OutLossFEMM_str += "coeff_dict = " + str(self.coeff_dict) + linesep
        return OutLossFEMM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OutLoss
        if not super(OutLossFEMM, self).__eq__(other):
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
        if other.meshsolution != self.meshsolution:
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

        # Check the properties inherited from OutLoss
        diff_list.extend(super(OutLossFEMM, self).compare(other, name=name))
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
                        other.axes_dict[key], name=name + ".axes_dict"
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
        if (other.meshsolution is None and self.meshsolution is not None) or (
            other.meshsolution is not None and self.meshsolution is None
        ):
            diff_list.append(name + ".meshsolution None mismatch")
        elif self.meshsolution is not None:
            diff_list.extend(
                self.meshsolution.compare(
                    other.meshsolution, name=name + ".meshsolution"
                )
            )
        if other._coeff_dict != self._coeff_dict:
            diff_list.append(name + ".coeff_dict")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from OutLoss
        S += super(OutLossFEMM, self).__sizeof__()
        if self.axes_dict is not None:
            for key, value in self.axes_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.Pstator)
        S += getsizeof(self.Protor)
        S += getsizeof(self.Pmagnet)
        S += getsizeof(self.Pprox)
        S += getsizeof(self.Pjoule)
        S += getsizeof(self.meshsolution)
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
        OutLossFEMM_dict = super(OutLossFEMM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.axes_dict is None:
            OutLossFEMM_dict["axes_dict"] = None
        else:
            OutLossFEMM_dict["axes_dict"] = dict()
            for key, obj in self.axes_dict.items():
                if obj is not None:
                    OutLossFEMM_dict["axes_dict"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    OutLossFEMM_dict["axes_dict"][key] = None
        OutLossFEMM_dict["Pstator"] = self.Pstator
        OutLossFEMM_dict["Protor"] = self.Protor
        OutLossFEMM_dict["Pmagnet"] = self.Pmagnet
        OutLossFEMM_dict["Pprox"] = self.Pprox
        OutLossFEMM_dict["Pjoule"] = self.Pjoule
        if self.meshsolution is None:
            OutLossFEMM_dict["meshsolution"] = None
        else:
            OutLossFEMM_dict["meshsolution"] = self.meshsolution.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        OutLossFEMM_dict["coeff_dict"] = (
            self.coeff_dict.copy() if self.coeff_dict is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OutLossFEMM_dict["__class__"] = "OutLossFEMM"
        return OutLossFEMM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.axes_dict = None
        self.Pstator = None
        self.Protor = None
        self.Pmagnet = None
        self.Pprox = None
        self.Pjoule = None
        if self.meshsolution is not None:
            self.meshsolution._set_None()
        self.coeff_dict = None
        # Set to None the properties inherited from OutLoss
        super(OutLossFEMM, self)._set_None()

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

    def _get_meshsolution(self):
        """getter of meshsolution"""
        return self._meshsolution

    def _set_meshsolution(self, value):
        """setter of meshsolution"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "meshsolution"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            MeshSolution = import_class(
                "pyleecan.Classes", "MeshSolution", "meshsolution"
            )
            value = MeshSolution()
        check_var("meshsolution", value, "MeshSolution")
        self._meshsolution = value

        if self._meshsolution is not None:
            self._meshsolution.parent = self

    meshsolution = property(
        fget=_get_meshsolution,
        fset=_set_meshsolution,
        doc=u"""Meshsolution containing loss density map

        :Type: MeshSolution
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
