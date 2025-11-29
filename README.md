# <img alt="Pyleecan" src="https://www.pyleecan.org/_static/favicon.png" height="120">

[![PyPI version](https://badge.fury.io/py/pyleecan.svg)](https://badge.fury.io/py/pyleecan)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

## పరిచయం (Presentation)

**PYLEECAN** ప్రాజెక్ట్ అనేది విద్యుత్ యంత్రాలు మరియు డ్రైవ్‌ల యొక్క బహుళ భౌతిక రూపకల్పన మరియు ఆప్టిమైజేషన్ కోసం **సులభమైన, ఏకీకృత మరియు అనుకూలమైన సిమ్యులేషన్ ఫ్రేమ్‌వర్క్** ను అందిస్తుంది.

**PYLEECAN** యొక్క ప్రధాన లక్ష్యం విద్యుత్ ఇంజనీరింగ్‌లో **పునరుత్పత్తి చేయగల పరిశోధన** మరియు **ఓపెన్-సైన్స్** ను ప్రోత్సహించడం. ఇది విద్యుత్ ఇంజనీరింగ్‌లోని పరిశోధకులు, R&D ఇంజనీర్లు మరియు ఉపాధ్యాయుల కోసం రూపొందించబడింది.

ఉదాహరణకు, పీహెచ్‌డీ విద్యార్థులు **PYLEECAN** తో ప్రారంభించాలి:

- విద్యుత్ ఇంజనీరింగ్ కోసం ఇప్పటికే ఉన్న ఆల్గోరిథమ్‌లను ఉపయోగించడం ద్వారా మీరు చాలా సమయాన్ని ఆదా చేయవచ్చు (ఉదా: Scilab లేదా Matlab ను Femm తో కలపడం).
- మీ పరిశోధన కోసం కమ్యూనిటీ నిపుణుల అనుభవాన్ని పొందవచ్చు.
- మీ కోడ్‌ను నిర్వహించడానికి మరియు ఇతరులు మీ ఫలితాలను సులభంగా పునరుత్పత్తి చేయడానికి ప్రాజెక్ట్‌లో మీరు కూడా సహకరించవచ్చు.

ఈ అన్ని లక్ష్యాలను సాధించడానికి, **PYLEECAN ఓపెన్ సోర్స్** (Apache V2 లైసెన్స్) కింద విడుదల చేయబడింది.

---

## ప్రారంభం (Getting Started)

PYLEECANని ఇన్‌స్టాల్ చేయడం మరియు ఉపయోగించడం కోసం పూర్తి వివరాలు [Pyleecan వెబ్‌సైట్](https://www.pyleecan.org/get.pyleecan.html) లో లభ్యమవుతాయి.

⚠️ గమనిక: PySide2 కారణంగా PYLEECAN ప్రస్తుతం Python 3.11 తో అనుకూలంగా లేదు. భవిష్యత్తులో 3.11 కి నవీకరించాలనే ప్రణాళిక ఉంది.

---

## ప్రాజెక్ట్ మూలం మరియు ప్రస్తుత స్థితి (Origin and Current Status)

**[EOMYS ENGINEERING](https://eomys.com/?lang=en)** ఈ ఓపెన్-సోర్స్ ప్రాజెక్ట్‌ను 2018లో విద్యుత్ మోటార్ల అధ్యయనాల కోసం ప్రారంభించింది. ప్రస్తుతం ఈ ప్రాజెక్ట్ **[Green Forge Coop](https://www.linkedin.com/company/greenforgecoop/)** అనే లాభాపేక్షలేని సంస్థ మద్దతుతో కొనసాగుతోంది. ఇది **[Mosqito](https://github.com/Eomys/MoSQITo)** (ధ్వని నాణ్యత కోసం) మరియు **[SciDataTool](https://github.com/Eomys/SciDataTool)** (శాస్త్రీయ డేటా విశ్లేషణ కోసం) అభివృద్ధికి కూడా మద్దతు ఇస్తుంది.

---

## ప్రధాన నమూనాలు మరియు కలయికలు (Main Models and Couplings)

- **PYLEECAN** ను **[FEMM](http://www.femm.info)** తో పూర్తిగా అనుసంధానించబడింది, nonlinear magnetostatic విశ్లేషణ కోసం (Windows లో మాత్రమే అందుబాటులో ఉంది).
- అనేక నష్టం నమూనాలు (FEMM అవుట్‌పుట్ ఆధారంగా) ఉన్నాయి.
- PMSM మరియు SCIM యంత్రాల equivalent circuit పరిష్కరించడానికి విద్యుత్ నమూనా కలదు.
- **[GMSH](http://gmsh.info/)** తో అనుసంధానించబడి 2D/3D ఫైనైట్ ఎలిమెంట్ మెష్ జనరేషన్‌కి మద్దతు ఇస్తుంది.
- బహుళ లక్ష్య ఆప్టిమైజేషన్ లైబ్రరీలతో అనుసంధానం.
- **Parameter Sweep** ను వేరువేరు వేగాల సిమ్యులేషన్లకు ఉపయోగించవచ్చు.

---

## ప్రధాన టోపాలజీ లక్షణాలు (Main Topologies Features)

- **GUI** ద్వారా ప్రధాన 2D రేడియల్ ఫ్లక్స్ టోపాలజీలు (**SPMSM, IPMSM, SCIM, DFIM, WRSM, SRM, SynRM**) నిర్వచించవచ్చు.
- DXF ఫైళ్ల నుండి స్లాట్ లేదా హోల్ దిగుమతి చేసుకోవచ్చు.
- **Star of Slot Winding** ([swat-em](https://swat-em.readthedocs.io/en/latest/)) లేదా యూజర్ నిర్వచించిన winding మద్దతు.
- సంక్లిష్ట యంత్రాల generic geometry మోడలర్.
- Notches, Uneven Bore లేదా Yoke ఆకారం, రెండు కంటే ఎక్కువ laminations ఉన్న యంత్రాలకు మద్దతు.

ఉదాహరణలను [గ్యాలరీ](https://pyleecan.org/gallery.html) లో చూడవచ్చు.

---

## సహకారం (Contributing)

మీకు ఏదైనా టోపాలజీ లేదా నిర్దిష్ట మోడల్‌లో ఆసక్తి ఉంటే, దానిపై చర్చించడానికి **[issue](https://github.com/Eomys/pyleecan/issues)** లేదా **[discussion](https://github.com/Eomys/pyleecan/discussions)** ప్రారంభించండి.  
మేము దానిని ఎలా అభివృద్ధి చేయాలో వివరించవచ్చు లేదా అభివృద్ధి జాబితాలో చేర్చవచ్చు.  
ప్రయోగాత్మక డేటా మరియు తాజా శాస్త్రీయ పరిశోధన ఆధారిత మోడల్ ధృవీకరణకు మేము ఎల్లప్పుడూ ఎదురుచూస్తున్నాము.

---

## రోడ్‌మ్యాప్ (Roadmap)

ప్రాజెక్ట్ యొక్క మధ్య/దీర్ఘకాల ప్రణాళిక [ఇక్కడ](https://github.com/Eomys/pyleecan/issues/214) అందుబాటులో ఉంది.

---

## డాక్యుమెంటేషన్ / వెబ్‌సైట్ (Documentation / Website)

ప్రాజెక్ట్‌కు సంబంధించిన అన్ని సమాచారం [www.pyleecan.org](http://www.pyleecan.org) లో అందుబాటులో ఉంది.  
**[మీడియా పేజీ](https://pyleecan.org/media.html)** లో ప్రచురణలు, వీడియోలు మరియు స్క్రీన్‌షాట్లు లభిస్తాయి.

---

## సంప్రదించండి (Contact)

మమ్మల్ని సంప్రదించండి:
* **[GitHub Issues](https://github.com/Eomys/pyleecan/issues)** ద్వారా (కొత్త ఫీచర్, ప్రశ్న, లేదా బగ్ నివేదన)
* **ఇమెయిల్**: pyleecan(at)framalistes.org

మమ్మల్ని అనుసరించండి:
* **[న్యూస్‌లెటర్](https://pyleecan.org/)**
* **[GFC YouTube ఛానల్](https://www.youtube.com/channel/UCfp83IQbz9znqsU28keMjZw)** (వెబినార్‌లు, ట్యుటోరియల్ వీడియోలతో)
* **[GFC LinkedIn పేజీ](https://www.linkedin.com/company/greenforgecoop/)**

---

