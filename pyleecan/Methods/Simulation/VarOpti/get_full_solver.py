from ....Classes.OptiProblem import OptiProblem

def evaluate(output):
        """Skip calculations"""
        pass

def get_full_solver(self):
    """Method to return a fully setted solver"""

    # Create reference simulation
    ref_simu = self.parent.copy()
    ref_simu.var_simu = self.var_simu  # var_simu default is None
    ref_simu.index = None
    ref_simu.layer = self.parent.layer + 1

    # Creation of the problem
    problem = OptiProblem(
        simu=ref_simu,         
        design_var=self.paramexplorer_list,
        obj_func=self.objective_list,
        datakeeper_list=self.datakeeper_list,
        constraint=self.constraint_list,
        eval_func=evaluate
    )

    # Reset the parent because when put into problem, parent of simu becomes OptiProblem instead of OutPut
    problem.simu.parent = self.parent.parent
    # Copy the solver to don't rewrite it and give the problem
    solver = self.solver.copy()
    solver.problem = problem

    return solver