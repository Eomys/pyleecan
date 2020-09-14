# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutLoss.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutLoss
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.OutLoss.get_loss import get_loss
except ImportError as error:
    get_loss = error


from ._check import InitUnKnowClassError
from .MeshSolution import MeshSolution


class OutLoss(FrozenClass):
    """Gather the loss module outputs"""

    VERSION = 1

    # cf Methods.Output.OutLoss.get_loss
    if isinstance(get_loss, ImportError):
        get_loss = property(
            fget=lambda x: raise_(
                ImportError("Can't use OutLoss method get_loss: " + str(get_loss))
            )
        )
    else:
        get_loss = get_loss
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
        losses=[],
        meshsolution=-1,
        logger_name="Pyleecan.OutLoss",
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

        if meshsolution == -1:
            meshsolution = MeshSolution()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            losses = obj.losses
            meshsolution = obj.meshsolution
            logger_name = obj.logger_name
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "losses" in list(init_dict.keys()):
                losses = init_dict["losses"]
            if "meshsolution" in list(init_dict.keys()):
                meshsolution = init_dict["meshsolution"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Initialisation by argument
        self.parent = None
        if losses == -1:
            losses = []
        self.losses = losses
        # meshsolution can be None, a MeshSolution object or a dict
        if isinstance(meshsolution, dict):
            self.meshsolution = MeshSolution(init_dict=meshsolution)
        elif isinstance(meshsolution, str):
            from ..Functions.load import load

            self.meshsolution = load(meshsolution)
        else:
            self.meshsolution = meshsolution
        self.logger_name = logger_name

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutLoss_str = ""
        if self.parent is None:
            OutLoss_str += "parent = None " + linesep
        else:
            OutLoss_str += "parent = " + str(type(self.parent)) + " object" + linesep
        OutLoss_str += (
            "losses = "
            + linesep
            + str(self.losses).replace(linesep, linesep + "\t")
            + linesep
        )
        if self.meshsolution is not None:
            tmp = (
                self.meshsolution.__str__()
                .replace(linesep, linesep + "\t")
                .rstrip("\t")
            )
            OutLoss_str += "meshsolution = " + tmp
        else:
            OutLoss_str += "meshsolution = None" + linesep + linesep
        OutLoss_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        return OutLoss_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.losses != self.losses:
            return False
        if other.meshsolution != self.meshsolution:
            return False
        if other.logger_name != self.logger_name:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OutLoss_dict = dict()
        OutLoss_dict["losses"] = self.losses
        if self.meshsolution is None:
            OutLoss_dict["meshsolution"] = None
        else:
            OutLoss_dict["meshsolution"] = self.meshsolution.as_dict()
        OutLoss_dict["logger_name"] = self.logger_name
        # The class name is added to the dict fordeserialisation purpose
        OutLoss_dict["__class__"] = "OutLoss"
        return OutLoss_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.losses = None
        if self.meshsolution is not None:
            self.meshsolution._set_None()
        self.logger_name = None

    def _get_losses(self):
        """getter of losses"""
        return self._losses

    def _set_losses(self, value):
        """setter of losses"""
        check_var("losses", value, "list")
        self._losses = value

    losses = property(
        fget=_get_losses,
        fset=_set_losses,
        doc=u"""List of the computed losses of SciDataTool's DataND type

        :Type: list
        """,
    )

    def _get_meshsolution(self):
        """getter of meshsolution"""
        return self._meshsolution

    def _set_meshsolution(self, value):
        """setter of meshsolution"""
        check_var("meshsolution", value, "MeshSolution")
        self._meshsolution = value

        if self._meshsolution is not None:
            self._meshsolution.parent = self

    meshsolution = property(
        fget=_get_meshsolution,
        fset=_set_meshsolution,
        doc=u"""FEA software mesh and post processing results

        :Type: MeshSolution
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
