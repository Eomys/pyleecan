# -*- coding: utf-8 -*-

from ....Functions.FEMM.draw_FEMM import draw_FEMM
from ....Functions.Electrical.coordinate_transformation import n2dq
from ....Classes._FEMMHandler import FEMMHandler
from numpy import pi, split, mean


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

    # Open FEMM
    femm = FEMMHandler()
    # Setup the FEMM simulation
    # Geometry building and assigning property in FEMM
    FEMM_dict = draw_FEMM(
        femm=femm,
        output=output,
        is_mmfr=1,
        is_mmfs=1,
        sym=sym,
        is_antiper=self.is_antiper_a,
        type_calc_leakage=self.type_calc_leakage,
        kgeo_fineness=0.75,
    )

    # Solve for all time step and store all the results in output
    Phi_wind = self.solve_FEMM(femm, output, sym, FEMM_dict)

    # D/Q transform
    time = output.elec.time
    felec = output.elec.felec
    fluxdq = split(n2dq(Phi_wind, 2 * pi * felec * time, n=qs), 2, axis=1)

    return (mean(fluxdq[0]), mean(fluxdq[1]))
