from numpy import array, zeros, nan
from os.path import join

from ....Functions.Load.import_class import import_class
from ....Classes.VarLoad import VarLoad


def run(self, out):
    """PostProcessing to generate a LUT after the corresponding simulation

    Parameters
    ----------
    self : PostLUT
        A PostLUT object
    out: Output
        Output object coming from LUT calculation workflow

    """

    XOutput = import_class("pyleecan.Classes", "XOutput")
    Output = import_class("pyleecan.Classes", "Output")
    LUTdq = import_class("pyleecan.Classes", "LUTdq")
    LUTslip = import_class("pyleecan.Classes", "LUTslip")

    # Init LUT object
    if out.simu.machine.is_synchronous():
        LUT = LUTdq()
    else:
        LUT = LUTslip()
    LUT._set_None()  # Make sure that everything is set from simu
    LUT.simu = out.simu
    # Store electrical output (if any)
    LUT.elec = out.elec

    # Fill LUT variables
    if LUT.simu.mag is not None:
        # Check that the Simulation is the expected one
        if not isinstance(out, XOutput):
            raise Exception("Need an XOutput to compute LUT")
        elif not isinstance(out.simu.var_simu, VarLoad):
            raise Exception("LUT object can only be computed with VarLoad object")
        # elif not out.simu.var_simu.is_keep_all_output:
        #     raise Exception(
        #         "LUT object can only be computed with is_keep_all_output=True"
        #     )

        stator_label = out.simu.machine.stator.get_label()
        OP_matrix = LUT.get_OP_matrix()
        Nsimu = OP_matrix.shape[0]
        LUT.output_list = [None] * OP_matrix.shape[0]
        if "Phi_{wind}" in out.keys():  # Datakeeper
            for ii in range(Nsimu):
                LUT.output_list[ii] = Output()
                LUT.output_list[ii]._set_None()
                LUT.output_list[ii].mag.Phi_wind = {
                    stator_label: out["Phi_{wind}"].result[ii]
                }
        elif out.output_list is not None:
            for ii in range(Nsimu):
                LUT.output_list[ii] = Output()
                LUT.output_list[ii]._set_None()
                LUT.output_list[ii].mag.Phi_wind = out.output_list[ii].mag.Phi_wind

    # Save/Store LUT object
    if self.is_save_LUT:
        LUT.save(
            save_path=join(out.get_path_result(), "LUT.h5"),
        )
    if self.is_store_LUT:
        self.LUT = LUT
