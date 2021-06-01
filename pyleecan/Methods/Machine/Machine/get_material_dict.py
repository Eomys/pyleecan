from ....Classes.Material import Material


def get_material_dict(self, path="self", is_unique=False):
    """
    Get the dict of materials contained in a Machine

    Parameters
    ----------
    self : Machine
        A Machine object
    path : str
        prefix to use for material object path
    is_unique : bool
        True each material will only one in the dict

    Returns
    -------
    materials : dict
        dict of materials contained in the object (key="obj path" like self.mat_type)
    """

    mach_mat_dict = get_material(self, path=path)
    if is_unique:
        result = dict()
        name_list = list()
        for key, mat in mach_mat_dict.items():
            if mat.name is not None and mat.name not in name_list:
                result[key] = mat
                name_list.append(mat.name)
        return result
    else:
        return mach_mat_dict


def get_material(obj, path="self"):
    """
    Get the dict of materials contained in a pyleecan object

    Parameters
    ----------
    obj : Pyleecan object

    Returns
    -------
    materials : dict
        dict of materials contained in the object (key=obj path like self.mat_type)
    """
    materials = dict()
    path += "."
    for key, value in obj.as_dict().items():
        # Get an object attribute
        sub_obj = getattr(obj, key)

        # Add it if it's a Material
        if isinstance(sub_obj, Material):
            materials[path + key] = sub_obj

        # Check the sub object if it's a Pyleecan object
        elif isinstance(value, dict) and "__class__" in value:
            materials.update(get_material(sub_obj, path=path + key))
        elif isinstance(value, list):
            for ii, v in enumerate(value):
                if isinstance(v, dict) and "__class__" in v:
                    materials.update(get_material(sub_obj[ii], path=path + key))

    return materials
