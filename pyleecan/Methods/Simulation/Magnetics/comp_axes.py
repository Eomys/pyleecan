# -*- coding: utf-8 -*-
from ....Functions.Simulation.create_from_axis import create_from_axis


def comp_axes(self, output):
    """Compute the axes required in any Magnetics module

    Parameters
    ----------
    self : Magnetic
        a Magnetic object
    output : Output
        an Output object (to update)

    Returns
    -------
    axes_dict: {Data}
        Dict containing Time and Angle axes including (anti-)periodicties used in any Magnetics module

    """

    # Store Time axis in OutMag
    output.mag.Time = output.elec.Time.copy()

    # Store Angle axis in OutMag
    output.mag.Angle = output.elec.Angle.copy()

    # Calculate axes for Magnetics module calculation
    # Get time and space (anti-)periodicities of the machine
    (
        per_a,
        is_antiper_a,
        per_t,
        is_antiper_t,
    ) = output.get_machine_periodicity()

    # Compute Time axis based on the one stored in OutElec
    Time, is_periodicity_t = create_from_axis(
        axis_in=output.mag.Time,
        per=per_t,
        is_aper=is_antiper_t,
        is_include_per=self.is_periodicity_t,
        is_remove_aper=False,
    )

    if is_periodicity_t != self.is_periodicity_t:
        # Remove time periodicity in Magnetic model
        self.is_periodicity_t = False
        Nt_tot = Time.get_length(is_oneperiod=False)
        self.get_logger().warning(
            "WARNING: In Magnetic model, Nt_tot="
            + str(Nt_tot)
            + " is not divisible by the machine time periodicity ("
            + str(per_t)
            + "). Time periodicity removed"
        )

    # Compute Angle axis based on the one stored in OutElec
    Angle, is_periodicity_a = create_from_axis(
        axis_in=output.mag.Angle,
        per=per_a,
        is_aper=is_antiper_a,
        is_include_per=self.is_periodicity_a,
        is_remove_aper=False,
    )

    if is_periodicity_a != self.is_periodicity_a:
        # Remove time periodicity in Magnetic model
        self.is_periodicity_a = False
        Na_tot = Angle.get_length(is_oneperiod=False)
        self.get_logger().warning(
            "WARNING: In Magnetic model, Na_tot="
            + str(Na_tot)
            + " is not divisible by the machine angular periodicity ("
            + str(per_a)
            + "). Angular periodicity removed"
        )

    axes_dict = {"Time": Time, "Angle": Angle}

    return axes_dict
