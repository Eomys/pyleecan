from qtpy.QtWidgets import QSpinBox


class SpinBox(QSpinBox):
    """A SpinBox Widget which allows to validate with enter key"""

    def __init__(self, *args, **kwargs):
        """Same constructor as QSpinBox"""

        # Call the SpinBox constructor
        super(SpinBox, self).__init__(*args, **kwargs)
        self.setKeyboardTracking(False)

    def keyPressEvent(self, event):
        """To send valueChanged when pressing Enter and Return keys"""
        if event.text() == "\r":
            self.clearFocus()
        else:
            # call base class keyPressEvent
            super(SpinBox, self).keyPressEvent(event)
