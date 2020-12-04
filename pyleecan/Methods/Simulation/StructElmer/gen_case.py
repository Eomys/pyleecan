# -*- coding: utf-8 -*-

from os.path import join, split
from numpy import pi

from ....Classes.Section import Section
from ....Classes.SolverInputFile import SolverInputFile
from ....Methods.Elmer.Section import File, Variable, MATC


# temp shortcut
# names = [
#     "Magnet_0_Body",
#     "Lamination_0_Body",
#     "Magnet_1_Body",
#     "Magnet_0_Right_Slave",
#     "Magnet_0_Bottom_Slave",
#     "Magnet_0_Left_Slave",
#     "Magnet_0_Top_Slave",
#     "Magnet_1_Left_Slave",
#     "Magnet_1_Bottom_Slave",
#     "Magnet_1_Right_Slave",
#     "Magnet_0_Right_Master",
#     "Magnet_0_Bottom_Master",
#     "Magnet_0_Left_Master",
#     "Magnet_0_Top_Master",
#     "Magnet_1_Left_Master",
#     "Magnet_1_Bottom_Master",
#     "Magnet_1_Right_Master",
#     "Magnet_1_Top_Master",
#     "Magnet_1_Top_Slave",
#     "MASTER_ROTOR_BOUNDARY",
#     "SLAVE_ROTOR_BOUNDARY",
# ]

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

    # --- prepare sections ---
    # bodies
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

    # simulation
    sim = Section(section="Simulation")
    sim["Max Output Level"] = 5
    sim["Coordinate System"] = "Cartesian 2D"
    sim["Coordinate Mapping"] = [1, 2, 3]
    sim["Simulation Type"] = "Steady State"
    sim["Steady State Max Iterations"] = 1
    sim["Initialize Dirichlet Conditions"] = False
    sim["Output File"] = File("simulation.result")
    sim["Use Mesh Names"] = True

    # constants
    const = Section(section="Constants")
    const["Gravity"] = [0.0, -1.0, 0.0, 9.82]

    # --- solvers ---
    solver_list = []

    # solver 1
    i = 1
    solver = Section(section="Solver", id=i)
    solver.comment = "Moves the magnets as defined in the body force section"
    solver["Exec Solver"] = "Before all"
    solver["Equation"] = "MeshDeform"
    solver["Procedure"] = [File("RigidMeshMapper"), File("RigidMeshMapper")]
    solver_list.append(solver)

    # solver 2
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
    solver["Linear System Convergence Tolerance"] = 1.0e-12
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

    # solver 3
    # i += 1
    # solver = Section(section='Solver', id=i)

    # Exec Solver = After Simulation
    # Equation = SaveScalars
    # Procedure = "SaveData" "SaveScalars"
    # Filename = forces.dat

    # Operator 1 = body force int
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

    # Solver 4
    i += 1
    solver = Section(section="Solver", id=i)
    # solver["Exec Solver"] = "never"
    solver["Equation"] = "result output"
    solver["Procedure"] = [File("ResultOutputSolve"), File("ResultOutputSolver")]
    solver["Output File Name"] = File("case")
    solver["Vtu Format"] = True
    solver["Displace Mesh"] = True
    solver["Single Precision"] = False
    solver_list.append(solver)

    # Solver 5
    # Equation = "SaveMaterial"
    # Procedure = File "SaveData" "SaveMaterials"

    # !Parameter 1 = String "Stress Bodyforce 1"
    # !Parameter 2 = String "Stress Bodyforce 2"
    # !Body Force Parameters = 1

    # End

    # equations
    eqs = Section(section="Equation", id=1)
    eqs["Name"] = "Equation"
    eqs["Active Solvers"] = [i + 1 for i in range(len(solver_list))]

    # materials
    # TODO get magnets materials is inconvienent
    mag_mat = output.simu.machine.rotor.hole[0].magnet_0.mat_type
    lam_mat = output.simu.machine.rotor.mat_type

    mat = [
        Section(section="Material", id=ID_LAM),
        Section(section="Material", id=ID_MAG),
    ]

    materials = [None, None, None]  # one extra element since ID_xx starts with 1
    materials[ID_LAM] = lam_mat
    materials[ID_MAG] = mag_mat

    for idx in range(len(mat)):
        ID = mat[idx].id
        mat[idx]["Name"] = materials[ID].name
        mat[idx]["Density"] = float(materials[ID].struct.rho)
        mat[idx]["Youngs modulus"] = float(materials[ID].struct.Ex)
        mat[idx]["Poisson ratio"] = float(materials[ID].struct.nu_xy)
        # TODO check anisotropy

    # boundary conditions

    boundaries = []
    i = 0

    # pair master and slave of Magnet_x_Top, Magnet_0_Right and Magnet_1_Left
    paired_bnds = [
        "Magnet_0_Top",
        "Magnet_1_Top",
        "Magnet_0_Right",
        "Magnet_1_Left",
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
    boundaries.append(bnd)

    i += 1
    bnd = Section(section="Boundary Condition", id=i)
    bnd["Name"] = "SLAVE_ROTOR_BOUNDARY"
    bnd["Displacement 1"] = 0.0
    bnd["Normal-Tangential Displacement"] = True
    boundaries.append(bnd)

    # body force
    omega = 2 * pi * self.parent.input.N0
    bfs = []
    for ID in [ID_LAM, ID_MAG]:
        matc = MATC(expr=f"{materials[ID].struct.rho}*{omega}^2*tx(0)")
        bf = Section(section="Body Force", id=ID)
        bf["Name"] = "Stress"
        bf["Mesh Rotate 3"] = 0.0
        bf["Stress Bodyforce 1"] = Variable(name="Coordinate 1", value=matc)
        bf["Stress Bodyforce 2"] = Variable(name="Coordinate 2", value=matc)
        bfs.append(bf)

    # list of section - list need to be extended, single obj. can be appended
    sect_list = []
    sect_list.extend(bodies)
    sect_list.append(sim)
    sect_list.append(const)
    sect_list.extend(mat)
    sect_list.extend(solver_list)
    sect_list.append(eqs)
    sect_list.extend(boundaries)
    sect_list.extend(bfs)

    # create SolverInputFile obj.
    sif = SolverInputFile(sections=sect_list)

    # save the sif file
    with open(sif_file, "wt") as f:
        sif.write(f)
