# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/Mode.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/Mode
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .SolutionMat import SolutionMat

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.Mode.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Simulation.Mode.plot_animated import plot_animated
except ImportError as error:
    plot_animated = error

try:
    from ..Methods.Simulation.Mode.get_shape_xyz import get_shape_xyz
except ImportError as error:
    get_shape_xyz = error

try:
    from ..Methods.Simulation.Mode.get_shape_pol import get_shape_pol
except ImportError as error:
    get_shape_pol = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError


class Mode(SolutionMat):
    """Structural module: Mode object"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.Mode.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Mode method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Simulation.Mode.plot_animated
    if isinstance(plot_animated, ImportError):
        plot_animated = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Mode method plot_animated: " + str(plot_animated)
                )
            )
        )
    else:
        plot_animated = plot_animated
    # cf Methods.Simulation.Mode.get_shape_xyz
    if isinstance(get_shape_xyz, ImportError):
        get_shape_xyz = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Mode method get_shape_xyz: " + str(get_shape_xyz)
                )
            )
        )
    else:
        get_shape_xyz = get_shape_xyz
    # cf Methods.Simulation.Mode.get_shape_pol
    if isinstance(get_shape_pol, ImportError):
        get_shape_pol = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Mode method get_shape_pol: " + str(get_shape_pol)
                )
            )
        )
    else:
        get_shape_pol = get_shape_pol
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        nat_freq=None,
        order_circ=None,
        order_long=None,
        field=None,
        indice=None,
        axis_name=None,
        axis_size=None,
        type_cell="triangle",
        label=None,
        dimension=2,
        unit="",
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
            if "nat_freq" in list(init_dict.keys()):
                nat_freq = init_dict["nat_freq"]
            if "order_circ" in list(init_dict.keys()):
                order_circ = init_dict["order_circ"]
            if "order_long" in list(init_dict.keys()):
                order_long = init_dict["order_long"]
            if "field" in list(init_dict.keys()):
                field = init_dict["field"]
            if "indice" in list(init_dict.keys()):
                indice = init_dict["indice"]
            if "axis_name" in list(init_dict.keys()):
                axis_name = init_dict["axis_name"]
            if "axis_size" in list(init_dict.keys()):
                axis_size = init_dict["axis_size"]
            if "type_cell" in list(init_dict.keys()):
                type_cell = init_dict["type_cell"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
            if "dimension" in list(init_dict.keys()):
                dimension = init_dict["dimension"]
            if "unit" in list(init_dict.keys()):
                unit = init_dict["unit"]
        # Set the properties (value check and convertion are done in setter)
        self.nat_freq = nat_freq
        self.order_circ = order_circ
        self.order_long = order_long
        # Call SolutionMat init
        super(Mode, self).__init__(
            field=field,
            indice=indice,
            axis_name=axis_name,
            axis_size=axis_size,
            type_cell=type_cell,
            label=label,
            dimension=dimension,
            unit=unit,
        )
        # The class is frozen (in SolutionMat init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Mode_str = ""
        # Get the properties inherited from SolutionMat
        Mode_str += super(Mode, self).__str__()
        Mode_str += "nat_freq = " + str(self.nat_freq) + linesep
        Mode_str += "order_circ = " + str(self.order_circ) + linesep
        Mode_str += "order_long = " + str(self.order_long) + linesep
        return Mode_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SolutionMat
        if not super(Mode, self).__eq__(other):
            return False
        if other.nat_freq != self.nat_freq:
            return False
        if other.order_circ != self.order_circ:
            return False
        if other.order_long != self.order_long:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from SolutionMat
        diff_list.extend(super(Mode, self).compare(other, name=name))
        if other._nat_freq != self._nat_freq:
            diff_list.append(name + ".nat_freq")
        if other._order_circ != self._order_circ:
            diff_list.append(name + ".order_circ")
        if other._order_long != self._order_long:
            diff_list.append(name + ".order_long")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from SolutionMat
        S += super(Mode, self).__sizeof__()
        S += getsizeof(self.nat_freq)
        S += getsizeof(self.order_circ)
        S += getsizeof(self.order_long)
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

        # Get the properties inherited from SolutionMat
        Mode_dict = super(Mode, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        Mode_dict["nat_freq"] = self.nat_freq
        Mode_dict["order_circ"] = self.order_circ
        Mode_dict["order_long"] = self.order_long
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Mode_dict["__class__"] = "Mode"
        return Mode_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.nat_freq = None
        self.order_circ = None
        self.order_long = None
        # Set to None the properties inherited from SolutionMat
        super(Mode, self)._set_None()

    def _get_nat_freq(self):
        """getter of nat_freq"""
        return self._nat_freq

    def _set_nat_freq(self, value):
        """setter of nat_freq"""
        check_var("nat_freq", value, "float")
        self._nat_freq = value

    nat_freq = property(
        fget=_get_nat_freq,
        fset=_set_nat_freq,
        doc=u"""Natural frequency of the mode

        :Type: float
        """,
    )

    def _get_order_circ(self):
        """getter of order_circ"""
        return self._order_circ

    def _set_order_circ(self, value):
        """setter of order_circ"""
        check_var("order_circ", value, "int", Vmin=0)
        self._order_circ = value

    order_circ = property(
        fget=_get_order_circ,
        fset=_set_order_circ,
        doc=u"""Circumferential order

        :Type: int
        :min: 0
        """,
    )

    def _get_order_long(self):
        """getter of order_long"""
        return self._order_long

    def _set_order_long(self, value):
        """setter of order_long"""
        check_var("order_long", value, "int", Vmin=0)
        self._order_long = value

    order_long = property(
        fget=_get_order_long,
        fset=_set_order_long,
        doc=u"""Longitudinal order

        :Type: int
        :min: 0
        """,
    )
