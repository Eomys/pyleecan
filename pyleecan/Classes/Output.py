# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/Output.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/Output
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.Output.getter.comp_angle_rotor import comp_angle_rotor
except ImportError as error:
    comp_angle_rotor = error

try:
    from ..Methods.Output.Output.getter.get_angle_rotor_initial import (
        get_angle_rotor_initial,
    )
except ImportError as error:
    get_angle_rotor_initial = error

try:
    from ..Methods.Output.Output.getter.get_angle_rotor import get_angle_rotor
except ImportError as error:
    get_angle_rotor = error

try:
    from ..Methods.Output.Output.getter.get_BH_rotor import get_BH_rotor
except ImportError as error:
    get_BH_rotor = error

try:
    from ..Methods.Output.Output.getter.get_BH_stator import get_BH_stator
except ImportError as error:
    get_BH_stator = error

try:
    from ..Methods.Output.Output.getter.get_path_result import get_path_result
except ImportError as error:
    get_path_result = error

try:
    from ..Methods.Output.Output.getter.get_machine_periodicity import (
        get_machine_periodicity,
    )
except ImportError as error:
    get_machine_periodicity = error

try:
    from ..Methods.Output.Output.getter.get_fund_harm import get_fund_harm
except ImportError as error:
    get_fund_harm = error

try:
    from ..Methods.Output.Output.getter.get_data_from_str import get_data_from_str
except ImportError as error:
    get_data_from_str = error

try:
    from ..Methods.Output.Output.getter.export_to_mat import export_to_mat
except ImportError as error:
    export_to_mat = error

try:
    from ..Methods.Output.Output.plot.Magnetic.plot_B_mesh import plot_B_mesh
except ImportError as error:
    plot_B_mesh = error

try:
    from ..Methods.Output.Output.print_memory import print_memory
except ImportError as error:
    print_memory = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Output(FrozenClass):
    """Main Output object: gather all the outputs of all the modules"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.Output.getter.comp_angle_rotor
    if isinstance(comp_angle_rotor, ImportError):
        comp_angle_rotor = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method comp_angle_rotor: " + str(comp_angle_rotor)
                )
            )
        )
    else:
        comp_angle_rotor = comp_angle_rotor
    # cf Methods.Output.Output.getter.get_angle_rotor_initial
    if isinstance(get_angle_rotor_initial, ImportError):
        get_angle_rotor_initial = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method get_angle_rotor_initial: "
                    + str(get_angle_rotor_initial)
                )
            )
        )
    else:
        get_angle_rotor_initial = get_angle_rotor_initial
    # cf Methods.Output.Output.getter.get_angle_rotor
    if isinstance(get_angle_rotor, ImportError):
        get_angle_rotor = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method get_angle_rotor: " + str(get_angle_rotor)
                )
            )
        )
    else:
        get_angle_rotor = get_angle_rotor
    # cf Methods.Output.Output.getter.get_BH_rotor
    if isinstance(get_BH_rotor, ImportError):
        get_BH_rotor = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method get_BH_rotor: " + str(get_BH_rotor)
                )
            )
        )
    else:
        get_BH_rotor = get_BH_rotor
    # cf Methods.Output.Output.getter.get_BH_stator
    if isinstance(get_BH_stator, ImportError):
        get_BH_stator = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method get_BH_stator: " + str(get_BH_stator)
                )
            )
        )
    else:
        get_BH_stator = get_BH_stator
    # cf Methods.Output.Output.getter.get_path_result
    if isinstance(get_path_result, ImportError):
        get_path_result = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method get_path_result: " + str(get_path_result)
                )
            )
        )
    else:
        get_path_result = get_path_result
    # cf Methods.Output.Output.getter.get_machine_periodicity
    if isinstance(get_machine_periodicity, ImportError):
        get_machine_periodicity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method get_machine_periodicity: "
                    + str(get_machine_periodicity)
                )
            )
        )
    else:
        get_machine_periodicity = get_machine_periodicity
    # cf Methods.Output.Output.getter.get_fund_harm
    if isinstance(get_fund_harm, ImportError):
        get_fund_harm = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method get_fund_harm: " + str(get_fund_harm)
                )
            )
        )
    else:
        get_fund_harm = get_fund_harm
    # cf Methods.Output.Output.getter.get_data_from_str
    if isinstance(get_data_from_str, ImportError):
        get_data_from_str = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method get_data_from_str: "
                    + str(get_data_from_str)
                )
            )
        )
    else:
        get_data_from_str = get_data_from_str
    # cf Methods.Output.Output.getter.export_to_mat
    if isinstance(export_to_mat, ImportError):
        export_to_mat = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method export_to_mat: " + str(export_to_mat)
                )
            )
        )
    else:
        export_to_mat = export_to_mat
    # cf Methods.Output.Output.plot.Magnetic.plot_B_mesh
    if isinstance(plot_B_mesh, ImportError):
        plot_B_mesh = property(
            fget=lambda x: raise_(
                ImportError("Can't use Output method plot_B_mesh: " + str(plot_B_mesh))
            )
        )
    else:
        plot_B_mesh = plot_B_mesh
    # cf Methods.Output.Output.print_memory
    if isinstance(print_memory, ImportError):
        print_memory = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method print_memory: " + str(print_memory)
                )
            )
        )
    else:
        print_memory = print_memory
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
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
        self.parent = None
        self.simu = simu
        self.path_result = path_result
        self.geo = geo
        self.elec = elec
        self.mag = mag
        self.struct = struct
        self.post = post
        self.logger_name = logger_name
        self.force = force
        self.loss = loss

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Output_str = ""
        if self.parent is None:
            Output_str += "parent = None " + linesep
        else:
            Output_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.simu is not None:
            tmp = self.simu.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "simu = " + tmp
        else:
            Output_str += "simu = None" + linesep + linesep
        Output_str += 'path_result = "' + str(self.path_result) + '"' + linesep
        if self.geo is not None:
            tmp = self.geo.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "geo = " + tmp
        else:
            Output_str += "geo = None" + linesep + linesep
        if self.elec is not None:
            tmp = self.elec.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "elec = " + tmp
        else:
            Output_str += "elec = None" + linesep + linesep
        if self.mag is not None:
            tmp = self.mag.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "mag = " + tmp
        else:
            Output_str += "mag = None" + linesep + linesep
        if self.struct is not None:
            tmp = self.struct.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "struct = " + tmp
        else:
            Output_str += "struct = None" + linesep + linesep
        if self.post is not None:
            tmp = self.post.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "post = " + tmp
        else:
            Output_str += "post = None" + linesep + linesep
        Output_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        if self.force is not None:
            tmp = self.force.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "force = " + tmp
        else:
            Output_str += "force = None" + linesep + linesep
        if self.loss is not None:
            tmp = self.loss.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "loss = " + tmp
        else:
            Output_str += "loss = None" + linesep + linesep
        return Output_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.simu != self.simu:
            return False
        if other.path_result != self.path_result:
            return False
        if other.geo != self.geo:
            return False
        if other.elec != self.elec:
            return False
        if other.mag != self.mag:
            return False
        if other.struct != self.struct:
            return False
        if other.post != self.post:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.force != self.force:
            return False
        if other.loss != self.loss:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (other.simu is None and self.simu is not None) or (
            other.simu is not None and self.simu is None
        ):
            diff_list.append(name + ".simu None mismatch")
        elif self.simu is not None:
            diff_list.extend(
                self.simu.compare(
                    other.simu,
                    name=name + ".simu",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other._path_result != self._path_result:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._path_result)
                    + ", other="
                    + str(other._path_result)
                    + ")"
                )
                diff_list.append(name + ".path_result" + val_str)
            else:
                diff_list.append(name + ".path_result")
        if (other.geo is None and self.geo is not None) or (
            other.geo is not None and self.geo is None
        ):
            diff_list.append(name + ".geo None mismatch")
        elif self.geo is not None:
            diff_list.extend(
                self.geo.compare(
                    other.geo,
                    name=name + ".geo",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.elec is None and self.elec is not None) or (
            other.elec is not None and self.elec is None
        ):
            diff_list.append(name + ".elec None mismatch")
        elif self.elec is not None:
            diff_list.extend(
                self.elec.compare(
                    other.elec,
                    name=name + ".elec",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.mag is None and self.mag is not None) or (
            other.mag is not None and self.mag is None
        ):
            diff_list.append(name + ".mag None mismatch")
        elif self.mag is not None:
            diff_list.extend(
                self.mag.compare(
                    other.mag,
                    name=name + ".mag",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.struct is None and self.struct is not None) or (
            other.struct is not None and self.struct is None
        ):
            diff_list.append(name + ".struct None mismatch")
        elif self.struct is not None:
            diff_list.extend(
                self.struct.compare(
                    other.struct,
                    name=name + ".struct",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.post is None and self.post is not None) or (
            other.post is not None and self.post is None
        ):
            diff_list.append(name + ".post None mismatch")
        elif self.post is not None:
            diff_list.extend(
                self.post.compare(
                    other.post,
                    name=name + ".post",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other._logger_name != self._logger_name:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._logger_name)
                    + ", other="
                    + str(other._logger_name)
                    + ")"
                )
                diff_list.append(name + ".logger_name" + val_str)
            else:
                diff_list.append(name + ".logger_name")
        if (other.force is None and self.force is not None) or (
            other.force is not None and self.force is None
        ):
            diff_list.append(name + ".force None mismatch")
        elif self.force is not None:
            diff_list.extend(
                self.force.compare(
                    other.force,
                    name=name + ".force",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.loss is None and self.loss is not None) or (
            other.loss is not None and self.loss is None
        ):
            diff_list.append(name + ".loss None mismatch")
        elif self.loss is not None:
            diff_list.extend(
                self.loss.compare(
                    other.loss,
                    name=name + ".loss",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.simu)
        S += getsizeof(self.path_result)
        S += getsizeof(self.geo)
        S += getsizeof(self.elec)
        S += getsizeof(self.mag)
        S += getsizeof(self.struct)
        S += getsizeof(self.post)
        S += getsizeof(self.logger_name)
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

        Output_dict = dict()
        if self.simu is None:
            Output_dict["simu"] = None
        else:
            Output_dict["simu"] = self.simu.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Output_dict["path_result"] = self.path_result
        if self.geo is None:
            Output_dict["geo"] = None
        else:
            Output_dict["geo"] = self.geo.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.elec is None:
            Output_dict["elec"] = None
        else:
            Output_dict["elec"] = self.elec.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.mag is None:
            Output_dict["mag"] = None
        else:
            Output_dict["mag"] = self.mag.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.struct is None:
            Output_dict["struct"] = None
        else:
            Output_dict["struct"] = self.struct.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.post is None:
            Output_dict["post"] = None
        else:
            Output_dict["post"] = self.post.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Output_dict["logger_name"] = self.logger_name
        if self.force is None:
            Output_dict["force"] = None
        else:
            Output_dict["force"] = self.force.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.loss is None:
            Output_dict["loss"] = None
        else:
            Output_dict["loss"] = self.loss.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        Output_dict["__class__"] = "Output"
        return Output_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.simu is None:
            simu_val = None
        else:
            simu_val = self.simu.copy()
        path_result_val = self.path_result
        if self.geo is None:
            geo_val = None
        else:
            geo_val = self.geo.copy()
        if self.elec is None:
            elec_val = None
        else:
            elec_val = self.elec.copy()
        if self.mag is None:
            mag_val = None
        else:
            mag_val = self.mag.copy()
        if self.struct is None:
            struct_val = None
        else:
            struct_val = self.struct.copy()
        if self.post is None:
            post_val = None
        else:
            post_val = self.post.copy()
        logger_name_val = self.logger_name
        if self.force is None:
            force_val = None
        else:
            force_val = self.force.copy()
        if self.loss is None:
            loss_val = None
        else:
            loss_val = self.loss.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            simu=simu_val,
            path_result=path_result_val,
            geo=geo_val,
            elec=elec_val,
            mag=mag_val,
            struct=struct_val,
            post=post_val,
            logger_name=logger_name_val,
            force=force_val,
            loss=loss_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.simu is not None:
            self.simu._set_None()
        self.path_result = None
        if self.geo is not None:
            self.geo._set_None()
        if self.elec is not None:
            self.elec._set_None()
        if self.mag is not None:
            self.mag._set_None()
        if self.struct is not None:
            self.struct._set_None()
        if self.post is not None:
            self.post._set_None()
        self.logger_name = None
        if self.force is not None:
            self.force._set_None()
        if self.loss is not None:
            self.loss._set_None()

    def _get_simu(self):
        """getter of simu"""
        return self._simu

    def _set_simu(self, value):
        """setter of simu"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "simu")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Simulation = import_class("pyleecan.Classes", "Simulation", "simu")
            value = Simulation()
        check_var("simu", value, "Simulation")
        self._simu = value

        if self._simu is not None:
            self._simu.parent = self

    simu = property(
        fget=_get_simu,
        fset=_set_simu,
        doc=u"""Simulation object that generated the Output

        :Type: Simulation
        """,
    )

    def _get_path_result(self):
        """getter of path_result"""
        return self._path_result

    def _set_path_result(self, value):
        """setter of path_result"""
        check_var("path_result", value, "str")
        self._path_result = value

    path_result = property(
        fget=_get_path_result,
        fset=_set_path_result,
        doc=u"""Path to the folder to same the results

        :Type: str
        """,
    )

    def _get_geo(self):
        """getter of geo"""
        return self._geo

    def _set_geo(self, value):
        """setter of geo"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "geo")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            OutGeo = import_class("pyleecan.Classes", "OutGeo", "geo")
            value = OutGeo()
        check_var("geo", value, "OutGeo")
        self._geo = value

        if self._geo is not None:
            self._geo.parent = self

    geo = property(
        fget=_get_geo,
        fset=_set_geo,
        doc=u"""Geometry output

        :Type: OutGeo
        """,
    )

    def _get_elec(self):
        """getter of elec"""
        return self._elec

    def _set_elec(self, value):
        """setter of elec"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "elec")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            OutElec = import_class("pyleecan.Classes", "OutElec", "elec")
            value = OutElec()
        check_var("elec", value, "OutElec")
        self._elec = value

        if self._elec is not None:
            self._elec.parent = self

    elec = property(
        fget=_get_elec,
        fset=_set_elec,
        doc=u"""Electrical module output

        :Type: OutElec
        """,
    )

    def _get_mag(self):
        """getter of mag"""
        return self._mag

    def _set_mag(self, value):
        """setter of mag"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "mag")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            OutMag = import_class("pyleecan.Classes", "OutMag", "mag")
            value = OutMag()
        check_var("mag", value, "OutMag")
        self._mag = value

        if self._mag is not None:
            self._mag.parent = self

    mag = property(
        fget=_get_mag,
        fset=_set_mag,
        doc=u"""Magnetic module output

        :Type: OutMag
        """,
    )

    def _get_struct(self):
        """getter of struct"""
        return self._struct

    def _set_struct(self, value):
        """setter of struct"""
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
                "pyleecan.Classes", value.get("__class__"), "struct"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            OutStruct = import_class("pyleecan.Classes", "OutStruct", "struct")
            value = OutStruct()
        check_var("struct", value, "OutStruct")
        self._struct = value

        if self._struct is not None:
            self._struct.parent = self

    struct = property(
        fget=_get_struct,
        fset=_set_struct,
        doc=u"""Structural module output

        :Type: OutStruct
        """,
    )

    def _get_post(self):
        """getter of post"""
        return self._post

    def _set_post(self, value):
        """setter of post"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "post")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            OutPost = import_class("pyleecan.Classes", "OutPost", "post")
            value = OutPost()
        check_var("post", value, "OutPost")
        self._post = value

        if self._post is not None:
            self._post.parent = self

    post = property(
        fget=_get_post,
        fset=_set_post,
        doc=u"""Post-Processing settings

        :Type: OutPost
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

    def _get_force(self):
        """getter of force"""
        return self._force

    def _set_force(self, value):
        """setter of force"""
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
                "pyleecan.Classes", value.get("__class__"), "force"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            OutForce = import_class("pyleecan.Classes", "OutForce", "force")
            value = OutForce()
        check_var("force", value, "OutForce")
        self._force = value

        if self._force is not None:
            self._force.parent = self

    force = property(
        fget=_get_force,
        fset=_set_force,
        doc=u"""Force module output

        :Type: OutForce
        """,
    )

    def _get_loss(self):
        """getter of loss"""
        return self._loss

    def _set_loss(self, value):
        """setter of loss"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "loss")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            OutLoss = import_class("pyleecan.Classes", "OutLoss", "loss")
            value = OutLoss()
        check_var("loss", value, "OutLoss")
        self._loss = value

        if self._loss is not None:
            self._loss.parent = self

    loss = property(
        fget=_get_loss,
        fset=_set_loss,
        doc=u"""Loss module output

        :Type: OutLoss
        """,
    )
