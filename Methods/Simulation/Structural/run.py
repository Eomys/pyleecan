# -*- coding: utf-8 -*-

from pyleecan.Methods.Simulation.Input import InputError


def run(self):
    """Run the Structural module    
    """
    if self.parent is None:
        raise InputError(
            "ERROR: The Structural object must be in a Simulation object to run"
        )
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    output = self.parent.parent

    self.comp_time_angle(output)

    # Compute the magnetic force according to the airgap flux
    self.force.comp_force(output)
    if self.force.is_comp_nodal_force:
        self.force.comp_force_nodal()
