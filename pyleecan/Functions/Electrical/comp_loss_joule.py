def comp_loss_joule(lam, T_op, OP, type_skin_effect):
    """Calculate joule losses in given lamination and OP

    Parameters
    ----------
    lam: LamSlotWind
        a lamination object with windings
    T_op: float
        Winding temperature in degree Celsius
    OP: OP
        An Op object
    type_skin_effect: int
        1 to include skin effect, 0 to ignore it

    Returns
    -------
    Pjoule : float
        Joule losses [W]
    """

    Rs = lam.comp_resistance_wind(T=T_op)
    qs = lam.winding.qs

    if type_skin_effect > 0:
        # Account for skin effect
        kr_skin = lam.winding.conductor.comp_skin_effect_resistance(
            T_op=T_op, freq=OP.get_felec()
        )
        Rs *= kr_skin

    # Calculate overall joule losses
    Pjoule = qs * Rs * (OP.Id_ref**2 + OP.Iq_ref**2)

    return Pjoule
