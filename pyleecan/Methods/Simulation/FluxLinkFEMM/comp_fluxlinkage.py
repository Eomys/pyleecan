# -*- coding: utf-8 -*-

from ....Functions.FEMM.draw_FEMM import draw_FEMM
from ....Functions.Electrical.coordinate_transformation import n2dq

from numpy import zeros, linspace, pi, split, mean, sqrt
import matplotlib.pyplot as plt


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
    zp = output.simu.machine.stator.get_pole_pair_number()
    Nt_tot = self.Nt_tot
    angle_offset_initial = output.get_angle_offset_initial()
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
    output.elec.angle_rotor = rot_dir * angle

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
    
    # Define d axis angle for the d,q transform
    angle_offset_initial = output.get_angle_offset_initial()
    d_angle = (angle-angle_offset_initial) * zp
    fluxdq = split(n2dq(Phi_wind, d_angle, n=qs), 2, axis=1)
    Flux_link = mean(fluxdq[0]) / sqrt(3)
    
    flux = split(Phi_wind, 3, axis=1)
    fig = plt.figure()
    plt.plot(angle, flux[0], color="tab:blue", label="A")
    plt.plot(angle, flux[1], color="tab:red", label="B")
    plt.plot(angle, flux[2], color="tab:olive", label="C")
    plt.plot(angle, fluxdq[0], color="k", label="D")
    plt.plot(angle, fluxdq[1], color="g", label="Q")
    plt.legend()
    fig.savefig("test_fluxlink.png")

    # Reinitialize replaced data
    output.elec.angle_rotor = angle_rotor
    output.elec.Is = Is
    output.elec.Ir = Ir

    return Flux_link
