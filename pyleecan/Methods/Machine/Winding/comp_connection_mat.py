from numpy import zeros, swapaxes, sign

from ....Methods.Machine.Winding import WindingError

from swat_em import datamodel


def comp_connection_mat(self, Zs=None, p=None):
    """Compute the Winding Matrix for

    Parameters
    ----------
    self : Winding
        A: Winding object
    Zs : int
        Number of Slot (Integer >0)
    p : int
        Number of pole pairs (Integer >0)

    Returns
    -------
    wind_mat: numpy.ndarray
        Winding Matrix (1, 1, Zs, qs)

    Raises
    ------
    WindingT2DefNtError
        Zs/qs/2 must be an integer

    """

    if Zs is None:
        if not hasattr(self.parent, "slot") and not hasattr(self.parent, "slot_list"):
            raise WindingError("The Winding object must be in a Lamination object.")

        Zs = self.parent.get_Zs()

    if p is None:
        if self.parent is None:
            raise WindingError("The Winding object must be in a Lamination object.")

        p = self.parent.get_pole_pair_number()

    assert Zs > 0, "Zs must be >0"
    assert Zs % 1 == 0, "Zs must be an integer"

    assert p > 0, "p must be >0"
    assert p % 1 == 0, "p must be an integer"

    qs = self.qs  # Phase Number

    Ntcoil = self.Ntcoil  # number of turns per coils

    Nlayer = self.Nlayer  # number of layers

    # Coil pitch (or coil span)
    if self.coil_pitch in [0, None]:
        # Number of slots per pole and per phase
        spp = Zs / (2 * p * qs)
        if spp > 0.5:
            # distributed winding
            self.coil_pitch = int(qs * spp)
        else:
            # tooth concentrated winding
            self.coil_pitch = 1

    # generate a datamodel for the winding
    wdg = datamodel()

    # generate winding from inputs
    wdg.genwdg(Q=Zs, P=2 * p, m=qs, layers=Nlayer, turns=Ntcoil, w=self.coil_pitch)

    # init connexion matrix
    wind_mat = zeros((Nlayer, 1, Zs, qs))

    # get connexion matrix from swat-em
    wind_mat_swat = wdg.get_phases()

    # perform checks
    assert p == wdg.get_num_polepairs(), (
        "number of pole pairs is not as requested (returned "
        + str(wdg.get_num_polepairs())
        + " expected "
        + str(p)
        + ")"
    )
    assert qs == wdg.get_num_phases(), (
        "number of phases is not as requested (returned "
        + str(wdg.get_num_phases())
        + " expected "
        + str(qs)
        + ")"
    )

    # convert swat-em connexion matrix to pyleecan connexion matrix
    for qq, phase in enumerate(wind_mat_swat):
        for ll, layer in enumerate(phase):
            if len(layer) > 0:
                for cond in layer:
                    wind_mat[Nlayer - ll - 1, 0, abs(cond) - 1, qq] = (
                        sign(cond) * Ntcoil
                    )

    # permute radial and tangential layers if coil span is 1
    if wdg.get_coilspan() == 1:
        wind_mat = swapaxes(wind_mat, 0, 1)

    # check that requested number of parallel connections is feasible
    Npcp_list = wdg.get_parallel_connections()
    if self.Npcp is None:
        self.Npcp = Npcp_list[0]
    elif self.Npcp > 2 * p:
        self.Npcp = 2 * p
        self.get_logger().warning(
            "Number of parallel circuits per phase must be < 2*p, assign it to: "
            + str(self.Npcp)
        )
    # if self.Npcp not in Npcp_list:

    #     if self.Npcp is not None:
    #         self.get_logger().warning(
    #             "Requested number of parallel circuits per phase is not feasible, assign it to: "
    #             + str(Npcp_list[0])
    #         )

    #     self.Npcp = Npcp_list[0]

    # enforce the number of layers if it is not as requested
    Nlayer_actual = wdg.get_num_layers()
    if self.Nlayer != Nlayer_actual:
        self.Nlayer = Nlayer_actual
        self.get_logger().info(
            "Requested number of layers is not feasible, assign it to: "
            + str(Nlayer_actual)
        )

    # get periodicities
    # self.per_a = wdg.get_periodicity_t()
    # self.is_aper_a = wdg.get_is_symmetric()

    # To check periodicities swat-em / pyleecan definitions
    self.per_a, self.is_aper_a = self.comp_periodicity(wind_mat=wind_mat)
    # if is_aper_a:  # Different def for Anti per
    #     per_a = per_a / 2
    # if self.per_a != per_a or self.is_aper_a != is_aper_a:
    #     self.get_logger().warning(
    #         "(Anti-)periodicity calculated by pyleecan and SWAT_EM differs"
    #     )

    # Set default values
    if self.is_reverse_wind is None:
        self.is_reverse_wind = False
    if self.Nslot_shift_wind is None:
        self.Nslot_shift_wind = 0

    return wind_mat
