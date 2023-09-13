# -*- coding: utf-8 -*-


def comp_parameters(self, output, Tsta=None, Trot=None):
    """Compute the parameters dict for the equivalent electrical circuit:
    resistance, inductance and back electromotive force
    Parameters
    ----------
    self : EEC_LSRPM
        an EEC_LSRPM object
    output : Output
        an Output object
    """
    machine = output.simu.machine
    p = machine.rotor.winding.p
    PAR = self.parameters

    if self.N0 is None and self.felec is None:
        N0 = 100 * 60 / p
        felec = 100
    elif self.N0 is None and self.felec is not None:
        N0 = self.felec * 60 / p
    elif self.N0 is not None and self.felec is None:
        N0 = self.N0
        felec = N0 / 60 * p
    else:
        N0 = self.N0
        felec = self.felec

    N_s = machine.stator.winding.comp_Ntspc()  # stator number of turns
    # TODO defind the method "comp_N_auxiliary"
    # N_a = machine.stator.winding.comp_N_auxiliary() # damper winding number of turns
    norm = 1  # rotor - stator transformation factor N_a=N_s

    self.parameters["norm"] = norm

    Tws = 20 if "Tws" not in self.parameters else self.parameter["Tws"]
    Twr = 20 if "Twr" not in self.parameters else self.parameter["Twr"]

    # TODO all methods should be verfied for PMSM with damper winding
    if "R_s" not in self.parameters or self.parameters["Rs"] is None:
        # 3 phase equivalent stator resistance
        self.parameters["Rs"] = machine.stator.comp_resistance_wind(T=Tws)

    if "R_a" not in self.parameters or self.parameters["R_a"] is None:
        # 3 phase equivalent damper resistance
        # TODO have to defind the method"comp_resistance_damper_winding"
        R_a = machine.rotor.comp_resistance_damper_winding(T=Twr, qs=3)
        self.parameters["R_a"] = norm**2 * R_a

    if "Phi_m" not in PAR:
        PAR["Phi_m"] = self.fluxlink.comp_fluxlinkage(output)

    if "C_a" not in PAR:
        self.parameters["C_a"] = 0  # Not sure

    is_comp_ind = False
    # check for complete parameter set
    # (there may be some redundancy here but it seems simplier to implement)
    # if not all(k in PAR for k in ("Phid", "Phiq", "Ld", "Lq")):
    #     is_comp_ind = True

    # check for d- and q-current (change)
    if "I_ds" not in PAR or PAR["I_ds"] != output.elec.Ids_ref:
        PAR["I_ds"] = output.elec.Ids_ref
        is_comp_ind = True

    if "I_qs" not in PAR or PAR["I_qs"] != output.elec.Iqs_ref:
        PAR["I_qs"] = output.elec.Iqs_ref
        is_comp_ind = True

    if "I_da" not in PAR or PAR["I_da"] != output.elec.Ida_ref:
        PAR["I_da"] = output.elec.Ida_ref
        is_comp_ind = True

    if "I_qa" not in PAR or PAR["I_qa"] != output.elec.Iqa_ref:
        PAR["I_qa"] = output.elec.Iqa_ref
        is_comp_ind = True

    if "L_dss" not in self.parameters or self.parameters["L_dss"] is None:
        is_comp_ind = True

    if "L_dmu" not in self.parameters or self.parameters["L_dmu"] is None:
        is_comp_ind = True

    if "L_dsa" not in self.parameters or self.parameters["L_dsa"] is None:
        is_comp_ind = True

    if "L_daa" not in self.parameters or self.parameters["L_daa"] is None:
        is_comp_ind = True

    if "L_qss" not in self.parameters or self.parameters["L_qss"] is None:
        is_comp_ind = True

    if "L_qmu" not in self.parameters or self.parameters["L_qmu"] is None:
        is_comp_ind = True

    if "Lr_qaa" not in self.parameters or self.parameters["Lr_qaa"] is None:
        is_comp_ind = True

    # compute inductance if necessary
    if is_comp_ind:
        print("We will return soon")
        print("Please input all variables")

    # TODO It is complexe to calculate
    # (Phi_ds, Phi_qs) = self.indmag.comp_inductance(output) #Have to calculate stator flux by FEA
    # (phi_da, phi_qa) = self.indmag.comp_inductance(output) #Have to calculate damper flux bu FEA

    # PAR["Phi_ds"] = Phi_ds
    # PAR["Phi_qs"] = Phi_qs
    # PAR["Phi_da"] = Phi_da
    # PAR["Phi_qa"] = Phi_qa
