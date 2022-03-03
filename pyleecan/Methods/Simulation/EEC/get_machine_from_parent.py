def get_machine_from_parent(self):
    """Get machine object from parent

    Parameters
    ----------
    self : EEC
        an EEC object

    Returns
    ----------
    machine : Machine
        a Machine object
    """

    parent = self.parent
    while parent is not None and not hasattr(parent, "machine"):
        parent = parent.parent

    if parent is not None:
        return parent.machine
    else:
        # Try to import machine from simu object
        parent = self.parent
        while parent is not None and not hasattr(parent, "simu"):
            parent = parent.parent
        if parent is not None:
            return parent.simu.machine
        else:
            return None
