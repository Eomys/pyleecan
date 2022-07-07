import numpy as np

from ....Classes.EEC_PMSM import EEC_PMSM
from ....Classes.OutLoss import OutLoss

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the ElecLUTdq module"""
    if self.parent is None:
        raise InputError("The Electrical object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("The Simulation object must be in an Output object to run")

    self.get_logger().info("Starting Electrical module")

    # Get output, machine and OP
    output = self.parent.parent

    machine = output.simu.machine
    OP = output.elec.OP

    # Get winding resistance
    Rs = machine.stator.comp_resistance_wind(T=self.Tsta)

    # Account for skin effect
    if self.type_skin_effect > 0:
        # Calculate skin effect coefficient
        kr_skin = machine.stator.winding.conductor.comp_skin_effect_resistance(
            T_op=self.Tsta, freq=OP.get_felec()
        )
        Rs *= kr_skin
    else:
        kr_skin = 1

    # Maximum phase current
    if self.Irms_max is None:
        if self.Jrms_max is None:
            raise Exception("Irms_max and Jrms_max cannot be both None")
        # Calculate maximum current function of current density
        Swire = machine.stator.winding.conductor.comp_surface_active()
        Npcp = machine.stator.winding.Npcp
        self.Irms_max = self.Jrms_max * Swire * Npcp
    else:
        self.Irms_max = output.simu.input.Irms_max

    if self.LUT_enforced is not None:
        # Take enforced LUT
        LUT = self.LUT_enforced

        # Get Id_min, Id_max, Iq_min, Iq_max from OP_matrix
        OP_matrix = LUT.get_OP_array("N0", "Id", "Iq")
        self.Id_min = OP_matrix[:, 1].min()
        self.Id_max = OP_matrix[:, 1].max()
        self.Iq_min = OP_matrix[:, 2].min()
        self.Iq_max = OP_matrix[:, 2].max()

    else:
        # Run look up table calculation
        # Check dq current boundaries
        if self.Id_min is None:
            if self.n_Id == 1 and self.Id_max is not None:
                self.Id_min = self.Id_max
            else:
                self.Id_min = -self.Irms_max
        if self.Id_max is None:
            if self.n_Id == 1 and self.Id_min is not None:
                self.Id_max = self.Id_min
            else:
                self.Id_max = self.Irms_max
        if self.Iq_min is None:
            if self.n_Iq == 1 and self.Iq_max is not None:
                self.Iq_min = self.Iq_max
            else:
                self.Iq_min = -self.Irms_max
        if self.Iq_max is None:
            if self.n_Iq == 1 and self.Iq_min is not None:
                self.Iq_max = self.Iq_min
            else:
                self.Iq_max = self.Irms_max

        # Run method to calculate LUT
        LUT = self.comp_LUTdq()

        # Store LUT
        output.simu.elec.LUT_enforced = LUT

    if OP.Pem_av_ref is not None or OP.Pem_av_in is not None:
        out_dict = self.solve_power(LUT, Rs)
    else:
        out_dict = self.solve_MTPA(LUT, Rs)

    # Store electrical quantities
    if "P_out" in out_dict:
        output.elec.P_out = out_dict["P_out"]
    if "P_in" in out_dict:
        output.elec.P_in = out_dict["P_in"]
    if "efficiency" in out_dict:
        output.elec.OP.efficiency = out_dict["efficiency"]
    if "Tem_av" in out_dict:
        output.elec.Tem_av = out_dict["Tem_av"]

    # Store voltage and currents
    output.elec.OP.Id_ref = out_dict["Id"]
    output.elec.OP.Iq_ref = out_dict["Iq"]
    output.elec.OP.Ud_ref = out_dict["Ud"]
    output.elec.OP.Uq_ref = out_dict["Uq"]

    # Store EEC parameters
    output.elec.eec = EEC_PMSM(
        Phid=out_dict["Phid"],
        Phiq=out_dict["Phiq"],
        Phid_mag=out_dict["Phid_mag"],
        Phiq_mag=out_dict["Phiq_mag"],
        R1=Rs,
        Tsta=self.Tsta,
        Trot=self.Trot,
        type_skin_effect=self.type_skin_effect,
        Xkr_skinS=kr_skin,
    )
    if "Ld" in out_dict:
        output.elec.eec.Ld = out_dict["Ld"]
    if "Lq" in out_dict:
        output.elec.eec.Lq = out_dict["Lq"]

    if "Pjoule" in out_dict:
        output.elec.Pj_losses = out_dict["Pjoule"]

    if "Pstator" in out_dict:
        # Store losses
        output.loss = OutLoss(
            Pjoule=out_dict["Pjoule"],
            Pstator=out_dict["Pstator"],
            Pmagnet=out_dict["Pmagnet"],
            Protor=out_dict["Protor"],
            Pprox=out_dict["Pprox"],
        )

    # Calculate slot current density
    output.elec.get_Jrms()

    # Calculate linear current density along airgap
    Irms = np.sqrt(output.elec.OP.Id_ref ** 2 + output.elec.OP.Iq_ref ** 2)
    Irms_slot = Irms * machine.stator.winding.Ntcoil / machine.stator.winding.Npcp
    slot_pitch = 2 * np.pi / machine.stator.get_Zs() * machine.stator.Rint
    output.elec.Arms = Irms_slot / slot_pitch

    if "Erms" in out_dict:
        # Store back-emf rms value
        output.elec.Erms = out_dict["Erms"]

    if "Tem_rip_pp" in out_dict:
        # Store torque ripple
        output.mag.Tem_rip_pp = out_dict["Tem_rip_pp"]
        output.mag.Tem_rip_norm = out_dict["Tem_rip_norm"]
