from numpy import pi


def is_full_pitch_active(self):
    """Returns True if the active surface angular width
    matches the slot pitch (like SlotM17 or SlotM18)
    (used to set Boundary conditions in FEMM airgap)

    Parameters
    ----------
    self : SlotM17
        A SlotM17 object

    Returns
    -------
    is_full_pitch_active : bool
        True if the active surface angular width matches the slot pitch
    """

    return True
