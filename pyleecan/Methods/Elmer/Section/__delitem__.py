# -*- coding: utf-8 -*-
def __delitem__(self, key):
    """Called to implement deletion of self[key]."""
    self._statements.__delitem__(key)
    self._comments.__delitem__(key)
