# -*- coding: utf-8 -*-

from numpy import array, pi, real, imag
from scipy.linalg import solve


def solve_EEC(self, output):
    """Compute the parameters dict for the equivalent electrical circuit
    TODO find ref. to cite, maybe wikipedia?
    cf "Advanced Electrical Drives, analysis, modeling, control"
    Rik de doncker, Duco W.J. Pulle, Andre Veltman, Springer edition

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

    felec = output.elec.felec
    ws = 2 * pi * felec

    # Prepare linear system

    # Solve system
    if "Us" in self.parameters:
        Us = self.parameters["Us"]
        # input vector
        b = array([
            real(Us), imag(Us),  0, 0, 0, 0, 0, 0, 0, 0
        ])
        # system matrix (unknowns order: Um, Is, Im, Ir', Ife each real and imagine parts)
        # TODO simplify system for less unknows (only calculate them afterwards, e.g. Um, Im, Ife)
        A = array([
            # sum of (real and imagine) voltages equals the input voltage Us
            [1, 0, Rs, -Xs, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 1, Xs, +Rs, 0, 0, 0, 0, 0, 0, 0, 0], 
            # sum of (real and imagine) currents are zeros
            [0, 0, -1, 0, 1, 0, 1, 0, 1, 0 ], 
            [0, 0, 0, -1, 0, 1, 0, 1, 0, 1 ], 
            # j*Xm*Im = Um
            [-1, 0, 0, 0, 0, -Xm, 0, 0, 0, 0,], 
            [0, -1, 0, 0, +Xm, 0, 0, 0, 0, 0],
            # (Rr'/s + j*Xr')*Ir' = Um
            [-1, 0, 0, 0, 0, 0, Rr_, -Xr_, 0, 0], 
            [0, -1, 0, 0, 0, 0, +Xm, +Rr_, 0, 0],
            # Rfe*Ife = Um
            [-1, 0, 0, 0, 0, 0, 0, 0, Rfe, 0], 
            [0, +1, 0, 0, 0, 0, 0, 0, 0, Ref],
        ])
        # TODO delete last row and column if Rfe is None

        X = solve(A, b)
        
        Um = X[0] + j*X[1]
        Is = X[2] + j*X[3]
        Ir_ = X[6] + j*X[7]
        Ife = X[8] + j*x[9]

        #output.elec.Id_ref = XI[0]
        #output.elec.Iq_ref = XI[1]
    else:
        pass
        # TODO

    # Compute currents
    # output.elec.Is = None
    # output.elec.Is = output.elec.get_Is()

    # Compute voltage
    # output.elec.Us = None
    # output.elec.Us = output.elec.get_Us()
