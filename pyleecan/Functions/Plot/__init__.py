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
