import numpy as np

from scipy import signal, integrate


def comp_voltage(self, Tpwmu, PF_angle=0, is_sin=True, is_norm=True):
    """Generalized DPWM using numerical method according to
    'Impact of Modulation Schemes on DC-Link Capacitor of VSI in HEV Applications'

    Parameters
    ----------
    Tpwmu : ndarray
        time vector
    PF_angle: float
        power factor angle only for GDPWM, default to 0
    is_sin: bool
        True to generate sine wave, False to generate cosine wave
    is_norm: int
        True to normalize signal between -1 and 1

    Returns
    -------
     v_pwm : ndarray
        n-phase PWM voltage waveform
     Vas : ndarray
        modulation waveform
     M_I : float
        modulation index
     carrier : ndarray
        carrier waveform

    """

    freq0 = self.f
    freq0_max = self.fmax
    fmode = self.fmode
    fswimode = self.fswimode
    fswi = self.fswi
    fswi_max = self.fswi_max
    qs = self.qs
    Vdc1 = self.Vdc1
    phase_dir = self.phase_dir
    type_DPWM = self.typePWM
    var_amp = self.var_amp
    current_dir = self.current_dir
    Phi0 = self.Phi0

    # Check inputs
    if type_DPWM != 8:
        if fswimode in [1, 4]:
            raise Exception("Only Sine PWM supports the variable fundamental frequency")
        if fmode == 1:
            raise Exception("Only Sine PWM supports the variable fundamental frequency")

    Npsim = len(Tpwmu)
    carrier = np.ones(len(Tpwmu))

    if fmode == 0:  # Fixed speed:
        ws = current_dir * 2 * np.pi * freq0

    elif fmode == 1:  # Variable speed:
        freq0_array = (freq0_max - freq0) / Tpwmu[-1] * Tpwmu + freq0 * np.ones(Npsim)
        ws = current_dir * np.pi * freq0_array

    if fswimode == 0:  # Fixed fswi:
        if type_DPWM == 8:
            carrier = Vdc1 / 2 * self.comp_carrier(Tpwmu)
        else:
            Th = 1 / fswi

    elif fswimode == 1:  # Variable fswi (ramp):
        wswiT = current_dir * (
            np.pi * (fswi_max - fswi) / Tpwmu[-1] * Tpwmu**2 + 2 * np.pi * fswi * Tpwmu
        )
        carrier = Vdc1 / 2 * signal.sawtooth(wswiT, 0.5)

    elif fswimode == 2 or fswimode == 3:  # Random fswi & Symmetrical random fswi
        t1 = round(Tpwmu[-1] * 5000000)  # Number of points
        if fswimode == 3:
            num_slice = round((fswi_max + fswi) / 2 * Tpwmu[-1])
            delta_fswi = np.random.randint(
                fswi, high=fswi_max + 1, size=num_slice * 2, dtype=int
            )
            delta_fswi[1::2] = delta_fswi[0::2] * -1

        else:
            num_slice = round((fswi_max + fswi) / 2 * Tpwmu[-1])
            delta_fswi = np.random.randint(
                fswi, high=fswi_max + 1, size=num_slice * 2, dtype=int
            )
            delta_fswi[1::2] = delta_fswi[1::2] * -1

        fswi_base = np.array(np.ones(t1))
        S_delta = 1
        delta_t = S_delta / abs(delta_fswi)
        time = sum(delta_t)
        delta_point = delta_t[:-1] / time * t1
        delta_point = np.array(delta_point)
        delta_point = np.append(delta_point, t1 - sum(delta_point))
        fswi = np.concatenate(
            [
                fswi_base[0 : round(delta_point[ii])] * delta_fswi[ii]
                for ii in range(len(delta_fswi))
            ]
        )
        if len(fswi) < t1:
            fswi = np.concatenate((fswi, fswi[-1] * np.ones(t1 - len(fswi))))
        else:
            fswi = fswi[:t1]

        Tpwmu_10 = np.linspace(0, (t1 - 1) / 5000000, t1, endpoint=True)
        np.linspace(0, (t1 - 1) / 5000000, t1, endpoint=True)
        carrier = integrate.cumtrapz(fswi, Tpwmu_10, initial=0)
        Aml_tri = max(carrier)
        carrier = carrier / Aml_tri * Vdc1 - Vdc1 / 2 * np.ones(np.size(Tpwmu_10))
        carrier = signal.resample(carrier, len(Tpwmu))

    elif fswimode == 4:  # Random amplitude carrier wave
        carrier = Vdc1 / 2 * (self.comp_carrier(Tpwmu))
        num_slice = int(fswi * Tpwmu[-1])
        delta_amp = np.random.randint(
            -var_amp, high=var_amp + 1, size=int(num_slice), dtype=int
        ) / 100 + np.ones(int(num_slice))

        amp_base = np.ones(len(Tpwmu))
        S_delta = 1

        delta_t = S_delta / fswi * np.ones(int(num_slice))

        delta_point = np.round(delta_t / Tpwmu[-1], 4) * len(Tpwmu)
        delta_point = np.array(delta_point).astype(int)
        amp = np.concatenate(
            [
                amp_base[0 : delta_point[ii]] * delta_amp[ii]
                for ii in range(len(delta_amp))
            ]
        )
        if len(amp) < len(Tpwmu):
            amp = np.concatenate((amp, amp[-1] * np.ones(len(Tpwmu) - len(amp))))
        else:
            amp = amp[: len(Tpwmu)]
        carrier = carrier * amp

    M_I = self.get_modulation_index()

    k = 1  # 2/sqrt(3)#2/sqrt(3) factor to have higher fundamental compared to SPWM
    if phase_dir == -1:
        Phase = [0, -1, 1]
    else:
        Phase = [0, 1, -1]

    amp = k * M_I * (Vdc1 / 2)
    angle0 = ws * Tpwmu + Phi0

    if is_sin:
        Vas = amp * np.sin(angle0 + Phase[0] * 2 * np.pi / 3)
        Vbs = amp * np.sin(angle0 + Phase[1] * 2 * np.pi / 3)
        Vcs = amp * np.sin(angle0 + Phase[2] * 2 * np.pi / 3)

    else:
        Vas = amp * np.cos(angle0 + Phase[0] * 2 * np.pi / 3)
        Vbs = amp * np.cos(angle0 + Phase[1] * 2 * np.pi / 3)
        Vcs = amp * np.cos(angle0 + Phase[2] * 2 * np.pi / 3)

    if type_DPWM == 8:
        v_pwm = np.zeros((qs, Npsim))
        amp_dc = 1 if is_norm else Vdc1 / 2

        v_pwm[0] = np.where(Vas < carrier, -amp_dc, amp_dc)
        v_pwm[1] = np.where(Vbs < carrier, -amp_dc, amp_dc)
        v_pwm[2] = np.where(Vcs < carrier, -amp_dc, amp_dc)
    else:
        V_min = np.amin(
            np.concatenate((Vas[:, None], Vbs[:, None], Vcs[:, None]), axis=1), axis=1
        )
        V_max = np.amax(
            np.concatenate((Vas[:, None], Vbs[:, None], Vcs[:, None]), axis=1), axis=1
        )

        alpha_rad = 0

        if type_DPWM == 0:  # GDPWM
            if PF_angle >= -np.pi / 6 and PF_angle <= np.pi / 6:
                alpha_rad = PF_angle
            elif PF_angle > np.pi / 6 and PF_angle <= 5 * np.pi / 12:
                alpha_rad = np.pi / 6
            elif PF_angle >= -5 * np.pi / 12 and PF_angle < -np.pi / 6:
                alpha_rad = -np.pi / 6
            elif PF_angle > 5 * np.pi / 12 and PF_angle <= np.pi / 2:
                alpha_rad = np.pi / 3
            elif PF_angle >= -np.pi / 2 and PF_angle < -5 * np.pi / 12:
                alpha_rad = -np.pi / 3

        elif type_DPWM == 3:  # elif type_waveform==63 #DPWM0
            alpha_rad = -30 * np.pi / 180
        elif type_DPWM == 4:  # elif type_waveform==64 #DPWM1
            alpha_rad = 0
        elif type_DPWM == 5:  # elif type_waveform==65 #DPWM2
            alpha_rad = 30 * np.pi / 180

        angle1 = angle0 - alpha_rad
        if is_sin:
            Vas_g = amp * np.sin(angle1 + Phase[0] * 2 * np.pi / 3)
            Vbs_g = amp * np.sin(angle1 + Phase[1] * 2 * np.pi / 3)
            Vcs_g = amp * np.sin(angle1 + Phase[2] * 2 * np.pi / 3)
        else:
            Vas_g = amp * np.cos(angle1 + Phase[0] * 2 * np.pi / 3)
            Vbs_g = amp * np.cos(angle1 + Phase[1] * 2 * np.pi / 3)
            Vcs_g = amp * np.cos(angle1 + Phase[2] * 2 * np.pi / 3)

        V_offset = np.zeros(Npsim)

        min_abc = np.squeeze(
            np.amin(
                np.concatenate(
                    (Vas_g[:, None], Vbs_g[:, None], Vcs_g[:, None]), axis=1
                ),
                axis=1,
            )
        )
        max_abc = np.squeeze(
            np.amax(
                np.concatenate(
                    (Vas_g[:, None], Vbs_g[:, None], Vcs_g[:, None]), axis=1
                ),
                axis=1,
            )
        )
        i1 = min_abc + max_abc > 0
        i2 = min_abc + max_abc < 0
        V_offset[i1] = Vdc1 / 2 - V_max[i1]
        V_offset[i2] = -Vdc1 / 2 - V_min[i2]

        # type_DPWM {0, 1, 2, 3, 4, 5, 6, 7} # {GDPWM, DPWMMIN, DPWMMAX, DPWM0, DPWM1, DPWM2, DPWM3, SVPWM)
        if type_DPWM == 1:  # type_waveform==61 #DPWMMIN
            V_offset = -V_min - Vdc1 / 2
        elif type_DPWM == 2:  # elif type_waveform==62 #DPWMMAX
            V_offset = -V_max + Vdc1 / 2
        elif type_DPWM == 6:  # elif type_waveform==66 #DPWM3
            min_abc = np.amin(
                np.concatenate((Vas[:, None], Vbs[:, None], Vcs[:, None]), axis=1),
                axis=1,
            )
            max_abc = np.amax(
                np.concatenate((Vas[:, None], Vbs[:, None], Vcs[:, None]), axis=1),
                axis=1,
            )
            i1 = min_abc + max_abc < 0
            i2 = min_abc + max_abc > 0
            V_offset[i1] = Vdc1 / 2 - V_max[i1]
            V_offset[i2] = -Vdc1 / 2 - V_min[i2]
        elif type_DPWM == 7:  # elif type_waveform==67 #SVPWM
            V_offset = -1 / 2 * (V_max + V_min)

        Van = Vas + V_offset
        Vbn = Vbs + V_offset
        Vcn = Vcs + V_offset

        T1 = Th / 4 - Th / (2 * Vdc1) * Van
        T2 = Th / 4 - Th / (2 * Vdc1) * Vbn
        T3 = Th / 4 - Th / (2 * Vdc1) * Vcn
        n = np.floor(Tpwmu / Th).astype(int)
        v_pwm = Vdc1 / 2 * np.ones((qs, Npsim))
        v_pwm[0, Tpwmu < (T1 + n * Th)] = -Vdc1 / 2
        v_pwm[0, Tpwmu > ((n + 1) * Th - T1)] = -Vdc1 / 2
        v_pwm[1, Tpwmu < (T2 + n * Th)] = -Vdc1 / 2
        v_pwm[1, Tpwmu > ((n + 1) * Th - T2)] = -Vdc1 / 2
        v_pwm[2, Tpwmu < (T3 + n * Th)] = -Vdc1 / 2
        v_pwm[2, Tpwmu > ((n + 1) * Th - T3)] = -Vdc1 / 2

    return v_pwm, Vas, M_I, carrier
