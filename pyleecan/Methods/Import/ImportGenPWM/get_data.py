# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:57:25 2020

@author: Sijie
"""


import numpy as np
from ....Functions.Electrical.comp_PWM import comp_volt_PWM_NUM


def get_data(self):
    """Generate the PWM matrix

    Parameters
    ----------
    self : ImportGenPWM
        An ImportGenPWM object

    Returns
    -------
    matrix: ndarray
        The generated PWM matrix

    """
    # Tpwmu=np.arange(fs*duration)/fs,
    Tpwmu = np.linspace(0, self.duration, self.fs * self.duration, endpoint=True)
    v_pwm, Vas, MI, triangle = comp_volt_PWM_NUM(
        Tpwmu=Tpwmu,
        freq0=self.f,
        freq0_max=self.fmax,
        fmode=self.fmode,
        fswimode=self.fswimode,
        fswi=self.fswi,
        fswi_max=self.fswi_max,
        qs=3,
        Vdc1=self.Vdc1,
        U0=self.U0,
        type_carrier=self.type_carrier,
        rot_dir=-1,
        type_DPWM=self.typePWM,
        PF_angle=0,
        is_plot=False,
        var_amp=self.var_amp,
    )

    ref = np.zeros(np.size(v_pwm[0])).astype(np.float32)
    PWM1 = np.where(v_pwm[0] < ref, -1, 1)  # .astype(np.float32)
    PWM2 = np.where(v_pwm[1] < ref, -1, 1)  # .astype(np.float32)
    PWM3 = np.where(v_pwm[2] < ref, -1, 1)  # .astype(np.float32)
    Triphase = np.column_stack([PWM1, PWM2, PWM3])
    return Triphase, Vas, MI, triangle
