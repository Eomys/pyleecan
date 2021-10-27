from os.path import join

from ....Classes.InputCurrent import InputCurrent
from ....Classes.MagFEMM import MagFEMM
from ....Classes.Simulation import Simulation
from ....Classes.Simu1 import Simu1
from ....Functions.Electrical.dqh_transformation import n2dqh_DataTime


def comp_inductance(self, machine, OP_ref):
    """Compute using FEMM the inductance (Current driven only)

    Parameters
    ----------
    self : IndMagFEMM
        an IndMagFEMM object
    machine : Machine
        a Machine object
    OP_ref: OperatingPoint
        an OP object

    Returns
    ----------
    Phi_d_mean: float
        Flux linkage along d-axis
    """

    self.get_logger().info("Compute dq inductances with FEMM")

    # Get simulation name and result path
    if isinstance(machine.parent, Simulation) and machine.parent.name not in [None, ""]:
        simu_name = machine.parent.name + "_IndMagFEMM"
        path_result = (
            join(machine.parent.path_result, "IndMagFEMM")
            if machine.parent.path_result not in [None, ""]
            else None
        )
    elif machine.name not in [None, ""]:
        simu_name = machine.name + "_IndMagFEMM"
        path_result = None
    else:
        simu_name = "IndMagFEMM"
        path_result = None

    # Define simulation
    simu_ind = Simu1(
        elec=None, name=simu_name, path_result=path_result, machine=machine
    )
    simu_ind.input = InputCurrent(OP=OP_ref, Nt_tot=self.Nt_tot, Na_tot=2048)
    simu_ind.mag = MagFEMM(
        is_periodicity_t=True,
        is_periodicity_a=self.is_periodicity_a,
        is_sliding_band=self.is_sliding_band,
        Kgeo_fineness=self.Kgeo_fineness,
        type_calc_leakage=self.type_calc_leakage,
        nb_worker=self.nb_worker,
    )

    # Run Simulation
    out_ind = simu_ind.run()

    # Post-Process
    stator_label = machine.stator.get_label()
    Phidqh = n2dqh_DataTime(out_ind.mag.Phi_wind[stator_label])
    Phi_dqh_mean = Phidqh.get_along("time=mean", "phase")[Phidqh.symbol]

    return (Phi_dqh_mean[0], Phi_dqh_mean[1])
