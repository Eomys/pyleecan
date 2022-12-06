from numpy import interp, zeros

from ....Classes.SliceModel import SliceModel


def get_slice_model(self):
    """Compute the slice axis required in any Magnetics module

    Parameters
    ----------
    self : SliceModel
        a SliceModel object

    Returns
    -------
    Slice: DataPattern
        Slice axis

    """

    if self.Slice_enforced is None:

        machine = self.parent.machine

        # Rotor length
        L = machine.rotor.L1

        # Check rotor skew
        rotor_skew = machine.rotor.skew
        is_rotor_skew = rotor_skew is not None

        # Enforce slice model depending on rotor skew
        slice_model = SliceModel(L=L)

        if not is_rotor_skew:
            # Single slice model
            Nslices = 2
            z_list = [-0.5 * L, 0.5 * L]
            is_step = True
            angle_rotor = zeros(Nslices)

        elif is_rotor_skew:
            # Slice model is given by skew slices
            if rotor_skew.type_skew == "linear" and not rotor_skew.is_step:
                if self.Nslices_enforced is None:
                    Nslices = 5
                    self.get_logger().debug(
                        "Enforce Nslices_enforced = " + str(Nslices)
                    )
                else:
                    Nslices = self.Nslices_enforced
                if self.type_distribution_enforced is None:
                    type_distribution = "uniform"
                    self.get_logger().debug(
                        "Enforce type_distribution_enforced = " + type_distribution
                    )

                else:
                    type_distribution = self.type_distribution_enforced

                # Calculating rotor skew pattern
                angle_skew, z_skew = rotor_skew.comp_pattern()
                # Calculating requested slice distribution
                slice_model.Nslices = Nslices
                slice_model.type_distribution = type_distribution
                z_norm = slice_model.get_distribution()
                z_list = [z * L for z in z_norm]
                # Interpolating rotor skew angle given new slice distribution
                angle_rotor = interp(z_list, z_skew, angle_skew)

            else:
                if self.Nslices_enforced is not None:
                    self.get_logger().info(
                        "Nslice_enforced is defined but rotor is stepped-skew, set mag.slice_model.Nslices = "
                        + str(rotor_skew.Nstep)
                    )
                angle_rotor, z_list = rotor_skew.comp_pattern()
                Nslices = len(z_list)
            is_step = rotor_skew.is_step

        # Store values in slice model
        slice_model.z_list = z_list
        slice_model.Nslices = Nslices
        slice_model.angle_rotor = angle_rotor
        slice_model.angle_stator = zeros(Nslices)
        slice_model.is_step = is_step
        slice_model.is_skew = is_rotor_skew

        self.Slice_enforced = slice_model

    return self.Slice_enforced
