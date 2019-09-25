# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Methods.Output.Output.getter.get_BH_stator import get_BH_stator
from pyleecan.Methods.Output.Output.getter.get_BH_rotor import get_BH_rotor
from pyleecan.Methods.Output.Output.getter.get_path_result import get_path_result
from pyleecan.Methods.Output.Output.getter.get_angle_rotor import get_angle_rotor
from pyleecan.Methods.Output.Output.plot.Magnetic.plot_B_space import plot_B_space
from pyleecan.Methods.Output.Output.plot.Structural.plot_force_space import plot_force_space

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Simulation import Simulation
from pyleecan.Classes.OutGeo import OutGeo
from pyleecan.Classes.OutElec import OutElec
from pyleecan.Classes.OutMag import OutMag
from pyleecan.Classes.OutStruct import OutStruct
from pyleecan.Classes.OutPost import OutPost



class Output(FrozenClass):
    """Main Output object: gather all the outputs of all the modules"""

    VERSION = 1

    # cf Methods.Output.Output.getter.get_BH_stator
    get_BH_stator = get_BH_stator
    # cf Methods.Output.Output.getter.get_BH_rotor
    get_BH_rotor = get_BH_rotor
    # cf Methods.Output.Output.getter.get_path_result
    get_path_result = get_path_result
    # cf Methods.Output.Output.getter.get_angle_rotor
    get_angle_rotor = get_angle_rotor
    # cf Methods.Output.Output.plot.Magnetic.plot_B_space
    plot_B_space = plot_B_space
    # cf Methods.Output.Output.plot.Structural.plot_force_space
    plot_force_space = plot_force_space
    # save method is available in all object
    save = save

    def __init__(self, simu=-1, path_res="", geo=-1, elec=-1, mag=-1, struct=-1, post=-1, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

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
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["simu", "path_res", "geo", "elec", "mag", "struct", "post"])
            # Overwrite default value with init_dict content
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
        # Initialisation by argument
        self.parent = None
        # simu can be None, a Simulation object or a dict
        if isinstance(simu, dict):
            # Check that the type is correct (including daughter)
            class_name = simu.get('__class__')
            if class_name not in ['Simulation', 'Simu1']:
                raise InitUnKnowClassError("Unknow class name "+class_name+" in init_dict for " + prop_name)
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes."+class_name, fromlist=[class_name])
            class_obj = getattr(module,class_name)
            self.simu = class_obj(init_dict=simu)
        else:
            self.simu = simu
        self.path_res = path_res
        # geo can be None, a OutGeo object or a dict
        if isinstance(geo, dict):
            self.geo = OutGeo(init_dict=geo)
        else:
            self.geo = geo
        # elec can be None, a OutElec object or a dict
        if isinstance(elec, dict):
            self.elec = OutElec(init_dict=elec)
        else:
            self.elec = elec
        # mag can be None, a OutMag object or a dict
        if isinstance(mag, dict):
            self.mag = OutMag(init_dict=mag)
        else:
            self.mag = mag
        # struct can be None, a OutStruct object or a dict
        if isinstance(struct, dict):
            self.struct = OutStruct(init_dict=struct)
        else:
            self.struct = struct
        # post can be None, a OutPost object or a dict
        if isinstance(post, dict):
            self.post = OutPost(init_dict=post)
        else:
            self.post = post

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Output_str = ""
        if self.parent is None:
            Output_str += "parent = None " + linesep
        else:
            Output_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Output_str += "simu = " + str(self.simu.as_dict()) + linesep + linesep
        Output_str += 'path_res = "' + str(self.path_res) + '"' + linesep
        Output_str += "geo = " + str(self.geo.as_dict()) + linesep + linesep
        Output_str += "elec = " + str(self.elec.as_dict()) + linesep + linesep
        Output_str += "mag = " + str(self.mag.as_dict()) + linesep + linesep
        Output_str += "struct = " + str(self.struct.as_dict()) + linesep + linesep
        Output_str += "post = " + str(self.post.as_dict())
        return Output_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.simu != self.simu:
            return False
        if other.path_res != self.path_res:
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
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Output_dict = dict()
        if self.simu is None:
            Output_dict["simu"] = None
        else:
            Output_dict["simu"] = self.simu.as_dict()
        Output_dict["path_res"] = self.path_res
        if self.geo is None:
            Output_dict["geo"] = None
        else:
            Output_dict["geo"] = self.geo.as_dict()
        if self.elec is None:
            Output_dict["elec"] = None
        else:
            Output_dict["elec"] = self.elec.as_dict()
        if self.mag is None:
            Output_dict["mag"] = None
        else:
            Output_dict["mag"] = self.mag.as_dict()
        if self.struct is None:
            Output_dict["struct"] = None
        else:
            Output_dict["struct"] = self.struct.as_dict()
        if self.post is None:
            Output_dict["post"] = None
        else:
            Output_dict["post"] = self.post.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        Output_dict["__class__"] = "Output"
        return Output_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.simu is not None:
            self.simu._set_None()
        self.path_res = None
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

    def _get_simu(self):
        """getter of simu"""
        return self._simu

    def _set_simu(self, value):
        """setter of simu"""
        check_var("simu", value, "Simulation")
        self._simu = value

        if self._simu is not None:
            self._simu.parent = self
    # Simulation object that generated the Output
    # Type : Simulation
    simu = property(fget=_get_simu, fset=_set_simu,
                    doc=u"""Simulation object that generated the Output""")

    def _get_path_res(self):
        """getter of path_res"""
        return self._path_res

    def _set_path_res(self, value):
        """setter of path_res"""
        check_var("path_res", value, "str")
        self._path_res = value

    # Path to the folder to same the results
    # Type : str
    path_res = property(fget=_get_path_res, fset=_set_path_res,
                        doc=u"""Path to the folder to same the results""")

    def _get_geo(self):
        """getter of geo"""
        return self._geo

    def _set_geo(self, value):
        """setter of geo"""
        check_var("geo", value, "OutGeo")
        self._geo = value

        if self._geo is not None:
            self._geo.parent = self
    # Geometry output
    # Type : OutGeo
    geo = property(fget=_get_geo, fset=_set_geo,
                   doc=u"""Geometry output""")

    def _get_elec(self):
        """getter of elec"""
        return self._elec

    def _set_elec(self, value):
        """setter of elec"""
        check_var("elec", value, "OutElec")
        self._elec = value

        if self._elec is not None:
            self._elec.parent = self
    # Electrical module output
    # Type : OutElec
    elec = property(fget=_get_elec, fset=_set_elec,
                    doc=u"""Electrical module output""")

    def _get_mag(self):
        """getter of mag"""
        return self._mag

    def _set_mag(self, value):
        """setter of mag"""
        check_var("mag", value, "OutMag")
        self._mag = value

        if self._mag is not None:
            self._mag.parent = self
    # Magnetic module output
    # Type : OutMag
    mag = property(fget=_get_mag, fset=_set_mag,
                   doc=u"""Magnetic module output""")

    def _get_struct(self):
        """getter of struct"""
        return self._struct

    def _set_struct(self, value):
        """setter of struct"""
        check_var("struct", value, "OutStruct")
        self._struct = value

        if self._struct is not None:
            self._struct.parent = self
    # Structural module output
    # Type : OutStruct
    struct = property(fget=_get_struct, fset=_set_struct,
                      doc=u"""Structural module output""")

    def _get_post(self):
        """getter of post"""
        return self._post

    def _set_post(self, value):
        """setter of post"""
        check_var("post", value, "OutPost")
        self._post = value

        if self._post is not None:
            self._post.parent = self
    # Post-Processing settings
    # Type : OutPost
    post = property(fget=_get_post, fset=_set_post,
                    doc=u"""Post-Processing settings""")
