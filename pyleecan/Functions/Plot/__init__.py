from ..Load.import_class import import_class
from ...definitions import config_dict

dict_2D = {
    "color_list": config_dict["PLOT"]["COLOR_DICT"]["COLOR_LIST"],
    "font_name": config_dict["PLOT"]["FONT_NAME"],
    "font_size_title": config_dict["PLOT"]["FONT_SIZE_TITLE"],
    "font_size_label": config_dict["PLOT"]["FONT_SIZE_LABEL"],
    "font_size_legend": config_dict["PLOT"]["FONT_SIZE_LEGEND"],
}

dict_3D = {
    "colormap": config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"],
    "font_name": config_dict["PLOT"]["FONT_NAME"],
    "font_size_title": config_dict["PLOT"]["FONT_SIZE_TITLE"],
    "font_size_label": config_dict["PLOT"]["FONT_SIZE_LABEL"],
    "font_size_legend": config_dict["PLOT"]["FONT_SIZE_LEGEND"],
}

unit_dict = {
    "time": "s",
    "angle": "rad",
    "freqs": "Hz",
    "wavenumber": "",
    "phase": "",
    "z": "m",
    "radius": "m",
    "distance": "m",
}

norm_dict = {
    "elec_order": "Electrical order []",
    "mech_order": "Mechanical order []",
    "space_order": "Space order []",
    "distance": "Distance [m]",
    "angle_rotor": "Rotor mechanical angle [°]",
}

axes_dict = {
    "freqs": "frequency",
}

fft_dict = {
    "time": "freqs",
    "angle": "wavenumber",
}

ifft_dict = {
    "freqs": "time",
    "wavenumber": "angle",
}

## Paramater for Schematics plot
P_FONT_SIZE = 12  # Point Font size
SC_FONT_SIZE = 12  # Schematics Font size
TEXT_BOX = dict(  # Parameter of the text box
    boxstyle="round",
    ec=(0.0, 0.0, 0.0),
    fc=(1.0, 1.0, 1.0),
)
# Arrow parameters
ARROW_WIDTH = 2
ARROW_COLOR = "black"
# Schematics lines
SC_LINE_COLOR = "black"
SC_LINE_STYLE = "dotted"
SC_LINE_WIDTH = 1
# Main lines
MAIN_LINE_COLOR = "0.5"  # Gray
MAIN_LINE_STYLE = "dotted"
MAIN_LINE_WIDTH = 1


def plot_quote(Z1, Zlim1, Zlim2, Z2, offset_label=0, fig=None, ax=None, label=None):
    """Function to plot a "quote" for the scematics"""
    Segment = import_class("pyleecan.Classes", "Segment")
    line1 = Segment(Z1, Zlim1)
    line2 = Segment(Zlim1, Zlim2)
    line3 = Segment(Zlim2, Z2)
    line1.plot(
        fig=fig,
        ax=ax,
        color=SC_LINE_COLOR,
        linestyle=SC_LINE_STYLE,
        linewidth=SC_LINE_WIDTH,
    )
    line2.plot(
        fig=fig,
        ax=ax,
        color=ARROW_COLOR,
        linewidth=ARROW_WIDTH,
        label=label,
        offset_label=offset_label,
        is_arrow=True,
        fontsize=SC_FONT_SIZE,
    )
    line3.plot(
        fig=fig,
        ax=ax,
        color=SC_LINE_COLOR,
        linestyle=SC_LINE_STYLE,
        linewidth=SC_LINE_WIDTH,
    )
