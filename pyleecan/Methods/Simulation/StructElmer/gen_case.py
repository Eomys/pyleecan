# -*- coding: utf-8 -*-

from os.path import join, split
from numpy import pi

from ....Classes.Section import Section
from ....Classes.SolverInputFile import SolverInputFile
from ....Methods.Elmer.Section import File, Variable, MATC


# constants
# TODO set these constants in dependence of actual number of bodies, i.e. one set of
#     respective sections per body
# TODO set magnet material properties by utilizing label 'translation' dict
#     therefore a 'get_material_by_label' function would be very handy (unite with FEMM)
ID_LAM = 1
ID_MAG = 2


def gen_case(self, output, mesh_names):
    """Setup the Elmer Case file (.sif file)"""

    # get the save path
    save_dir = self.get_path_save_fea(output)

    sif_file = join(save_dir, "case.sif")

    # save solver start info
    start_file = join(save_dir, "ELMERSOLVER_STARTINFO")

    with open(start_file, "wt") as fout:
        fout.write(split(sif_file)[1])

    # generate list of mesh names
    names = []
    for value in mesh_names.values():
        names.extend(value)

    # --- prepare sections ----------------------------------------------------------- #
    # --- bodies --------------------------------------------------------------------- #
    bodies = []
    for name in names:
        if "Body" in name:
            body = Section(section="Body", id=len(bodies) + 1)
            body["name"] = name
            body["Equation"] = 1
            if "Magnet" in name:
                body["Material"] = ID_MAG
            elif "Lamination" in name:
                body["Material"] = ID_LAM
            body["Body Force"] = 1

            bodies.append(body)

    # --- simulation ----------------------------------------------------------------- #
    sim = Section(section="Simulation")
    sim["Max Output Level"] = 5
    sim["Coordinate System"] = "Cartesian 2D"
    sim["Coordinate Mapping"] = [1, 2, 3]
    sim["Simulation Type"] = "Steady State"
    sim["Steady State Max Iterations"] = 1
    sim["Initialize Dirichlet Conditions"] = False
    # sim["Output File"] = File("simulation.result")
    sim["Use Mesh Names"] = True

    # --- constants ------------------------------------------------------------------ #
    const = Section(section="Constants")
    const["Gravity"] = [0.0, -1.0, 0.0, 9.82]

    # --- solvers -------------------------------------------------------------------- #
    solver_list = []

    # solver - move mesh before simulation
    i = 1
    solver = Section(section="Solver", id=i)
    solver.comment = "Moves the magnets as defined in the body force section"
    solver["Exec Solver"] = "Before all"
    solver["Equation"] = "MeshDeform"
    solver["Procedure"] = [File("RigidMeshMapper"), File("RigidMeshMapper")]
    solver_list.append(solver)

    # solver - elasticity simulation
    i += 1
    solver = Section(section="Solver", id=i)
    solver["Equation"] = "Linear Elasticity"
    solver["Procedure"] = [File("ElasticSolve"), File("ElasticSolver")]
    solver["Variable"] = "-dofs 2 Displacement"
    solver["Linear System Solver"] = "Iterative"
    solver["Linear System Preconditioning"] = "ILU3"
    solver["Linear System Residual Output"] = 10
    solver["Linear System Max Iterations"] = 400
    solver["Linear System Iterative Method"] = "GCR"
    solver["Linear System Convergence Tolerance"] = 1.0e-9
    solver["Linear System Abort Not Converged"] = False
    solver["Linear System Residual Mode"] = True
    solver["Nonlinear System Convergence Tolerance"] = 1.0e-7
    solver["Nonlinear System Max Iterations"] = 20
    solver["Nonlinear System Relaxation Factor"] = 1.0
    # solver['Displace Mesh'] = True
    solver["Calculate Principal"] = True
    solver["Calculate Loads"] = True
    solver["Calculate Stresses"] = True
    solver["Calculate Strains"] = True
    solver["Apply Contact BCs"] = True
    solver["Stabilize"] = True
    solver["Elasticity Solver Linear"] = True
    solver["Optimize Bandwidth"] = True
    solver_list.append(solver)

    # solver - save results as vtu if requested
    i += 1
    solver = Section(section="Solver", id=i)
    solver["Exec Solver"] = "After Simulation" if self.is_save_FEA else "Never"
    solver["Equation"] = "result output"
    solver["Procedure"] = [File("ResultOutputSolve"), File("ResultOutputSolver")]
    solver["Output Directory"] = File("Results")
    solver["Output File Name"] = File("case")
    solver["Vtu Format"] = True
    # solver["Ascii Output"] = True  # to save vtu as ascii
    solver["Save Geometry Ids"] = True
    solver["Displace Mesh"] = True
    solver["Single Precision"] = True  # default: False, False == 32 bit, True == 64 bit
    solver_list.append(solver)

    # solver - save statistical, integral, min, max, mean, ... values
    i += 1
    solver = Section(section="Solver", id=i)
    solver["Exec Solver"] = "After Simulation"
    solver["Equation"] = "SaveScalars"
    solver["Procedure"] = [File("SaveData"), File("SaveScalars")]
    solver["Output Directory"] = File("Results")
    solver["Filename"] = File("Scalars.dat")
    solver["Operator 1"] = "boundary int"
    solver["Variable 1"] = "Principal Stress 1"
    solver["Mask Name 1"] = "MASTER_ROTOR_BOUNDARY"
    solver["Operator 2"] = "boundary int"
    solver["Variable 2"] = "Principal Stress 2"
    solver["Mask Name 2"] = "MASTER_ROTOR_BOUNDARY"
    solver["Operator 3"] = "boundary int"
    solver["Variable 3"] = "Principal Stress 1"
    solver["Mask Name 3"] = "SLAVE_ROTOR_BOUNDARY"
    solver["Operator 4"] = "boundary int"
    solver["Variable 4"] = "Principal Stress 2"
    solver["Mask Name 4"] = "SLAVE_ROTOR_BOUNDARY"
    solver_list.append(solver)

    # solver - save line values
    # if no variable given, all variables are saved
    i += 1
    solver = Section(section="Solver", id=i)
    solver["Exec Solver"] = "After Simulation"
    solver["Equation"] = "SaveLineValues"
    solver["Procedure"] = [File("SaveData"), File("SaveLine")]
    solver["Output Directory"] = File("Results")
    solver["Filename"] = File("LineValues.dat")
    solver["Variable 1"] = "Displacement 1"
    solver["Variable 2"] = "Displacement 2"
    solver["Variable 3"] = "Principal Stress 1"
    solver["Variable 4"] = "Principal Stress 2"
    solver["Variable 5"] = "VonMises"
    # solver["Save Mask 1"] = "MASTER_ROTOR_BOUNDARY"
    # solver["Skip Boundary Info"] = Logical True
    solver_list.append(solver)

    # Variable 1 = Stress Bodyforce 1
    # Mask Name 1 = BodyForce
    # Operator 2 = boundary int
    # Variable 2 = Displacement Loads 1
    # Mask Name 2 = Top_0
    # Operator 3 = boundary int
    # Variable 3 = Displacement Loads 2
    # Mask Name 3 = Top_0
    # Operator 4 = boundary int
    # Variable 4 = Displacement Contact Load 1
    # Mask Name 4 = Top_0

    # Solver 5
    # Equation = "SaveMaterial"
    # Procedure = File "SaveData" "SaveMaterials"
    # !Parameter 1 = String "Stress Bodyforce 1"
    # !Parameter 2 = String "Stress Bodyforce 2"
    # !Body Force Parameters = 1

    # --- equations ------------------------------------------------------------------ #
    eqs = Section(section="Equation", id=1)
    eqs["Name"] = "Equation"
    eqs["Active Solvers"] = [i + 1 for i in range(len(solver_list))]

    # --- materials ------------------------------------------------------------------ #
    # TODO get magnets materials is inconvienent
    materials = [None, None, None]  # one extra element since ID_xx starts with 1

    mat_section = [Section(section="Material", id=ID_LAM)]
    materials[ID_LAM] = output.simu.machine.rotor.mat_type

    if self.include_magnets:
        mat_section.append(Section(section="Material", id=ID_MAG))
        materials[ID_MAG] = output.simu.machine.rotor.hole[0].magnet_0.mat_type

    # add materials to material sections
    for idx in range(len(mat_section)):
        ID = mat_section[idx].id
        mat_section[idx]["Name"] = materials[ID].name
        mat_section[idx]["Density"] = float(materials[ID].struct.rho)
        mat_section[idx]["Youngs modulus"] = float(materials[ID].struct.Ex)
        mat_section[idx]["Poisson ratio"] = float(materials[ID].struct.nu_xy)
        # TODO check anisotropy

    # --- boundary conditions -------------------------------------------------------- #

    boundaries = []
    i = 0

    # pair master and slave of Magnet_x_Top, Magnet_0_Right and Magnet_1_Left
    paired_bnds = [
        "Rotor_Magnet_0_Top",
        "Rotor_Magnet_1_Top",
        "Rotor_Magnet_0_Right",
        "Rotor_Magnet_1_Left",
    ]

    for name in paired_bnds:
        master = name + "_Master"
        slave = name + "_Slave"
        if master in names and slave in names:
            # "slave"
            i += 1
            bnd = Section(section="Boundary Condition", id=i)
            bnd["Name"] = slave
            bnd["Normal-Tangential Displacement"] = True
            bnd["Periodic BC"] = i + 1  # next bnd will be the corresponding master
            bnd["Periodic BC Displacement 1"] = True  # normal disp is fixed between M&S
            bnd["Periodic BC Displacement 2"] = False  # tangential disp is independent
            bnd["Periodic BC Pressure"] = False  # pressure can be independent
            bnd["Top_0"] = True  # for save values
            boundaries.append(bnd)

            # "master"
            i += 1
            bnd = Section(section="Boundary Condition", id=i)
            bnd["Name"] = master
            bnd["Normal-Tangential Displacement"] = True
            boundaries.append(bnd)

    # no normal displacement on lamination sides
    i += 1
    bnd = Section(section="Boundary Condition", id=i)
    bnd["Name"] = "MASTER_ROTOR_BOUNDARY"
    bnd["Displacement 1"] = 0.0
    bnd["Normal-Tangential Displacement"] = True
    bnd["Save Line"] = True
    bnd["Save Scalars"] = True
    bnd["MASTER_ROTOR_BOUNDARY"] = True  # mask name for SaveLine and SaveScalar
    boundaries.append(bnd)

    i += 1
    bnd = Section(section="Boundary Condition", id=i)
    bnd["Name"] = "SLAVE_ROTOR_BOUNDARY"
    bnd["Displacement 1"] = 0.0
    bnd["Normal-Tangential Displacement"] = True
    bnd["Save Line"] = True
    bnd["Save Scalars"] = True
    bnd["SLAVE_ROTOR_BOUNDARY"] = True  # mask name for SaveLine and SaveScalar
    boundaries.append(bnd)

    i += 1  # Boundary to save line values
    bnd = Section(section="Boundary Condition", id=i)
    bnd["Name"] = "ROTOR_BORE_CURVE"
    # bnd["Normal-Tangential Displacement"] = True
    bnd["Save Line"] = True
    bnd["Save Scalars"] = True
    boundaries.append(bnd)

    # --- body force ----------------------------------------------------------------- #
    omega = 2 * pi * self.parent.input.N0 / 60
    bfs = []

    ID_list = [
        ID_LAM,
    ]
    if self.include_magnets:
        ID_list.append(ID_MAG)

    for ID in ID_list:
        matc = MATC(expr=f"{materials[ID].struct.rho}*{omega}^2*tx(0)")
        bf = Section(section="Body Force", id=ID)
        bf["Name"] = "Stress"
        bf["Mesh Rotate 3"] = 0.0
        bf["Stress Bodyforce 1"] = Variable(name="Coordinate 1", value=matc)
        bf["Stress Bodyforce 2"] = Variable(name="Coordinate 2", value=matc)
        bfs.append(bf)

    # -------------------------------------------------------------------------------- #
    # list of section - list need to be extended, single obj. can be appended
    sect_list = []
    sect_list.extend(bodies)
    sect_list.append(sim)
    sect_list.append(const)
    sect_list.extend(mat_section)
    sect_list.extend(solver_list)
    sect_list.append(eqs)
    sect_list.extend(boundaries)
    sect_list.extend(bfs)

    # create SolverInputFile obj.
    sif = SolverInputFile(sections=sect_list)

    # save the sif file
    with open(sif_file, "wt") as f:
        sif.write(f)
