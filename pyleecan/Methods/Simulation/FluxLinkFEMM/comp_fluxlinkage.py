# -*- coding: utf-8 -*-

from ....Functions.FEMM.draw_FEMM import draw_FEMM
from ....Functions.Electrical.coordinate_transformation import n2dq

from numpy import zeros, linspace, pi, split, mean


def comp_fluxlinkage(self, output):
    """Compute using FEMM the flux linkage

    Parameters
    ----------
    self : FluxLinkFEMM
        a FluxLinkFEMM object
    output : Output
        an Output object
    """

    qs = output.simu.machine.stator.winding.qs
    p = output.simu.machine.stator.winding.p
    Nt_tot = self.Nt_tot
    d_angle_diff = output.get_d_angle_diff()
    rot_dir = output.get_rot_dir()

    # Store data to be replaced
    angle_rotor = output.get_angle_rotor()
    Is = output.elec.Is
    Ir = output.elec.Ir

    # Set currents at 0A for the FEMM simulation
    output.elec.Is = zeros((Nt_tot, qs))
    output.elec.Ir = zeros((Nt_tot, qs))

    # Set the symmetry factor if needed
    if self.is_symmetry_a:
        sym = self.sym_a
        if self.is_antiper_a:
            sym *= 2
        if self.is_sliding_band:
            self.is_sliding_band = (
                True  # When there is a symmetry, there must be a sliding band.
            )
    else:
        sym = 1

    # Set rotor angle for the FEMM simulation
    angle = linspace(0, 2 * pi / sym, Nt_tot)
    output.elec.angle_rotor = angle

    # Define d axis angle for the d,q transform
    d_angle = rot_dir * (angle - d_angle_diff)

    # Setup the FEMM simulation
    # Geometry building and assigning property in FEMM
    FEMM_dict = draw_FEMM(
        output,
        is_mmfr=1,
        is_mmfs=1,
        sym=sym,
        is_antiper=self.is_antiper_a,
        type_calc_leakage=self.type_calc_leakage,
    )

    # Solve for all time step and store all the results in output
    Phi_wind = self.solve_FEMM(output, sym, FEMM_dict)
    fluxdq = split(n2dq(Phi_wind, p * d_angle, n=qs), 2, axis=1)
    Flux_link = mean(fluxdq[0])

    # Reinitialize replaced data
    output.elec.angle_rotor = angle_rotor
    output.elec.Is = Is
    output.elec.Ir = Ir

    return Flux_link
