def comp_Is(self, time):
    """Compute the stator current on the given time vector to use it in Magnetics model

    Parameters
    ----------
    self : OutElec
        an OutElec object
    time : ndarray
        Time vector on which to interpolate stator currents stored in OutElec

    Returns
    -------
    Is: ndarray
        Stator current matrix [qs,Nt]
    """
    # Get stator lamination
    stator = self.parent.simu.machine.stator

    if hasattr(stator, "winding") and stator.winding is not None:

        # Get the number of parallel circuit per phase of stator winding
        Npcpp = stator.winding.Npcpp

        # Get stator currents
        Is_data = self.get_Is()

        # Interpolate stator currents on input time vector
        Is = (
            Is_data.get_along(
                "time=axis_data",
                "phase",
                axis_data={"time": time},
            )["Is"]
            / Npcpp
        )

        # Add time dimension if Is is calculated only for one time step
        if len(Is.shape) == 1:
            Is = Is[:, None]

    else:
        Is = None

    return Is
