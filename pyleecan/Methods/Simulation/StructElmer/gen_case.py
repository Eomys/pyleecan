# -*- coding: utf-8 -*-

from os.path import join, split

from ....Classes.Section import Section
from ....Classes.SolverInputFile import SolverInputFile
from ....Methods.Elmer.Section import File


# temp shortcut
names = [
    "Magnet_0_Body",
    "Lamination_0_Body",
    "Magnet_1_Body",
    "Magnet_0_Right_Slave",
    "Magnet_0_Bottom_Slave",
    "Magnet_0_Left_Slave",
    "Magnet_0_Top_Slave",
    "Magnet_1_Left_Slave",
    "Magnet_1_Bottom_Slave",
    "Magnet_1_Right_Slave",
    "Magnet_0_Right_Master",
    "Magnet_0_Bottom_Master",
    "Magnet_0_Left_Master",
    "Magnet_0_Top_Master",
    "Magnet_1_Left_Master",
    "Magnet_1_Bottom_Master",
    "Magnet_1_Right_Master",
    "Magnet_1_Top_Master",
    "Magnet_1_Top_Slave",
    "MASTER_ROTOR_BOUNDARY",
    "SLAVE_ROTOR_BOUNDARY",
]


def gen_case(self, output):
    """Setup the Elmer Case file (.sif file)"""

    # get the save path
    save_dir = self.get_path_save_fea(output)

    sif_file = join(save_dir, "case.sif")

    # save solver start info
    start_file = join(save_dir, "ELMERSOLVER_STARTINFO")

    with open(start_file, "wt") as fout:
        fout.write(split(sif_file)[1])

    # --- prepare sections ---
    # bodies
    bodies = []
    for name in names:
        if "Body" in name:
            body = Section(section="Body", id=len(bodies) + 1)
            body["name"] = name
            body["Equation"] = 1
            if "Magnet" in name:
                body["Material"] = 2
            elif "Lamination" in name:
                body["Material"] = 2
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
    const = Section(section="Constant")
    const["Gravity"] = [0.0, -1.0, 0.0, 9.82]

    # equations
    eqs = Section(section="Equations")
    eqs["Name"] = "Equations"
    eqs["Active Solvers"] = [1, 2, 3, 4, 5]

    # list of section
    sect_list = []
    sect_list.extend(bodies)
    sect_list.append(sim)
    sect_list.append(const)
    sect_list.append(eqs)

    # create SolverInputFile obj.
    sif = SolverInputFile(sections=sect_list)

    # save the sif file
    with open(sif_file, "wt") as f:
        sif.write(f)
