from ....Functions.Electrical.coordinate_transformation import dq2n
from numpy import pi, array, transpose
from SciDataTool import Data1D, DataTime
from ....Functions.Winding.gen_phase_list import gen_name


def get_Is(self):
    """Return the stator current
    """
    if self.Is is None:
        # Generate current according to Id/Iq
        Isdq = array([self.Id_ref, self.Iq_ref])
        time = self.time
        qs = self.parent.simu.machine.stator.winding.qs
        felec = self.felec

        # add stator current
        Is = dq2n(Isdq, 2 * pi * felec * time, n=qs)
        Time = Data1D(name="time", unit="s", values=time)
        Phase = Data1D(
            name="phase",
            unit="",
            values=gen_name(qs, is_add_phase=True),
            is_components=True,
        )
        self.Is = DataTime(
            name="Stator current", unit="A", symbol="Is", axes=[Phase, Time], values=transpose(Is)
        )
    return self.Is
