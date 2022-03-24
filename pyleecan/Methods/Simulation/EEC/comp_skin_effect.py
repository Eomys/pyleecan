def comp_skin_effect(self):
    """Compute the skin effect factors (update value in object)

    Parameters
    ----------
    self : EEC
        An EEC objects
    """

    assert self.OP is not None
    assert self.Tsta is not None
    assert self.Trot is not None
    machine = self.get_machine_from_parent()
    CondS = machine.stator.winding.conductor
    felec = self.OP.get_felec()

    # compute skin_effect on stator side
    self.Xkr_skinS = CondS.comp_skin_effect_resistance(
        freq=felec, T_op=self.Tsta, T_ref=20
    )

    self.Xke_skinS = CondS.comp_skin_effect_inductance(
        freq=felec, T_op=self.Tsta, T_ref=20
    )
