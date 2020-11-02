
from numpy import pi, array, transpose

from SciDataTool import Data1D, DataTime

from ....Functions.Electrical.coordinate_transformation import dq2n
from ....Functions.Winding.gen_phase_list import gen_name


def get_Is(self):
    """Return the stator current DataTime object

    Parameters
    ----------
    self : OutElec
        an OutElec object
        
    """
    # Calculate stator currents if Is is not in OutElec
    if self.Is is None:
        # Generate current according to Id/Iq
        Isdq = array([self.Id_ref, self.Iq_ref])
        time = self.Time.get_values(is_oneperiod=True)
        qs = self.parent.simu.machine.stator.winding.qs
        felec = self.felec

        # Get rotation direction of the fundamental magnetic field created by the winding
        rot_dir = self.parent.get_rot_dir()

        # Get stator current function of time
        Is = dq2n(Isdq, 2 * pi * felec * time, n=qs, rot_dir=rot_dir, is_n_rms=False)

        Phase = Data1D(
            name="phase",
            unit="",
            values=gen_name(qs),
            is_components=True,
        )
        self.Is = DataTime(
            name="Stator current",
            unit="A",
            symbol="Is",
            axes=[Phase, self.Time.copy()],
            values=transpose(Is),
        )
    return self.Is
