from numpy import zeros, array

from ....Classes.EEC_PMSM import EEC_PMSM

from ....Functions.Electrical.dqh_transformation import n2dqh_DataTime


def get_Phi_dqh_mean(self):
    """Get the mean value of stator flux along dqh axes

    Parameters
    ----------
    self : LUTdq
        a LUTdq object

    Returns
    ----------
    Phi_dqh_mean : ndarray
        mean flux linkage in dqh frame (N_dq, 3)
    """

    if self.Phi_dqh_mean is None:

        N_OP = len(self.output_list)

        Phi_dqh_mean = zeros((N_OP, 3))

        stator_label = self.simu.machine.stator.get_label()

        phase_dir = self.output_list[0].elec.phase_dir

        for ii in range(N_OP):
            eec_i = self.output_list[ii].elec.eec

            if eec_i is not None and eec_i.Phid is not None and eec_i.Phiq is not None:
                # Get values from eec
                Phi_dqh_mean[ii, :] = array([eec_i.Phid, eec_i.Phiq, 0])

            else:
                # Integrate stator winding flux contained in LUT over z
                Phi_wind = (
                    self.output_list[ii]
                    .mag.Phi_wind_slice[stator_label]
                    .get_data_along("time", "phase", "z=integrate")
                )

                # dqh transform
                Phi_dqh = n2dqh_DataTime(
                    Phi_wind,
                    is_dqh_rms=True,
                    phase_dir=phase_dir,
                )
                # mean over time axis
                Phi_dqh_mean[ii, :] = Phi_dqh.get_along("time=mean", "phase")[
                    Phi_dqh.symbol
                ]

                # Store values in eec for further use
                if eec_i is None:
                    eec_i = EEC_PMSM()
                    self.output_list[ii].elec.eec = eec_i
                eec_i.Phid = float(Phi_dqh_mean[ii, 0])
                eec_i.Phiq = float(Phi_dqh_mean[ii, 1])

        # Store for next call
        self.Phi_dqh_mean = Phi_dqh_mean

    return self.Phi_dqh_mean
