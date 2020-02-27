def add_evaluation(self, output, is_valid, design_var, fitness, ngen):
    """Add an evaluation to the OutputMultiOpti object
    
    Parameters
    ----------
    self : OutputMultiOpti
        Object containing genetic algorithm resutls
    output : Output
        Output
    is_valid : boolean
        Validity of the individual
    design_var : {OptiDesignVar}
        Design variables
    fitness : list
        Fitness of the individual
    ngen : boolean
        Number of the generation
    """

    self.add_output(output, is_valid, design_var)
    self.fitness.append(fitness)
    self.ngen.append(ngen)
