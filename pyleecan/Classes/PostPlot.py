# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Post/PostPlot.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Post/PostPlot
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .PostMethod import PostMethod

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Post.PostPlot.run import run
except ImportError as error:
    run = error


from ._check import InitUnKnowClassError


class PostPlot(PostMethod):
    """Post-processing to do a plot which is a method of Output or other class if attribute is not None"""

    VERSION = 1

    # cf Methods.Post.PostPlot.run
    if isinstance(run, ImportError):
        run = property(
            fget=lambda x: raise_(
                ImportError("Can't use PostPlot method run: " + str(run))
            )
        )
    else:
        run = run
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        module_plot=None,
        attribute=None,
        parameters=None,
        plot_name=None,
        is_show_plot=True,
        save_format="png",
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "module_plot" in list(init_dict.keys()):
                module_plot = init_dict["module_plot"]
            if "attribute" in list(init_dict.keys()):
                attribute = init_dict["attribute"]
            if "parameters" in list(init_dict.keys()):
                parameters = init_dict["parameters"]
            if "plot_name" in list(init_dict.keys()):
                plot_name = init_dict["plot_name"]
            if "is_show_plot" in list(init_dict.keys()):
                is_show_plot = init_dict["is_show_plot"]
            if "save_format" in list(init_dict.keys()):
                save_format = init_dict["save_format"]
        # Set the properties (value check and convertion are done in setter)
        self.module_plot = module_plot
        self.attribute = attribute
        self.parameters = parameters
        self.plot_name = plot_name
        self.is_show_plot = is_show_plot
        self.save_format = save_format
        # Call PostMethod init
        super(PostPlot, self).__init__()
        # The class is frozen (in PostMethod init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        PostPlot_str = ""
        # Get the properties inherited from PostMethod
        PostPlot_str += super(PostPlot, self).__str__()
        PostPlot_str += 'module_plot = "' + str(self.module_plot) + '"' + linesep
        PostPlot_str += 'attribute = "' + str(self.attribute) + '"' + linesep
        PostPlot_str += "parameters = " + str(self.parameters) + linesep
        PostPlot_str += 'plot_name = "' + str(self.plot_name) + '"' + linesep
        PostPlot_str += "is_show_plot = " + str(self.is_show_plot) + linesep
        PostPlot_str += 'save_format = "' + str(self.save_format) + '"' + linesep
        return PostPlot_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from PostMethod
        if not super(PostPlot, self).__eq__(other):
            return False
        if other.module_plot != self.module_plot:
            return False
        if other.attribute != self.attribute:
            return False
        if other.parameters != self.parameters:
            return False
        if other.plot_name != self.plot_name:
            return False
        if other.is_show_plot != self.is_show_plot:
            return False
        if other.save_format != self.save_format:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from PostMethod
        PostPlot_dict = super(PostPlot, self).as_dict()
        PostPlot_dict["module_plot"] = self.module_plot
        PostPlot_dict["attribute"] = self.attribute
        PostPlot_dict["parameters"] = (
            self.parameters.copy() if self.parameters is not None else None
        )
        PostPlot_dict["plot_name"] = self.plot_name
        PostPlot_dict["is_show_plot"] = self.is_show_plot
        PostPlot_dict["save_format"] = self.save_format
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        PostPlot_dict["__class__"] = "PostPlot"
        return PostPlot_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.module_plot = None
        self.attribute = None
        self.parameters = None
        self.plot_name = None
        self.is_show_plot = None
        self.save_format = None
        # Set to None the properties inherited from PostMethod
        super(PostPlot, self)._set_None()

    def _get_module_plot(self):
        """getter of module_plot"""
        return self._module_plot

    def _set_module_plot(self, value):
        """setter of module_plot"""
        check_var("module_plot", value, "str")
        self._module_plot = value

    module_plot = property(
        fget=_get_module_plot,
        fset=_set_module_plot,
        doc=u"""Name of the plot method of the Output to call

        :Type: str
        """,
    )

    def _get_attribute(self):
        """getter of attribute"""
        return self._attribute

    def _set_attribute(self, value):
        """setter of attribute"""
        check_var("attribute", value, "str")
        self._attribute = value

    attribute = property(
        fget=_get_attribute,
        fset=_set_attribute,
        doc=u"""Attribute to add to Output to reach the plot given by module_plot

        :Type: str
        """,
    )

    def _get_parameters(self):
        """getter of parameters"""
        return self._parameters

    def _set_parameters(self, value):
        """setter of parameters"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("parameters", value, "dict")
        self._parameters = value

    parameters = property(
        fget=_get_parameters,
        fset=_set_parameters,
        doc=u"""Dictionnary of parameters to pass the plot method

        :Type: dict
        """,
    )

    def _get_plot_name(self):
        """getter of plot_name"""
        return self._plot_name

    def _set_plot_name(self, value):
        """setter of plot_name"""
        check_var("plot_name", value, "str")
        self._plot_name = value

    plot_name = property(
        fget=_get_plot_name,
        fset=_set_plot_name,
        doc=u"""Name of the plot

        :Type: str
        """,
    )

    def _get_is_show_plot(self):
        """getter of is_show_plot"""
        return self._is_show_plot

    def _set_is_show_plot(self, value):
        """setter of is_show_plot"""
        check_var("is_show_plot", value, "bool")
        self._is_show_plot = value

    is_show_plot = property(
        fget=_get_is_show_plot,
        fset=_set_is_show_plot,
        doc=u"""True to show the figure after plotting

        :Type: bool
        """,
    )

    def _get_save_format(self):
        """getter of save_format"""
        return self._save_format

    def _set_save_format(self, value):
        """setter of save_format"""
        check_var("save_format", value, "str")
        self._save_format = value

    save_format = property(
        fget=_get_save_format,
        fset=_set_save_format,
        doc=u"""File format extension ("png", "svg", "eps") in which to save the figure

        :Type: str
        """,
    )
