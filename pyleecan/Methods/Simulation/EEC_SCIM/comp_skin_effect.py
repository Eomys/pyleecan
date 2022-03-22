def comp_skin_effect(self):
    """Compute and set the skin effect factors (update value in object)

    Parameters
    ----------
    self : EEC_SCIM
        An EEC_SCIM objects
    """

    assert self.OP is not None
    assert self.Tsta is not None
    assert self.Trot is not None
    machine = self.get_machine_from_parent()
    CondS = machine.stator.winding.conductor
    CondR = machine.rotor.winding.conductor
    felec = self.OP.get_felec()
    slip = self.OP.get_slip()

    # compute skin_effect on stator side
    self.Xkr_skinS = CondS.comp_skin_effect_resistance(
        freq=felec, T_op=self.Tsta, T_ref=20
    )

    self.Xke_skinS = CondS.comp_skin_effect_inductance(
        freq=felec, T_op=self.Tsta, T_ref=20
    )

    # compute skin_effect on rotor side
    if felec * slip > 0:
        self.Xkr_skinR = CondR.comp_skin_effect_resistance(
            freq=felec * slip, T_op=self.Trot, T_ref=20
        )

        self.Xke_skinR = CondR.comp_skin_effect_inductance(
            freq=felec * slip, T_op=self.Trot, T_ref=20
        )
    else:
        self.Xkr_skinR, self.Xke_skinR = 1, 1
