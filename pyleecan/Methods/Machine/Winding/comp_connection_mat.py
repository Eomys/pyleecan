# -*- coding: utf-8 -*-

from numpy import zeros, swapaxes, sign

from ....Methods.Machine.Winding import WindingError
from ....Functions.Winding.reverse_wind_mat import reverse_wind_mat
from ....Functions.Winding.shift_wind_mat import shift_wind_mat

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
        if self.parent is None:
            raise WindingError(
                "ERROR: The Winding object must be in a Lamination object."
            )

        if self.parent.slot is None:
            raise WindingError(
                "ERROR: The Winding object must be in a Lamination object with Slot."
            )

        Zs = self.parent.slot.Zs

    if p is None:
        if self.parent is None:
            raise WindingError(
                "ERROR: The Winding object must be in a Lamination object."
            )

        p = self.parent.get_pole_pair_number()

    assert Zs > 0, "Zs must be >0"
    assert Zs % 1 == 0, "Zs must be an integer"

    assert p > 0, "p must be >0"
    assert p % 1 == 0, "p must be an integer"

    qs = self.qs  # Phase Number

    Ntcoil = self.Ntcoil  # number of turns per coils

    Nlayer = self.Nlayer  # number of layers

    coil_pitch = self.coil_pitch  # coil pitch (coil span)

    # generate a datamodel for the winding
    wdg = datamodel()

    # generate winding from inputs
    wdg.genwdg(Q=Zs, P=2 * p, m=qs, layers=Nlayer, turns=Ntcoil, w=coil_pitch)

    # init connexion matrix
    wind_mat = zeros((Nlayer, 1, Zs, qs))

    # get connexion matrix from swat-em
    wind_mat_swat = wdg.get_phases()

    # perform checks
    assert p == wdg.get_num_polepairs(), "number of pole pairs is not as requested"
    assert qs == wdg.get_num_phases(), "number of phases is not as requested"

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
    if self.Npcp not in Npcp_list:

        if self.Npcp is not None:
            self.get_logger().warning(
                "Requested number of parallel circuits per phase is not feasible, assign it to: "
                + str(Npcp_list[0])
            )

        self.Npcp = Npcp_list[0]

    # enforce the number of layers if it is not as requested
    Nlayer_actual = wdg.get_num_layers()
    if self.Nlayer != Nlayer_actual:
        self.Nlayer = Nlayer_actual
        self.get_logger().info(
            "Requested number of layers is not feasible, assign it to: "
            + str(Nlayer_actual)
        )

    # get periodicities
    self.per_a = wdg.get_periodicity_t()
    self.is_aper_a = wdg.get_is_symmetric()
    per_a, is_aper_a = self.comp_periodicity(wind_mat=wind_mat)
    # if is_aper_a:  # Different def for Anti per  ?
    #     per_a = per_a / 2
    if self.per_a != per_a or self.is_aper_a != is_aper_a:
        self.get_logger().warning(
            "(Anti-)periodicity calculated by pyleecan and SWAT_EM differs"
        )

    # Set default values
    if self.is_reverse_wind is None:
        self.is_reverse_wind = False
    if self.Nslot_shift_wind is None:
        self.Nslot_shift_wind = 0
    # Apply the transformations
    if self.is_reverse_wind:
        wind_mat = reverse_wind_mat(wind_mat)
    if self.Nslot_shift_wind > 0:
        wind_mat = shift_wind_mat(wind_mat, self.Nslot_shift_wind)

    return wind_mat
