import numpy as np
from SciDataTool import DataTime, VectorField, Data1D

from pyleecan.Classes.Interpolation import Interpolation
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.SolutionVector import SolutionVector



def comp_alpha_coeffs(mu,M):
    """compute alpha1 and alpha2 for magnetostrictive tensor according to IEEETranMagn2004"""
    a10 = 0.719
    a12 = -0.078
    a14 = -0.042
    a20 = -0.391
    a22 = 0.114
    a24 = 0.004

    M_norm = np.linalg.norm(M,axis=(0,1))
    mu_times_Mnorm_squared = np.multiply(mu,M_norm)**2

    alpha1 = a10 + a12*mu_times_Mnorm_squared + a14*mu*mu_times_Mnorm_squared**2
    alpha2 = a20 + a22*mu_times_Mnorm_squared + a24*mu*mu_times_Mnorm_squared**2

    return alpha1, alpha2


def comp_magnetrosctrictive_tensor(mu,M,Nt_tot):
    """compute magnetostrictive tensor according to IEEETranMagn2004"""
    alpha1, alpha2 = comp_alpha_coeffs(mu,M)

    magnetostric_tensor = np.zeros((2,2,Nt_tot))

    for ti in range(Nt_tot):
        mu_ti = mu[ti]

        M_times_M = np.dot(M[:,:,ti],np.transpose(M[:,:,ti]))

        M_norm_squared = np.linalg.norm(M[:,:,ti])**2
        I = np.eye(2,2)
        
        first_member = -alpha1[ti]*mu_ti*M_times_M
        second_member = -alpha2[ti]*mu_ti*M_norm_squared*I

        magnetostric_tensor[:,:,ti] = first_member + second_member

    return magnetostric_tensor


def comp_force_nodal(self, output, axes_dict):
    """Run the nodal forces calculation based on a tensor.

    from publications:


    Parameters
    ----------
    self : ForceVWP
        A ForceVWP object

    output : Output
        an Output object (to update)

    """
    dim = 2
    Nt_tot = output.mag.Time.get_length()  # Number of time step

    meshsolution_mag = output.mag.meshsolution # tout ce qui sort de FEMM
    mesh_mag = output.mag.meshsolution.mesh
    # nouvel objet maillage car on peut vouloir un maillage différent en sortie
    meshsolution = MeshSolution(
        mesh=mesh_mag, is_same_mesh=True, dimension=meshsolution_mag.dimension
    )
    # entrefer, windings, stator, ...
    meshsolution.group = meshsolution_mag.group

    # output.struct.magnetic_mesh.is_same_mesh = meshsolution_mag.is_same_mesh


    #On récupère les champs de dimension Nelem * Nt_tot * 2 (x,y)
    mesh = meshsolution.get_mesh(0)
    B_sol = meshsolution_mag.get_solution(label="B")
    H_sol = meshsolution_mag.get_solution(label="H")
    mu_sol = meshsolution_mag.get_solution(label="\mu")

    


    Time = axes_dict["Time"]

    # Import angular vector from Angle Data object
    if self.is_periodicity_t is not None:
        is_periodicity_t = self.is_periodicity_t

    # Import time vector from Time Data object
    is_periodicity_t, is_antiper_t = Time.get_periodicity()
    time = Time.get_values(
        is_oneperiod=is_periodicity_t,
        is_antiperiod=is_antiper_t and is_periodicity_t,
    )

    # Load magnetic flux B and H, and mu
    resultB = B_sol.field.get_xyz_along(
        "indice",
        "time=axis_data",
        axis_data={"time": time},
    )
    indice = resultB["indice"]
    Bx = resultB["comp_x"]
    By = resultB["comp_y"]
    B = np.stack((Bx, By),axis=2)

    resultH = H_sol.field.get_xyz_along(
        "indice",
        "time=axis_data",
        axis_data={"time": time},
    )
    Hx = resultH["comp_x"]
    Hy = resultH["comp_y"]
    H = np.stack((Hx, Hy),axis=2)

    resultmu = mu_sol.field.get_along(
        "indice",
        "time=axis_data",
        axis_data={"time": time},
    )
    mu = resultmu["\\mu"]

    # Bidouille pour produit matriciel plus clair, on met le temps en 3eme dimension
    B = np.moveaxis(B, 0, -1)
    H = np.moveaxis(H, 0, -1)
    mu = np.moveaxis(mu, 0, -1)

    for key in mesh.cell:  # type d'éléments
        # [nodes_subpart]

        # For every type of element (now only Triangle3, TO BE extended), pour l'instant B et H cst dans élément 
        
        # mesh.cell[key].interpolation = Interpolation()
        # mesh.cell[key].interpolation.init_key(key=key, nb_gauss=1)

        nb_pt_per_cell = mesh.cell[key].nb_pt_per_cell # 3 pour 1,2,3 dans triangle
        connect = mesh.cell[key].get_connectivity() # lien entre indice local et global
        nb_elem = len(connect)

        nb_pt = mesh.point.nb_pt #nb de point totaux, 3*nb_elem - redondances 

        # Nodal forces init
        f = np.zeros((nb_pt,2,Nt_tot), dtype=np.float)
       

        # ref_cell = mesh.cell[key].interpolation.ref_cell // pas besoin d'interpoler car tout est cst 

        # Gauss points
        # pts_gauss, poidsGauss, nb_gauss = mesh.cell[
        #     key
        # ].interpolation.gauss_point.get_gauss_points()

        #indice_elem = mesh.cell[key].indice

        for e_ind,e in enumerate(indice): # boucle sur les éléments e, plutot enumerate(indice_elem)
            point_indices = connect[e_ind, :]
            vertice = mesh.get_vertice(e_ind)[key]

            Be = B[e_ind, :, :]
            He = H[e_ind, :, :]
            mue = mu[e_ind, :]

            Me = np.reshape(Be/mue - He,(dim,1,Nt_tot)) 

            tme = comp_magnetrosctrictive_tensor(mue,Me,Nt_tot)


            

            # Loop on edges
            for n in range(nb_pt_per_cell): # nb_pt : nbre de point par éléments, on peut rajouter un nbre_edge_per_cell

                inode = point_indices[n%nb_pt_per_cell] #faut en récup 2 nous, le suivant par ordre croissant par définition (01 12 20 pour triangle)
                next_inode = point_indices[(n+1)%nb_pt_per_cell]

                edge_vector = vertice[(n+1)%nb_pt_per_cell] - vertice[n%nb_pt_per_cell] # coordonées du vecteur nn+1
                
                # Volume ratio (Green Ostro), with a conventional 1/2
                L = np.linalg.norm(edge_vector)
                Ve0 = L/2 

                normal_to_edge = (edge_vector[1],-edge_vector[0])/L # normalized normal vector n

                edge_force = np.dot(normal_to_edge,np.swapaxes(tme,0,1)) # need to swap bc of np.dot doc, this is equal to np.transpose(np.dot(np.transpose(b),np.transpose(tme)))

            
                fe = Ve0 * edge_force

                f[inode,:,:] = f[inode,:,:] + fe
                f[next_inode,:,:] = f[next_inode,:,:] + fe
                

              

    indices_points = np.sort(np.unique(connect))
    Indices_Point = Data1D(name="indice", values=indices_points, is_components=True)
    Time = B_sol.field.components["x"].axes[0]
    components = {}
    if not np.all((f[:,0,:] == 0)):
        fx_data = DataTime(
            name="Nodal force (x)",
            unit="N",
            symbol="Fx",
            axes=[Time, Indices_Point],
            values=f[:,0,:],
        )
        components["x"] = fx_data
    if not np.all((f[:,1,:] == 0)):
        fy_data = DataTime(
            name="Nodal force (y)",
            unit="N",
            symbol="Fy",
            axes=[Time, Indices_Point],
            values=f[:,1,:],
        )
        components["y"] = fy_data

    vec_force = VectorField(name="Nodal forces", symbol="F", components=components)
    solforce = SolutionVector(field=vec_force, type_cell="point", label="F")
    meshsolution.solution.append(solforce)

    output.force.vwp_nodal = meshsolution
    pass
