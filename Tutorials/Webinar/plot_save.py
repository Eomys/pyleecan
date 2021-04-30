import matplotlib.pyplot as plt
from os.path import join


def plot_save(output):
    """Save the machine and torque of the simulation"""

    # Plot machine
    output.simu.machine.plot()
    # Figure cleanup
    fig = plt.gcf()
    plt.axis("off")
    plt.gca().get_legend().remove()
    fig.set_size_inches(20, 20)
    # Set title and save
    if output.simu.index is not None:
        plt.title(
            "Simulation "
            + str(output.simu.index)
            + " Tem_av="
            + format(output.mag.Tem_av, ".4g"),
            fontsize=40,
        )
        fig.savefig(
            join(
                output.get_path_result(),
                "machine_" + format(output.simu.index, "04d") + ".png",
            ),
            dpi=100,
        )
    else:  # Reference
        plt.title(
            "Reference Simulation Tem_av=" + format(output.mag.Tem_av, ".4g"),
            fontsize=40,
        )
        fig.savefig(join(output.get_path_result(), "machine_ref.png"), dpi=100)
