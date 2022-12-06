from scipy.io import savemat


def export_to_mat(self, file_path):
    """Export the main outputs to a .mat file


    Parameters
    ----------
    self : Output
        An Output object
    file_path : str
        Path to save the generated mat file
    """

    # Dict to save
    data_dict = dict()

    # Data size
    data_dict["Na_tot"] = self.simu.input.Na_tot
    data_dict["Nt_tot"] = self.simu.input.Nt_tot

    # Electrical data
    if self.elec is not None:
        if self.elec.OP is not None:
            data_dict["N0"] = self.elec.OP.N0
            I_dict = self.elec.OP.get_Id_Iq()
            data_dict["Id"] = I_dict["Id"]
            data_dict["Iq"] = I_dict["Iq"]
            if hasattr(self.elec.OP, "If_ref"):
                data_dict["If"] = self.elec.OP.If_ref
            Is = self.elec.get_Is()
            if Is is not None:
                data_dict["Is"] = Is.get_along("phase", "time")["I_s"]
    # Magnetic data
    if self.mag is not None:
        data_dict["time"] = self.mag.axes_dict["time"].get_values()
        data_dict["angle"] = self.mag.axes_dict["angle"].get_values()
        if self.mag.B is not None:
            data_dict["B_rad"] = self.mag.B.components["radial"].get_along(
                "time", "angle"
            )["B_{rad}"]
            data_dict["B_tan"] = self.mag.B.components["tangential"].get_along(
                "time", "angle"
            )["B_{circ}"]
        if self.mag.Tem is not None:
            data_dict["Tem"] = self.mag.Tem.get_along("time")["T_{em}"]
        if self.mag.Tem_av is not None:
            data_dict["Tem_av"] = self.mag.Tem_av
        if self.mag.Tem_rip_norm is not None:
            data_dict["Tem_rip_norm"] = self.mag.Tem_rip_norm
        if self.mag.Tem_rip_pp is not None:
            data_dict["Tem_rip_pp"] = self.mag.Tem_rip_pp
        if self.mag.Phi_wind_stator is not None:
            data_dict["Phi_wind_stator"] = self.mag.Phi_wind_stator.get_along(
                "time", "phase"
            )["Phi_{wind}"]
        # if self.mag.emf is not None:
        #     data_dict["emf"] = self.mag.emf.get_along("time")
    # Save result
    savemat(file_path, data_dict)
