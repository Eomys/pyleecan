# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the Magnetics module"""
    if self.parent is None:
        raise InputError(
            "ERROR: The Magnetic object must be in a Simulation object to run"
        )
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    self.get_logger().info("Starting Magnetic module")
    output = self.parent.parent

    # Compute and store time and angle axes from previous output
    # and returns additional axes in axes_dict
    axes_dict = self.comp_time_angle(output)

    # Calculate airgap flux
    self.comp_flux_airgap(output, axes_dict)
