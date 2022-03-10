from os import replace
from numpy import pi
from ...Classes.Arc import Arc
import sys
import gmsh
from os.path import splitext


def gen_3D_mesh(
    lamination,
    save_path="Lamination.msh",
    sym=-1,
    mesh_size=5e-3,
    user_mesh_dict=None,
    is_rect=False,
    Nlayer=20,
    display=True,
):
    """Draw 3D mesh of the lamination
    Parameters
    ----------
    lamination: LamSlot
        Lamintation with slot to draw
    save_path: str
        Path to save the msh result file
    sym : int
        Number of symmetry to apply
    mesh_size : float
        Size of the mesh [m]
    user_mesh_dict : dict
        To enforce the number of elements on the lines
    is_rect : bool
        To use rectangular elements
    Nlayer : int
        Number of mesh layer on Z axis
    display : bool
        To display gmsh logs
    Returns
    -------
    None
    """
    # The defaut symmetry is Zs => We draw only one tooth
    if sym == -1:
        tooth_surf = lamination.slot.get_surface_tooth()
        Zs = lamination.get_Zs()
    else:
        tooth_surf = lamination.build_geometry(sym=sym)[0]
        Zs = sym

    # For readibility
    model = gmsh.model
    factory = model.geo
    L = lamination.L1  # Lamination length

    # Start a new model
    gmsh.initialize()

    gmsh.option.setNumber("General.Terminal", int(display))

    gmsh.option.setNumber("Geometry.CopyMeshingMethod", 1)
    model.add("Pyleecan")

    # Create all the points of the tooth
    NPoint = 0  # Number of point created
    for line in tooth_surf.get_lines():
        Z = line.get_begin()
        NPoint += 1
        factory.addPoint(Z.real, Z.imag, -L / 2, mesh_size, NPoint)

    # Draw all the lines of the tooth
    NLine = 0  # Number of line created
    for line in tooth_surf.get_lines():
        NLine += 1
        if NLine == len(tooth_surf.get_lines()):
            if isinstance(line, Arc):
                Zc = line.get_center()
                NPoint += 1
                factory.addPoint(Zc.real, Zc.imag, -L / 2, mesh_size, NPoint)
                factory.addCircleArc(NLine, NPoint - 1, 1, NLine)
            else:
                factory.addLine(NLine, 1, NLine)
        else:
            if isinstance(line, Arc):
                Zc = line.get_center()
                NPoint += 1
                factory.addPoint(Zc.real, Zc.imag, -L / 2, mesh_size, NPoint)
                factory.addCircleArc(NLine, NPoint, NLine + 1, NLine)
            else:
                factory.addLine(NLine, NLine + 1, NLine)

    # Create the Tooth surface
    gmsh.model.geo.addCurveLoop(list(range(1, NLine + 1)), 1)
    gmsh.model.geo.addPlaneSurface([1], 1)
    gmsh.model.addPhysicalGroup(2, [1], 1)
    gmsh.model.setPhysicalName(2, 1, "Tooth")

    # convert triangle mesh to rectangle mesh
    if is_rect:
        factory.mesh.setRecombine(2, 1)

    # Change the mesh size for each line
    if user_mesh_dict is not None:
        # Compute basic mesh_dict
        mesh_dict = tooth_surf.comp_mesh_dict(element_size=mesh_size)
        # Overwrite basic mesh dict with user one
        mesh_dict.update(user_mesh_dict)
        # Apply the number of element on each line of the surface
        for ii, line in enumerate(tooth_surf.get_lines()):
            factory.mesh.setTransfiniteCurve(
                ii + 1, mesh_dict[str(ii)] + 1, "Progression"
            )

    # Copy/Rotate all the tooth to get the 2D lamination
    surf_list = [1]
    for ii in range(Zs):
        ov = factory.copy([(2, 1)])
        factory.rotate(ov, 0, 0, -L / 2, 0, 0, 1, (ii + 1) * 2 * pi / Zs)
        surf_list.append(ov[0][1])
    gmsh.model.addPhysicalGroup(2, surf_list, 2)
    gmsh.model.setPhysicalName(2, 2, "Lamination")

    # Extrude the lamination
    for surf in surf_list:
        if is_rect == True:
            ov = factory.extrude(
                [(2, surf)], 0, 0, L, numElements=[Nlayer], recombine=True
            )
        else:
            ov = factory.extrude(
                [(2, surf)], 0, 0, L, numElements=[Nlayer], recombine=False
            )
    model.addPhysicalGroup(3, list(range(1, Zs + 1)), 1)
    if lamination.is_stator:
        model.setPhysicalName(3, 1, "stator")
    else:
        model.setPhysicalName(3, 1, "rotor")

    # Generate the 3D mesh
    factory.synchronize()

    filename, file_extension = splitext(save_path)
    if file_extension == ".geo":
        gmsh.write(filename + ".geo_unrolled")
        replace(filename + ".geo_unrolled", filename + file_extension)
    else:
        gmsh.model.mesh.generate(3)
        gmsh.write(save_path)

    # Save and close

    gmsh.finalize()
