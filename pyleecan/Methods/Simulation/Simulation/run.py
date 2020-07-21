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

    if self.var_simu is not None:
        # Multi-simulation
        if self.parent is None:
            results = XOutput(simu=self)
        else:
            if not isinstance(self.parent, XOutput):
                raise TypeError(
                    "A multisimulation has been defined, type XOutput expected for simu.parent, got {}".format(
                        type(self.parent).__name__
                    )
                )

        # Compute the reference simulation
        if self.var_simu.ref_simu_index is None:
            self.run_single()

        self.var_simu.run()

    else:
        if self.parent is None:
            results = Output(simu=self)
        else:
            results = self.parent

        self.run_single()

    return results
