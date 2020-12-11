# -*- coding: utf-8 -*-
from numpy import angle, exp, linspace, pi, sum, zeros


def comp_phasor_angle(self, Zs=None):
    """Compute the phasor angle of the winding phases related to the first slot

    Parameters
    ----------
    self : Winding
        A: Winding object
    Zs : int
        Number of Slot (Integer >0)

    Returns
    -------
    angle_vec: numpy.ndarray
        Phasor Angle Vector (qs)

    Raises
    ------

    """
    if Zs is None:
        if self.parent is None:
            raise WindingError(
                "ERROR: The Winding object must be in a Lamination object."
            )

        if self.parent.slot is None:
            raise WindingError(
                "ERROR: The Winding object must be in a Lamination object with Slot."
            )

        Zs = self.parent.slot.Zs

    assert Zs > 0, "Zs must be >0"
    assert Zs % 1 == 0, "Zs must be an integer"

    wind_mat = self.comp_connection_mat(Zs)
    p = self.p
    qs = self.qs  # number of phases

    slot_ang = (
        linspace(0, Zs, num=Zs, endpoint=False) * 2 * pi / Zs * p
    )  # slot electrical angle
    phasor = exp(1j * slot_ang)  # slot voltage phasor

    angle_vec = zeros(qs)

    for phase in range(qs):
        wind_sum = sum(wind_mat[:, :, :, phase], (0, 1))
        phasor_sum = sum(wind_sum * phasor)
        angle_vec[phase] = angle(phasor_sum)

    return angle_vec
