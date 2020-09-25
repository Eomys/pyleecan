# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/Interpolation/Interpolation.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/Interpolation
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from ._check import InitUnKnowClassError
from .RefCell import RefCell
from .GaussPoint import GaussPoint
from .ScalarProduct import ScalarProduct


class Interpolation(FrozenClass):
    """Store shape functions"""

    VERSION = 1

    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        ref_cell=None,
        gauss_point=None,
        scalar_product=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if ref_cell == -1:
            ref_cell = RefCell()
        if gauss_point == -1:
            gauss_point = GaussPoint()
        if scalar_product == -1:
            scalar_product = ScalarProduct()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            ref_cell = obj.ref_cell
            gauss_point = obj.gauss_point
            scalar_product = obj.scalar_product
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "ref_cell" in list(init_dict.keys()):
                ref_cell = init_dict["ref_cell"]
            if "gauss_point" in list(init_dict.keys()):
                gauss_point = init_dict["gauss_point"]
            if "scalar_product" in list(init_dict.keys()):
                scalar_product = init_dict["scalar_product"]
        # Initialisation by argument
        self.parent = None
        # ref_cell can be None, a RefCell object or a dict
        if isinstance(ref_cell, dict):
            # Check that the type is correct (including daughter)
            class_name = ref_cell.get("__class__")
            if class_name not in ["RefCell", "RefSegmentP1", "RefTriangle3"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for ref_cell"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.ref_cell = class_obj(init_dict=ref_cell)
        elif isinstance(ref_cell, str):
            from ..Functions.load import load

            ref_cell = load(ref_cell)
            # Check that the type is correct (including daughter)
            class_name = ref_cell.__class__.__name__
            if class_name not in ["RefCell", "RefSegmentP1", "RefTriangle3"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for ref_cell"
                )
            self.ref_cell = ref_cell
        else:
            self.ref_cell = ref_cell
        # gauss_point can be None, a GaussPoint object or a dict
        if isinstance(gauss_point, dict):
            # Check that the type is correct (including daughter)
            class_name = gauss_point.get("__class__")
            if class_name not in ["GaussPoint", "FPGNSeg", "FPGNTri"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for gauss_point"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.gauss_point = class_obj(init_dict=gauss_point)
        elif isinstance(gauss_point, str):
            from ..Functions.load import load

            gauss_point = load(gauss_point)
            # Check that the type is correct (including daughter)
            class_name = gauss_point.__class__.__name__
            if class_name not in ["GaussPoint", "FPGNSeg", "FPGNTri"]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for gauss_point"
                )
            self.gauss_point = gauss_point
        else:
            self.gauss_point = gauss_point
        # scalar_product can be None, a ScalarProduct object or a dict
        if isinstance(scalar_product, dict):
            # Check that the type is correct (including daughter)
            class_name = scalar_product.get("__class__")
            if class_name not in ["ScalarProduct", "ScalarProductL2"]:
                raise InitUnKnowClassError(
                    "Unknow class name "
                    + class_name
                    + " in init_dict for scalar_product"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.scalar_product = class_obj(init_dict=scalar_product)
        elif isinstance(scalar_product, str):
            from ..Functions.load import load

            scalar_product = load(scalar_product)
            # Check that the type is correct (including daughter)
            class_name = scalar_product.__class__.__name__
            if class_name not in ["ScalarProduct", "ScalarProductL2"]:
                raise InitUnKnowClassError(
                    "Unknow class name "
                    + class_name
                    + " in init_dict for scalar_product"
                )
            self.scalar_product = scalar_product
        else:
            self.scalar_product = scalar_product

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Interpolation_str = ""
        if self.parent is None:
            Interpolation_str += "parent = None " + linesep
        else:
            Interpolation_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        if self.ref_cell is not None:
            tmp = self.ref_cell.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Interpolation_str += "ref_cell = " + tmp
        else:
            Interpolation_str += "ref_cell = None" + linesep + linesep
        if self.gauss_point is not None:
            tmp = (
                self.gauss_point.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            Interpolation_str += "gauss_point = " + tmp
        else:
            Interpolation_str += "gauss_point = None" + linesep + linesep
        if self.scalar_product is not None:
            tmp = (
                self.scalar_product.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            Interpolation_str += "scalar_product = " + tmp
        else:
            Interpolation_str += "scalar_product = None" + linesep + linesep
        return Interpolation_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.ref_cell != self.ref_cell:
            return False
        if other.gauss_point != self.gauss_point:
            return False
        if other.scalar_product != self.scalar_product:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)"""

        Interpolation_dict = dict()
        if self.ref_cell is None:
            Interpolation_dict["ref_cell"] = None
        else:
            Interpolation_dict["ref_cell"] = self.ref_cell.as_dict()
        if self.gauss_point is None:
            Interpolation_dict["gauss_point"] = None
        else:
            Interpolation_dict["gauss_point"] = self.gauss_point.as_dict()
        if self.scalar_product is None:
            Interpolation_dict["scalar_product"] = None
        else:
            Interpolation_dict["scalar_product"] = self.scalar_product.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        Interpolation_dict["__class__"] = "Interpolation"
        return Interpolation_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.ref_cell is not None:
            self.ref_cell._set_None()
        if self.gauss_point is not None:
            self.gauss_point._set_None()
        if self.scalar_product is not None:
            self.scalar_product._set_None()

    def _get_ref_cell(self):
        """getter of ref_cell"""
        return self._ref_cell

    def _set_ref_cell(self, value):
        """setter of ref_cell"""
        check_var("ref_cell", value, "RefCell")
        self._ref_cell = value

        if self._ref_cell is not None:
            self._ref_cell.parent = self

    ref_cell = property(
        fget=_get_ref_cell,
        fset=_set_ref_cell,
        doc=u"""

        :Type: RefCell
        """,
    )

    def _get_gauss_point(self):
        """getter of gauss_point"""
        return self._gauss_point

    def _set_gauss_point(self, value):
        """setter of gauss_point"""
        check_var("gauss_point", value, "GaussPoint")
        self._gauss_point = value

        if self._gauss_point is not None:
            self._gauss_point.parent = self

    gauss_point = property(
        fget=_get_gauss_point,
        fset=_set_gauss_point,
        doc=u"""

        :Type: GaussPoint
        """,
    )

    def _get_scalar_product(self):
        """getter of scalar_product"""
        return self._scalar_product

    def _set_scalar_product(self, value):
        """setter of scalar_product"""
        check_var("scalar_product", value, "ScalarProduct")
        self._scalar_product = value

        if self._scalar_product is not None:
            self._scalar_product.parent = self

    scalar_product = property(
        fget=_get_scalar_product,
        fset=_set_scalar_product,
        doc=u"""

        :Type: ScalarProduct
        """,
    )
