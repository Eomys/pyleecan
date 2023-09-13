from numpy import max as np_max, min as np_min, mean as np_mean

from SciDataTool import DataTime, VectorField, DataFreq, Norm_ref

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

    # Store axes dict
    self.axes_dict = axes_dict

    # Get time/frequency axis
    if "freqs" in axes_dict:
        ax1 = axes_dict["freqs"]
        if "freqs_Tem" in axes_dict:
            ax1_Tem = axes_dict["freqs_Tem"]
        else:
            ax1_Tem = None
    else:
        ax1 = axes_dict["time"]
        if "time_Tem" in axes_dict:
            ax1_Tem = axes_dict["time_Tem"]
        else:
            ax1_Tem = None

    # Get angle/wavenumber axis
    if "wavenumber" in axes_dict:
        ax2 = axes_dict["wavenumber"]
    else:
        ax2 = axes_dict["angle"]

    # Store airgap flux as VectorField object
    # Axes for each airgap flux component
    axis_list = [ax1, ax2, axes_dict["z"]]

    # Create VectorField with empty components
    if "B_{rad}" in out_dict or "B_{circ}" in out_dict or "B_{ax}" in out_dict:
        self.B = VectorField(
            name="Air gap flux density",
            symbol="B",
        )

    # Radial flux component
    if "B_{rad}" in out_dict:
        self.B.components["radial"] = DataTime(
            name="Air gap radial flux density",
            unit="T",
            symbol="B_{rad}",
            axes=axis_list,
            values=out_dict.pop("B_{rad}"),
        )
    # Tangential flux component
    if "B_{circ}" in out_dict:
        self.B.components["tangential"] = DataTime(
            name="Air gap circumferential flux density",
            unit="T",
            symbol="B_{circ}",
            axes=axis_list,
            values=out_dict.pop("B_{circ}"),
        )
    # Axial flux component
    if "B_{ax}" in out_dict:
        self.B.components["axial"] = DataTime(
            name="Air gap axial flux density",
            unit="T",
            symbol="B_{ax}",
            axes=axis_list,
            values=out_dict.pop("B_{ax}"),
        )

    # Store electromagnetic torque over time, and global values: average, peak to peak and ripple
    if (
        "Tem" in out_dict
        or (
            self.parent is not None
            and self.parent.simu is not None
            and self.parent.simu.machine is not None
            and self.B is not None
            and "radial" in self.B.components.keys()
            and "tangential" in self.B.components.keys()
        )
        and ax1_Tem is not None
    ):
        if "Tem" in out_dict:
            Tem_slice = out_dict.pop("Tem")
        else:
            Tem_slice = self.comp_torque_MT()

        # Store electromagnetic torque per slice (in Newton)
        self.Tem_slice = DataTime(
            name="Electromagnetic torque (axial density)",
            unit="N",
            symbol="T_{em}",
            axes=[ax1_Tem, axes_dict["z"]],
            values=Tem_slice,
            normalizations={"ref": Norm_ref(ref=self.Tem_norm)},
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

    # Store list of winding flux linkage, stator winding fluxlinkage
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
                axes=[ax1, Phase, axes_dict["z"]],
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
