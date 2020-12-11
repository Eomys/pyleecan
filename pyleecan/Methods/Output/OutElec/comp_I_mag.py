from ....Classes.WindingSC import WindingSC
from numpy import array


def comp_I_mag(self, time, is_stator, phase=None):
    """Compute the current on the given lamination and time vector to use it in Magnetics model
    Phase currents are divided by the number of parallel circuits per pole
    and per phase to account for actual current in slot conductors

    Parameters
    ----------
    self : OutElec
        an OutElec object
    time : ndarray
        Time vector on which to interpolate currents stored in OutElec
    is_stator: bool
        True if lamination is stator
    per_a: int
        (Anti-)periodicity factor

    Returns
    -------
    I: ndarray
        Current matrix accounting for periodicities [q_pera,len(time)]
    """

    # Get lamination
    if is_stator:
        lam = self.parent.simu.machine.stator
    else:
        lam = self.parent.simu.machine.rotor

    if hasattr(lam, "winding") and lam.winding is not None:

        # Get the number of parallel circuit per phase of winding
        if hasattr(lam.winding, "Npcpp") and lam.winding.Npcpp is not None:
            Npcpp = lam.winding.Npcpp
        else:
            Npcpp = 1

        # Get current DataTime
        if is_stator:
            I_data = self.get_Is()
        else:
            I_data = self.Ir

        if phase is None:
            # Take all phases that are in the I_data Data object
            str_phase = "phase"
        else:
            str_phase = "phase" + str(phase)

        # Interpolate stator currents on input time vector
        I = (
            I_data.get_along(
                "time=axis_data",
                str_phase,
                axis_data={"time": time},
            )[I_data.symbol]
            / Npcpp
        )

        # Add time dimension if Is is calculated only for one time step
        if len(I.shape) == 1:
            I = I[:, None]

    else:
        I = None

    return I
