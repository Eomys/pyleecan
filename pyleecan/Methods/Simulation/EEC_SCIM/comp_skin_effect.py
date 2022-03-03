def comp_skin_effect(self):
    """Compute the skin effect factors (update value in object)

    Parameters
    ----------
    self : EEC_SCIM
        An EEC_SCIM objects
    """

    assert self.OP is not None
    assert self.Tsta is not None
    assert self.Trot is not None
    machine = self.get_machine()
    CondS = machine.stator.winding.conductor
    CondR = machine.rotor.winding.conductor
    felec = self.OP.get_felec()
    slip = self.OP.get_slip()

    # compute skin_effect on stator side
    if self.type_skin_effect:
        Tfact1 = CondS.comp_temperature_effect(T_op=self.Tsta, T_ref=20)
        self.Xkr_skinS, self.Xke_skinS = CondS.comp_skin_effect(
            freq=felec, Tfact=Tfact1
        )
    else:
        self.Xkr_skinS, self.Xke_skinS = 1, 1

    # compute skin_effect on rotor side
    if self.type_skin_effect and felec * slip > 0:
        Tfact2 = CondR.comp_temperature_effect(T_op=self.Trot, T_ref=20)
        self.Xkr_skinR, self.Xke_skinR = CondR.comp_skin_effect(
            freq=felec * slip, Tfact=Tfact2
        )
    else:
        self.Xkr_skinR, self.Xke_skinR = 1, 1
