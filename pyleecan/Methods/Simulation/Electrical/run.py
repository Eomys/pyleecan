# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the Electrical module"""
    if self.parent is None:
        raise InputError(
            "ERROR: The Electrical object must be in a Simulation object to run"
        )
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    self.get_logger().info("Starting Electric module")

    output = self.parent.parent

    if self.eec is not None:

        # # Generate drive
        # self.eec.gen_drive(output)

        # Compute parameters of the electrical equivalent circuit
        self.eec.comp_parameters(output)

        # Solve the electrical equivalent circuit
        self.eec.solve_EEC(output)

        # Compute losses due to Joule effects
        self.eec.comp_joule_losses(output)

        # Compute electromagnetic power
        self.comp_power(output)

        # Compute torque
        self.comp_torque(output)
