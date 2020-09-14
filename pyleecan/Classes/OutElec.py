# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutElec.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutElec
"""

from os import linesep
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.OutElec.get_Nr import get_Nr
except ImportError as error:
    get_Nr = error

try:
    from ..Methods.Output.OutElec.get_Is import get_Is
except ImportError as error:
    get_Is = error

try:
    from ..Methods.Output.OutElec.get_Us import get_Us
except ImportError as error:
    get_Us = error


from numpy import array, array_equal
from cloudpickle import dumps, loads
from ._check import CheckTypeError
try :
    from SciDataTool.Classes.DataND import DataND
except ImportError :
    DataND = ImportError
from ._check import InitUnKnowClassError


class OutElec(FrozenClass):
    """Gather the electric module outputs"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.OutElec.get_Nr
    if isinstance(get_Nr, ImportError):
        get_Nr = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_Nr: " + str(get_Nr))
            )
        )
    else:
        get_Nr = get_Nr
    # cf Methods.Output.OutElec.get_Is
    if isinstance(get_Is, ImportError):
        get_Is = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_Is: " + str(get_Is))
            )
        )
    else:
        get_Is = get_Is
    # cf Methods.Output.OutElec.get_Us
    if isinstance(get_Us, ImportError):
        get_Us = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutElec method get_Us: " + str(get_Us))
            )
        )
    else:
        get_Us = get_Us
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, time=None, angle=None, Is=None, Ir=None, angle_rotor=None, N0=None, rot_dir=-1, angle_rotor_initial=0, logger_name="Pyleecan.OutElec", mmf_unit=None, Tem_av_ref=None, Id_ref=None, Iq_ref=None, felec=None, Ud_ref=None, Uq_ref=None, Pj_losses=None, Pem_av_ref=None, Us=None, init_dict = None, init_str = None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None :  # Initialisation by str
            from ..Functions.load import load
            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            time = obj.time
            angle = obj.angle
            Is = obj.Is
            Ir = obj.Ir
            angle_rotor = obj.angle_rotor
            N0 = obj.N0
            rot_dir = obj.rot_dir
            angle_rotor_initial = obj.angle_rotor_initial
            logger_name = obj.logger_name
            mmf_unit = obj.mmf_unit
            Tem_av_ref = obj.Tem_av_ref
            Id_ref = obj.Id_ref
            Iq_ref = obj.Iq_ref
            felec = obj.felec
            Ud_ref = obj.Ud_ref
            Uq_ref = obj.Uq_ref
            Pj_losses = obj.Pj_losses
            Pem_av_ref = obj.Pem_av_ref
            Us = obj.Us
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
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
            if "N0" in list(init_dict.keys()):
                N0 = init_dict["N0"]
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "mmf_unit" in list(init_dict.keys()):
                mmf_unit = init_dict["mmf_unit"]
            if "Tem_av_ref" in list(init_dict.keys()):
                Tem_av_ref = init_dict["Tem_av_ref"]
            if "Id_ref" in list(init_dict.keys()):
                Id_ref = init_dict["Id_ref"]
            if "Iq_ref" in list(init_dict.keys()):
                Iq_ref = init_dict["Iq_ref"]
            if "felec" in list(init_dict.keys()):
                felec = init_dict["felec"]
            if "Ud_ref" in list(init_dict.keys()):
                Ud_ref = init_dict["Ud_ref"]
            if "Uq_ref" in list(init_dict.keys()):
                Uq_ref = init_dict["Uq_ref"]
            if "Pj_losses" in list(init_dict.keys()):
                Pj_losses = init_dict["Pj_losses"]
            if "Pem_av_ref" in list(init_dict.keys()):
                Pem_av_ref = init_dict["Pem_av_ref"]
            if "Us" in list(init_dict.keys()):
                Us = init_dict["Us"]
        # Initialisation by argument
        self.parent = None
        # time can be None, a ndarray or a list
        set_array(self, "time", time)
        # angle can be None, a ndarray or a list
        set_array(self, "angle", angle)
        # Check if the type DataND has been imported with success
        if isinstance(DataND, ImportError):
            raise ImportError('Unknown type DataND please install SciDataTool')
        self.Is = Is
        self.Ir = Ir
        # angle_rotor can be None, a ndarray or a list
        set_array(self, "angle_rotor", angle_rotor)
        self.N0 = N0
        self.rot_dir = rot_dir
        self.angle_rotor_initial = angle_rotor_initial
        self.logger_name = logger_name
        self.mmf_unit = mmf_unit
        self.Tem_av_ref = Tem_av_ref
        self.Id_ref = Id_ref
        self.Iq_ref = Iq_ref
        self.felec = felec
        self.Ud_ref = Ud_ref
        self.Uq_ref = Uq_ref
        self.Pj_losses = Pj_losses
        self.Pem_av_ref = Pem_av_ref
        self.Us = Us

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutElec_str = ""
        if self.parent is None:
            OutElec_str += "parent = None " + linesep
        else:
            OutElec_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutElec_str += "time = " + linesep + str(self.time).replace(linesep, linesep + "\t") + linesep + linesep
        OutElec_str += "angle = " + linesep + str(self.angle).replace(linesep, linesep + "\t") + linesep + linesep
        OutElec_str += "Is = "+ str(self.Is) + linesep + linesep
        OutElec_str += "Ir = "+ str(self.Ir) + linesep + linesep
        OutElec_str += "angle_rotor = " + linesep + str(self.angle_rotor).replace(linesep, linesep + "\t") + linesep + linesep
        OutElec_str += "N0 = " + str(self.N0) + linesep
        OutElec_str += "rot_dir = " + str(self.rot_dir) + linesep
        OutElec_str += "angle_rotor_initial = " + str(self.angle_rotor_initial) + linesep
        OutElec_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        OutElec_str += "mmf_unit = "+ str(self.mmf_unit) + linesep + linesep
        OutElec_str += "Tem_av_ref = " + str(self.Tem_av_ref) + linesep
        OutElec_str += "Id_ref = " + str(self.Id_ref) + linesep
        OutElec_str += "Iq_ref = " + str(self.Iq_ref) + linesep
        OutElec_str += "felec = " + str(self.felec) + linesep
        OutElec_str += "Ud_ref = " + str(self.Ud_ref) + linesep
        OutElec_str += "Uq_ref = " + str(self.Uq_ref) + linesep
        OutElec_str += "Pj_losses = " + str(self.Pj_losses) + linesep
        OutElec_str += "Pem_av_ref = " + str(self.Pem_av_ref) + linesep
        OutElec_str += "Us = "+ str(self.Us) + linesep + linesep
        return OutElec_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if not array_equal(other.time, self.time):
            return False
        if not array_equal(other.angle, self.angle):
            return False
        if other.Is != self.Is:
            return False
        if other.Ir != self.Ir:
            return False
        if not array_equal(other.angle_rotor, self.angle_rotor):
            return False
        if other.N0 != self.N0:
            return False
        if other.rot_dir != self.rot_dir:
            return False
        if other.angle_rotor_initial != self.angle_rotor_initial:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.mmf_unit != self.mmf_unit:
            return False
        if other.Tem_av_ref != self.Tem_av_ref:
            return False
        if other.Id_ref != self.Id_ref:
            return False
        if other.Iq_ref != self.Iq_ref:
            return False
        if other.felec != self.felec:
            return False
        if other.Ud_ref != self.Ud_ref:
            return False
        if other.Uq_ref != self.Uq_ref:
            return False
        if other.Pj_losses != self.Pj_losses:
            return False
        if other.Pem_av_ref != self.Pem_av_ref:
            return False
        if other.Us != self.Us:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OutElec_dict = dict()
        if self.time is None:
            OutElec_dict["time"] = None
        else:
            OutElec_dict["time"] = self.time.tolist()
        if self.angle is None:
            OutElec_dict["angle"] = None
        else:
            OutElec_dict["angle"] = self.angle.tolist()
        if self.Is is None:
            OutElec_dict["Is"] = None
        else: # Store serialized data (using cloudpickle) and str to read it in json save files
            OutElec_dict['Is'] ={"__class__" : str(type(self._Is)),"__repr__":str(self._Is.__repr__()),"serialized":dumps(self._Is).decode('ISO-8859-2')}
        if self.Ir is None:
            OutElec_dict["Ir"] = None
        else: # Store serialized data (using cloudpickle) and str to read it in json save files
            OutElec_dict['Ir'] ={"__class__" : str(type(self._Ir)),"__repr__":str(self._Ir.__repr__()),"serialized":dumps(self._Ir).decode('ISO-8859-2')}
        if self.angle_rotor is None:
            OutElec_dict["angle_rotor"] = None
        else:
            OutElec_dict["angle_rotor"] = self.angle_rotor.tolist()
        OutElec_dict["N0"] = self.N0
        OutElec_dict["rot_dir"] = self.rot_dir
        OutElec_dict["angle_rotor_initial"] = self.angle_rotor_initial
        OutElec_dict["logger_name"] = self.logger_name
        if self.mmf_unit is None:
            OutElec_dict["mmf_unit"] = None
        else: # Store serialized data (using cloudpickle) and str to read it in json save files
            OutElec_dict['mmf_unit'] ={"__class__" : str(type(self._mmf_unit)),"__repr__":str(self._mmf_unit.__repr__()),"serialized":dumps(self._mmf_unit).decode('ISO-8859-2')}
        OutElec_dict["Tem_av_ref"] = self.Tem_av_ref
        OutElec_dict["Id_ref"] = self.Id_ref
        OutElec_dict["Iq_ref"] = self.Iq_ref
        OutElec_dict["felec"] = self.felec
        OutElec_dict["Ud_ref"] = self.Ud_ref
        OutElec_dict["Uq_ref"] = self.Uq_ref
        OutElec_dict["Pj_losses"] = self.Pj_losses
        OutElec_dict["Pem_av_ref"] = self.Pem_av_ref
        if self.Us is None:
            OutElec_dict["Us"] = None
        else: # Store serialized data (using cloudpickle) and str to read it in json save files
            OutElec_dict['Us'] ={"__class__" : str(type(self._Us)),"__repr__":str(self._Us.__repr__()),"serialized":dumps(self._Us).decode('ISO-8859-2')}
        # The class name is added to the dict fordeserialisation purpose
        OutElec_dict["__class__"] = "OutElec"
        return OutElec_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.time = None
        self.angle = None
        self.Is = None
        self.Ir = None
        self.angle_rotor = None
        self.N0 = None
        self.rot_dir = None
        self.angle_rotor_initial = None
        self.logger_name = None
        self.mmf_unit = None
        self.Tem_av_ref = None
        self.Id_ref = None
        self.Iq_ref = None
        self.felec = None
        self.Ud_ref = None
        self.Uq_ref = None
        self.Pj_losses = None
        self.Pem_av_ref = None
        self.Us = None

    def _get_time(self):
        """getter of time"""
        return self._time

    def _set_time(self, value):
        """setter of time"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("time", value, "ndarray")
        self._time = value

    time = property(
        fget=_get_time,
        fset=_set_time,
        doc=u"""Electrical time vector (no symmetry)

        :Type: ndarray
        """,
    )

    def _get_angle(self):
        """getter of angle"""
        return self._angle

    def _set_angle(self, value):
        """setter of angle"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("angle", value, "ndarray")
        self._angle = value

    angle = property(
        fget=_get_angle,
        fset=_set_angle,
        doc=u"""Electrical position vector (no symmetry)

        :Type: ndarray
        """,
    )

    def _get_Is(self):
        """getter of Is"""
        return self._Is

    def _set_Is(self, value):
        """setter of Is"""
        try: # Check the type 
            check_var("Is", value, "dict")
        except CheckTypeError:
            check_var("Is", value, "SciDataTool.Classes.DataND.DataND")
            # property can be set from a list to handle loads
        if type(value) == dict: # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]
            self._Is = loads(value["serialized"].encode('ISO-8859-2'))
        else: 
            self._Is= value 
    Is = property(
        fget=_get_Is,
        fset=_set_Is,
        doc=u"""Stator currents as a function of time (each column correspond to one phase)

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_Ir(self):
        """getter of Ir"""
        return self._Ir

    def _set_Ir(self, value):
        """setter of Ir"""
        try: # Check the type 
            check_var("Ir", value, "dict")
        except CheckTypeError:
            check_var("Ir", value, "SciDataTool.Classes.DataND.DataND")
            # property can be set from a list to handle loads
        if type(value) == dict: # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]
            self._Ir = loads(value["serialized"].encode('ISO-8859-2'))
        else: 
            self._Ir= value 
    Ir = property(
        fget=_get_Ir,
        fset=_set_Ir,
        doc=u"""Rotor currents as a function of time (each column correspond to one phase)

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )

    def _get_angle_rotor(self):
        """getter of angle_rotor"""
        return self._angle_rotor

    def _set_angle_rotor(self, value):
        """setter of angle_rotor"""
        if value is None:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("angle_rotor", value, "ndarray")
        self._angle_rotor = value

    angle_rotor = property(
        fget=_get_angle_rotor,
        fset=_set_angle_rotor,
        doc=u"""Rotor angular position as a function of time (if None computed according to Nr)

        :Type: ndarray
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

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use

        :Type: str
        """,
    )

    def _get_mmf_unit(self):
        """getter of mmf_unit"""
        return self._mmf_unit

    def _set_mmf_unit(self, value):
        """setter of mmf_unit"""
        try: # Check the type 
            check_var("mmf_unit", value, "dict")
        except CheckTypeError:
            check_var("mmf_unit", value, "SciDataTool.Classes.DataND.DataND")
            # property can be set from a list to handle loads
        if type(value) == dict: # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]
            self._mmf_unit = loads(value["serialized"].encode('ISO-8859-2'))
        else: 
            self._mmf_unit= value 
    mmf_unit = property(
        fget=_get_mmf_unit,
        fset=_set_mmf_unit,
        doc=u"""Unit magnetomotive force

        :Type: SciDataTool.Classes.DataND.DataND
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

    def _get_felec(self):
        """getter of felec"""
        return self._felec

    def _set_felec(self, value):
        """setter of felec"""
        check_var("felec", value, "float")
        self._felec = value

    felec = property(
        fget=_get_felec,
        fset=_set_felec,
        doc=u"""Electrical Frequency

        :Type: float
        """,
    )

    def _get_Ud_ref(self):
        """getter of Ud_ref"""
        return self._Ud_ref

    def _set_Ud_ref(self, value):
        """setter of Ud_ref"""
        check_var("Ud_ref", value, "float")
        self._Ud_ref = value

    Ud_ref = property(
        fget=_get_Ud_ref,
        fset=_set_Ud_ref,
        doc=u"""d-axis voltage magnitude

        :Type: float
        """,
    )

    def _get_Uq_ref(self):
        """getter of Uq_ref"""
        return self._Uq_ref

    def _set_Uq_ref(self, value):
        """setter of Uq_ref"""
        check_var("Uq_ref", value, "float")
        self._Uq_ref = value

    Uq_ref = property(
        fget=_get_Uq_ref,
        fset=_set_Uq_ref,
        doc=u"""q-axis voltage magnitude

        :Type: float
        """,
    )

    def _get_Pj_losses(self):
        """getter of Pj_losses"""
        return self._Pj_losses

    def _set_Pj_losses(self, value):
        """setter of Pj_losses"""
        check_var("Pj_losses", value, "float")
        self._Pj_losses = value

    Pj_losses = property(
        fget=_get_Pj_losses,
        fset=_set_Pj_losses,
        doc=u"""Electrical Joule losses

        :Type: float
        """,
    )

    def _get_Pem_av_ref(self):
        """getter of Pem_av_ref"""
        return self._Pem_av_ref

    def _set_Pem_av_ref(self, value):
        """setter of Pem_av_ref"""
        check_var("Pem_av_ref", value, "float")
        self._Pem_av_ref = value

    Pem_av_ref = property(
        fget=_get_Pem_av_ref,
        fset=_set_Pem_av_ref,
        doc=u"""Average Electromagnetic power

        :Type: float
        """,
    )

    def _get_Us(self):
        """getter of Us"""
        return self._Us

    def _set_Us(self, value):
        """setter of Us"""
        try: # Check the type 
            check_var("Us", value, "dict")
        except CheckTypeError:
            check_var("Us", value, "SciDataTool.Classes.DataND.DataND")
            # property can be set from a list to handle loads
        if type(value) == dict: # Load type from saved dict {"type":type(value),"str": str(value),"serialized": serialized(value)]
            self._Us = loads(value["serialized"].encode('ISO-8859-2'))
        else: 
            self._Us= value 
    Us = property(
        fget=_get_Us,
        fset=_set_Us,
        doc=u"""Stator voltage as a function of time (each column correspond to one phase)

        :Type: SciDataTool.Classes.DataND.DataND
        """,
    )
