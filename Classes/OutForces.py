# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError


class OutForces(FrozenClass):
    """Gather the force module outputs"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, Prad=None, Ptan=None, Pradwr=None, Ptanwr=None, nodal_forces=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["Prad", "Ptan", "Pradwr", "Ptanwr", "nodal_forces"])
            # Overwrite default value with init_dict content
            if "Prad" in list(init_dict.keys()):
                Prad = init_dict["Prad"]
            if "Ptan" in list(init_dict.keys()):
                Ptan = init_dict["Ptan"]
            if "Pradwr" in list(init_dict.keys()):
                Pradwr = init_dict["Pradwr"]
            if "Ptanwr" in list(init_dict.keys()):
                Ptanwr = init_dict["Ptanwr"]
            if "nodal_forces" in list(init_dict.keys()):
                nodal_forces = init_dict["nodal_forces"]
        # Initialisation by argument
        self.parent = None
        # Prad can be None, a ndarray or a list
        set_array(self, "Prad", Prad)
        # Ptan can be None, a ndarray or a list
        set_array(self, "Ptan", Ptan)
        # Pradwr can be None, a ndarray or a list
        set_array(self, "Pradwr", Pradwr)
        # Ptanwr can be None, a ndarray or a list
        set_array(self, "Ptanwr", Ptanwr)
        self.nodal_forces = nodal_forces

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutForces_str = ""
        if self.parent is None:
            OutForces_str += "parent = None " + linesep
        else:
            OutForces_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutForces_str += "Prad = " + linesep + str(self.Prad) + linesep + linesep
        OutForces_str += "Ptan = " + linesep + str(self.Ptan) + linesep + linesep
        OutForces_str += "Pradwr = " + linesep + str(self.Pradwr) + linesep + linesep
        OutForces_str += "Ptanwr = " + linesep + str(self.Ptanwr) + linesep + linesep
        OutForces_str += "nodal_forces = " + str(self.nodal_forces)
        return OutForces_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if not array_equal(other.Prad, self.Prad):
            return False
        if not array_equal(other.Ptan, self.Ptan):
            return False
        if not array_equal(other.Pradwr, self.Pradwr):
            return False
        if not array_equal(other.Ptanwr, self.Ptanwr):
            return False
        if other.nodal_forces != self.nodal_forces:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OutForces_dict = dict()
        if self.Prad is None:
            OutForces_dict["Prad"] = None
        else:
            OutForces_dict["Prad"] = self.Prad.tolist()
        if self.Ptan is None:
            OutForces_dict["Ptan"] = None
        else:
            OutForces_dict["Ptan"] = self.Ptan.tolist()
        if self.Pradwr is None:
            OutForces_dict["Pradwr"] = None
        else:
            OutForces_dict["Pradwr"] = self.Pradwr.tolist()
        if self.Ptanwr is None:
            OutForces_dict["Ptanwr"] = None
        else:
            OutForces_dict["Ptanwr"] = self.Ptanwr.tolist()
        OutForces_dict["nodal_forces"] = self.nodal_forces
        # The class name is added to the dict fordeserialisation purpose
        OutForces_dict["__class__"] = "OutForces"
        return OutForces_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Prad = None
        self.Ptan = None
        self.Pradwr = None
        self.Ptanwr = None
        self.nodal_forces = None

    def _get_Prad(self):
        """getter of Prad"""
        return self._Prad

    def _set_Prad(self, value):
        """setter of Prad"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Prad", value, "ndarray")
        self._Prad = value

    # Radial magnetic air-gap surface force (space,time) 
    # Type : ndarray
    Prad = property(fget=_get_Prad, fset=_set_Prad,
                    doc=u"""Radial magnetic air-gap surface force (space,time) """)

    def _get_Ptan(self):
        """getter of Ptan"""
        return self._Ptan

    def _set_Ptan(self, value):
        """setter of Ptan"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Ptan", value, "ndarray")
        self._Ptan = value

    # Tangential magnetic air-gap surface force (space,time) 
    # Type : ndarray
    Ptan = property(fget=_get_Ptan, fset=_set_Ptan,
                    doc=u"""Tangential magnetic air-gap surface force (space,time) """)

    def _get_Pradwr(self):
        """getter of Pradwr"""
        return self._Pradwr

    def _set_Pradwr(self, value):
        """setter of Pradwr"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Pradwr", value, "ndarray")
        self._Pradwr = value

    # Radial magnetic air-gap surface force (harmonic,wavenumber) 
    # Type : ndarray
    Pradwr = property(fget=_get_Pradwr, fset=_set_Pradwr,
                      doc=u"""Radial magnetic air-gap surface force (harmonic,wavenumber) """)

    def _get_Ptanwr(self):
        """getter of Ptanwr"""
        return self._Ptanwr

    def _set_Ptanwr(self, value):
        """setter of Ptanwr"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Ptanwr", value, "ndarray")
        self._Ptanwr = value

    # Tangential magnetic air-gap surface force  (harmonic,wavenumber) 
    # Type : ndarray
    Ptanwr = property(fget=_get_Ptanwr, fset=_set_Ptanwr,
                      doc=u"""Tangential magnetic air-gap surface force  (harmonic,wavenumber) """)

    def _get_nodal_forces(self):
        """getter of nodal_forces"""
        return self._nodal_forces

    def _set_nodal_forces(self, value):
        """setter of nodal_forces"""
        check_var("nodal_forces", value, "dict")
        self._nodal_forces = value

    # Dictionnary containing nodal forces fx,fy 
    # Type : dict
    nodal_forces = property(fget=_get_nodal_forces, fset=_set_nodal_forces,
                            doc=u"""Dictionnary containing nodal forces fx,fy """)
