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

    alpha1 = a10 + a12*mu*M**2 + a14*mu*M**4
    alpha2 = a20 + a22*mu*M**2 + a24*mu*M**4

    return alpha1, alpha2


def comp_magnetrosctrictive_tensor(mu,M):
    """compute magnetostrictive tensor according to IEEETranMagn2004"""
    alpha1, alpha2 = comp_alpha_coeffs(mu,M)

    return -alpha1*mu*np.dot(M,np.transpose(M))-alpha2*mu*np.linalg.norm(M)**2*np.eye(2)


def comp_force_nodal(self, output):
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

    mesh = meshsolution.get_mesh(0)
    B_sol = meshsolution_mag.get_solution(label="B")
    H_sol = meshsolution_mag.get_solution(label="H")
    mu_sol = meshsolution_mag.get_solution(label="\mu")

    #On récupère les champs de dimension Nelem * Nt_tot * 2 (x,y)
    B = B_sol.get_field()
    H = H_sol.get_field()

    # Bidouille pour produit matriciel plus clair
    axis = B_sol.get_axis()
    pos_indice = list(axis.keys()).index("indice")
    B = np.moveaxis(B, pos_indice, 0)
    H = np.moveaxis(H, pos_indice, 0)

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
        f = np.zeros((Nt_tot, nb_pt), dtype=np.float)
       

        # ref_cell = mesh.cell[key].interpolation.ref_cell // pas besoin d'interpoler car tout est cst 

        # Gauss points
        # pts_gauss, poidsGauss, nb_gauss = mesh.cell[
        #     key
        # ].interpolation.gauss_point.get_gauss_points()

        indice_elem = mesh.cell[key].indice

        for ie in range(nb_elem): # boucle sur les éléments e, plutot enumerate(indice_elem)
            e_ind = indice_elem[ie]
            point_indices = connect[ie, :]
            vertice = mesh.get_vertice(e_ind)[key]

            Be = np.transpose(B[ie, :])
            He = np.transpose(H[ie, :])
            mue = Mu[ie]

            Me = Be/mue - He 

            tme = comp_magnetrosctrictive_tensor(mue,Me)


            

            # Loop on edges
            for n in range(nb_pt_per_cell): # nb_pt : nbre de point par éléments, on peut rajouter un nbre_edge_per_cell

                inode = point_indices[n%nb_pt_per_cell] #faut en récup 2 nous, le suivant par ordre croissant par définition (01 12 20 pour triangle)
                next_inode = point_indices[(n+1)%nb_pt_per_cell]

                edge_indices = next_inode - inode # coordonées du vecteur nn+1
                
                # Volume ratio (Green Ostro), with a conventional 1/2
                L = np.linalg.norm(edge_indices)
                Ve0 = L/2 

                normal_to_edge = (edge_indices[1],-edge_indices[0])/L # normalized normal vector n

                edge_force = np.dot(normal_to_edge,tme)

            
                fe = Ve0 * edge_force
                f[:, inode] = f[:, inode] + fe
                f[:, next_inode] = f[:, next_inode] + fe
                

              

    indices_points = np.sort(np.unique(connect))
    Indices_Point = Data1D(name="indice", values=indices_points, is_components=True)
    Time = B_sol.field.components["x"].axes[0]
    components = {}
    if not np.all((fx == 0)):
        fx_data = DataTime(
            name="Nodal force (x)",
            unit="N",
            symbol="Fx",
            axes=[Time, Indices_Point],
            values=fx,
        )
        components["x"] = fx_data
    if not np.all((fy == 0)):
        fy_data = DataTime(
            name="Nodal force (y)",
            unit="N",
            symbol="Fy",
            axes=[Time, Indices_Point],
            values=fy,
        )
        components["y"] = fy_data

    vec_force = VectorField(name="Nodal forces", symbol="F", components=components)
    solforce = SolutionVector(field=vec_force, type_cell="point", label="F")
    meshsolution.solution.append(solforce)

    output.force.vwp_nodal = meshsolution
    pass
