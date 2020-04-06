# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Mesh/Solution.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from pyleecan.Classes._check import check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Mesh.Solution.get_field import get_field
except ImportError as error:
    get_field = error

try:
    from pyleecan.Methods.Mesh.Solution.set_field import set_field
except ImportError as error:
    set_field = error


from numpy import array, empty
from pyleecan.Classes._check import InitUnKnowClassError


class Solution(FrozenClass):
    """Define a solution related to a Mesh object."""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.Solution.get_field
    if isinstance(get_field, ImportError):
        get_field = property(
            fget=lambda x: raise_(
                ImportError("Can't use Solution method get_field: " + str(get_field))
            )
        )
    else:
        get_field = get_field
    # cf Methods.Mesh.Solution.set_field
    if isinstance(set_field, ImportError):
        set_field = property(
            fget=lambda x: raise_(
                ImportError("Can't use Solution method set_field: " + str(set_field))
            )
        )
    else:
        set_field = set_field
    # save method is available in all object
    save = save

    def __init__(self, nodal=dict(), edge=dict(), face=dict(), volume=dict(), init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            assert(type(init_dict) is dict)
            # Overwrite default value with init_dict content
            if "nodal" in list(init_dict.keys()):
                nodal = init_dict["nodal"]
            if "edge" in list(init_dict.keys()):
                edge = init_dict["edge"]
            if "face" in list(init_dict.keys()):
                face = init_dict["face"]
            if "volume" in list(init_dict.keys()):
                volume = init_dict["volume"]
        # Initialisation by argument
        self.parent = None
        # nodal can be None or a dict of ndarray
        self.nodal = dict()
        if type(nodal) is dict:
            for key, obj in nodal.items():
                if obj is None:  # Default value
                    value = empty(0)
                elif isinstance(obj, list):
                    value = array(obj)
                self.nodal[key] = value
        elif nodal is None:
            self.nodal = dict()
        else:
            self.nodal = nodal# Should raise an error
        # edge can be None or a dict of ndarray
        self.edge = dict()
        if type(edge) is dict:
            for key, obj in edge.items():
                if obj is None:  # Default value
                    value = empty(0)
                elif isinstance(obj, list):
                    value = array(obj)
                self.edge[key] = value
        elif edge is None:
            self.edge = dict()
        else:
            self.edge = edge# Should raise an error
        # face can be None or a dict of ndarray
        self.face = dict()
        if type(face) is dict:
            for key, obj in face.items():
                if obj is None:  # Default value
                    value = empty(0)
                elif isinstance(obj, list):
                    value = array(obj)
                self.face[key] = value
        elif face is None:
            self.face = dict()
        else:
            self.face = face# Should raise an error
        # volume can be None or a dict of ndarray
        self.volume = dict()
        if type(volume) is dict:
            for key, obj in volume.items():
                if obj is None:  # Default value
                    value = empty(0)
                elif isinstance(obj, list):
                    value = array(obj)
                self.volume[key] = value
        elif volume is None:
            self.volume = dict()
        else:
            self.volume = volume# Should raise an error

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Solution_str = ""
        if self.parent is None:
            Solution_str += "parent = None " + linesep
        else:
            Solution_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if len(self.nodal) == 0:
            Solution_str += "nodal = dict()"
        for key, obj in self.nodal.items():
            Solution_str += "nodal["+key+"] = "+str(self.nodal[key]) + linesep + linesep
        if len(self.edge) == 0:
            Solution_str += "edge = dict()"
        for key, obj in self.edge.items():
            Solution_str += "edge["+key+"] = "+str(self.edge[key]) + linesep + linesep
        if len(self.face) == 0:
            Solution_str += "face = dict()"
        for key, obj in self.face.items():
            Solution_str += "face["+key+"] = "+str(self.face[key]) + linesep + linesep
        if len(self.volume) == 0:
            Solution_str += "volume = dict()"
        for key, obj in self.volume.items():
            Solution_str += "volume["+key+"] = "+str(self.volume[key]) + linesep + linesep
        return Solution_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.nodal != self.nodal:
            return False
        if other.edge != self.edge:
            return False
        if other.face != self.face:
            return False
        if other.volume != self.volume:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Solution_dict = dict()
        Solution_dict["nodal"] = dict()
        for key, obj in self.nodal.items():
            Solution_dict["nodal"][key] = obj.tolist()
        Solution_dict["edge"] = dict()
        for key, obj in self.edge.items():
            Solution_dict["edge"][key] = obj.tolist()
        Solution_dict["face"] = dict()
        for key, obj in self.face.items():
            Solution_dict["face"][key] = obj.tolist()
        Solution_dict["volume"] = dict()
        for key, obj in self.volume.items():
            Solution_dict["volume"][key] = obj.tolist()
        # The class name is added to the dict fordeserialisation purpose
        Solution_dict["__class__"] = "Solution"
        return Solution_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.nodal = dict()
        self.edge = dict()
        self.face = dict()
        self.volume = dict()

    def get_logger(self):
        """getter of the logger"""
        if hasattr(self,'logger_name'):
            return getLogger(self.logger_name)
        elif self.parent != None:
            return self.parent.get_logger()
        else:
            return getLogger('Pyleecan')

    def _get_nodal(self):
        """getter of nodal"""
        return self._nodal

    def _set_nodal(self, value):
        """setter of nodal"""
        if type(value) is dict:
            for key, obj in value.items():
                if type(obj) is list:
                    try:
                        obj = array(obj)
                    except:
                        pass
        check_var("nodal", value, "{ndarray}")
        self._nodal = value

    # A solution related to nodes
    # Type : {ndarray}
    nodal = property(
        fget=_get_nodal, fset=_set_nodal, doc=u"""A solution related to nodes"""
    )

    def _get_edge(self):
        """getter of edge"""
        return self._edge

    def _set_edge(self, value):
        """setter of edge"""
        if type(value) is dict:
            for key, obj in value.items():
                if type(obj) is list:
                    try:
                        obj = array(obj)
                    except:
                        pass
        check_var("edge", value, "{ndarray}")
        self._edge = value

    # A solution related to edges
    # Type : {ndarray}
    edge = property(
        fget=_get_edge, fset=_set_edge, doc=u"""A solution related to edges"""
    )

    def _get_face(self):
        """getter of face"""
        return self._face

    def _set_face(self, value):
        """setter of face"""
        if type(value) is dict:
            for key, obj in value.items():
                if type(obj) is list:
                    try:
                        obj = array(obj)
                    except:
                        pass
        check_var("face", value, "{ndarray}")
        self._face = value

    # A solution related to faces
    # Type : {ndarray}
    face = property(
        fget=_get_face, fset=_set_face, doc=u"""A solution related to faces"""
    )

    def _get_volume(self):
        """getter of volume"""
        return self._volume

    def _set_volume(self, value):
        """setter of volume"""
        if type(value) is dict:
            for key, obj in value.items():
                if type(obj) is list:
                    try:
                        obj = array(obj)
                    except:
                        pass
        check_var("volume", value, "{ndarray}")
        self._volume = value

    # A solution related to volumes
    # Type : {ndarray}
    volume = property(
        fget=_get_volume, fset=_set_volume, doc=u"""A solution related to volumes"""
    )
