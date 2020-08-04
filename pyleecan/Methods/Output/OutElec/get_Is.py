from ....Functions.Electrical.coordinate_transformation import dq2n
from numpy import ones


def get_Is(self):
    """Return the stator current
    """
    if self.Is is None or len(self.Is) == 0:
        # Generate current according to Id/Iq
        Isdq = ones((self.time.shape[0], 2))
        Isdq[:, 0] *= self.Id_ref
        Isdq[:, 1] *= self.Iq_ref
        # calculate/get rotor angle and calculate phase currents
        angle_rotor = self.parent.get_angle_rotor()
        angle = angle_rotor - self.parent.simu.machine.comp_angle_offset_initial()
        zp = self.parent.simu.machine.stator.get_pole_pair_number()
        qs = self.parent.simu.machine.stator.winding.qs

        # add stator current
        Is = dq2n(Isdq, angle * zp, n=qs)
        self.Is = Is
    return self.Is
