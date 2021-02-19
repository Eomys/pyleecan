def run(self):
    """Run the simulation and optionnaly its multisimulation

    Returns
    -------
    output: Output
        Contains simulation results
    """
    # In-function import to avoid ImportError
    from ....Classes.XOutput import XOutput
    from ....Classes.Output import Output

    # Multi-simulation
    if self.var_simu is not None:
        # make sure simulation output is of class XOutput
        if self.parent is None:
            results = XOutput(simu=self)
        else:
            if not isinstance(self.parent, XOutput):
                msg = (
                    "Simulation.run: A multisimulation has been defined, "
                    + "type XOutput expected for simu.parent, "
                    + f"got {type(self.parent).__name__}. "
                    + "Setting new parent XOutput for simu."
                )
                self.get_logger.warning(msg)
                results = XOutput(simu=self)
            else:
                results = self.parent

        # Logger setup
        self.init_logger(results)

        # Compute the multisimulation
        self.var_simu.run()

    # 'normal' simulation
    else:
        # Output initialization
        if self.parent is None:
            results = Output(simu=self)
        else:
            results = self.parent

        # Logger setup
        if self.index is None:
            self.init_logger(results)
        else:
            self.init_logger(results, is_create=False, is_log_start=False)

        # Compute the simulation
        self.run_single()

    if self.index is None:
        msg = "End of simulation"
        if self.name not in ["", None]:
            msg += " " + self.name
        self.get_logger().info(msg)
    return results
