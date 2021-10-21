from numpy.lib.shape_base import expand_dims
from numpy import zeros, array
from ....Methods.Simulation.Input import InputError
from ....Classes.EEC_SCIM import EEC_SCIM
from ....Classes.EEC_PMSM import EEC_PMSM
from ....Classes.EEC_ANL import EEC_ANL
from ....Classes.MachineSCIM import MachineSCIM
from ....Classes.MachineSIPMSM import MachineSIPMSM
from ....Classes.MachineIPMSM import MachineIPMSM


def run(self):
    """Run the Electrical module"""
    if self.parent is None:
        raise InputError("The Electrical object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("The Simulation object must be in an Output object to run")

    self.get_logger().info("Starting Electric module")

    output = self.parent.parent

    machine = output.simu.machine

    if self.eec is None:
        # Init EEC depending on machine type
        if isinstance(machine, MachineSCIM):
            self.eec = EEC_SCIM()
        elif isinstance(machine, (MachineSIPMSM, MachineIPMSM)):
            self.eec = EEC_PMSM()
    else:
        # Check that EEC is consistent with machine type
        if isinstance(machine, MachineSCIM) and (
            not isinstance(self.eec, EEC_SCIM) and not isinstance(self.eec, EEC_ANL)
        ):
            raise Exception(
                "Cannot run Electrical model if machine is SCIM and eec is not EEC_SCIM or EEC_ANL"
            )
        elif isinstance(machine, (MachineSIPMSM, MachineIPMSM)) and (
            not isinstance(self.eec, EEC_PMSM) and not isinstance(self.eec, EEC_ANL)
        ):
            raise Exception(
                "Cannot run Electrical model if machine is PMSM and eec is not EEC_PMSM or EEC_ANL"
            )

    if self.ELUT_enforced is not None:
        # enforce parameters of EEC coming from enforced ELUT at right temperatures
        if self.eec.parameters is None:
            self.eec.parameters = dict()
        self.eec.parameters.update(self.ELUT_enforced.get_param_dict(OP=output.elec.OP))

    # Generate drive
    # self.eec.gen_drive(output)
    # self.eec.parameters["U0_ref"] = output.elec.U0_ref
    # self.eec.parameters["Ud_ref"] = output.elec.OP.get_Ud_Uq()["Ud"]
    # self.eec.parameters["Uq_ref"] = output.elec.OP.get_Ud_Uq()["Uq"]

    # Compute parameters of the electrical equivalent circuit if some parameters are missing in ELUT
    self.eec.comp_parameters(
        machine,
        OP=output.elec.OP,
        Tsta=self.Tsta,
        Trot=self.Trot,
    )

    # Solve the electrical equivalent circuit
    out_dict = self.eec.solve_EEC()

    # Solve for each harmonic in case of Us_PWM
    out_dict_harm = dict()
    if output.elec.Us_PWM is not None:
        Us_harm = output.elec.get_Us_harm()
        result = Us_harm.get_along("freqs", "phase")
        Udqh = result[Us_harm.symbol]
        freqs = result["freqs"].tolist()
        Is_harm = zeros((len(freqs), machine.stator.winding.qs), dtype=complex)
        # Remove Id/Iq from eec parameters
        del self.eec.parameters["Id"]
        del self.eec.parameters["Iq"]
        for i, f in enumerate(freqs):
            # Update eec paremeters
            self.eec.freq0 = f
            self.eec.parameters["Ud"] = Udqh[i, 0]
            self.eec.parameters["Uq"] = Udqh[i, 1]
            # Solve eec
            out_dict_i = self.eec.solve_EEC()
            Is_harm[i, :] = array([out_dict_i["Id"], out_dict_i["Iq"], 0])
        out_dict_harm["Is_harm"] = Is_harm
        out_dict_harm["axes_list"] = Us_harm.get_axes()

    # Compute losses due to Joule effects
    out_dict = self.eec.comp_joule_losses(out_dict, machine)

    # Compute electromagnetic power
    out_dict = self.comp_power(out_dict, machine)

    # Compute torque
    self.comp_torque(out_dict, output.elec.OP.get_N0())

    # Store electrical quantities contained in out_dict in OutElec, as Data object if necessary
    output.elec.store(out_dict, out_dict_harm)
