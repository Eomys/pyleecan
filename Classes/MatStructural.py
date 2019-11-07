# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Classes.check import InitUnKnowClassError


class MatStructural(FrozenClass):
    """Material Structural properties"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(
        self,
        rho=7650,
        Ex=215000000000.0,
        Ey=215000000000.0,
        Ez=80000000000,
        nu_xy=0.3,
        nu_xz=0.03,
        nu_yz=0.03,
        Gxz=2000000000,
        Gxy=0,
        Gyz=2000000000,
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
                    "rho",
                    "Ex",
                    "Ey",
                    "Ez",
                    "nu_xy",
                    "nu_xz",
                    "nu_yz",
                    "Gxz",
                    "Gxy",
                    "Gyz",
                ],
            )
            # Overwrite default value with init_dict content
            if "rho" in list(init_dict.keys()):
                rho = init_dict["rho"]
            if "Ex" in list(init_dict.keys()):
                Ex = init_dict["Ex"]
            if "Ey" in list(init_dict.keys()):
                Ey = init_dict["Ey"]
            if "Ez" in list(init_dict.keys()):
                Ez = init_dict["Ez"]
            if "nu_xy" in list(init_dict.keys()):
                nu_xy = init_dict["nu_xy"]
            if "nu_xz" in list(init_dict.keys()):
                nu_xz = init_dict["nu_xz"]
            if "nu_yz" in list(init_dict.keys()):
                nu_yz = init_dict["nu_yz"]
            if "Gxz" in list(init_dict.keys()):
                Gxz = init_dict["Gxz"]
            if "Gxy" in list(init_dict.keys()):
                Gxy = init_dict["Gxy"]
            if "Gyz" in list(init_dict.keys()):
                Gyz = init_dict["Gyz"]
        # Initialisation by argument
        self.parent = None
        self.rho = rho
        self.Ex = Ex
        self.Ey = Ey
        self.Ez = Ez
        self.nu_xy = nu_xy
        self.nu_xz = nu_xz
        self.nu_yz = nu_yz
        self.Gxz = Gxz
        self.Gxy = Gxy
        self.Gyz = Gyz

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MatStructural_str = ""
        if self.parent is None:
            MatStructural_str += "parent = None " + linesep
        else:
            MatStructural_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        MatStructural_str += "rho = " + str(self.rho) + linesep
        MatStructural_str += "Ex = " + str(self.Ex) + linesep
        MatStructural_str += "Ey = " + str(self.Ey) + linesep
        MatStructural_str += "Ez = " + str(self.Ez) + linesep
        MatStructural_str += "nu_xy = " + str(self.nu_xy) + linesep
        MatStructural_str += "nu_xz = " + str(self.nu_xz) + linesep
        MatStructural_str += "nu_yz = " + str(self.nu_yz) + linesep
        MatStructural_str += "Gxz = " + str(self.Gxz) + linesep
        MatStructural_str += "Gxy = " + str(self.Gxy) + linesep
        MatStructural_str += "Gyz = " + str(self.Gyz)
        return MatStructural_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.rho != self.rho:
            return False
        if other.Ex != self.Ex:
            return False
        if other.Ey != self.Ey:
            return False
        if other.Ez != self.Ez:
            return False
        if other.nu_xy != self.nu_xy:
            return False
        if other.nu_xz != self.nu_xz:
            return False
        if other.nu_yz != self.nu_yz:
            return False
        if other.Gxz != self.Gxz:
            return False
        if other.Gxy != self.Gxy:
            return False
        if other.Gyz != self.Gyz:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        MatStructural_dict = dict()
        MatStructural_dict["rho"] = self.rho
        MatStructural_dict["Ex"] = self.Ex
        MatStructural_dict["Ey"] = self.Ey
        MatStructural_dict["Ez"] = self.Ez
        MatStructural_dict["nu_xy"] = self.nu_xy
        MatStructural_dict["nu_xz"] = self.nu_xz
        MatStructural_dict["nu_yz"] = self.nu_yz
        MatStructural_dict["Gxz"] = self.Gxz
        MatStructural_dict["Gxy"] = self.Gxy
        MatStructural_dict["Gyz"] = self.Gyz
        # The class name is added to the dict fordeserialisation purpose
        MatStructural_dict["__class__"] = "MatStructural"
        return MatStructural_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.rho = None
        self.Ex = None
        self.Ey = None
        self.Ez = None
        self.nu_xy = None
        self.nu_xz = None
        self.nu_yz = None
        self.Gxz = None
        self.Gxy = None
        self.Gyz = None

    def _get_rho(self):
        """getter of rho"""
        return self._rho

    def _set_rho(self, value):
        """setter of rho"""
        check_var("rho", value, "float", Vmin=0)
        self._rho = value

    # mass per unit volume [kg/m3]
    # Type : float, min = 0
    rho = property(
        fget=_get_rho, fset=_set_rho, doc=u"""mass per unit volume [kg/m3]"""
    )

    def _get_Ex(self):
        """getter of Ex"""
        return self._Ex

    def _set_Ex(self, value):
        """setter of Ex"""
        check_var("Ex", value, "float", Vmin=0)
        self._Ex = value

    # equivalent Young modulus (XY is lamination plane; Z is rotation axis)
    # Type : float, min = 0
    Ex = property(
        fget=_get_Ex,
        fset=_set_Ex,
        doc=u"""equivalent Young modulus (XY is lamination plane; Z is rotation axis)""",
    )

    def _get_Ey(self):
        """getter of Ey"""
        return self._Ey

    def _set_Ey(self, value):
        """setter of Ey"""
        check_var("Ey", value, "float", Vmin=0)
        self._Ey = value

    # equivalent Young modulus (XY is lamination plane; Z is rotation axis)
    # Type : float, min = 0
    Ey = property(
        fget=_get_Ey,
        fset=_set_Ey,
        doc=u"""equivalent Young modulus (XY is lamination plane; Z is rotation axis)""",
    )

    def _get_Ez(self):
        """getter of Ez"""
        return self._Ez

    def _set_Ez(self, value):
        """setter of Ez"""
        check_var("Ez", value, "float", Vmin=0)
        self._Ez = value

    # equivalent Young modulus (XY is lamination plane; Z is rotation axis)
    # Type : float, min = 0
    Ez = property(
        fget=_get_Ez,
        fset=_set_Ez,
        doc=u"""equivalent Young modulus (XY is lamination plane; Z is rotation axis)""",
    )

    def _get_nu_xy(self):
        """getter of nu_xy"""
        return self._nu_xy

    def _set_nu_xy(self, value):
        """setter of nu_xy"""
        check_var("nu_xy", value, "float", Vmin=0)
        self._nu_xy = value

    # equivalent Poisson ratio in the XY plane (XY is lamination plane; Z is rotation axis)
    # Type : float, min = 0
    nu_xy = property(
        fget=_get_nu_xy,
        fset=_set_nu_xy,
        doc=u"""equivalent Poisson ratio in the XY plane (XY is lamination plane; Z is rotation axis)""",
    )

    def _get_nu_xz(self):
        """getter of nu_xz"""
        return self._nu_xz

    def _set_nu_xz(self, value):
        """setter of nu_xz"""
        check_var("nu_xz", value, "float", Vmin=0)
        self._nu_xz = value

    # equivalent Poisson ratio in the XZ plane (XY is lamination plane; Z is rotation axis)
    # Type : float, min = 0
    nu_xz = property(
        fget=_get_nu_xz,
        fset=_set_nu_xz,
        doc=u"""equivalent Poisson ratio in the XZ plane (XY is lamination plane; Z is rotation axis)""",
    )

    def _get_nu_yz(self):
        """getter of nu_yz"""
        return self._nu_yz

    def _set_nu_yz(self, value):
        """setter of nu_yz"""
        check_var("nu_yz", value, "float", Vmin=0)
        self._nu_yz = value

    # equivalent Poisson ratio in the YZ plane (XY is lamination plane; Z is rotation axis)
    # Type : float, min = 0
    nu_yz = property(
        fget=_get_nu_yz,
        fset=_set_nu_yz,
        doc=u"""equivalent Poisson ratio in the YZ plane (XY is lamination plane; Z is rotation axis)""",
    )

    def _get_Gxz(self):
        """getter of Gxz"""
        return self._Gxz

    def _set_Gxz(self, value):
        """setter of Gxz"""
        check_var("Gxz", value, "float", Vmin=0)
        self._Gxz = value

    # shear modulus in XY plane (XY is lamination plane; Z is rotation axis)
    # Type : float, min = 0
    Gxz = property(
        fget=_get_Gxz,
        fset=_set_Gxz,
        doc=u"""shear modulus in XY plane (XY is lamination plane; Z is rotation axis)""",
    )

    def _get_Gxy(self):
        """getter of Gxy"""
        return self._Gxy

    def _set_Gxy(self, value):
        """setter of Gxy"""
        check_var("Gxy", value, "float", Vmin=0)
        self._Gxy = value

    # shear modulus in XZ plane (XY is lamination plane; Z is rotation axis)
    # Type : float, min = 0
    Gxy = property(
        fget=_get_Gxy,
        fset=_set_Gxy,
        doc=u"""shear modulus in XZ plane (XY is lamination plane; Z is rotation axis)""",
    )

    def _get_Gyz(self):
        """getter of Gyz"""
        return self._Gyz

    def _set_Gyz(self, value):
        """setter of Gyz"""
        check_var("Gyz", value, "float", Vmin=0)
        self._Gyz = value

    # shear modulus in YZ plane (XY is lamination plane; Z is rotation axis)
    # Type : float, min = 0
    Gyz = property(
        fget=_get_Gyz,
        fset=_set_Gyz,
        doc=u"""shear modulus in YZ plane (XY is lamination plane; Z is rotation axis)""",
    )
