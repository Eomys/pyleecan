# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Mesh import Mesh

from pyleecan.Methods.Mesh.MeshTriangle.comp_projection_mesh2mesh import comp_projection_mesh2mesh

from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError


class MeshTriangle(Mesh):
    """Gather the parameters of a mesh with only triangles"""

    VERSION = 1

    # cf Methods.Mesh.MeshTriangle.comp_projection_mesh2mesh
    comp_projection_mesh2mesh = comp_projection_mesh2mesh
    # save method is available in all object
    save = save

    def __init__(self, element=None, node=None, submeshe=None, jacobian=None, jacobian_derivative=None, det_jacobian=None, gauss_point=None, solution=None, nb_elem=None, nb_node=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["element", "node", "submeshe", "jacobian", "jacobian_derivative", "det_jacobian", "gauss_point", "solution", "nb_elem", "nb_node"])
            # Overwrite default value with init_dict content
            if "element" in list(init_dict.keys()):
                element = init_dict["element"]
            if "node" in list(init_dict.keys()):
                node = init_dict["node"]
            if "submeshe" in list(init_dict.keys()):
                submeshe = init_dict["submeshe"]
            if "jacobian" in list(init_dict.keys()):
                jacobian = init_dict["jacobian"]
            if "jacobian_derivative" in list(init_dict.keys()):
                jacobian_derivative = init_dict["jacobian_derivative"]
            if "det_jacobian" in list(init_dict.keys()):
                det_jacobian = init_dict["det_jacobian"]
            if "gauss_point" in list(init_dict.keys()):
                gauss_point = init_dict["gauss_point"]
            if "solution" in list(init_dict.keys()):
                solution = init_dict["solution"]
            if "nb_elem" in list(init_dict.keys()):
                nb_elem = init_dict["nb_elem"]
            if "nb_node" in list(init_dict.keys()):
                nb_node = init_dict["nb_node"]
        # Initialisation by argument
        # element can be None, a ndarray or a list
        set_array(self, "element", element)
        # node can be None, a ndarray or a list
        set_array(self, "node", node)
        self.submeshe = submeshe
        # jacobian can be None, a ndarray or a list
        set_array(self, "jacobian", jacobian)
        # jacobian_derivative can be None, a ndarray or a list
        set_array(self, "jacobian_derivative", jacobian_derivative)
        # det_jacobian can be None, a ndarray or a list
        set_array(self, "det_jacobian", det_jacobian)
        # gauss_point can be None, a ndarray or a list
        set_array(self, "gauss_point", gauss_point)
        self.solution = solution
        self.nb_elem = nb_elem
        self.nb_node = nb_node
        # Call Mesh init
        super(MeshTriangle, self).__init__()
        # The class is frozen (in Mesh init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MeshTriangle_str = ""
        # Get the properties inherited from Mesh
        MeshTriangle_str += super(MeshTriangle, self).__str__() + linesep
        MeshTriangle_str += "element = " + linesep + str(self.element) + linesep + linesep
        MeshTriangle_str += "node = " + linesep + str(self.node) + linesep + linesep
        MeshTriangle_str += "submeshe = " + str(self.submeshe) + linesep
        MeshTriangle_str += "jacobian = " + linesep + str(self.jacobian) + linesep + linesep
        MeshTriangle_str += "jacobian_derivative = " + linesep + str(self.jacobian_derivative) + linesep + linesep
        MeshTriangle_str += "det_jacobian = " + linesep + str(self.det_jacobian) + linesep + linesep
        MeshTriangle_str += "gauss_point = " + linesep + str(self.gauss_point) + linesep + linesep
        MeshTriangle_str += "solution = " + str(self.solution) + linesep
        MeshTriangle_str += "nb_elem = " + str(self.nb_elem) + linesep
        MeshTriangle_str += "nb_node = " + str(self.nb_node)
        return MeshTriangle_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Mesh
        if not super(MeshTriangle, self).__eq__(other):
            return False
        if not array_equal(other.element, self.element):
            return False
        if not array_equal(other.node, self.node):
            return False
        if other.submeshe != self.submeshe:
            return False
        if not array_equal(other.jacobian, self.jacobian):
            return False
        if not array_equal(other.jacobian_derivative, self.jacobian_derivative):
            return False
        if not array_equal(other.det_jacobian, self.det_jacobian):
            return False
        if not array_equal(other.gauss_point, self.gauss_point):
            return False
        if other.solution != self.solution:
            return False
        if other.nb_elem != self.nb_elem:
            return False
        if other.nb_node != self.nb_node:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Mesh
        MeshTriangle_dict = super(MeshTriangle, self).as_dict()
        if self.element is None:
            MeshTriangle_dict["element"] = None
        else:
            MeshTriangle_dict["element"] = self.element.tolist()
        if self.node is None:
            MeshTriangle_dict["node"] = None
        else:
            MeshTriangle_dict["node"] = self.node.tolist()
        MeshTriangle_dict["submeshe"] = self.submeshe
        if self.jacobian is None:
            MeshTriangle_dict["jacobian"] = None
        else:
            MeshTriangle_dict["jacobian"] = self.jacobian.tolist()
        if self.jacobian_derivative is None:
            MeshTriangle_dict["jacobian_derivative"] = None
        else:
            MeshTriangle_dict["jacobian_derivative"] = self.jacobian_derivative.tolist()
        if self.det_jacobian is None:
            MeshTriangle_dict["det_jacobian"] = None
        else:
            MeshTriangle_dict["det_jacobian"] = self.det_jacobian.tolist()
        if self.gauss_point is None:
            MeshTriangle_dict["gauss_point"] = None
        else:
            MeshTriangle_dict["gauss_point"] = self.gauss_point.tolist()
        MeshTriangle_dict["solution"] = self.solution
        MeshTriangle_dict["nb_elem"] = self.nb_elem
        MeshTriangle_dict["nb_node"] = self.nb_node
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MeshTriangle_dict["__class__"] = "MeshTriangle"
        return MeshTriangle_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.element = None
        self.node = None
        self.submeshe = None
        self.jacobian = None
        self.jacobian_derivative = None
        self.det_jacobian = None
        self.gauss_point = None
        self.solution = None
        self.nb_elem = None
        self.nb_node = None
        # Set to None the properties inherited from Mesh
        super(MeshTriangle, self)._set_None()

    def _get_element(self):
        """getter of element"""
        return self._element

    def _set_element(self, value):
        """setter of element"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("element", value, "ndarray")
        self._element = value

    # Triangles connectivity (3 nodes per elements)
    # Type : ndarray
    element = property(fget=_get_element, fset=_set_element,
                       doc=u"""Triangles connectivity (3 nodes per elements)""")

    def _get_node(self):
        """getter of node"""
        return self._node

    def _set_node(self, value):
        """setter of node"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("node", value, "ndarray")
        self._node = value

    # Nodes coordinates
    # Type : ndarray
    node = property(fget=_get_node, fset=_set_node,
                    doc=u"""Nodes coordinates""")

    def _get_submeshe(self):
        """getter of submeshe"""
        return self._submeshe

    def _set_submeshe(self, value):
        """setter of submeshe"""
        check_var("submeshe", value, "dict")
        self._submeshe = value

    # Elements indices from the same part of the machine (stator, rotor, airgap …)
    # Type : dict
    submeshe = property(fget=_get_submeshe, fset=_set_submeshe,
                        doc=u"""Elements indices from the same part of the machine (stator, rotor, airgap …)""")

    def _get_jacobian(self):
        """getter of jacobian"""
        return self._jacobian

    def _set_jacobian(self, value):
        """setter of jacobian"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("jacobian", value, "ndarray")
        self._jacobian = value

    # Jacobian of each element
    # Type : ndarray
    jacobian = property(fget=_get_jacobian, fset=_set_jacobian,
                        doc=u"""Jacobian of each element""")

    def _get_jacobian_derivative(self):
        """getter of jacobian_derivative"""
        return self._jacobian_derivative

    def _set_jacobian_derivative(self, value):
        """setter of jacobian_derivative"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("jacobian_derivative", value, "ndarray")
        self._jacobian_derivative = value

    # Jacobian derivative of each element
    # Type : ndarray
    jacobian_derivative = property(fget=_get_jacobian_derivative, fset=_set_jacobian_derivative,
                                   doc=u"""Jacobian derivative of each element""")

    def _get_det_jacobian(self):
        """getter of det_jacobian"""
        return self._det_jacobian

    def _set_det_jacobian(self, value):
        """setter of det_jacobian"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("det_jacobian", value, "ndarray")
        self._det_jacobian = value

    # Determinant of jacobian
    # Type : ndarray
    det_jacobian = property(fget=_get_det_jacobian, fset=_set_det_jacobian,
                            doc=u"""Determinant of jacobian""")

    def _get_gauss_point(self):
        """getter of gauss_point"""
        return self._gauss_point

    def _set_gauss_point(self, value):
        """setter of gauss_point"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("gauss_point", value, "ndarray")
        self._gauss_point = value

    # Point where the jacobian is calculated (for integration purpose)
    # Type : ndarray
    gauss_point = property(fget=_get_gauss_point, fset=_set_gauss_point,
                           doc=u"""Point where the jacobian is calculated (for integration purpose)""")

    def _get_solution(self):
        """getter of solution"""
        return self._solution

    def _set_solution(self, value):
        """setter of solution"""
        check_var("solution", value, "dict")
        self._solution = value

    # Field solution from the FEA
    # Type : dict
    solution = property(fget=_get_solution, fset=_set_solution,
                        doc=u"""Field solution from the FEA""")

    def _get_nb_elem(self):
        """getter of nb_elem"""
        return self._nb_elem

    def _set_nb_elem(self, value):
        """setter of nb_elem"""
        check_var("nb_elem", value, "int")
        self._nb_elem = value

    # Total number of elements
    # Type : int
    nb_elem = property(fget=_get_nb_elem, fset=_set_nb_elem,
                       doc=u"""Total number of elements""")

    def _get_nb_node(self):
        """getter of nb_node"""
        return self._nb_node

    def _set_nb_node(self, value):
        """setter of nb_node"""
        check_var("nb_node", value, "int")
        self._nb_node = value

    # Total number of nodes
    # Type : int
    nb_node = property(fget=_get_nb_node, fset=_set_nb_node,
                       doc=u"""Total number of nodes""")
