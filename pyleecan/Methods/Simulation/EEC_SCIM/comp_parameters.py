# -*- coding: utf-8 -*-
from numpy import zeros, sqrt, pi, tile
from ....Functions.Electrical.coordinate_transformation import n2ab, ab2n


def comp_parameters(self, output):
    """Compute the parameters dict for the equivalent electrical circuit:
    resistance, inductance
    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    output : Output
        an Output object
    """
    # number of time steps for averaging (FEMM only) TODO make user input of it
    n_step = 32

    # get some machine parameters
    machine = output.simu.machine
    Zsr = machine.rotor.slot.Zs
    qsr = machine.rotor.winding.qs
    p = machine.get_pole_pair_number()
    qss = machine.stator.winding.qs
    sym = machine.comp_periodicity()[0]

    xi = machine.stator.winding.comp_winding_factor()
    Ntspc = machine.stator.winding.comp_Ntspc()
    norm = (xi[0] * Ntspc) / (Zsr / 6)  # rotor - stator transformation norm

    self.parameters["norm"] = norm

    # get temperatures TODO remove/replace, since this is a temp. solution only
    Tws = 20 if "Tws" not in self.parameters else self.parameter["Tws"]
    Twr = 20 if "Twr" not in self.parameters else self.parameter["Twr"]

    #
    is_comp_ind = False

    # Parameters to compute only once
    if "Rs" not in self.parameters or self.parameters["Rs"] is None:
        self.parameters["Rs"] = machine.stator.comp_resistance_wind(T=Tws)

    if "Rr_norm" not in self.parameters or self.parameters["Rr_norm"] is None:
        # 3 phase equivalent rotor resistance
        Rr = machine.rotor.comp_resistance_wind(T=Twr, qs=3)
        self.parameters["Rr_norm"] = norm ** 2 * Rr

    if "slip" not in self.parameters or self.parameters["slip"] is None:
        zp = output.simu.machine.stator.get_pole_pair_number()
        Nr = output.elec.N0
        Ns = output.elec.felec / zp * 60
        self.parameters["slip"] = (Ns - Nr) / Ns
        # print(f"slip = {(Ns - Nr) / Ns}")

    if "Lm" not in self.parameters or self.parameters["Lm"] is None:
        is_comp_ind = True

    if "Ls" not in self.parameters or self.parameters["Ls"] is None:
        is_comp_ind = True

    if "Lr_norm" not in self.parameters or self.parameters["Lr_norm"] is None:
        is_comp_ind = True

    if "Rfe" not in self.parameters:
        self.parameters["Rfe"] = None  # TODO calculate (or estimate at least)

    if is_comp_ind:
        # setup a MagFEMM simulation to get the parameters
        # TODO utilize paralellization
        # TODO maybe use IndMagFEMM or FluxlinkageFEMM
        # TODO but for now they are not suitable so I utilize 'normal' MagFEMM simu
        from ....Classes.Simu1 import Simu1
        from ....Classes.InputCurrent import InputCurrent
        from ....Classes.MagFEMM import MagFEMM
        from ....Classes.Output import Output
        from ....Classes.ImportGenVectLin import ImportGenVectLin
        from ....Classes.ImportMatrixVal import ImportMatrixVal

        # set frequency and time
        # TODO what will be the best settings to get a good average with min. samples
        N0 = 1500
        T = 60 / N0 / 2 / qss
        felec = 50
        Ir = ImportMatrixVal(value=zeros((n_step, qsr)))
        time = ImportGenVectLin(start=0, stop=T, num=n_step, endpoint=False)

        # estimate magnetizing current
        Imu = 2

        # setup the simu object
        simu = Simu1(name="EEC_comp_parameter", machine=machine.copy())
        # Definition of the enforced output of the electrical module
        simu.input = InputCurrent(
            Is=None,
            Id_ref=Imu,
            Iq_ref=0,
            Ir=Ir,  # zero current for the rotor
            N0=N0,
            angle_rotor=None,  # Will be computed
            time=time,
            felec=felec,
        )

        # Definition of the magnetic simulation (no symmetry)
        simu.mag = MagFEMM(
            type_BH_stator=0,
            type_BH_rotor=0,
            is_periodicity_a=False,
            is_periodicity_t=False,
            Kgeo_fineness=0.5,
            Kmesh_fineness=0.5,
        )
        simu.force = None
        simu.struct = None

        # --- compute the main inductance and stator stray inductance ---
        # set output and run first simulation
        out = Output(simu=simu)
        out.simu.run()

        # compute average rotor and stator fluxlinkage
        # TODO check wind_mat that the i-th bars is in the i-th slots
        Phi_s, Phi_r = _comp_flux_mean(out, qsr, sym)

        self.parameters["Lm"] = (Phi_r * norm * Zsr / 3) / Imu
        self.parameters["Ls"] = (Phi_s - (Phi_r * norm * Zsr / 3)) / Imu

        # --- compute the main inductance and rotor stray inductance ---
        # set new output
        out = Output(simu=simu)

        # set current values
        Ir_ = zeros([n_step, 2])
        Ir_[:, 0] = Imu * norm * sqrt(2)
        Ir = ab2n(Ir_, n=qsr // sym)  # TODO no rotation for now

        Ir = ImportMatrixVal(value=tile(Ir, (1, sym)))

        simu.input.Is = None
        simu.input.Id_ref = 0
        simu.input.Iq_ref = 0
        simu.input.Ir = Ir

        out.simu.run()

        # compute average rotor and stator fluxlinkage
        # TODO check wind_mat that the i-th bars is in the i-th slots
        Phi_s, Phi_r = _comp_flux_mean(out, qsr, sym)

        self.parameters["Lm_"] = Phi_s / Imu
        self.parameters["Lr_norm"] = ((Phi_r * norm * Zsr / 3) - Phi_s) / Imu


def _comp_flux_mean(out, qsr, sym):
    # get the fluxlinkage
    # TODO add fix for single time value
    Phi = out.mag.Phi_wind_rotor.get_along("time", "phase")["Phi_{wind}"]

    # compute mean value of periodic bar fluxlinkage
    qsr_eff = qsr // sym
    Phi_ab = zeros([Phi.shape[0], 2])
    for ii in range(sym):
        id0 = qsr_eff * ii
        id1 = qsr_eff * (ii + 1)
        Phi_ab += n2ab(Phi[:, id0:id1], n=qsr_eff) / sym

    # compute rotor and stator fluxlinkage
    Phi_r = abs(Phi_ab[:, 0] + 1j * Phi_ab[:, 1]).mean() / sqrt(2)

    # TODO add fix for single time value
    Phi_ab = n2ab(out.mag.Phi_wind_stator.get_along("time", "phase")["Phi_{wind}"])
    Phi_s = abs(Phi_ab[:, 0] + 1j * Phi_ab[:, 1]).mean() / sqrt(2)

    return Phi_s, Phi_r
