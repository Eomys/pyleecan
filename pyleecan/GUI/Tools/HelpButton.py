from PySide2.QtCore import QUrl, Qt
from PySide2.QtGui import QCursor, QDesktopServices, QPixmap
from PySide2.QtWidgets import QLabel


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
