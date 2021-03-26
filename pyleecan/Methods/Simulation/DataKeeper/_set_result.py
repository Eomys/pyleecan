from ....Functions.Load.import_class import import_class
from ....Classes._check import check_var


def _set_result(self, value):
    """setter of result"""
    if type(value) is int and value == -1:
        value = list()
    # Load pyleecan/SciDataTool objects
    for ii, val in enumerate(value):
        if isinstance(val, dict) and "__class__" in val:
            try:
                class_obj = import_class(
                    "pyleecan.Classes", val.get("__class__"), "result_ref"
                )
            except:
                class_obj = import_class(
                    "SciDataTool.Classes", val.get("__class__"), "result_ref"
                )
            value[ii] = class_obj(init_dict=val)
    check_var("result", value, "list")
    self._result = value
