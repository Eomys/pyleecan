# -*- coding: utf-8 -*-

from numpy import array, pi, real, imag
from scipy.linalg import solve


def solve_EEC(self, output):
    """Compute the parameters dict for the equivalent electrical circuit
    TODO find ref. to cite
    cf "Title"
    Autor, Publisher

                  --->                     ---->
     -----Rs------XsIs---- --- -----Rr'----Xr'Ir'----
    |                     |   |                       |
    |                     Rfe Xm                      Rr'*(s-1)/s
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
    Rs = self.parameters["Rs"]
    Rr = self.parameters["Rr"]
    Rfe = self.parameters["Rfe"]
    Ls = self.parameters["Ls"]
    Lr = self.parameters["Lr"]
    Lm = self.parameters["Lm"]

    s = self.parameters["s"]

    felec = output.elec.felec
    ws = 2 * pi * felec

    Xs = ws * Ls
    Xm = ws * Lm
    Xr = ws * Lr

    Rr_s = Rr / s if s != 0 else 1e16  # TODO modify system instead

    # Prepare linear system

    # Solve system
    if "Ud" in self.parameters:
        Us = self.parameters["Ud"] + 1j * self.parameters["Uq"]
        # input vector
        b = array([real(Us), imag(Us), 0, 0, 0, 0, 0, 0, 0, 0])
        # system matrix (unknowns order: Um, Is, Im, Ir', Ife each real and imagine parts)
        # TODO simplify system for less unknows (only calculate them afterwards, e.g. Um, Im, Ife)
        # fmt: off
        A = array(
            [ 
                # sum of (real and imagine) voltages equals the input voltage Us
                [ 1,  0, Rs, -Xs,  0,   0,    0,    0,   0,   0, ], 
                [ 0,  1, Xs,  Rs,  0,   0,    0,    0,   0,   0, ], 
                # sum of (real and imagine) currents are zeros
                [ 0,  0, -1,   0,  1,   0,    1,    0,   1,   0, ], 
                [ 0,  0,  0,  -1,  0,   1,    0,    1,   0,   1, ], 
                # j*Xm*Im = Um
                [-1,  0,  0,   0,  0, -Xm,    0,    0,   0,   0, ], 
                [ 0, -1,  0,   0, Xm,   0,    0,    0,   0,   0, ],
                # (Rr'/s + j*Xr')*Ir' = Um
                [-1,  0,  0,   0,  0,   0, Rr_s,  -Xr,   0,   0, ], 
                [ 0, -1,  0,   0,  0,   0,   Xr, Rr_s,   0,   0, ],
                # Rfe*Ife = Um
                [-1,  0,  0,   0,  0,   0,    0,    0, Rfe,   0, ], 
                [ 0, -1,  0,   0,  0,   0,    0,    0,   0, Rfe, ],
            ]
        ) 
        # fmt: on
        # delete last row and column if Rfe is None
        if Rfe is None:
            A = A[:-2, :-2]
            b = b[:-2]

        # print(b)
        # print(A)
        X = solve(A.astype(float), b.astype(float))

        Is = X[2] + 1j * X[3]

        """
        Um = X[0] + 1j * X[1]
        Ir_ = X[6] + 1j * X[7]
        print(Um)
        print(Is)
        print(Ir_)
        if Rfe is not None:
            Ife = X[8] + 1j * X[9]
            print(Ife)
        """
        # TODO use logger for output of some quantities

        output.elec.Id_ref = real(Is)  # use Id_ref / Iq_ref for now
        output.elec.Iq_ref = imag(Is)
    else:
        pass
        # TODO

    # Compute currents
    output.elec.Is = None
    output.elec.Is = output.elec.get_Is()

    # Compute voltage
    output.elec.Us = None
    output.elec.Us = output.elec.get_Us()
