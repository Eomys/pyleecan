import numpy as np

from ....Functions.Winding.comp_cond_function import comp_cond_function


def comp_wind_function(self, angle, angle_rotor, per_a=1, is_aper_a=False):
    """Computation of the winding function for the squirrel cage lamination.
    By convention a tooth is centered on the X axis

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object
    angle : ndarray
        Space discretization to compute the winding functions
    angle_rotor: ndarray
        Rotor angular position over time [rad] (only for compatibility at the moment)
    per_a : int
        Spatial periodicity factor

    Returns
    -------
    wf: ndarray
        Winding function Matrix (qs,Nt,Na)
    """

    Na = angle.size
    Nt = angle_rotor.size

    Zs = self.slot.Zs  # Number of slot

    Zs0 = int(Zs / per_a)

    # if is_aper_a:
    #   Zs0 = int(Zs0 / 2)

    slot_opening = self.slot.comp_angle_opening()

    wf = np.zeros((Zs0, Nt, Na))

    alpha_slot = np.linspace(0, 2 * np.pi, Zs, endpoint=False) + np.pi / Zs

    for b in range(Zs0):
        # interpolation is creating spurious harmonics so winding function is recalculated for each bar
        alpha_coil = np.mod(alpha_slot[b] + angle_rotor, 2 * np.pi / per_a)

        # Single winding function in every slot and angle for nth layer [Na, Zs]
        wf_b = -0.5 * comp_cond_function(
            alpha_coil[:, None], slot_opening, angle[None, :]
        )

        wf[b, ...] = wf_b

    # import matplotlib.pyplot as plt

    # plt.figure()
    # plt.plot(wf[0, 0, :])
    # plt.plot(wf[1, 0, :])
    # plt.plot(wf[-1, 0, :])
    # plt.show()

    return wf
