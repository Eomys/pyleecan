# -*- coding: utf-8 -*-
from ....Functions.Simulation.create_from_axis import create_from_axis


def comp_time_angle(self, output):
    """Compute the time and space discretization of the Force module

    Parameters
    ----------
    self : Force
        a Force object
    output : Output
        an Output object (to update)
    """

    # Get time and space (anti-)periodicities of the machine
    (
        per_a,
        is_antiper_a,
        per_t,
        is_antiper_t,
    ) = output.get_machine_periodicity()

    # Compute Time axis based on the one stored in OutMag and removing anti-periodicty
    Time, is_periodicity_t = create_from_axis(
        axis_in=output.mag.Time,
        per=per_t,
        is_aper=is_antiper_t,
        is_include_per=self.is_periodicity_t,
        is_remove_aper=True,
    )

    if is_periodicity_t != self.is_periodicity_t:
        Nt_tot = Time.get_length(is_oneperiod=False)
        self.get_logger().warning(
            "WARNING: In Force model, Nt_tot="
            + str(Nt_tot)
            + " is not divisible by the machine time periodicity ("
            + str(per_t)
            + "). Time periodicity removed"
        )

    # Store Time axis in OutForce
    output.force.Time = Time

    # Compute Angle axis based on the one stored in OutMag and removing anti-periodicty
    Angle, is_periodicity_a = create_from_axis(
        axis_in=output.mag.Angle,
        per=per_a,
        is_aper=is_antiper_a,
        is_include_per=self.is_periodicity_a,
        is_remove_aper=True,
    )

    if is_periodicity_a != self.is_periodicity_a:
        Na_tot = Angle.get_length(is_oneperiod=False)
        self.get_logger().warning(
            "WARNING: In Force model, Na_tot="
            + str(Na_tot)
            + " is not divisible by the machine angular periodicity ("
            + str(per_a)
            + "). Angular periodicity removed"
        )

    # Store Angle axis in OutForce
    output.force.Angle = Angle
