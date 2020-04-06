# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Output/OutputMulti.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from pyleecan.Classes._check import check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Output.OutputMulti.add_output import add_output
except ImportError as error:
    add_output = error


from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.Output import Output


class OutputMulti(FrozenClass):


    # cf Methods.Output.OutputMulti.add_output
    if isinstance(add_output, ImportError):
        add_output = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use OutputMulti method add_output: " + str(add_output)
                )
            )
        )
    else:
        add_output = add_output
    # save method is available in all object
    save = save

    def __init__(self, output_ref=-1, outputs=list(), is_valid=[], design_var=[], design_var_names=[], init_dict=None):
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
            assert(type(init_dict) is dict)
            # Overwrite default value with init_dict content
            if "output_ref" in list(init_dict.keys()):
                output_ref = init_dict["output_ref"]
            if "outputs" in list(init_dict.keys()):
                outputs = init_dict["outputs"]
            if "is_valid" in list(init_dict.keys()):
                is_valid = init_dict["is_valid"]
            if "design_var" in list(init_dict.keys()):
                design_var = init_dict["design_var"]
            if "design_var_names" in list(init_dict.keys()):
                design_var_names = init_dict["design_var_names"]
        # Initialisation by argument
        self.parent = None
        # output_ref can be None, a Output object or a dict
        if isinstance(output_ref, dict):
            self.output_ref = Output(init_dict=output_ref)
        else:
            self.output_ref = output_ref
        # outputs can be None or a list of Output object
        self.outputs = list()
        if type(outputs) is list:
            for obj in outputs:
                if obj is None:  # Default value
                    self.outputs.append(Output())
                elif isinstance(obj, dict):
                    self.outputs.append(Output(init_dict=obj))
                else:
                    self.outputs.append(obj)
        elif outputs is None:
            self.outputs = list()
        else:
            self.outputs = outputs
        self.is_valid = is_valid
        self.design_var = design_var
        self.design_var_names = design_var_names

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        OutputMulti_str = ""
        if self.parent is None:
            OutputMulti_str += "parent = None " + linesep
        else:
            OutputMulti_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.output_ref is not None:
            tmp = self.output_ref.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OutputMulti_str += "output_ref = "+ tmp
        else:
            OutputMulti_str += "output_ref = None" + linesep + linesep
        if len(self.outputs) == 0:
            OutputMulti_str += "outputs = []" + linesep
        for ii in range(len(self.outputs)):
            tmp = self.outputs[ii].__str__().replace(linesep, linesep + "\t") + linesep
            OutputMulti_str += "outputs["+str(ii)+"] ="+ tmp + linesep + linesep
        OutputMulti_str += "is_valid = " + linesep + str(self.is_valid).replace(linesep, linesep + "\t") + linesep
        OutputMulti_str += "design_var = " + linesep + str(self.design_var).replace(linesep, linesep + "\t") + linesep
        OutputMulti_str += "design_var_names = " + linesep + str(self.design_var_names).replace(linesep, linesep + "\t") + linesep
        return OutputMulti_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.output_ref != self.output_ref:
            return False
        if other.outputs != self.outputs:
            return False
        if other.is_valid != self.is_valid:
            return False
        if other.design_var != self.design_var:
            return False
        if other.design_var_names != self.design_var_names:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        OutputMulti_dict = dict()
        if self.output_ref is None:
            OutputMulti_dict["output_ref"] = None
        else:
            OutputMulti_dict["output_ref"] = self.output_ref.as_dict()
        OutputMulti_dict["outputs"] = list()
        for obj in self.outputs:
            OutputMulti_dict["outputs"].append(obj.as_dict())
        OutputMulti_dict["is_valid"] = self.is_valid
        OutputMulti_dict["design_var"] = self.design_var
        OutputMulti_dict["design_var_names"] = self.design_var_names
        # The class name is added to the dict fordeserialisation purpose
        OutputMulti_dict["__class__"] = "OutputMulti"
        return OutputMulti_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.output_ref is not None:
            self.output_ref._set_None()
        for obj in self.outputs:
            obj._set_None()
        self.is_valid = None
        self.design_var = None
        self.design_var_names = None

    def get_logger(self):
        """getter of the logger"""
        if hasattr(self,'logger_name'):
            return getLogger(self.logger_name)
        elif self.parent != None:
            return self.parent.get_logger()
        else:
            return getLogger('Pyleecan')

    def _get_output_ref(self):
        """getter of output_ref"""
        return self._output_ref

    def _set_output_ref(self, value):
        """setter of output_ref"""
        check_var("output_ref", value, "Output")
        self._output_ref = value

        if self._output_ref is not None:
            self._output_ref.parent = self
    # Reference output of the multi simulation
    # Type : Output
    output_ref = property(
        fget=_get_output_ref, fset=_set_output_ref, doc=u"""Reference output of the multi simulation"""
    )

    def _get_outputs(self):
        """getter of outputs"""
        for obj in self._outputs:
            if obj is not None:
                obj.parent = self
        return self._outputs

    def _set_outputs(self, value):
        """setter of outputs"""
        check_var("outputs", value, "[Output]")
        self._outputs = value

        for obj in self._outputs:
            if obj is not None:
                obj.parent = self

    # list of output from the multi-simulation
    # Type : [Output]
    outputs = property(
        fget=_get_outputs, fset=_set_outputs, doc=u"""list of output from the multi-simulation"""
    )

    def _get_is_valid(self):
        """getter of is_valid"""
        return self._is_valid

    def _set_is_valid(self, value):
        """setter of is_valid"""
        check_var("is_valid", value, "list")
        self._is_valid = value

    # list to indicate if the corresponding output is valid
    # Type : list
    is_valid = property(
        fget=_get_is_valid,
        fset=_set_is_valid,
        doc=u"""list to indicate if the corresponding output is valid""",
    )

    def _get_design_var(self):
        """getter of design_var"""
        return self._design_var

    def _set_design_var(self, value):
        """setter of design_var"""
        check_var("design_var", value, "list")
        self._design_var = value

    # list of design variables corresponding to the output
    # Type : list
    design_var = property(
        fget=_get_design_var,
        fset=_set_design_var,
        doc=u"""list of design variables corresponding to the output""",
    )

    def _get_design_var_names(self):
        """getter of design_var_names"""
        return self._design_var_names

    def _set_design_var_names(self, value):
        """setter of design_var_names"""
        check_var("design_var_names", value, "list")
        self._design_var_names = value

    # list of str containing the design variables names sorted alphabetically
    # Type : list
    design_var_names = property(
        fget=_get_design_var_names,
        fset=_set_design_var_names,
        doc=u"""list of str containing the design variables names sorted alphabetically""",
    )
