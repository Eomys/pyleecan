import numpy as np

from SciDataTool import DataTime, Data1D


def gen_drive(self, output):
    """Generate the drive for the equivalent electrical circuit (only PWM drive for now)

    Parameters
    ----------
    self : Electrical
        an Electrical object
    output : Output
        an Output object
    """

    self.get_logger().info("Calculating PWM voltage")

    p = output.simu.machine.get_pole_pair_number()

    # Get PWM object
    PWM = output.elec.PWM

    if PWM.U0 in [0, None]:
        raise Exception("Cannot calculate PWM voltage if PWM.U0 is None or 0")

    # Get operating point
    OP = output.elec.OP

    if PWM.is_star:
        # Calculate modulation index to account for quick variations
        M_I = PWM.get_modulation_index()

        # Number of points depends on modulation index
        PWM.fs /= max([M_I, 0.05])

    # Number of points depends on modulation index
    Nt_tot = int(PWM.fs * PWM.duration)

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

    # Get DataFreq object and frequency axis by taking FFT
    Us_df = Us_dt.get_data_along("freqs<" + str(self.freq_max), "phase")
    Freqs = Us_df.axes[0]
    freqs = Freqs.get_values()

    # Filter frequencies with low amplitude and create new frequency axis
    Un_norm = np.linalg.norm(Us_df.values, axis=-1)
    Iamp_n = Un_norm > 1e-2 * Un_norm.max()
    Us_df.axes[0] = Data1D(
        name=Freqs.name,
        unit=Freqs.unit,
        symbol=Freqs.symbol,
        values=freqs[Iamp_n],
        normalizations=Freqs.normalizations,
        is_components=False,
        symmetries=Freqs.symmetries,
    )
    Us_df.values = Us_df.values[Iamp_n, :]

    # Store voltage spectrum in OutElec
    output.elec.Us = Us_dt.to_datadual(datafreq=Us_df)

    # Store Time_PWM axis in axes_dict
    output.elec.axes_dict["time"] = Time_PWM

    # Us_dt.plot_2D_Data("time", "phase[]")
