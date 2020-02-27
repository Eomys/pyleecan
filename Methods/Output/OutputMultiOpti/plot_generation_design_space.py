import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def plot_generation_design_space(self, dvar1=0, dvar2=1):
    """Plot every individual in the 2D design variable space according to dvar1 and dvar2
    
    Parameters
    ----------
    self : OutputMultiOpti
    dvar1 : int or str
        design variable name or position in the dict to represent
    dvar2 : int or str
        second design variable name or position in the dict to represent
    
    """

    # Check inputs
    if not isinstance(dvar1, int) and not isinstance(dvar1, str):
        raise TypeError("Expecting int or str for dvar1, received", type(dvar1))
    if not isinstance(dvar2, int) and not isinstance(dvar2, str):
        raise TypeError("Expecting int or str for dvar2, received", type(dvar2))

    # Get both objective function index and name
    if isinstance(dvar1, int):
        idx_dvar1 = dvar1
        dvar1 = self.design_var_names[idx_dvar1]
    else:
        dvar1 = self.design_var_names.index(dvar1)
    if isinstance(dvar2, int):
        idx_dvar2 = dvar2
        dvar2 = self.design_var_names[idx_dvar2]
    else:
        dvar2 = self.design_var_names.index(dvar2)

    # TODO define the colormap according to Pyleecan graphical chart
    # Colormap definition
    cm = LinearSegmentedColormap.from_list(
        "colormap",
        [(35 / 255, 89 / 255, 133 / 255), (250 / 255, 202 / 255, 56 / 255)],
        N=max(self.ngen),
    )

    # Get fitness and ngen
    is_valid = np.array(self.is_valid)
    design_var = np.array(self.design_var)
    ngen = np.array(self.ngen)

    # Keep only valid values
    indx = np.where(is_valid)[0]

    design_var = design_var[indx]
    ngen = ngen[indx]
    fig, ax = plt.subplots()

    # Plot fitness values
    scatter = ax.scatter(
        design_var[:, idx_dvar1], design_var[:, idx_dvar2], s=8, c=ngen, cmap=cm
    )
    legend1 = ax.legend(
        *scatter.legend_elements(), loc="upper right", title="Generation"
    )
    ax.add_artist(legend1)
    ax.set_xlabel(dvar1)
    ax.set_ylabel(dvar2)
    ax.set_title("Design variable values for each individual")

    ax.autoscale()
    fig.show()
