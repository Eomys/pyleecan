from swat_em import datamodel, plots
from swat_em.config import config

from ....definitions import config_dict


def plot_radial(self, is_show_fig=True):
    """Plots the winding radial pattern

    Parameters
    ----------
    self : Winding
        A Winding object
    is_show_fig : bool
        True to call fig.show

    """
    Zs = self.parent.get_Zs()

    p = self.parent.get_pole_pair_number()

    # generate a datamodel for the winding
    wdg = datamodel()

    # generate winding from inputs
    wdg.genwdg(
        Q=Zs,
        P=2 * p,
        m=self.qs,
        layers=self.Nlayer,
        turns=self.Ntcoil,
        w=self.coil_pitch,
    )
    if (
        not isinstance(config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"][0], str)
        and len(config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"][0]) == 4
    ):  # rgba to hex
        config["plt"]["phase_colors"] = [
            "#{:02x}{:02x}{:02x}".format(
                int(color[0] * 255 * (1 - color[3]) + 255 * color[3]),
                int(color[1] * 255 * (1 - color[3]) + 255 * color[3]),
                int(color[2] * 255 * (1 - color[3]) + 255 * color[3]),
            )
            for color in config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]
        ]
    else:
        config["plt"]["phase_colors"] = config_dict["PLOT"]["COLOR_DICT"][
            "PHASE_COLORS"
        ]
    plt = plots._polar_layout_plot(None, None, wdg)
    plt.plot(show=is_show_fig, optimize_overhang=False)
