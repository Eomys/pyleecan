from os.path import join

from numpy import mean, split
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Simulation import Simulation

from ....Functions.Electrical.coordinate_transformation import n2dqh


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
    simu_ind = Simulation(
        elec=None, name=simu_name, path_result=path_result, machine=machine_fl
    )
    simu_ind.input = InputCurrent(
        N0=2000, Id_ref=0, Iq_ref=0, Nt_tot=self.Nt_tot, Na_tot=2048
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
    angle_rotor = out_ind.get_angle_rotor()
    angle_offset_initial = out_ind.get_angle_offset_initial()
    zp = machine.get_pole_pair_number()
    Phi_wind = out_ind.mag.Phi_wind_stator
    # Define d axis angle for the d,q transform
    d_angle = (angle_rotor - angle_offset_initial) * zp
    fluxdq = split(n2dqh(Phi_wind, d_angle), 2, axis=1)
    return (mean(fluxdq[0]), mean(fluxdq[1]))
