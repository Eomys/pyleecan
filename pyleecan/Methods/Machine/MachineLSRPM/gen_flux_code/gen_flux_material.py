# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Apr 07 11:52:05 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo Winding and Magnet Material
"""


def gen_flux_material(code, mat_list=[]):
    """Create All the Material for flux

    Parameters
    ----------
    code :
        Code to expand
    mat_list :
        Material list to add to the default one (no duplicate)

    Returns
    -------
    string
        code: New state of the code

    """

    # Default material for Magnet and Winding
    code += "#Default Magnet Material\n"
    code += "lastInstance = Material(name='Magnet_Mat',\n\
             propertyBH=PropertyBhMagnetCylindrical(br=['1.1','0','0'],\n\
                                                    mur='1.05'))\n\n"
    code += "#Flux Copper for winding\n"
    code += (
        "lastInstance = Material(name='FLU_COPPER', "
        "propertyJE=PropertyJeTLinearFunction(slope='0.00427', "
        "rhoConstant='1.564E-8', referenceTemperature=Temperature("
        "temperature='0.0'), temperature=Temperature("
        "temperature='20.0')), specificHeat=RhoCpConstant("
        "rhoCp='3518000.0'), propertyBH=PropertyBhLinear(mur='1.0'), "
        "thermalConductivity=KtIsotropic(k='394.0'))\n\n"
    )

    for mat in mat_list:
        # Adding From B(H) curve
        if (
            type(mat).__name__ == "MatLamination"
            and type(mat.BH_curve).__name__ != "BHCurve"
        ):  # The curve is set
            code += "#" + mat.name + " for Iron (Lamination)\n"
            code += (
                "Material(name='"
                + mat.name
                + "', propertyBH="
                + mat.BH_curve.export_flux()
                + ")\n\n"
            )
        # Flux import
        elif mat.name in ["FLU_M400_50A", "M400_50A"]:
            code += "#Flux M400_50A for Iron (Lamination)\n"
            code += (
                "Material(name='"
                + mat.name
                + "', propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0, b=0.0), BHPoint(h=28.98351, b=0.100188), BHPoint(h=40.29485, b=0.199875), BHPoint(h=46.62721, b=0.299829), BHPoint(h=52.22972, b=0.399271), BHPoint(h=58.56646, b=0.499299), BHPoint(h=66.01757, b=0.600456), BHPoint(h=74.89961, b=0.699733), BHPoint(h=85.0121, b=0.798468), BHPoint(h=99.45005, b=0.899148), BHPoint(h=121.0487, b=0.99903), BHPoint(h=153.7771, b=1.099347), BHPoint(h=211.8938, b=1.199984), BHPoint(h=343.7375, b=1.297546), BHPoint(h=754.7981, b=1.396596), BHPoint(h=2061.964, b=1.499972), BHPoint(h=4484.748, b=1.598976), BHPoint(h=7899.275, b=1.696744), BHPoint(h=8779.022, b=1.717938), BHPoint(h=10000.0, b=1.746), BHPoint(h=20000.0, b=1.883), BHPoint(h=30000.0, b=1.947), BHPoint(h=50000.0, b=2.018), BHPoint(h=100000.0, b=2.117), BHPoint(h=200000.0, b=2.262), BHPoint(h=300000.0, b=2.394)], equivalentHarmonicCurve=EquivalentBhUnmodified()))\n\n"
            )

        elif mat.name in ["FLU_M330_35A", "M330_35A"]:
            code += "#Flux M330_35A for Iron (Lamination)\n"
            code += (
                "Material(name='"
                + mat.name
                + "', propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0, b=0.0), BHPoint(h=36.64, b=0.1), BHPoint(h=47.53, b=0.2), BHPoint(h=55.58, b=0.3), BHPoint(h=62.71, b=0.4), BHPoint(h=69.08, b=0.5), BHPoint(h=76.17, b=0.6), BHPoint(h=83.94, b=0.7), BHPoint(h=93.95, b=0.8), BHPoint(h=107.46, b=0.9), BHPoint(h=126.31, b=0.998), BHPoint(h=156.25, b=1.099), BHPoint(h=211.23, b=1.198), BHPoint(h=331.96, b=1.299), BHPoint(h=680.89, b=1.397), BHPoint(h=1812.22, b=1.498), BHPoint(h=4107.99, b=1.598), BHPoint(h=7465.22, b=1.697), BHPoint(h=8375.76, b=1.719), BHPoint(h=10000.0, b=1.754), BHPoint(h=20000.0, b=1.885), BHPoint(h=30000.0, b=1.949), BHPoint(h=50000.0, b=2.019), BHPoint(h=100000.0, b=2.118), BHPoint(h=200000.0, b=2.262), BHPoint(h=300000.0, b=2.394)], equivalentHarmonicCurve=EquivalentBhUnmodified()))\n\n"
            )

        elif mat.name in ["FLU_M270_35A", "M270_35A"]:
            code += "#Flux M270_35A for Iron (Lamination)\n"
            code += (
                "Material(name='"
                + mat.name
                + "', propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0, b=0.0), BHPoint(h=29.38, b=0.1), BHPoint(h=37.39, b=0.2), BHPoint(h=45.24, b=0.3), BHPoint(h=50.18, b=0.4), BHPoint(h=55.45, b=0.5), BHPoint(h=62.07, b=0.6), BHPoint(h=70.32, b=0.7), BHPoint(h=81.92, b=0.8), BHPoint(h=96.58, b=0.9), BHPoint(h=118.68, b=1.0), BHPoint(h=155.51, b=1.1), BHPoint(h=226.67, b=1.2), BHPoint(h=416.07, b=1.3), BHPoint(h=1059.27, b=1.4), BHPoint(h=2756.65, b=1.5), BHPoint(h=5441.9, b=1.59), BHPoint(h=7069.65, b=1.64), BHPoint(h=8213.34, b=1.67), BHPoint(h=10000.0, b=1.723), BHPoint(h=20000.0, b=1.859), BHPoint(h=30000.0, b=1.922), BHPoint(h=50000.0, b=1.991), BHPoint(h=100000.0, b=2.089), BHPoint(h=200000.0, b=2.233), BHPoint(h=300000.0, b=2.365)], equivalentHarmonicCurve=EquivalentBhUnmodified()))\n\n"
            )

        elif mat.name in ["FLU_M600_65A", "M600_65A"]:
            code += "#Flux M600_65A for Iron (Lamination)\n"
            code += (
                "Material(name='"
                + mat.name
                + "', propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0, b=0.0), BHPoint(h=48.82523, b=0.099985), BHPoint(h=57.6865, b=0.199768), BHPoint(h=65.76662, b=0.299425), BHPoint(h=72.55672, b=0.399957), BHPoint(h=81.73358, b=0.499079), BHPoint(h=91.5352, b=0.599273), BHPoint(h=101.2865, b=0.699121), BHPoint(h=113.9602, b=0.799615), BHPoint(h=128.3954, b=0.898526), BHPoint(h=147.8156, b=0.999751), BHPoint(h=179.3674, b=1.100534), BHPoint(h=229.8152, b=1.198895), BHPoint(h=324.225, b=1.299151), BHPoint(h=544.184, b=1.399598), BHPoint(h=1118.169, b=1.499568), BHPoint(h=2472.983, b=1.599411), BHPoint(h=4990.856, b=1.696836), BHPoint(h=9201.883, b=1.800448), BHPoint(h=10000.0, b=1.818), BHPoint(h=20000.0, b=1.956), BHPoint(h=30000.0, b=2.02), BHPoint(h=50000.0, b=2.09), BHPoint(h=100000.0, b=2.188), BHPoint(h=200000.0, b=2.332), BHPoint(h=300000.0, b=2.464)], equivalentHarmonicCurve=EquivalentBhUnmodified()))\n\n"
            )

        elif mat.name in ["FLU_M800_65A", "M800_65A"]:
            code += "#Flux M800_65A for Iron (Lamination)\n"
            code += (
                "Material(name='"
                + mat.name
                + "', propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0, b=0.0), BHPoint(h=61.25108, b=0.099965), BHPoint(h=79.0855, b=0.199719), BHPoint(h=90.52255, b=0.299294), BHPoint(h=101.2513, b=0.399654), BHPoint(h=111.8278, b=0.499029), BHPoint(h=121.7675, b=0.599419), BHPoint(h=132.1524, b=0.69946), BHPoint(h=141.409, b=0.798561), BHPoint(h=153.3806, b=0.898264), BHPoint(h=169.2126, b=0.998844), BHPoint(h=196.132, b=1.098922), BHPoint(h=238.8507, b=1.199442), BHPoint(h=314.9601, b=1.299146), BHPoint(h=470.928, b=1.399786), BHPoint(h=854.721, b=1.496587), BHPoint(h=1879.024, b=1.597992), BHPoint(h=4071.388, b=1.696593), BHPoint(h=5755.238, b=1.746644), BHPoint(h=7784.65, b=1.795649), BHPoint(h=9024.47, b=1.821708), BHPoint(h=10000.0, b=1.842), BHPoint(h=20000.0, b=1.976), BHPoint(h=30000.0, b=2.042), BHPoint(h=50000.0, b=2.114), BHPoint(h=100000.0, b=2.215), BHPoint(h=200000.0, b=2.361), BHPoint(h=300000.0, b=2.493)], equivalentHarmonicCurve=EquivalentBhUnmodified()))\n\n"
            )

    return code
