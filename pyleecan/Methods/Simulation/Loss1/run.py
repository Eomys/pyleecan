# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the Force module
    """
    if self.parent is None:
        raise InputError("ERROR: The Loss object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("ERROR: The Loss object must be in an Output object to run")

    output = self.parent.parent
    machine = self.parent.machine

    # Compute the losses of the machine parts
    if self.lam_stator is not None:
        self.lam_stator.comp_loss(output, machine.stator, "Lamination")

    # if self.lam_rotor is not None:
    #     self.lam_rotor.comp_loss(output, "Plam_rotor")

    # if self.wind_stator is not None:
    #     self.wind_stator.comp_loss(output, "Pwind_stator")

    # if self.wind_rotor is not None:
    #     self.wind_rotor.comp_loss(output, "Pwind_rotor")

    # if self.mag_stator is not None:
    #     self.mag_stator.comp_loss(output, "Pmag_stator")

    # if self.mag_rotor is not None:
    #     self.mag_rotor.comp_loss(output, "Pmag_rotor")

    # if self.windage is not None:
    #     self.windage.comp_loss(output, "Pwindage")

    # if self.bearing is not None:
    #     self.bearing.comp_loss(output, "Pbearing")

    # if self.shaft is not None:
    #     self.shaft.comp_loss(output, "Pshaft")

    # if self.frame is not None:
    #     self.frame.comp_loss(output, "Pframe")

    # if self.additional is not None:
    #     self.additional.comp_loss(output, "Padd")
