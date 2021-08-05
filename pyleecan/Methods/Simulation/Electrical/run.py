# -*- coding: utf-8 -*-

from numpy.lib.shape_base import expand_dims
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

    # taking simulation fundamental frequency & temperatures #TODO
    felec = 50

    # Compute and store time and angle axes from elec output
    # and returns additional axes in axes_dict
    axes_dict = self.comp_axes(output)

    # Generate drive
    # self.eec.gen_drive(output)

    if self.ELUT_enforced is not None:
        # enforce parameters of EEC coming from enforced ELUT at right frequency & temperatures
        self.eec.parameters = self.ELUT_enforced.get_parameters(
            felec=felec, Tsta=self.Tsta, Trot=self.Trot
        )
    else:
        # Compute parameters of the electrical equivalent circuit if ELUT not given
        out_dict = self.eec.comp_parameters(output, self.ELUT_enforced)

    # Solve the electrical equivalent circuit
    out_dict = self.eec.solve_EEC(output)

    # Compute losses due to Joule effects
    out_dict = self.eec.comp_joule_losses(output)

    # Compute electromagnetic power
    out_dict = self.comp_power(output)

    # Compute torque
    out_dict = self.comp_torque(output)

    # Store electrical quantities contained in out_dict in OutElec, as Data object if necessary
    out_dict.store(out_dict, axes_dict)
