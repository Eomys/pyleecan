# -*- coding: utf-8 -*-
from os.path import abspath, dirname, join, normpath

GEN_DIR = normpath(abspath(dirname(__file__)))
MAIN_DIR = normpath(abspath(join(dirname(__file__), "..")))
DOC_DIR = normpath(join(GEN_DIR, "ClassesRef"))  # Absolute path to doc dir

PYTHON_TYPE = ["float", "int", "str", "bool", "complex", "list", "dict"]
# Indentation according to PEP 8
TAB = "    "
TAB2 = TAB + TAB
TAB3 = TAB + TAB + TAB
TAB4 = TAB + TAB + TAB + TAB
TAB5 = TAB + TAB + TAB + TAB + TAB
TAB6 = TAB + TAB + TAB + TAB + TAB + TAB
TAB7 = TAB + TAB + TAB + TAB + TAB + TAB + TAB
