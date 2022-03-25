import numpy as np

import matplotlib.pyplot as plt


def get_data(self, is_norm=True, is_plot=False, Time=None):
    """Generate the PWM matrix

    Parameters
    ----------
    self : ImportGenPWM
        An ImportGenPWM object
    is_norm : bool
        True to normalize signal

    Returns
    -------
    vpwm : ndarray
        n-phase PWM voltage waveform
    Vas : ndarray
        modulation waveform
    MI : float
        modulation index
    carrier : ndarray
        carrier waveform
    Tpwmu : ndarray
        time vector
    """

    if Time is None:
        # Number of points
        N = int(self.fs * self.duration)
        # Define time vector
        Tpwmu = np.linspace(0, self.duration, N, endpoint=False)
    else:
        Tpwmu = Time.get_values(is_smallestperiod=True)

    # Get PWM voltage values
    v_pwm, Vas, MI, carrier = self.comp_voltage(
        Tpwmu=Tpwmu, PF_angle=0, is_norm=is_norm, is_sin=False
    )

    if is_norm:
        ref = np.zeros(np.size(v_pwm[0])).astype(np.float32)
        PWM1 = np.where(v_pwm[0] < ref, -1, 1)  # .astype(np.float32)
        PWM2 = np.where(v_pwm[1] < ref, -1, 1)  # .astype(np.float32)
        PWM3 = np.where(v_pwm[2] < ref, -1, 1)  # .astype(np.float32)
    else:
        PWM1 = v_pwm[0]
        PWM2 = v_pwm[1]
        PWM3 = v_pwm[2]
    Vpwm = np.column_stack([PWM1, PWM2, PWM3])

    if self.is_star:  # star coupling
        mean = Vpwm.mean(axis=1)
        PWM1 = PWM1 - mean
        PWM2 = PWM2 - mean
        PWM3 = PWM3 - mean
        Vpwm = np.column_stack([PWM1, PWM2, PWM3])

    if is_plot:
        Nt = 10000
        plt.figure()
        plt.plot(Tpwmu[:Nt], carrier[:Nt])
        plt.plot(Tpwmu[:Nt], v_pwm[0, :Nt])
        plt.plot(Tpwmu[:Nt], Vas[:Nt])

        plt.figure()
        plt.plot(Tpwmu[:Nt], carrier[:Nt])
        plt.plot(Tpwmu[:Nt], Vpwm[:Nt, 0])
        plt.plot(Tpwmu[:Nt], Vas[:Nt])
        plt.show()

        plt.figure()
        plt.plot(Tpwmu[:Nt], mean[:Nt])

    return Vpwm, Vas, MI, carrier, Tpwmu
