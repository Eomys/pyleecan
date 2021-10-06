# -*- coding: utf-8 -*-
from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the Magnetics module"""
    if self.parent is None:
        raise InputError(
            "ERROR: The Magnetic object must be in a Simulation object to run"
        )
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    self.get_logger().info("Starting Magnetic module")
    output = self.parent.parent

    # Compute and store time and angle axes from elec output
    # and returns additional axes in axes_dict
    axes_dict = self.comp_axes(output)

    if self.is_mmfs:
        Is = output.elec.get_Is(Time=axes_dict["time"], is_current_harm=self.is_current_harm)
        Is_val = output.elec.comp_I_mag(Time=axes_dict["time"], is_stator=True, I_data=Is, is_periodicity_t=self.is_periodicity_t)
    else:
        Is_val = None
    # Get rotor current from elec out
    if self.is_mmfr:
        # Ir = output.elec.get_Ir(Time=axes_dict["time"]) TODO
        Ir_val =  output.elec.comp_I_mag(Time=axes_dict["time"], is_stator=False, is_periodicity_t=self.is_periodicity_t)
    else:
        Ir_val = None

    # Calculate airgap flux
    out_dict = self.comp_flux_airgap(output, axes_dict, Is=Is_val, Ir=Ir_val)

    # Store magnetic quantities contained in out_dict in OutMag, as Data object if necessary
    output.mag.store(out_dict, axes_dict)
    output.mag.comp_power()
