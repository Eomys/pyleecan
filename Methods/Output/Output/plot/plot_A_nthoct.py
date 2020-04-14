# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pyleecan.Functions.Plot.plot_A_2D import plot_A_2D


def plot_A_nthoct(
    self, Data_str, n, freq_max=10000, is_norm=False, unit="SI", out_list=[],
):
    """Plots a field as a function of time

    Parameters
    ----------
    self : Output
        an Output object
    Data_str : str
        name of the Data Object to plot (e.g. "mag.Br")
    n : int
        fraction of octave band
    freq_max : int
        maximum frequency to be displayed
    is_norm : bool
        boolean indicating if the field must be normalized
    unit : str
        unit in which to plot the field
    out_list : list
        list of Output objects to compare
    """

    # Get Data object names
    Phys = getattr(self, Data_str.split(".")[0])
    A = getattr(Phys, Data_str.split(".")[1])
    B_list = []
    for out in out_list:
        Phys = getattr(out, Data_str.split(".")[0])
        B_list.append(getattr(Phys, Data_str.split(".")[1]))

    # Set plot
    fig = plt.figure(tight_layout=True, figsize=(20, 10))
    legend_list = [self.post.legend_name]
    for out in out_list:
        legend_list.append(out.post.legend_name)
    color_list = [self.post.line_color]
    for out in out_list:
        color_list.append(out.post.line_color)
    xlabel = "Frequency [Hz]"
    if unit == "SI":
        unit = A.unit
    if is_norm:
        ylabel = r"$\frac{" + A.symbol + "}{" + A.symbol + "_0}\, [" + unit + "]$"
    else:
        ylabel = r"$" + A.symbol + "\, [" + unit + "]$"

    (freq_oct, A_oct) = self.get_nthoctave(n, 0, freq_max, unit=unit)

    title = "FFT of " + A.name + " in 1/" + str(n) + " octave base"

    # Plot the original graph
    plot_A_2D(
        freq_oct,
        [A_oct],
        is_newfig=False,
        fig=fig,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        type="barchart",
    )
