from swat_em import datamodel, plots


def plot_radial(self):
    """Plots the winding radial pattern

    Parameters
    ----------
    self : Winding
        A Winding object

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
    plt = plots._polar_layout_plot(None, None, wdg)
    plt.plot(show=True, optimize_overhang=False)
