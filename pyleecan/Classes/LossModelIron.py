# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/LossModelIron.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/LossModelIron
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
from .LossModel import LossModel

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.LossModelIron.comp_coeff import comp_coeff
except ImportError as error:
    comp_coeff = error

try:
    from ..Methods.Simulation.LossModelIron.comp_loss import comp_loss
except ImportError as error:
    comp_loss = error


from ._check import InitUnKnowClassError


class LossModelIron(LossModel):
    """General iron Loss Model Class"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.LossModelIron.comp_coeff
    if isinstance(comp_coeff, ImportError):
        comp_coeff = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossModelIron method comp_coeff: " + str(comp_coeff)
                )
            )
        )
    else:
        comp_coeff = comp_coeff
    # cf Methods.Simulation.LossModelIron.comp_loss
    if isinstance(comp_loss, ImportError):
        comp_loss = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossModelIron method comp_loss: " + str(comp_loss)
                )
            )
        )
    else:
        comp_loss = comp_loss
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        k_hy=None,
        k_ed=None,
        k_ex=None,
        alpha_hy=None,
        alpha_ed=None,
        alpha_ex=None,
        name="",
        group="",
        is_show_fig=False,
        coeff_dict=None,
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
            if "k_hy" in list(init_dict.keys()):
                k_hy = init_dict["k_hy"]
            if "k_ed" in list(init_dict.keys()):
                k_ed = init_dict["k_ed"]
            if "k_ex" in list(init_dict.keys()):
                k_ex = init_dict["k_ex"]
            if "alpha_hy" in list(init_dict.keys()):
                alpha_hy = init_dict["alpha_hy"]
            if "alpha_ed" in list(init_dict.keys()):
                alpha_ed = init_dict["alpha_ed"]
            if "alpha_ex" in list(init_dict.keys()):
                alpha_ex = init_dict["alpha_ex"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
            if "is_show_fig" in list(init_dict.keys()):
                is_show_fig = init_dict["is_show_fig"]
            if "coeff_dict" in list(init_dict.keys()):
                coeff_dict = init_dict["coeff_dict"]
        # Set the properties (value check and convertion are done in setter)
        self.k_hy = k_hy
        self.k_ed = k_ed
        self.k_ex = k_ex
        self.alpha_hy = alpha_hy
        self.alpha_ed = alpha_ed
        self.alpha_ex = alpha_ex
        # Call LossModel init
        super(LossModelIron, self).__init__(
            name=name, group=group, is_show_fig=is_show_fig, coeff_dict=coeff_dict
        )
        # The class is frozen (in LossModel init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LossModelIron_str = ""
        # Get the properties inherited from LossModel
        LossModelIron_str += super(LossModelIron, self).__str__()
        LossModelIron_str += "k_hy = " + str(self.k_hy) + linesep
        LossModelIron_str += "k_ed = " + str(self.k_ed) + linesep
        LossModelIron_str += "k_ex = " + str(self.k_ex) + linesep
        LossModelIron_str += "alpha_hy = " + str(self.alpha_hy) + linesep
        LossModelIron_str += "alpha_ed = " + str(self.alpha_ed) + linesep
        LossModelIron_str += "alpha_ex = " + str(self.alpha_ex) + linesep
        return LossModelIron_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LossModel
        if not super(LossModelIron, self).__eq__(other):
            return False
        if other.k_hy != self.k_hy:
            return False
        if other.k_ed != self.k_ed:
            return False
        if other.k_ex != self.k_ex:
            return False
        if other.alpha_hy != self.alpha_hy:
            return False
        if other.alpha_ed != self.alpha_ed:
            return False
        if other.alpha_ex != self.alpha_ex:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from LossModel
        diff_list.extend(super(LossModelIron, self).compare(other, name=name))
        if other._k_hy != self._k_hy:
            diff_list.append(name + ".k_hy")
        if other._k_ed != self._k_ed:
            diff_list.append(name + ".k_ed")
        if other._k_ex != self._k_ex:
            diff_list.append(name + ".k_ex")
        if other._alpha_hy != self._alpha_hy:
            diff_list.append(name + ".alpha_hy")
        if other._alpha_ed != self._alpha_ed:
            diff_list.append(name + ".alpha_ed")
        if other._alpha_ex != self._alpha_ex:
            diff_list.append(name + ".alpha_ex")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from LossModel
        S += super(LossModelIron, self).__sizeof__()
        S += getsizeof(self.k_hy)
        S += getsizeof(self.k_ed)
        S += getsizeof(self.k_ex)
        S += getsizeof(self.alpha_hy)
        S += getsizeof(self.alpha_ed)
        S += getsizeof(self.alpha_ex)
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

        # Get the properties inherited from LossModel
        LossModelIron_dict = super(LossModelIron, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        LossModelIron_dict["k_hy"] = self.k_hy
        LossModelIron_dict["k_ed"] = self.k_ed
        LossModelIron_dict["k_ex"] = self.k_ex
        LossModelIron_dict["alpha_hy"] = self.alpha_hy
        LossModelIron_dict["alpha_ed"] = self.alpha_ed
        LossModelIron_dict["alpha_ex"] = self.alpha_ex
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LossModelIron_dict["__class__"] = "LossModelIron"
        return LossModelIron_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.k_hy = None
        self.k_ed = None
        self.k_ex = None
        self.alpha_hy = None
        self.alpha_ed = None
        self.alpha_ex = None
        # Set to None the properties inherited from LossModel
        super(LossModelIron, self)._set_None()

    def _get_k_hy(self):
        """getter of k_hy"""
        return self._k_hy

    def _set_k_hy(self, value):
        """setter of k_hy"""
        check_var("k_hy", value, "float")
        self._k_hy = value

    k_hy = property(
        fget=_get_k_hy,
        fset=_set_k_hy,
        doc=u"""Hysteresis loss coefficient

        :Type: float
        """,
    )

    def _get_k_ed(self):
        """getter of k_ed"""
        return self._k_ed

    def _set_k_ed(self, value):
        """setter of k_ed"""
        check_var("k_ed", value, "float")
        self._k_ed = value

    k_ed = property(
        fget=_get_k_ed,
        fset=_set_k_ed,
        doc=u"""Eddy current loss coefficient

        :Type: float
        """,
    )

    def _get_k_ex(self):
        """getter of k_ex"""
        return self._k_ex

    def _set_k_ex(self, value):
        """setter of k_ex"""
        check_var("k_ex", value, "float")
        self._k_ex = value

    k_ex = property(
        fget=_get_k_ex,
        fset=_set_k_ex,
        doc=u"""Excess loss coefficient

        :Type: float
        """,
    )

    def _get_alpha_hy(self):
        """getter of alpha_hy"""
        return self._alpha_hy

    def _set_alpha_hy(self, value):
        """setter of alpha_hy"""
        check_var("alpha_hy", value, "float")
        self._alpha_hy = value

    alpha_hy = property(
        fget=_get_alpha_hy,
        fset=_set_alpha_hy,
        doc=u"""Hysteresis loss power coefficient

        :Type: float
        """,
    )

    def _get_alpha_ed(self):
        """getter of alpha_ed"""
        return self._alpha_ed

    def _set_alpha_ed(self, value):
        """setter of alpha_ed"""
        check_var("alpha_ed", value, "float")
        self._alpha_ed = value

    alpha_ed = property(
        fget=_get_alpha_ed,
        fset=_set_alpha_ed,
        doc=u"""Eddy current loss power coefficient

        :Type: float
        """,
    )

    def _get_alpha_ex(self):
        """getter of alpha_ex"""
        return self._alpha_ex

    def _set_alpha_ex(self, value):
        """setter of alpha_ex"""
        check_var("alpha_ex", value, "float")
        self._alpha_ex = value

    alpha_ex = property(
        fget=_get_alpha_ex,
        fset=_set_alpha_ex,
        doc=u"""Excess loss power coefficient

        :Type: float
        """,
    )
