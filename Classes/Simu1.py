# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.Simulation import Simulation

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Machine import Machine
from pyleecan.Classes.MachineSync import MachineSync
from pyleecan.Classes.MachineAsync import MachineAsync
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.Classes.MachineSyRM import MachineSyRM
from pyleecan.Classes.Input import Input
from pyleecan.Classes.InCurrent import InCurrent


class Simu1(Simulation):
    """Five sequential weak coupling multi physics simulation"""

    VERSION = 1

    # save method is available in all object
    save = save

    def __init__(self, name="", desc="", machine=-1, input=-1, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if machine == -1:
            machine = Machine()
        if input == -1:
            input = Input()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["name", "desc", "machine", "input"])
            # Overwrite default value with init_dict content
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "machine" in list(init_dict.keys()):
                machine = init_dict["machine"]
            if "input" in list(init_dict.keys()):
                input = init_dict["input"]
        # Initialisation by argument
        # Call Simulation init
        super(Simu1, self).__init__(name=name, desc=desc, machine=machine, input=input)
        # The class is frozen (in Simulation init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Simu1_str = ""
        # Get the properties inherited from Simulation
        Simu1_str += super(Simu1, self).__str__() + linesep
        return Simu1_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Simulation
        if not super(Simu1, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Simulation
        Simu1_dict = super(Simu1, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        Simu1_dict["__class__"] = "Simu1"
        return Simu1_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Simulation
        super(Simu1, self)._set_None()
