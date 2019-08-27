# -*- coding: utf-8 -*-

from pyleecan.Methods.Simulation.Input import InputError


def run(self):
    """Run the Magnetics module    
    """
    if self.parent is None:
        raise InputError(
            "ERROR: The Magnetic object must be in a Simulation object to run"
        )
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    output = self.parent.parent

    self.comp_time_angle(output)

    self.comp_flux_airgap(output)
