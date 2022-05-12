# -*- coding: utf-8 -*-

import re
import matplotlib.pyplot as plt
from numpy import pi
from scipy.optimize import curve_fit
from itertools import groupby
import textwrap


def comp_coeff(self):

    winding = self.parent.parent.machine.stator.winding
    sigma = winding.conductor.cond_mat.elec.get_conductivity()
    d = winding.conductor.Wwire
    kf = winding.comp_winding_factor()
    k_p = kf * pi ** 2 / 8 * sigma * d ** 2
    self.k_p = k_p
