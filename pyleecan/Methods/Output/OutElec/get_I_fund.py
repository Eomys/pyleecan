from numpy import pi, array, where, isclose, zeros

from SciDataTool import Data1D, DataTime, DataFreq

from ....Functions.Electrical.coordinate_transformation import dq2n
from ....Functions.Winding.gen_phase_list import gen_name


def get_I_fund(self, Time=None):
    """Return the stator current DataTime object

    Parameters
    ----------
    self : OutElec
        an OutElec object

    """
    if Time is None:
        Time = self.axes_dict["time"]
    time = Time.get_values(is_smallestperiod=True)
    qs = self.parent.simu.machine.stator.winding.qs
    felec = self.felec

    Phase = Data1D(
        name="phase",
        unit="",
        values=gen_name(qs),
        is_components=True,
    )

    if self.Is is None:
        if (
            self.Id_ref is not None
            and self.Iq_ref is not None
            and self.Id_ref != 0
            and self.Iq_ref != 0
        ):
            # Generate current according to Id/Iq
            Isdq = array([self.Id_ref, self.Iq_ref])

            # Get rotation direction of the fundamental magnetic field created by the winding
            rot_dir = self.parent.get_rot_dir()

            # Get stator current function of time
            Is = dq2n(
                Isdq, 2 * pi * felec * time, n=qs, rot_dir=rot_dir, is_n_rms=False
            )
        else:
            Is = zeros((time.size, qs))

        I_fund = DataTime(
            name="Stator current",
            unit="A",
            symbol="I_s",
            axes=[Time, Phase],
            values=Is,
        )

    else:
        result = self.Is.get_along("freqs", "phase")
        Is_val = result["I_s"]
        freqs = result["freqs"]
        ifund = where(isclose(freqs, felec))
        Is_fund = Is_val[ifund, :]

        Freq = Data1D(
            name="freqs",
            unit="Hz",
            values=freqs[ifund],
        )

        I_fund = DataFreq(
            name="Stator current",
            unit="A",
            symbol="I_s",
            axes=[Freq, Phase],
            values=Is_fund,
        )

    return I_fund
