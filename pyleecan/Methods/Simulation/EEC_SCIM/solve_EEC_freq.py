# -*- coding: utf-8 -*-

from ....Functions.Electrical.coordinate_transformation import dq2n
from ....Functions.Winding.gen_phase_list import gen_name

from numpy import array, pi, real, imag, tile
from scipy.linalg import solve
from SciDataTool import Data1D, DataTime


def solve_EEC_freq(self, output):
    """Solves the equivalent electrical circuit for each frequency (not only fundamental)
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
        an EEC_SCIM object, including ELUT
    output : Output
        an Output object
    """
    ELUT = self.ELUT        #Electrical Look Up Table containing Lm(Im)
    k_skin = self.k_skin    #skin effect factor array

    # initial calculation of unsaturated magnetization current
    Lm0 = ELUT.phim[0] 
    EEC.solve_EEC()
    Im0 = EEC.



    Rr_s = Rr / slip if slip != 0 else 1e16  # TODO modify system instead

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

        Ir_norm = array([X[6], X[7]])

        # TODO use logger for output of some quantities

        output.elec.Id_ref = X[2]  # use Id_ref / Iq_ref for now
        output.elec.Iq_ref = X[3]
    else:
        pass
        # TODO

    # Compute stator currents
    output.elec.Is = None
    output.elec.Is = output.elec.get_Is()

    # Compute stator voltage
    output.elec.Us = None
    output.elec.Us = output.elec.get_Us()

    # Compute rotor currents
    time = output.elec.Time.get_values(is_oneperiod=True)
    Nt = time.size
    qsr = output.simu.machine.rotor.winding.qs
    sym = output.simu.machine.comp_periodicity()[0]

    Ir_ = tile(Ir_norm, (Nt, 1)) * norm

    w_slip = ws * slip

    # Get rotation direction
    rot_dir = output.get_rot_dir()

    # compute actual rotor bar currents
    # TODO fix: initial rotor pos. is disregarded for now
    Ir = dq2n(Ir_, w_slip * time, n=qsr // sym, rot_dir=rot_dir, is_n_rms=False)
    Ir = tile(Ir, (1, sym))

    Phase = Data1D(
        name="phase",
        unit="",
        values=gen_name(qsr),
        is_components=True,
    )
    output.elec.Ir = DataTime(
        name="Rotor current",
        unit="A",
        symbol="Ir",
        axes=[Phase, output.elec.Time.copy()],
        values=Ir.T,
    )
