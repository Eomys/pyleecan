# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/LossModelBertotti.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .LossModel import LossModel

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.LossModelBertotti.comp_loss import comp_loss
except ImportError as error:
    comp_loss = error

try:
    from ..Methods.Simulation.LossModelBertotti.comp_coeff_Bertotti import (
        comp_coeff_Bertotti,
    )
except ImportError as error:
    comp_coeff_Bertotti = error


from ._check import InitUnKnowClassError


class LossModelBertotti(LossModel):
    """Bertotti Loss Model Class"""

    VERSION = 1
    F_REF = 50
    B_REF = 1.5

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.LossModelBertotti.comp_loss
    if isinstance(comp_loss, ImportError):
        comp_loss = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossModelBertotti method comp_loss: " + str(comp_loss)
                )
            )
        )
    else:
        comp_loss = comp_loss
    # cf Methods.Simulation.LossModelBertotti.comp_coeff_Bertotti
    if isinstance(comp_coeff_Bertotti, ImportError):
        comp_coeff_Bertotti = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LossModelBertotti method comp_coeff_Bertotti: "
                    + str(comp_coeff_Bertotti)
                )
            )
        )
    else:
        comp_coeff_Bertotti = comp_coeff_Bertotti
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

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

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            k_hy = obj.k_hy
            k_ed = obj.k_ed
            k_ex = obj.k_ex
            alpha_hy = obj.alpha_hy
            alpha_ed = obj.alpha_ed
            alpha_ex = obj.alpha_ex
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
        # Initialisation by argument
        self.k_hy = k_hy
        self.k_ed = k_ed
        self.k_ex = k_ex
        self.alpha_hy = alpha_hy
        self.alpha_ed = alpha_ed
        self.alpha_ex = alpha_ex
        # Call LossModel init
        super(LossModelBertotti, self).__init__()
        # The class is frozen (in LossModel init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        LossModelBertotti_str = ""
        # Get the properties inherited from LossModel
        LossModelBertotti_str += super(LossModelBertotti, self).__str__()
        LossModelBertotti_str += "k_hy = " + str(self.k_hy) + linesep
        LossModelBertotti_str += "k_ed = " + str(self.k_ed) + linesep
        LossModelBertotti_str += "k_ex = " + str(self.k_ex) + linesep
        LossModelBertotti_str += "alpha_hy = " + str(self.alpha_hy) + linesep
        LossModelBertotti_str += "alpha_ed = " + str(self.alpha_ed) + linesep
        LossModelBertotti_str += "alpha_ex = " + str(self.alpha_ex) + linesep
        return LossModelBertotti_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LossModel
        if not super(LossModelBertotti, self).__eq__(other):
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

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from LossModel
        LossModelBertotti_dict = super(LossModelBertotti, self).as_dict()
        LossModelBertotti_dict["k_hy"] = self.k_hy
        LossModelBertotti_dict["k_ed"] = self.k_ed
        LossModelBertotti_dict["k_ex"] = self.k_ex
        LossModelBertotti_dict["alpha_hy"] = self.alpha_hy
        LossModelBertotti_dict["alpha_ed"] = self.alpha_ed
        LossModelBertotti_dict["alpha_ex"] = self.alpha_ex
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        LossModelBertotti_dict["__class__"] = "LossModelBertotti"
        return LossModelBertotti_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.k_hy = None
        self.k_ed = None
        self.k_ex = None
        self.alpha_hy = None
        self.alpha_ed = None
        self.alpha_ex = None
        # Set to None the properties inherited from LossModel
        super(LossModelBertotti, self)._set_None()

    def _get_k_hy(self):
        """getter of k_hy"""
        return self._k_hy

    def _set_k_hy(self, value):
        """setter of k_hy"""
        check_var("k_hy", value, "float")
        self._k_hy = value

    # Hysteresis loss coefficient
    # Type : float
    k_hy = property(
        fget=_get_k_hy, fset=_set_k_hy, doc=u"""Hysteresis loss coefficient"""
    )

    def _get_k_ed(self):
        """getter of k_ed"""
        return self._k_ed

    def _set_k_ed(self, value):
        """setter of k_ed"""
        check_var("k_ed", value, "float")
        self._k_ed = value

    # Eddy current loss coefficient
    # Type : float
    k_ed = property(
        fget=_get_k_ed, fset=_set_k_ed, doc=u"""Eddy current loss coefficient"""
    )

    def _get_k_ex(self):
        """getter of k_ex"""
        return self._k_ex

    def _set_k_ex(self, value):
        """setter of k_ex"""
        check_var("k_ex", value, "float")
        self._k_ex = value

    # Excess loss coefficient
    # Type : float
    k_ex = property(fget=_get_k_ex, fset=_set_k_ex, doc=u"""Excess loss coefficient""")

    def _get_alpha_hy(self):
        """getter of alpha_hy"""
        return self._alpha_hy

    def _set_alpha_hy(self, value):
        """setter of alpha_hy"""
        check_var("alpha_hy", value, "float")
        self._alpha_hy = value

    # Hysteresis loss power coefficient
    # Type : float
    alpha_hy = property(
        fget=_get_alpha_hy,
        fset=_set_alpha_hy,
        doc=u"""Hysteresis loss power coefficient""",
    )

    def _get_alpha_ed(self):
        """getter of alpha_ed"""
        return self._alpha_ed

    def _set_alpha_ed(self, value):
        """setter of alpha_ed"""
        check_var("alpha_ed", value, "float")
        self._alpha_ed = value

    # Eddy current loss power coefficient
    # Type : float
    alpha_ed = property(
        fget=_get_alpha_ed,
        fset=_set_alpha_ed,
        doc=u"""Eddy current loss power coefficient""",
    )

    def _get_alpha_ex(self):
        """getter of alpha_ex"""
        return self._alpha_ex

    def _set_alpha_ex(self, value):
        """setter of alpha_ex"""
        check_var("alpha_ex", value, "float")
        self._alpha_ex = value

    # Excess loss power coefficient
    # Type : float
    alpha_ex = property(
        fget=_get_alpha_ex, fset=_set_alpha_ex, doc=u"""Excess loss power coefficient"""
    )
