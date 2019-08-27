from Classes.MeshTriangle import MeshTriangle
from femm import callfemm
import os
import numpy as np
from pyleecan.Generator import MAIN_DIR
from os.path import join
import meshio
import gmsh

def get_FEMM_mesh(self, is_save_mesh, is_save_FEA, j_t0):
    """Load the mesh data and solution data
    """
    gmsh.initialize()
    #gmsh.option.setNumber('General.Terminal', 1)
    #gmsh.model.add('Test')

    idlab = '1'  # For parallelization

    path_txt = join(MAIN_DIR, "Functions", "FEMM") + '\\'
    path_txt_lua = path_txt.replace('\\', '/')
    path_lua_in = join(path_txt, "get_mesh_data_FEMM.lua")
    path_lua_out = path_txt + "get_mesh_data_FEMM" + idlab + ".lua"


    path_save = join(MAIN_DIR, "Results", self.parent.name, "Femm", "Mesh") + '\\'

    # Create a new LUA script with current paths
    file_lua = open(path_lua_in, 'r')
    text_lua = file_lua.read()
    file_lua.close()
    text_lua = text_lua.replace("my_path_txt", path_txt_lua)
    text_lua = text_lua.replace("my_id_matlab", idlab)

    file_lua_out = open(path_lua_out, 'w')
    file_lua_out.write(text_lua)
    file_lua_out.close()

    # Run the LUA externally using FEMM LUA console and store the data in the
    # temporary text files
    path_lua_out2 = path_lua_out.replace('\\', '/')
    callfemm('dofile(\"' + path_lua_out2 + '\")')

    # Delete the LUA script
    os.remove(path_lua_out)

    # Read the nodes and elements files
    listNd0 = np.loadtxt(path_txt + 'nodes' + idlab + '.txt', delimiter=' ')
    listElem0 = np.loadtxt(path_txt + 'elements' + idlab + '.txt', dtype='i', delimiter=' ')
    NbNd = len(listNd0)
    NbElem = len(listElem0)

    # Node list
    listNd = np.zeros(shape=(NbNd, 3))
    listNd[:, 0] = listNd0[:, 0]
    listNd[:, 1] = listNd0[:, 1]

    # Element list
    # listElem = np.zeros(shape=(NbElem, 3))
    listElem = listElem0[:, 0:3] - 1

    # Delete text files
    os.remove(path_txt + 'nodes' + idlab + '.txt')
    os.remove(path_txt + 'elements' + idlab + '.txt')

    # Read the results file
    results = np.loadtxt(path_txt + 'results' + idlab + '.txt', delimiter=' ')

    # Delete text files
    os.remove(path_txt + 'results' + idlab + '.txt')

    # Create Mesh and Solution dictionaries
    mesh = MeshTriangle()

    mesh.nb_elem = NbElem
    mesh.nb_node = NbNd

    indice_stator = np.transpose(np.where(listElem0[:, 6] == 1))

    # Save data
    if is_save_mesh:

        if not os.path.exists(path_save):
            os.makedirs(path_save)

        mesh.node = listNd
        mesh.element = listElem
        mesh.submeshe = dict()
        mesh.submeshe["stator"] = indice_stator

        # Compute jacobians and derivatives with gmsh API
        cells = {
             "triangle": listElem,
        }

        field_data = {
             "Bx": results[:, 0],
            "By": results[:, 1],
            "Hx": results[:, 2],
            "Hy": results[:, 3],
            "mu": results[:, 4],
        }

        mesh_tmp = meshio.Mesh(listNd, cells, field_data)
        meshio.write(path_save + "femm.msh", mesh_tmp)
        gmsh.open(path_save + "femm.msh")
        gmsh.model.mesh.generate()

        #os.remove(path_save + "femm.msh")

        jacobian_data = gmsh.model.mesh.getJacobians(2, "Gauss1")
        mesh.jacobian = jacobian_data[0]
        mesh.det_jacobian = jacobian_data[1]
        mesh.gauss_point = jacobian_data[2]
        #mesh.jacobian_derivative = gmsh.model.mesh.get
        # # xx = gmsh.model.mesh.getJacobians(2, "Gauss1")
        # # gmsh.model.mesh.getNodes("1")
        #xx = gmsh.model.mesh.getElement(1)

        # Store the data in matrices
        mesh.solution = dict()
        mesh.solution["Bx"] = results[:, 0]
        mesh.solution["By"] = results[:, 1]
        mesh.solution["Hx"] = results[:, 2]
        mesh.solution["Hy"] = results[:, 3]
        mesh.solution["mu"] = results[:, 4]

        gmsh.clear()
        gmsh.finalize()

        if is_save_FEA:
            # saving:
            np.savetxt(path_save + 'Solution_' + str(j_t0) + '.dat', results, header="# Bx By Hx Hy mu")
            np.savetxt(path_save + 'Mesh_nodes' + str(j_t0) + '.dat', listNd)
            np.savetxt(path_save + 'Mesh_elem' + str(j_t0) + '.dat', listElem)

    return mesh
