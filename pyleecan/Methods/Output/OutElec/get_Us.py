from ....Functions.Electrical.coordinate_transformation import dqh2n
from numpy import pi, array, transpose
from SciDataTool import Data1D, DataTime
from ....Functions.Winding.gen_phase_list import gen_name


def get_Us(self):
    """Return the stator voltage"""
    if self.Us is None:
        # Generate current according to Ud/Uq
        Usdq = array([self.Ud_ref, self.Uq_ref])
        time = self.axes_dict["time"].get_values(is_oneperiod=True)
        qs = self.parent.simu.machine.stator.winding.qs
        felec = self.felec

        # add stator current
        Us = dqh2n(Usdq, 2 * pi * felec * time, n=qs)
        Phase = Data1D(
            name="phase",
            unit="",
            values=gen_name(qs),
            is_components=True,
        )
        self.Us = DataTime(
            name="Stator voltage",
            unit="V",
            symbol="Us",
            axes=[Phase, self.axes_dict["time"].copy()],
            values=transpose(Us),
        )
    return self.Us
