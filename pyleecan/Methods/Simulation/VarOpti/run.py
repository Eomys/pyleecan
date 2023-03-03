def run(self):
    """Run method for VarOpti to solve the problem"""

    solver = self.get_full_solver()

    # Launch simulations
    xoutput = solver.solve(xoutput=self.parent.parent)

    return xoutput
