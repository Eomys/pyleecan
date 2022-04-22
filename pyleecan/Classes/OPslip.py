# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/OPslip.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/OPslip
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
from .OP import OP

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.OPslip.get_Id_Iq import get_Id_Iq
except ImportError as error:
    get_Id_Iq = error

try:
    from ..Methods.Simulation.OPslip.get_felec import get_felec
except ImportError as error:
    get_felec = error

try:
    from ..Methods.Simulation.OPslip.get_N0 import get_N0
except ImportError as error:
    get_N0 = error

try:
    from ..Methods.Simulation.OPslip.get_Ud_Uq import get_Ud_Uq
except ImportError as error:
    get_Ud_Uq = error

try:
    from ..Methods.Simulation.OPslip.set_Id_Iq import set_Id_Iq
except ImportError as error:
    set_Id_Iq = error

try:
    from ..Methods.Simulation.OPslip.get_I0_Phi0 import get_I0_Phi0
except ImportError as error:
    get_I0_Phi0 = error

try:
    from ..Methods.Simulation.OPslip.get_slip import get_slip
except ImportError as error:
    get_slip = error

try:
    from ..Methods.Simulation.OPslip.set_I0_Phi0 import set_I0_Phi0
except ImportError as error:
    set_I0_Phi0 = error

try:
    from ..Methods.Simulation.OPslip.set_Ud_Uq import set_Ud_Uq
except ImportError as error:
    set_Ud_Uq = error

try:
    from ..Methods.Simulation.OPslip.get_U0_UPhi0 import get_U0_UPhi0
except ImportError as error:
    get_U0_UPhi0 = error

try:
    from ..Methods.Simulation.OPslip.set_U0_UPhi0 import set_U0_UPhi0
except ImportError as error:
    set_U0_UPhi0 = error


from ._check import InitUnKnowClassError


class OPslip(OP):
    """Operating Point defined with slip, I0"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.OPslip.get_Id_Iq
    if isinstance(get_Id_Iq, ImportError):
        get_Id_Iq = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPslip method get_Id_Iq: " + str(get_Id_Iq))
            )
        )
    else:
        get_Id_Iq = get_Id_Iq
    # cf Methods.Simulation.OPslip.get_felec
    if isinstance(get_felec, ImportError):
        get_felec = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPslip method get_felec: " + str(get_felec))
            )
        )
    else:
        get_felec = get_felec
    # cf Methods.Simulation.OPslip.get_N0
    if isinstance(get_N0, ImportError):
        get_N0 = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPslip method get_N0: " + str(get_N0))
            )
        )
    else:
        get_N0 = get_N0
    # cf Methods.Simulation.OPslip.get_Ud_Uq
    if isinstance(get_Ud_Uq, ImportError):
        get_Ud_Uq = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPslip method get_Ud_Uq: " + str(get_Ud_Uq))
            )
        )
    else:
        get_Ud_Uq = get_Ud_Uq
    # cf Methods.Simulation.OPslip.set_Id_Iq
    if isinstance(set_Id_Iq, ImportError):
        set_Id_Iq = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPslip method set_Id_Iq: " + str(set_Id_Iq))
            )
        )
    else:
        set_Id_Iq = set_Id_Iq
    # cf Methods.Simulation.OPslip.get_I0_Phi0
    if isinstance(get_I0_Phi0, ImportError):
        get_I0_Phi0 = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPslip method get_I0_Phi0: " + str(get_I0_Phi0))
            )
        )
    else:
        get_I0_Phi0 = get_I0_Phi0
    # cf Methods.Simulation.OPslip.get_slip
    if isinstance(get_slip, ImportError):
        get_slip = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPslip method get_slip: " + str(get_slip))
            )
        )
    else:
        get_slip = get_slip
    # cf Methods.Simulation.OPslip.set_I0_Phi0
    if isinstance(set_I0_Phi0, ImportError):
        set_I0_Phi0 = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPslip method set_I0_Phi0: " + str(set_I0_Phi0))
            )
        )
    else:
        set_I0_Phi0 = set_I0_Phi0
    # cf Methods.Simulation.OPslip.set_Ud_Uq
    if isinstance(set_Ud_Uq, ImportError):
        set_Ud_Uq = property(
            fget=lambda x: raise_(
                ImportError("Can't use OPslip method set_Ud_Uq: " + str(set_Ud_Uq))
            )
        )
    else:
        set_Ud_Uq = set_Ud_Uq
    # cf Methods.Simulation.OPslip.get_U0_UPhi0
    if isinstance(get_U0_UPhi0, ImportError):
        get_U0_UPhi0 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OPslip method get_U0_UPhi0: " + str(get_U0_UPhi0)
                )
            )
        )
    else:
        get_U0_UPhi0 = get_U0_UPhi0
    # cf Methods.Simulation.OPslip.set_U0_UPhi0
    if isinstance(set_U0_UPhi0, ImportError):
        set_U0_UPhi0 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OPslip method set_U0_UPhi0: " + str(set_U0_UPhi0)
                )
            )
        )
    else:
        set_U0_UPhi0 = set_U0_UPhi0
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        I0_ref=None,
        IPhi0_ref=None,
        slip_ref=0,
        U0_ref=None,
        UPhi0_ref=None,
        N0=None,
        felec=None,
        Tem_av_ref=None,
        Pem_av_ref=None,
        Pem_av_in=None,
        efficiency=None,
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
            if "I0_ref" in list(init_dict.keys()):
                I0_ref = init_dict["I0_ref"]
            if "IPhi0_ref" in list(init_dict.keys()):
                IPhi0_ref = init_dict["IPhi0_ref"]
            if "slip_ref" in list(init_dict.keys()):
                slip_ref = init_dict["slip_ref"]
            if "U0_ref" in list(init_dict.keys()):
                U0_ref = init_dict["U0_ref"]
            if "UPhi0_ref" in list(init_dict.keys()):
                UPhi0_ref = init_dict["UPhi0_ref"]
            if "N0" in list(init_dict.keys()):
                N0 = init_dict["N0"]
            if "felec" in list(init_dict.keys()):
                felec = init_dict["felec"]
            if "Tem_av_ref" in list(init_dict.keys()):
                Tem_av_ref = init_dict["Tem_av_ref"]
            if "Pem_av_ref" in list(init_dict.keys()):
                Pem_av_ref = init_dict["Pem_av_ref"]
            if "Pem_av_in" in list(init_dict.keys()):
                Pem_av_in = init_dict["Pem_av_in"]
            if "efficiency" in list(init_dict.keys()):
                efficiency = init_dict["efficiency"]
        # Set the properties (value check and convertion are done in setter)
        self.I0_ref = I0_ref
        self.IPhi0_ref = IPhi0_ref
        self.slip_ref = slip_ref
        self.U0_ref = U0_ref
        self.UPhi0_ref = UPhi0_ref
        # Call OP init
        super(OPslip, self).__init__(
            N0=N0,
            felec=felec,
            Tem_av_ref=Tem_av_ref,
            Pem_av_ref=Pem_av_ref,
            Pem_av_in=Pem_av_in,
            efficiency=efficiency,
        )
        # The class is frozen (in OP init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OPslip_str = ""
        # Get the properties inherited from OP
        OPslip_str += super(OPslip, self).__str__()
        OPslip_str += "I0_ref = " + str(self.I0_ref) + linesep
        OPslip_str += "IPhi0_ref = " + str(self.IPhi0_ref) + linesep
        OPslip_str += "slip_ref = " + str(self.slip_ref) + linesep
        OPslip_str += "U0_ref = " + str(self.U0_ref) + linesep
        OPslip_str += "UPhi0_ref = " + str(self.UPhi0_ref) + linesep
        return OPslip_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OP
        if not super(OPslip, self).__eq__(other):
            return False
        if other.I0_ref != self.I0_ref:
            return False
        if other.IPhi0_ref != self.IPhi0_ref:
            return False
        if other.slip_ref != self.slip_ref:
            return False
        if other.U0_ref != self.U0_ref:
            return False
        if other.UPhi0_ref != self.UPhi0_ref:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from OP
        diff_list.extend(super(OPslip, self).compare(other, name=name))
        if other._I0_ref != self._I0_ref:
            diff_list.append(name + ".I0_ref")
        if other._IPhi0_ref != self._IPhi0_ref:
            diff_list.append(name + ".IPhi0_ref")
        if other._slip_ref != self._slip_ref:
            diff_list.append(name + ".slip_ref")
        if other._U0_ref != self._U0_ref:
            diff_list.append(name + ".U0_ref")
        if other._UPhi0_ref != self._UPhi0_ref:
            diff_list.append(name + ".UPhi0_ref")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from OP
        S += super(OPslip, self).__sizeof__()
        S += getsizeof(self.I0_ref)
        S += getsizeof(self.IPhi0_ref)
        S += getsizeof(self.slip_ref)
        S += getsizeof(self.U0_ref)
        S += getsizeof(self.UPhi0_ref)
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

        # Get the properties inherited from OP
        OPslip_dict = super(OPslip, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        OPslip_dict["I0_ref"] = self.I0_ref
        OPslip_dict["IPhi0_ref"] = self.IPhi0_ref
        OPslip_dict["slip_ref"] = self.slip_ref
        OPslip_dict["U0_ref"] = self.U0_ref
        OPslip_dict["UPhi0_ref"] = self.UPhi0_ref
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OPslip_dict["__class__"] = "OPslip"
        return OPslip_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.I0_ref = None
        self.IPhi0_ref = None
        self.slip_ref = None
        self.U0_ref = None
        self.UPhi0_ref = None
        # Set to None the properties inherited from OP
        super(OPslip, self)._set_None()

    def _get_I0_ref(self):
        """getter of I0_ref"""
        return self._I0_ref

    def _set_I0_ref(self, value):
        """setter of I0_ref"""
        check_var("I0_ref", value, "float")
        self._I0_ref = value

    I0_ref = property(
        fget=_get_I0_ref,
        fset=_set_I0_ref,
        doc=u"""Current rms value

        :Type: float
        """,
    )

    def _get_IPhi0_ref(self):
        """getter of IPhi0_ref"""
        return self._IPhi0_ref

    def _set_IPhi0_ref(self, value):
        """setter of IPhi0_ref"""
        check_var("IPhi0_ref", value, "float")
        self._IPhi0_ref = value

    IPhi0_ref = property(
        fget=_get_IPhi0_ref,
        fset=_set_IPhi0_ref,
        doc=u"""Current phase

        :Type: float
        """,
    )

    def _get_slip_ref(self):
        """getter of slip_ref"""
        return self._slip_ref

    def _set_slip_ref(self, value):
        """setter of slip_ref"""
        check_var("slip_ref", value, "float")
        self._slip_ref = value

    slip_ref = property(
        fget=_get_slip_ref,
        fset=_set_slip_ref,
        doc=u"""Rotor mechanical slip

        :Type: float
        """,
    )

    def _get_U0_ref(self):
        """getter of U0_ref"""
        return self._U0_ref

    def _set_U0_ref(self, value):
        """setter of U0_ref"""
        check_var("U0_ref", value, "float")
        self._U0_ref = value

    U0_ref = property(
        fget=_get_U0_ref,
        fset=_set_U0_ref,
        doc=u"""stator voltage (phase to neutral)

        :Type: float
        """,
    )

    def _get_UPhi0_ref(self):
        """getter of UPhi0_ref"""
        return self._UPhi0_ref

    def _set_UPhi0_ref(self, value):
        """setter of UPhi0_ref"""
        check_var("UPhi0_ref", value, "float")
        self._UPhi0_ref = value

    UPhi0_ref = property(
        fget=_get_UPhi0_ref,
        fset=_set_UPhi0_ref,
        doc=u"""Voltage phase

        :Type: float
        """,
    )
