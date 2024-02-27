import pytest

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal


material_l = list()

# definition a material with curve B(H) into file .mot
other_dict = {
    "[POSCO 30PNX1500F_red_Keddy]": {
        "Type": "Fixed_Solid",
        "Solid Type": "Steel",
        "Thermal Conductivity": "22",
        "Specific Heat": "460",
        "Density": "7600",
        "YieldStress": "220",
        "PoissonsRatio": "0.25",
        "YoungsCoefficient": "165",
        "KcValue": "0.65",
        "ElectricalResistivity": "5.2E-07",
        "TempCoefElectricalResistivity": "0",
        "LaminationThickness": "0.3",
        "KhValue_Steinmetz": "0.02585023541",
        "KhValue_Bertotti": "0.005645721646",
        "KhValue_Bertotti_Maxwell": "0.02019666399",
        "KeddyValue_Steinmetz": "1.376E-06",
        "KexcValue": "0.001553693148",
        "KexcValue_Maxwell": "0",
        "alphaValue_Steinmetz": "1.796674567",
        "alphaValue_Bertotti": "4.030731381",
        "alphaValue_Bertotti_Maxwell": "2",
        "betavalue_Steinmetz": "0.1848999063",
        "BValue[0]": "0",
        "HValue[0]": "0",
        "BValue[1]": "0.015649299",
        "HValue[1]": "5.925085189",
        "BValue[2]": "0.029080305",
        "HValue[2]": "9.92738115",
        "BValue[3]": "0.043126797",
        "HValue[3]": "13.35116772",
        "BValue[4]": "0.057073019",
        "HValue[4]": "16.23462434",
        "BValue[5]": "0.071273982",
        "HValue[5]": "18.75264919",
        "BValue[6]": "0.085804451",
        "HValue[6]": "20.96305685",
        "BValue[7]": "0.100185126",
        "HValue[7]": "22.84875748",
        "BValue[8]": "0.115188039",
        "HValue[8]": "24.57592254",
        "BValue[9]": "0.130234227",
        "HValue[9]": "26.06710231",
        "BValue[10]": "0.145940106",
        "HValue[10]": "27.48519573",
        "BValue[11]": "0.160929839",
        "HValue[11]": "28.63021526",
        "BValue[12]": "0.178770528",
        "HValue[12]": "29.92795254",
        "BValue[13]": "0.196144138",
        "HValue[13]": "31.02679313",
        "BValue[14]": "0.216704791",
        "HValue[14]": "32.25435298",
        "BValue[15]": "0.237265341",
        "HValue[15]": "33.40119058",
        "BValue[16]": "0.259064518",
        "HValue[16]": "34.52875665",
        "BValue[17]": "0.283976051",
        "HValue[17]": "35.78976895",
        "BValue[18]": "0.308993354",
        "HValue[18]": "37.01660156",
        "BValue[19]": "0.337564957",
        "HValue[19]": "38.38778881",
        "BValue[20]": "0.365831493",
        "HValue[20]": "39.70116149",
        "BValue[21]": "0.3972291",
        "HValue[21]": "41.18216007",
        "BValue[22]": "0.428664037",
        "HValue[22]": "42.65043218",
        "BValue[23]": "0.462377258",
        "HValue[23]": "44.24815076",
        "BValue[24]": "0.49673169",
        "HValue[24]": "45.92550075",
        "BValue[25]": "0.533588543",
        "HValue[25]": "47.78029422",
        "BValue[26]": "0.569860298",
        "HValue[26]": "49.62963348",
        "BValue[27]": "0.608061875",
        "HValue[27]": "51.6902323",
        "BValue[28]": "0.64777003",
        "HValue[28]": "53.97299909",
        "BValue[29]": "0.687665108",
        "HValue[29]": "56.40812001",
        "BValue[30]": "0.729589748",
        "HValue[30]": "59.17522025",
        "BValue[31]": "0.770269629",
        "HValue[31]": "62.03358752",
        "BValue[32]": "0.812431406",
        "HValue[32]": "65.28647565",
        "BValue[33]": "0.852757259",
        "HValue[33]": "68.75098695",
        "BValue[34]": "0.892517056",
        "HValue[34]": "72.50384392",
        "BValue[35]": "0.932258704",
        "HValue[35]": "76.67340218",
        "BValue[36]": "0.969666525",
        "HValue[36]": "81.09312666",
        "BValue[37]": "1.007180872",
        "HValue[37]": "86.07863406",
        "BValue[38]": "1.042977945",
        "HValue[38]": "91.58410904",
        "BValue[39]": "1.078470989",
        "HValue[39]": "97.85826338",
        "BValue[40]": "1.112988026",
        "HValue[40]": "105.1021754",
        "BValue[41]": "1.145116004",
        "HValue[41]": "113.2231238",
        "BValue[42]": "1.177215012",
        "HValue[42]": "123.0556017",
        "BValue[43]": "1.207567415",
        "HValue[43]": "134.8341402",
        "BValue[44]": "1.237020847",
        "HValue[44]": "149.4477747",
        "BValue[45]": "1.266803973",
        "HValue[45]": "168.8574738",
        "BValue[46]": "1.295567983",
        "HValue[46]": "194.5576899",
        "BValue[47]": "1.324662734",
        "HValue[47]": "230.840519",
        "BValue[48]": "1.354220358",
        "HValue[48]": "288.7423641",
        "BValue[49]": "1.384555412",
        "HValue[49]": "375.8718418",
        "BValue[50]": "1.411987573",
        "HValue[50]": "500.7698741",
        "BValue[51]": "1.449658962",
        "HValue[51]": "764.4614362",
        "BValue[52]": "1.483970014",
        "HValue[52]": "1132.827564",
        "BValue[53]": "1.518294132",
        "HValue[53]": "1635.421688",
        "BValue[54]": "1.553071063",
        "HValue[54]": "2275.458153",
        "BValue[55]": "1.588169044",
        "HValue[55]": "3047.14823",
        "BValue[56]": "1.623383947",
        "HValue[56]": "3966.367291",
        "BValue[57]": "1.659970704",
        "HValue[57]": "5041.118476",
        "BValue[58]": "1.676279902",
        "HValue[58]": "5587.033536",
        "BValue[59]": "1.702102645",
        "HValue[59]": "6521.448014",
        "BValue[60]": "1.727972742",
        "HValue[60]": "7552.98371",
        "BValue[61]": "1.754369262",
        "HValue[61]": "8716.147565",
        "BValue[62]": "1.783455054",
        "HValue[62]": "10137.14989",
        "BValue[63]": "1.820044258",
        "HValue[63]": "12308.50544",
        "BValue[64]": "1.850570657",
        "HValue[64]": "14430.11864",
        "BValue[65]": "1.882656839",
        "HValue[65]": "17163.91186",
        "BValue[66]": "1.915632633",
        "HValue[66]": "21091.04887",
        "BValue[67]": "1.955163403",
        "HValue[67]": "30061.10788",
    }
}

# result expected with curve B(H)
material_l.append(
    {
        "other_dict": other_dict,
        "material_name": "POSCO 30PNX1500F_red_Keddy",
        "is_isotropic": True,
        "curve_B_H": [
            ["0", "0"],
            ["5.925085189", "0.015649299"],
            ["9.92738115", "0.029080305"],
            ["13.35116772", "0.043126797"],
            ["16.23462434", "0.057073019"],
            ["18.75264919", "0.071273982"],
            ["20.96305685", "0.085804451"],
            ["22.84875748", "0.100185126"],
            ["24.57592254", "0.115188039"],
            ["26.06710231", "0.130234227"],
            ["27.48519573", "0.145940106"],
            ["28.63021526", "0.160929839"],
            ["29.92795254", "0.178770528"],
            ["31.02679313", "0.196144138"],
            ["32.25435298", "0.216704791"],
            ["33.40119058", "0.237265341"],
            ["34.52875665", "0.259064518"],
            ["35.78976895", "0.283976051"],
            ["37.01660156", "0.308993354"],
            ["38.38778881", "0.337564957"],
            ["39.70116149", "0.365831493"],
            ["41.18216007", "0.3972291"],
            ["42.65043218", "0.428664037"],
            ["44.24815076", "0.462377258"],
            ["45.92550075", "0.49673169"],
            ["47.78029422", "0.533588543"],
            ["49.62963348", "0.569860298"],
            ["51.6902323", "0.608061875"],
            ["53.97299909", "0.64777003"],
            ["56.40812001", "0.687665108"],
            ["59.17522025", "0.729589748"],
            ["62.03358752", "0.770269629"],
            ["65.28647565", "0.812431406"],
            ["68.75098695", "0.852757259"],
            ["72.50384392", "0.892517056"],
            ["76.67340218", "0.932258704"],
            ["81.09312666", "0.969666525"],
            ["86.07863406", "1.007180872"],
            ["91.58410904", "1.042977945"],
            ["97.85826338", "1.078470989"],
            ["105.1021754", "1.112988026"],
            ["113.2231238", "1.145116004"],
            ["123.0556017", "1.177215012"],
            ["134.8341402", "1.207567415"],
            ["149.4477747", "1.237020847"],
            ["168.8574738", "1.266803973"],
            ["194.5576899", "1.295567983"],
            ["230.840519", "1.324662734"],
            ["288.7423641", "1.354220358"],
            ["375.8718418", "1.384555412"],
            ["500.7698741", "1.411987573"],
            ["764.4614362", "1.449658962"],
            ["1132.827564", "1.483970014"],
            ["1635.421688", "1.518294132"],
            ["2275.458153", "1.553071063"],
            ["3047.14823", "1.588169044"],
            ["3966.367291", "1.623383947"],
            ["5041.118476", "1.659970704"],
            ["5587.033536", "1.676279902"],
            ["6521.448014", "1.702102645"],
            ["7552.98371", "1.727972742"],
            ["8716.147565", "1.754369262"],
            ["10137.14989", "1.783455054"],
            ["12308.50544", "1.820044258"],
            ["14430.11864", "1.850570657"],
            ["17163.91186", "1.882656839"],
            ["21091.04887", "1.915632633"],
            ["30061.10788", "1.955163403"],
        ],
    }
)

# definition a material with not curve B(H) into file .mot
other_dict = {
    "[POSCO 30PNX1500F_red_Keddy]": {
        "Type": "Fixed_Solid",
        "Solid Type": "Steel",
        "Thermal Conductivity": "22",
        "Specific Heat": "460",
        "Density": "7600",
        "YieldStress": "220",
        "PoissonsRatio": "0.25",
        "YoungsCoefficient": "165",
        "KcValue": "0.65",
        "ElectricalResistivity": "5.2E-07",
        "TempCoefElectricalResistivity": "0",
        "LaminationThickness": "0.3",
        "KhValue_Steinmetz": "0.02585023541",
        "KhValue_Bertotti": "0.005645721646",
        "KhValue_Bertotti_Maxwell": "0.02019666399",
        "KeddyValue_Steinmetz": "1.376E-06",
        "KexcValue": "0.001553693148",
        "KexcValue_Maxwell": "0",
        "alphaValue_Steinmetz": "1.796674567",
        "alphaValue_Bertotti": "4.030731381",
        "alphaValue_Bertotti_Maxwell": "2",
        "betavalue_Steinmetz": "0.1848999063",
    }
}

# result expected if haven't curve B(H)
material_l.append(
    {
        "other_dict": other_dict,
        "material_name": "POSCO 30PNX1500F_red_Keddy",
        "is_isotropic": True,
        "curve_B_H": None,
    }
)


class TestComplexRulecurve_B_H(object):
    @pytest.mark.parametrize("test_dict", material_l)
    def test_curve_B_H(self, test_dict):
        """test rule complex"""

        # retreive other_dict
        other_dict = test_dict["other_dict"]

        # Construct the machine in which the slot will be set
        machine = MachineSIPMSM()

        # selection material and path in dict .mot
        param_dict = {
            "material": "POSCO 30PNX1500F_red_Keddy",
            "path_P": "machine.stator.mat_type",
        }

        # Define and apply the slot rule
        rule = RuleComplex(
            fct_name="curve_B(H)", folder="MotorCAD", param_dict=param_dict
        )
        # first rule complex use to define a slot
        machine = rule.convert_to_P(other_dict, machine, {"m": 1})

        # retreive expected values
        material_name = test_dict["material_name"]
        is_isotropic = test_dict["is_isotropic"]
        curve_B_H = test_dict["curve_B_H"]

        # check the convertion
        msg = f"{machine.stator.mat_type.name} expected {material_name}"
        assert machine.stator.mat_type.name == pytest.approx(material_name), msg

        msg = f"{machine.stator.mat_type.is_isotropic} expected {is_isotropic}"
        assert machine.stator.mat_type.is_isotropic == pytest.approx(is_isotropic), msg

        # check for curve B(H)
        tab_curve_expected = curve_B_H

        # if file_mot haven't curve B(H), class of mag isn't change and value doesn't exist
        if curve_B_H == None:
            if isinstance(machine.stator.mat_type.mag.BH_curve, ImportMatrixVal):
                raise Exception("BH_curve.value should not be defined")
            try:
                tab_curve = machine.stator.mat_type.mag.BH_curve.value
                raise Exception("BH_curve.value should not be defined")
            except:
                pass

        else:
            msg = f"{machine.stator.mat_type.mag.BH_curve.__class__.__name__} exepected {ImportMatrixVal}"
            assert (
                machine.stator.mat_type.mag.BH_curve.__class__ == ImportMatrixVal
            ), msg

            # if a curve is set into materail, check if all element are equivalent
            tab_curve = machine.stator.mat_type.mag.BH_curve.value
            for nb_ele, ele in enumerate(tab_curve):
                msg = f"{ele[0]} exepected {tab_curve_expected[nb_ele][0]}"
                assert ele[0] == tab_curve_expected[nb_ele][0], msg
                msg = f"{ele[1]} exepected {tab_curve_expected[nb_ele][1]}"
                assert ele[1] == tab_curve_expected[nb_ele][1], msg


if __name__ == "__main__":
    a = TestComplexRulecurve_B_H()
    for test_dict in material_l:
        a.test_curve_B_H(test_dict)
    print("Test Done")
