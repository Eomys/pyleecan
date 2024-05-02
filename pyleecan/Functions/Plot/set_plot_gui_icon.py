import matplotlib.pyplot as plt
from qtpy.QtCore import QSize
from qtpy.QtGui import QIcon

from ...GUI.Resources import pixmap_dict


def set_plot_gui_icon():
    """Add the software icon on the current plot"""
    thismanager = plt.get_current_fig_manager()
    if thismanager is not None:
        icon = QIcon()
        icon.addFile(pixmap_dict["soft_icon"], QSize(), QIcon.Normal, QIcon.Off)
        thismanager.window.setWindowIcon(icon)
