# -*- coding: utf-8 -*-
"""
@date Created on Wed Mar 13 15:05:30 2019
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Methods.Simulation.Input import InputError
from Classes.ForceMT import ForceMT
from Classes.ForceVWP import ForceVWP

def run(self):
    """Run the force calculations

    Parameters
    ----------
    self : SimuImportMag
        A SimuImportMag object

    """

    if self.parent is None:
        raise InputError("ERROR: Simulation object must be inside an Output object")
    output = self.parent
    output.geo = self.machine.comp_output_geo()

    # Init the input of the first module
    self.input.gen_input()

    # Run the modules
    # if self.elec is not None:
    #     self.elec.run()
    #if self.mag is not None:
    #    self.mag.run()
    if self.struct is not None:
        self.struct.run()

    # if self.ac is not None:
    #     self.ac.run()
