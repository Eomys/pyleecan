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
    # Try to find simulation parent (output.simu.elec.eec)
    while parent is not None and not hasattr(parent, "machine"):
        parent = parent.parent

    if parent is not None and hasattr(parent, "machine"):
        return parent.machine
    else:
        # Try to find output parent (output.elec.eec)
        parent = self.parent
        while parent is not None and not hasattr(parent, "simu"):
            parent = parent.parent
        if parent is not None:
            return parent.simu.machine
        else:
            return None
