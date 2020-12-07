# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the Force module"""
    if self.parent is None:
        raise InputError(
            "ERROR: The Force object must be in a Simulation object to run"
        )
    if self.parent.parent is None:
        raise InputError("ERROR: The Force object must be in an Output object to run")

    self.get_logger().info("Starting Force module")

    output = self.parent.parent

    # Compute and store time and angle axes from previous output
    # and returns additional axes in axes_dict
    axes_dict = self.comp_axes(output)

    # Compute the magnetic force according to the Force model
    out_dict = self.comp_force(output, axes_dict)

    # Store force quantities contained in out_dict in OutForce, as Data object if necessary
    output.force.store(out_dict, axes_dict)

    # Compute the air-gap surface force transfer if required
    if self.is_agsf_transfer:
        self.comp_AGSF_transfer(output)
