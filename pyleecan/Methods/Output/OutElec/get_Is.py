from ....Functions.Electrical.coordinate_transformation import dq2n
from numpy import pi, array


def get_Is(self):
    """Return the stator current
    """
    if self.Is is None or len(self.Is) == 0:
        # Generate current according to Id/Iq
        Isdq = array([self.Id_ref, self.Iq_ref])
        time = self.time
        qs = self.parent.simu.machine.stator.winding.qs
        felec = self.felec

        # add stator current
        Is = dq2n(Isdq, 2 * pi * felec * time, n=qs)
        self.Is = Is
    return self.Is
