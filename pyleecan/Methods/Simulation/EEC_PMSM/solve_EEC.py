# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from ....Functions.Electrical.coordinate_transformation import dq2n, ab2n
from SciDataTool import Data1D, DataTime
from ....Functions.Winding.gen_phase_list import gen_name

from numpy import (
    array,
    pi,
    zeros,
    linspace,
    split,
    column_stack,
    transpose,
    real,
    imag,
    sqrt,
    abs as np_abs,
)
from scipy.linalg import solve


def solve_EEC(self, output):
    """Compute the parameters dict for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    output : Output
        an Output object
    """

    qs = output.simu.machine.stator.winding.qs
    p = output.simu.machine.stator.winding.p
    freq0 = self.freq0
    ws = 2 * pi * freq0
    d_angle_diff = output.get_d_angle_diff()
    rot_dir = output.get_rot_dir()
    angle_rotor = output.get_angle_rotor()
    N_tot = len(self.parameters["Ud"])

    # Prepare linear system
    XR = array(
        [
            [self.parameters["R20"], -ws * 1j * self.parameters["Lq"]],
            [ws * 1j * self.parameters["Ld"], self.parameters["R20"]],
        ],
        dtype=complex,
    )
    XE = array([0, self.parameters["BEMF"]], dtype=complex)
    Idq = zeros((N_tot, 2), dtype=complex)
    for i in range(N_tot):
        XU = array([self.parameters["Ud"][i], self.parameters["Uq"][i]], dtype=complex)
        Idq[i, :] = solve(XR, XU - XE)
    # XU = zeros((N_tot, 2), dtype=complex)
    # XE = zeros((N_tot, 2), dtype=complex)
    # XU[:,0] = self.parameters["Ud"]
    # XU[:,1] = self.parameters["Uq"]
    # XR[:,0,0] = self.parameters["R20"]
    # XR[:,0,1] = -ws*self.parameters["Lq"]
    # XR[:,1,0] = ws*self.parameters["Ld"]
    # XR[:,1,1] = self.parameters["R20"]
    # XE[:,1] = self.parameters["BEMF"]

    # dq to abc transform
    d_angle = rot_dir * (angle_rotor - d_angle_diff)
    Is = np_abs(ab2n(Idq, n=qs))
    time = linspace(0, 1, 2048)
    print(time)
    Time = Data1D(name="time", unit="s", values=time)
    phases_names = gen_name(qs, is_add_phase=True)
    Phases = Data1D(
        name="phases", unit="dimless", values=phases_names, is_components=True
    )
    output.elec.Currents = DataTime(
        name="Stator currents",
        unit="A",
        symbol="I_s",
        axes=[Phases, Time],
        values=transpose(Is),
    )

    # print("Idq")
    # print(Idq)
    # time = linspace(0, N_tot, N_tot)
    # fig = plt.figure()
    # plt.plot(time, Idq[:, 0], color="tab:blue", label="D")
    # plt.plot(time, Idq[:, 1], color="tab:red", label="Q")
    # plt.legend()
    # fig.savefig("C:\\Users\\HP\\Documents\\Helene\\test_currents_dq.png")

    # # Transform from d/q axes to phases
    # # Define d axis angle for the d,q transform
    # d_angle = rot_dir * (angle_rotor - d_angle_diff)
    # Is = dq2n(Idq, p * d_angle, n=qs)
    # print("Iabc")
    # print(Is)
    Ir = zeros(Is.shape)

    # # Store in a Data object
    # phases_names = gen_name(qs, is_add_phase=True)
    # Phases = Data1D(name="phases", unit="dimless", values=phases_names)
    # Freqs = Data1D(name="freqs", unit="Hz", values=freqs)
    # output.elec.Currents = DataFreq(
    #     name="Stator currents", unit="A", symbol="I_s", axes=[Freqs, Phases], values=Is,
    # )

    # (time, IsA) = output.elec.Currents.get_along("time")
    # (time, IsB) = output.elec.Currents.get_along("time", "phases[1]")
    # (time, IsC) = output.elec.Currents.get_along("time", "phases[2]")

    fig = plt.figure()
    Is_list = split(Is, 3, axis=1)
    plt.plot(time, Is_list[0], color="tab:blue", label="A")
    plt.plot(time, Is_list[1], color="tab:red", label="B")
    plt.plot(time, Is_list[2], color="tab:olive", label="C")
    plt.legend()
    fig.savefig("C:\\Users\\HP\\Documents\\Helene\\test_currents.png")
    output.elec.Is = Is
    output.elec.Ir = Ir
