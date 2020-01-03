# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Output/OutputMultiOpti.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.OutputMulti import OutputMulti

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Output import Output


class OutputMultiOpti(OutputMulti):
    """Optimization results"""


    # save method is available in all object
    save = save

    def __init__(self, fitness=[], const_vel=[], output_ref=-1, outputs=list(), is_valid=[], init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if output_ref == -1:
            output_ref = Output()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["fitness", "const_vel", "output_ref", "outputs", "is_valid"])
            # Overwrite default value with init_dict content
            if "fitness" in list(init_dict.keys()):
                fitness = init_dict["fitness"]
            if "const_vel" in list(init_dict.keys()):
                const_vel = init_dict["const_vel"]
            if "output_ref" in list(init_dict.keys()):
                output_ref = init_dict["output_ref"]
            if "outputs" in list(init_dict.keys()):
                outputs = init_dict["outputs"]
            if "is_valid" in list(init_dict.keys()):
                is_valid = init_dict["is_valid"]
        # Initialisation by argument
        self.fitness = fitness
        self.const_vel = const_vel
        # Call OutputMulti init
        super(OutputMultiOpti, self).__init__(output_ref=output_ref, outputs=outputs, is_valid=is_valid)
        # The class is frozen (in OutputMulti init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutputMultiOpti_str = ""
        # Get the properties inherited from OutputMulti
        OutputMultiOpti_str += super(OutputMultiOpti, self).__str__() + linesep
        OutputMultiOpti_str += "fitness = " + linesep + str(self.fitness) + linesep
        OutputMultiOpti_str += "const_vel = " + linesep + str(self.const_vel)
        return OutputMultiOpti_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OutputMulti
        if not super(OutputMultiOpti, self).__eq__(other):
            return False
        if other.fitness != self.fitness:
            return False
        if other.const_vel != self.const_vel:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from OutputMulti
        OutputMultiOpti_dict = super(OutputMultiOpti, self).as_dict()
        OutputMultiOpti_dict["fitness"] = self.fitness
        OutputMultiOpti_dict["const_vel"] = self.const_vel
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        OutputMultiOpti_dict["__class__"] = "OutputMultiOpti"
        return OutputMultiOpti_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.fitness = None
        self.const_vel = None
        # Set to None the properties inherited from OutputMulti
        super(OutputMultiOpti, self)._set_None()

    def _get_fitness(self):
        """getter of fitness"""
        return self._fitness

    def _set_fitness(self, value):
        """setter of fitness"""
        check_var("fitness", value, "list")
        self._fitness = value

    # List of the corresponding output objective values
    # Type : list
    fitness = property(
        fget=_get_fitness,
        fset=_set_fitness,
        doc=u"""List of the corresponding output objective values""",
    )

    def _get_const_vel(self):
        """getter of const_vel"""
        return self._const_vel

    def _set_const_vel(self, value):
        """setter of const_vel"""
        check_var("const_vel", value, "list")
        self._const_vel = value

    # List of the corresponding output constraint values
    # Type : list
    const_vel = property(
        fget=_get_const_vel,
        fset=_set_const_vel,
        doc=u"""List of the corresponding output constraint values""",
    )
