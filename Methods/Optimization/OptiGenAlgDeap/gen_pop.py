from pyleecan.Classes.OptiGenAlgIndivDeap import OptiGenAlgIndivDeap
from pyleecan.Classes.Output import Output


def gen_pop(self):
    """Generate the population
    
    Parameters
    ----------
    self : OptiGenAlgNsga2Deap
        Solver using NSGA-II from DEAP  
    """
    self.pop = []
    for _ in range(self.size_pop):
        self.pop.append(
            OptiGenAlgIndivDeap(
                output=Output(simu=self.problem.output.simu.as_dict()),
                design_var=self.problem.design_var,
            )
        )
