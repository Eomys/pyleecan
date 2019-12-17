# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.MatMagnetics import MatMagnetics

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Material.MatLamination.get_BH import get_BH
except ImportError as error:
    get_BH = error


from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.ImportMatrix import ImportMatrix


class MatLamination(MatMagnetics):
    """lamination properties"""

    VERSION = 1

    # cf Methods.Material.MatLamination.get_BH
    if isinstance(get_BH, ImportError):
        get_BH = property(
            fget=lambda x: raise_(
                ImportError("Can't use MatLamination method get_BH: " + str(get_BH))
            )
        )
    else:
        get_BH = get_BH
    # save method is available in all object
    save = save

    def __init__(self, Wlam=0.0005, BH_curve=-1, mur_lin=1, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if BH_curve == -1:
            BH_curve = ImportMatrix()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["Wlam", "BH_curve", "mur_lin"])
            # Overwrite default value with init_dict content
            if "Wlam" in list(init_dict.keys()):
                Wlam = init_dict["Wlam"]
            if "BH_curve" in list(init_dict.keys()):
                BH_curve = init_dict["BH_curve"]
            if "mur_lin" in list(init_dict.keys()):
                mur_lin = init_dict["mur_lin"]
        # Initialisation by argument
        self.Wlam = Wlam
        # BH_curve can be None, a ImportMatrix object or a dict
        if isinstance(BH_curve, dict):
            # Check that the type is correct (including daughter)
            class_name = BH_curve.get("__class__")
            if class_name not in [
                "ImportMatrix",
                "ImportGenMatrixSin",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for BH_curve"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.BH_curve = class_obj(init_dict=BH_curve)
        else:
            self.BH_curve = BH_curve
        # Call MatMagnetics init
        super(MatLamination, self).__init__(mur_lin=mur_lin)
        # The class is frozen (in MatMagnetics init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        MatLamination_str = ""
        # Get the properties inherited from MatMagnetics
        MatLamination_str += super(MatLamination, self).__str__() + linesep
        MatLamination_str += "Wlam = " + str(self.Wlam) + linesep
        if self.BH_curve is not None:
            MatLamination_str += (
                "BH_curve = " + str(self.BH_curve.as_dict()) + linesep + linesep
            )
        else:
            MatLamination_str += "BH_curve = None"
        return MatLamination_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MatMagnetics
        if not super(MatLamination, self).__eq__(other):
            return False
        if other.Wlam != self.Wlam:
            return False
        if other.BH_curve != self.BH_curve:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from MatMagnetics
        MatLamination_dict = super(MatLamination, self).as_dict()
        MatLamination_dict["Wlam"] = self.Wlam
        if self.BH_curve is None:
            MatLamination_dict["BH_curve"] = None
        else:
            MatLamination_dict["BH_curve"] = self.BH_curve.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MatLamination_dict["__class__"] = "MatLamination"
        return MatLamination_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Wlam = None
        if self.BH_curve is not None:
            self.BH_curve._set_None()
        # Set to None the properties inherited from MatMagnetics
        super(MatLamination, self)._set_None()

    def _get_Wlam(self):
        """getter of Wlam"""
        return self._Wlam

    def _set_Wlam(self, value):
        """setter of Wlam"""
        check_var("Wlam", value, "float", Vmin=0)
        self._Wlam = value

    # lamination sheet width without insulation [m] (for magnetic loss model)
    # Type : float, min = 0
    Wlam = property(
        fget=_get_Wlam,
        fset=_set_Wlam,
        doc=u"""lamination sheet width without insulation [m] (for magnetic loss model)""",
    )

    def _get_BH_curve(self):
        """getter of BH_curve"""
        return self._BH_curve

    def _set_BH_curve(self, value):
        """setter of BH_curve"""
        check_var("BH_curve", value, "ImportMatrix")
        self._BH_curve = value

        if self._BH_curve is not None:
            self._BH_curve.parent = self

    # B(H) curve (two columns matrix, H and B(H))
    # Type : ImportMatrix
    BH_curve = property(
        fget=_get_BH_curve,
        fset=_set_BH_curve,
        doc=u"""B(H) curve (two columns matrix, H and B(H))""",
    )
