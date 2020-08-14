# -*- coding: utf-8 -*-

from ....Functions.Electrical.coordinate_transformation import dq2n
from SciDataTool import Data1D, DataTime
from ....Functions.Winding.gen_phase_list import gen_name

from numpy import array, pi, transpose
from scipy.linalg import solve


def solve_EEC(self, output):
    """Compute the parameters dict for the equivalent electrical circuit
    cf "Advanced Electrical Drives, analysis, modeling, control"
    Rik de doncker, Duco W.J. Pulle, Andre Veltman, Springer edition
    
                 <---                               --->
     -----R-----wsLqIq----              -----R-----wsLdId----
    |                     |            |                     |
    |                     |            |                    BEMF
    |                     |            |                     |
     ---------Id----------              ---------Iq----------
             
             --->                               ---> 
              Ud                                 Uq
              
    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    output : Output
        an Output object
    """

    qs = output.simu.machine.stator.winding.qs
    felec = output.elec.felec
    ws = 2 * pi * felec
    time = output.elec.time

    # Prepare linear system
    XR = array(
        [
            [self.parameters["R20"], -ws * self.parameters["Lq"]],
            [ws * self.parameters["Ld"], self.parameters["R20"]],
        ]
    )
    XE = array([0, self.parameters["BEMF"]])
    XU = array([self.parameters["Ud"], self.parameters["Uq"]])
    Idq = solve(XR, XU - XE)

    # dq to abc transform
    Is = dq2n(Idq, 2 * pi * felec * time, n=qs)

    # Store currents into a Data object
    Time = Data1D(name="time", unit="s", values=time)
    phases_names = gen_name(qs, is_add_phase=True)
    Phases = Data1D(
        name="phases", unit="dimless", values=phases_names, is_components=True
    )
    output.elec.Is = DataTime(
        name="Stator currents",
        unit="A",
        symbol="I_s",
        axes=[Phases, Time],
        values=transpose(Is),
    )
    output.elec.Ir = None
    output.elec.Id_ref = Idq[0]
    output.elec.Iq_ref = Idq[1]
