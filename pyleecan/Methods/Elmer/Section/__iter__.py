# -*- coding: utf-8 -*-


def __iter__(self):
    """Method to behave like a dict and iterate the keys"""
    return self._statements.__iter__()
