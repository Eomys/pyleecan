# Default number of point added for the discrtization of an arc
ARC_NPOINT_D = 99
# Default number of point added for the discrtization of a line
LINE_NPOINT_D = 0

# Color for plot
STATOR_COLOR = "b"
# STATOR_COLOR = '0.75' #For Website slot shape
ROTOR_COLOR = "g"
SHAFT_COLOR = "k"
FRAME_COLOR = "m"
MAGNET_COLOR = "0.75"
BAR_COLOR = "r"
SCR_COLOR = (1, 0, 0, 0.25)  # Short circuit ring
VENT_COLOR = "w"
VENT_EDGE = "k"
PATCH_COLOR = "w"
PATCH_EDGE = "k"
PATCH_COLOR_ALPHA = (0, 0, 0, 0)
PATCH_EDGE_ALPHA = (1, 0, 0, 1)
# Winding Phase
# PHASE_COLOR = ["r", "c", "y","#994499", "#FF00F0",'m','k','b','g']
PHASE_COLOR = [
    (0, 0, 1, 0.5),
    (1, 0, 0, 0.5),
    (0, 1, 0, 0.5),
    (1, 0.5, 0, 0.5),
    (1, 1, 0, 0.5),
    (0, 0, 0, 0.5),
    (1, 0.5, 1, 0.5),
    (0.5, 1, 1, 0.5),
    (1, 1, 0.5, 0.5),
]
PHASE_NAME = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


class MachineCheckError(Exception):
    """ """

    pass
