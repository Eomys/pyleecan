from deap.base import Fitness
from pyleecan.Classes.Output import Output
from pyleecan.Methods.Optimization.OptiGenAlgIndivDeap.update import update


class OptiGenAlgIndivDeap(list):
    # cf Methods.Optimization.OptiGenAlgIndivDEAP.update
    update = update

    def __init__(self, output=Output(), design_var={}):

        # Extract design variables
        keys = list(design_var.keys())
        var = []

        keys.sort()
        for key in keys:
            tmp = design_var[key].function(design_var[key].space)
            exec(design_var[key].name + "=tmp")
            var.append(tmp)

        list.__init__(self, var)

        # Create the fitness
        fitness = Fitness
        fitness.weights = [-1 for _ in keys]
        self.fitness = fitness()

        # Store the keys
        self.keys = keys

        # Store the design variables
        self.design_var = design_var

        # Store the design variables values
        self.design_var_value = var

        # Output with the design variables set
        self.output = output

    def __str__(self):
        return list.__str__(self)
