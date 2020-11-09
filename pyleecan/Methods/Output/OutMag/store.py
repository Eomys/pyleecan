# -*- coding: utf-8 -*-
from numpy import mean, max as np_max, min as np_min

from SciDataTool import DataTime, VectorField, Data1D

from ....Functions.Winding.gen_phase_list import gen_name


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
    axis_list = [Time, axes_dict["Angle"]]
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

        Tem = out_dict.pop("Tem")

        self.Tem = DataTime(
            name="Electromagnetic torque",
            unit="Nm",
            symbol="T_{em}",
            axes=[axes_dict["Time_Tem"]],
            values=Tem,
        )

        # Calculate average torque in Nm
        self.Tem_av = mean(Tem)
        self.get_logger().debug("Average Torque: " + str(self.Tem_av) + " N.m")

        # Calculate peak to peak torque in absolute value Nm
        self.Tem_rip_pp = abs(np_max(Tem) - np_min(Tem))  # [N.m]

        # Calculate torque ripple in percentage
        if self.Tem_av != 0:
           self.Tem_rip_norm = self.Tem_rip_pp / self.Tem_av  # []
        else:
            self.Tem_rip_norm = None

    # Store stator winding flux and calculate electromotive force
    if "Phi_wind_stator" in out_dict:

        # Store stator winding flux
        qs = self.parent.simu.machine.stator.winding.qs

        Phase = Data1D(
            name="phase",
            unit="",
            values=gen_name(qs),
            is_components=True,
        )

        self.Phi_wind_stator = DataTime(
            name="Stator Winding Flux",
            unit="Wb",
            symbol="Phi_{wind}",
            axes=[Time, Phase],
            values=out_dict.pop("Phi_wind_stator"),
        )

        # Electromotive force computation
        self.comp_emf()
        
    # Store MeshSolution object and save it as .h5 file if requested
    if "meshsolution" in out_dict:

        # Store meshsolution in OutMag
        self.meshsolution = out_dict.pop("meshsolution")

        # Save meshsolution as .h5 on disk if requested
        if self.is_save_FEA:
            save_path = self.get_path_save(output)
            save_path_fea = join(save_path, "MeshSolutionFEMM.h5")
            self.meshsolution.save(save_path_fea)
