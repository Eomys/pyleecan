from ....Functions.Load.import_class import import_class
from ....Classes._check import check_var


def _set_split_active_surf_dict(self, value):
    """setter of split_active_surf_dict"""
    if type(value) is dict:
        for key, obj_list in value.items():
            if type(obj_list) is list:
                for ii, obj in enumerate(obj_list):
                    if type(obj) is dict and "__class__" in obj:
                        class_obj = import_class(
                            "pyleecan.Classes",
                            obj["__class__"],
                            "split_active_surf_dict",
                        )
                        value[key][ii] = class_obj(init_dict=obj)
    if value == -1:
        value = dict()
    check_var("split_active_surf_dict", value, "dict")
    self._split_active_surf_dict = value
