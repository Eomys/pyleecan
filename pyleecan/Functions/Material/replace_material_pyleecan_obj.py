from ...Classes.Material import Material
from ...Functions.Material.compare_material import compare_material


def replace_material_pyleecan_obj(obj, mat1, mat2, comp_name_path=True):
    """
    replace first material by the second in the object

    Parameters
    ----------
    obj: Pyleecan object
    mat1: Material
        material to replace
    mat2: Material
        new material
    comp_name_path: bool
        replace strictly mat1 or replace materials without comparing mat1.path and mat1.name

    Returns
    -------
    is_change: bool
        True if a material has been replaced
    """
    is_change = False
    obj_dict = obj.as_dict()
    if comp_name_path:
        for key, val in obj_dict.items():
            if isinstance(getattr(obj, key), Material) and getattr(obj, key) == mat1:
                setattr(obj, key, mat2)
                is_change = True
            # Call the function recursively to modify attributes materials
            elif isinstance(val, dict):
                is_change_recurs = replace_material_pyleecan_obj(
                    getattr(obj, key), mat1, mat2, comp_name_path
                )
                # update is_change if needed
                if not is_change:
                    is_change = is_change_recurs
    else:
        for key, val in obj_dict.items():
            # Compare materials with mat1 without name and path
            if isinstance(getattr(obj, key), Material) and compare_material(
                getattr(obj, key), mat1
            ):
                setattr(obj, key, mat2)
                is_change = True
            # Call the function recursively to modify attributes materials
            elif isinstance(val, dict):
                is_change_recurs = replace_material_pyleecan_obj(
                    getattr(obj, key), mat1, mat2, comp_name_path
                )
                # update is_change if needed
                if not is_change:
                    is_change = is_change_recurs

    return is_change
