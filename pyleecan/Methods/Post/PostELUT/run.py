from numpy import array, zeros, nan

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

        # Store data for each OP
        if isinstance(out, XOutput):

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
            if "T_{em}" in dk_list and None not in out["T_{em}"].result:
                ELUT.Tem = out["T_{em}"].result
            if "Phi_{wind}" in dk_list and None not in out["Phi_{wind}"].result:
                ELUT.Phi_wind_stator = out["Phi_{wind}"].result
                ELUT.Phi_dqh = out["Phi_{dq}"].result
            if "EMF" in dk_list and None not in out["EMF"].result:
                ELUT.bemf = out["EMF"].result
        else:
            # Store operating point matrix in OutElec
            ELUT.OP_matrix = nan * zeros((1, 5))
            ELUT.OP_matrix[:, 0] = out.elec.N0
            ELUT.OP_matrix[:, 1] = out.elec.Id_ref
            ELUT.OP_matrix[:, 2] = out.elec.Iq_ref
            if out.elec.Tem_av_ref is not None:
                ELUT.OP_matrix[:, 3] = out.elec.Tem_av_ref

            # Fill ELUT variables
            if out.mag.Tem is not None:
                ELUT.Tem = [out.mag.Tem]
            if out.mag.Phi_wind_stator is not None:
                ELUT.Phi_wind_stator = [out.mag.Phi_wind_stator]
                ELUT.Phi_dqh = [out.mag.comp_Phi_dq()]
            if out.mag.emf is not None:
                ELUT.bemf = [out.mag.emf]

        # # Set if the interpolation must be made along a curve
        # ELUT.set_is_interp_along_curve()

        # Store axes_dict
        if ELUT.Tem is not None:
            axes_dict = dict()
            axes_list = ELUT.Tem[0].get_axes()
            # if MLUT.AGSF is not None and self.is_fft_AGSF:
            #     axes_list.extend(MLUT.AGSF[0].get_axes())
            for axis in axes_list:
                axes_dict[axis.name] = axis
            ELUT.axes_dict = axes_dict

        # if self.is_save_ELUT:

        #     # Save ELUT object
        #     ELUT.save_partial(
        #         folder_path=out.simu.get_machine_data_path(
        #             data_name="ELUT", is_create_folder=True
        #         ),
        #         file_name="ELUT",
        #         is_Tem=ELUT.Tem is not None,
        #         is_Phi_wind_stator=ELUT.Phi_wind_stator is not None,
        #         is_Phi_dq=ELUT.Phi_dq is not None,
        #         is_EMF=ELUT.bemf is not None,
        #     )

        if self.is_store_ELUT:
            # Store ELUT in PostELUT object
            self.ELUT = ELUT

    else:
        raise Exception("PostELUT for asynchronous machines not developed yet")
