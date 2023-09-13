from numpy import pi

from SciDataTool import Data1D, DataLinspace, Norm_ref


def comp_axis_angle(self, p, Rag, per_a=None, is_antiper_a=None, Angle_in=None):
    """Compute angle axis with or without periodicities and including normalizations

    Parameters
    ----------
    self : Input
        an Input object
    p : int
        Machine pole pair number
    Rag: float
        Airgap mean radius [m]
    per_a : int
        angle periodicity
    is_antiper_a : bool
        if the angle axis is antiperiodic
    Angle_in: Data
        Input axis angle

    Returns
    -------
    Timee_in: Data
        Requested axis angle

    """

    norm_angle = {"space_order": Norm_ref(ref=p), "distance": Norm_ref(ref=1 / Rag)}

    # Compute angle axis based on input one
    if Angle_in is not None:
        if per_a is None or is_antiper_a is None:
            # Get periodicity from input Angle axis
            per_a, is_antiper_a = Angle_in.get_periodicity()
            per_a = int(per_a / 2) if is_antiper_a else per_a
        # Get Angle axis on requested periodicities
        Angle = Angle_in.get_axis_periodic(Nper=per_a, is_aper=is_antiper_a)
        Angle.normalizations = norm_angle

    # Create angle axis
    elif self.angle is None:
        # Create angle axis as a DataLinspace
        Angle = DataLinspace(
            name="angle",
            unit="rad",
            initial=0,
            final=2 * pi,
            number=self.Na_tot,
            include_endpoint=False,
            normalizations=norm_angle,
        )
        # Add angle (anti-)periodicity
        if per_a > 1 or is_antiper_a:
            Angle = Angle.get_axis_periodic(per_a, is_antiper_a)

    else:
        # Load angle data
        angle = self.angle.get_data()
        self.Na_tot = angle.size
        Angle = Data1D(
            name="angle", unit="rad", values=angle, normalizations=norm_angle
        )
        # Add angle (anti-)periodicity
        sym_a = dict()
        if is_antiper_a:
            sym_a["antiperiod"] = per_a
        elif per_a > 1:
            sym_a["period"] = per_a
        Angle.symmetries = sym_a
        Angle = Angle.to_linspace()

    return Angle
