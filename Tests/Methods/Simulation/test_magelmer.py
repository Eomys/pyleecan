from os import makedirs
from os.path import join, isdir
import pytest
from numpy import array, linspace, ones, pi, zeros, sqrt, cos
from Tests import save_plot_path
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagElmer import MagElmer
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Output import Output
from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.definitions import DATA_DIR

# Gather results in the same folder
save_path = join(save_plot_path, "Elmer")
if not isdir(save_path):
    makedirs(save_path)


mesh_dict = {
    "Lamination_Rotor_Bore_Radius_Ext": 180,
    "surface_line_0": 5,
    "surface_line_1": 10,
    "surface_line_2": 5,
    "surface_line_3": 5,
    "surface_line_4": 10,
    "surface_line_5": 5,
    "Lamination_Stator_Bore_Radius_Int": 10,
    "Lamination_Stator_Yoke_Side_Right": 30,
    "Lamination_Stator_Yoke_Side_Left": 30,
    "int_airgap_arc": 120,
    "int_sb_arc": 120,
    "ext_airgap_arc": 120,
    "ext_sb_arc": 120,
    "airbox_line_1": 10,
    "airbox_line_2": 10,
    "airbox_arc": 20,
}


@pytest.mark.MagElmer
@pytest.mark.long_5s
@pytest.mark.IPMSM
@pytest.mark.SingleOP
@pytest.mark.periodicity
def test_ipm_Elmer():
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    Toyota_Prius.stator.slot.H1 = 1e-3
    simu = Simu1(name="test_ipm_Elmer", machine=Toyota_Prius)

    # Definition of the enforced output of the electrical module
    # N0 = 1500
    # Is = ImportMatrixVal(value=array([[20, -10, -10],[20, -10, -10],[20, -10, -10]]))
    # Ir = ImportMatrixVal(value=zeros((1, 28)))
    # Nt_tot = 3
    # Na_tot = 4096
    # simu.input = InputCurrent(
    #     Is=Is,
    #     Ir=Ir,  # zero current for the rotor
    #     N0=N0,
    #     Nt_tot=Nt_tot,
    #     Na_tot=Na_tot,
    #     angle_rotor_initial=0.2244,
    # )

    # Definition of a sinusoidal current
    simu.input = InputCurrent()
    # simu.input.Id_ref = 0  # [A]
    # simu.input.Iq_ref = 250  # [A]
    # simu.input.Nt_tot = 32 * 8    # Number of time step
    # simu.input.Na_tot = 2048     # Spatial discretization
    simu.input.OP = OPdq(N0=2000)  # Rotor speed [rpm]
    p = Toyota_Prius.stator.winding.p
    time = linspace(0, 60 / simu.input.OP.N0, num=32 * p, endpoint=False)
    simu.input.time = time
    simu.input.angle = linspace(0, 2 * pi, num=2048, endpoint=False)
    I0 = 250
    felec = p * simu.input.OP.N0 / 60
    rot_dir = simu.machine.stator.comp_mmf_dir()
    Phi0 = 140 * pi / 180
    Ia = I0 * cos(2 * pi * felec * time + 0 * rot_dir * 2 * pi / 3 + Phi0)
    Ib = I0 * cos(2 * pi * felec * time + 1 * rot_dir * 2 * pi / 3 + Phi0)
    Ic = I0 * cos(2 * pi * felec * time + 2 * rot_dir * 2 * pi / 3 + Phi0)
    # simu.input.set_Id_Iq(I0=250/sqrt(2), Phi0=140*pi/180)
    simu.input.Is = array([Ia, Ib, Ic]).transpose()

    # Definition of the magnetic simulation
    # 2 sym + antiperiodicity = 1/4 Lamination
    simu.mag = MagElmer(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=True,
        is_periodicity_t=True,
        FEA_dict=mesh_dict,
        is_get_mesh=True,
        is_save_FEA=True,
    )
    # Stop after magnetic computation
    simu.force = None
    simu.struct = None
    # Run simulation
    outp = Output(simu=simu)
    simu.run()
    # outp.mag.Tem.plot_2D_Data("time", **dict_2D)
    # outp.elec.get_Is().plot_2D_Data("time", "phase", **dict_2D)
    # outp.mag.Tem.plot_2D_Data("time[smallestperiod]", **dict_2D)
    # outp.mag.meshsolution.plot_contour(label="B")
    # outp.mag.meshsolution.plot_contour(label="A")
    # outp.mag.meshsolution.plot_contour(label="J")
    return outp


@pytest.mark.MagElmer
@pytest.mark.long_5s
@pytest.mark.SPMSM
@pytest.mark.SingleOP
@pytest.mark.periodicity
def test_spm_Elmer():
    # Import the machine from a script
    PMSM_A = load(join(DATA_DIR, "Machine", "SPMSM_001.json"))
    PMSM_A.rotor.slot = SlotM10(W1=15e-3, H1=3e-3, H0=0.0, W0=15e-3, Zs=8)
    # PMSM_A.rotor.slot = SlotMFlat(H0=0.0, W0=15e-3, Zs=8)
    # PMSM_A.rotor.slot.magnet = [MagnetType10(W1=15e-3, H1=3e-3)]
    mesh_dict["Lamination_Rotor_Bore_Radius_Ext"] = 20

    # Create the Simulation
    simu = Simu1(name="test_spm_Elmer", machine=PMSM_A)

    # Definition of a sinusoidal current
    simu.input = InputCurrent()
    # simu.input.Id_ref = 0  # [A]
    # simu.input.Iq_ref = 250  # [A]
    # simu.input.Nt_tot = 32 * 8    # Number of time step
    # simu.input.Na_tot = 2048     # Spatial discretization
    simu.input.OP = OPdq(N0=2000)  # Rotor speed [rpm]
    p = PMSM_A.stator.winding.p
    time = linspace(0, 60 / simu.input.OP.N0, num=32 * p, endpoint=False)
    simu.input.time = time
    simu.input.angle = linspace(0, 2 * pi, num=2048, endpoint=False)
    I0 = 150
    felec = p * simu.input.OP.N0 / 60
    rot_dir = simu.machine.stator.comp_mmf_dir()
    Phi0 = 140 * pi / 180
    Ia = I0 * cos(2 * pi * felec * time + 0 * rot_dir * 2 * pi / 3 + Phi0)
    Ib = I0 * cos(2 * pi * felec * time + 1 * rot_dir * 2 * pi / 3 + Phi0)
    Ic = I0 * cos(2 * pi * felec * time + 2 * rot_dir * 2 * pi / 3 + Phi0)
    # simu.input.set_Id_Iq(I0=250/sqrt(2), Phi0=140*pi/180)
    simu.input.Is = array([Ia, Ib, Ic]).transpose()

    # Definition of the magnetic simulation
    # 2 sym + antiperiodicity = 1/4 Lamination
    simu.mag = MagElmer(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=True,
        is_periodicity_t=True,
        FEA_dict=mesh_dict,
        is_get_mesh=False,
        is_save_FEA=False,
    )
    # Stop after magnetic computation
    simu.force = None
    simu.struct = None
    # Run simulation
    outp = Output(simu=simu)
    simu.run()
    outp.mag.Tem.plot_2D_Data("time", **dict_2D)
    # outp.elec.get_Is().plot_2D_Data("time", "phase", **dict_2D)
    # outp.mag.Tem.plot_2D_Data("time[smallestperiod]", **dict_2D)
    # outp.mag.meshsolution.plot_contour(label="B")
    # outp.mag.meshsolution.plot_contour(label="A")
    # outp.mag.meshsolution.plot_contour(label="J")

    return outp


if __name__ == "__main__":
    out = test_ipm_Elmer()
    out = test_spm_Elmer()
