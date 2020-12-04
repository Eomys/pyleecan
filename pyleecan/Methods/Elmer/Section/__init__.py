# -*- coding: utf-8 -*-


class ElmerSectionError(Exception):
    pass


# class to represent type 'File' in Elmer
class File(str):
    pass


# class to represent type 'Variable' in Elmer
# TODO multiple variable as list
class Variable:
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value


# class to represent MATC expressions in Elmer
class MATC:
    def __init__(self, expr=None):
        self.expr = expr
