# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
from numpy import meshgrid, append, pi, angle as np_angle

# from numpy import amax, argsort, meshgrid, negative, abs, array


def plot_Br_fft2(self, colormap, out_list=[]):
    """Plot the airgap flux as a function of space

    Parameters
    ----------
    self: Output
        an Output object
    Dataobject: Data
        a Data object
    out_list: list
        List of Output objects to compare
    """

    # Display settings
    #    freq_disp_max = 13000
    unitr = "[]"
    unitf = "[Hz]"

    # Extract the field
    [freqs, wavenumber, MTr_mag] = self.mag.Br.get_magnitude_along(
        "freqs=[0,13000]", "wavenumber", unit="dB"
    )

    [freqs, wavenumber, MTr_phase] = self.mag.Br.get_phase_along(
        "freqs=[0,13000]", "wavenumber", unit="°"
    )

    MTr_phase = np_angle(self.mag.Br.values[:657]) * 180 / pi
    MTr_phase = MTr_phase - 90

    wavenumber = append(wavenumber, wavenumber[-1] + 1)
    freqs = append(freqs, freqs[-1] + 1)
    wavenumber_map, freqs_map = meshgrid(wavenumber, freqs)

    # Plot 3D scatter
    fig, axs = plt.subplots(2, 1, constrained_layout=True, figsize=(20, 10))
    c = axs[0].pcolormesh(
        freqs_map, wavenumber_map, MTr_mag, cmap=colormap, vmin=0, vmax=50
    )
    #    ax.scatter(freqs_map, wavenumber_map, MTr_mag, cmap=colormap, marker='s')
    axs[0].set_xlabel("Frequencies " + unitf)
    axs[0].set_ylabel("Wavenumber " + unitr)
    clb = fig.colorbar(c, ax=axs[0])
    clb.ax.set_title("MTr [dB]")

    c = axs[1].pcolormesh(
        freqs_map, wavenumber_map, MTr_phase, cmap=colormap, vmin=-180, vmax=180
    )
    #    ax.scatter(freqs_map, wavenumber_map, MTr_phase, cmap=colormap, marker='s')
    axs[1].set_xlabel("Frequencies " + unitf)
    axs[1].set_ylabel("Wavenumber " + unitr)
    clb = fig.colorbar(c, ax=axs[1])
    clb.ax.set_title("Angle(MTr) [°]")

    title = "FFT2 of radial stress applying on stator"
    fig.canvas.set_window_title(title)
    fig.suptitle(title, fontsize=16)

    fig.show()
