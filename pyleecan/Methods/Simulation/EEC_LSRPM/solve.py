# -*- coding: utf-8 -*-

from numpy import array, pi
from scipy.linalg import solve


def solve_EEC(self, output):
    """Compute the parameters dict for the equivalent electrical circuit
      cf PhD thesis of SIJIE NI
      "Damper winding for noise and vibration reductionof Permanent Magnet Synchronous Machine"


       -----R_s--L_dss--------------------------------            -----R_s-----L_qss----------------------------------------------------
      |                                   |           |         |                                                            |         |
    ^ |                                  L_dmu      L_daa     ^ |                                                            |        Lr_qaa
    | |                                   |           |       | |                                                            |         |
    | Uds                                L_dsa      R_a       | Uqs                                                        L_qmu      Rr_a
    | |                                   |           |       | |                                                            |         |
      |                                   |         C_a         |                                                            |         C_a
      |                                   |           |         |                                                            |         |
       --wsL_qssI_qs---wsL_qmu(I_qs-Ir_qa)------------            ---wsPhi_m---wsL_dssI_ds---ws(L_dss+L_dmu)(I_ds-Ir_da)----------------
          <--------   <----------------                              <------   <----------   <-------------------------
          <----------------------------                              <-------------------------------------------------
                  wsPhi_qs                                                wsPhi_ds

      Parameters
      ----------
      self : EEC_LSRPM
          an EEC_LSRPM object
      output : Output
          an Output object
    """

    felec = output.elec.felec
    ws = 2 * pi * felec

    R_s = self.parameters["R_s"]
    Rr_a = self.parameters["Rr_a"]
    C_a = self.parameters["C_a"]
    norm = self.parameters["norm"]
    Phi_m = self.parametrs["Phi_m"]

    # d-axis
    L_dss = self.parameters["L_dss"]
    L_dmu = self.parameters["L_dmu"]
    L_dsa = self.parameters["L_dsa"]
    L_daa = self.parameters["L_daa"]
    U_ds = self.parameters["U_ds"]
    I_ds = self.parameters["I_ds"]
    I_da = self.parameters["I_da"]

    # q-axis
    L_qss = self.parameters["L_qss"]
    L_qmu = self.parameters["L_qmu"]
    Lr_qaa = self.parameters["Lr_qaa"]
    U_qs = self.parameters["U_qs"]
    I_qs = self.parameters["I_qs"]
    I_qa = self.parameters["I_qa"]

    # Prepare linear system

    # Solve system
    if "U_ds" in self.parameters:
        XR = array(
            [
                [R_s, -ws * (L_qss + L_qmu), 0, -ws * L_qmu],
                [ws * (L_dss + L_dmu + L_dsa), R_s, -ws * (L_dmu + L_dsa), 0],
                [0, -ws * L_qmu, Rr_a + 1 / (ws * C_a), ws * (Lr_qaa + L_qmu)],
                [
                    ws * (L_dmu + L_dsa),
                    0,
                    -ws * (L_daa + L_dmu + L_dsa),
                    Rr_a + 1 / (ws * C_a),
                ],
            ]
        )
        XE = array([0, ws * Phi_m, 0, ws * Phi_m])
        XU = array([U_ds, U_qs, 0, 0])
        XI = solve(XR, XU - XE)

        output.elec.Ids_ref = XI[0]
        output.elec.Iqs_ref = XI[1]
        output.elec.Ida_ref = XI[2]
        output.elec.Iqa_ref = XI[3]
    else:
        output.elec.Uds_ref = (
            I_ds * (R_s + ws * L_dss)
            + (I_ds - I_da) * ws * (L_dmu + L_dsa)
            - ws * L_qmu * (I_qs - I_qa)
            - ws * L_qss * I_qs
        )
        output.elec.Uqs_ref = (
            I_qs * (R_s + ws * L_qss)
            + (I_qs - I_qa) * ws * L_qmu
            + ws * Phi_m
            + ws * L_dss * I_ds
            + ws * (L_dss + L_dmu) * (I_ds - I_da)
        )

    # Compute currents
    output.elec.Is = None
    output.elec.Is = output.elec.get_Is()

    # Compute voltage
    output.elec.Us = None
    output.elec.Us = output.elec.get_Us()
