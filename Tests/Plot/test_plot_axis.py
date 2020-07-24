from os.path import join

import pytest
import matplotlib.pyplot as plt
from numpy import exp, pi, ones, array, zeros
from numpy import argmax, cos, abs as np_abs, angle as np_angle

from pyleecan.definitions import config_dict
from Tests import save_plot_path as save_path
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.InputFlux import InputFlux
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportMatlab import ImportMatlab

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
SCIM_001 = load(join(DATA_DIR, "Machine", "SCIM_001.json"))
SynRM_001 = load(join(DATA_DIR, "Machine", "SynRM_001.json"))
SIPMSM_001 = load(join(DATA_DIR, "Machine", "SIPMSM_001.json"))
CURVE_COLORS = config_dict["PLOT"]["COLOR_DICT"]["CURVE_COLORS"]


def test_axis_LamSlotMag():
    """Axis convention for LamSlot with magnet
    """
    SIPMSM_001.rotor.plot()
    R1 = SIPMSM_001.rotor.Rext * 1.1
    R2 = SIPMSM_001.rotor.Rext * 1.2
    R3 = SIPMSM_001.rotor.Rext * 1.4
    axes = plt.gca()

    # X axis
    Zx = R1
    plt.arrow(0, 0, Zx.real, Zx.imag, color=CURVE_COLORS[0])
    Zlx = R2
    axes.text(Zlx.real, Zlx.imag, "X axis")

    # Y axis
    Zy = R1 * exp(1j * pi / 2)
    plt.arrow(0, 0, Zy.real, Zy.imag, color=CURVE_COLORS[0])
    # Zly = R2 * exp(1j * pi / 2)
    # axes.text(Zly.real, Zly.imag, "Y axis")

    # D axis
    D_axis = SIPMSM_001.rotor.comp_angle_d_axis()
    Zd = R1 * exp(1j * D_axis)
    plt.arrow(0, 0, Zd.real, Zd.imag, color=CURVE_COLORS[1])
    Zld = R2 * exp(1j * D_axis)
    axes.text(Zld.real, Zld.imag, "D axis")

    # Q axis
    Q_axis = SIPMSM_001.rotor.comp_angle_q_axis()
    Zq = R1 * exp(1j * Q_axis)
    plt.arrow(0, 0, Zq.real, Zq.imag, color=CURVE_COLORS[1])
    Zlq = R2 * exp(1j * Q_axis)
    axes.text(Zlq.real, Zlq.imag, "Y & Q axis")

    axes.get_legend().remove()
    axes.set_xlim(-R3, R3)
    axes.set_ylim(-R3, R3)

    # Save and check
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_axis_LamSlotMag.png"))
    assert D_axis == pi / 4
    assert Q_axis == pi / 2


def test_axis_LamHoleMag():
    """Axis convention for LamHole with magnet
    """
    IPMSM_A.rotor.plot()
    R1 = IPMSM_A.rotor.Rext * 1.1
    R2 = IPMSM_A.rotor.Rext * 1.2
    R3 = IPMSM_A.rotor.Rext * 1.4
    axes = plt.gca()

    # X axis
    Zx = R1
    plt.arrow(0, 0, Zx.real, Zx.imag, color=CURVE_COLORS[0])
    Zlx = R2
    axes.text(Zlx.real, Zlx.imag, "X axis")

    # Y axis
    Zy = R1 * exp(1j * pi / 2)
    plt.arrow(0, 0, Zy.real, Zy.imag, color=CURVE_COLORS[0])
    Zly = R2 * exp(1j * pi / 2)
    axes.text(Zly.real, Zly.imag, "Y axis")

    # D axis
    D_axis = IPMSM_A.rotor.comp_angle_d_axis()
    Zd = R1 * exp(1j * D_axis)
    plt.arrow(0, 0, Zd.real, Zd.imag, color=CURVE_COLORS[1])
    Zld = R2 * exp(1j * D_axis)
    axes.text(Zld.real, Zld.imag, "D axis")

    # Q axis
    Q_axis = IPMSM_A.rotor.comp_angle_q_axis()
    Zq = R1 * exp(1j * Q_axis)
    plt.arrow(0, 0, Zq.real, Zq.imag, color=CURVE_COLORS[1])
    Zlq = R2 * exp(1j * Q_axis)
    axes.text(Zlq.real, Zlq.imag, "Q axis")

    axes.get_legend().remove()
    axes.set_xlim(-0.1, R3)
    axes.set_ylim(-0.1, R3)

    # Save and check
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_axis_LamHoleMag.png"))
    assert D_axis == pi / 8
    assert Q_axis == pi / 4


def test_axis_LamHole():
    """Axis convention for LamHole
    """
    SynRM_001.rotor.plot()
    R1 = SynRM_001.rotor.Rext * 1.1
    R2 = SynRM_001.rotor.Rext * 1.2
    R3 = SynRM_001.rotor.Rext * 1.4
    axes = plt.gca()

    # X axis
    Zx = R1
    plt.arrow(0, 0, Zx.real, Zx.imag, color=CURVE_COLORS[0])
    # Zlx = R2
    # axes.text(Zlx.real, Zlx.imag, "X axis")

    # Y axis
    Zy = R1 * exp(1j * pi / 2)
    plt.arrow(0, 0, Zy.real, Zy.imag, color=CURVE_COLORS[0])
    Zly = R2 * exp(1j * pi / 2)
    axes.text(Zly.real, Zly.imag, "Y axis")

    # D axis
    D_axis = SynRM_001.rotor.comp_angle_d_axis()
    Zd = R1 * exp(1j * D_axis)
    plt.arrow(0, 0, Zd.real, Zd.imag, color=CURVE_COLORS[1])
    Zld = R2 * exp(1j * D_axis)
    axes.text(Zld.real, Zld.imag, "D & X axis")

    # Q axis
    Q_axis = SynRM_001.rotor.comp_angle_q_axis()
    Zq = R1 * exp(1j * Q_axis)
    plt.arrow(0, 0, Zq.real, Zq.imag, color=CURVE_COLORS[1])
    Zlq = R2 * exp(1j * Q_axis)
    axes.text(Zlq.real, Zlq.imag, "Q axis")

    axes.get_legend().remove()
    axes.set_xlim(-R3, R3)
    axes.set_ylim(-R3, R3)

    plt.title("Rotor of SynRM")
    # Save and check
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_axis_LamHole.png"))
    assert D_axis == 0
    assert Q_axis == pi / 4


@pytest.mark.FEMM
@pytest.mark.long
def test_axis_LamWind():
    """Axis convention for LamWind
    """
    SCIM_001.stator.plot()
    R1 = SCIM_001.stator.Rext * 1.1
    R2 = SCIM_001.stator.Rext * 1.2
    R3 = SCIM_001.stator.Rext * 1.4
    axes = plt.gca()

    # X axis
    Zx = R1
    plt.arrow(0, 0, Zx.real, Zx.imag, color=CURVE_COLORS[0])
    Zlx = R2
    axes.text(Zlx.real, Zlx.imag, "X axis")

    # Y axis
    Zy = R1 * exp(1j * pi / 2)
    plt.arrow(0, 0, Zy.real, Zy.imag, color=CURVE_COLORS[0])
    Zly = R2 * exp(1j * pi / 2)
    axes.text(Zly.real, Zly.imag, "Y axis")

    # D axis
    D_axis = SCIM_001.stator.comp_angle_d_axis()
    assert D_axis == pytest.approx(1.6577, rel=0.01)
    Zd = R1 * exp(1j * D_axis)
    plt.arrow(0, 0, Zd.real, Zd.imag, color=CURVE_COLORS[1])
    Zld = R2 * exp(1j * D_axis)
    axes.text(Zld.real - 0.1, Zld.imag, "D axis")

    # Q axis
    Q_axis = SCIM_001.stator.comp_angle_q_axis()
    Zq = R1 * exp(1j * Q_axis)
    plt.arrow(0, 0, Zq.real, Zq.imag, color=CURVE_COLORS[1])
    Zlq = R2 * exp(1j * Q_axis)
    axes.text(Zlq.real, Zlq.imag, "Q axis")

    axes.get_legend().remove()
    axes.set_xlim(-R3, R3)
    axes.set_ylim(-R3, R3)

    # Save and check
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_axis_LamWind.png"))

    SCIM_001.stator.plot_mmf_unit()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_axis_LamWind_mmf.png"))

    # Plot maximum of the fundamental of the mmf
    MMF = SCIM_001.stator.comp_mmf_unit()
    p = SCIM_001.stator.get_pole_pair_number()
    results = MMF.get_along("angle")
    angle_rotor = results["angle"]
    mmf_angle = results[MMF.symbol]
    results = MMF.get_along("wavenumber")
    wavenumber = results["wavenumber"]
    mmf_ft = results[MMF.symbol]

    # Find the angle where the FFT is max
    indr_fund = np_abs(wavenumber - p).argmin()
    phimax = np_angle(mmf_ft[indr_fund])
    magmax = np_abs(mmf_ft[indr_fund])
    mmf_waveform = magmax * cos(p * angle_rotor + phimax)
    ind_max = argmax(mmf_waveform)
    d_angle = angle_rotor[ind_max]
    (sym, _) = SCIM_001.stator.comp_sym()
    d_angle = d_angle % (2 * pi / sym)

    fig = plt.figure("MMF fundamental")
    plt.plot(angle_rotor, mmf_angle)
    plt.plot(angle_rotor, mmf_waveform)
    plt.plot(d_angle, mmf_waveform[ind_max], "rx")
    plt.text(
        d_angle,
        mmf_waveform[ind_max] * 1.1,
        "Max at " + format(d_angle, ".5g") + " rad",
    )

    fig.savefig(join(save_path, "test_axis_LamWind_fund.png"))

    simu = Simu1(name="test_flux", machine=SCIM_001)

    # Definition of the enforced output of the electrical module
    Nr = ImportMatrixVal(value=ones(1) * 1500)
    Is = ImportMatrixVal(value=array([[1, -1 / 2, -1 / 2]]))  # Id=1, Iq=0
    Ir = ImportMatrixVal(value=zeros((1, 28)))
    time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=False)
    angle = ImportGenVectLin(start=0, stop=2 * pi, num=4096, endpoint=False)

    simu.input = InputCurrent(
        Is=Is,
        Ir=Ir,  # zero current for the rotor
        Nr=Nr,
        angle_rotor=None,  # Will be computed
        time=time,
        angle=angle,
        angle_rotor_initial=0,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        is_mmfr=False,
        type_BH_stator=2,
        type_BH_rotor=2,
        is_symmetry_a=False,
        is_antiper_a=False,
    )
    simu.force = None
    simu.struct = None

    out = Output(simu=simu)
    simu.run()

    plt.close("all")
    out.plot_B_space(is_deg=False)
    fig = plt.gcf()
    fig.axes[0].plot(d_angle, max(max(out.mag.Br.values)), "rx")
    fig.axes[0].text(d_angle, max(max(out.mag.Br.values)), "Max of mmf")
    fig.savefig(join(save_path, "test_axis_LamWind_flux.png"))
