from numpy import ones, pi, array
from os.path import join
import matplotlib.pyplot as plt
from ....Tests import save_validation_path as save_path

from ....Classes.Simu1 import Simu1

from ....Classes.InputCurrent import InputCurrent
from ....Classes.InputFlux import InputFlux
from ....Classes.ImportGenVectLin import ImportGenVectLin
from ....Classes.ImportMatrixVal import ImportMatrixVal
from ....Classes.ImportMatlab import ImportMatlab

from ....Classes.MagFEMM import MagFEMM
from ....Classes.Output import Output
from ....Tests import DATA_DIR
from ....Tests.Validation.Machine.SIPMSM_001 import SIPMSM_001


def test_Magnetic_FEMM_sym():
    """Validation of a polar SIPMSM with inset magnet
    Armature load (magnet field canceled by is_mmfr=False)

    from publication
    A. Rahideh and T. Korakianitis,
    “Analytical Magnetic Field Calculation of Slotted Brushless Permanent-Magnet Machines With Surface Inset Magnets,”
    vol. 48, no. 10, pp. 2633–2649, 2012.
    Test compute the Flux in FEMM, with and without symmetry
    and with MANATEE semi-analytical subdomain model
    """
    simu = Simu1(name="EM_SIPMSM_AL_001", machine=SIPMSM_001)

    # Definition of the enforced output of the electrical module
    Nr = ImportMatrixVal(value=ones(2) * 150)
    Is = ImportMatrixVal(
        value=array([[14.1421, -7.0711, -7.0711], [-14.1421, 7.0711, 7.0711]])
    )
    time = ImportGenVectLin(start=0, stop=0.1, num=2, endpoint=True)
    angle = ImportGenVectLin(start=0, stop=2 * pi, num=1024, endpoint=False)

    Ar = ImportMatrixVal(value=array([2.5219, 0.9511]) + pi / 6)
    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        Nr=None,
        angle_rotor=Ar,  # Will be computed
        time=time,
        angle=angle,
        angle_rotor_initial=0,
    )

    # Definition of the magnetic simulation (is_mmfr=False => no flux from the magnets)
    simu.mag = MagFEMM(
        is_stator_linear_BH=2,
        is_rotor_linear_BH=2,
        is_symmetry_a=False,
        is_mmfr=False,
        angle_stator=-pi / 6,
    )
    simu.struct = None
    # Just load the Output and ends (we could also have directly filled the Output object)
    simu_load = Simu1(init_dict=simu.as_dict())
    simu_load.mag = None
    mat_file = join(DATA_DIR, "EM_SIPMSM_AL_001_MANATEE_SDM.mat")
    Br = ImportMatlab(file_path=mat_file, var_name="XBr")
    Bt = ImportMatlab(file_path=mat_file, var_name="XBt")
    simu_load.input = InputFlux(time=time, angle=angle, Br=Br, Bt=Bt)

    out = Output(simu=simu)
    out.post.legend_name = "No symmetry"
    simu.run()

    out3 = Output(simu=simu_load)
    out3.post.legend_name = "MANATEE SDM"
    out3.post.line_color = "g--"
    simu_load.run()

    # Plot the result by comparing the two simulation (no sym / MANATEE SDM)
    plt.close("all")
    out.plot_B_space(out_list=[out3])

    fig = plt.gcf()
    fig.savefig(join(save_path, "test_EM_SIPMSM_AL_001_SDM.png"))
