def check_parent(obj, Nparent):
    """Recursively check that the object have the correct number of parent
    For instance: check_parent(stator, 3) will check that
    output.simu.machine.stator exist

    Parameters
    ----------
    obj :
        A pyleecan object
    Nparent : int
        Number of parent we expect the object to have

    Returns
    -------
    has_parent : bool
        True if the object has N parent
    """

    if Nparent == 0:
        return True
    elif obj.parent is None:
        return False
    else:
        return check_parent(obj.parent, Nparent - 1)
