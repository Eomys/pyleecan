import matplotlib.pyplot as plt
from os.path import join
from pyleecan.Functions.Plot import dict_2D


def plot_save(output):
    """Save the machine and force of the simulation"""

    fig = plt.figure(figsize=(8, 8))
    ax0 = fig.add_subplot(2, 1, 1)

    # Plot machine
    output.simu.machine.plot(sym=8, ax=ax0, fig=fig, is_show_fig=False)
    ax0.set_xlim(0, 0.130)
    ax0.set_ylim(0, 0.1)
    ax0.set_axis_off()
    ax0.set_title(None)

    # Plot forces
    ax2 = fig.add_subplot(2, 1, 2)
    output.force.AGSF.plot_2D_Data(
        "freqs->elec_order",
        "wavenumber=0",
        component_list=["radial"],
        ax=ax2,
        fig=fig,
        y_min=0,
        y_max=360000,
        is_show_fig=False,
        **dict_2D
    )
    # fig, (ax1, ax2) = plt.subplots(2)
    # # Plot machine
    # output.simu.machine.plot(fig=fig, ax=ax1, is_show_fig=False)
    # ax1.set_axis_off()
    # # Plot forces
    # output.force.AGSF.plot_2D_Data(
    #     "freqs->elec_order",
    #     "wavenumber=0",
    #     fig=fig,
    #     ax=ax2,
    #     is_show_fig=False,
    #     **dict_2D
    # )
    # Set title and save
    if output.simu.index is not None:
        plt.title(
            "Simulation W0="
            + format(output.simu.machine.stator.slot.W0, ".4g")
            + " N0="
            + format(output.simu.input.OP.N0, ".4g"),
            fontsize=20,
        )
        fig.savefig(
            join(
                output.get_path_result(),
                "machine_W0="
                + format(output.simu.machine.stator.slot.W0, ".4g")
                + "_N0="
                + format(output.simu.input.OP.N0, ".4g")
                + ".png",
            ),
            dpi=100,
        )
    else:  # Reference
        plt.title(
            "Reference Simulation",
            fontsize=20,
        )
        fig.savefig(join(output.get_path_result(), "machine_ref.png"), dpi=100)
    plt.close()  # Close after save
