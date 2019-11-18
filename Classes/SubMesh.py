# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Mesh.SubMesh.get_node_coord import get_node_coord
except ImportError as error:
    get_node_coord = error

try:
    from pyleecan.Methods.Mesh.SubMesh.get_element import get_element
except ImportError as error:
    get_element = error

try:
    from pyleecan.Methods.Mesh.SubMesh.set_submesh import set_submesh
except ImportError as error:
    set_submesh = error


from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Mesh import Mesh



class SubMesh(FrozenClass):
    """Define a submesh"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.SubMesh.get_node_coord
    if isinstance(get_node_coord, ImportError):
        get_node_coord = property(fget=lambda x: raise_(ImportError("Can't use SubMesh method get_node_coord: " + str(get_node_coord))))
    else:
        get_node_coord = get_node_coord
    # cf Methods.Mesh.SubMesh.get_element
    if isinstance(get_element, ImportError):
        get_element = property(fget=lambda x: raise_(ImportError("Can't use SubMesh method get_element: " + str(get_element))))
    else:
        get_element = get_element
    # cf Methods.Mesh.SubMesh.set_submesh
    if isinstance(set_submesh, ImportError):
        set_submesh = property(fget=lambda x: raise_(ImportError("Can't use SubMesh method set_submesh: " + str(set_submesh))))
    else:
        set_submesh = set_submesh
    # save method is available in all object
    save = save

    def __init__(self, mesh=None, parent_elem=None, parent_node=None, group_number=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if mesh == -1:
            mesh = Mesh()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["mesh", "parent_elem", "parent_node", "group_number"])
            # Overwrite default value with init_dict content
            if "mesh" in list(init_dict.keys()):
                mesh = init_dict["mesh"]
            if "parent_elem" in list(init_dict.keys()):
                parent_elem = init_dict["parent_elem"]
            if "parent_node" in list(init_dict.keys()):
                parent_node = init_dict["parent_node"]
            if "group_number" in list(init_dict.keys()):
                group_number = init_dict["group_number"]
        # Initialisation by argument
        self.parent = None
        # mesh can be None, a Mesh object or a dict
        if isinstance(mesh, dict):
            # Check that the type is correct (including daughter)
            class_name = mesh.get('__class__')
            if class_name not in ['Mesh', 'MeshFEMM', 'MeshMat', 'MeshForce']:
                raise InitUnKnowClassError("Unknow class name "+class_name+" in init_dict for mesh")
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes."+class_name, fromlist=[class_name])
            class_obj = getattr(module,class_name)
            self.mesh = class_obj(init_dict=mesh)
        else:
            self.mesh = mesh
        # parent_elem can be None, a ndarray or a list
        set_array(self, "parent_elem", parent_elem)
        # parent_node can be None, a ndarray or a list
        set_array(self, "parent_node", parent_node)
        # group_number can be None, a ndarray or a list
        set_array(self, "group_number", group_number)

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SubMesh_str = ""
        if self.parent is None:
            SubMesh_str += "parent = None " + linesep
        else:
            SubMesh_str += "parent = " + str(type(self.parent)) + " object" + linesep
        SubMesh_str += "mesh = " + str(self.mesh.as_dict()) + linesep + linesep
        SubMesh_str += "parent_elem = " + linesep + str(self.parent_elem) + linesep + linesep
        SubMesh_str += "parent_node = " + linesep + str(self.parent_node) + linesep + linesep
        SubMesh_str += "group_number = " + linesep + str(self.group_number)
        return SubMesh_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.mesh != self.mesh:
            return False
        if not array_equal(other.parent_elem, self.parent_elem):
            return False
        if not array_equal(other.parent_node, self.parent_node):
            return False
        if not array_equal(other.group_number, self.group_number):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        SubMesh_dict = dict()
        if self.mesh is None:
            SubMesh_dict["mesh"] = None
        else:
            SubMesh_dict["mesh"] = self.mesh.as_dict()
        if self.parent_elem is None:
            SubMesh_dict["parent_elem"] = None
        else:
            SubMesh_dict["parent_elem"] = self.parent_elem.tolist()
        if self.parent_node is None:
            SubMesh_dict["parent_node"] = None
        else:
            SubMesh_dict["parent_node"] = self.parent_node.tolist()
        if self.group_number is None:
            SubMesh_dict["group_number"] = None
        else:
            SubMesh_dict["group_number"] = self.group_number.tolist()
        # The class name is added to the dict fordeserialisation purpose
        SubMesh_dict["__class__"] = "SubMesh"
        return SubMesh_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.mesh is not None:
            self.mesh._set_None()
        self.parent_elem = None
        self.parent_node = None
        self.group_number = None

    def _get_mesh(self):
        """getter of mesh"""
        return self._mesh

    def _set_mesh(self, value):
        """setter of mesh"""
        check_var("mesh", value, "Mesh")
        self._mesh = value

        if self._mesh is not None:
            self._mesh.parent = self
    # A self-standing mesh object
    # Type : Mesh
    mesh = property(fget=_get_mesh, fset=_set_mesh,
                    doc=u"""A self-standing mesh object""")

    def _get_parent_elem(self):
        """getter of parent_elem"""
        return self._parent_elem

    def _set_parent_elem(self, value):
        """setter of parent_elem"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("parent_elem", value, "ndarray")
        self._parent_elem = value

    # List of corresponding element number in the parent mesh
    # Type : ndarray
    parent_elem = property(fget=_get_parent_elem, fset=_set_parent_elem,
                           doc=u"""List of corresponding element number in the parent mesh""")

    def _get_parent_node(self):
        """getter of parent_node"""
        return self._parent_node

    def _set_parent_node(self, value):
        """setter of parent_node"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("parent_node", value, "ndarray")
        self._parent_node = value

    # List of corresponding node number in the parent mesh
    # Type : ndarray
    parent_node = property(fget=_get_parent_node, fset=_set_parent_node,
                           doc=u"""List of corresponding node number in the parent mesh""")

    def _get_group_number(self):
        """getter of group_number"""
        return self._group_number

    def _set_group_number(self, value):
        """setter of group_number"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("group_number", value, "ndarray")
        self._group_number = value

    # Group number defining this submesh. If several groups are indicated, the submesh corresponds to the intersection. Use (nbr,-1) to select the intersection of group "nbr" with all other groups.
    # Type : ndarray
    group_number = property(fget=_get_group_number, fset=_set_group_number,
                            doc=u"""Group number defining this submesh. If several groups are indicated, the submesh corresponds to the intersection. Use (nbr,-1) to select the intersection of group "nbr" with all other groups.""")
