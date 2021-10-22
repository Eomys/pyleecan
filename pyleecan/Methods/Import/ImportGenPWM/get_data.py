# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:57:25 2020

@author: Sijie
"""


import numpy as np
from ....Functions.Electrical.comp_PWM import comp_volt_PWM_NUM


def get_data(self, is_norm=True):
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
    N = int(self.fs * self.duration)  # Number of points
    Tpwmu = np.linspace(0, N / self.fs, N, endpoint=False)  # Time vector
    v_pwm, Vas, MI, carrier = comp_volt_PWM_NUM(
        Tpwmu=Tpwmu,
        freq0=self.f,
        freq0_max=self.fmax,
        fmode=self.fmode,
        fswimode=self.fswimode,
        fswi=self.fswi,
        fswi_max=self.fswi_max,
        qs=self.qs,
        Vdc1=self.Vdc1,
        U0=self.U0,
        type_carrier=self.type_carrier,
        rot_dir=self.rot_dir,
        type_DPWM=self.typePWM,
        PF_angle=0,
        var_amp=self.var_amp,
        is_norm=is_norm,
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
    return Vpwm, Vas, MI, carrier, Tpwmu
