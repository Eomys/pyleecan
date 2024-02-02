from typing import Any, Dict, Optional, Tuple

from pyvista import themes
from pyvista.plotting import BasePlotter, Plotter

from ....definitions import config_dict

FONT_FAMILY_PYVISTA = config_dict["PLOT"]["FONT_FAMILY_PYVISTA"]


def configure_plot(
    pv_plotter: Optional[BasePlotter], win_title: str, is_show_axes: bool = True
) -> Tuple[BasePlotter, Dict[str, Any]]:
    """Configure a pyvista plot. If the plotter doesn't exist, create one depending on available package: PyVista or PyVistaQt.

    Parameters
    ----------
    pv_plotter : pyvista plotter
        a pyvista plotter
    win_title : str
        title of the window
    save_path : str
        path where to save the plot
    """

    if pv_plotter is None:
        # Instantiate pv_plotter
        pv_plotter = Plotter(
            notebook=False, title=win_title, theme=themes.DocumentTheme()
        )

    # isometric view with z towards left
    pv_plotter.view_isometric()

    if is_show_axes:
        pv_plotter.add_axes(
            color="k", x_color="#da3061", y_color="#0069a1", z_color="#bbcf1c"
        )
    sargs = dict(
        interactive=True,
        title_font_size=12,
        label_font_size=10,
        font_family=FONT_FAMILY_PYVISTA,
        color="black",
    )

    return pv_plotter, sargs
