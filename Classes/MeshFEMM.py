# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.MeshMat import MeshMat

from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.SubMesh import SubMesh


class MeshFEMM(MeshMat):
    """Gather the parameters of a mesh with only triangles"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(
        self,
        B=None,
        H=None,
        mu=None,
        element=None,
        node=None,
        group=None,
        nb_elem=None,
        nb_node=None,
        submesh=list(),
        nb_node_per_element=None,
        name=None,
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
                    "B",
                    "H",
                    "mu",
                    "element",
                    "node",
                    "group",
                    "nb_elem",
                    "nb_node",
                    "submesh",
                    "nb_node_per_element",
                    "name",
                ],
            )
            # Overwrite default value with init_dict content
            if "B" in list(init_dict.keys()):
                B = init_dict["B"]
            if "H" in list(init_dict.keys()):
                H = init_dict["H"]
            if "mu" in list(init_dict.keys()):
                mu = init_dict["mu"]
            if "element" in list(init_dict.keys()):
                element = init_dict["element"]
            if "node" in list(init_dict.keys()):
                node = init_dict["node"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
            if "nb_elem" in list(init_dict.keys()):
                nb_elem = init_dict["nb_elem"]
            if "nb_node" in list(init_dict.keys()):
                nb_node = init_dict["nb_node"]
            if "submesh" in list(init_dict.keys()):
                submesh = init_dict["submesh"]
            if "nb_node_per_element" in list(init_dict.keys()):
                nb_node_per_element = init_dict["nb_node_per_element"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
        # Initialisation by argument
        # B can be None, a ndarray or a list
        set_array(self, "B", B)
        # H can be None, a ndarray or a list
        set_array(self, "H", H)
        # mu can be None, a ndarray or a list
        set_array(self, "mu", mu)
        # Call MeshMat init
        super(MeshFEMM, self).__init__(
            element=element,
            node=node,
            group=group,
            nb_elem=nb_elem,
            nb_node=nb_node,
            submesh=submesh,
            nb_node_per_element=nb_node_per_element,
            name=name,
        )
        # The class is frozen (in MeshMat init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MeshFEMM_str = ""
        # Get the properties inherited from MeshMat
        MeshFEMM_str += super(MeshFEMM, self).__str__() + linesep
        MeshFEMM_str += "B = " + linesep + str(self.B) + linesep + linesep
        MeshFEMM_str += "H = " + linesep + str(self.H) + linesep + linesep
        MeshFEMM_str += "mu = " + linesep + str(self.mu)
        return MeshFEMM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MeshMat
        if not super(MeshFEMM, self).__eq__(other):
            return False
        if not array_equal(other.B, self.B):
            return False
        if not array_equal(other.H, self.H):
            return False
        if not array_equal(other.mu, self.mu):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from MeshMat
        MeshFEMM_dict = super(MeshFEMM, self).as_dict()
        if self.B is None:
            MeshFEMM_dict["B"] = None
        else:
            MeshFEMM_dict["B"] = self.B.tolist()
        if self.H is None:
            MeshFEMM_dict["H"] = None
        else:
            MeshFEMM_dict["H"] = self.H.tolist()
        if self.mu is None:
            MeshFEMM_dict["mu"] = None
        else:
            MeshFEMM_dict["mu"] = self.mu.tolist()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MeshFEMM_dict["__class__"] = "MeshFEMM"
        return MeshFEMM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.B = None
        self.H = None
        self.mu = None
        # Set to None the properties inherited from MeshMat
        super(MeshFEMM, self)._set_None()

    def _get_B(self):
        """getter of B"""
        return self._B

    def _set_B(self, value):
        """setter of B"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("B", value, "ndarray")
        self._B = value

    # Magnetic flux per element
    # Type : ndarray
    B = property(fget=_get_B, fset=_set_B, doc=u"""Magnetic flux per element""")

    def _get_H(self):
        """getter of H"""
        return self._H

    def _set_H(self, value):
        """setter of H"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("H", value, "ndarray")
        self._H = value

    # Magnetic field per element
    # Type : ndarray
    H = property(fget=_get_H, fset=_set_H, doc=u"""Magnetic field per element""")

    def _get_mu(self):
        """getter of mu"""
        return self._mu

    def _set_mu(self, value):
        """setter of mu"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("mu", value, "ndarray")
        self._mu = value

    # Pemreability per element
    # Type : ndarray
    mu = property(fget=_get_mu, fset=_set_mu, doc=u"""Pemreability per element""")
