# -*- coding: utf-8 -*-

from ....Functions.Electrical.coordinate_transformation import n2dq
from numpy import split, transpose, mean, pi

import matplotlib.pyplot as plt


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
    felec = output.elec.felec
    time = output.elec.time

    # Compute voltage
    Voltage = self.drive.get_wave()

    # d,q transform
    voltage = Voltage.values
    voltage_dq = split(n2dq(transpose(voltage), -2 * pi * felec * time, n=qs), 2, axis=1)
    
    fig = plt.figure()
    plt.plot(time[:50], voltage[0,:50], color="tab:blue", label="A")
    plt.plot(time[:50], voltage[1,:50], color="tab:red", label="B")
    plt.plot(time[:50], voltage[2,:50], color="tab:olive", label="C")
    plt.plot(time[:50], voltage_dq[0][:50], color="k", label="D")
    plt.plot(time[:50], voltage_dq[1][:50], color="g", label="Q")
    plt.legend()
    fig.savefig("test_tension.png")

    # Store into EEC parameters
    self.parameters["Ud"] = mean(voltage_dq[0])
    self.parameters["Uq"] = mean(voltage_dq[1])
