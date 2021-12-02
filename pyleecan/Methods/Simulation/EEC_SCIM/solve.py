from numpy import sqrt


def solve(self):
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

    Phi_m = self.parameters["Phi_m"]
    I_m = self.parameters["I_m"]

    # solving elementary system, initial start with unsaturated inductance
    Lm = Phi_m[0] / I_m[0]
    I1, I2, Im, If, Lm, delta_Lm = self.solve_elementary(Lm)
    if Phi_m.size > 1:
        # iteration until convergence is reached, and max number of iterations on EEC
        delta_Lm_max = 1e-6
        Nmax = 20
        niter_Lm = 1
        while abs(delta_Lm) > delta_Lm_max and niter_Lm < Nmax:
            I1, I2, Im, If, Lm, delta_Lm = self.solve_elementary(Lm)

            niter_Lm = niter_Lm + 1

    out_dict = dict()

    out_dict["Ud"] = self.parameters["U0_ref"]
    out_dict["Uq"] = 0
    out_dict["Id"] = I1.real
    out_dict["Iq"] = I1.imag
    out_dict["I1"] = I1
    out_dict["I2"] = I2
    out_dict["Ir"] = I2 * self.parameters["K21I"] * sqrt(2)
    out_dict["Im"] = Im
    out_dict["If"] = If

    return out_dict

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
    # Ir = dqh2n(Ir_, w_slip * time, n=qsr // sym, rot_dir=rot_dir, is_n_rms=False)
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
