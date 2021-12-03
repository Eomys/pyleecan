from numpy import max as np_max, min as np_min, mean as np_mean

from SciDataTool import DataTime, VectorField

from ....Functions.labels import STATOR_LAB


def store(self, out_dict, axes_dict):
    """Store the standard outputs of Magnetics that are temporarily in out_dict as arrays into OutMag as Data object

    Parameters
    ----------
    self : OutMag
        the OutMag object to update
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in comp_flux_airgap
    axes_dict: {Data}
        Dict of axes used for magnetic calculation

    """

    # Store axes_dict
    self.axes_dict = axes_dict

    # Get time axis
    Time = axes_dict["time"]

    # Store airgap flux as VectorField object
    # Axes for each airgap flux component
    axis_list = [Time, axes_dict["angle"], axes_dict["z"]]

    # Create VectorField with empty components
    if "Br" in out_dict or "Bt" in out_dict or "Bz" in out_dict:
        self.B = VectorField(
            name="Airgap flux density",
            symbol="B",
        )

    # Radial flux component
    if "Br" in out_dict:
        self.B.components["radial"] = DataTime(
            name="Airgap radial flux density",
            unit="T",
            symbol="B_r",
            axes=axis_list,
            values=out_dict.pop("Br"),
        )
    # Tangential flux component
    if "Bt" in out_dict:
        self.B.components["tangential"] = DataTime(
            name="Airgap circumferential flux density",
            unit="T",
            symbol="B_t",
            axes=axis_list,
            values=out_dict.pop("Bt"),
        )
    # Axial flux component
    if "Bz" in out_dict:
        self.B.components["axial"] = DataTime(
            name="Airgap axial flux density",
            unit="T",
            symbol="B_z",
            axes=axis_list,
            values=out_dict.pop("Bz"),
        )

    # Store electromagnetic torque over time, and global values: average, peak to peak and ripple
    if "Tem" in out_dict:

        # Store electromagnetic torque per slice (in Newton)
        self.Tem_slice = DataTime(
            name="Electromagnetic torque (axial density)",
            unit="N",
            symbol="T_{em}",
            axes=[axes_dict["time_Tem"], axes_dict["z"]],
            values=out_dict.pop("Tem"),
        )

        # Integrate over slice axis to get overall torque (in Newton meter)
        self.Tem = self.Tem_slice.get_data_along("time[smallestperiod]", "z=integrate")
        self.Tem.name = "Electromagnetic torque"

        # Calculate average torque in Nm
        self.Tem_av = np_mean(self.Tem.values)
        # self.Tem_av = float(self.Tem.get_along("time=mean")[self.Tem.symbol])

        # Calculate peak to peak torque in absolute value [N.m]
        self.Tem_rip_pp = abs(np_max(self.Tem.values) - np_min(self.Tem.values))

        # Calculate torque ripple in percentage [%]
        if self.Tem_av != 0:
            self.Tem_rip_norm = self.Tem_rip_pp / self.Tem_av
        else:
            self.Tem_rip_norm = None

    # Store list of winding fluxlinkage, stator winding fluxlinkage
    # and calculate electromotive force
    if "Phi_wind" in out_dict:
        machine = self.parent.simu.machine
        self.Phi_wind_slice = dict()
        self.Phi_wind = dict()
        for key, phi_wind in out_dict["Phi_wind"].items():
            # Store stator winding flux
            lam = machine.get_lam_by_label(key)

            Phase = self.parent.elec.axes_dict["phase_" + key]
            prefix = "Stator" if lam.is_stator else "Rotor"

            # Store winding flux linkage per phase and per slice (in Weber per meter)
            self.Phi_wind_slice[key] = DataTime(
                name=prefix + " Winding Flux (axial density)",
                unit="Wb/m",
                symbol="Phi_{wind}",
                axes=[Time, Phase, axes_dict["z"]],
                values=phi_wind,
            )
            # Integrate over slice axis to get overall winding flux linkage (in Weber)
            self.Phi_wind[key] = self.Phi_wind_slice[key].get_data_along(
                "time[smallestperiod]", "phase", "z=integrate"
            )
            self.Phi_wind[key].name = prefix + " Winding Flux"

        # Particular case: Phi_wind for stator-0 has its own property
        if STATOR_LAB + "-0" in out_dict["Phi_wind"].keys():
            # TODO fix for multi stator/lamination
            self.Phi_wind_stator = self.Phi_wind[STATOR_LAB + "-0"]

        # Electromotive force computation
        # self.comp_emf()

    # Store MeshSolution object
    if "meshsolution" in out_dict:
        self.meshsolution = out_dict.pop("meshsolution")

    if "Rag" in out_dict:
        self.Rag = out_dict.pop("Rag")
