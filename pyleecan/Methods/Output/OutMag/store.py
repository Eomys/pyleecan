from numpy import mean, max as np_max, min as np_min

from SciDataTool import DataTime, VectorField, Data1D

from ....Functions.Winding.gen_phase_list import gen_name
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

    # Get time axis
    Time = axes_dict["Time"]

    # Store airgap flux as VectorField object
    # Axes for each airgap flux component
    axis_list = [Time, axes_dict["Angle"], axes_dict["z"]]
    # Create VectorField with empty components
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
            name="Airgap tangential flux density",
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
            name="Electromagnetic torque per slice",
            unit="N",
            symbol="T_{em}",
            axes=[axes_dict["Time_Tem"], axes_dict["z"]],
            values=out_dict.pop("Tem"),
        )

        # Integrate over slice axis to get overall torque (in Newton meter)
        self.Tem = self.Tem_slice.get_data_along("time[smallestperiod]", "z=integrate")

        # Calculate average torque in Nm
        Tem_values = self.Tem.get_along("time[smallestperiod]")[self.Tem.symbol]
        self.Tem_av = mean(Tem_values)
        self.get_logger().debug("Average Torque: " + str(self.Tem_av) + " N.m")

        # Calculate peak to peak torque in absolute value Nm
        self.Tem_rip_pp = abs(np_max(Tem_values) - np_min(Tem_values))  # [N.m]

        # Calculate torque ripple in percentage
        if self.Tem_av != 0:
            self.Tem_rip_norm = self.Tem_rip_pp / self.Tem_av  # []
        else:
            self.Tem_rip_norm = None

    # Store list of winding fluxlinkage, stator winding fluxlinkage
    # and calculate electromotive force
    if "Phi_wind" in out_dict:
        machine = self.parent.simu.machine
        self.Phi_wind_slice = dict()
        self.Phi_wind = dict()
        for key in out_dict["Phi_wind"].keys():
            # Store stator winding flux
            lam = machine.get_lam_by_label(key)
            qs = lam.winding.qs

            Phase = Data1D(
                name="phase",
                unit="",
                values=gen_name(qs),
                is_components=True,
            )
            prefix = "Stator" if lam.is_stator else "Rotor"

            # Get flux linkae values from output dict
            phi_wind_val = out_dict.pop("Phi_wind")

            # Store winding flux linkage per phase and per slice (in Weber per meter)
            self.Phi_wind_slice[key] = DataTime(
                name=prefix + " Winding Flux",
                unit="Wb",
                symbol="Phi_{wind}",
                axes=[Time, Phase, axes_dict["z"]],
                values=phi_wind_val[key],
            )
            # Integrate over slice axis to get overall winding flux linkage (in Weber)
            self.Phi_wind[key] = self.Phi_wind_slice[key].get_data_along(
                "time[smallestperiod]", "phase", "z=integrate"
            )

        if (
            STATOR_LAB + "-0" in out_dict["Phi_wind"].keys()
        ):  # TODO fix for multi stator
            self.Phi_wind_stator = self.Phi_wind[STATOR_LAB + "-0"]

        # Electromotive force computation
        self.comp_emf()

    # Store MeshSolution object
    if "meshsolution" in out_dict:
        self.meshsolution = out_dict.pop("meshsolution")

    if "Rag" in out_dict:
        self.Rag = out_dict.pop("Rag")
