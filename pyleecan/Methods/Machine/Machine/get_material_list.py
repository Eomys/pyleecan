from ....Functions.Machine.get_material import get_material


def get_material_list(self):
    """
    Get the list of unique materials contained in a Machine

    Parameters
    ----------
    obj : Pyleecan object

    Returns
    -------
    materials : list of unique materials contained in the object
    """

    return get_material(self)
