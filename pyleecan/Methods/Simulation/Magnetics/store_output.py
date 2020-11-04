# -*- coding: utf-8 -*-
from numpy import mean, max as np_max, min as np_min

from SciDataTool import DataTime, VectorField, Data1D

from ....Functions.Winding.gen_phase_list import gen_name


def store_output(self, output, out_dict, axes_dict):
    """Store the standard outputs of Magnetics that are temporarily in out_dict as arrays into OutMag as Data object

    Parameters
    ----------
    self : Magnetic
        a Magnetic object
    output : Output
        an Output object (to update)
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
    output.mag.B = VectorField(
        name="Airgap flux density",
        symbol="B",
    )
    # Radial flux component
    if "Br" in out_dict:
        output.mag.B.components["radial"] = DataTime(
            name="Airgap radial flux density",
            unit="T",
            symbol="B_r",
            axes=axis_list,
            values=out_dict.pop("Br"),
        )
    # Tangential flux component
    if "Bt" in out_dict:
        output.mag.B.components["tangential"] = DataTime(
            name="Airgap tangential flux density",
            unit="T",
            symbol="B_t",
            axes=axis_list,
            values=out_dict.pop("Bt"),
        )
    # Axial flux component
    if "Bz" in out_dict:
        output.mag.B.components["axial"] = DataTime(
            name="Airgap axial flux density",
            unit="T",
            symbol="B_z",
            axes=axis_list,
            values=out_dict.pop("Bz"),
        )

    # Store electromagnetic torque over time, and global values: average, peak to peak and ripple
    if "Tem" in out_dict:

        Tem = out_dict.pop("Tem")

        output.mag.Tem = DataTime(
            name="Electromagnetic torque",
            unit="Nm",
            symbol="T_{em}",
            axes=[axes_dict["Time_Tem"]],
            values=Tem,
        )

        # Calculate average torque in Nm
        output.mag.Tem_av = mean(Tem)
        self.get_logger().debug("Average Torque: " + str(output.mag.Tem_av) + " N.m")

        # Calculate peak to peak torque in absolute value Nm
        output.mag.Tem_rip_pp = abs(np_max(Tem) - np_min(Tem))  # [N.m]

        # Calculate torque ripple in percentage
        if output.mag.Tem_av != 0:
            output.mag.Tem_rip_norm = output.mag.Tem_rip_pp / output.mag.Tem_av  # []
        else:
            output.mag.Tem_rip_norm = None

    # Store stator winding flux and calculate electromotive force
    if "Phi_wind_stator" in out_dict:

        # Store stator winding flux
        qs = self.parent.machine.stator.winding.qs

        Phase = Data1D(
            name="phase",
            unit="",
            values=gen_name(qs),
            is_components=True,
        )

        output.mag.Phi_wind_stator = DataTime(
            name="Stator Winding Flux",
            unit="Wb",
            symbol="Phi_{wind}",
            axes=[Time, Phase],
            values=out_dict.pop("Phi_wind_stator"),
        )

        # Electromotive force computation
        output.mag.comp_emf()
