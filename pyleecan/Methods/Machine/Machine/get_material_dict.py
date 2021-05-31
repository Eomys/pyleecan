from ....Classes.Material import Material


def get_material_dict(self, path="self"):
    """
    Get the dict of materials contained in a Machine

    Parameters
    ----------
    self : Machine
        A Machine object

    Returns
    -------
    materials : dict
        dict of materials contained in the object (key="obj path" like self.mat_type)
    """

    return get_material(self, path=path)


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
