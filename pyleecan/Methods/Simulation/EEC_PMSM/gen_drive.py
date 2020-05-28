# -*- coding: utf-8 -*-

from ....Functions.Electrical.coordinate_transformation import n2dq
from numpy import split, transpose, linspace
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
    p = output.simu.machine.stator.winding.p
    angle = output.get_angle_rotor()
    d_angle_diff = output.get_d_angle_diff()
    rot_dir = output.get_rot_dir()

    # Define d axis angle for the d,q transform
    d_angle = rot_dir * (angle - d_angle_diff)

    # Compute voltage
    voltage = self.drive.get_wave()

    # d,q transform
    voltage_dq = n2dq(transpose(voltage), p * d_angle, n=qs)

    # Store into EEC parameters
    self.parameters["Ud"] = voltage_dq[:, 0]
    self.parameters["Uq"] = voltage_dq[:, 1]

    fig = plt.figure()
    time = linspace(0, 1, 2048)
    plt.plot(time, voltage[0, :], color="tab:blue", label="A")
    plt.plot(time, voltage[1, :], color="tab:red", label="B")
    plt.plot(time, voltage[2, :], color="tab:olive", label="C")
    plt.legend()
    fig.savefig("C:\\Users\\HP\\Documents\\Helene\\test_voltage.png")
