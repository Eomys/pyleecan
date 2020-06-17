import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def plot_generation_design_space(self, dvar1=0, dvar2=1, valid_only=False):
    """Plot every individual in the 2D design variable space according to dvar1 and dvar2
    
    Parameters
    ----------
    self : OutputMultiOpti
    dvar1 : int or str
        design variable name or position in the dict to represent
    dvar2 : int or str
        second design variable name or position in the dict to represent
    valid_only : bool
        bool to only show valid individuals
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
        idx_dvar1 = self.design_var_names.index(dvar1)
    if isinstance(dvar2, int):
        idx_dvar2 = dvar2
        dvar2 = self.design_var_names[idx_dvar2]
    else:
        idx_dvar2 = self.design_var_names.index(dvar2)

    # TODO define the colormap according to Pyleecan graphical chart
    # Colormap definition
    cm = LinearSegmentedColormap.from_list(
        "colormap",
        [(35 / 255, 89 / 255, 133 / 255), (250 / 255, 202 / 255, 56 / 255)],
        N=max(self.ngen) + 1,
    )

    # Get fitness and ngen
    is_valid = np.array(self.is_valid)
    design_var = np.array(self.design_var)
    ngen = np.array(self.ngen)

    # Keep only valid values
    indx_valid = np.where(is_valid)[0]
    design_var_valid = design_var[indx_valid]
    ngen_valid = ngen[indx_valid]
    fig, ax = plt.subplots()

    # Plot design_var_values values
    scatter = ax.scatter(
        design_var_valid[:, idx_dvar1],
        design_var_valid[:, idx_dvar2],
        s=19.5,
        c=ngen_valid,
        cmap=cm,
    )
    handles, labels = scatter.legend_elements()

    if not valid_only:  # Add the not valid individuals
        indx_not_valid = np.where(is_valid == False)
        design_var_not_valid = design_var[indx_not_valid]
        ngen_not_valid = ngen[indx_not_valid]
        colors = cm(ngen_not_valid)
        scatter2 = ax.scatter(
            design_var_not_valid[:, idx_dvar1],
            design_var_not_valid[:, idx_dvar2],
            linewidths=0.5,
            edgecolors="r",  # highlight the failure in red
            alpha=0.9,
            s=20,
            facecolors=colors,
        )
        # Add a custom legend to specify invalid element
        # see https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/custom_legends.html
        handles.extend(
            [
                plt.Line2D(
                    [0],
                    [0],
                    marker="o",
                    color="w",
                    label="Scatter",
                    markerfacecolor="None",
                    markeredgecolor="r",
                    markersize=7,
                ),
            ]
        )
        labels.append("invalid")

    legend1 = ax.legend(
        handles=handles, labels=labels, loc="upper right", title="Generation"
    )
    ax.add_artist(legend1)
    ax.set_xlabel(dvar1)
    ax.set_ylabel(dvar2)
    ax.set_title("Design variable values for each individual")

    ax.autoscale()
    fig.show()
