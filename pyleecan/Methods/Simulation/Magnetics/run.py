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

    self.comp_time_angle(output)

    if output.elec.rot_dir is None:
        output.elec.rot_dir = (
            output.simu.machine.stator.comp_rot_dir()
        )  # TODO: create comp_rot_dir() in machine object

    self.comp_flux_airgap(output)
