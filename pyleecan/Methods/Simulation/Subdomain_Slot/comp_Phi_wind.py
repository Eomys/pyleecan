from numpy import log, pi, einsum


def comp_Phi_wind(self):
    """Method description

    Parameters
    ----------
    self: Subdomain_Slot
        a Subdomain_Slot object

    Returns
    ----------
    var: type
        var description
    """

    sdm = self.parent

    lam = sdm.machine_polar_eq.stator
    per_a = sdm.per_a
    # antiper_a = sdm.antiper_a

    mu0 = 4 * pi * 1e-7

    R_5 = self.Rbore
    R_6 = self.Ryoke

    As = self.A
    Ji = self.Ji

    c = self.slot_width

    Lst1 = lam.L1

    # Stator slot surface
    Ss = abs((R_6**2 - R_5**2) / 2 * c)

    phi_i0 = Lst1 * (
        As
        + c
        * mu0
        / (16 * Ss)
        * (
            R_5**4
            - 4 * R_5**2 * R_6**2 * log(R_5)
            + 2 * R_5**2 * R_6**2
            + 4 * R_6**4 * log(R_6)
            - 3 * R_6**4
        )
        * Ji
    )

    wind_mat = lam.winding.comp_connection_mat()
    Nslot = self.number_per_a
    Npcp1 = lam.winding.Npcp

    Phi_wind = einsum(
        "mj, klmi -> ij", per_a * phi_i0 / Npcp1, wind_mat[:, :, :Nslot, :]
    )

    return Phi_wind
