# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/XOutput.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/XOutput
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
    from ..Methods.Output.XOutput.append import append
except ImportError as error:
    append = error

try:
    from ..Methods.Output.XOutput.count import count
except ImportError as error:
    count = error

try:
    from ..Methods.Output.XOutput.get_param_simu import get_param_simu
except ImportError as error:
    get_param_simu = error

try:
    from ..Methods.Output.XOutput.get_paramexplorer import get_paramexplorer
except ImportError as error:
    get_paramexplorer = error

try:
    from ..Methods.Output.XOutput.get_pareto_index import get_pareto_index
except ImportError as error:
    get_pareto_index = error

try:
    from ..Methods.Output.XOutput.get_simu import get_simu
except ImportError as error:
    get_simu = error

try:
    from ..Methods.Output.XOutput.get_symbol_list import get_symbol_list
except ImportError as error:
    get_symbol_list = error

try:
    from ..Methods.Output.XOutput.get_xoutput_ref import get_xoutput_ref
except ImportError as error:
    get_xoutput_ref = error

try:
    from ..Methods.Output.XOutput.insert import insert
except ImportError as error:
    insert = error

try:
    from ..Methods.Output.XOutput.items import items
except ImportError as error:
    items = error

try:
    from ..Methods.Output.XOutput.keys import keys
except ImportError as error:
    keys = error

try:
    from ..Methods.Output.XOutput.plot_generation import plot_generation
except ImportError as error:
    plot_generation = error

try:
    from ..Methods.Output.XOutput.plot_multi import plot_multi
except ImportError as error:
    plot_multi = error

try:
    from ..Methods.Output.XOutput.plot_pareto import plot_pareto
except ImportError as error:
    plot_pareto = error

try:
    from ..Methods.Output.XOutput.pop import pop
except ImportError as error:
    pop = error

try:
    from ..Methods.Output.XOutput.print_memory import print_memory
except ImportError as error:
    print_memory = error

try:
    from ..Methods.Output.XOutput.remove import remove
except ImportError as error:
    remove = error


from ._check import InitUnKnowClassError
from .ParamExplorer import ParamExplorer
from .Output import Output
from .DataKeeper import DataKeeper
from .Simulation import Simulation
from .OutGeo import OutGeo
from .OutElec import OutElec
from .OutMag import OutMag
from .OutStruct import OutStruct
from .OutPost import OutPost
from .OutForce import OutForce
from .OutLoss import OutLoss


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
    # cf Methods.Output.XOutput.append
    if isinstance(append, ImportError):
        append = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method append: " + str(append))
            )
        )
    else:
        append = append
    # cf Methods.Output.XOutput.count
    if isinstance(count, ImportError):
        count = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method count: " + str(count))
            )
        )
    else:
        count = count
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
    # cf Methods.Output.XOutput.get_paramexplorer
    if isinstance(get_paramexplorer, ImportError):
        get_paramexplorer = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use XOutput method get_paramexplorer: "
                    + str(get_paramexplorer)
                )
            )
        )
    else:
        get_paramexplorer = get_paramexplorer
    # cf Methods.Output.XOutput.get_pareto_index
    if isinstance(get_pareto_index, ImportError):
        get_pareto_index = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use XOutput method get_pareto_index: "
                    + str(get_pareto_index)
                )
            )
        )
    else:
        get_pareto_index = get_pareto_index
    # cf Methods.Output.XOutput.get_simu
    if isinstance(get_simu, ImportError):
        get_simu = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method get_simu: " + str(get_simu))
            )
        )
    else:
        get_simu = get_simu
    # cf Methods.Output.XOutput.get_symbol_list
    if isinstance(get_symbol_list, ImportError):
        get_symbol_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use XOutput method get_symbol_list: " + str(get_symbol_list)
                )
            )
        )
    else:
        get_symbol_list = get_symbol_list
    # cf Methods.Output.XOutput.get_xoutput_ref
    if isinstance(get_xoutput_ref, ImportError):
        get_xoutput_ref = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use XOutput method get_xoutput_ref: " + str(get_xoutput_ref)
                )
            )
        )
    else:
        get_xoutput_ref = get_xoutput_ref
    # cf Methods.Output.XOutput.insert
    if isinstance(insert, ImportError):
        insert = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method insert: " + str(insert))
            )
        )
    else:
        insert = insert
    # cf Methods.Output.XOutput.items
    if isinstance(items, ImportError):
        items = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method items: " + str(items))
            )
        )
    else:
        items = items
    # cf Methods.Output.XOutput.keys
    if isinstance(keys, ImportError):
        keys = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method keys: " + str(keys))
            )
        )
    else:
        keys = keys
    # cf Methods.Output.XOutput.plot_generation
    if isinstance(plot_generation, ImportError):
        plot_generation = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use XOutput method plot_generation: " + str(plot_generation)
                )
            )
        )
    else:
        plot_generation = plot_generation
    # cf Methods.Output.XOutput.plot_multi
    if isinstance(plot_multi, ImportError):
        plot_multi = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method plot_multi: " + str(plot_multi))
            )
        )
    else:
        plot_multi = plot_multi
    # cf Methods.Output.XOutput.plot_pareto
    if isinstance(plot_pareto, ImportError):
        plot_pareto = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method plot_pareto: " + str(plot_pareto))
            )
        )
    else:
        plot_pareto = plot_pareto
    # cf Methods.Output.XOutput.pop
    if isinstance(pop, ImportError):
        pop = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method pop: " + str(pop))
            )
        )
    else:
        pop = pop
    # cf Methods.Output.XOutput.print_memory
    if isinstance(print_memory, ImportError):
        print_memory = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use XOutput method print_memory: " + str(print_memory)
                )
            )
        )
    else:
        print_memory = print_memory
    # cf Methods.Output.XOutput.remove
    if isinstance(remove, ImportError):
        remove = property(
            fget=lambda x: raise_(
                ImportError("Can't use XOutput method remove: " + str(remove))
            )
        )
    else:
        remove = remove
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        paramexplorer_list=-1,
        output_list=-1,
        xoutput_dict=-1,
        nb_simu=0,
        xoutput_ref=None,
        xoutput_ref_index=None,
        simu=-1,
        path_result="",
        geo=-1,
        elec=-1,
        mag=-1,
        struct=-1,
        post=-1,
        logger_name="Pyleecan.Output",
        force=-1,
        loss=-1,
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
            if "paramexplorer_list" in list(init_dict.keys()):
                paramexplorer_list = init_dict["paramexplorer_list"]
            if "output_list" in list(init_dict.keys()):
                output_list = init_dict["output_list"]
            if "xoutput_dict" in list(init_dict.keys()):
                xoutput_dict = init_dict["xoutput_dict"]
            if "nb_simu" in list(init_dict.keys()):
                nb_simu = init_dict["nb_simu"]
            if "xoutput_ref" in list(init_dict.keys()):
                xoutput_ref = init_dict["xoutput_ref"]
            if "xoutput_ref_index" in list(init_dict.keys()):
                xoutput_ref_index = init_dict["xoutput_ref_index"]
            if "simu" in list(init_dict.keys()):
                simu = init_dict["simu"]
            if "path_result" in list(init_dict.keys()):
                path_result = init_dict["path_result"]
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
            if "loss" in list(init_dict.keys()):
                loss = init_dict["loss"]
        # Set the properties (value check and convertion are done in setter)
        self.paramexplorer_list = paramexplorer_list
        self.output_list = output_list
        self.xoutput_dict = xoutput_dict
        self.nb_simu = nb_simu
        self.xoutput_ref = xoutput_ref
        self.xoutput_ref_index = xoutput_ref_index
        # Call Output init
        super(XOutput, self).__init__(
            simu=simu,
            path_result=path_result,
            geo=geo,
            elec=elec,
            mag=mag,
            struct=struct,
            post=post,
            logger_name=logger_name,
            force=force,
            loss=loss,
        )
        # The class is frozen (in Output init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        XOutput_str = ""
        # Get the properties inherited from Output
        XOutput_str += super(XOutput, self).__str__()
        if len(self.paramexplorer_list) == 0:
            XOutput_str += "paramexplorer_list = []" + linesep
        for ii in range(len(self.paramexplorer_list)):
            tmp = (
                self.paramexplorer_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            XOutput_str += (
                "paramexplorer_list[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        if len(self.output_list) == 0:
            XOutput_str += "output_list = []" + linesep
        for ii in range(len(self.output_list)):
            tmp = (
                self.output_list[ii].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            XOutput_str += "output_list[" + str(ii) + "] =" + tmp + linesep + linesep
        if len(self.xoutput_dict) == 0:
            XOutput_str += "xoutput_dict = dict()" + linesep
        for key, obj in self.xoutput_dict.items():
            tmp = (
                self.xoutput_dict[key].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            XOutput_str += "xoutput_dict[" + key + "] =" + tmp + linesep + linesep
        XOutput_str += "nb_simu = " + str(self.nb_simu) + linesep
        if self.xoutput_ref is not None:
            tmp = (
                self.xoutput_ref.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            XOutput_str += "xoutput_ref = " + tmp
        else:
            XOutput_str += "xoutput_ref = None" + linesep + linesep
        XOutput_str += "xoutput_ref_index = " + str(self.xoutput_ref_index) + linesep
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
        if other.xoutput_ref != self.xoutput_ref:
            return False
        if other.xoutput_ref_index != self.xoutput_ref_index:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Output
        diff_list.extend(super(XOutput, self).compare(other, name=name))
        if (
            other.paramexplorer_list is None and self.paramexplorer_list is not None
        ) or (other.paramexplorer_list is not None and self.paramexplorer_list is None):
            diff_list.append(name + ".paramexplorer_list None mismatch")
        elif self.paramexplorer_list is None:
            pass
        elif len(other.paramexplorer_list) != len(self.paramexplorer_list):
            diff_list.append("len(" + name + ".paramexplorer_list)")
        else:
            for ii in range(len(other.paramexplorer_list)):
                diff_list.extend(
                    self.paramexplorer_list[ii].compare(
                        other.paramexplorer_list[ii],
                        name=name + ".paramexplorer_list[" + str(ii) + "]",
                    )
                )
        if (other.output_list is None and self.output_list is not None) or (
            other.output_list is not None and self.output_list is None
        ):
            diff_list.append(name + ".output_list None mismatch")
        elif self.output_list is None:
            pass
        elif len(other.output_list) != len(self.output_list):
            diff_list.append("len(" + name + ".output_list)")
        else:
            for ii in range(len(other.output_list)):
                diff_list.extend(
                    self.output_list[ii].compare(
                        other.output_list[ii],
                        name=name + ".output_list[" + str(ii) + "]",
                    )
                )
        if (other.xoutput_dict is None and self.xoutput_dict is not None) or (
            other.xoutput_dict is not None and self.xoutput_dict is None
        ):
            diff_list.append(name + ".xoutput_dict None mismatch")
        elif self.xoutput_dict is None:
            pass
        elif len(other.xoutput_dict) != len(self.xoutput_dict):
            diff_list.append("len(" + name + "xoutput_dict)")
        else:
            for key in self.xoutput_dict:
                diff_list.extend(
                    self.xoutput_dict[key].compare(
                        other.xoutput_dict[key], name=name + ".xoutput_dict"
                    )
                )
        if other._nb_simu != self._nb_simu:
            diff_list.append(name + ".nb_simu")
        if (other.xoutput_ref is None and self.xoutput_ref is not None) or (
            other.xoutput_ref is not None and self.xoutput_ref is None
        ):
            diff_list.append(name + ".xoutput_ref None mismatch")
        elif self.xoutput_ref is not None:
            diff_list.extend(
                self.xoutput_ref.compare(other.xoutput_ref, name=name + ".xoutput_ref")
            )
        if other._xoutput_ref_index != self._xoutput_ref_index:
            diff_list.append(name + ".xoutput_ref_index")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Output
        S += super(XOutput, self).__sizeof__()
        if self.paramexplorer_list is not None:
            for value in self.paramexplorer_list:
                S += getsizeof(value)
        if self.output_list is not None:
            for value in self.output_list:
                S += getsizeof(value)
        if self.xoutput_dict is not None:
            for key, value in self.xoutput_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.nb_simu)
        S += getsizeof(self.xoutput_ref)
        S += getsizeof(self.xoutput_ref_index)
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

        # Get the properties inherited from Output
        XOutput_dict = super(XOutput, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.paramexplorer_list is None:
            XOutput_dict["paramexplorer_list"] = None
        else:
            XOutput_dict["paramexplorer_list"] = list()
            for obj in self.paramexplorer_list:
                if obj is not None:
                    XOutput_dict["paramexplorer_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    XOutput_dict["paramexplorer_list"].append(None)
        if self.output_list is None:
            XOutput_dict["output_list"] = None
        else:
            XOutput_dict["output_list"] = list()
            for obj in self.output_list:
                if obj is not None:
                    XOutput_dict["output_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    XOutput_dict["output_list"].append(None)
        if self.xoutput_dict is None:
            XOutput_dict["xoutput_dict"] = None
        else:
            XOutput_dict["xoutput_dict"] = dict()
            for key, obj in self.xoutput_dict.items():
                if obj is not None:
                    XOutput_dict["xoutput_dict"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    XOutput_dict["xoutput_dict"][key] = None
        XOutput_dict["nb_simu"] = self.nb_simu
        if self.xoutput_ref is None:
            XOutput_dict["xoutput_ref"] = None
        else:
            XOutput_dict["xoutput_ref"] = self.xoutput_ref.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        XOutput_dict["xoutput_ref_index"] = self.xoutput_ref_index
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        XOutput_dict["__class__"] = "XOutput"
        return XOutput_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.paramexplorer_list = None
        self.output_list = None
        self.xoutput_dict = None
        self.nb_simu = None
        if self.xoutput_ref is not None:
            self.xoutput_ref._set_None()
        self.xoutput_ref_index = None
        # Set to None the properties inherited from Output
        super(XOutput, self)._set_None()

    def _get_paramexplorer_list(self):
        """getter of paramexplorer_list"""
        if self._paramexplorer_list is not None:
            for obj in self._paramexplorer_list:
                if obj is not None:
                    obj.parent = self
        return self._paramexplorer_list

    def _set_paramexplorer_list(self, value):
        """setter of paramexplorer_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "paramexplorer_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("paramexplorer_list", value, "[ParamExplorer]")
        self._paramexplorer_list = value

    paramexplorer_list = property(
        fget=_get_paramexplorer_list,
        fset=_set_paramexplorer_list,
        doc=u"""List containing ParamExplorer

        :Type: [ParamExplorer]
        """,
    )

    def _get_output_list(self):
        """getter of output_list"""
        if self._output_list is not None:
            for obj in self._output_list:
                if obj is not None:
                    obj.parent = self
        return self._output_list

    def _set_output_list(self, value):
        """setter of output_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "output_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("output_list", value, "[Output]")
        self._output_list = value

    output_list = property(
        fget=_get_output_list,
        fset=_set_output_list,
        doc=u"""List containing Output (or Xoutput) for each simulation

        :Type: [Output]
        """,
    )

    def _get_xoutput_dict(self):
        """getter of xoutput_dict"""
        if self._xoutput_dict is not None:
            for key, obj in self._xoutput_dict.items():
                if obj is not None:
                    obj.parent = self
        return self._xoutput_dict

    def _set_xoutput_dict(self, value):
        """setter of xoutput_dict"""
        if type(value) is dict:
            for key, obj in value.items():
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "xoutput_dict"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("xoutput_dict", value, "{DataKeeper}")
        self._xoutput_dict = value

    xoutput_dict = property(
        fget=_get_xoutput_dict,
        fset=_set_xoutput_dict,
        doc=u"""dictionary containing DataKeeper

        :Type: {DataKeeper}
        """,
    )

    def _get_nb_simu(self):
        """getter of nb_simu"""
        return self._nb_simu

    def _set_nb_simu(self, value):
        """setter of nb_simu"""
        check_var("nb_simu", value, "int", Vmin=0)
        self._nb_simu = value

    nb_simu = property(
        fget=_get_nb_simu,
        fset=_set_nb_simu,
        doc=u"""Number of simulations excluding reference simulation

        :Type: int
        :min: 0
        """,
    )

    def _get_xoutput_ref(self):
        """getter of xoutput_ref"""
        return self._xoutput_ref

    def _set_xoutput_ref(self, value):
        """setter of xoutput_ref"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "xoutput_ref"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Output()
        check_var("xoutput_ref", value, "Output")
        self._xoutput_ref = value

        if self._xoutput_ref is not None:
            self._xoutput_ref.parent = self

    xoutput_ref = property(
        fget=_get_xoutput_ref,
        fset=_set_xoutput_ref,
        doc=u"""Xoutput (or Output) of the reference simulation (only if is_keep_all_output is True and not included in output_list)

        :Type: Output
        """,
    )

    def _get_xoutput_ref_index(self):
        """getter of xoutput_ref_index"""
        return self._xoutput_ref_index

    def _set_xoutput_ref_index(self, value):
        """setter of xoutput_ref_index"""
        check_var("xoutput_ref_index", value, "int")
        self._xoutput_ref_index = value

    xoutput_ref_index = property(
        fget=_get_xoutput_ref_index,
        fset=_set_xoutput_ref_index,
        doc=u"""Index of the Xoutput (or Output) of the reference simulation in the output_list (only if is_keep_all_output is True)

        :Type: int
        """,
    )
