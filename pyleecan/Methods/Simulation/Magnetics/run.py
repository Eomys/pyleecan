from numpy import zeros, ndarray, iscomplexobj, tile

from pyleecan.Classes.MeshSolution import MeshSolution

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the Magnetics module"""
    if self.parent is None:
        raise InputError("The Magnetic object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("The Simulation object must be in an Output object to run")
    self.get_logger().info("Starting Magnetic module")
    self.get_logger().debug("Using " + self.__class__.__name__ + " object")

    output = self.parent.parent

    # Get slice model and store it in output
    slice_model = self.get_slice_model()
    output.mag.Slice = slice_model

    # Compute and store time and angle axes from elec output
    # and returns additional axes in axes_dict
    axes_dict = self.comp_axes(output)

    # Get z axis
    Slice_axis = axes_dict["z"]
    unique_indices = Slice_axis.unique_indices

    # Get stator and rotor currents if requested
    if "time" in axes_dict:
        Is_val, Ir_val = self.comp_I_mag(output, Time=axes_dict["time"])
    else:
        Is_val, Ir_val = None, None

    # First iteration to check dimensions
    # Assign stator and rotor angle shifts
    self.angle_stator_shift = float(slice_model.angle_stator[unique_indices[0]])
    self.angle_rotor_shift = float(slice_model.angle_rotor[unique_indices[0]])

    # Calculate airgap flux
    Nslices = len(unique_indices)
    if Nslices > 1:
        self.get_logger().info("Solving slice 1 / " + str(Nslices))
    out_dict = self.comp_flux_airgap(output, axes_dict, Is_val=Is_val, Ir_val=Ir_val)

    is_loop = True

    if Nslices == 1:
        is_loop = False
        is_resize = True
        for key in ["B_{rad}", "B_{circ}", "B_{ax}", "Tem"]:
            if key in out_dict:
                if len(out_dict[key].shape) == 3:
                    is_resize = False
                    break
        if is_resize:
            for key in out_dict:
                if isinstance(out_dict[key], ndarray):
                    out_dict[key] = out_dict[key][..., None]
                elif key == "Phi_wind":
                    for phi_key in out_dict[key]:
                        if len(out_dict[key][phi_key]) != 3:
                            out_dict[key][phi_key] = out_dict[key][phi_key][..., None]
    else:
        for key in ["B_{rad}", "B_{circ}", "B_{ax}", "Tem", "Phi_wind"]:
            if key in out_dict:
                if key == "Phi_wind":
                    # Take first value in Phi_wind dict
                    val = list(out_dict[key].values())[0]
                else:
                    val = out_dict[key]
                if len(val.shape) == 3:
                    if val.shape[2] > 1:
                        # Flux is already 3D -> no loop
                        is_loop = False
        if not is_loop:
            for ii in range(Nslices)[1:]:
                self.get_logger().info(
                    "Solving slice " + str(ii + 1) + " / " + str(Nslices)
                )

    if is_loop:
        for key in out_dict:
            if isinstance(out_dict[key], ndarray):
                field = out_dict[key].copy()
                if iscomplexobj(field):
                    dtype = complex
                else:
                    dtype = float
                out_dict[key] = zeros(
                    tuple([s for s in field.shape] + [Nslices]), dtype=dtype
                )
                out_dict[key][..., 0] = field
            elif isinstance(out_dict[key], dict):
                for key2 in out_dict[key]:
                    if isinstance(out_dict[key][key2], ndarray):
                        if iscomplexobj(out_dict[key][key2]):
                            dtype = complex
                        else:
                            dtype = float
                        field = out_dict[key][key2].copy()
                        out_dict[key][key2] = zeros(
                            tuple([s for s in field.shape] + [Nslices]), dtype=dtype
                        )
                        out_dict[key][key2][..., 0] = field

        # Loop over other slices
        for ii, index in enumerate(unique_indices[1:]):
            self.get_logger().info(
                "Solving slice " + str(ii + 2) + " / " + str(Nslices)
            )
            # Assign stator and rotor angle shifts
            self.angle_stator_shift = float(slice_model.angle_stator[index])
            self.angle_rotor_shift = float(slice_model.angle_rotor[index])

            # Calculate airgap flux
            out_dict_index = self.comp_flux_airgap(
                output,
                axes_dict,
                Is_val=Is_val,
                Ir_val=Ir_val,
            )

            # Store in out_dict matrices
            for key in out_dict_index:
                if isinstance(out_dict_index[key], ndarray):
                    out_dict[key][..., ii + 1] = out_dict_index[key]
                elif isinstance(out_dict[key], dict):
                    for key2 in out_dict[key]:
                        out_dict[key][key2][..., ii + 1] = out_dict_index[key][key2]
                elif isinstance(out_dict[key], MeshSolution):
                    out_dict[key] = self.build_MS_sliced(
                        out_dict[key], out_dict_index[key], axes_dict, Nslices, ii + 2
                    )
                else:
                    # TODO store other outputs in lists
                    out_dict[key] = out_dict_index[key]

    # Store magnetic quantities contained in out_dict in OutMag, as Data object if necessary
    output.mag.store(out_dict, axes_dict)
    output.mag.comp_power()
