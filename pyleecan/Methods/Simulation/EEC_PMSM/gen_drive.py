# -*- coding: utf-8 -*-

from ....Functions.Electrical.coordinate_transformation import n2dq
from numpy import split, transpose, mean, pi


def gen_drive(self, output):
    """Generate the drive for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    output : Output
        an Output object
    """

    qs = output.simu.machine.stator.winding.qs
    rot_dir = output.get_rot_dir()
    freq0 = self.freq0
    time = output.elec.time

    # Compute voltage
    Voltage = self.drive.get_wave()

    # d,q transform
    voltage = Voltage.values
    voltage_dq = split(
        n2dq(transpose(voltage), -rot_dir * 2 * pi * freq0 * time, n=qs), 2, axis=1
    )

    # Store into EEC parameters
    self.parameters["Ud"] = mean(voltage_dq[0])
    self.parameters["Uq"] = mean(voltage_dq[1])
