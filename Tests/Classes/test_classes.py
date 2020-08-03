# -*- coding: utf-8 -*-

from os.path import join
from os import remove, chdir

import pytest
from importlib import import_module
import matplotlib.pyplot as plt
from numpy import array_equal, empty, array
from pyleecan.Generator.read_fct import read_all
from pyleecan.Generator.ClassGenerator.init_method_generator import get_mother_attr
from pyleecan.definitions import DOC_DIR
from Tests.find import (
    find_test_value,
    is_type_list,
    is_type_dict,
    MissingTypeError,
    PYTHON_TYPE,
)
from Tests import save_path
from pyleecan.Classes._check import CheckMinError, CheckTypeError, CheckMaxError
from pyleecan.Classes._check import NotADictError
from pyleecan.Classes._frozen import FrozenClass, FrozenError

# Get the dict of all the classes and their information
gen_dict = read_all(DOC_DIR)  # dict of class dict
# Remove one list level (packages Machine, Simulation, Material...)
class_list = list(gen_dict.values())

from pyleecan.Classes.import_all import *


"""
This test check that all the classes matches the current documentation
It makes sure that the class generator works and was run
"""


@pytest.mark.parametrize("class_dict", class_list)
def test_class_init_default(class_dict):
    """Check if every propeties in the doc is created
    by __init__ with the default value"""
    # Import and init the class
    # module = import_module(
    #     "...Classes." + class_dict["package"] + "." + class_dict["name"]
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
            assert result == prop["value"], (
                "Error for class "
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
            assert result == value, (
                "Error for class "
                + class_dict["name"]
                + " for property: "
                + prop["name"],
            )
        elif is_type_list(type_name):  # List of pyleecan type
            assert result == list(), (
                "Error for class "
                + class_dict["name"]
                + " for property: "
                + prop["name"],
            )
        elif is_type_dict(type_name):  # Dict of pyleecan type
            assert result == dict(), (
                "Error for class "
                + class_dict["name"]
                + " for property: "
                + prop["name"],
            )
        elif type_name == "ndarray":
            if type(prop["value"]) is list:
                expect = array(prop["value"])
            else:
                expect = empty(0)
            assert array_equal(result, expect), (
                "Error for class "
                + class_dict["name"]
                + " for property: "
                + prop["name"]
            )

        elif type(prop["value"]) is str and "()" in prop["value"]:
            assert result == eval(prop["value"]), (
                "Error for class "
                + class_dict["name"]
                + " for property: "
                + prop["name"],
            )
        elif prop["value"] != "":
            assert result == prop["value"], (
                "Error for class "
                + class_dict["name"]
                + " for property: "
                + prop["name"],
            )
        else:  # pyleecan type
            assert result == eval(type_name + "()"), (
                "Error for class "
                + class_dict["name"]
                + " for property: "
                + prop["name"],
            )


@pytest.mark.parametrize("class_dict", class_list)
def test_class_init_str(class_dict):
    """Check if the class can be initiate from a file"""
    test_obj = eval(class_dict["name"] + "()")

    # Save the object in a file
    chdir(save_path)
    tmp_file = join(save_path, "tmp.json").replace("\\", "/")
    test_obj.save(tmp_file)

    # Initate a second object from the saved file
    test_obj2 = eval(class_dict["name"] + "(init_str='tmp.json')")
    remove(tmp_file)

    # Compare the two objects
    assert test_obj == test_obj2


@pytest.mark.parametrize("class_dict", class_list)
def test_class_as_dict(class_dict):
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
        elif type(prop["value"]) is str and "()" in prop["value"]:
            d[prop["name"]] = eval(prop["value"] + ".as_dict()")
        elif prop["type"] in PYTHON_TYPE:
            d[prop["name"]] = prop["value"]
        elif prop["type"] == "dict":
            if prop["value"] == "":
                d[prop["name"]] = {}
            else:
                d[prop["name"]] = prop["value"]
        elif prop["type"] == "list":
            if prop["value"] == "":
                d[prop["name"]] = []
            else:
                d[prop["name"]] = prop["value"]
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
        assert d[key] == result_dict[key], (
            "Error for class "
            + class_dict["name"]
            + " for property: "
            + key
            + ", expected: "
            + str(d[key])
            + ", returned: "
            + str(result_dict[key]),
        )
    assert d.keys() == result_dict.keys()


@pytest.mark.parametrize("class_dict", class_list)
def test_class_set_None(class_dict):
    """Check that _set_None set to None every non pyleecantype properties
    """

    test_obj = eval(class_dict["name"] + "()")
    test_obj._set_None()
    prop_list = get_mother_attr(gen_dict, class_dict, "properties")[0]
    for prop in prop_list:
        # ndarray set as None are set as array([])
        if prop["type"] == "ndarray":
            assert array_equal(test_obj.__getattribute__(prop["name"]), array([]))
        elif prop["type"] in PYTHON_TYPE:
            assert test_obj.__getattribute__(prop["name"]) == None


@pytest.mark.parametrize("class_dict", class_list)
def test_class_frozen(class_dict):
    """Check if the class is frozen after __init__"""
    test_obj = eval(class_dict["name"] + "()")
    with pytest.raises(FrozenError):
        test_obj.UnKnow_Property_For_Frozen_Test = 10


@pytest.mark.parametrize("class_dict", class_list)
def test_class_inherit(class_dict):
    """Check if the class inherit of its mother class"""
    if class_dict["mother"] != "":
        assert (
            eval("issubclass(" + class_dict["name"] + ", " + class_dict["mother"] + ")")
            == True
        )
    else:
        assert eval("issubclass(" + class_dict["name"] + ", FrozenClass)") == True


@pytest.mark.parametrize("class_dict", class_list)  # [86:87]
def test_class_methods(class_dict):
    """Check if the class has all its methods"""
    test_obj = eval(class_dict["name"] + "()")

    meth_list = get_mother_attr(gen_dict, class_dict, "methods")[0]
    for meth in meth_list:
        meth = meth.split(".")[-1]  # Get the methods name if in a folder

        # Check if the method exists, shouldn't be raised because of the class generator
        assert eval("hasattr(" + class_dict["name"] + ", '" + meth + "')") == True, (
            class_dict["name"] + " has no method: " + meth
        )

        # Check if the methods doesn't raise ImportError
        try:
            eval("test_obj." + meth + "()")
        except ImportError as err:
            raise err  # Raise the ImportError because the method doesn't exist
        except:
            pass

    # Some methods may generate plots
    plt.close("all")


@pytest.mark.parametrize("class_dict", class_list)
def test_class_type_float(class_dict):
    """Check if the setter is type sensitive for float"""
    test_obj = eval(class_dict["name"] + "()")

    prop_list = get_mother_attr(gen_dict, class_dict, "properties")[0]
    for prop in prop_list:
        value = find_test_value(prop, "float")
        # Check the doc to know if it should raise an error or not
        if prop["type"] in ["float", "complex"]:
            # No error expected
            test_obj.__setattr__(prop["name"], value)
            assert test_obj.__getattribute__(prop["name"]) == value
        else:
            # CheckTypeError expected
            with pytest.raises(CheckTypeError):
                test_obj.__setattr__(prop["name"], value)


@pytest.mark.parametrize("class_dict", class_list)
def test_class_min(class_dict):
    """Check if the setter respect the specified min"""
    # Setup
    test_obj = eval(class_dict["name"] + "()")

    prop_list = get_mother_attr(gen_dict, class_dict, "properties")[0]
    for prop in prop_list:
        if prop["min"] != "" and prop["type"] in ["float", "int"]:
            min_val = eval(prop["type"] + "(" + str(prop["min"]) + ")")
            # Test Ok
            test_obj.__setattr__(prop["name"], min_val)
            assert test_obj.__getattribute__(prop["name"]) == min_val, (
                "Error for class "
                + class_dict["name"]
                + " for property: "
                + prop["name"]
            )

            # Test Fail
            with pytest.raises(CheckMinError):
                test_obj.__setattr__(prop["name"], min_val - 1)


@pytest.mark.parametrize("class_dict", class_list)
def test_class_max(class_dict):
    """Check if the setter respect the specified max"""
    # Setup
    test_obj = eval(class_dict["name"] + "()")

    prop_list = get_mother_attr(gen_dict, class_dict, "properties")[0]
    for prop in prop_list:
        if prop["max"] != "" and prop["type"] in ["float", "int"]:
            max_val = eval(prop["type"] + "(" + str(prop["max"]) + ")")
            # Test Ok
            test_obj.__setattr__(prop["name"], max_val)
            assert test_obj.__getattribute__(prop["name"]) == max_val, (
                "Error for class "
                + class_dict["name"]
                + " for property: "
                + prop["name"]
            )

            # Test Fail
            with pytest.raises(CheckMaxError):
                test_obj.__setattr__(prop["name"], max_val + 1)


@pytest.mark.parametrize("class_dict", class_list)
def test_class_prop_doc(class_dict):
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
        assert result == prop["desc"].split("\\n")


@pytest.mark.parametrize("class_dict", class_list)
def test_class_copy(class_dict):
    """Check if the copy method is correct
    """

    test_obj = eval(class_dict["name"] + "()")
    result = test_obj.copy()
    assert test_obj == result
