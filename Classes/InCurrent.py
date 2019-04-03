# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Input import Input

from pyleecan.Methods.Simulation.InCurrent.gen_input import gen_input

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.ImportMatrix import ImportMatrix
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportMatrixXls import ImportMatrixXls
from pyleecan.Classes.ImportGenVectSin import ImportGenVectSin
from pyleecan.Classes.ImportGenMatrixSin import ImportGenMatrixSin


class InCurrent(Input):
    """Input to skip the electrical module and start with the magnetic one"""

    VERSION = 1

    # cf Methods.Simulation.InCurrent.gen_input
    gen_input = gen_input
    # save method is available in all object
    save = save

    def __init__(
        self,
        time=None,
        angle=None,
        Is=None,
        Ir=None,
        angle_rotor=None,
        Nr=None,
        rot_dir=-1,
        angle_rotor_initial=0,
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if time == -1:
            time = ImportMatrix()
        if angle == -1:
            angle = ImportMatrix()
        if Is == -1:
            Is = ImportMatrix()
        if Ir == -1:
            Ir = ImportMatrix()
        if angle_rotor == -1:
            angle_rotor = ImportMatrix()
        if Nr == -1:
            Nr = ImportMatrix()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
                    "time",
                    "angle",
                    "Is",
                    "Ir",
                    "angle_rotor",
                    "Nr",
                    "rot_dir",
                    "angle_rotor_initial",
                ],
            )
            # Overwrite default value with init_dict content
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Is" in list(init_dict.keys()):
                Is = init_dict["Is"]
            if "Ir" in list(init_dict.keys()):
                Ir = init_dict["Ir"]
            if "angle_rotor" in list(init_dict.keys()):
                angle_rotor = init_dict["angle_rotor"]
            if "Nr" in list(init_dict.keys()):
                Nr = init_dict["Nr"]
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
        # Initialisation by argument
        # time can be None, a ImportMatrix object or a dict
        if isinstance(time, dict):
            # Call the correct constructor according to the dict
            load_dict = {
                "ImportMatrixVal": ImportMatrixVal,
                "ImportMatrixXls": ImportMatrixXls,
                "ImportGenVectSin": ImportGenVectSin,
                "ImportGenMatrixSin": ImportGenMatrixSin,
                "ImportMatrix": ImportMatrix,
            }
            obj_class = time.get("__class__")
            if obj_class is None:
                self.time = ImportMatrix(init_dict=time)
            elif obj_class in list(load_dict.keys()):
                self.time = load_dict[obj_class](init_dict=time)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError("Unknow class name in init_dict for time")
        else:
            self.time = time
        # angle can be None, a ImportMatrix object or a dict
        if isinstance(angle, dict):
            # Call the correct constructor according to the dict
            load_dict = {
                "ImportMatrixVal": ImportMatrixVal,
                "ImportMatrixXls": ImportMatrixXls,
                "ImportGenVectSin": ImportGenVectSin,
                "ImportGenMatrixSin": ImportGenMatrixSin,
                "ImportMatrix": ImportMatrix,
            }
            obj_class = angle.get("__class__")
            if obj_class is None:
                self.angle = ImportMatrix(init_dict=angle)
            elif obj_class in list(load_dict.keys()):
                self.angle = load_dict[obj_class](init_dict=angle)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError("Unknow class name in init_dict for angle")
        else:
            self.angle = angle
        # Is can be None, a ImportMatrix object or a dict
        if isinstance(Is, dict):
            # Call the correct constructor according to the dict
            load_dict = {
                "ImportMatrixVal": ImportMatrixVal,
                "ImportMatrixXls": ImportMatrixXls,
                "ImportGenVectSin": ImportGenVectSin,
                "ImportGenMatrixSin": ImportGenMatrixSin,
                "ImportMatrix": ImportMatrix,
            }
            obj_class = Is.get("__class__")
            if obj_class is None:
                self.Is = ImportMatrix(init_dict=Is)
            elif obj_class in list(load_dict.keys()):
                self.Is = load_dict[obj_class](init_dict=Is)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError("Unknow class name in init_dict for Is")
        else:
            self.Is = Is
        # Ir can be None, a ImportMatrix object or a dict
        if isinstance(Ir, dict):
            # Call the correct constructor according to the dict
            load_dict = {
                "ImportMatrixVal": ImportMatrixVal,
                "ImportMatrixXls": ImportMatrixXls,
                "ImportGenVectSin": ImportGenVectSin,
                "ImportGenMatrixSin": ImportGenMatrixSin,
                "ImportMatrix": ImportMatrix,
            }
            obj_class = Ir.get("__class__")
            if obj_class is None:
                self.Ir = ImportMatrix(init_dict=Ir)
            elif obj_class in list(load_dict.keys()):
                self.Ir = load_dict[obj_class](init_dict=Ir)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError("Unknow class name in init_dict for Ir")
        else:
            self.Ir = Ir
        # angle_rotor can be None, a ImportMatrix object or a dict
        if isinstance(angle_rotor, dict):
            # Call the correct constructor according to the dict
            load_dict = {
                "ImportMatrixVal": ImportMatrixVal,
                "ImportMatrixXls": ImportMatrixXls,
                "ImportGenVectSin": ImportGenVectSin,
                "ImportGenMatrixSin": ImportGenMatrixSin,
                "ImportMatrix": ImportMatrix,
            }
            obj_class = angle_rotor.get("__class__")
            if obj_class is None:
                self.angle_rotor = ImportMatrix(init_dict=angle_rotor)
            elif obj_class in list(load_dict.keys()):
                self.angle_rotor = load_dict[obj_class](init_dict=angle_rotor)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError(
                    "Unknow class name in init_dict for angle_rotor"
                )
        else:
            self.angle_rotor = angle_rotor
        # Nr can be None, a ImportMatrix object or a dict
        if isinstance(Nr, dict):
            # Call the correct constructor according to the dict
            load_dict = {
                "ImportMatrixVal": ImportMatrixVal,
                "ImportMatrixXls": ImportMatrixXls,
                "ImportGenVectSin": ImportGenVectSin,
                "ImportGenMatrixSin": ImportGenMatrixSin,
                "ImportMatrix": ImportMatrix,
            }
            obj_class = Nr.get("__class__")
            if obj_class is None:
                self.Nr = ImportMatrix(init_dict=Nr)
            elif obj_class in list(load_dict.keys()):
                self.Nr = load_dict[obj_class](init_dict=Nr)
            else:  # Avoid generation error or wrong modification in json
                raise InitUnKnowClassError("Unknow class name in init_dict for Nr")
        else:
            self.Nr = Nr
        self.rot_dir = rot_dir
        self.angle_rotor_initial = angle_rotor_initial
        # Call Input init
        super(InCurrent, self).__init__()
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        InCurrent_str = ""
        # Get the properties inherited from Input
        InCurrent_str += super(InCurrent, self).__str__() + linesep
        InCurrent_str += "time = " + str(self.time.as_dict()) + linesep + linesep
        InCurrent_str += "angle = " + str(self.angle.as_dict()) + linesep + linesep
        InCurrent_str += "Is = " + str(self.Is.as_dict()) + linesep + linesep
        InCurrent_str += "Ir = " + str(self.Ir.as_dict()) + linesep + linesep
        InCurrent_str += (
            "angle_rotor = " + str(self.angle_rotor.as_dict()) + linesep + linesep
        )
        InCurrent_str += "Nr = " + str(self.Nr.as_dict()) + linesep + linesep
        InCurrent_str += "rot_dir = " + str(self.rot_dir) + linesep
        InCurrent_str += "angle_rotor_initial = " + str(self.angle_rotor_initial)
        return InCurrent_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InCurrent, self).__eq__(other):
            return False
        if other.time != self.time:
            return False
        if other.angle != self.angle:
            return False
        if other.Is != self.Is:
            return False
        if other.Ir != self.Ir:
            return False
        if other.angle_rotor != self.angle_rotor:
            return False
        if other.Nr != self.Nr:
            return False
        if other.rot_dir != self.rot_dir:
            return False
        if other.angle_rotor_initial != self.angle_rotor_initial:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Input
        InCurrent_dict = super(InCurrent, self).as_dict()
        if self.time is None:
            InCurrent_dict["time"] = None
        else:
            InCurrent_dict["time"] = self.time.as_dict()
        if self.angle is None:
            InCurrent_dict["angle"] = None
        else:
            InCurrent_dict["angle"] = self.angle.as_dict()
        if self.Is is None:
            InCurrent_dict["Is"] = None
        else:
            InCurrent_dict["Is"] = self.Is.as_dict()
        if self.Ir is None:
            InCurrent_dict["Ir"] = None
        else:
            InCurrent_dict["Ir"] = self.Ir.as_dict()
        if self.angle_rotor is None:
            InCurrent_dict["angle_rotor"] = None
        else:
            InCurrent_dict["angle_rotor"] = self.angle_rotor.as_dict()
        if self.Nr is None:
            InCurrent_dict["Nr"] = None
        else:
            InCurrent_dict["Nr"] = self.Nr.as_dict()
        InCurrent_dict["rot_dir"] = self.rot_dir
        InCurrent_dict["angle_rotor_initial"] = self.angle_rotor_initial
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        InCurrent_dict["__class__"] = "InCurrent"
        return InCurrent_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.time is not None:
            self.time._set_None()
        if self.angle is not None:
            self.angle._set_None()
        if self.Is is not None:
            self.Is._set_None()
        if self.Ir is not None:
            self.Ir._set_None()
        if self.angle_rotor is not None:
            self.angle_rotor._set_None()
        if self.Nr is not None:
            self.Nr._set_None()
        self.rot_dir = None
        self.angle_rotor_initial = None
        # Set to None the properties inherited from Input
        super(InCurrent, self)._set_None()

    def _get_time(self):
        """getter of time"""
        return self._time

    def _set_time(self, value):
        """setter of time"""
        check_var("time", value, "ImportMatrix")
        self._time = value

        if self._time is not None:
            self._time.parent = self

    # Electrical time vector (no symmetry) to import
    # Type : ImportMatrix
    time = property(
        fget=_get_time,
        fset=_set_time,
        doc=u"""Electrical time vector (no symmetry) to import""",
    )

    def _get_angle(self):
        """getter of angle"""
        return self._angle

    def _set_angle(self, value):
        """setter of angle"""
        check_var("angle", value, "ImportMatrix")
        self._angle = value

        if self._angle is not None:
            self._angle.parent = self

    # Electrical position vector (no symmetry) to import
    # Type : ImportMatrix
    angle = property(
        fget=_get_angle,
        fset=_set_angle,
        doc=u"""Electrical position vector (no symmetry) to import""",
    )

    def _get_Is(self):
        """getter of Is"""
        return self._Is

    def _set_Is(self, value):
        """setter of Is"""
        check_var("Is", value, "ImportMatrix")
        self._Is = value

        if self._Is is not None:
            self._Is.parent = self

    # Stator currents as a function of time (each column correspond to one phase) to import
    # Type : ImportMatrix
    Is = property(
        fget=_get_Is,
        fset=_set_Is,
        doc=u"""Stator currents as a function of time (each column correspond to one phase) to import""",
    )

    def _get_Ir(self):
        """getter of Ir"""
        return self._Ir

    def _set_Ir(self, value):
        """setter of Ir"""
        check_var("Ir", value, "ImportMatrix")
        self._Ir = value

        if self._Ir is not None:
            self._Ir.parent = self

    # Rotor currents as a function of time (each column correspond to one phase) to import
    # Type : ImportMatrix
    Ir = property(
        fget=_get_Ir,
        fset=_set_Ir,
        doc=u"""Rotor currents as a function of time (each column correspond to one phase) to import""",
    )

    def _get_angle_rotor(self):
        """getter of angle_rotor"""
        return self._angle_rotor

    def _set_angle_rotor(self, value):
        """setter of angle_rotor"""
        check_var("angle_rotor", value, "ImportMatrix")
        self._angle_rotor = value

        if self._angle_rotor is not None:
            self._angle_rotor.parent = self

    # Rotor angular position as a function of time (if None computed according to Nr) to import
    # Type : ImportMatrix
    angle_rotor = property(
        fget=_get_angle_rotor,
        fset=_set_angle_rotor,
        doc=u"""Rotor angular position as a function of time (if None computed according to Nr) to import""",
    )

    def _get_Nr(self):
        """getter of Nr"""
        return self._Nr

    def _set_Nr(self, value):
        """setter of Nr"""
        check_var("Nr", value, "ImportMatrix")
        self._Nr = value

        if self._Nr is not None:
            self._Nr.parent = self

    # Rotor speed as a function of time to import
    # Type : ImportMatrix
    Nr = property(
        fget=_get_Nr,
        fset=_set_Nr,
        doc=u"""Rotor speed as a function of time to import""",
    )

    def _get_rot_dir(self):
        """getter of rot_dir"""
        return self._rot_dir

    def _set_rot_dir(self, value):
        """setter of rot_dir"""
        check_var("rot_dir", value, "float", Vmin=-1, Vmax=1)
        self._rot_dir = value

    # Rotation direction of the rotor 1 trigo, -1 clockwise
    # Type : float, min = -1, max = 1
    rot_dir = property(
        fget=_get_rot_dir,
        fset=_set_rot_dir,
        doc=u"""Rotation direction of the rotor 1 trigo, -1 clockwise""",
    )

    def _get_angle_rotor_initial(self):
        """getter of angle_rotor_initial"""
        return self._angle_rotor_initial

    def _set_angle_rotor_initial(self, value):
        """setter of angle_rotor_initial"""
        check_var("angle_rotor_initial", value, "float")
        self._angle_rotor_initial = value

    # Initial angular position of the rotor at t=0
    # Type : float
    angle_rotor_initial = property(
        fget=_get_angle_rotor_initial,
        fset=_set_angle_rotor_initial,
        doc=u"""Initial angular position of the rotor at t=0""",
    )
