# -*- coding: utf-8 -*-


def __setitem__(self, key, value):
    """Called to implement assignment to self[key]."""
    if isinstance(value, tuple):
        self._statements.__setitem__(key, value[0])
        if len(tuple) >= 1:
            self._comments.__setitem__(key, value[1])
        else:
            self._comments.__setitem__(key, None)
    else:
        self._statements.__setitem__(key, value)
        self._comments.__setitem__(key, None)
