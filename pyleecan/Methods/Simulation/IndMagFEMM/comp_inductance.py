# -*- coding: utf-8 -*-

from ....Functions.FEMM.draw_FEMM import draw_FEMM
from ....Functions.Electrical.coordinate_transformation import n2dq, dq2n

from numpy import array, zeros, linspace, pi, split, mean

import matplotlib.pyplot as plt


def comp_inductance(self, output):
    """Compute using FEMM the inductance

    Parameters
    ----------
    self : IndMagFEMM
        an IndMagFEMM object
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
    angle = linspace(0, 2 * pi / sym, Nt_tot, endpoint=False)
    output.elec.angle_rotor = angle / zp

    # Define d axis angle for the d,q transform
    d_angle = rot_dir * (angle + 1.31)

    # Set currents at 1A + Park transformation for the Id FEMM simulation
    output.elec.Is = dq2n(array([1, 0]), d_angle, n=qs)
    output.elec.Ir = zeros((Nt_tot, qs))

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
    
    time = linspace(0, Nt_tot, Nt_tot)
    flux = split(Phi_wind, 3, axis=1)
    fluxdq = split(n2dq(Phi_wind, d_angle, n=qs), 2, axis=1)
    fig = plt.figure()
    plt.plot(time, flux[0], color="tab:blue", label="A")
    plt.plot(time, flux[1], color="tab:red", label="B")
    plt.plot(time, flux[2], color="tab:olive", label="C")
    plt.plot(time, fluxdq[0], color="k", label="D")
    plt.plot(time, fluxdq[1], color="g", label="Q")
    plt.legend()
    fig.savefig("test_inductanceD.png")
    Lmd = mean(fluxdq[0])

    # Set currents at 1A + Park transformation for the Iq FEMM simulation
    output.elec.Is = dq2n(array([0, 1]), d_angle, n=qs)
    output.elec.Ir = zeros((Nt_tot, qs))

    # Solve for Lq
    Phi_wind = self.solve_FEMM(output, sym, FEMM_dict)
    
    flux = split(Phi_wind, 3, axis=1)
    fluxdq = split(n2dq(Phi_wind, d_angle, n=qs), 2, axis=1)
    fig = plt.figure()
    plt.plot(time, flux[0], color="tab:blue", label="A")
    plt.plot(time, flux[1], color="tab:red", label="B")
    plt.plot(time, flux[2], color="tab:olive", label="C")
    plt.plot(time, fluxdq[0], color="k", label="D")
    plt.plot(time, fluxdq[1], color="g", label="Q")
    plt.legend()
    fig.savefig("test_inductanceQ.png")
    Lmq = mean(fluxdq[1])

    # Reinitialize replaced data
    output.elec.angle_rotor = angle_rotor
    output.elec.Is = Is
    output.elec.Ir = Ir

    return (Lmd, Lmq)
