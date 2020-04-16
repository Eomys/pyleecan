# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from ......Functions.Plot.plot_A_2D import plot_A_2D


def plot_ASWL(self, ASWL, is_dBA=False, out_list=[]):
    """Plot the airgap flux as a function of space

    Parameters
    ----------
    self: Output
        an Output object
    Dataobject: Data
        a Data object
    j_t0: int
        Index of the time vector to plot
    is_deg: bool
        True to plot in degree, False in rad
    out_list: list
        List of Output objects to compare
    """

    # Set fft plot
    freq_max = 25000

    # Set plot
    fig = plt.figure(constrained_layout=True, figsize=(20, 10))
    title = "Time signal"
    xlabel = "Time [s]"
    ylabel = "Sound [" + ASWL.unit + "]"

    # Extract the field
    if is_dBA:
        unitA = "dBA"
    else:
        unitA = "dB"
    [time, ASWL_time] = ASWL.get_along("time=[0,0.1]")
    [freqs, ASWL_FT] = ASWL.get_magnitude_along("freqs=[0," + str(freq_max) + "]")
    [freq_oct, ASWL_oct] = ASWL.get_nthoctave(3, 0, freq_max, unit=unitA)

    # Plot the original graph
    plot_A_2D(
        time,
        [ASWL_time],
        is_newfig=False,
        fig=fig,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
    )

    xlabel = "Frequency [Hz]"
    ylabel = "Sound [" + unitA + "]"
    title = "FFT"
    plot_A_2D(
        freqs,
        [ASWL_FT],
        is_newfig=False,
        fig=fig,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        type="bargraph",
    )

    title = "FFT in 1/3 octave base"
    plot_A_2D(
        freq_oct,
        [ASWL_oct],
        is_newfig=False,
        fig=fig,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        type="barchart",
    )

    title = "A-weighted sound power level spectra"
    fig.canvas.set_window_title(title)
    fig.suptitle(title, fontsize=16)
