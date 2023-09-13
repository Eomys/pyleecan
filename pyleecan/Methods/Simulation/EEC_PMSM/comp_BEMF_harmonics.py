# -*- coding: utf-8 -*-
from numpy import sqrt, cos, sin, pi
import numpy as np
from SciDataTool import DataLinspace, DataTime
import matplotlib.pyplot as plt


def comp_BEMF_harmonics(Phi_A, Phi_B, Phi_C, delta, time):
    """
    Compute the back electromotive force harmonics from magnet fluxes (PMSM)

    Parameters
    ----------
    Phi_A: Magnetic flux of phase A
    Phi_B: Magnetic flux of phase B
    Phi_C: Magnetic flux of phase C
    delta: Rotor angular position
    time: time vector

    """

    # Park transformation (keep the amplitude factor=2/3)
    Phi_d = (
        2
        / 3
        * (
            Phi_A * cos(delta)
            + Phi_B * cos(delta - 2 * pi / 3)
            + Phi_C * cos(delta + 2 * pi / 3)
        )
    )
    Phi_q = (
        2
        / 3
        * (
            -Phi_A * sin(delta)
            - Phi_B * sin(delta - 2 * pi / 3)
            - Phi_C * sin(delta + 2 * pi / 3)
        )
    )
    Phi_h = 2 / 3 * 1 / 2 * (Phi_A + Phi_B + Phi_C)

    # Create time vector in form of DataLinspace
    time_axis = DataLinspace(
        name="time",
        unit="s",
        initial=0,
        final=time[-1],
        number=len(time),
        include_endpoint=True,
    )

    # Load Phi into DataTime
    Phi_A_data = DataTime(
        name="Phi_A",
        symbol="Phi_A",
        unit="Wb",
        normalizations=None,
        axes=[time_axis],
        values=Phi_A,
    )

    Phi_B_data = DataTime(
        name="Phi_B",
        symbol="Phi_B",
        unit="Wb",
        normalizations=None,
        axes=[time_axis],
        values=Phi_B,
    )
    Phi_C_data = DataTime(
        name="Phi_C",
        symbol="Phi_C",
        unit="Wb",
        normalizations=None,
        axes=[time_axis],
        values=Phi_C,
    )

    Phi_d_data = DataTime(
        name="Phi_d",
        symbol="Phi_d",
        unit="Wb",
        normalizations=None,
        axes=[time_axis],
        values=Phi_d,
    )

    Phi_q_data = DataTime(
        name="Phi_q",
        symbol="Phi_q",
        unit="Wb",
        normalizations=None,
        axes=[time_axis],
        values=Phi_q,
    )
    Phi_h_data = DataTime(
        name="Phi_h",
        symbol="Phi_h",
        unit="Wb",
        normalizations=None,
        axes=[time_axis],
        values=Phi_h,
    )

    # Phi_q_data.plot_2D_Data("time")
    # Phi_q_data.plot_2D_Data("freqs", type_plot='curve')
    # plt.show()

    # Calculate FFT for Phi on the dq0 frame
    d = Phi_d_data.get_along("freqs")
    freqs_d = d["freqs"]
    complx_d = d["Phi_d"]

    q = Phi_q_data.get_along("freqs")
    freqs_q = q["freqs"]
    complx_q = q["Phi_q"]

    h = Phi_h_data.get_along("freqs")
    freqs_h = h["freqs"]
    complx_h = h["Phi_h"]

    # Calculate back-emf (E) on dq0 frame
    E_d = -2 * pi * freqs_q * complx_q + 2 * pi * freqs_d * complx_d * 1j
    E_q = 2 * pi * freqs_d * complx_d + 2 * pi * freqs_q * complx_q * 1j
    E_h = 2 * pi * freqs_h * complx_h * 1j

    return E_d, E_q, E_h, freqs_d, freqs_q, freqs_h


if __name__ == "__main__":
    # Example:
    N = 10000
    # sample spacing
    T = 1.0 / 20000
    time = np.linspace(0.0, N * T, N, endpoint=False)
    Phi_A = (
        0.5 * np.cos(50.0 * 2.0 * np.pi * time)
        + 0.001 * np.cos(100 * 2.0 * np.pi * time)
        + 0.0009 * np.cos(150 * 2.0 * np.pi * time)
    )
    Phi_B = (
        0.5 * np.cos(50.0 * 2.0 * np.pi * time - 2 * pi / 3)
        + 0.001 * np.cos(100 * 2.0 * np.pi * time - 2 * pi / 3)
        + 0.0009 * np.cos(150 * 2.0 * np.pi * time - 2 * pi / 3)
    )
    Phi_C = (
        0.5 * np.cos(50.0 * 2.0 * np.pi * time + 2 * pi / 3)
        + 0.001 * np.cos(100 * 2.0 * np.pi * time + 2 * pi / 3)
        + 0.0009 * np.cos(150 * 2.0 * np.pi * time + 2 * pi / 3)
    )
    delta = 50.0 * 2.0 * np.pi * time

    E_d, E_q, E_h, freqs_d, freqs_q, freqs_h = comp_BEMF_harmonics(
        Phi_A=Phi_A, Phi_B=Phi_B, Phi_C=Phi_C, delta=delta, time=time
    )

    fig, axs = plt.subplots(3)
    axs[0].plot(freqs_d, abs(E_d))
    axs[1].plot(freqs_q, abs(E_q))
    axs[2].plot(freqs_h, abs(E_h))
    plt.show()
