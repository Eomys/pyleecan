from ....definitions import config_dict

FONT_FAMILY_PYVISTA = config_dict["PLOT"]["FONT_FAMILY_PYVISTA"]


def configure_plot(p, win_title, save_path):
    """Configure a pyvista plot. If the plotter doesn't exist, create one depending on avaialble package.

    Parameters
    ----------
    p : pyvista plotter
        a pyvista plotter
    win_title : str
        title of the window
    save_path : str
        path where to save the plot
    """

    if p is None:
        # Configure plot
        if save_path is None:
            try:
                import pyvistaqt as pv

                is_pyvistaqt = True
            except:
                import pyvista as pv

                is_pyvistaqt = False
        else:
            import pyvista as pv

            is_pyvistaqt = False

        if is_pyvistaqt:
            p = pv.BackgroundPlotter(title=win_title)
            p.set_background("white")
        else:
            pv.set_plot_theme("document")
            p = pv.Plotter(notebook=False, title=win_title)

    # isometric view with z towards left
    p.view_isometric()
    # p.camera_position = [
    #     p.camera_position[0],
    #     (
    #         p.camera_position[1][0],
    #         p.camera_position[1][2],
    #         p.camera_position[1][0],
    #     ),
    #     (
    #         p.camera_position[2][1],
    #         p.camera_position[2][2],
    #         p.camera_position[2][0],
    #     ),
    # ]

    p.add_axes(color="k", x_color="#da3061", y_color="#0069a1", z_color="#bbcf1c")

    sargs = dict(
        interactive=True,
        title_font_size=12,
        label_font_size=10,
        font_family=FONT_FAMILY_PYVISTA,
        color="black",
    )

    return p, sargs
