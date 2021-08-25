from numpy import array_equal, roll, squeeze, sum as np_sum, lcm
from numpy.linalg import norm


def comp_periodicity_spatial(self, wind_mat=None):
    """Computes the winding matrix (anti-)periodicity

    Parameters
    ----------
    self : Winding
        A Winding object
    wind_mat : ndarray
        Winding connection matrix

    Returns
    -------
    per_a: int
        Number of spatial periods of the winding
    is_aper_a: bool
        True if the winding is anti-periodic over space

    """

    if wind_mat is None:
        wind_mat = self.get_connection_mat()

    assert len(wind_mat.shape) == 4, "dim 4 expected for wind_mat"

    # Summing on all the layers (Nlay_r and Nlay_theta)
    wind_mat2 = squeeze(np_sum(np_sum(wind_mat, axis=1), axis=0))

    qs = wind_mat.shape[3]  # Number of phase
    Zs = wind_mat.shape[2]  # Number of Slot

    Nperw = 1  # Number of electrical period of the winding
    Nperslot = 1  # Periodicity of the winding in number of slots

    # Looking for the periodicity of each phase
    for q in range(0, qs):
        k = 1
        is_per = False
        while k <= Zs and not is_per:
            # We shift the array arround the slot and check if it's the same
            if array_equal(wind_mat2[:, q], roll(wind_mat2[:, q], shift=k)):
                is_per = True
            else:
                k += 1
        # least common multiple to find common periodicity between different phase
        Nperslot = lcm(Nperslot, k)

    # If Nperslot > Zs no symmetry
    if Nperslot > 0 and Nperslot < Zs:
        # nb of periods of the winding (2 means 180°)
        Nperw = Zs / float(Nperslot)
        # if Zs cannot be divided by Nperslot (non integer)
        if Nperw % 1 != 0:
            Nperw = 1

    # Check for anti symmetries in the elementary winding pattern
    if (
        Nperslot % 2 == 0
        and norm(
            wind_mat2[0 : Nperslot // 2, :] + wind_mat2[Nperslot // 2 : Nperslot, :]
        )
        == 0
    ):
        is_aper_a = True
        Nperw = Nperw * 2
    else:
        is_aper_a = False

    return int(Nperw), is_aper_a
