# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Output/XOutput.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Output import Output

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.XOutput.__delitem__ import __delitem__
except ImportError as error:
    __delitem__ = error

try:
    from ..Methods.Output.XOutput.__getitem__ import __getitem__
except ImportError as error:
    __getitem__ = error

try:
    from ..Methods.Output.XOutput.__iter__ import __iter__
except ImportError as error:
    __iter__ = error

try:
    from ..Methods.Output.XOutput.__len__ import __len__
except ImportError as error:
    __len__ = error

try:
    from ..Methods.Output.XOutput.__missing__ import __missing__
except ImportError as error:
    __missing__ = error

try:
    from ..Methods.Output.XOutput.__next__ import __next__
except ImportError as error:
    __next__ = error

try:
    from ..Methods.Output.XOutput.__reversed__ import __reversed__
except ImportError as error:
    __reversed__ = error

try:
    from ..Methods.Output.XOutput.__setitem__ import __setitem__
except ImportError as error:
    __setitem__ = error

try:
    from ..Methods.Output.XOutput.count import count
except ImportError as error:
    count = error

try:
    from ..Methods.Output.XOutput.insert import insert
except ImportError as error:
    insert = error

try:
    from ..Methods.Output.XOutput.pop import pop
except ImportError as error:
    pop = error

try:
    from ..Methods.Output.XOutput.remove import remove
except ImportError as error:
    remove = error

try:
    from ..Methods.Output.XOutput.append import append
except ImportError as error:
    append = error

try:
    from ..Methods.Output.XOutput.get_simu import get_simu
except ImportError as error:
    get_simu = error

try:
    from ..Methods.Output.XOutput.keys import keys
except ImportError as error:
    keys = error

try:
    from ..Methods.Output.XOutput.items import items
except ImportError as error:
    items = error

try:
    from ..Methods.Output.XOutput.get_param_simu import get_param_simu
except ImportError as error:
    get_param_simu = error

try:
    from ..Methods.Output.XOutput.get_param_array import get_param_array
except ImportError as error:
    get_param_array = error

try:
    from ..Methods.Output.XOutput.plot_multi import plot_multi
except ImportError as error:
    plot_multi = error


from ._check import InitUnKnowClassError
from .Simulation import Simulation
from .OutGeo import OutGeo
from .OutElec import OutElec
from .OutMag import OutMag
from .OutStruct import OutStruct
from .OutPost import OutPost
from .OutForce import OutForce


class XOutput(Output):
    """XOutput object: gather all the outputs of all the modules for multiple simulations"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.XOutput.__delitem__
    if isinstance(__delitem__, ImportError):
        __delitem__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method __delitem__: " + str(__delitem__))
            )
        )
    else:
        __delitem__ = __delitem__
    # cf Methods.Output.XOutput.__getitem__
    if isinstance(__getitem__, ImportError):
        __getitem__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method __getitem__: " + str(__getitem__))
            )
        )
    else:
        __getitem__ = __getitem__
    # cf Methods.Output.XOutput.__iter__
    if isinstance(__iter__, ImportError):
        __iter__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method __iter__: " + str(__iter__))
            )
        )
    else:
        __iter__ = __iter__
    # cf Methods.Output.XOutput.__len__
    if isinstance(__len__, ImportError):
        __len__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method __len__: " + str(__len__))
            )
        )
    else:
        __len__ = __len__
    # cf Methods.Output.XOutput.__missing__
    if isinstance(__missing__, ImportError):
        __missing__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method __missing__: " + str(__missing__))
            )
        )
    else:
        __missing__ = __missing__
    # cf Methods.Output.XOutput.__next__
    if isinstance(__next__, ImportError):
        __next__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method __next__: " + str(__next__))
            )
        )
    else:
        __next__ = __next__
    # cf Methods.Output.XOutput.__reversed__
    if isinstance(__reversed__, ImportError):
        __reversed__ = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use XOutput method __reversed__: " + str(__reversed__)
                )
            )
        )
    else:
        __reversed__ = __reversed__
    # cf Methods.Output.XOutput.__setitem__
    if isinstance(__setitem__, ImportError):
        __setitem__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method __setitem__: " + str(__setitem__))
            )
        )
    else:
        __setitem__ = __setitem__
    # cf Methods.Output.XOutput.count
    if isinstance(count, ImportError):
        count = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method count: " + str(count))
            )
        )
    else:
        count = count
    # cf Methods.Output.XOutput.insert
    if isinstance(insert, ImportError):
        insert = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method insert: " + str(insert))
            )
        )
    else:
        insert = insert
    # cf Methods.Output.XOutput.pop
    if isinstance(pop, ImportError):
        pop = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method pop: " + str(pop))
            )
        )
    else:
        pop = pop
    # cf Methods.Output.XOutput.remove
    if isinstance(remove, ImportError):
        remove = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method remove: " + str(remove))
            )
        )
    else:
        remove = remove
    # cf Methods.Output.XOutput.append
    if isinstance(append, ImportError):
        append = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method append: " + str(append))
            )
        )
    else:
        append = append
    # cf Methods.Output.XOutput.get_simu
    if isinstance(get_simu, ImportError):
        get_simu = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method get_simu: " + str(get_simu))
            )
        )
    else:
        get_simu = get_simu
    # cf Methods.Output.XOutput.keys
    if isinstance(keys, ImportError):
        keys = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method keys: " + str(keys))
            )
        )
    else:
        keys = keys
    # cf Methods.Output.XOutput.items
    if isinstance(items, ImportError):
        items = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method items: " + str(items))
            )
        )
    else:
        items = items
    # cf Methods.Output.XOutput.get_param_simu
    if isinstance(get_param_simu, ImportError):
        get_param_simu = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use XOutput method get_param_simu: " + str(get_param_simu)
                )
            )
        )
    else:
        get_param_simu = get_param_simu
    # cf Methods.Output.XOutput.get_param_array
    if isinstance(get_param_array, ImportError):
        get_param_array = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use XOutput method get_param_array: " + str(get_param_array)
                )
            )
        )
    else:
        get_param_array = get_param_array
    # cf Methods.Output.XOutput.plot_multi
    if isinstance(plot_multi, ImportError):
        plot_multi = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method plot_multi: " + str(plot_multi))
            )
        )
    else:
        plot_multi = plot_multi
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
        paramexplorer_list=[],
        output_list=[],
        xoutput_dict={},
        nb_simu=0,
        shape=None,
        simu=-1,
        path_res="",
        geo=-1,
        elec=-1,
        mag=-1,
        struct=-1,
        post=-1,
        logger_name="Pyleecan.Output",
        force=-1,
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

        if simu == -1:
            simu = Simulation()
        if geo == -1:
            geo = OutGeo()
        if elec == -1:
            elec = OutElec()
        if mag == -1:
            mag = OutMag()
        if struct == -1:
            struct = OutStruct()
        if post == -1:
            post = OutPost()
        if force == -1:
            force = OutForce()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            paramexplorer_list = obj.paramexplorer_list
            output_list = obj.output_list
            xoutput_dict = obj.xoutput_dict
            nb_simu = obj.nb_simu
            shape = obj.shape
            simu = obj.simu
            path_res = obj.path_res
            geo = obj.geo
            elec = obj.elec
            mag = obj.mag
            struct = obj.struct
            post = obj.post
            logger_name = obj.logger_name
            force = obj.force
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "paramexplorer_list" in list(init_dict.keys()):
                paramexplorer_list = init_dict["paramexplorer_list"]
            if "output_list" in list(init_dict.keys()):
                output_list = init_dict["output_list"]
            if "xoutput_dict" in list(init_dict.keys()):
                xoutput_dict = init_dict["xoutput_dict"]
            if "nb_simu" in list(init_dict.keys()):
                nb_simu = init_dict["nb_simu"]
            if "shape" in list(init_dict.keys()):
                shape = init_dict["shape"]
            if "simu" in list(init_dict.keys()):
                simu = init_dict["simu"]
            if "path_res" in list(init_dict.keys()):
                path_res = init_dict["path_res"]
            if "geo" in list(init_dict.keys()):
                geo = init_dict["geo"]
            if "elec" in list(init_dict.keys()):
                elec = init_dict["elec"]
            if "mag" in list(init_dict.keys()):
                mag = init_dict["mag"]
            if "struct" in list(init_dict.keys()):
                struct = init_dict["struct"]
            if "post" in list(init_dict.keys()):
                post = init_dict["post"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "force" in list(init_dict.keys()):
                force = init_dict["force"]
        # Initialisation by argument
        self.paramexplorer_list = paramexplorer_list
        self.output_list = output_list
        self.xoutput_dict = xoutput_dict
        self.nb_simu = nb_simu
        self.shape = shape
        # Call Output init
        super(XOutput, self).__init__(
            simu=simu,
            path_res=path_res,
            geo=geo,
            elec=elec,
            mag=mag,
            struct=struct,
            post=post,
            logger_name=logger_name,
            force=force,
        )
        # The class is frozen (in Output init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        XOutput_str = ""
        # Get the properties inherited from Output
        XOutput_str += super(XOutput, self).__str__()
        XOutput_str += (
            "paramexplorer_list = "
            + linesep
            + str(self.paramexplorer_list).replace(linesep, linesep + "\t")
            + linesep
        )
        XOutput_str += (
            "output_list = "
            + linesep
            + str(self.output_list).replace(linesep, linesep + "\t")
            + linesep
        )
        XOutput_str += "xoutput_dict = " + str(self.xoutput_dict) + linesep
        XOutput_str += "nb_simu = " + str(self.nb_simu) + linesep
        if self.shape is not None:
            tmp = self.shape.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            XOutput_str += "shape = " + tmp + linesep
        else:
            XOutput_str += "shape = None" + linesep
        return XOutput_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Output
        if not super(XOutput, self).__eq__(other):
            return False
        if other.paramexplorer_list != self.paramexplorer_list:
            return False
        if other.output_list != self.output_list:
            return False
        if other.xoutput_dict != self.xoutput_dict:
            return False
        if other.nb_simu != self.nb_simu:
            return False
        if other.shape != self.shape:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Output
        XOutput_dict = super(XOutput, self).as_dict()
        XOutput_dict["paramexplorer_list"] = self.paramexplorer_list
        XOutput_dict["output_list"] = self.output_list
        XOutput_dict["xoutput_dict"] = self.xoutput_dict
        XOutput_dict["nb_simu"] = self.nb_simu
        XOutput_dict["shape"] = self.shape
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        XOutput_dict["__class__"] = "XOutput"
        return XOutput_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.paramexplorer_list = None
        self.output_list = None
        self.xoutput_dict = None
        self.nb_simu = None
        self.shape = None
        # Set to None the properties inherited from Output
        super(XOutput, self)._set_None()

    def _get_paramexplorer_list(self):
        """getter of paramexplorer_list"""
        return self._paramexplorer_list

    def _set_paramexplorer_list(self, value):
        """setter of paramexplorer_list"""
        check_var("paramexplorer_list", value, "list")
        self._paramexplorer_list = value

    # List containing ParamExplorer
    # Type : list
    paramexplorer_list = property(
        fget=_get_paramexplorer_list,
        fset=_set_paramexplorer_list,
        doc=u"""List containing ParamExplorer""",
    )

    def _get_output_list(self):
        """getter of output_list"""
        return self._output_list

    def _set_output_list(self, value):
        """setter of output_list"""
        check_var("output_list", value, "list")
        self._output_list = value

    # List containing Output for each simulation
    # Type : list
    output_list = property(
        fget=_get_output_list,
        fset=_set_output_list,
        doc=u"""List containing Output for each simulation""",
    )

    def _get_xoutput_dict(self):
        """getter of xoutput_dict"""
        return self._xoutput_dict

    def _set_xoutput_dict(self, value):
        """setter of xoutput_dict"""
        check_var("xoutput_dict", value, "dict")
        self._xoutput_dict = value

    # Dictionnary containing VarParam DataKeeper results in ndarray
    # Type : dict
    xoutput_dict = property(
        fget=_get_xoutput_dict,
        fset=_set_xoutput_dict,
        doc=u"""Dictionnary containing VarParam DataKeeper results in ndarray""",
    )

    def _get_nb_simu(self):
        """getter of nb_simu"""
        return self._nb_simu

    def _set_nb_simu(self, value):
        """setter of nb_simu"""
        check_var("nb_simu", value, "int", Vmin=0)
        self._nb_simu = value

    # Number of simulations excluding reference simulation
    # Type : int, min = 0
    nb_simu = property(
        fget=_get_nb_simu,
        fset=_set_nb_simu,
        doc=u"""Number of simulations excluding reference simulation""",
    )

    def _get_shape(self):
        """getter of shape"""
        return self._shape

    def _set_shape(self, value):
        """setter of shape"""
        check_var("shape", value, "tuple")
        self._shape = value

    # Simulation shape
    # Type : tuple
    shape = property(fget=_get_shape, fset=_set_shape, doc=u"""Simulation shape""")
