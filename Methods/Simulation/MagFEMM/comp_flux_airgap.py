# -*- coding: utf-8 -*-
"""@package comp_flux_airgap
@date Created on août 01 15:46 2018
@author franco_i
"""

from pyleecan.Functions.FEMM.draw_FEMM import draw_FEMM
from pyleecan.Functions.FEMM.solve_FEMM import solve_FEMM
from pyleecan.Functions.FEMM.set_FEMM_circuit_prop import set_FEMM_circuit_prop
from pyleecan.Functions.FEMM.update_FEMM_simulation import update_FEMM_simulation
import femm
from numpy import pi, linspace, sin, cos, zeros, transpose
from pyleecan.Functions.FEMM import acsolver, pbtype, precision, minangle


def comp_flux_airgap(self, output):
    """Compute using FEMM the flux in the airgap

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    output : Output
        an Output object
    """

    # Setup the FEMM simulation
    # Geometry building and assigning property in FEMM
    materials, circuits = draw_FEMM(
        output,
        is_mmfr=self.is_mmfr,
        is_mmfs=self.is_mmfs,
        j_t0=1,
        type_calc_leakage=self.type_calc_leakage,
        sym=1,  # output.geo.sym,
        is_remove_vent=self.is_remove_vent,
        is_remove_slotS=self.is_remove_slotS,
        is_remove_slotR=self.is_remove_slotR,
        is_stator_linear_BH=self.is_stator_linear_BH,
        is_rotor_linear_BH=self.is_rotor_linear_BH,
        kgeo_fineness=1,
        kmesh_fineness=1,
        path_save=self.get_path_save(output),
    )

    # Compute the data for each time step
    Br = zeros((output.mag.Nt_tot, output.mag.Na_tot))
    Bt = zeros((output.mag.Nt_tot, output.mag.Na_tot))
    angle = output.mag.angle
    for ii in range(len(output.elec.time)):
        update_FEMM_simulation(
            output, materials, circuits, self.is_mmfs, self.is_mmfr, j_t0=ii
        )
        # Run the computation
        femm.mi_zoomnatural()  # Zoom out
        freqpb = 0  # setting 2D magnetostatic problem
        Lfemm = output.simu.machine.rotor.comp_length()
        femm.mi_probdef(freqpb, "meters", pbtype, precision, Lfemm, minangle, acsolver)
        femm.mi_analyze()
        femm.mi_loadsolution()
        # Get the result
        for jj in range(len(angle)):
            B = femm.mo_getgapb("bc_ag2", angle[jj] * 180 / pi)
            Br[ii, jj] = B[0]
            Bt[ii, jj] = B[1]
            # B = femm.mo_getb(
            #     output.geo.Rgap_mec * cos(angle[jj]),
            #     output.geo.Rgap_mec * sin(angle[jj]),
            # )
            # Bx = B[0].real
            # By = B[1].real
            # Br[ii, jj] = Bx * cos(angle[jj]) + By * sin(angle[jj])
            # Bt[ii, jj] = -Bx * sin(angle[jj]) + By * cos(angle[jj])
    # Store the results
    output.mag.Br = Br
    output.mag.Bt = Bt
