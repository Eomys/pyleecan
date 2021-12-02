import numpy as np

from SciDataTool import DataTime


def gen_drive(self, output):
    """Generate the drive for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    output : Output
        an Output object

    Returns
    ----------
    Us_dqh_freq: DataFreq
        Harmonic content of stator voltage in dqh frame
    """

    self.get_logger().info("Calculating PWM voltage")

    p = output.simu.machine.get_pole_pair_number()

    # Get PWM object
    PWM = output.elec.PWM

    # Get operating point
    OP = output.elec.OP

    # Get the number of switching groups
    PWM.Nswi = int(np.ceil(self.freq_max / PWM.fswi))

    if PWM.is_star:
        # Calculate modulation index to account for quick variations
        M_I = PWM.get_modulation_index()

        # Number of points depends on modulation index
        PWM.fs /= max([M_I, 0.05])

    # Number of points depends on modulation index
    Nt_tot = int(PWM.fs * PWM.duration)

    # Get PWM theoretical frequencies
    Freqs_op, orders = output.elec.get_freqs_th(is_dqh=False, freq_max=self.freq_max)
    freqs_th = Freqs_op.values

    # Get time axis
    input_pwm = type(output.simu.input)(
        OP=OP,
        Nt_tot=Nt_tot,
        t_final=PWM.duration,
        current_dir=output.elec.current_dir,
        rot_dir=output.geo.rot_dir,
    )
    Time_PWM = input_pwm.comp_axis_time(p, per_t=1, is_antiper_t=False)

    # Generate PWM signal
    Uabc = PWM.get_data(is_norm=False, Time=Time_PWM)[0]

    # Get phase axis
    stator_label = output.simu.machine.stator.get_label()
    Phase = output.elec.axes_dict["phase_" + stator_label]

    # Create DataTime object
    Us_dt = DataTime(
        name="Stator voltage",
        symbol="U_s",
        unit="V",
        axes=[Time_PWM, Phase],
        values=Uabc,
    )

    # Recalculate PWM voltage waveform with convenient supply frequency
    if self.type_calc_PWM_harm == 1:
        # Copy PWM object
        PWM_bis = output.elec.PWM.copy()

        # Calculate PWM harmonics for fswi multiple of felec
        PWM_bis.f = PWM_bis.fswi / (4 * PWM_bis.Nsidebands)
        PWM_bis.duration = 2 * p / PWM_bis.f
        OP_bis = output.elec.OP.copy()
        OP_bis.felec = PWM_bis.f
        OP_bis.N0 = 60 * PWM_bis.f / p

        # Calculate theoretical frequencies for dummy felec
        f_PWM = np.array([0, PWM_bis.f, PWM_bis.fswi])
        freqs_th_bis = np.abs(np.matmul(orders, f_PWM[:, None])[:, 0])

        # adjust PWM maximum frequency
        PWM_bis.fs = max([2 * freqs_th_bis.max(), PWM_bis.fs])

        # Get time axis
        input_pwm_bis = type(output.simu.input)(
            OP=OP_bis,
            Nt_tot=Nt_tot,
            t_final=PWM_bis.duration,
            current_dir=output.elec.current_dir,
            rot_dir=output.geo.rot_dir,
        )
        Time_PWM_bis = input_pwm_bis.comp_axis_time(p, per_t=1, is_antiper_t=False)

        # Generate PWM signal
        Uabc_bis = PWM_bis.get_data(is_norm=False, Time=Time_PWM_bis)[0]

        # Create DataTime object
        Us_dt_bis = DataTime(
            name="Stator voltage",
            symbol="U_s",
            unit="V",
            axes=[Time_PWM_bis, Phase],
            values=Uabc_bis,
        )

    if self.type_calc_PWM_harm == 1:
        # Get FFT frequency vector
        freqs_fft = Time_PWM_bis.get_values(operation="time_to_freqs")

        # Find closest index of each frequency in the grid
        If = np.argmin(np.abs(freqs_fft[:, None] - freqs_th_bis[None, :]), axis=0)

        # Extract data at theoretical frequencies
        Us_df = Us_dt_bis.get_data_along("freqs" + str(If.tolist()), "phase")

        # Map theoretical frequencies to operational frequencies
        Us_df.axes[0] = Freqs_op

    else:
        # Filter harmonics in spectrum removing leakage
        Us_df = Us_dt.filter_spectral_leakage(freqs_th)

    # Store voltage spectrum in OutElec
    output.elec.Us = Us_dt.to_datadual(Us_df)

    # Store Time_PWM axis in axes_dict
    output.elec.axes_dict["time"] = Time_PWM

    # Us_dt.plot_2D_Data("time", "phase[]")
    # Us_df.plot_2D_Data("freqs", "phase[0]", data_list=[Us_dt, Us_df1], barwidth=500)
