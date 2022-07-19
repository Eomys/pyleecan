# -*- coding: utf-8 -*-
from deap import base, creator, tools
from ....Classes.Output import Output
from ....Classes.XOutput import XOutput
from ....Classes.VarSimu import VarSimu


def create_toolbox(self):
    """OptiGenAlgNsga2Deap method to create DEAP toolbox
    Parameters
    ----------
    self : OptiGenAlgNsga2Deap

    Returns
    -------
    self : OptiGenAlgNsga2Deap
        OptiGenAlgNsga2Deap with toolbox created
    """

    # Create toolbox
    self.toolbox = base.Toolbox()

    # Create Fitness and individual
    creator.create(
        "FitnessMin", base.Fitness, weights=[-1 for _ in self.problem.obj_func]
    )
    creator.create("Individual", list, typecode="d", fitness=creator.FitnessMin)

    self.toolbox.register("creator", creator.Individual)

    # Create default output
    if isinstance(self.problem.simu.parent, Output):
        output = self.problem.simu.parent
    elif isinstance(
        self.problem.simu.var_simu, VarSimu
    ):  # Optimization of a multi-simulation
        output = XOutput(simu=self.problem.simu.copy())
    else:
        output = Output(simu=self.problem.simu.copy())

    # Register individual and population
    self.toolbox.register(
        "individual",
        create_indiv,
        self.toolbox.creator,
        output,
        self.problem.design_var,
    )

    self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)


def create_indiv(create, output, design_var_list):
    """Create individual using DEAP tools

    Parameters
    ----------
    creator : function
        function to create the individual
    output : ....Classes.Output
        output of the individual
    design_var_list : list
        Design variables

    Returns:
    --------
    indiv : list
        individual
    """

    # Extract design variables
    var = []

    for design_var in design_var_list:
        # Generate the first value
        value = design_var.get_value(design_var.space)
        design_var.setter(output.simu, value)
        var.append(value)

    ind = create(var)

    # Store the design_var_name_list
    ind.design_var_name_list = [dv.name for dv in design_var_list]

    # Store setters in a list
    ind.setter_list = [dv.setter for dv in design_var_list]

    # Store the design variables
    ind.design_var = design_var_list

    # Store the simulation validity
    ind.is_simu_valid = False

    # Store the number of constraints violations
    ind.cstr_viol = 0

    # Output with the design variables set
    ind.output = type(output)(simu=output.simu.as_dict(keep_function=True))

    return ind
