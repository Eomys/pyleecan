import numpy as np
import matplotlib.pyplot as plt
import time

from SciDataTool.Functions.Plot.plot_3D import plot_3D

t0 = time.time()

# % SDM validation step 1.1 :
# % Paper Lubin 2010b and Lubin_2011b
# % Machine with no load rotor, rotor slots, current sheet on stator side

# %% VALIDATION CASES
# % 0 = Lubin_2010a fig.6
# % 1 = Lubin_2010a fig.11
# % 2 = Lubin_2010a fig.12
# % 3 = Lubin_2011b fig.5
validation_case = 3


# %% PROBLEM PARAMETERS

mu_0 = np.pi * 4e-7

R_1 = 0.04
R_2 = 0.07
R_3 = 0.08
L = 0.1

theta_i0 = 135 * np.pi / 180

N = 50
K = 50

K_1 = 1e5

if validation_case == 0:
    Z_r = 1
    p = 1
    alpha = 0
    beta = 0.78
    m = 1


if validation_case == 1:
    Z_r = 4
    p = 2
    N = 50
    K = 50
    K_1 = 1e5
    theta_i0 = 135 * np.pi / 180
    alpha = np.pi / 4
    beta = 0.78
    m = 1


if validation_case == 2:
    Z_r = 4
    p = 2
    N = 50
    K = 50
    K_1 = 1e5
    theta_i0 = 135 * np.pi / 180
    alpha = 0

    m = 1


if validation_case == 3:
    Z_r = 18
    p = 2
    N = 200
    K = 20
    K_1 = 8e4
    theta_i0 = 140 * np.pi / 180
    alpha = np.pi / 2
    beta = 0.6 * 3.14 / Z_r
    m = 1
    R_1 = 0.04
    R_2 = 0.06
    R_3 = 0.063
    L = 0.5


# %% AIRGAP FLUX COMPUTATION

i = np.arange(0, Z_r) + 1
k = np.arange(0, K) + 1
n = np.arange(0, N) + 1

kni, nik, ikn = np.meshgrid(k, n, i)

kni = np.reshape(kni, (N, K * Z_r))
nik = np.reshape(nik, (N, K * Z_r))
ikn = np.reshape(ikn, (N, K * Z_r))

theta_rot = np.linspace(0, 2 * np.pi, 100)

Csts = np.zeros((100, 4 * N + K * Z_r))

for ii, a0 in enumerate(theta_rot):
    theta_i = 2 * np.pi / Z_r * (i - 1) + theta_i0 + a0
    theta_ikn = 2 * np.pi / Z_r * (ikn - 1) + theta_i0 * np.ones(ikn.shape) + a0

    I_coskcosni = (
        beta**2
        * nik
        * (
            (-1) ** kni * np.sin(nik * (beta + 2 * theta_ikn) / 2)
            + np.sin(nik * (beta - 2 * theta_ikn) / 2)
        )
        / (beta**2 * nik**2 - np.pi**2 * kni**2)
    )
    I_cosksinni = (
        beta**2
        * nik
        * (
            -((-1) ** kni) * np.cos(nik * (beta + 2 * theta_ikn) / 2)
            + np.cos(nik * (beta - 2 * theta_ikn) / 2)
        )
        / (beta**2 * nik**2 - np.pi**2 * kni**2)
    )

    P_nik_R2_R3 = (R_3 / R_2) ** nik + (R_2 / R_3) ** nik
    E_nik_R2_R3 = -((R_3 / R_2) ** nik) + (R_2 / R_3) ** nik
    E_kni_R1_R2 = -((R_2 / R_1) ** (np.pi * kni / beta)) + (R_1 / R_2) ** (
        np.pi * kni / beta
    )
    P_kni_R1_R2 = (R_2 / R_1) ** (np.pi * kni / beta) + (R_1 / R_2) ** (
        np.pi * kni / beta
    )

    Jm_cos = np.zeros(N)
    Jm_cos[m * p - 1] = mu_0 * K_1 * np.cos(m * p * (alpha + a0))

    Jm_sin = np.zeros(N)
    Jm_sin[m * p - 1] = mu_0 * K_1 * np.sin(m * p * (alpha + a0))

    M15 = 1 / (R_2 * beta) * I_coskcosni * kni * E_kni_R1_R2 / P_kni_R1_R2

    M35 = 1 / (R_2 * beta) * I_cosksinni * kni * E_kni_R1_R2 / P_kni_R1_R2

    M51 = -2 * R_2 / beta * I_coskcosni * P_nik_R2_R3 / (nik * E_nik_R2_R3)
    M52 = 4 * R_3 / beta * I_coskcosni / (nik * E_nik_R2_R3)
    M53 = -2 * R_2 / beta * I_cosksinni * P_nik_R2_R3 / (nik * E_nik_R2_R3)
    M54 = 4 * R_3 / beta * I_cosksinni / (nik * E_nik_R2_R3)

    L1 = np.concatenate(
        (np.eye(N), np.zeros((N, N)), np.zeros((N, N)), np.zeros((N, N)), M15), axis=1
    )

    L2 = np.concatenate(
        (
            np.zeros((N, N)),
            np.eye(N),
            np.zeros((N, N)),
            np.zeros((N, N)),
            np.zeros((N, Z_r * K)),
        ),
        axis=1,
    )

    L3 = np.concatenate(
        (np.zeros((N, N)), np.zeros((N, N)), np.eye(N), np.zeros((N, N)), M35), axis=1
    )

    L4 = np.concatenate(
        (
            np.zeros((N, N)),
            np.zeros((N, N)),
            np.zeros((N, N)),
            np.eye(N),
            np.zeros((N, Z_r * K)),
        ),
        axis=1,
    )

    L5 = np.concatenate((M51.T, M52.T, M53.T, M54.T, np.eye(Z_r * K)), axis=1)

    Mat = np.concatenate((L1, L2, L3, L4, L5), axis=0)

    Vect = np.concatenate((np.zeros(N), Jm_cos, np.zeros(N), Jm_sin, np.zeros(Z_r * K)))

    Csts[ii, :] = np.linalg.solve(Mat, Vect)

A_In = Csts[:, :N]
B_In = Csts[:, N : 2 * N]
C_In = Csts[:, 2 * N : 3 * N]
D_In = Csts[:, 3 * N : 4 * N]

theta = np.arange(0, 360) * np.pi / 180

thetan, ntheta = np.meshgrid(theta, n)

r = (R_2 + R_3) / 2
# % r = R_2
n = n[None, :]
P_n_r_R3 = (r / R_3) ** n + (R_3 / r) ** n
P_n_r_R2 = (r / R_2) ** n + (R_2 / r) ** n
E_n_r_R3 = (r / R_3) ** n - (R_3 / r) ** n
E_n_r_R2 = (r / R_2) ** n - (R_2 / r) ** n
E_n_R2_R3 = -((R_3 / R_2) ** n) + (R_2 / R_3) ** n


cosn = np.cos(ntheta * thetan)
sinn = np.sin(ntheta * thetan)

Bthetag_cos = -(
    R_2 / r * A_In * E_n_r_R3 / E_n_R2_R3 - R_3 / r * B_In * E_n_r_R2 / E_n_R2_R3
)
Bthetag_sin = -(
    R_2 / r * C_In * E_n_r_R3 / E_n_R2_R3 - R_3 / r * D_In * E_n_r_R2 / E_n_R2_R3
)
Bthetag = np.matmul(Bthetag_cos, cosn) + np.matmul(Bthetag_sin, sinn)

Brg_sin = -(
    R_2 / r * A_In * P_n_r_R3 / E_n_R2_R3 - R_3 / r * B_In * P_n_r_R2 / E_n_R2_R3
)
Brg_cos = R_2 / r * C_In * P_n_r_R3 / E_n_R2_R3 - R_3 / r * D_In * P_n_r_R2 / E_n_R2_R3
Brg = np.matmul(Brg_cos, cosn) + np.matmul(Brg_sin, sinn)

print("Elapsed time: " + str(time.time() - t0))

# %% PLOT

plt.figure()
plt.plot(theta, Brg[0, :], "k")
plt.plot(theta, Bthetag[0, :], "r")
plt.show()
# plt.figure()
# plt.plot(n[0], Brg_cos[0, :], "k")
# plt.plot(n[0], Brg_sin[0, :], "r")

# plt.show()

plot_3D(
    theta_rot,
    theta,
    Brg,
    type_plot="pcolor",
    y_min=0,
    y_max=theta.max(),
    x_min=0,
    x_max=theta_rot.max(),
)

pass

# subplot(2,2,2)
# bar(Brg_cos)
# hold on
# bar(Brg_sin, 'r')
# subplot(2,2,4)
# bar(Bthetag_cos)
# hold on
# bar(Bthetag_sin, 'r')
