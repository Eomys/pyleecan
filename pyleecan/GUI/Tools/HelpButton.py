from qtpy.QtCore import QUrl, Qt
from qtpy.QtGui import QCursor, QDesktopServices, QPixmap
from qtpy.QtWidgets import QLabel


class HelpButton(QLabel):
    """A Qlabel with a ? icon, and a click event that open a link"""

    def __init__(self, *args, **kwargs):
        """Same constructor as QLineEdit + config validator"""
        self.url = "https://eomys.com/"

        # Call the QLabel constructor
        super(HelpButton, self).__init__(*args, **kwargs)

        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setPixmap(QPixmap(":/images/images/icon/help_16.png"))

    def mousePressEvent(self, event=None):
        """Open the help link in the default browser

        Parameters
        ----------
        self :
            A HelpButton object
        event :
             (Default value = None)

        Returns
        -------

        """
        QDesktopServices.openUrl(QUrl(self.url))
