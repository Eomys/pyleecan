from numpy import pi, interp


def solve_EEC(self, output):
    """Compute the parameters dict for the equivalent electrical circuit
    TODO find ref. to cite
    cf "Title"
    Autor, Publisher

                  --->                     ---->
     -----Rs------XsIs---- --- -----Rr'----XrIr----
    |                     |   |                       |
    |                     Rfe Xm                      Rr*(s-1)/s
    |                     |   |                       |
     ---------Is---------- --- ---------Ir------------

             --->
              Us

    Parameters
    ----------
    self : EEC_SCIM
        an EEC_SCIM object
    output : Output
        an Output object
    """
    Rs = self.parameters["R1"]
    Rr = self.parameters["R2"]
    Rfe = self.parameters["Rfe"]
    Ls = self.parameters["L1"]
    Lr = self.parameters["L2"]
    Phi_m = self.parameters["Phi_m"]
    I_m = self.parameters["I_m"]
    K21Z = self.parameters["K21Z"]
    slip = self.parameters["slip"]
    U0_ref = self.parameters["U0_ref"]

    felec = output.elec.felec
    ws = 2 * pi * felec

    # solving elementary system, initial start with unsaturated inductance
    Lm_init = Phi_m[0] / I_m[0]
    I1, I2, Im, If, Lm, delta_Lm = solve_EEC_elementary(
        U0_ref, Rs, Rr, Ls, Lr, Rfe, ws, slip, Phi_m, I_m, Lm_init
    )
    if len(Phi_m) > 1:
        # iteration until convergence is reached, and max number of iterations on EEC
        delta_Lm_max = 1e-6
        Nmax = 20
        niter_Lm = 1
        while abs(delta_Lm) > delta_Lm_max and niter_Lm < Nmax:
            Lm_init = Lm
            I1, I2, Im, If, Lm, delta_Lm = solve_EEC_elementary(
                U0_ref, Rs, Rr, Ls, Lr, Rfe, ws, slip, Phi_m, I_m, Lm_init
            )

            niter_Lm = niter_Lm + 1

    # output.elec.Id_ref = real(I1)  # real part of phase current, use Id_ref for now
    # output.elec.Iq_ref = real(I2)  # imag part of phase current, use Iq_ref for now
    output.elec.I10 = I1
    output.elec.I20 = I2

    # # Compute stator currents
    # output.elec.Is = None
    # output.elec.Is = output.elec.get_Is()

    # # Compute stator voltage
    # output.elec.Us = None
    # output.elec.Us = output.elec.get_Us()

    # # Compute rotor currents
    # time = output.elec.axes_dict["time"].get_values(is_oneperiod=True)
    # Nt = time.size
    # qsr = output.simu.machine.rotor.winding.qs
    # sym = output.simu.machine.comp_periodicity_spatial()[0]

    # Ir_ = tile(Ir_norm, (Nt, 1)) * norm

    # w_slip = ws * slip

    # # Get rotation direction
    # rot_dir = output.get_rot_dir()

    # # compute actual rotor bar currents
    # # TODO fix: initial rotor pos. is disregarded for now
    # Ir = dq2n(Ir_, w_slip * time, n=qsr // sym, rot_dir=rot_dir, is_n_rms=False)
    # Ir = tile(Ir, (1, sym))

    # Phase = Data1D(
    #     name="phase",
    #     unit="",
    #     values=gen_name(qsr),
    #     is_components=True,
    # )
    # output.elec.Ir = DataTime(
    #     name="Rotor current",
    #     unit="A",
    #     symbol="Ir",
    #     axes=[Phase, output.elec.axes_dict["time"].copy()],
    #     values=Ir.T,
    # )


def solve_EEC_elementary(U0, R1, R2, L1, L2, Rfe, ws, slip, Phi_m, I_m, Lm_init):
    # basic matrix solver of SCIM EEC in complex domain

    if Lm_init is None:
        # estimation of magnetization inductance based on unsaturated inductance
        Lm_init = Phi_m[0] / I_m[0]

    Xm = ws * Lm_init
    X1 = ws * L1
    X2 = ws * L2
    Zm = 1j * Xm
    # magnetizing branch impedance, including iron loss resistance
    Zmf = 1 / (1 / Zm + 1 / Rfe)

    # rotor impedance
    Z2 = 1j * X2 + R2 / slip

    # stator impedance
    Z1 = 1j * X1 + R1

    # total impedance
    if slip != 0:
        Ztot = Z1 + 1 / (1 / Zmf + 1 / Z2)
    else:
        Ztot = Z1 + Zmf

    I1 = (U0 + 1j * 0) / Ztot
    E = U0 - Z1 * I1
    Im = E / Zm
    If = E / Rfe
    I2 = I1 - (Im + If)

    # recalculating magnetizing inductance
    Phim = interp(abs(Im), I_m, Phi_m)

    Lm = Phim / abs(Im)

    # calculation of non linearity effect (should be ->0 when Lm(Im)=Lm_init)
    delta_Lm = abs((Lm - Lm_init) / Lm_init)

    # A = array(
    #         [
    #             # sum of (real and imaginary) voltages equals the input voltage Us
    #             [ 1,  0, Rs, -Xs,  0,   0,    0,    0,   0,   0, ],
    #             [ 0,  1, Xs,  Rs,  0,   0,    0,    0,   0,   0, ],
    #             # sum of (real and imaginary) currents are zeros
    #             [ 0,  0, -1,   0,  1,   0,    1,    0,   1,   0, ],
    #             [ 0,  0,  0,  -1,  0,   1,    0,    1,   0,   1, ],
    #             # j*Xm*Im = Um
    #             [-1,  0,  0,   0,  0, -Xm,    0,    0,   0,   0, ],
    #             [ 0, -1,  0,   0, Xm,   0,    0,    0,   0,   0, ],
    #             # (Rr'/s + j*Xr')*Ir' = Um
    #             [-1,  0,  0,   0,  0,   0, Rr_s,  -Xr,   0,   0, ],
    #             [ 0, -1,  0,   0,  0,   0,   Xr, Rr_s,   0,   0, ],
    #             # Rfe*Ife = Um
    #             [-1,  0,  0,   0,  0,   0,    0,    0, Rfe,   0, ],
    #             [ 0, -1,  0,   0,  0,   0,    0,    0,   0, Rfe, ],
    #         ]
    #     )
    #     # fmt: on
    #     # delete last row and column if Rfe is None
    #     if Rfe is None:
    #         A = A[:-2, :-2]
    #         b = b[:-2]

    #     # print(b)
    #     # print(A)
    #     X = solve(A.astype(float), b.astype(float))

    return I1, I2, Im, If, Lm, delta_Lm
