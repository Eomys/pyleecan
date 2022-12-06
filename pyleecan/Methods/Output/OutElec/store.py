import numpy as np

from SciDataTool import DataFreq, Data1D


def store(self, out_dict):
    """Store the standard outputs of Electrical that are temporarily in out_dict as arrays into OutElec as Data object

    Parameters
    ----------
    self : OutElec
        the OutElec object to update
    out_dict : dict
        Dict containing all electrical quantities that have been calculated in EEC

    """

    output = self.parent
    machine = output.simu.machine

    # Store Id, Iq, Ud, Uq in OP
    self.OP.set_Id_Iq(Id=out_dict["Id"], Iq=out_dict["Iq"])
    self.OP.set_Ud_Uq(Ud=out_dict["Ud"], Uq=out_dict["Uq"])

    self.Pj_losses = out_dict["Pj_losses"]
    self.Tem_av = out_dict["Tem_av"]
    self.Pem_av = out_dict["Pem_av"]
    self.get_Jrms()

    if "Ir" in out_dict and self.OP.get_slip() != 0:
        # Calculate rotor currents for each bar
        p = machine.get_pole_pair_number()
        Zr = machine.rotor.get_Zs()
        rotor_lab = machine.rotor.get_label()
        Phase = self.axes_dict["phase_" + rotor_lab]

        Time = self.axes_dict["time"]

        angle_bars = Phase.get_values(is_smallestperiod=True)

        phase_dir = output.elec.phase_dir
        d_angle = machine.stator.comp_angle_d_axis()

        # Get rotor current fundamental given by EEC
        if phase_dir == -1:
            Ir_fund = np.conj(out_dict["Ir"])
        else:
            Ir_fund = out_dict["Ir"]
        # Get phase angle of stator mmf fundamental
        phimax = 2 * np.pi - p * d_angle
        # Mechanical phase of first bar: q-axis phase + half of rotor slot pitch
        PhiMech = phimax + np.pi / 2 + p * np.pi / Zr

        Ir_val = np.zeros((2, angle_bars.size), dtype=complex)
        Ir_val[1, :] = Ir_fund * np.exp(-phase_dir * 1j * (p * angle_bars + PhiMech))

        felec_rot = self.OP.get_felec() * self.OP.get_slip()

        norm_freq = dict()
        if Time.normalizations is not None and len(Time.normalizations) > 0:
            for key, val in Time.normalizations.items():
                norm_freq[key] = val.copy()

        Freqs = Data1D(
            name="freqs",
            symbol="",
            unit="Hz",
            values=np.array([0, felec_rot]),
            normalizations=norm_freq,
        )

        self.Ir = DataFreq(
            name="Rotor current",
            unit="A",
            symbol="Ir",
            axes=[Freqs, Phase],
            values=Ir_val,
        )

        # Ir = self.Ir.get_data_along(
        #     "time=axis_data",
        #     "phase[smallestperiod]",
        #     axis_data={"time": Time.get_values()},
        # )

        # Ir.plot_3D_Data("time", "phase", is_shading_flat=True)

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
        Ifund = np.where(np.abs(freqs - self.OP.felec) < 1e-4)[0]
        if Ifund.size == 0:
            # Add felec at the first place
            freqs = np.insert(freqs, 0, self.OP.felec, axis=0)
            # Add fundamental values
            Is_val = np.insert(Is_PWM.values, 0, Is_fund, axis=0)
            # Store values in Is
            Isort = np.argsort(freqs)
            Is.axes[0].values = freqs[Isort]
            Is.values = Is_val[Isort, :]
        else:
            # felec already in frequency axis, simply replace by fundamental value
            Is.axes[0].values = freqs
            Is_PWM.values[Ifund, :] = Is_fund
            Is.values = Is_PWM.values

        # Store current in OutElec
        self.Is = Is

        # Is_PWM.plot_2D_Data(
        #     "time=axis_data",
        #     "phase[]",
        #     axis_data={"time": self.axes_dict["time"].get_values()},
        # )
