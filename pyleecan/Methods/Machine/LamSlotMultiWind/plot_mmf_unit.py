from ....Functions.Load.import_class import import_class


def plot_mmf_unit(self, r_max=100, fig=None, save_path=None, is_show_fig=True):
    """Plot the winding unit mmf as a function of space
    Parameters
    ----------

    self : LamSlotMultiWind
        an LamSlotMultiWind object
    Na : int
        Space discretization
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    is_show_fig : bool
        To call show at the end of the method
    """

    # Call method of LamSlotWind
    LamSlotWind = import_class("pyleecan.Classes", "LamSlotWind")

    LamSlotWind.plot_mmf_unit(
        self, r_max=r_max, fig=fig, save_path=save_path, is_show_fig=is_show_fig
    )
