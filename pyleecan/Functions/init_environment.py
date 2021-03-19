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
from ..loggers import GUI_LOG_NAME
from ..default_config_dict import default_config_dict

DEFAULT_FONT = "Arial"
DEFAULT_COLOR_MAP = "RdBu_r"


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
    """Initialize the USER DIR with the default files"""
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

    logger = getLogger(GUI_LOG_NAME)
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
    # Create default config dict
    init_config_dict()


def update_user_dir():
    """Initialize the USER DIR with the default files"""
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

    logger = getLogger(GUI_LOG_NAME)

    # Data initialization
    mach_path = join(USER_DIR, "Machine")
    if isdir(mach_path):
        shutil.rmtree(mach_path)
    shutil.copytree(join(MAIN_DIR, "Data", "Machine"), mach_path)
    logger.debug("Updating USER_DIR Machines in " + mach_path)

    mat_path = join(USER_DIR, "Material")
    if isdir(mat_path):
        shutil.rmtree(mat_path)
    shutil.copytree(join(MAIN_DIR, "Data", "Material"), mat_path)
    logger.debug("Updating USER_DIR Materials in " + mat_path)

    plot_path = join(USER_DIR, "Plot")
    if isdir(plot_path):
        shutil.rmtree(plot_path)
    shutil.copytree(join(MAIN_DIR, "Data", "Plot"), plot_path)
    logger.debug("Updating USER_DIR Plot in " + plot_path)

    gui_path = join(USER_DIR, "GUI")
    if isdir(gui_path):
        shutil.rmtree(gui_path)
    shutil.copytree(join(MAIN_DIR, "Data", "GUI"), gui_path)
    logger.debug("Updating USER_DIR GUI in " + gui_path)


def init_config_dict():
    """Create the default config dict and save it in USER_DIR"""
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

    # Get version
    module = __import__(
        "pyleecan",
        globals=globals(),
        locals=locals(),
        fromlist=["__version__"],
        level=0,
    )
    version = module.__version__
    logger = getLogger(GUI_LOG_NAME)

    # Initialization to make sure all the parameters exist
    config_dict = default_config_dict.copy()
    config_dict["version"] = version
    save_config_dict(config_dict)
    logger.debug("Init config_dict at :" + CONF_PATH + "(version=" + version + ")")


def get_config_dict():
    """Return the config dict (update with default to make sure all parameter exist)

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
    # Get version
    module = __import__(
        "pyleecan",
        globals=globals(),
        locals=locals(),
        fromlist=["__version__"],
        level=0,
    )
    version = module.__version__

    logger = getLogger(GUI_LOG_NAME)

    # Make sure user dir exist
    if not isfile(CONF_PATH):
        init_user_dir()

    # Overwrite default config_dict with USER_DIR values
    config_dict = default_config_dict.copy()
    with open(CONF_PATH, "r") as config_file:
        update_dict(source=config_dict, update=load(config_file))

    # Update Library if new version
    if "version" not in config_dict:
        config_dict["version"] = "No_version"
    if config_dict["version"] != version:
        logger.debug(
            "Updating USER_DIR from version "
            + config_dict["version"]
            + " to version "
            + version
        )
        update_user_dir()
    config_dict["version"] = version
    save_config_dict(config_dict)

    # Load the color_dict
    def_color_path = join(USER_DIR, "Plot", "pyleecan_color.json")
    color_path = join(USER_DIR, "Plot", config_dict["PLOT"]["COLOR_DICT_NAME"])
    # Get default
    with open(def_color_path, "r") as color_file:
        config_dict["PLOT"]["COLOR_DICT"] = load(color_file)
    # Overwritte with user colors
    if color_path != def_color_path and isfile(color_path):
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
            config_dict["PLOT"]["COLOR_DICT"]["COLOR_MAP"] = DEFAULT_COLOR_MAP
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
        config_dict["PLOT"]["FONT_NAME"] = DEFAULT_FONT  # Default font

    # Update config_dict content
    config_dict["MAIN"]["MACHINE_DIR"] = join(USER_DIR, "Machine")
    config_dict["MAIN"]["MATLIB_DIR"] = join(USER_DIR, "Material")
    config_dict["GUI"]["CSS_PATH"] = join(
        USER_DIR, "GUI", config_dict["GUI"]["CSS_NAME"]
    )

    return config_dict


def update_dict(source, update):
    for key, value in update.items():
        if isinstance(value, dict):
            source[key] = update_dict(source.get(key, {}), value)
        else:
            source[key] = value
    return source
