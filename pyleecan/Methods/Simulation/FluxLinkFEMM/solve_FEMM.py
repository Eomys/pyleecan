import femm

from numpy import zeros
from ....Functions.FEMM.update_FEMM_simulation import update_FEMM_simulation
from ....Functions.FEMM.comp_FEMM_Phi_wind import comp_FEMM_Phi_wind


def solve_FEMM(self, femm, output, sym, FEMM_dict):

    L1 = output.simu.machine.stator.comp_length()
    Nt_tot = self.Nt_tot  # Number of time step

    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        qs = output.simu.machine.stator.winding.qs  # Winding phase number
        Npcpp = output.simu.machine.stator.winding.Npcpp
        Phi_wind_stator = zeros((Nt_tot, qs))
    else:
        Phi_wind_stator = None

    # Create the mesh
    femm.mi_createmesh()

    # Compute the data for each time step
    for ii in range(Nt_tot):
        # Update rotor position and currents
        update_FEMM_simulation(
            femm=femm,
            output=output,
            materials=FEMM_dict["materials"],
            circuits=FEMM_dict["circuits"],
            is_mmfs=1,
            is_mmfr=1,
            j_t0=ii,
            is_sliding_band=self.is_sliding_band,
        )

        # Run the computation
        femm.mi_analyze()
        femm.mi_loadsolution()

        if (
            hasattr(output.simu.machine.stator, "winding")
            and output.simu.machine.stator.winding is not None
        ):
            # Phi_wind computation
            Phi_wind_stator[ii, :] = comp_FEMM_Phi_wind(
                femm,
                qs,
                Npcpp,
                is_stator=True,
                Lfemm=FEMM_dict["Lfemm"],
                L1=L1,
                sym=sym,
            )

    return Phi_wind_stator
