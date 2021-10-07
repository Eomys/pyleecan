from numpy import array, zeros, nan
from os.path import join

from ....Classes.ELUT_PMSM import ELUT_PMSM
from ....Functions.Load.import_class import import_class


def run(self, out):
    """PostProcessing to generate an ELUT after the corresponding simulation

    Parameters
    ----------
    self : PostELUT
        A PostELUT object
    out: Output
        Output object coming from ELUT calculation workflow

    """

    if out.simu.machine.is_synchronous():
        # Init ELUT object
        ELUT = ELUT_PMSM()

        XOutput = import_class("pyleecan.Classes", "XOutput")

        if not isinstance(out, XOutput):
            raise Exception("Need an XOutput to compute ELUT")
        else:
            # Store data for each OP
            # Number of columns in OP_matrix
            ndim = out.simu.var_simu.OP_matrix.shape[1]

            # Store operating point matrix in VarLoadCurrent object
            ELUT.OP_matrix = nan * zeros((out.nb_simu, 5))
            ELUT.OP_matrix[:, 0] = array(out["N0"].result)
            ELUT.OP_matrix[:, 1] = array(out["Id"].result)
            ELUT.OP_matrix[:, 2] = array(out["Iq"].result)
            if ndim > 3:
                for ii in range(3, ndim):
                    ELUT.OP_matrix[:, ii] = array(out.simu.var_simu.OP_matrix[:, ii])

            # Fill ELUT variables
            dk_list = list(out.keys())
            if "Phi_{dq}" in dk_list:
                ELUT.Phi_dqh = out["Phi_{dq}"].result

            # Find Id=Iq=0
            OP_list = ELUT.OP_matrix[:, 1:3].tolist()
            if [0, 0] in OP_list:
                ii = OP_list.index([0, 0])
            else:
                raise Exception("Operating Point Id=Iq=0 is required to compute ELUT")
            # Compute back electromotive force
            out.output_list[ii].mag.comp_emf()
            BEMF = out.output_list[ii].mag.emf
            BEMF.name = "Stator Winding Back Electromotive Force"
            BEMF.symbol = "BEMF"
            ELUT.bemf = BEMF

            # # Set if the interpolation must be made along a curve
            # ELUT.set_is_interp_along_curve()

            if self.is_save_ELUT:
                # Save ELUT object
                ELUT.save(
                    save_path=join(out.get_path_result(), "ELUT.h5"),
                )

            if self.is_store_ELUT:
                # Store ELUT in PostELUT object
                self.ELUT = ELUT

    else:
        raise Exception("PostELUT for asynchronous machines not developed yet")
