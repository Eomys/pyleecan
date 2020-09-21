# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/InputCurrent.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/InputCurrent
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Input import Input

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.InputCurrent.gen_input import gen_input
except ImportError as error:
    gen_input = error

try:
    from ..Methods.Simulation.InputCurrent.set_Id_Iq import set_Id_Iq
except ImportError as error:
    set_Id_Iq = error

try:
    from ..Methods.Simulation.InputCurrent.comp_felec import comp_felec
except ImportError as error:
    comp_felec = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .ImportMatrix import ImportMatrix
from .Import import Import


class InputCurrent(Input):
    """Input to skip the electrical module and start with the magnetic one"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.InputCurrent.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputCurrent method gen_input: " + str(gen_input)
                )
            )
        )
    else:
        gen_input = gen_input
    # cf Methods.Simulation.InputCurrent.set_Id_Iq
    if isinstance(set_Id_Iq, ImportError):
        set_Id_Iq = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputCurrent method set_Id_Iq: " + str(set_Id_Iq)
                )
            )
        )
    else:
        set_Id_Iq = set_Id_Iq
    # cf Methods.Simulation.InputCurrent.comp_felec
    if isinstance(comp_felec, ImportError):
        comp_felec = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputCurrent method comp_felec: " + str(comp_felec)
                )
            )
        )
    else:
        comp_felec = comp_felec
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Is=None,
        Ir=None,
        angle_rotor=None,
        N0=None,
        rot_dir=-1,
        angle_rotor_initial=0,
        Tem_av_ref=None,
        Id_ref=None,
        Iq_ref=None,
        time=None,
        angle=None,
        Nt_tot=2048,
        Nrev=1,
        Na_tot=2048,
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

        if Is == -1:
            Is = ImportMatrix()
        if Ir == -1:
            Ir = ImportMatrix()
        if angle_rotor == -1:
            angle_rotor = Import()
        if time == -1:
            time = ImportMatrix()
        if angle == -1:
            angle = ImportMatrix()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            Is = obj.Is
            Ir = obj.Ir
            angle_rotor = obj.angle_rotor
            N0 = obj.N0
            rot_dir = obj.rot_dir
            angle_rotor_initial = obj.angle_rotor_initial
            Tem_av_ref = obj.Tem_av_ref
            Id_ref = obj.Id_ref
            Iq_ref = obj.Iq_ref
            time = obj.time
            angle = obj.angle
            Nt_tot = obj.Nt_tot
            Nrev = obj.Nrev
            Na_tot = obj.Na_tot
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Is" in list(init_dict.keys()):
                Is = init_dict["Is"]
            if "Ir" in list(init_dict.keys()):
                Ir = init_dict["Ir"]
            if "angle_rotor" in list(init_dict.keys()):
                angle_rotor = init_dict["angle_rotor"]
            if "N0" in list(init_dict.keys()):
                N0 = init_dict["N0"]
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
            if "Tem_av_ref" in list(init_dict.keys()):
                Tem_av_ref = init_dict["Tem_av_ref"]
            if "Id_ref" in list(init_dict.keys()):
                Id_ref = init_dict["Id_ref"]
            if "Iq_ref" in list(init_dict.keys()):
                Iq_ref = init_dict["Iq_ref"]
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Nrev" in list(init_dict.keys()):
                Nrev = init_dict["Nrev"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
        # Initialisation by argument
        # Is can be None, a ImportMatrix object or a dict
        if isinstance(Is, dict):
            # Check that the type is correct (including daughter)
            class_name = Is.get("__class__")
            if class_name not in [
                "ImportMatrix",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for Is"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.Is = class_obj(init_dict=Is)
        elif isinstance(Is, str):
            from ..Functions.load import load

            Is = load(Is)
            # Check that the type is correct (including daughter)
            class_name = Is.__class__.__name__
            if class_name not in [
                "ImportMatrix",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for Is"
                )
            self.Is = Is
        else:
            self.Is = Is
        # Ir can be None, a ImportMatrix object or a dict
        if isinstance(Ir, dict):
            # Check that the type is correct (including daughter)
            class_name = Ir.get("__class__")
            if class_name not in [
                "ImportMatrix",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for Ir"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.Ir = class_obj(init_dict=Ir)
        elif isinstance(Ir, str):
            from ..Functions.load import load

            Ir = load(Ir)
            # Check that the type is correct (including daughter)
            class_name = Ir.__class__.__name__
            if class_name not in [
                "ImportMatrix",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for Ir"
                )
            self.Ir = Ir
        else:
            self.Ir = Ir
        # angle_rotor can be None, a Import object or a dict
        if isinstance(angle_rotor, dict):
            # Check that the type is correct (including daughter)
            class_name = angle_rotor.get("__class__")
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for angle_rotor"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.angle_rotor = class_obj(init_dict=angle_rotor)
        elif isinstance(angle_rotor, str):
            from ..Functions.load import load

            angle_rotor = load(angle_rotor)
            # Check that the type is correct (including daughter)
            class_name = angle_rotor.__class__.__name__
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for angle_rotor"
                )
            self.angle_rotor = angle_rotor
        else:
            self.angle_rotor = angle_rotor
        self.N0 = N0
        self.rot_dir = rot_dir
        self.angle_rotor_initial = angle_rotor_initial
        self.Tem_av_ref = Tem_av_ref
        self.Id_ref = Id_ref
        self.Iq_ref = Iq_ref
        # Call Input init
        super(InputCurrent, self).__init__(
            time=time, angle=angle, Nt_tot=Nt_tot, Nrev=Nrev, Na_tot=Na_tot
        )
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        InputCurrent_str = ""
        # Get the properties inherited from Input
        InputCurrent_str += super(InputCurrent, self).__str__()
        if self.Is is not None:
            tmp = self.Is.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputCurrent_str += "Is = " + tmp
        else:
            InputCurrent_str += "Is = None" + linesep + linesep
        if self.Ir is not None:
            tmp = self.Ir.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputCurrent_str += "Ir = " + tmp
        else:
            InputCurrent_str += "Ir = None" + linesep + linesep
        if self.angle_rotor is not None:
            tmp = (
                self.angle_rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            InputCurrent_str += "angle_rotor = " + tmp
        else:
            InputCurrent_str += "angle_rotor = None" + linesep + linesep
        InputCurrent_str += "N0 = " + str(self.N0) + linesep
        InputCurrent_str += "rot_dir = " + str(self.rot_dir) + linesep
        InputCurrent_str += (
            "angle_rotor_initial = " + str(self.angle_rotor_initial) + linesep
        )
        InputCurrent_str += "Tem_av_ref = " + str(self.Tem_av_ref) + linesep
        InputCurrent_str += "Id_ref = " + str(self.Id_ref) + linesep
        InputCurrent_str += "Iq_ref = " + str(self.Iq_ref) + linesep
        return InputCurrent_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InputCurrent, self).__eq__(other):
            return False
        if other.Is != self.Is:
            return False
        if other.Ir != self.Ir:
            return False
        if other.angle_rotor != self.angle_rotor:
            return False
        if other.N0 != self.N0:
            return False
        if other.rot_dir != self.rot_dir:
            return False
        if other.angle_rotor_initial != self.angle_rotor_initial:
            return False
        if other.Tem_av_ref != self.Tem_av_ref:
            return False
        if other.Id_ref != self.Id_ref:
            return False
        if other.Iq_ref != self.Iq_ref:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Input
        InputCurrent_dict = super(InputCurrent, self).as_dict()
        if self.Is is None:
            InputCurrent_dict["Is"] = None
        else:
            InputCurrent_dict["Is"] = self.Is.as_dict()
        if self.Ir is None:
            InputCurrent_dict["Ir"] = None
        else:
            InputCurrent_dict["Ir"] = self.Ir.as_dict()
        if self.angle_rotor is None:
            InputCurrent_dict["angle_rotor"] = None
        else:
            InputCurrent_dict["angle_rotor"] = self.angle_rotor.as_dict()
        InputCurrent_dict["N0"] = self.N0
        InputCurrent_dict["rot_dir"] = self.rot_dir
        InputCurrent_dict["angle_rotor_initial"] = self.angle_rotor_initial
        InputCurrent_dict["Tem_av_ref"] = self.Tem_av_ref
        InputCurrent_dict["Id_ref"] = self.Id_ref
        InputCurrent_dict["Iq_ref"] = self.Iq_ref
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        InputCurrent_dict["__class__"] = "InputCurrent"
        return InputCurrent_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.Is is not None:
            self.Is._set_None()
        if self.Ir is not None:
            self.Ir._set_None()
        if self.angle_rotor is not None:
            self.angle_rotor._set_None()
        self.N0 = None
        self.rot_dir = None
        self.angle_rotor_initial = None
        self.Tem_av_ref = None
        self.Id_ref = None
        self.Iq_ref = None
        # Set to None the properties inherited from Input
        super(InputCurrent, self)._set_None()

    def _get_Is(self):
        """getter of Is"""
        return self._Is

    def _set_Is(self, value):
        """setter of Is"""
        if isinstance(value, ndarray):
            value = ImportMatrixVal(value=value)
        elif isinstance(value, list):
            value = ImportMatrixVal(value=array(value))
        check_var("Is", value, "ImportMatrix")
        self._Is = value

        if self._Is is not None:
            self._Is.parent = self

    Is = property(
        fget=_get_Is,
        fset=_set_Is,
        doc=u"""Stator currents as a function of time (each column correspond to one phase) to import

        :Type: ImportMatrix
        """,
    )

    def _get_Ir(self):
        """getter of Ir"""
        return self._Ir

    def _set_Ir(self, value):
        """setter of Ir"""
        if isinstance(value, ndarray):
            value = ImportMatrixVal(value=value)
        elif isinstance(value, list):
            value = ImportMatrixVal(value=array(value))
        check_var("Ir", value, "ImportMatrix")
        self._Ir = value

        if self._Ir is not None:
            self._Ir.parent = self

    Ir = property(
        fget=_get_Ir,
        fset=_set_Ir,
        doc=u"""Rotor currents as a function of time (each column correspond to one phase) to import

        :Type: ImportMatrix
        """,
    )

    def _get_angle_rotor(self):
        """getter of angle_rotor"""
        return self._angle_rotor

    def _set_angle_rotor(self, value):
        """setter of angle_rotor"""
        check_var("angle_rotor", value, "Import")
        self._angle_rotor = value

        if self._angle_rotor is not None:
            self._angle_rotor.parent = self

    angle_rotor = property(
        fget=_get_angle_rotor,
        fset=_set_angle_rotor,
        doc=u"""Rotor angular position as a function of time (if None computed according to Nr) to import

        :Type: Import
        """,
    )

    def _get_N0(self):
        """getter of N0"""
        return self._N0

    def _set_N0(self, value):
        """setter of N0"""
        check_var("N0", value, "float")
        self._N0 = value

    N0 = property(
        fget=_get_N0,
        fset=_set_N0,
        doc=u"""Rotor speed

        :Type: float
        """,
    )

    def _get_rot_dir(self):
        """getter of rot_dir"""
        return self._rot_dir

    def _set_rot_dir(self, value):
        """setter of rot_dir"""
        check_var("rot_dir", value, "float", Vmin=-1, Vmax=1)
        self._rot_dir = value

    rot_dir = property(
        fget=_get_rot_dir,
        fset=_set_rot_dir,
        doc=u"""Rotation direction of the rotor 1 trigo, -1 clockwise

        :Type: float
        :min: -1
        :max: 1
        """,
    )

    def _get_angle_rotor_initial(self):
        """getter of angle_rotor_initial"""
        return self._angle_rotor_initial

    def _set_angle_rotor_initial(self, value):
        """setter of angle_rotor_initial"""
        check_var("angle_rotor_initial", value, "float")
        self._angle_rotor_initial = value

    angle_rotor_initial = property(
        fget=_get_angle_rotor_initial,
        fset=_set_angle_rotor_initial,
        doc=u"""Initial angular position of the rotor at t=0

        :Type: float
        """,
    )

    def _get_Tem_av_ref(self):
        """getter of Tem_av_ref"""
        return self._Tem_av_ref

    def _set_Tem_av_ref(self, value):
        """setter of Tem_av_ref"""
        check_var("Tem_av_ref", value, "float")
        self._Tem_av_ref = value

    Tem_av_ref = property(
        fget=_get_Tem_av_ref,
        fset=_set_Tem_av_ref,
        doc=u"""Theorical Average Electromagnetic torque

        :Type: float
        """,
    )

    def _get_Id_ref(self):
        """getter of Id_ref"""
        return self._Id_ref

    def _set_Id_ref(self, value):
        """setter of Id_ref"""
        check_var("Id_ref", value, "float")
        self._Id_ref = value

    Id_ref = property(
        fget=_get_Id_ref,
        fset=_set_Id_ref,
        doc=u"""d-axis current magnitude

        :Type: float
        """,
    )

    def _get_Iq_ref(self):
        """getter of Iq_ref"""
        return self._Iq_ref

    def _set_Iq_ref(self, value):
        """setter of Iq_ref"""
        check_var("Iq_ref", value, "float")
        self._Iq_ref = value

    Iq_ref = property(
        fget=_get_Iq_ref,
        fset=_set_Iq_ref,
        doc=u"""q-axis current magnitude

        :Type: float
        """,
    )
