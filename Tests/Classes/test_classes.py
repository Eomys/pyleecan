# -*- coding: utf-8 -*-

from os.path import join

from importlib import import_module
from unittest import TestCase
from ddt import ddt, data
from numpy import array_equal, empty, array
from pyleecan.Generator.read_fct import read_all
from pyleecan.Generator.class_generator import get_mother_attr
from pyleecan.Generator import DOC_DIR
from pyleecan.Tests.find import (
    find_test_value,
    is_type_list,
    is_type_dict,
    MissingTypeError,
    PYTHON_TYPE,
)

from pyleecan.Classes.check import CheckMinError, CheckTypeError, CheckMaxError
from pyleecan.Classes.check import NotADictError
from pyleecan.Classes.frozen import FrozenClass, FrozenError

# Get the dict of all the classes and their information
gen_dict = read_all(DOC_DIR)  # dict of class dict
# Remove one list level (packages Machine, Simulation, Material...)
class_list = list(gen_dict.values())
from pyleecan.Classes.import_all import *


@ddt
class test_all_Classes(TestCase):
    """This test check that all the classes matches the current documentation
    It makes sure that the class generator works and was run
    """

    @data(*class_list)
    def test_class_init_default(self, class_dict):
        """Check if every propeties in the doc is created
        by __init__ with the default value"""
        # Import and init the class
        # module = import_module(
        #     "pyleecan.Classes." + class_dict["package"] + "." + class_dict["name"]
        # )
        # class_to_test = getattr(module, class_dict["name"])

        test_obj = eval(class_dict["name"] + "()")

        # Get the property to test
        prop_list = get_mother_attr(gen_dict, class_dict, "properties")[0]
        for prop in prop_list:
            type_name = prop["type"]
            result = test_obj.__getattribute__(prop["name"])
            if prop["value"] == "None":
                prop["value"] = None
            if type_name in PYTHON_TYPE:
                self.assertEqual(
                    result,
                    prop["value"],
                    msg="Error for class "
                    + class_dict["name"]
                    + " for property: "
                    + prop["name"],
                )
            elif type_name == "dict":
                # Default value is empty dict
                if prop["value"] == "":
                    value = {}
                else:
                    value = prop["value"]
                self.assertEqual(
                    result,
                    value,
                    msg="Error for class "
                    + class_dict["name"]
                    + " for property: "
                    + prop["name"],
                )
            elif is_type_list(type_name):  # List of pyleecan type
                self.assertEqual(
                    result,
                    list(),
                    msg="Error for class "
                    + class_dict["name"]
                    + " for property: "
                    + prop["name"],
                )
            elif is_type_dict(type_name):  # Dict of pyleecan type
                self.assertEqual(
                    result,
                    dict(),
                    msg="Error for class "
                    + class_dict["name"]
                    + " for property: "
                    + prop["name"],
                )
            elif type_name == "ndarray":
                if type(prop["value"]) is list:
                    expect = array(prop["value"])
                else:
                    expect = empty(0)
                self.assertTrue(
                    array_equal(result, expect),
                    msg="Error for class "
                    + class_dict["name"]
                    + " for property: "
                    + prop["name"],
                )
            elif prop["value"] != "":
                self.assertEqual(
                    result,
                    prop["value"],
                    msg="Error for class "
                    + class_dict["name"]
                    + " for property: "
                    + prop["name"],
                )
            else:  # pyleecan type
                self.assertEqual(
                    result,
                    eval(type_name + "()"),
                    msg="Error for class "
                    + class_dict["name"]
                    + " for property: "
                    + prop["name"],
                )

    @data(*class_list)
    def test_class_as_dict(self, class_dict):
        """Check if as_dict return the correct dict"""
        # Setup
        d = dict()
        prop_list = get_mother_attr(gen_dict, class_dict, "properties")[0]
        # Generated the expected result dict
        for prop in prop_list:
            if prop["type"] == "ndarray":
                if type(prop["value"]) is list:
                    d[prop["name"]] = prop["value"]
                else:
                    d[prop["name"]] = list()
            elif prop["value"] in ["None", None]:
                d[prop["name"]] = None
            elif prop["type"] in PYTHON_TYPE:
                d[prop["name"]] = prop["value"]
            elif prop["type"] == "dict":
                d[prop["name"]] = {}
            elif is_type_list(prop["type"]):  # List of pyleecan type
                d[prop["name"]] = list()
            elif is_type_dict(prop["type"]):  # Dict of pyleecan type
                d[prop["name"]] = dict()
            else:  # pyleecan type
                d[prop["name"]] = eval(prop["type"] + "().as_dict()")
        d["__class__"] = class_dict["name"]

        test_obj = eval(class_dict["name"] + "()")
        # Test
        result_dict = test_obj.as_dict()
        for key in result_dict:
            self.assertEqual(
                d[key],
                result_dict[key],
                msg="Error for class "
                + class_dict["name"]
                + " for property: "
                + key
                + ", expected: "
                + str(d[key])
                + ", returned: "
                + str(result_dict[key]),
            )
        self.assertEqual(d.keys(), result_dict.keys())

    @data(*class_list)
    def test_class_set_None(self, class_dict):
        """Check that _set_None set to None every non pyleecantype properties
        """

        test_obj = eval(class_dict["name"] + "()")
        test_obj._set_None()
        prop_list = get_mother_attr(gen_dict, class_dict, "properties")[0]
        for prop in prop_list:
            if prop["type"] == "ndarray" or prop["type"] in PYTHON_TYPE:
                self.assertIsNone(test_obj.__getattribute__(prop["name"]))

    @data(*class_list)
    def test_class_frozen(self, class_dict):
        """Check if the class is frozen after __init__"""
        test_obj = eval(class_dict["name"] + "()")
        with self.assertRaises(FrozenError):
            test_obj.UnKnow_Property_For_Frozen_Test = 10

    @data(*class_list)
    def test_class_inherit(self, class_dict):
        """Check if the class inherit of its mother class"""
        if class_dict["mother"] != "":
            self.assertTrue(
                eval(
                    "issubclass("
                    + class_dict["name"]
                    + ", "
                    + class_dict["mother"]
                    + ")"
                )
            )
        else:
            self.assertTrue(eval("issubclass(" + class_dict["name"] + ", FrozenClass)"))

    @data(*class_list)
    def test_class_methods(self, class_dict):
        """Check if the class has all its methods"""
        meth_list = get_mother_attr(gen_dict, class_dict, "methods")[0]
        for meth in meth_list:
            meth = meth.split(".")[-1]  # Get the methods name if in a folder
            self.assertTrue(
                eval("hasattr(" + class_dict["name"] + ", '" + meth + "')"),
                msg=class_dict["name"] + " has no method: " + meth,
            )

    @data(*class_list)
    def test_class_type_float(self, class_dict):
        """Check if the setter is type sensitive for float"""
        test_obj = eval(class_dict["name"] + "()")

        prop_list = get_mother_attr(gen_dict, class_dict, "properties")[0]
        for prop in prop_list:
            value = find_test_value(prop, "float")
            # Check the doc to know if it should raise an error or not
            if prop["type"] in ["float", "complex"]:
                # No error expected
                test_obj.__setattr__(prop["name"], value)
                self.assertEqual(test_obj.__getattribute__(prop["name"]), value)
            else:
                # CheckTypeError expected
                with self.assertRaises(CheckTypeError):
                    test_obj.__setattr__(prop["name"], value)

    @data(*class_list)
    def test_class_min(self, class_dict):
        """Check if the setter respect the specified min"""
        # Setup
        test_obj = eval(class_dict["name"] + "()")

        prop_list = get_mother_attr(gen_dict, class_dict, "properties")[0]
        for prop in prop_list:
            if prop["min"] != "" and prop["type"] in ["float", "int"]:
                min_val = eval(prop["type"] + "(" + str(prop["min"]) + ")")
                # Test Ok
                test_obj.__setattr__(prop["name"], min_val)
                self.assertEqual(
                    test_obj.__getattribute__(prop["name"]),
                    min_val,
                    msg="Error for class "
                    + class_dict["name"]
                    + " for property: "
                    + prop["name"],
                )
                # Test Fail
                with self.assertRaises(CheckMinError):
                    test_obj.__setattr__(prop["name"], min_val - 1)

    @data(*class_list)
    def test_class_max(self, class_dict):
        """Check if the setter respect the specified max"""
        # Setup
        test_obj = eval(class_dict["name"] + "()")

        prop_list = get_mother_attr(gen_dict, class_dict, "properties")[0]
        for prop in prop_list:
            if prop["max"] != "" and prop["type"] in ["float", "int"]:
                max_val = eval(prop["type"] + "(" + str(prop["max"]) + ")")
                # Test Ok
                test_obj.__setattr__(prop["name"], max_val)
                self.assertEqual(
                    test_obj.__getattribute__(prop["name"]),
                    max_val,
                    msg="Error for class "
                    + class_dict["name"]
                    + " for property: "
                    + prop["name"],
                )
                # Test Fail
                with self.assertRaises(CheckMaxError):
                    test_obj.__setattr__(prop["name"], max_val + 1)

    @data(*class_list)
    def test_class_prop_doc(self, class_dict):
        """Check if the property's doc is the same as in the doc file
        Works with multiline doc and specifics caracters"""

        prop_list = get_mother_attr(gen_dict, class_dict, "properties")[0]
        for prop in prop_list:
            result = eval(
                "getattr("
                + class_dict["name"]
                + ", '"
                + prop["name"]
                + "').__doc__.splitlines()"
            )
            self.assertEqual(result, prop["desc"].split("\\n"))
