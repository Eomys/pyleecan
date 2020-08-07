
from numpy import pi, zeros
from os.path import join
import matplotlib.pyplot as plt
from numpy.testing import assert_almost_equal

from Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1


from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportGenMatrixSin import ImportGenMatrixSin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal

from pyleecan.Classes.EEC_PMSM import EEC_PMSM
from pyleecan.Classes.FluxLinkFEMM import FluxLinkFEMM
from pyleecan.Classes.IndMagFEMM import IndMagFEMM
from pyleecan.Classes.DriveWave import DriveWave
from pyleecan.Classes.Output import Output
import pytest
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_E_IPMSM_FL_002():
    """Validation of the PMSM Electrical Equivalent Circuit with the Prius machine
    """

    simu = Simu1(name="E_IPMSM_FL_002", machine=IPMSM_A)
    
    # Definition of the enforced output of the electrical module
    freq0 = 50
    zp = IPMSM_A.stator.get_pole_pair_number()
    N0 = 60 * freq0 / zp
    
    time = ImportGenVectLin(start=0, stop=1, num=2048, endpoint=False)
    angle = ImportGenVectLin(start=0, stop=2 * pi, num=2048, endpoint=False)
    
    Is_mat = zeros((2048, 3))
    Is = ImportMatrixVal(value=Is_mat)
    
    drive = ImportGenMatrixSin()
    drive.init_vector(
        f=[freq0, freq0, freq0],
        A=[220, 220, 220],
        Phi=[0, -2*pi / 3, -4*pi / 3],
        N=2048,
        Tf=1,
    )
    
    simu.input = InputCurrent(
        Is=Is,
        Ir=None,
        N0=N0,
        angle_rotor=None,  # Will be computed
        time=time,
        angle=angle,
        angle_rotor_initial=0.86,
    )
    
    # Definition of the electrical simulation (FEMM)
    simu.elec.eec = EEC_PMSM(
        indmag=IndMagFEMM(is_symmetry_a=True, sym_a=4, is_antiper_a=True, Nt_tot=3),
        fluxlink=FluxLinkFEMM(is_symmetry_a=True, sym_a=4, is_antiper_a=True, Nt_tot=3),
        drive=DriveWave(wave=drive),
    )
    
    simu.mag = None
    simu.force = None
    simu.struct = None
    
    out = Output(simu=simu)
    simu.run()
    
    # TODO Check Id and Iq
    # Id_ref = ?
    # Iq_ref = ?
    # assert_almost_equal(out.elec.Id_ref, Id_ref, decimal=2)
    # assert_almost_equal(out.elec.Iq_ref, Iq_ref, decimal=2)
    
    # Plot the currents as a function of time
    plt.close("all")
    out.plot_A_time(
        "elec.Currents",
        index_list=[0, 1, 2],
        save_path=join(save_path, "test_E_IPMSM_FL_002_currents.png"),
    )
