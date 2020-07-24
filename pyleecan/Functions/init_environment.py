import platform
import shutil
import sys
from json import dump, load
from logging import getLogger
from os import makedirs
from os.path import abspath, dirname, isdir, isfile, join, normpath, realpath

from matplotlib.cm import get_cmap, register_cmap
from matplotlib.colors import ListedColormap
from matplotlib import font_manager
from numpy import load as np_load

from ..default_config_dict import default_config_dict


def save_config_dict(config_dict):
    """update the config file with config_dict values

    Parameters
    ----------
    config_dict : dict
        new values to put in the config file
    """
    # dynamic import to avoid loop
    module = __import__(
        "pyleecan.definitions",
        globals=globals(),
        locals=locals(),
        fromlist=["CONF_PATH"],
        level=0,
    )
    CONF_PATH = module.CONF_PATH
    with open(CONF_PATH, "w") as config_file:
        dump(config_dict, config_file, sort_keys=True, indent=4, separators=(",", ": "))


def init_user_dir():
    """Initialize the USER DIR with the default files
    """
    # dynamic import to avoid loop
    module = __import__(
        "pyleecan.definitions",
        globals=globals(),
        locals=locals(),
        fromlist=["USER_DIR", "MAIN_DIR"],
        level=0,
    )
    USER_DIR = module.USER_DIR
    MAIN_DIR = module.MAIN_DIR

    logger = getLogger("Pyleecan")

    # Create the main folder
    if not isdir(USER_DIR):
        makedirs(USER_DIR)
        # Copy initial DATA
        logger.debug("Initialization of USER_DIR in " + USER_DIR)

    # Data initialization
    mach_path = join(USER_DIR, "Machine")
    if not isdir(mach_path):
        shutil.copytree(join(MAIN_DIR, "Data", "Machine"), mach_path)
        logger.debug("Initialization USER_DIR Machines in " + mach_path)

    mat_path = join(USER_DIR, "Material")
    if not isdir(mat_path):
        shutil.copytree(join(MAIN_DIR, "Data", "Material"), mat_path)
        logger.debug("Initialization USER_DIR Materials in " + mat_path)

    plot_path = join(USER_DIR, "Plot")
    if not isdir(plot_path):
        shutil.copytree(join(MAIN_DIR, "Data", "Plot"), plot_path)
        logger.debug("Initialization USER_DIR Plot in " + plot_path)

    gui_path = join(USER_DIR, "GUI")
    if not isdir(gui_path):
        shutil.copytree(join(MAIN_DIR, "Data", "GUI"), gui_path)
        logger.debug("Initialization USER_DIR GUI in " + gui_path)


def get_config_dict():
    """Return the config dict (create the default one if needed)

    Returns
    -------
    config_dict: dict
        Dictionnary gather the parameters of the software
    """
    # dynamic import to avoid loop
    module = __import__(
        "pyleecan.definitions",
        globals=globals(),
        locals=locals(),
        fromlist=["USER_DIR", "CONF_PATH"],
        level=0,
    )
    USER_DIR = module.USER_DIR
    CONF_PATH = module.CONF_PATH

    logger = getLogger("Pyleecan")

    # Initialization to make sure all the parameters exist
    init_user_dir()
    config_dict = default_config_dict.copy()
    if isfile(CONF_PATH):
        with open(CONF_PATH, "r") as config_file:
            update_dict(source=config_dict, update=load(config_file))
    else:
        logger.debug("Creating missing config_dict in " + CONF_PATH)
    save_config_dict(config_dict)

    # Load the color_dict
    color_path = join(USER_DIR, "Plot", config_dict["PLOT"]["COLOR_DICT_NAME"])
    def_color_path = join(USER_DIR, "Plot", "pyleecan_color.json")
    if not isfile(color_path):  # Default colors
        logger.warning(
            "Unable to load colors from " + color_path + ", using default colors"
        )
        color_path = join(USER_DIR, "Plot", "pyleecan_color.json")

    # Load default to make sure that the keys are all there
    with open(def_color_path, "r") as color_file:
        config_dict["PLOT"]["COLOR_DICT"] = load(color_file)
    if color_path != def_color_path:
        with open(color_path, "r") as color_file:
            update_dict(
                source=config_dict["PLOT"]["COLOR_DICT"], update=load(color_file)
            )

    # Register the colormap
    cmap_name = config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"]
    if "." not in cmap_name:
        cmap_path = join(USER_DIR, "Plot", cmap_name) + ".npy"
    try:
        get_cmap(name=cmap_name)
    except:
        if not isfile(cmap_path):  # Default colormap
            config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"] = "RdBu_r"
        else:
            cmap = np_load(cmap_path)
            cmp = ListedColormap(cmap)
            register_cmap(name=config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"], cmap=cmp)

    # Check if font is available
    font_name = config_dict["PLOT"]["FONT_NAME"]
    if font_name not in [f.name for f in font_manager.fontManager.ttflist]:
        logger.warning(
            "WARNING: "
            + font_name
            + "font not available. Try: matplotlib.font_manager._rebuild()"
        )
        config_dict["PLOT"]["FONT_NAME"] = "Arial"  # Default font

    return config_dict


def update_dict(source, update):
    for key, value in update.items():
        if isinstance(value, dict):
            source[key] = update_dict(source.get(key, {}), value)
        else:
            source[key] = value
    return source
