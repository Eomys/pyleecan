import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def plot_generation(self, x_symbol, y_symbol, ax=None):
    """Plot every fitness values according to the two fitness

    Parameters
    ----------
    self : XOutput
    obj1 : str
        symbol of the ParamExplorer or the DataKeeper
    obj2 : str
        symbol of the ParamExplorer or the DataKeeper
    """

    # TODO define the colormap according to Pyleecan graphical chart
    # Colormap definition
    cm = LinearSegmentedColormap.from_list(
        "colormap",
        [(35 / 255, 89 / 255, 133 / 255), (250 / 255, 202 / 255, 56 / 255)],
        N=max(self["ngen"].result) + 1,
    )

    # Get fitness and ngen
    is_valid = np.array(self["is_valid"].result)
    ngen = np.array(self["ngen"].result)

    # Keep only valid values
    indx = np.where(is_valid)[0]

    ngen = ngen[indx]

    # Get x_data
    if x_symbol in self.keys():  # DataKeeper
        x_data = self[x_symbol]
        x_values = np.array(x_data.result)[indx]
    else:  # ParamSetter
        x_data = self.get_paramexplorer(x_symbol)
        x_values = np.array(x_data.value)[indx]

    # x_label definition
    x_label = x_symbol
    if x_data.unit not in ["", None]:
        x_label += " [{}]".format(x_data.unit)

    # Get y_data
    if y_symbol in self.keys():  # DataKeeper
        y_data = self[y_symbol]
        y_values = np.array(y_data.result)[indx]
    else:  # ParamSetter
        y_data = self.get_paramexplorer(y_symbol)
        y_values = np.array(y_data.value)[indx]

    # y_label definition
    y_label = y_symbol
    if y_data.unit not in ["", None]:
        y_label += " [{}]".format(y_data.unit)

    if ax is None:
        fig, ax = plt.subplots()

        # Plot fitness values
        scatter = ax.scatter(x_values, y_values, s=8, c=ngen, cmap=cm)

        # Add legend
        legend1 = ax.legend(
            *scatter.legend_elements(), loc="upper right", title="Generation"
        )
        ax.add_artist(legend1)

        # Extend xlim to give some space to the legend
        left, right = ax.get_xlim()
        ax.set_xlim(left, right + 0.2 * abs(right - left))

        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title("Fitness values for each individual")
        fig.show()

    else:
        # Plot fitness values
        scatter = ax.scatter(x_values, y_values, s=8, c=ngen, cmap=cm)

        # Add legend
        legend1 = ax.legend(
            *scatter.legend_elements(), loc="upper right", title="Generation"
        )
        ax.add_artist(legend1)

        # Extend xlim to give some space to the legend
        left, right = ax.get_xlim()
        ax.set_xlim(left, right + 0.2 * abs(right - left))

        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title("Fitness values for each individual")

        return ax
