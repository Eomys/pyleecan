from deap.base import Fitness
from pyleecan.Classes.Output import Output
from pyleecan.Methods.Optimization.OptiGenAlgIndivDEAP.update import update


class OptiGenAlgIndivDEAP(list):
    # cf Methods.Optimization.OptiGenAlgIndivDEAP.update
    update = update

    def __init__(self, output=Output(), design_var={}, weights=()):
        if not isinstance(weights, tuple) and not isinstance(weights, list):
            raise TypeError("Indiv.weights must be a tuple or a list.")
        if len(weights) == 0:
            raise Exception("Weights cannot be empty.")

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
        fitness.weights = weights
        self.fitness = fitness()

        # Store the design variables
        self.design_var = design_var

        # Output with the design variables set
        self.output = output

    def __str__(self):
        return list.__str__(self)
