# -*- coding: utf-8 -*-

from os import chdir, listdir, remove
from os.path import isdir, join

import pytest
from cloudpickle import dumps
from numpy import array, array_equal
from pyleecan.Classes._check import CheckMaxError, CheckMinError, CheckTypeError
from pyleecan.Classes._frozen import FrozenClass, FrozenError
from pyleecan.Classes.import_all import *
from pyleecan.definitions import DOC_DIR, MAIN_DIR
from pyleecan.Generator import PYTHON_TYPE
from pyleecan.Generator.ClassGenerator.init_method_generator import get_mother_attr
from pyleecan.Generator.read_fct import read_all
from Tests import save_path
from Tests.find import find_test_value, is_type_dict, is_type_list

# Get the dict of all the classes and their information
gen_dict = read_all(DOC_DIR)  # dict of class dict
# Remove one list level (packages Machine, Simulation, Material...)
class_list = list(gen_dict.values())

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
        if type_name == "dict":
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
        elif type_name in PYTHON_TYPE:
            if type_name == "list" and prop["value"] == -1:
                assert result == [], (
                    "Error for class "
                    + class_dict["name"]
                    + " for property: "
                    + prop["name"],
                )
            else:
                assert result == prop["value"], (
                    "Error for class "
                    + class_dict["name"]
                    + " for property: "
                    + prop["name"],
                )
        elif is_type_list(type_name):  # List of pyleecan type
            if prop["value"] == "":
                value = []
            else:
                value = prop["value"]
            assert result == value, (
                "Error for class "
                + class_dict["name"]
                + " for property: "
                + prop["name"],
            )
        elif is_type_dict(type_name):  # Dict of pyleecan type
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
        elif type_name == "ndarray":
            if type(prop["value"]) is list:
                expect = array(prop["value"])
            else:
                expect = None
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
            if prop["value"] == "":
                d[prop["name"]] = None
            else:
                d[prop["name"]] = prop["value"]
        elif prop["value"] in ["None", None]:
            d[prop["name"]] = None
        elif type(prop["value"]) is str and "()" in prop["value"]:
            d[prop["name"]] = eval(prop["value"] + ".as_dict()")
        elif prop["type"] == "complex":
            d[prop["name"]] = str(prop["value"])
        elif prop["type"] == "dict":
            if prop["value"] == "":
                d[prop["name"]] = {}
            else:
                d[prop["name"]] = prop["value"]
        elif prop["type"] == "list":
            if prop["value"] in ["", -1]:
                d[prop["name"]] = []
            else:
                d[prop["name"]] = prop["value"]
        elif prop["type"] in PYTHON_TYPE:  # PYTHON_TYPE and not dict or list
            d[prop["name"]] = prop["value"]
        elif "." in prop["type"]:  # Imported type or list of imported type
            val = eval(prop["value"])
            d[prop["name"]] = {
                "__class__": str(type(val)),
                "__repr__": str(val.__repr__()),
                "serialized": dumps(val).decode("ISO-8859-2"),
            }
        elif is_type_list(prop["type"]):  # List of pyleecan type
            d[prop["name"]] = list()
        elif is_type_dict(prop["type"]):  # Dict of pyleecan type
            d[prop["name"]] = dict()
        else:  # pyleecan type
            d[prop["name"]] = eval(prop["type"] + "().as_dict()")
    d["__class__"] = class_dict["name"]

    test_obj = eval(class_dict["name"] + "()")
    # Test
    try:
        result_dict = test_obj.as_dict(type_handle_ndarray=0, keep_function=False)
    except Exception as e:
        raise Exception(
            "Error while calling as_dict for " + class_dict["name"] + ":\n" + str(e)
        )
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
    assert d.keys() == result_dict.keys(), (
        "Wrong as_dict keys for class "
        + class_dict["name"]
        + " returned "
        + str(result_dict.keys())
        + " expected "
        + str(d.keys())
    )


@pytest.mark.parametrize("class_dict", class_list)
def test_class_set_None(class_dict):
    """Check that _set_None set to None every non pyleecantype properties"""

    test_obj = eval(class_dict["name"] + "()")
    test_obj._set_None()
    prop_list = get_mother_attr(gen_dict, class_dict, "properties")[0]
    for prop in prop_list:
        # ndarray set as None are set as array([])
        if prop["type"] in PYTHON_TYPE or prop["type"] == "ndarray":
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


@pytest.mark.parametrize("class_dict", class_list)
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

        meth_obj = eval("getattr(" + class_dict["name"] + ", '" + meth + "')")
        assert not isinstance(meth_obj, property), meth_obj.fget("")


@pytest.mark.parametrize("class_dict", class_list)
def test_class_uncleaned_methods(class_dict):
    """Check if all the method in the class folder is in the csv"""
    folder_path = join(MAIN_DIR, "Methods", class_dict["package"], class_dict["name"])

    meth_list = get_mother_attr(gen_dict, class_dict, "methods")[0]
    if len(meth_list) == 0 and isdir(folder_path):
        raise Exception(
            class_dict["name"]
            + " has no method in the csv but the method folder exist: "
            + folder_path
        )
    elif len(meth_list) != 0 and isdir(folder_path):
        dir_list = listdir(folder_path)
        if "__init__.py" in dir_list:
            dir_list.remove("__init__.py")
        if "__pycache__" in dir_list:
            dir_list.remove("__pycache__")
        # Get only python file
        file_list = [path for path in dir_list if path[-3:] == ".py"]
        # Add subfolder
        for path in dir_list:
            if isdir(join(folder_path, path)):
                file_list.extend(
                    [
                        path + "." + name
                        for name in listdir(join(folder_path, path))
                        if name[-3:] == ".py"
                    ]
                )
                if path + ".__init__.py" in file_list:
                    file_list.remove(path + ".__init__.py")
        # Check if all files are methods
        for file_name in file_list:
            assert file_name[:-3] in meth_list, (
                class_dict["name"]
                + " method folder contains a file not referenced in the csv: "
                + file_name
            )
        assert len(set(class_dict["methods"])) == len(class_dict["methods"]), (
            class_dict["name"] + " check for duplicate method in csv"
        )
    # else : no method and no folder => Ok


@pytest.mark.parametrize("class_dict", class_list)
def test_class_type_float(class_dict):
    """Check if the setter is type sensitive for float"""
    test_obj = eval(class_dict["name"] + "()")

    prop_list = get_mother_attr(gen_dict, class_dict, "properties")[0]
    for prop in prop_list:
        value = find_test_value(prop, "float")
        msg = "Error for class " + class_dict["name"] + " with " + prop["name"]
        # Check the doc to know if it should raise an error or not
        if prop["type"] in ["float", "complex", "", None]:
            # No error expected
            test_obj.__setattr__(prop["name"], value)

            assert test_obj.__getattribute__(prop["name"]) == value, msg
        elif (
            prop["type"] == "int"
            and prop["min"] not in ["", None]
            and prop["max"] not in ["", None]
            and prop["min"] == prop["max"]
        ):
            # Integer with only one value possible => find_test_value returns this value as float so it passes
            test_obj.__setattr__(prop["name"], value)
            assert test_obj.__getattribute__(prop["name"]) == value, msg
        else:
            # CheckTypeError expected
            with pytest.raises(CheckTypeError):
                # print(msg + " value " + str(value) + " type " + str(type(value)))
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

        # Check only the part from the csv
        type_index = 2
        for line in result[2:]:
            if ":Type:" in line:
                break
            else:
                type_index += 1
        assert result[: type_index - 1] == prop["desc"].split("\\n")
        # assert [res.split(" [")[0] for res in result[: type_index - 1]] == [
        #     p.split(" [")[0] for p in prop["desc"].split("\\n")
        # ]


@pytest.mark.parametrize("class_dict", class_list)
def test_class_copy(class_dict):
    """Check if the copy method is correct"""

    test_obj = eval(class_dict["name"] + "()")
    result = test_obj.copy()
    assert test_obj == result


if __name__ == "__main__":
    # test_class_as_dict(class_list[116])
    test_class_prop_doc(class_list[160])
