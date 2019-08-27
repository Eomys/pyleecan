# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.OutMag import OutMag

from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Mesh import Mesh



class OutMagFEMM(OutMag):
    """Gather the FEMM related output"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, FEMM_dict=None, FEMM_Mesh=list(), time=None, angle=None, Nt_tot=None, Na_tot=None, Br=None, Bt=None, Tem=None, Tem_av=None, Tem_rip=None, Phi_wind_stator=None, emf=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["FEMM_dict", "FEMM_Mesh", "time", "angle", "Nt_tot", "Na_tot", "Br", "Bt", "Tem", "Tem_av", "Tem_rip", "Phi_wind_stator", "emf"])
            # Overwrite default value with init_dict content
            if "FEMM_dict" in list(init_dict.keys()):
                FEMM_dict = init_dict["FEMM_dict"]
            if "FEMM_Mesh" in list(init_dict.keys()):
                FEMM_Mesh = init_dict["FEMM_Mesh"]
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
            if "Br" in list(init_dict.keys()):
                Br = init_dict["Br"]
            if "Bt" in list(init_dict.keys()):
                Bt = init_dict["Bt"]
            if "Tem" in list(init_dict.keys()):
                Tem = init_dict["Tem"]
            if "Tem_av" in list(init_dict.keys()):
                Tem_av = init_dict["Tem_av"]
            if "Tem_rip" in list(init_dict.keys()):
                Tem_rip = init_dict["Tem_rip"]
            if "Phi_wind_stator" in list(init_dict.keys()):
                Phi_wind_stator = init_dict["Phi_wind_stator"]
            if "emf" in list(init_dict.keys()):
                emf = init_dict["emf"]
        # Initialisation by argument
        self.FEMM_dict = FEMM_dict
        # FEMM_Mesh can be None or a list of Mesh object
        self.FEMM_Mesh = list()
        if type(FEMM_Mesh) is list:
            for obj in FEMM_Mesh:
                if obj is None:  # Default value
                    self.FEMM_Mesh.append(Mesh())
                elif isinstance(obj, dict):
                    self.FEMM_Mesh.append(Mesh(init_dict=obj))
                else:
                    self.FEMM_Mesh.append(obj)
        elif FEMM_Mesh is None:
            self.FEMM_Mesh = list()
        else:
            self.FEMM_Mesh = FEMM_Mesh
        # Call OutMag init
        super(OutMagFEMM, self).__init__(time=time, angle=angle, Nt_tot=Nt_tot, Na_tot=Na_tot, Br=Br, Bt=Bt, Tem=Tem, Tem_av=Tem_av, Tem_rip=Tem_rip, Phi_wind_stator=Phi_wind_stator, emf=emf)
        # The class is frozen (in OutMag init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutMagFEMM_str = ""
        # Get the properties inherited from OutMag
        OutMagFEMM_str += super(OutMagFEMM, self).__str__() + linesep
        OutMagFEMM_str += "FEMM_dict = " + str(self.FEMM_dict) + linesep
        if len(self.FEMM_Mesh) == 0:
            OutMagFEMM_str += "FEMM_Mesh = []"
        for ii in range(len(self.FEMM_Mesh)):
            OutMagFEMM_str += "FEMM_Mesh["+str(ii)+"] = "+str(self.FEMM_Mesh[ii].as_dict())+"\n"
        return OutMagFEMM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OutMag
        if not super(OutMagFEMM, self).__eq__(other):
            return False
        if other.FEMM_dict != self.FEMM_dict:
            return False
        if other.FEMM_Mesh != self.FEMM_Mesh:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from OutMag
        OutMagFEMM_dict = super(OutMagFEMM, self).as_dict()
        OutMagFEMM_dict["FEMM_dict"] = self.FEMM_dict
        OutMagFEMM_dict["FEMM_Mesh"] = list()
        for obj in self.FEMM_Mesh:
            OutMagFEMM_dict["FEMM_Mesh"].append(obj.as_dict())
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        OutMagFEMM_dict["__class__"] = "OutMagFEMM"
        return OutMagFEMM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.FEMM_dict = None
        for obj in self.FEMM_Mesh:
            obj._set_None()
        # Set to None the properties inherited from OutMag
        super(OutMagFEMM, self)._set_None()

    def _get_FEMM_dict(self):
        """getter of FEMM_dict"""
        return self._FEMM_dict

    def _set_FEMM_dict(self, value):
        """setter of FEMM_dict"""
        check_var("FEMM_dict", value, "dict")
        self._FEMM_dict = value

    # Dictionnary containing the main FEMM parameter
    # Type : dict
    FEMM_dict = property(fget=_get_FEMM_dict, fset=_set_FEMM_dict,
                         doc=u"""Dictionnary containing the main FEMM parameter""")

    def _get_FEMM_Mesh(self):
        """getter of FEMM_Mesh"""
        for obj in self._FEMM_Mesh:
            if obj is not None:
                obj.parent = self
        return self._FEMM_Mesh

    def _set_FEMM_Mesh(self, value):
        """setter of FEMM_Mesh"""
        check_var("FEMM_Mesh", value, "[Mesh]")
        self._FEMM_Mesh = value

        for obj in self._FEMM_Mesh:
            if obj is not None:
                obj.parent = self
    # List of mesh and solution for each time step
    # Type : [Mesh]
    FEMM_Mesh = property(fget=_get_FEMM_Mesh, fset=_set_FEMM_Mesh,
                         doc=u"""List of mesh and solution for each time step""")
