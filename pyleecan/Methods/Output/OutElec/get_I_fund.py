from numpy import array, where, isclose, zeros

from SciDataTool import Data1D, DataTime, DataFreq

from ....Functions.Electrical.coordinate_transformation import dqh2n


def get_I_fund(self, Time=None):
    """Return the stator current DataTime object

    Parameters
    ----------
    self : OutElec
        an OutElec object

    """
    if Time is None:
        Time = self.axes_dict["time"]
    angle_elec = Time.get_values(is_smallestperiod=True, normalization="angle_elec")
    qs = self.parent.simu.machine.stator.winding.qs
    stator_label = "phase_" + self.parent.simu.machine.stator.get_label()
    felec = self.felec

    Phase = self.axes_dict[stator_label]

    if self.Is is None:
        if (
            self.Id_ref is not None
            and self.Iq_ref is not None
            and (self.Id_ref != 0 or self.Iq_ref != 0)
        ):
            # Generate current according to Id/Iq, Ih=0
            Is_dqh = zeros((angle_elec.size, 3))
            Is_dqh[:, 0] = self.Id_ref
            Is_dqh[:, 1] = self.Iq_ref

            # Get stator current function of time
            Is = dqh2n(Is_dqh, angle_elec, n=qs, is_n_rms=False)
        else:
            Is = zeros((angle_elec.size, qs))

        I_fund = DataTime(
            name="Stator current",
            unit="A",
            symbol="I_s",
            axes=[Time, Phase],
            values=Is,
        )

    else:
        result = self.Is.get_along("freqs", "phase")
        Is_val = result[self.Is.symbol]
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
