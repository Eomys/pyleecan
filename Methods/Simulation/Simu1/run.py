# -*- coding: utf-8 -*-

from pyleecan.Methods.Simulation.Input import InputError


def run(self):
    """Run the simulation

    Parameters
    ----------
    self : Simu1
        A Simu1 object

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
    if self.mag is not None:
        self.mag.run()
    # if self.HT is not None:
    #     self.HT.run()
    if self.struct is not None:
        self.struct.run()
    # if self.ac is not None:
    #     self.ac.run()
