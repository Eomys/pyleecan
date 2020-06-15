from numpy import linspace, floor, zeros, pi, where, sum as np_sum, cos, sqrt, ndarray
import matplotlib.pyplot as plt
import xlrd
from scipy.io.wavfile import write
from scipy.signal import chirp
from scipy.integrate import cumtrapz

# from SciDataTool import Data1D, DataTime


def comp_carrier(time, fswi, type_carrier):
    """Function to compute the carrier
    """
    T = 1 / fswi
    time = time % T

    if type_carrier == 1:  # forward toothsaw carrier
        Y = (
            where(time <= 0.5 * T, time, 0) * time
            + where(time > 0.5 * T, time, 0) * (time - T)
        ) / (0.5 * T)
    elif type_carrier == 2:  # backwards toothsaw carrier
        Y = -(
            where(time <= 0.5 * T, time, 0) * time
            + where(time > 0.5 * T, time, 0) * (time - T)
        ) / (0.5 * T)
    else:  # symmetrical toothsaw carrier
        t1 = (1 + type_carrier) * T / 4
        t2 = T - t1
        Y = (
            where(time <= t1, 1, 0) * time / t1
            + where(time > t1, 1, 0)
            * where(time < t2, 1, 0)
            * (-time + 0.5 * T)
            / (-t1 + 0.5 * T)
            + where(time >= t2, 1, 0) * (time - T) / (T - t2)
        )
    return Y


# Load parameters from the excel file
XLS_PATH = "C:/Users/Pierre/Desktop/Happy_birthday_temps_frequence.xlsx"
book = xlrd.open_workbook(XLS_PATH)
sheet = book.sheet_by_index(0)
length_list = list()
fswi_list = list()
freq0_list = list()
Tfull_signal = 0
for ii in range(1, sheet.ncols):
    length_list.append(sheet.cell(2, ii).value * 60)
    Tfull_signal += length_list[-1]
    fswi_list.append(sheet.cell(9, ii).value * 16 / 2)
    freq0_list.append(sheet.cell(6, ii).value / 2)

# Generate all signals
Fe = 44100
signal = list()
Nsignal = 0  # Full size of the final signal

# Start with a chirp
Tc = 5
time = linspace(0, Tc, Tc * Fe)
s1 = chirp(t=time, f0=50, t1=Tc, f1=freq0_list[0])
signal.append(zeros((Tc * Fe, 3)))
signal[-1][:, 0] = (s1 + cos(2 * pi * freq0_list[0] * time)) * 0.33

Nsignal += len(time)
length_list[0] *= 3  # Longer first note

# PWM song
for ii in range(len(length_list)):
    # Input and arguments
    freq0 = freq0_list[ii]
    Nper = 1
    time = linspace(0, length_list[ii], int(length_list[ii] * Fe))
    fswi = fswi_list[ii]
    qs = 3
    rot_dir = 1
    Vdc1 = 1
    M = 1
    U0 = M * Vdc1 / (2 * sqrt(2))
    Amod = U0 * sqrt(2)  # magnitude of the modulating signal
    type_carrier = 0

    assert time[0] == 0
    Tstep = time[1] - time[0]
    Tstart = 0
    TFinal = time[-1]
    Nper = floor(freq0 * TFinal)
    Npsim = len(time)
    Nsignal += Npsim

    XU = zeros((Npsim, qs))
    ws = 2 * pi * freq0
    Ts = 1 / freq0
    PhiMod = rot_dir * linspace(0, qs - 1, qs) * 2 * pi / qs

    # asynchronous or synchronous intersective numerical SPWM
    # carrier signal (not necessarily symmetrical or deterministic)
    Fcar = (Vdc1 / 2) * comp_carrier(time, fswi, type_carrier)

    # initialization of phase to phase voltage matrix
    v_pwm = zeros((Npsim, qs))
    # intersective calculations
    for qq in range(qs):
        v_pwm[:, qq] = Amod * cos(2 * pi * freq0 * time.transpose() + PhiMod[qq])
        v_pwm[:, qq] = where(v_pwm[:, qq] >= Fcar, +Vdc1 / 2, -Vdc1 / 2)

    XU = v_pwm
    for qq in range(qs):
        # going from phase to phase voltage v_pwm1 to phase to ground voltage v_pwmA
        # (2/3)*v_pwm2-v_pwm/3-v_pwm3/3 gives a different results XXX
        # I=[1:(q-1) (q+1):qs]; %vector of all phases except q
        XU[:, qq] = v_pwm[:, qq] - np_sum(v_pwm, 1) / qs

    # Integration
    # L = 0.01
    # XU[:-1,0] = 1/L*cumtrapz(XU[:,0],time)
    # XU[-1,0] = XU[0,0]
    signal.append(XU)

# Creating final result
result = zeros((Nsignal, qs))
index = 0
for data in signal:
    result[index : (index + data.shape[0]), :] = data
    index += data.shape[0]


# Integration
# Tf = Tc+sum(length_list)
# time = linspace(0,Tf,Nsignal)
# L = 0.01
# dt = time[1] - time[0]
# time_int = linspace(0,Tf+dt,Nsignal+1)
# XU_int = zeros((Nsignal+1,))
# XU_int[:-1] = result[:,0]
# XU_int[-1] = result[-2,0]
# result = 1/L*cumtrapz(XU_int, time_int)

# Save / Display results
write("result.wav", Fe, result[:, 0])
plt.plot(result[:, 0])
plt.show()
