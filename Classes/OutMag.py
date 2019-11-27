# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.MeshSolution import MeshSolution


class OutMag(FrozenClass):
    """Gather the magnetic module outputs"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(
        self,
        time=None,
        angle=None,
        Nt_tot=None,
        Na_tot=None,
        Br=None,
        Bt=None,
        Tem=None,
        Tem_av=None,
        Tem_rip=None,
        Phi_wind_stator=None,
        emf=None,
        meshsolution=list(),
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
                    "time",
                    "angle",
                    "Nt_tot",
                    "Na_tot",
                    "Br",
                    "Bt",
                    "Tem",
                    "Tem_av",
                    "Tem_rip",
                    "Phi_wind_stator",
                    "emf",
                    "meshsolution",
                ],
            )
            # Overwrite default value with init_dict content
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
            if "meshsolution" in list(init_dict.keys()):
                meshsolution = init_dict["meshsolution"]
        # Initialisation by argument
        self.parent = None
        # time can be None, a ndarray or a list
        set_array(self, "time", time)
        # angle can be None, a ndarray or a list
        set_array(self, "angle", angle)
        self.Nt_tot = Nt_tot
        self.Na_tot = Na_tot
        # Br can be None, a ndarray or a list
        set_array(self, "Br", Br)
        # Bt can be None, a ndarray or a list
        set_array(self, "Bt", Bt)
        # Tem can be None, a ndarray or a list
        set_array(self, "Tem", Tem)
        self.Tem_av = Tem_av
        self.Tem_rip = Tem_rip
        # Phi_wind_stator can be None, a ndarray or a list
        set_array(self, "Phi_wind_stator", Phi_wind_stator)
        # emf can be None, a ndarray or a list
        set_array(self, "emf", emf)
        # meshsolution can be None or a list of MeshSolution object
        self.meshsolution = list()
        if type(meshsolution) is list:
            for obj in meshsolution:
                if obj is None:  # Default value
                    self.meshsolution.append(MeshSolution())
                elif isinstance(obj, dict):
                    self.meshsolution.append(MeshSolution(init_dict=obj))
                else:
                    self.meshsolution.append(obj)
        elif meshsolution is None:
            self.meshsolution = list()
        else:
            self.meshsolution = meshsolution

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutMag_str = ""
        if self.parent is None:
            OutMag_str += "parent = None " + linesep
        else:
            OutMag_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutMag_str += "time = " + linesep + str(self.time) + linesep + linesep
        OutMag_str += "angle = " + linesep + str(self.angle) + linesep + linesep
        OutMag_str += "Nt_tot = " + str(self.Nt_tot) + linesep
        OutMag_str += "Na_tot = " + str(self.Na_tot) + linesep
        OutMag_str += "Br = " + linesep + str(self.Br) + linesep + linesep
        OutMag_str += "Bt = " + linesep + str(self.Bt) + linesep + linesep
        OutMag_str += "Tem = " + linesep + str(self.Tem) + linesep + linesep
        OutMag_str += "Tem_av = " + str(self.Tem_av) + linesep
        OutMag_str += "Tem_rip = " + str(self.Tem_rip) + linesep
        OutMag_str += (
            "Phi_wind_stator = "
            + linesep
            + str(self.Phi_wind_stator)
            + linesep
            + linesep
        )
        OutMag_str += "emf = " + linesep + str(self.emf) + linesep + linesep
        if len(self.meshsolution) == 0:
            OutMag_str += "meshsolution = []"
        for ii in range(len(self.meshsolution)):
            OutMag_str += (
                "meshsolution["
                + str(ii)
                + "] = "
                + str(self.meshsolution[ii].as_dict())
                + "\n"
            )
        return OutMag_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if not array_equal(other.time, self.time):
            return False
        if not array_equal(other.angle, self.angle):
            return False
        if other.Nt_tot != self.Nt_tot:
            return False
        if other.Na_tot != self.Na_tot:
            return False
        if not array_equal(other.Br, self.Br):
            return False
        if not array_equal(other.Bt, self.Bt):
            return False
        if not array_equal(other.Tem, self.Tem):
            return False
        if other.Tem_av != self.Tem_av:
            return False
        if other.Tem_rip != self.Tem_rip:
            return False
        if not array_equal(other.Phi_wind_stator, self.Phi_wind_stator):
            return False
        if not array_equal(other.emf, self.emf):
            return False
        if other.meshsolution != self.meshsolution:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OutMag_dict = dict()
        if self.time is None:
            OutMag_dict["time"] = None
        else:
            OutMag_dict["time"] = self.time.tolist()
        if self.angle is None:
            OutMag_dict["angle"] = None
        else:
            OutMag_dict["angle"] = self.angle.tolist()
        OutMag_dict["Nt_tot"] = self.Nt_tot
        OutMag_dict["Na_tot"] = self.Na_tot
        if self.Br is None:
            OutMag_dict["Br"] = None
        else:
            OutMag_dict["Br"] = self.Br.tolist()
        if self.Bt is None:
            OutMag_dict["Bt"] = None
        else:
            OutMag_dict["Bt"] = self.Bt.tolist()
        if self.Tem is None:
            OutMag_dict["Tem"] = None
        else:
            OutMag_dict["Tem"] = self.Tem.tolist()
        OutMag_dict["Tem_av"] = self.Tem_av
        OutMag_dict["Tem_rip"] = self.Tem_rip
        if self.Phi_wind_stator is None:
            OutMag_dict["Phi_wind_stator"] = None
        else:
            OutMag_dict["Phi_wind_stator"] = self.Phi_wind_stator.tolist()
        if self.emf is None:
            OutMag_dict["emf"] = None
        else:
            OutMag_dict["emf"] = self.emf.tolist()
        OutMag_dict["meshsolution"] = list()
        for obj in self.meshsolution:
            OutMag_dict["meshsolution"].append(obj.as_dict())
        # The class name is added to the dict fordeserialisation purpose
        OutMag_dict["__class__"] = "OutMag"
        return OutMag_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.time = None
        self.angle = None
        self.Nt_tot = None
        self.Na_tot = None
        self.Br = None
        self.Bt = None
        self.Tem = None
        self.Tem_av = None
        self.Tem_rip = None
        self.Phi_wind_stator = None
        self.emf = None
        for obj in self.meshsolution:
            obj._set_None()

    def _get_time(self):
        """getter of time"""
        return self._time

    def _set_time(self, value):
        """setter of time"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("time", value, "ndarray")
        self._time = value

    # Magnetic time vector (no symmetry)
    # Type : ndarray
    time = property(
        fget=_get_time, fset=_set_time, doc=u"""Magnetic time vector (no symmetry)"""
    )

    def _get_angle(self):
        """getter of angle"""
        return self._angle

    def _set_angle(self, value):
        """setter of angle"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("angle", value, "ndarray")
        self._angle = value

    # Magnetic position vector (no symmetry)
    # Type : ndarray
    angle = property(
        fget=_get_angle,
        fset=_set_angle,
        doc=u"""Magnetic position vector (no symmetry)""",
    )

    def _get_Nt_tot(self):
        """getter of Nt_tot"""
        return self._Nt_tot

    def _set_Nt_tot(self, value):
        """setter of Nt_tot"""
        check_var("Nt_tot", value, "int")
        self._Nt_tot = value

    # Length of the time vector
    # Type : int
    Nt_tot = property(
        fget=_get_Nt_tot, fset=_set_Nt_tot, doc=u"""Length of the time vector"""
    )

    def _get_Na_tot(self):
        """getter of Na_tot"""
        return self._Na_tot

    def _set_Na_tot(self, value):
        """setter of Na_tot"""
        check_var("Na_tot", value, "int")
        self._Na_tot = value

    # Length of the angle vector
    # Type : int
    Na_tot = property(
        fget=_get_Na_tot, fset=_set_Na_tot, doc=u"""Length of the angle vector"""
    )

    def _get_Br(self):
        """getter of Br"""
        return self._Br

    def _set_Br(self, value):
        """setter of Br"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Br", value, "ndarray")
        self._Br = value

    # Radial airgap flux density
    # Type : ndarray
    Br = property(fget=_get_Br, fset=_set_Br, doc=u"""Radial airgap flux density""")

    def _get_Bt(self):
        """getter of Bt"""
        return self._Bt

    def _set_Bt(self, value):
        """setter of Bt"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Bt", value, "ndarray")
        self._Bt = value

    # Tangential airgap flux density
    # Type : ndarray
    Bt = property(fget=_get_Bt, fset=_set_Bt, doc=u"""Tangential airgap flux density""")

    def _get_Tem(self):
        """getter of Tem"""
        return self._Tem

    def _set_Tem(self, value):
        """setter of Tem"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Tem", value, "ndarray")
        self._Tem = value

    # Electromagnetic torque
    # Type : ndarray
    Tem = property(fget=_get_Tem, fset=_set_Tem, doc=u"""Electromagnetic torque""")

    def _get_Tem_av(self):
        """getter of Tem_av"""
        return self._Tem_av

    def _set_Tem_av(self, value):
        """setter of Tem_av"""
        check_var("Tem_av", value, "float")
        self._Tem_av = value

    # Average Electromagnetic torque
    # Type : float
    Tem_av = property(
        fget=_get_Tem_av, fset=_set_Tem_av, doc=u"""Average Electromagnetic torque"""
    )

    def _get_Tem_rip(self):
        """getter of Tem_rip"""
        return self._Tem_rip

    def _set_Tem_rip(self, value):
        """setter of Tem_rip"""
        check_var("Tem_rip", value, "float")
        self._Tem_rip = value

    # Torque ripple
    # Type : float
    Tem_rip = property(fget=_get_Tem_rip, fset=_set_Tem_rip, doc=u"""Torque ripple""")

    def _get_Phi_wind_stator(self):
        """getter of Phi_wind_stator"""
        return self._Phi_wind_stator

    def _set_Phi_wind_stator(self, value):
        """setter of Phi_wind_stator"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Phi_wind_stator", value, "ndarray")
        self._Phi_wind_stator = value

    # Stator winding flux
    # Type : ndarray
    Phi_wind_stator = property(
        fget=_get_Phi_wind_stator,
        fset=_set_Phi_wind_stator,
        doc=u"""Stator winding flux""",
    )

    def _get_emf(self):
        """getter of emf"""
        return self._emf

    def _set_emf(self, value):
        """setter of emf"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("emf", value, "ndarray")
        self._emf = value

    # Electromotive force
    # Type : ndarray
    emf = property(fget=_get_emf, fset=_set_emf, doc=u"""Electromotive force""")

    def _get_meshsolution(self):
        """getter of meshsolution"""
        for obj in self._meshsolution:
            if obj is not None:
                obj.parent = self
        return self._meshsolution

    def _set_meshsolution(self, value):
        """setter of meshsolution"""
        check_var("meshsolution", value, "[MeshSolution]")
        self._meshsolution = value

        for obj in self._meshsolution:
            if obj is not None:
                obj.parent = self

    # FEA software mesh and solution
    # Type : [MeshSolution]
    meshsolution = property(
        fget=_get_meshsolution,
        fset=_set_meshsolution,
        doc=u"""FEA software mesh and solution""",
    )
