from ...Generator import TAB, TAB2, TAB3, TAB4, TAB5
from ...Generator.read_fct import (
    is_list_pyleecan_type,
    is_dict_pyleecan_type,
    is_dict_list_pyleecan_type,
)


def generate_compare(gen_dict, class_dict):
    """Generate the code for the compare method of the class

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)

    class_dict : dict
        dictionary of the class to generate (keys are name, package, properties, methods...)

    Returns
    -------
    compare_str : str
        String containing the code for the compare method of the class
    """

    class_name = class_dict["name"]
    compare_str = ""  # This string is for the generated code

    # Code generation
    compare_str += (
        TAB
        + "def compare(self, other, name='self', ignore_list=None, is_add_value=False):\n"
    )
    compare_str += TAB2 + '"""Compare two objects and return list of differences"""\n\n'
    # Check the type
    compare_str += TAB2 + "if ignore_list is None:\n"
    compare_str += TAB3 + "ignore_list = list()\n"
    compare_str += TAB2 + "if type(other) != type(self):\n"
    compare_str += TAB3 + "return ['type('+name+')']\n"
    compare_str += TAB2 + "diff_list = list()\n"
    # Call mother eq
    if class_dict["mother"] != "":
        compare_str += (
            "\n"
            + TAB2
            + "# Check the properties inherited from "
            + class_dict["mother"]
            + "\n"
        )
        compare_str += (
            TAB2
            + "diff_list.extend(super("
            + class_name
            + ", self).compare(other,name=name, ignore_list=ignore_list, is_add_value=is_add_value))\n"
        )
    # Check that all the propoperties (except parent) are equal
    for prop in class_dict["properties"]:
        if prop["type"] == "ndarray":
            compare_str += (
                TAB2
                + "if not array_equal(other."
                + prop["name"]
                + ", self."
                + prop["name"]
                + "):\n"
            )
            compare_str += TAB3 + "diff_list.append(name+'." + prop["name"] + "')\n"
        elif prop["type"] in [None, ""]:
            compare_str += (
                TAB2
                + "if (other."
                + prop["name"]
                + " is None and self."
                + prop["name"]
                + " is not None) or (other."
                + prop["name"]
                + " is not None and self."
                + prop["name"]
                + " is None):\n"
            )
            compare_str += TAB3 + "diff_list.append(name+'." + prop["name"] + "')\n"
            compare_str += TAB2 + "elif self." + prop["name"] + " is None:\n"
            compare_str += TAB3 + "pass\n"
            compare_str += (
                TAB2
                + "elif isinstance(self."
                + prop["name"]
                + ", np.ndarray) and not np.array_equal(other."
                + prop["name"]
                + ", self."
                + prop["name"]
                + "):\n"
            )
            compare_str += TAB3 + "diff_list.append(name+'." + prop["name"] + "')\n"
            compare_str += (
                TAB2 + "elif hasattr(self." + prop["name"] + ", 'compare'):\n"
            )
            compare_str += (
                TAB3
                + "diff_list.extend(self."
                + prop["name"]
                + ".compare(other."
                + prop["name"]
                + ",name=name+'."
                + prop["name"]
                + "',ignore_list=ignore_list,is_add_value=is_add_value))\n"
            )
            compare_str += (
                TAB2
                + "elif other._"
                + prop["name"]
                + " != self._"
                + prop["name"]
                + ":\n"
            )
            compare_str += TAB3 + "diff_list.append(name+'." + prop["name"] + "')\n"
        elif prop["type"] == "[ndarray]":
            compare_str += (
                TAB2
                + "if (other."
                + prop["name"]
                + " is None and self."
                + prop["name"]
                + " is not None) or (other."
                + prop["name"]
                + " is not None and self."
                + prop["name"]
                + " is None):\n"
            )
            compare_str += TAB3 + "diff_list.append(name+'." + prop["name"] + "')\n"
            compare_str += TAB2 + "elif self." + prop["name"] + " is None:\n"
            compare_str += TAB3 + "pass\n"
            compare_str += (
                TAB2
                + "elif len(other."
                + prop["name"]
                + ") != len(self."
                + prop["name"]
                + "):\n"
            )
            compare_str += (
                TAB3 + "diff_list.append('len('+name+'." + prop["name"] + ")')\n"
            )
            compare_str += TAB2 + "else:\n"
            compare_str += TAB3 + "for ii in range(len(other." + prop["name"] + ")):\n"
            compare_str += (
                TAB4
                + "if not array_equal(other."
                + prop["name"]
                + "[ii], self."
                + prop["name"]
                + "[ii]):\n"
            )
            compare_str += (
                TAB5 + "diff_list.append(name+'." + prop["name"] + "['+str(ii)+']')\n"
            )
        elif prop["type"] == "{ndarray}":
            compare_str += (
                TAB2
                + "if (other."
                + prop["name"]
                + " is None and self."
                + prop["name"]
                + " is not None) or (other."
                + prop["name"]
                + " is not None and self."
                + prop["name"]
                + " is None):\n"
            )
            compare_str += (
                TAB3 + "diff_list.append(name+'." + prop["name"] + " None mismatch')\n"
            )
            compare_str += TAB2 + "elif self." + prop["name"] + " is None:\n"
            compare_str += TAB3 + "pass\n"
            compare_str += (
                TAB2
                + "elif len(other."
                + prop["name"]
                + ") != len(self."
                + prop["name"]
                + "):\n"
            )
            compare_str += (
                TAB3 + "diff_list.append('len('+name+'." + prop["name"] + ")')\n"
            )
            compare_str += TAB2 + "else:\n"
            compare_str += TAB3 + "for key in other." + prop["name"] + ":\n"
            compare_str += (
                TAB4
                + "if key not in self."
                + prop["name"]
                + " or not array_equal(other."
                + prop["name"]
                + "[key], self."
                + prop["name"]
                + "[key]):\n"
            )
            compare_str += (
                TAB5 + "diff_list.append(name+'." + prop["name"] + "['+str(key)+']')\n"
            )
        elif prop["type"] == "function":
            compare_str += (
                TAB2
                + "if other._"
                + prop["name"]
                + "_str != self._"
                + prop["name"]
                + "_str:\n"
            )
            compare_str += TAB3 + "diff_list.append(name+'." + prop["name"] + "')\n"
        elif prop["type"] == "float":  # To take into account "nan"
            compare_str += (
                TAB2
                + "if other._"
                + prop["name"]
                + " is not None and self._"
                + prop["name"]
                + " is not None and isnan(other._"
                + prop["name"]
                + ") and isnan(self._"
                + prop["name"]
                + "):\n"
            )
            compare_str += TAB3 + "pass\n"
            compare_str += (
                TAB2
                + "elif other._"
                + prop["name"]
                + " != self._"
                + prop["name"]
                + ":\n"
            )
            compare_str += TAB3 + "if is_add_value:\n"
            compare_str += (
                TAB4
                + "val_str = ' (self='+str(self._"
                + prop["name"]
                + ")+', other='+str(other._"
                + prop["name"]
                + ")+')'\n"
            )
            compare_str += (
                TAB4 + "diff_list.append(name+'." + prop["name"] + "'+val_str)\n"
            )
            compare_str += TAB3 + "else:\n"
            compare_str += TAB4 + "diff_list.append(name+'." + prop["name"] + "')\n"
        elif prop["type"] in ["str", "int", "bool", "complex", "dict", "list"]:
            compare_str += (
                TAB2 + "if other._" + prop["name"] + " != self._" + prop["name"] + ":\n"
            )
            compare_str += TAB3 + "if is_add_value:\n"
            compare_str += (
                TAB4
                + "val_str = ' (self='+str(self._"
                + prop["name"]
                + ")+', other='+str(other._"
                + prop["name"]
                + ")+')'\n"
            )
            compare_str += (
                TAB4 + "diff_list.append(name+'." + prop["name"] + "'+val_str)\n"
            )
            compare_str += TAB3 + "else:\n"
            compare_str += TAB4 + "diff_list.append(name+'." + prop["name"] + "')\n"
        elif is_dict_list_pyleecan_type(prop["type"]):
            compare_str += (
                TAB2
                + "if (other."
                + prop["name"]
                + " is None and self."
                + prop["name"]
                + " is not None) or (other."
                + prop["name"]
                + " is not None and self."
                + prop["name"]
                + " is None):\n"
            )
            compare_str += (
                TAB3 + "diff_list.append(name+'." + prop["name"] + " None mismatch')\n"
            )
            compare_str += TAB2 + "elif self." + prop["name"] + " is None:\n"
            compare_str += TAB3 + "pass\n"
            compare_str += (
                TAB2
                + "elif len(other."
                + prop["name"]
                + ") != len(self."
                + prop["name"]
                + "):\n"
            )
            compare_str += (
                TAB3 + "diff_list.append('len('+name+'" + prop["name"] + ")')\n"
            )
            compare_str += TAB2 + "else:\n"
            compare_str += TAB3 + "for key in self." + prop["name"] + ":\n"
            compare_str += (
                TAB4 + "for ii in range(len(self." + prop["name"] + "[key])):\n"
            )
            compare_str += (
                TAB5
                + "diff_list.extend(self."
                + prop["name"]
                + "[key][ii].compare(other."
                + prop["name"]
                + "[key][ii],name=name+'."
                + prop["name"]
                + "',ignore_list=ignore_list,is_add_value=is_add_value))\n"
            )
        elif is_list_pyleecan_type(prop["type"]):
            compare_str += (
                TAB2
                + "if (other."
                + prop["name"]
                + " is None and self."
                + prop["name"]
                + " is not None) or (other."
                + prop["name"]
                + " is not None and self."
                + prop["name"]
                + " is None):\n"
            )
            compare_str += (
                TAB3 + "diff_list.append(name+'." + prop["name"] + " None mismatch')\n"
            )
            compare_str += TAB2 + "elif self." + prop["name"] + " is None:\n"
            compare_str += TAB3 + "pass\n"
            compare_str += (
                TAB2
                + "elif len(other."
                + prop["name"]
                + ") != len(self."
                + prop["name"]
                + "):\n"
            )
            compare_str += (
                TAB3 + "diff_list.append('len('+name+'." + prop["name"] + ")')\n"
            )
            compare_str += TAB2 + "else:\n"
            compare_str += TAB3 + "for ii in range(len(other." + prop["name"] + ")):\n"
            compare_str += (
                TAB4
                + "diff_list.extend(self."
                + prop["name"]
                + "[ii].compare(other."
                + prop["name"]
                + "[ii],name=name+'."
                + prop["name"]
                + "['+str(ii)+']',ignore_list=ignore_list,is_add_value=is_add_value))\n"
            )
        elif is_dict_pyleecan_type(prop["type"]):
            compare_str += (
                TAB2
                + "if (other."
                + prop["name"]
                + " is None and self."
                + prop["name"]
                + " is not None) or (other."
                + prop["name"]
                + " is not None and self."
                + prop["name"]
                + " is None):\n"
            )
            compare_str += (
                TAB3 + "diff_list.append(name+'." + prop["name"] + " None mismatch')\n"
            )
            compare_str += TAB2 + "elif self." + prop["name"] + " is None:\n"
            compare_str += TAB3 + "pass\n"
            compare_str += (
                TAB2
                + "elif len(other."
                + prop["name"]
                + ") != len(self."
                + prop["name"]
                + "):\n"
            )
            compare_str += (
                TAB3 + "diff_list.append('len('+name+'" + prop["name"] + ")')\n"
            )
            compare_str += TAB2 + "else:\n"
            compare_str += TAB3 + "for key in self." + prop["name"] + ":\n"
            compare_str += (
                TAB4
                + "diff_list.extend(self."
                + prop["name"]
                + "[key].compare(other."
                + prop["name"]
                + "[key],name=name+'."
                + prop["name"]
                + "['+str(key)+']',ignore_list=ignore_list,is_add_value=is_add_value))\n"
            )
        elif "." in prop["type"] and "SciDataTool" not in prop["type"]:
            # External type
            compare_str += (
                TAB2
                + "if (other."
                + prop["name"]
                + " is None and self."
                + prop["name"]
                + " is not None) or (other."
                + prop["name"]
                + " is not None and self."
                + prop["name"]
                + " is None):\n"
            )
            compare_str += (
                TAB3 + "diff_list.append(name+'." + prop["name"] + " None mismatch')\n"
            )
            compare_str += (
                TAB2
                + "elif self."
                + prop["name"]
                + " is not None and self."
                + prop["name"]
                + " != other."
                + prop["name"]
                + ":\n"
            )
            compare_str += TAB3 + "diff_list.append(name+'." + prop["name"] + "')\n"
        else:  # pyleecan type
            compare_str += (
                TAB2
                + "if (other."
                + prop["name"]
                + " is None and self."
                + prop["name"]
                + " is not None) or (other."
                + prop["name"]
                + " is not None and self."
                + prop["name"]
                + " is None):\n"
            )
            compare_str += (
                TAB3 + "diff_list.append(name+'." + prop["name"] + " None mismatch')\n"
            )
            compare_str += TAB2 + "elif self." + prop["name"] + " is not None:\n"
            compare_str += (
                TAB3
                + "diff_list.extend(self."
                + prop["name"]
                + ".compare(other."
                + prop["name"]
                + ",name=name+'."
                + prop["name"]
                + "',ignore_list=ignore_list,is_add_value=is_add_value))\n"
            )
    compare_str += TAB2 + "# Filter ignore differences\n"
    compare_str += (
        TAB2 + "diff_list = list(filter(lambda x : x not in ignore_list, diff_list))\n"
    )
    compare_str += TAB2 + "return diff_list\n"

    return compare_str
