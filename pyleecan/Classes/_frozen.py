# -*- coding: utf-8 -*-

from numpy import array_equal, ndarray


class FrozenClass(object):
    """A FrozenClass is designed to avoid adding or accessing wrong properties
    For instance w.wire instead of w.Wwire will throw a Frozen Error
    """

    __isfrozen = False  # Current state

    def __setattr__(self, key, value):
        """Overide to avoid the add of new properties outside of __init__

        Parameters
        ----------
        self : FrozenClass
            The class to set
        key : str
            The name of the property to set
        value : ?
            The value to set

        Raises
        ------
        FrozenError
            You can't set a new property if the class is frozen
        """
        # You can't add a new property to a frozen object
        if self.__isfrozen and not hasattr(self, key):
            raise FrozenError(
                self.__class__.__name__ + ' class has no "' + key + '" ' "property"
            )
        object.__setattr__(self, key, value)

    def _freeze(self):
        """After the call of this function, you can't add new properties to
        this FrozenClass

        Parameters
        ----------
        self : FrozenClass
            The FrozenClass object to freeze

        Returns
        -------
        None
        """

        self.__isfrozen = True

    def __eq__(self, other):
        """Two FrozenClass instance are equal if they have the same __dict__

        Parameters
        ----------
        self : FrozenClass
            A FrozenClass object
        other: FrozenClass
            Another FrozenClass object

        Returns
        -------
        is_equal: bool
            True if self == other
        """

        if isinstance(other, self.__class__):
            for attr in self.__dict__:
                if isinstance(self.__dict__[attr], ndarray):
                    if not array_equal(self.__dict__[attr], other.__dict__[attr]):
                        return False
                else:
                    if self.__dict__[attr] != other.__dict__[attr]:
                        return False
            return True
        else:
            return False

    def __ne__(self, other):
        """Call __eq__

        Parameters
        ----------
        self : FrozenClass
            A FrozenClass object
        other: FrozenClass
            Another FrozenClass object

        Returns
        -------
        is_not_equal: bool
            True if self != other
        """

        return not self.__eq__(other)


class FrozenError(Exception):
    """Throw when the class is frozen and a new property is set"""

    pass
