# Load the machine
from os.path import join
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
import matplotlib.pyplot as plt

from os.path import join

from numpy import ones, pi, array, linspace, cos, sqrt, zeros

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.MagFEMM import MagFEMM

@pytest.mark.skip(reason="Radial magnetization not available yet for Hole")
def test_LSRPM_simulation():
    # Create the Simulation
    LSRPM = load(join(DATA_DIR, "Machine", "LSRPM_001.json"))
    # LSRPM.plot()
    simu_femm = Simu1(name="FEMM_simulation", machine=LSRPM)
    p = simu_femm.machine.stator.winding.p
    qs = simu_femm.machine.stator.winding.qs

    # Defining Simulation Input
    simu_femm.input = InputCurrent()

    # Rotor speed [rpm]
    simu_femm.input.N0 = 750

    # time discretization [s]
    time = linspace(
        start=0, stop=60 / simu_femm.input.N0, num=32 * p, endpoint=False
    )  # 32*p timesteps
    simu_femm.input.time = time

    # Angular discretization along the airgap circonference for flux density calculation
    simu_femm.input.angle = linspace(
        start=0, stop=2 * pi, num=2048, endpoint=False
    )  # 2048 steps

    # Stator currents as a function of time, each column correspond to one phase [A]
    I0_rms = 6.85
    felec = p * simu_femm.input.N0 / 60  # [Hz]
    rot_dir = simu_femm.machine.stator.comp_rot_dir()
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp

    Ia = (
        I0_rms * sqrt(2) * cos(2 * pi * felec * time + 0 * rot_dir * 2 * pi / qs + Phi0)
    )
    Ib = (
        I0_rms * sqrt(2) * cos(2 * pi * felec * time + 1 * rot_dir * 2 * pi / qs + Phi0)
    )
    Ic = (
        I0_rms * sqrt(2) * cos(2 * pi * felec * time + 2 * rot_dir * 2 * pi / qs + Phi0)
    )
    Id = zeros(time.shape)
    Ie = zeros(time.shape)
    If = zeros(time.shape)
    simu_femm.input.Is = array([Ia, Ib, Ic, Id, Ie, If]).transpose()

    simu_femm.mag = MagFEMM(
        type_BH_stator=0,  # 0 to use the material B(H) curve,
        # 1 to use linear B(H) curve according to mur_lin,
        # 2 to enforce infinite permeability (mur_lin =100000)
        type_BH_rotor=0,  # 0 to use the material B(H) curve,
        # 1 to use linear B(H) curve according to mur_lin,
        # 2 to enforce infinite permeability (mur_lin =100000)
        file_name="",  # Name of the file to save the FEMM model
    )

    # Only the magnetic module is defined
    simu_femm.elec = None
    simu_femm.force = None
    simu_femm.struct = None
    simu_femm.mag.is_periodicity_a = True
    simu_femm.mag.is_periodicity_t = True
    simu_femm.mag.nb_worker = (
        4  # Number of FEMM instances to run at the same time (1 by default)
    )
    simu_femm.mag.is_get_meshsolution = (
        True  # To get FEA mesh for latter post-procesing
    )
    simu_femm.mag.is_save_meshsolution_as_file = (
        False  # To save FEA results in a dat file
    )
    out_femm = simu_femm.run()
    # Radial magnetic flux
    out_femm.mag.B.plot_2D_Data("angle", "time[1]", component_list=["radial"])
    out_femm.mag.B.plot_2D_Data(
        "wavenumber=[0,76]", "time[1]", component_list=["radial"]
    )
    # Tangential magnetic flux
    out_femm.mag.B.plot_2D_Data("angle", "time[1]", component_list=["tangential"])
    out_femm.mag.B.plot_2D_Data(
        "wavenumber=[0,76]", "time[1]", component_list=["tangential"]
    )
    out_femm.mag.Tem.plot_2D_Data("time")
    print(out_femm.mag.Tem.values.shape)
    print(simu_femm.input.Nt_tot)
    out_femm.mag.meshsolution.plot_contour(label="B", group_names="stator core")

    plt.show()


if __name__ == "__main__":
    test_LSRPM_simulation()
