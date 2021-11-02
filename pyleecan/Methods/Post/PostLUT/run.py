from numpy import array, zeros, nan
from os.path import join

from ....Classes.LUTdq import LUTdq
from ....Functions.Load.import_class import import_class


def run(self, out):
    """PostProcessing to generate a LUT after the corresponding simulation

    Parameters
    ----------
    self : PostLUT
        A PostLUT object
    out: Output
        Output object coming from LUT calculation workflow

    """

    if out.simu.machine.is_synchronous():
        # Init LUT object
        LUT = LUTdq(phase_dir=out.elec.phase_dir)

        XOutput = import_class("pyleecan.Classes", "XOutput")

        if not isinstance(out, XOutput):
            raise Exception("Need an XOutput to compute LUT")
        else:
            # Store data for each OP
            # Number of columns in OP_matrix
            ndim = out.simu.var_simu.OP_matrix.shape[1]

            # Store operating point matrix in VarLoadCurrent object
            LUT.OP_matrix = nan * zeros((out.nb_simu, 5))
            LUT.OP_matrix[:, 0] = array(out["N0"].result)
            LUT.OP_matrix[:, 1] = array(out["Id"].result)
            LUT.OP_matrix[:, 2] = array(out["Iq"].result)
            if ndim > 3:
                for ii in range(3, ndim):
                    LUT.OP_matrix[:, ii] = array(out.simu.var_simu.OP_matrix[:, ii])

            # Fill LUT variables
            if "Phi_{wind}" in out.keys():
                LUT.Phi_wind = out["Phi_{wind}"].result
            elif out.output_list is not None:
                stator_label = out.simu.machine.stator.get_label()
                LUT.Phi_wind = [o.mag.Phi_wind[stator_label] for o in out.output_list]

            if self.is_save_LUT:
                # Save LUT object
                LUT.save(
                    save_path=join(out.get_path_result(), "LUT.h5"),
                )

            if self.is_store_LUT:
                # Store LUT in PostLUT object
                self.LUT = LUT

    else:
        raise Exception("PostLUT for asynchronous machines not developed yet")
