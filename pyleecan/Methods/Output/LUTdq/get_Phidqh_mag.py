from ....Functions.Electrical.dqh_transformation import n2dqh_DataTime


def get_Phidqh_mag(self):
    """Get the total d-axis inductance

    Parameters
    ----------
    self : LUTdq
        a LUTdq object

    Returns
    ----------
    Phi_dqh_mag : DataND
        magnets flux linkage in dqh frame (Nt_tot, 3)
    """

    if self.Phi_dqh_mag is None:

        # Find Id=Iq=0
        OP_list = self.get_OP_matrix()[:, 1:3].tolist()
        if [0, 0] in OP_list:
            ii = OP_list.index([0, 0])
        else:
            raise Exception("Operating Point Id=Iq=0 is required to compute LUT")

        stator_label = self.simu.machine.stator.get_label()

        # dqh transform
        Phi_dqh_mag = n2dqh_DataTime(
            self.output_list[ii].mag.Phi_wind[stator_label],
            is_dqh_rms=True,
            phase_dir=self.elec.phase_dir,
        )

        # Store for next call
        self.Phi_dqh_mag = Phi_dqh_mag

    return self.Phi_dqh_mag
