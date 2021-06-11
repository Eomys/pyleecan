from os import getcwd, remove
from os.path import isdir, isfile, join

import matplotlib.pyplot as plt
from numpy import array, cos, exp, linspace, ones, pi, sin, sqrt, zeros
from pyleecan.Classes.CondType21 import CondType21
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.LamSquirrelCageMag import LamSquirrelCageMag
from pyleecan.Classes.MachineLSPM import MachineLSPM
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingSC import WindingSC
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.Shaft import Shaft
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load
from Tests import save_plot_path as save_path


def test_plot_LSPM():
    """Define and Plot the LSPM machine"""
    LSPM = MachineLSPM(name="LSPM_001")

    Copper1 = load(join(DATA_DIR, "Material", "Copper1.json"))
    M400_50A = load(join(DATA_DIR, "Material", "M400-50A.json"))
    MagnetPrius = load(join(DATA_DIR, "Material", "MagnetPrius.json"))

    mm = 1e-3  # Millimeter

    # Stator Lamination setup
    stator = LamSlotWind(
        Rint=132.5 * mm,  # internal radius [m]
        Rext=200 * mm,  # external radius [m]
        L1=350
        * mm,  # Lamination stack active length [m] without radial ventilation airducts
        # but including insulation layers between lamination sheets
        Nrvd=0,  # Number of radial air ventilation duct
        Kf1=0.95,  # Lamination stacking / packing factor
        is_internal=False,
        is_stator=True,
    )

    # Stator Slot setup
    stator.slot = SlotW10(
        Zs=48,  # Slot number
        H0=1.0 * mm,  # Slot isthmus height
        H1=1 * mm,  # Height
        H2=30 * mm,  # Slot height below wedge
        W0=12 * mm,  # Slot isthmus width
        W1=14 * mm,  # Slot top width
        W2=12 * mm,  # Slot bottom width
    )

    # rotor winding setup
    stator.winding = Winding(
        qs=3,  # number of phases
        Lewout=0,  # staight length of conductor outside lamination before EW-bend
        p=2,  # number of pole pairs
        Ntcoil=9,  # number of turns per coil
        Npcp=1,  # number of parallel circuits per phase
        Nslot_shift_wind=0,
        is_reverse_wind=False,
    )

    # rotor Lamination setup
    rotor = LamSquirrelCageMag(
        Rint=45 * mm,
        Rext=131 * mm,
        is_internal=True,
        is_stator=False,
        L1=stator.L1,
        Hscr=20 * mm,
        Lscr=15 * mm,
        ring_mat=Copper1,
    )

    # rotor magnets setup
    rotor.hole = list()
    rotor.hole.append(
        HoleM52(Zh=4, W0=60 * mm, H0=25 * mm, H1=20 * mm, H2=0 * mm, W3=15 * mm)
    )
    rotor.hole[0].magnet_0.mat_type = MagnetPrius
    rotor.hole[0].magnet_0.type_magnetization = 1

    # rotor slot Setup
    rotor.slot = SlotW21(
        Zs=28,  # Slot number
        H0=3.0 * mm,  # Slot isthmus height
        H1=0 * mm,
        H2=15 * mm,  # Slot height below wedge
        W0=3 * mm,  # Slot isthmus width
        W1=13 * mm,
        W2=10 * mm,  # Slot bottom width
    )

    # squirrel cage Setup
    rotor.winding = WindingSC(
        is_reverse_wind=False,
        Nslot_shift_wind=0,
        qs=14,
        Ntcoil=1,
        Npcp=1,
        type_connection=0,
        p=3,
        Lewout=17 * mm,
        conductor=-1,
        init_dict=None,
        init_str=None,
    )

    # Squirrel Cage Conductor bars Setup
    rotor.winding.conductor = CondType21(
        Hbar=20 * mm,
        Wbar=10 * mm,
        Wins=0,
        cond_mat=-1,
        ins_mat=-1,
        init_dict=None,
        init_str=None,
    )
    # material setup
    stator.mat_type = M400_50A  # Stator Lamination material
    rotor.mat_type = M400_50A  # Rotor Lamination material
    stator.winding.conductor.cond_mat = Copper1  # Stator winding conductor material

    LSPM.stator = stator
    LSPM.rotor = rotor
    LSPM.shaft = Shaft(Drsh=rotor.Rint * 2)
    # LSPM.save(join(DATA_DIR, "Machine", "LSPM_001.json"))
    LSPM.plot(is_show_fig=False, save_path=join(save_path, "test_LSPM.png"))


if __name__ == "__main__":
    test_plot_LSPM()
