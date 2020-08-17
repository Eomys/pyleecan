from os import chdir

chdir("../../..")

from numpy import zeros, ones, pi, array
from os.path import join
import matplotlib.pyplot as plt
from Tests import save_validation_path as save_path
from Tests import TEST_DATA_DIR
from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.DXFImport import DXFImport
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Output import Output
import pytest
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_():
    """Validation of the TOYOTA Prius 2004 interior magnet (V shape) with distributed winding
    50 kW peak, 400 Nm peak at 1500 rpm from publication

    from publication
    Z. Yang, M. Krishnamurthy and I. P. Brown,
    "Electromagnetic and vibrational characteristic of IPM over full torque-speed range,"
    Electric Machines & Drives Conference (IEMDC), 2013 IEEE International, Chicago, IL, 2013, pp. 295-302.
    Test compute the Flux in FEMM, with and without DXF Import
    """
IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))

simu = Simu1(name="DXF_import", machine=IPMSM_A)

# Definition of the magnetic simulation (FEMM with symmetry and sliding band)
simu.mag = MagFEMM(
    type_BH_stator=0,
    type_BH_rotor=0,
    is_symmetry_a=True,
    sym_a=4,
    is_antiper_a=True,
    Kgeo_fineness=0.75,
)
# Run only Magnetic module
simu.force = None
simu.struct = None

simu.input = InputCurrent()
simu.input.Id_ref = -100  # [A]
simu.input.Iq_ref = 200  # [A]
simu.input.Nt_tot = 1  # Number of time step
simu.input.Na_tot = 2048  # Spatial discretization
simu.input.N0 = 2000  # Rotor speed [rpm]
simu.input.rot_dir = 1  # To enforce the rotation direction

# DXF import setup
simu.mag.rotor_dxf = DXFImport(
    file_path=join(TEST_DATA_DIR, "prius_test.dxf").replace("\\", "/")
)
# Set each surface name
surf_dict = dict()
surf_dict[0.0546 + 1j * 0.0224] = "Lamination_Rotor_Bore_Radius_Ext"
surf_dict[0.0763 + 0.00867j] = "Hole_Rotor_R0_T0_S0"
surf_dict[0.0669 + 0.01668j] = "HoleMagnet_Rotor_Parallel_N_R0_T0_S0"
surf_dict[0.0614 + 0.0254j] = "Hole_Rotor_R0_T1_S0"
surf_dict[0.0591 + 0.03555j] = "HoleMagnet_Rotor_Parallel_N_R0_T1_S0"
surf_dict[0.06009 + 0.0478j] = "Hole_Rotor_R0_T2_S0"
simu.mag.rotor_dxf.surf_dict = surf_dict
# Set every BC
BC_list = list()
BC_list.append((0.0489 + 1j * 0.0489, False, "bc_r1"))
BC_list.append((0, True, "bc_A0"))
BC_list.append((0.067, False, "bc_r1"))
simu.mag.rotor_dxf.BC_list = BC_list

# Run DXF simulation
out = simu.run()

# Run Normal simulation
simu2 = simu.copy()
simu2.mag.rotor_dxf = None
out2 = simu2.run()

# Plot/compare the flux
out.plot_A_space(
    "mag.B",
    data_list=[out2.mag.B],
    color_list=["k", "r"],
    legend_list=["Rotor from DXF", "Rotor from pyleecan"],
)
fig = plt.gcf()
fig.savefig(join(save_path, "test_DXF_Import.png"))
