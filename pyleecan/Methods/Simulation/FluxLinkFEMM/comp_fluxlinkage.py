from os.path import join

from ....Classes.InputCurrent import InputCurrent
from ....Classes.OPdq import OPdq
from ....Classes.MagFEMM import MagFEMM
from ....Classes.Simu1 import Simu1
from ....Classes.Simulation import Simulation
from ....Functions.Electrical.dqh_transformation import n2dqh_DataTime


def comp_fluxlinkage(self, machine):
    """Compute using FEMM the flux linkage

    Parameters
    ----------
    self : FluxLinkFEMM
        a FluxLinkFEMM object
    machine : Machine
        a Machine object

    Returns
    ----------
    Phi_d_mean: float
        Flux linkage along d-axis
    """

    self.get_logger().info("Compute flux linkage with FEMM")

    # Get simulation name and result path
    if isinstance(machine.parent, Simulation) and machine.parent.name not in [None, ""]:
        simu_name = machine.parent.name + "_FluxLinkFEMM"
        path_result = (
            join(machine.parent.path_result, "FluxLinkFEMM")
            if machine.parent.path_result not in [None, ""]
            else None
        )
    elif machine.name not in [None, ""]:
        simu_name = machine.name + "_FluxLinkFEMM"
        path_result = None
    else:
        simu_name = "FluxLinkFEMM"
        path_result = None

    # Define simulation
    simu_fl = Simu1(elec=None, name=simu_name, path_result=path_result, machine=machine)
    simu_fl.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0), Nt_tot=self.Nt_tot, Na_tot=2048
    )
    simu_fl.mag = MagFEMM(
        is_periodicity_t=True,
        is_periodicity_a=self.is_periodicity_a,
        is_sliding_band=self.is_sliding_band,
        Kgeo_fineness=self.Kgeo_fineness,
        type_calc_leakage=self.type_calc_leakage,
        nb_worker=self.nb_worker,
    )

    # Run Simulation
    out_fl = simu_fl.run()

    # Post-Process
    stator_label = machine.stator.get_label()
    Phidqh = n2dqh_DataTime(
        out_fl.mag.Phi_wind[stator_label], phase_dir=out_fl.elec.phase_dir
    )
    Phi_d_mean = float(Phidqh.get_along("time=mean", "phase[0]")[Phidqh.symbol])

    return Phi_d_mean
