# -*- coding: utf-8 -*-
from re import compile, search

from qtpy import QtGui
from qtpy.QtGui import QDoubleValidator
from qtpy.QtWidgets import QLineEdit

from ...GUI import gui_option

_float_re = compile(r"(([+-]?\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?)")


def valid_float_string(string):
    """

    Parameters
    ----------
    string :


    Returns
    -------

    """
    match = _float_re.search(string)
    return match.groups()[0] == string if match else False


class FloatEdit(QLineEdit):
    """A Line Edit Widget optimized to input float"""

    def __init__(self, unit="", *args, **kwargs):
        """Same constructor as QLineEdit + config validator"""
        self.unit = unit
        self.u = gui_option.unit

        # Call the Line Edit constructor
        super(FloatEdit, self).__init__(*args, **kwargs)

        # Setup the validator
        Validator = FloatValidator(-1e18, 1e18, 10)
        Validator.Notation = QDoubleValidator.ScientificNotation
        self.setValidator(Validator)

    def setValue(self, value):
        """Allow to set the containt of the Widget with a float

        Parameters
        ----------
        self :
            A FloatEdit object
        value :
            A float value to set the Text

        Returns
        -------

        """
        if value in [None, ""]:
            self.clear()
        else:
            if self.unit == "m":
                self.setText(format(self.u.get_m(value), ".8g"))
            else:
                self.setText(format(value, ".8g"))

    def value(self):
        """Return the content of the Widget as a float

        Parameters
        ----------
        self :
            A FloatEdit object

        Returns
        -------

        """
        try:
            self.setText(self.validator().fixup_txt(self.text(), self.u, self.unit))
            if self.text() == "":
                return None
            else:
                value = float(self.text())
            if self.unit == "m":
                return self.u.set_m(value)
            else:
                return value
        except Exception:
            return None


class FloatValidator(QDoubleValidator):
    """DoubleValidator with fixup method to correct the input"""

    def validate(self, string, position):
        """

        Parameters
        ----------
        string :

        position :


        Returns
        -------

        """
        string = string.replace(",", ".")

        match = search(r"^[+-]?($|(\d+\.?|\.?(\d+|$))\d*($|([eE][+-]?)?\d*$))", string)
        is_intermediate = True if match else False

        if valid_float_string(string) or string == "":
            state = QtGui.QValidator.Acceptable
        elif is_intermediate:
            state = QtGui.QValidator.Intermediate
        else:
            state = QtGui.QValidator.Invalid
        return (state, string, position)

    def fixup_txt(self, text, gui_unit, val_unit):
        """When the input text is wrong, fixup is called to correct it in
        the field

        Parameters
        ----------
        self :
            A FloatValidator object
        text :
            The text to correct
        gui_unit :
            Current gui unit system
        val_unit :
            Unit used by the FloatEdit

        Returns
        -------

        """
        if text != "":  # We can't correct an empty text
            # 12,10 can't be converted to float 12.10 can
            text = text.replace(",", ".")
            try:
                top = self.top()
                bottom = self.bottom()
                # Check unit
                if val_unit == "m":
                    top = gui_unit.get_m(top)
                    bottom = gui_unit.get_m(bottom)

                # If the input is too high...
                if float(text) > top:
                    # ... we replace it by the maximum
                    text = str(top)
                # If the input is too low...
                elif float(text) < bottom:
                    # ... we replace it by the minimum
                    text = str(bottom)
            except ValueError:  # Can't convert value to float => not complete
                pass
        return text
