# -*- coding: utf-8 -*-

from ....Functions.Electrical.coordinate_transformation import n2dq
from numpy import split

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
    angle = output.elec.get_angle_rotor()
    d_angle_diff = output.get_d_angle_diff()
    rot_dir = output.get_rot_dir()
    
    # Define d axis angle for the d,q transform
    d_angle = rot_dir * (angle - d_angle_diff)

    # Compute voltage
    voltage = self.drive.get_wave()
    
    # d,q transform
    voltage_dq = split(n2dq(voltage, p * d_angle, n=qs), 2, axis=1)
    
    # Store into EEC parameters
    self.eec.parameters["Ud"] = voltage_dq[0]
    self.eec.parameters["Uq"] = voltage_dq[1]
    