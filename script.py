# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath, normpath, join

sys.path.insert(0, normpath(abspath(join(dirname(__file__), ".."))))
sys.path.insert(0, normpath(abspath(dirname(__file__))))

from pyleecan.Classes.import_all import *

from numpy import pi, linspace, exp, cos, sin, array, sqrt, zeros, ones
import matplotlib.pyplot as plt

from Tests.Validation.Machine.SCIM_001 import SCIM_001
from Tests.Validation.Machine.SynRM_001 import SynRM_001

from Tests.Validation.Machine.IPMSM_A import IPMSM_A
from pyleecan.Functions.load import load


if __name__ == "__main__":
    IPMSM_A.frame = Frame(Rint=IPMSM_A.stator.Rext, Rext=IPMSM_A.stator.Rext + 0.02)
    IPMSM_A.plot()
    plt.show()
    # lam = LamSlot(is_internal=True, Rint=0, Rext=0.1325)
    # lam.slot = SlotCirc(Zs=6, H0=25e-3, W0=30e-3)
    # surf = lam.slot.build_geometry_wind(Nrad=1, Ntan=1)
    # lam.plot()
    # fig = plt.gcf()
    # surf[0].plot(fig=fig)

    # plt.show()
    # print(IPMSM_A.comp_initial_angle())

    # stator = LamSlotWind(
    #     Rint=0.1325,
    #     Rext=0.2,
    #     Nrvd=0,
    #     L1=0.35,
    #     Kf1=0.95,
    #     is_internal=False,
    #     is_stator=True,
    # )
    # stator.slot = SlotW10(
    #     Zs=36, H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3
    # )
    # stator.winding = WindingDW2L(
    #     qs=3, Lewout=15e-3, p=3, coil_pitch=5, Ntcoil=7, Npcpp=2
    # )
    # stator.plot_mmf_unit()
    # plt.show()

    # simu = Simu1(name="EM_IPMSM_FL_002", machine=IPMSM_A)

    # # Definition of the enforced output of the electrical module
    # Nr = ImportMatrixVal(value=ones(1) * 2504)
    # Is_mat = zeros((1, 3))
    # Is_mat[0, :] = array([0, 12.2474, -12.2474])
    # Is = ImportMatrixVal(value=Is_mat)
    # time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=False)
    # angle = ImportGenVectLin(start=0, stop=2 * pi, num=2048, endpoint=False)

    # simu.input = InputCurrent(
    #     Is=Is,
    #     Ir=None,  # No winding on the rotor
    #     Nr=Nr,
    #     angle_rotor=None,  # Will be computed
    #     time=time,
    #     angle=angle,
    #     angle_rotor_initial=0.86,
    # )

    # # Definition of the magnetic simulation (no symmetry)
    # simu.mag = MagFEMM(
    #     type_BH_stator=0,
    #     type_BH_rotor=0,
    #     is_symmetry_a=False,
    #     is_antiper_a=True,
    #     Kgeo_fineness=0.75,
    # )
    # simu.struct = None
    # # simu.struct.force = ForceMT()
    # # Copy the simu and activate the symmetry
    # simu_sym = Simu1(init_dict=simu.as_dict())
    # simu_sym.mag.is_symmetry_a = True
    # simu_sym.mag.sym_a = 4
    # simu_sym.mag.is_antiper_a = True
    # simu_sym.struct = None

    # out2 = Output(simu=simu_sym)
    # out2.post.legend_name = "1/2 symmetry"
    # out2.post.line_color = "r--"
    # simu_sym.run()
