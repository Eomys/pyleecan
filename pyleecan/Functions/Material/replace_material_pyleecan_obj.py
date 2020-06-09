def replace_material_pyleecan_obj(obj, mat1, mat2):
    """
    replace first material by the second in the object

    Parameters
    ----------
    obj: Pyleecan object
    mat1: Material
        material to replace
    mat2: Material
        new material
    """
    obj_dict = obj.as_dict()
    for key, val in obj_dict.items():
        if getattr(obj, key) == mat1:
            setattr(obj, key, mat2)
        elif isinstance(val, dict):
            replace_material_pyleecan_obj(getattr(obj, key), mat1, mat2)
