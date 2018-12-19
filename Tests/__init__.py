# -*- coding: utf-8 -*-
import logging
import os.path

from matplotlib import use

use("Qt5Agg")  # Use PyQt5 backend

TEST_DIR = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
LOG_DIR = os.path.join(TEST_DIR, "logtest.txt")
DOC_DIR = os.path.normpath(os.path.abspath(os.path.join(TEST_DIR, "..", "Doc")))

x = logging.getLogger("logtest")
x.setLevel(logging.DEBUG)
h = logging.FileHandler(LOG_DIR)
f = logging.Formatter("%(message)s")
h.setFormatter(f)
x.addHandler(h)
