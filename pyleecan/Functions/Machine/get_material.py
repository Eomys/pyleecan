from ...Classes.Material import Material
from ...Functions.Material.compare_material import compare_material


def get_material(obj):
    """
    Get the list of unique materials contained in a pyleecan object

    Parameters
    ----------
    obj : Pyleecan object

    Returns
    -------
    materials : list of unique materials contained in the object
    """
    materials = []
    for key, value in obj.as_dict().items():
        # Get an object attribute
        sub_obj = getattr(obj, key)

        # Add it if it's a Material
        if isinstance(sub_obj, Material):
            materials.append(sub_obj)

        # Check the sub object if it's a Pyleecan object
        elif isinstance(value, dict) and "__class__" in value:
            materials.extend(get_material(sub_obj))

    # Return a unique list
    for material in materials[:]:
        n_mat = 0
        for mat in materials:
            if compare_material(mat, material):
                n_mat += 1
                if n_mat > 1:  # material found twice in the list
                    materials.remove(material)
                    break

    return materials
