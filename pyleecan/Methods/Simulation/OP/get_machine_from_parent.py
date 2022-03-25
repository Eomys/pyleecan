def get_machine_from_parent(self):
    """Search in the parent to find the machine

    Parameters
    ----------
    self : OP
        An OP object

    Returns
    -------
    machine : Machine
        Machine from the parent (or None)
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
