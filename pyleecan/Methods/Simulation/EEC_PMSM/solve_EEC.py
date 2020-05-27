# -*- coding: utf-8 -*-

from ....Functions.Electrical.coordinate_transformation import dq2n
from SciDataTool import Data1D, DataLinspace, DataTime
from ....Functions.Winding.gen_phase_list import gen_name

from numpy import array, pi, zeros
from numpy.linalg import solve

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
    d_angle_diff = output.geo.get_d_angle_diff()
    rot_dir = output.geo.get_rot_dir()
    angle_rotor = output.get_angle_rotor()

    ws = 2*pi*freq0
    
    # Prepare linear system
    XU = array([self.parameters["Ud"], self.parameters["Uq"]])
    XR = array([[self.parameters["R20"], -ws*self.parameters["Lq"]],
                [self.parameters["R20"], ws*self.parameters["Ld"]]])
    XE = array([0, self.parameters["BEMF"]])
    
    # Solve linear system XU = XR.Idq + XE
    Idq = solve(XR, XU-XE[:,None])
    
    # Transform from d/q axes to phases
    # Define d axis angle for the d,q transform
    d_angle = rot_dir * (angle_rotor - d_angle_diff)
    Is = dq2n(Idq, p*d_angle, n=qs)
    Ir = zeros(Is.shape)
    
    # Store in a Data object
    phases_names = gen_name(qs, is_add_phase=True)
    Phases = Data1D(name="phases", unit="dimless", values=phases_names)
    Angle = DataLinspace(
        name="angle",
        unit="rad",
        initial=angle_rotor[0],
        final=angle_rotor[-1],
        number=len(angle_rotor),
        include_endpoint=False,
    )
    output.elec.Is = DataTime(
        name="Stator currents",
        unit="A",
        symbol="I_s",
        axes=[Phases, Angle],
        values=Is,
    )
    output.elec.Ir = DataTime(
        name="Rotor currents",
        unit="A",
        symbol="I_r",
        axes=[Phases, Angle],
        values=Ir,
    )
    
    output.elec.Ir = zeros(output.elec.Is.shape)