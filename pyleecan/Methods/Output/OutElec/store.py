from numpy import insert, where, abs as np_abs, argsort, array, exp, pi, arange

from SciDataTool import DataFreq, Data1D


def store(self, out_dict):
    """Store the standard outputs of Electrical that are temporarily in out_dict as arrays into OutElec as Data object

    Parameters
    ----------
    self : OutElec
        the OutElec object to update
    out_dict : dict
        Dict containing all electrical quantities that have been calculated in EEC
    out_dict_harm : dict
        Dict containing harmonic quantities that have been calculated in EEC

    """

    # Store Id, Iq, Ud, Uq
    self.OP.set_Id_Iq(Id=out_dict["Id"], Iq=out_dict["Iq"])
    self.OP.set_Ud_Uq(Ud=out_dict["Ud"], Uq=out_dict["Uq"])

    self.Pj_losses = out_dict["Pj_losses"]
    self.Tem_av_ref = out_dict["Tem_av_ref"]
    self.Pem_av_ref = out_dict["Pem_av_ref"]

    if "Ir" in out_dict:
        # Calculate rotor currents for each bar
        p = self.parent.simu.machine.get_pole_pair_number()
        rotor_lab = self.parent.simu.machine.rotor.get_label()
        Phase = self.axes_dict["phase_" + rotor_lab]

        Time = self.axes_dict["time"]

        angle_bars = Phase.get_values(is_smallestperiod=True)

        Ir = out_dict["Ir"] * exp(1j * p * angle_bars)

        felec_rot = self.OP.get_felec() * self.OP.get_slip()

        norm_freq = dict()
        if Time.normalizations is not None and len(Time.normalizations) > 0:
            for key, val in Time.normalizations.items():
                norm_freq[key] = val.copy()

        Freqs = Data1D(
            name="freqs",
            symbol="Freqs_PWM.symbol",
            unit="Hz",
            values=array([felec_rot]),
            normalizations=norm_freq,
        )

        self.Ir = DataFreq(
            name="Rotor current",
            unit="A",
            symbol="Ir",
            axes=[Freqs, Phase],
            values=Ir[:, None],
        )

        # self.Ir.plot_2D_Data(
        #     "time=axis_data", "phase[0,1,2]", axis_data={"time": Time.get_values()}
        # )

    if "Is_PWM" in out_dict:
        # Merge current PWM harmonics with fundamental current
        # Get PWM current from out_dict
        Is_PWM = out_dict.pop("Is_PWM")

        # Merge Spectrums
        # Get fundamental current spectrum
        Is = self.get_Is(is_freq=True)
        Is_fund = Is.get_along("freqs=" + str(self.OP.felec), "phase")[Is.symbol]
        # Get PWM frequency vector
        freqs = Is_PWM.axes[0].get_values()
        Ifund = where(np_abs(freqs - self.OP.felec) < 1e-4)[0]
        if Ifund.size == 0:
            # Add felec at the first place
            freqs = insert(freqs, 0, self.OP.felec, axis=0)
            # Add fundamental values
            Is_val = insert(Is_PWM.values, 0, Is_fund, axis=0)
            # Store values in Is
            Isort = argsort(freqs)
            Is.axes[0].values = freqs[Isort]
            Is.values = Is_val[Isort, :]
        else:
            # felec already in frequency axis, simply add fundamenal values
            Is.axes[0].values = freqs
            Is_PWM.values[Ifund, :] += Is_fund
            Is.values = Is_PWM.values

        # Store current in OutElec
        self.Is = Is
