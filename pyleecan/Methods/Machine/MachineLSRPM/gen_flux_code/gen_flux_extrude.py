# -*- coding: utf-8 -*-
"""@package Functions.gen_flux_code.gen_flux_extrude
Generate the code needed to extrude the end of the Face
@date Created on Thu Mar 31 10:25:02 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def gen_flux_extrude(code, Z, region_name, color, Lobj, Lmin):
    """Generate the code needed to extrude the Face (create the volume and
    the region)

    Parameters
    ----------
    code :
        Code to expand
    Z :
        Point on the Face to extrude
    region_name :
        Name to give to the created region
    color :
        Color of the region
    Lobj :
        Tuple (name, value) of the object length
    Lmin :
        Tuple (name, value) of the machine minimum length

    Returns
    -------
    string
        code: New state of the code

    """

    code += "#Extrusion of " + region_name + " center volume\n"
    code += (
        "lastInstance = Extrude(name='Extrude_"
        + region_name
        + "',\n\
        coordSys=CoordSys['XYZ1'],\n\
        color=Color['"
        + color
        + "'],\n\
        faces=[Face.selectByCoordinates(["
        + str(Z.real)
        + ","
        + str(Z.imag)
        + "])],\n\
    extrusionType=AlongVector(coordSys=CoordSys['XYZ1'],\n\
                              vectorDirection=['0','0','1'],\n\
                              distanceType=Distance(firstDistance='"
        + Lmin[0]
        + "',\n\
                                                      secondDistance='-0.5*"
        + Lmin[0]
        + "')),\n\
    visibility=Visibility['VISIBLE'],\n\
    sketch=Sketch['SKETCH_1'])\n"
    )

    if Lobj[1] > Lmin[1]:
        code += "#Extrusion of " + region_name + " top volume\n"
        # Extrude on oZ of L
        code += (
            "lastInstance = Extrude(name='Extrude_"
            + region_name
            + "_1',\n\
            coordSys=CoordSys['XYZ1'],\n\
            color=Color['"
            + color
            + "'],\n\
            faces=[Face.selectByCoordinates(["
            + str(Z.real)
            + ","
            + str(Z.imag)
            + "])],\n\
        extrusionType=AlongVector(coordSys=CoordSys['XYZ1'],\n\
                                  vectorDirection=['0','0','1'],\n\
                                  distanceType=Distance(firstDistance='("
            + Lobj[0]
            + "-"
            + Lmin[0]
            + ")*0.5',\n\
                                                          secondDistance='0.5*"
            + Lmin[0]
            + "')),\n\
        visibility=Visibility['VISIBLE'],\n\
        sketch=Sketch['SKETCH_1'])\n"
        )

        code += "#Extrusion of " + region_name + " bottom volume\n"
        # Extrude on oZ of L
        code += (
            "lastInstance = Extrude(name='Extrude_"
            + region_name
            + "_2',\n\
            coordSys=CoordSys['XYZ1'],\n\
            color=Color['"
            + color
            + "'],\n\
            faces=[Face.selectByCoordinates(["
            + str(Z.real)
            + ","
            + str(Z.imag)
            + "])],\n\
        extrusionType=AlongVector(coordSys=CoordSys['XYZ1'],\n\
                                  vectorDirection=['0','0','1'],\n\
                                  distanceType=Distance(firstDistance='-("
            + Lobj[0]
            + "-"
            + Lmin[0]
            + ")*0.5',\n\
                                                          secondDistance='-0.5*"
            + Lmin[0]
            + "')),\n\
        visibility=Visibility['VISIBLE'],\n\
        sketch=Sketch['SKETCH_1'])\n"
        )

        code += "#Fusion of the 3 Volumes into 1\n"
        code += (
            "lastInstance = BooleanUnion(name='Union_"
            + region_name
            + "',\n\
                     coordSys=CoordSys['XYZ1'],\n\
                     blank=ModelerObject['OBJ_EXTRUDE_"
            + region_name
            + "'],\n\
                     tools=[ModelerObject['OBJ_EXTRUDE_"
            + region_name
            + "_1'],\n\
                            ModelerObject['OBJ_EXTRUDE_"
            + region_name
            + "_2']],\n\
                     color=Color['"
            + color
            + "'],\n\
                     visibility=Visibility['VISIBLE'])\n"
        )

    # Create the RegionVolume and assign it to the last created Volume
    code += (
        "Volume[ALL][-1].region = RegionVolume(name='"
        + region_name
        + "', color=Color['"
        + color
        + "'])\n\n"
    )

    return code
