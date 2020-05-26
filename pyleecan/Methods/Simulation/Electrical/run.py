# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError


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
    
    # Generate drive
    self.gen_drive(output)
    # Compute parameters of the equivalent electrical circuit
    self.eec.comp_EEC_parameters(output)
    # Solve the equivalent electrical circuit
    self.eec.solve_EEC(output)
    # Compute losses due to Joule effects
    self.eec.comp_losses(output)
    # Compute torque
    self.eec.comp_torque(output)
