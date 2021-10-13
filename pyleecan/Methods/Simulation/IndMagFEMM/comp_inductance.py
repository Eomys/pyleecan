from os.path import join

from numpy import mean, split
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Simulation import Simulation
from pyleecan.Classes.Simu1 import Simu1
from ....Functions.Electrical.coordinate_transformation import n2dqh_DataTime


def comp_inductance(self, machine, Id_ref, Iq_ref):
    """Compute using FEMM the inductance (Current driven only)

    Parameters
    ----------
    self : IndMagFEMM
        an IndMagFEMM object
    output : Output
        an Output object
    """

    self.get_logger().info("INFO: Compute dq inductances with FEMM")

    # Remove skew
    machine_fl = machine.copy()
    machine_fl.rotor.skew = None
    machine_fl.stator.skew = None

    # Get simulation name and result path
    if isinstance(machine.parent, Simulation) and machine.parent.name not in [None, ""]:
        simu_name = machine.parent.name + "_FluxLinkage"
        path_result = (
            join(machine.parent.path_result, "FluxLinkage")
            if machine.parent.path_result not in [None, ""]
            else None
        )
    elif machine.name not in [None, ""]:
        simu_name = machine.name + "_FluxLinkage"
        path_result = None
    else:
        simu_name = "FluxLinkage"
        path_result = None

    # Define simulation
    simu_ind = Simu1(
        elec=None, name=simu_name, path_result=path_result, machine=machine_fl
    )
    simu_ind.input = InputCurrent(
        N0=2000, Id_ref=Id_ref, Iq_ref=Iq_ref, Nt_tot=self.Nt_tot, Na_tot=2048
    )
    simu_ind.mag = MagFEMM(
        is_periodicity_t=True,
        is_periodicity_a=True,
        is_sliding_band=self.is_sliding_band,
        Kgeo_fineness=self.Kgeo_fineness,
        type_calc_leakage=self.type_calc_leakage,
    )

    # Run Simulation
    out_ind = simu_ind.run()

    # Post-Process
    Phidqh = n2dqh_DataTime(out_ind.mag.Phi_wind_stator)
    Phi_d_mean = float(Phidqh.get_along("time=mean", "phase[0]")["Phi_{wind}"])
    Phi_q_mean = float(Phidqh.get_along("time=mean", "phase[1]")["Phi_{wind}"])
    return (Phi_d_mean, Phi_q_mean)
