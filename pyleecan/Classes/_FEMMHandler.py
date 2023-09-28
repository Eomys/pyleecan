import os
from math import exp
import re
from os.path import expanduser
import time

global is_windows_os

try:
    import pythoncom
    import win32com.client

    is_windows_os = True
except:
    print("No activex, using file I/O")
    is_windows_os = False

from six import string_types

sleeptime = 0.01


class _FEMMHandler(object):
    """
    Object to handle FEMM
    enable to start FEMM and run commands in it
    """

    def __init__(self, HandleToFEMM=None, init_dict=None):
        object.__init__(self)
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "HandleToFEMM" in list(init_dict.keys()):
                HandleToFEMM = init_dict["HandleToFEMM"]
        self.HandleToFEMM = HandleToFEMM
        if is_windows_os:
            pythoncom.CoInitialize()

    def as_dict(self, **kwargs):
        _FEMMHandler_dict = dict()
        _FEMMHandler_dict["__class__"] = "_FEMMHandler"
        _FEMMHandler_dict["HandleToFEMM"] = None
        return _FEMMHandler_dict

    def copy(self):
        return _FEMMHandler(HandleToFEMM=None)

    def compare(self, other, ignore_list=list(), name="self", is_add_value=False):
        """Compare two objects and return list of differences"""
        return list()

    def fixpath(self, myPath):
        return myPath.replace("\\", "/").replace("//", "/")

    def openfemm_Windows(self, *arg):
        if self.HandleToFEMM != None:
            raise Exception("An instance FEMM is already open")

        self.HandleToFEMM = win32com.client.Dispatch("femm.ActiveFEMM")

        # Call femm
        self.callfemm(
            "setcurrentdirectory(" + self.quote(self.fixpath(os.getcwd())) + ")"
        )
        if len(arg) == 0:
            self.main_restore()
            return
        if arg[0] == 0:
            self.main_restore()
            return

    def openfemm_Linux(self, *arg, winepath="", femmpath=""):
        # Opens FEMM, path to wine and FEMM directories can be given as openfemm(winepath='path/to/wine/',femmpath='path/to/femm/')."""
        global ifile, ofile

        if self.HandleToFEMM != None:
            raise Exception("An instance FEMM is already open")

        # find wine path
        if winepath != "":
            if os.path.isdir(winepath):
                winedir = winepath
            elif os.path.isfile(winepath):
                winedir = re.sub("wine$", "", winepath)
            else:
                raise Exception(
                    "Given path for wine does not exist. Please check 'winepath'."
                )
        else:
            # check all environment paths for wine
            envpath = os.getenv("PATH").split(":")
            # add good guesses
            envpath.extend(
                [
                    "/usr/bin",
                    "/usr/local/bin",
                    "/opt/bin",
                    "/opt/local/bin",
                    "/Applications/CrossOver.app/Contents/SharedSupport/CrossOver/bin",
                ]
            )
            for k in envpath:
                if os.path.exists(k + "/wine"):
                    winedir = k
                    break
            if "winedir" not in locals():
                raise Exception(
                    "Wine binary not found in default path. Please define a path as openfemm(winepath='path/to/wine/',femmpath='path/to/femm/')."
                )

        # find femm path
        if femmpath != "":
            if os.path.isdir(femmpath):
                femmdir = femmpath
            elif os.path.isfile(femmpath):
                femmdir = re.sub("femm.exe$", "", femmpath)
            else:
                raise Exception(
                    "Given path for FEMM does not exist. Please check 'femmpath'."
                )
        else:
            # check if femm.exe exists in user's wine directory
            rootpath = [
                expanduser("~") + "/.wine/drive_c/femm42/bin",
                expanduser("~") + "/.wine/drive_c/Program Files/femm42/bin",
                expanduser("~") + "/.wine/drive_c/Progra~1/femm42/bin",
            ]
            for k in rootpath:
                if os.path.exists(k + "/femm.exe"):
                    femmdir = k
                    break
            if "femmdir" not in locals():
                raise Exception(
                    "FEMM binary not found in default path. Please define a path as openfemm(femmpath='path/to/wine/',femmpath='path/to/femm/')."
                )

        ifile = self.fixpath(femmdir + "/ifile.txt")
        ofile = self.fixpath(femmdir + "/ofile.txt")

        if os.path.exists(ifile):
            os.unlink(ifile)
        if os.path.exists(ofile):
            os.unlink(ofile)

        # test to see if there is already a femm process open
        try:
            f = open(ifile, mode="wt")
        except:
            f = open(ifile, mode="w")

        f.write("flput(0)")
        f.close()
        time.sleep(sleeptime)
        try:
            f = open(ofile, mode="rt")
            f.close()
            os.unlink(ofile)
            print("FEMM is already open")
        except FileNotFoundError as e:
            os.unlink(ifile)
            os.system(
                self.fixpath(winedir + "/wine ")
                + self.fixpath(femmdir + "/femm.exe")
                + " -filelink &"
            )
        except OSError as e:
            print("Error opening with mode rt failed:", e)
            return
        self.HandleToFEMM = "FEMM_Open"

        self.callfemm(
            "setcurrentdirectory(" + self.quote(self.fixpath(os.getcwd())) + ")"
        )
        if len(arg) == 0:
            self.main_restore()
            return
        if arg[0] == 0:
            self.main_restore()
            return

    def openfemm(self, *arg, winepath="", femmpath=""):
        global is_windows_os
        if is_windows_os:
            self.openfemm_Windows(*arg)
        else:
            self.openfemm_Linux(*arg, winepath="", femmpath="")

    def closefemm_Windows(self):
        self.HandleToFEMM = None  # no reference to the handler, femm is closed

    def closefemm_Linux(self):
        global ifile, ofile
        self.callfemm("quit()")
        del ifile, ofile

    def closefemm(self):
        global is_windows_os

        if is_windows_os:
            self.closefemm_Windows()
        else:
            self.closefemm_Linux()

    def callfemm_Windows(self, myString):
        HandleToFEMM = self.HandleToFEMM
        x = (
            HandleToFEMM.mlab2femm(myString)
            .replace("[ ", "[")
            .replace(" ]", "]")
            .replace(" ", ",")
            .replace("I", "1j")
        )
        if len(x) == 0:
            x = []
        elif x[0] == "e":
            ErrorMsg = x.replace(",", " ").replace("1j", "I")
            raise Exception(ErrorMsg)
        else:
            x = eval(x)
        if len(x) == 1:
            x = x[0]
        return x

    def callfemm_Linux(self, myString):
        global ifile, ofile
        try:
            f = open(ifile, mode="wt")
        except:
            f = open(ifile, mode="w")

        f.write("flput(" + myString + ")")
        f.close()
        x = False
        while x == False:
            try:
                f = open(ofile, mode="rt")
                x = (
                    f.readline()
                    .replace("[ ", "[")
                    .replace(" ]", "]")
                    .replace(" ", ",")
                    .replace("I", "1j")
                )
                f.close()
            except FileNotFoundError as e:
                time.sleep(sleeptime)
                notfound = 1
                while notfound:
                    try:
                        f = open(ofile, mode="rt")
                        notfound = 0
                    except FileNotFoundError as e:
                        notfound = 1
                        time.sleep(sleeptime)
                    except OSError as e:
                        print("Error opening with mode rt failed:", e)
                        return
            except OSError as e:
                print("Error opening with mode rt failed:", e)
                return
        time.sleep(sleeptime)
        os.unlink(ofile)

        if len(x) == 0:
            x = []
        elif x[0] == "e":
            ErrorMsg = x.replace(",", " ").replace("1j", "I")
            raise Exception(ErrorMsg)
        else:
            x = eval(x)
        if len(x) == 1:
            x = x[0]
        return x

    def callfemm(self, myString):
        global is_windows_os
        # print(myString) # uncomment to see all the calls made to femm while working
        if is_windows_os:
            x = self.callfemm_Windows(myString)
        else:
            x = self.callfemm_Linux(myString)
        return x

    def main_restore(self):
        self.callfemm("main_restore()")

    def num(self, n):
        return str(n).replace("j", "*I")

    def numc(self, n):
        return self.num(n) + ","

    def quote(self, myString):
        return '"' + myString + '"'

    def quotec(self, myString):
        return '"' + myString + '",'

    def doargs(self, *arg):
        if len(arg) == 0:
            return "()"
        x = "("
        for k in range(0, len(arg)):
            y = arg[k]
            if isinstance(y, string_types):
                x = x + '"' + y + '"'
            else:
                x = x + str(y)
            if k == (len(arg) - 1):
                x = x + ")"
            else:
                x = x + ","
        return x

    def newdocument(self, k):
        self.callfemm("newdocument(" + self.num(k) + ")")

    def AWG(self, awg):
        return 8.2514694 * exp(-0.115943 * awg)

    def callfemm_noeval_Windows(self, myString):
        HandleToFEMM = self.HandleToFEMM
        HandleToFEMM.mlab2femm(myString)

    def callfemm_noeval_Linux(self, myString):
        global ifile, ofile
        try:
            f = open(ifile, mode="wt")
        except:
            f = open(ifile, mode="w")

        f.write("flput(" + myString + ")")
        f.close()
        u = -1
        while u == -1:
            try:
                f = open(ofile, mode="rt")
                u = f.readline()
                f.close()
            except FileNotFoundError as e:
                print("File not found Error2:", e)
                time.sleep(sleeptime)
                notfound = 1
                while notfound:
                    try:
                        f = open(ofile, mode="rt")
                        notfound = 0
                    except FileNotFoundError as e:
                        print("File not found Error3:", e)
                        notfound = 1
                        time.sleep(sleeptime)
                    except OSError as e:
                        print("Error opening with mode rt failed:", e)
                        return
                return

        os.unlink(ofile)

    def callfemm_noeval(self, myString):
        global is_windows_os

        if is_windows_os:
            self.callfemm_Windows(self, myString)
        else:
            self.callfemm_Linux(self, myString)

    def ci_addarc(self, *arg):
        self.callfemm("ci_addarc" + self.doargs(*arg))

    def ci_addblocklabel(self, *arg):
        self.callfemm("ci_addblocklabel" + self.doargs(*arg))

    def ci_addboundprop(self, *arg):
        self.callfemm("ci_addboundprop" + self.doargs(*arg))

    def ci_addconductorprop(self, *arg):
        self.callfemm("ci_addconductorprop" + self.doargs(*arg))

    def ci_addmaterial(self, *arg):
        self.callfemm("ci_addmaterial" + self.doargs(*arg))

    def ci_addnode(self, *arg):
        self.callfemm("ci_addnode" + self.doargs(*arg))

    def ci_addpointprop(self, *arg):
        self.callfemm("ci_addpointprop" + self.doargs(*arg))

    def ci_addsegment(self, *arg):
        self.callfemm("ci_addsegment" + self.doargs(*arg))

    def ci_analyze(self, *arg):
        self.callfemm("ci_analyze" + self.doargs(*arg))

    def ci_analyse(self, n):
        self.ci_analyze(n)

    def ci_attachdefault(self):
        self.callfemm("ci_attachdefault()")

    def ci_clearselected(self):
        self.callfemm("ci_clearselected()")

    def ci_cleartkpoints(self, n):
        self.callfemm("ci_cleartkpoints(" + self.quote(n) + ")")

    def ci_close(self):
        self.callfemm("ci_close()")

    def ci_copyrotate(self, *arg):
        self.callfemm("ci_copyrotate" + self.doargs(*arg))

    def ci_copyrotate2(self, *arg):
        self.callfemm("ci_copyrotate" + self.doargs(*arg))

    def ci_copytranslate(self, *arg):
        self.callfemm("ci_copytranslate" + self.doargs(*arg))

    def ci_createmesh(self):
        return self.callfemm("ci_createmesh()")

    def ci_createradius(self, x, y, r):
        self.callfemm(
            "ci_createradius(" + self.numc(x) + self.numc(y) + self.num(r) + ")"
        )

    def ci_deleteboundprop(self, n):
        self.callfemm("ci_deleteboundprop(" + self.quote(n) + ")")

    def ci_deleteconductor(self, n):
        self.callfemm("ci_deleteconductor(" + self.quote(n) + ")")

    def ci_deletematerial(self, n):
        self.callfemm("ci_deletematerial(" + self.quote(n) + ")")

    def ci_deletepointprop(self, n):
        self.callfemm("ci_deletepointprop(" + self.quote(n) + ")")

    def ci_deleteselected(self):
        self.callfemm("ci_deleteselected()")

    def ci_deleteselectedarcsegments(self):
        self.callfemm("ci_deleteselectedarcsegments()")

    def ci_deleteselectedlabels(self):
        self.callfemm("ci_deleteselectedlabels()")

    def ci_deleteselectednodes(self):
        self.callfemm("ci_deleteselectednodes()")

    def ci_deleteselectedsegments(self):
        self.callfemm("ci_deleteselectedsegments()")

    def ci_detachdefault(self):
        self.callfemm("ci_detachdefault()")

    def ci_drawarc(self, x1, y1, x2, y2, angle, maxseg):
        self.ci_addnode(x1, y1)
        self.ci_addnode(x2, y2)
        self.ci_addarc(x1, y1, x2, y2, angle, maxseg)

    def ci_drawline(self, x1, y1, x2, y2):
        self.ci_addnode(x1, y1)
        self.ci_addnode(x2, y2)
        self.ci_addsegment(x1, y1, x2, y2)

    def ci_drawrectangle(self, x1, y1, x2, y2):
        self.ci_drawline(x1, y1, x2, y1)
        self.ci_drawline(x2, y1, x2, y2)
        self.ci_drawline(x2, y2, x1, y2)
        self.ci_drawline(x1, y2, x1, y1)

    def ci_getmaterial(self, matname):
        self.callfemm("ci_getmaterial(" + self.quote(matname) + ")")

    def ci_hidegrid(self):
        self.callfemm("ci_hidegrid()")

    def ci_hidenames(self):
        self.callfemm("ci_shownames(0)")

    def ci_loadsolution(self):
        self.callfemm("ci_loadsolution()")

    def ci_makeABC(self, *args):
        self.callfemm("ci_makeABC" + self.doargs(*args))

    def ci_maximize(self):
        self.callfemm("ci_maximize()")

    def ci_minimize(self):
        self.callfemm("ci_minimize()")

    def ci_mirror(self, x1, x2, y1, y2):
        self.callfemm(
            "ci_mirror("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def ci_mirror2(self, x1, x2, y1, y2, editaction):
        self.callfemm(
            "ci_mirror("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.numc(y2)
            + self.num(editaction)
            + ")"
        )

    def ci_modifyboundprop(self, *arg):
        self.callfemm("ci_modifyboundprop" + self.doargs(*arg))

    def ci_modifyconductorprop(self, *arg):
        self.callfemm("ci_modifyconductorprop" + self.doargs(*arg))

    def ci_modifymaterial(self, *arg):
        self.callfemm("ci_modifymaterial" + self.doargs(*arg))

    def ci_modifypointprop(self, *arg):
        self.callfemm("ci_modifypointprop" + self.doargs(*arg))

    def ci_moverotate(self, bx, by, shiftangle):
        self.callfemm(
            "ci_moverotate("
            + self.numc(bx)
            + self.numc(by)
            + self.num(shiftangle)
            + ")"
        )

    def ci_movetranslate(self, bx, by):
        self.callfemm("ci_movetranslate(" + self.numc(bx) + self.num(by) + ")")

    def ci_movetranslate2(self, bx, by, editaction):
        self.callfemm(
            "ci_movetranslate("
            + self.numc(bx)
            + self.numc(by)
            + self.num(editaction)
            + ")"
        )

    def ci_probdef(self, *arg):
        self.callfemm("ci_probdef" + self.doargs(*arg))

    def ci_purgemesh(self):
        self.callfemm("ci_purgemesh()")

    def ci_readdxf(self, docname):
        self.callfemm("print(ci_readdxf(" + self.quote(docname) + "))")

    def ci_refreshview(self):
        self.callfemm("ci_refreshview()")

    def ci_resize(self, nWidth, nHeight):
        self.callfemm("ci_resize(" + self.numc(nWidth) + self.num(nHeight) + ")")

    def ci_restore(self):
        self.callfemm("ci_restore()")

    def ci_saveas(self, fn):
        self.callfemm("ci_saveas(" + self.quote(self.fixpath(fn)) + ")")

    def ci_savebitmap(self, n):
        self.callfemm("ci_savebitmap(" + self.quote(n) + ")")

    def ci_savedxf(self, docname):
        self.callfemm_noeval("ci_savedxf(" + self.quote(docname) + ")")

    def ci_savemetafile(self, n):
        self.callfemm("ci_savemetafile(" + self.quote(n) + ")")

    def ci_scale(self, bx, by, sc):
        self.callfemm("ci_scale(" + self.numc(bx) + self.numc(by) + self.numc(sc) + ")")

    def ci_scale2(self, bx, by, sc, ea):
        self.callfemm(
            "ci_scale("
            + self.numc(bx)
            + self.numc(by)
            + self.numc(sc)
            + self.num(ea)
            + ")"
        )

    def ci_selectarcsegment(self, x, y):
        return self.callfemm("ci_selectarcsegment(" + self.numc(x) + self.num(y) + ")")

    def ci_selectcircle(self, *arg):
        return self.callfemm("ci_selectcircle" + self.doargs(*arg))

    def ci_selectgroup(self, gr):
        return self.callfemm("ci_selectgroup(" + self.num(gr) + ")")

    def ci_selectlabel(self, x, y):
        return self.callfemm("ci_selectlabel(" + self.numc(x) + self.num(y) + ")")

    def ci_selectnode(self, x, y):
        return self.callfemm("ci_selectnode(" + self.numc(x) + self.num(y) + ")")

    def ci_selectrectangle(self, *arg):
        self.callfemm("ci_selectrectangle" + self.doargs(*arg))

    def ci_selectsegment(self, x, y):
        return self.callfemm("ci_selectsegment(" + self.numc(x) + self.num(y) + ")")

    def ci_setarcsegmentprop(self, maxsegdeg, propname, hide, group, incond):
        self.callfemm(
            "ci_setarcsegmentprop("
            + self.numc(maxsegdeg)
            + self.quotec(propname)
            + self.numc(hide)
            + self.numc(group)
            + self.quote(incond)
            + ")"
        )

    def ci_setblockprop(self, blockname, automesh, meshsize, group):
        self.callfemm(
            "ci_setblockprop("
            + self.quotec(blockname)
            + self.numc(automesh)
            + self.numc(meshsize)
            + self.num(group)
            + ")"
        )

    def ci_seteditmode(self, editmode):
        self.callfemm("ci_seteditmode(" + self.quote(editmode) + ")")

    def ci_setfocus(self, docname):
        self.callfemm("ci_setfocus(" + self.quote(docname) + ")")

    def ci_setgrid(self, density, ptype):
        self.callfemm("ci_setgrid(" + self.numc(density) + self.quote(ptype) + ")")

    def ci_setgroup(self, n):
        return self.callfemm("ci_setgroup(" + self.num(n) + ")")

    def ci_setnodeprop(self, nodeprop, groupno, incond):
        self.callfemm(
            "ci_setnodeprop("
            + self.quotec(nodeprop)
            + self.numc(groupno)
            + self.quote(incond)
            + ")"
        )

    def ci_setsegmentprop(self, pn, es, am, hi, gr, incond):
        self.callfemm(
            "ci_setsegmentprop("
            + self.quotec(pn)
            + self.numc(es)
            + self.numc(am)
            + self.numc(hi)
            + self.numc(gr)
            + self.quote(incond)
            + ")"
        )

    def ci_showgrid(self):
        self.callfemm("ci_showgrid()")

    def ci_showmesh(self):
        self.callfemm("ci_showmesh()")

    def ci_shownames(self):
        self.callfemm("ci_shownames(1)")

    def ci_smartmesh(self, n):
        self.callfemm("ci_smartmesh(" + self.num(n) + ")")

    def ci_snapgridoff(self):
        self.callfemm('ci_gridsnap("off")')

    def ci_snapgridon(self):
        self.callfemm('ci_gridsnap("on")')

    def ci_zoom(self, x1, y1, x2, y2):
        self.callfemm(
            "ci_zoom("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def ci_zoomin(self):
        self.callfemm("ci_zoomin()")

    def ci_zoomnatural(self):
        self.callfemm("ci_zoomnatural()")

    def ci_zoomout(self):
        self.callfemm("ci_zoomout()")

    def co_addcontour(self, x, y):
        self.callfemm("co_addcontour(" + self.numc(x) + self.num(y) + ")")

    def co_bendcontour(self, tta, dtta):
        self.callfemm("co_bendcontour(" + self.numc(tta) + self.num(dtta) + ")")

    def co_blockintegral(self, ptype):
        return self.callfemm("co_blockintegral(" + self.num(ptype) + ")")

    def co_clearblock(self):
        self.callfemm("co_clearblock()")

    def co_clearcontour(self):
        self.callfemm("co_clearcontour()")

    def co_close(self):
        self.callfemm("co_close()")

    def co_getconductorproperties(self, pname):
        return self.callfemm("co_getconductorproperties(" + self.quote(pname) + ")")

    def co_gete(self, x, y):
        z = self.co_getpointvalues(x, y)
        return [z[5], z[6]]

    def co_getelement(self, n):
        return self.callfemm("co_getelement(" + self.num(n) + ")")

    def co_getj(self, x, y):
        z = self.co_getpointvalues(x, y)
        return [z[1], z[2]]

    def co_getk(self, x, y):
        z = self.co_getpointvalues(x, y)
        return [z[3], z[4]]

    def co_getnode(self, n):
        return self.callfemm("co_getnode(" + self.num(n) + ")")

    def co_getpointvalues(self, x, y):
        return self.callfemm("co_getpointvalues(" + self.numc(x) + self.num(y) + ")")

    def co_getprobleminfo(self):
        return self.callfemm("co_getprobleminfo()")

    def co_getv(self, x, y):
        z = self.co_getpointvalues(x, y)
        return z[0]

    def co_groupselectblock(self, *arg):
        self.callfemm("co_groupselectblock" + self.doargs(*arg))

    def co_hidecontourplot(self):
        self.callfemm("co_hidecontourplot()")

    def co_hidedensityplot(self):
        self.callfemm("co_hidedensityplot()")

    def co_hidegrid(self):
        self.callfemm("co_hidegrid()")

    def co_hidemesh(self):
        self.callfemm("co_hidemesh()")

    def co_hidenames(self):
        self.callfemm("co_shownames(0)")

    def co_hidepoints(self):
        self.callfemm("co_hidepoints()")

    def co_lineintegral(self, ptype):
        return self.callfemm("co_lineintegral(" + self.num(ptype) + ")")

    def co_makeplot(self, *arg):
        self.callfemm("co_makeplot" + self.doargs(*arg))

    def co_maximize(self):
        self.callfemm("co_maximize()")

    def co_minimize(self):
        self.callfemm("co_minimize()")

    def co_numelements(self):
        return self.callfemm("co_numelements()")

    def co_numnodes(self):
        return self.callfemm("co_numnodes()")

    def co_refreshview(self):
        self.callfemm("co_refreshview()")

    def co_reload(self):
        self.callfemm("co_reload()")

    def co_resize(self, nWidth, nHeight):
        self.callfemm("co_resize(" + self.numc(nWidth) + self.num(nHeight) + ")")

    def co_restore(self):
        self.callfemm("co_restore()")

    def co_savebitmap(self, fn):
        self.callfemm("co_savebitmap(" + self.quote(self.fixpath(fn)) + ")")

    def co_savemetafile(self, fn):
        self.callfemm("co_savemetafile(" + self.quote(self.fixpath(fn)) + ")")

    def co_selectblock(self, x, y):
        self.callfemm("co_selectblock(" + self.numc(x) + self.num(y) + ")")

    def co_selectpoint(self, x, y):
        self.callfemm("co_selectpoint(" + self.numc(x) + self.num(y) + ")")

    def co_seteditmode(self, mode):
        self.callfemm("co_seteditmode(" + self.quote(mode) + ")")

    def co_setgrid(self, density, ptype):
        self.callfemm("co_setgrid(" + self.numc(density) + self.quote(ptype) + ")")

    def co_showcontourplot(self, numcontours, al, au):
        self.callfemm(
            "co_showcontourplot("
            + self.numc(numcontours)
            + self.numc(al)
            + self.num(au)
            + ")"
        )

    def co_showdensityplot(self, legend, gscale, ptype, bu, bl):
        self.callfemm(
            "co_showdensityplot("
            + self.numc(legend)
            + self.numc(gscale)
            + self.numc(ptype)
            + self.numc(bu)
            + self.num(bl)
            + ")"
        )

    def co_showgrid(self):
        self.callfemm("co_showgrid()")

    def co_showmesh(self):
        self.callfemm("co_showmesh()")

    def co_shownames(self):
        self.callfemm("co_shownames(1)")

    def co_showpoints(self):
        self.callfemm("co_showpoints()")

    def co_showvectorplot(self, *arg):
        self.callfemm("co_showvectorplot" + self.doargs(*arg))

    def co_smooth(self, flag):
        self.callfemm("co_smooth(" + self.quote(flag) + ")")

    def co_smoothoff(self):
        self.callfemm('co_smooth("off")')

    def co_smoothon(self):
        self.callfemm('co_smooth("on")')

    def co_snapgrid(self, flag):
        self.callfemm("co_gridsnap(" + self.quote(flag) + ")")

    def co_snapgridoff(self):
        self.callfemm('co_gridsnap("off")')

    def co_snapgridon(self):
        self.callfemm('co_gridsnap("on")')

    def co_zoom(self, x1, y1, x2, y2):
        self.callfemm(
            "co_zoom("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def co_zoomin(self):
        self.callfemm("co_zoomin()")

    def co_zoomnatural(self):
        self.callfemm("co_zoomnatural()")

    def co_zoomout(self):
        self.callfemm("co_zoomout()")

    def complex2str(self, x):
        return str(x)

    def create(self, n):
        self.callfemm("create(" + self.num(n) + ")")

    def ei_addarc(self, x1, y1, x2, y2, angle, maxseg):
        self.callfemm(
            "ei_addarc("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.numc(y2)
            + self.numc(angle)
            + self.num(maxseg)
            + ")"
        )

    def ei_addblocklabel(self, x, y):
        self.callfemm("ei_addblocklabel(" + self.numc(x) + self.num(y) + ")")

    def ei_addboundprop(self, pname, vs, qs, c0, c1, fmt):
        self.callfemm(
            "ei_addboundprop("
            + self.quotec(pname)
            + self.numc(vs)
            + self.numc(qs)
            + self.numc(c0)
            + self.numc(c1)
            + self.num(fmt)
            + ")"
        )

    def ei_addconductorprop(self, pname, vc, qc, ptype):
        self.callfemm(
            "ei_addconductorprop("
            + self.quotec(pname)
            + self.numc(vc)
            + self.numc(qc)
            + self.num(ptype)
            + ")"
        )

    def ei_addmaterial(self, pname, ex, ey, qv):
        self.callfemm(
            "ei_addmaterial("
            + self.quotec(pname)
            + self.numc(ex)
            + self.numc(ey)
            + self.num(qv)
            + ")"
        )

    def ei_addnode(self, x, y):
        self.callfemm("ei_addnode(" + self.numc(x) + self.num(y) + ")")

    def ei_addpointprop(self, pname, vp, qp):
        self.callfemm(
            "ei_addpointprop(" + self.quotec(pname) + self.numc(vp) + self.num(qp) + ")"
        )

    def ei_addsegment(self, x1, y1, x2, y2):
        self.callfemm(
            "ei_addsegment("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def ei_analyze(self, *arg):
        self.callfemm("ei_analyze" + self.doargs(*arg))

    def ei_analyse(self, n):
        self.ei_analyze(n)

    def ei_attachdefault(self):
        self.callfemm("ei_attachdefault()")

    def ei_attachouterspace(self):
        self.callfemm("ei_attachouterspace()")

    def ei_clearselected(self):
        self.callfemm("ei_clearselected()")

    def ei_close(self):
        self.callfemm("ei_close()")

    def ei_copyrotate(self, bx, by, angle, copies):
        self.callfemm(
            "ei_copyrotate("
            + self.numc(bx)
            + self.numc(by)
            + self.numc(angle)
            + self.num(copies)
            + ")"
        )

    def ei_copyrotate2(self, bx, by, angle, copies, editaction):
        self.callfemm(
            "ei_copyrotate("
            + self.numc(bx)
            + self.numc(by)
            + self.numc(angle)
            + self.numc(copies)
            + self.num(editaction)
            + ")"
        )

    def ei_copytranslate(self, bx, by, copies):
        self.callfemm(
            "ei_copytranslate(" + self.numc(bx) + self.numc(by) + self.num(copies) + ")"
        )

    def ei_copytranslate2(self, bx, by, copies, editaction):
        self.callfemm(
            "ei_copytranslate("
            + self.numc(bx)
            + self.numc(by)
            + self.numc(copies)
            + self.num(editaction)
            + ")"
        )

    def ei_createmesh(self):
        return self.callfemm("ei_createmesh()")

    def ei_createradius(self, x, y, r):
        self.callfemm(
            "ei_createradius(" + self.numc(x) + self.numc(y) + self.num(r) + ")"
        )

    def ei_defineouterspace(self, Zo, Ro, Ri):
        self.callfemm(
            "ei_defineouterspace(" + self.numc(Zo) + self.numc(Ro) + self.num(Ri) + ")"
        )

    def ei_deleteboundprop(self, n):
        self.callfemm("ei_deleteboundprop(" + self.quote(n) + ")")

    def ei_deleteconductor(self, n):
        self.callfemm("ei_deleteconductor(" + self.quote(n) + ")")

    def ei_deletematerial(self, n):
        self.callfemm("ei_deletematerial(" + self.quote(n) + ")")

    def ei_deletepointprop(self, n):
        self.callfemm("ei_deletepointprop(" + self.quote(n) + ")")

    def ei_deleteselected(self):
        self.callfemm("ei_deleteselected()")

    def ei_deleteselectedarcsegments(self):
        self.callfemm("ei_deleteselectedarcsegments()")

    def ei_deleteselectedlabels(self):
        self.callfemm("ei_deleteselectedlabels()")

    def ei_deleteselectednodes(self):
        self.callfemm("ei_deleteselectednodes()")

    def ei_deleteselectedsegments(self):
        self.callfemm("ei_deleteselectedsegments()")

    def ei_detachdefault(self):
        self.callfemm("ei_detachdefault()")

    def ei_detachouterspace(self):
        self.callfemm("ei_detachouterspace()")

    def ei_drawarc(self, x1, y1, x2, y2, angle, maxseg):
        self.ei_addnode(x1, y1)
        self.ei_addnode(x2, y2)
        self.ei_addarc(x1, y1, x2, y2, angle, maxseg)

    def ei_drawline(self, x1, y1, x2, y2):
        self.ei_addnode(x1, y1)
        self.ei_addnode(x2, y2)
        self.ei_addsegment(x1, y1, x2, y2)

    def ei_drawrectangle(self, x1, y1, x2, y2):
        self.ei_drawline(x1, y1, x2, y1)
        self.ei_drawline(x2, y1, x2, y2)
        self.ei_drawline(x2, y2, x1, y2)
        self.ei_drawline(x1, y2, x1, y1)

    def ei_getmaterial(self, matname):
        self.callfemm("ei_getmaterial(" + self.quote(matname) + ")")

    def ei_hidegrid(self):
        self.callfemm("ei_hidegrid()")

    def ei_hidenames(self):
        self.callfemm("ei_shownames(0)")

    def ei_loadsolution(self):
        self.callfemm("ei_loadsolution()")

    def ei_makeABC(self, *arg):
        self.callfemm("ei_makeABC" + self.doargs(*arg))

    def ei_maximize(self):
        self.callfemm("ei_maximize()")

    def ei_minimize(self):
        self.callfemm("ei_minimize()")

    def ei_mirror(self, x1, y1, x2, y2):
        self.callfemm(
            "ei_mirror("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def ei_mirror2(self, x1, y1, x2, y2, editaction):
        self.callfemm(
            "ei_mirror("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.numc(y2)
            + self.num(editaction)
            + ")"
        )

    def ei_modifyboundprop(self, *arg):
        self.callfemm("ei_modifyboundprop" + self.doargs(*arg))

    def ei_modifyconductorprop(self, *arg):
        self.callfemm("ei_modifyconductorprop" + self.doargs(*arg))

    def ei_modifymaterial(self, *arg):
        self.callfemm("ei_modifymaterial" + self.doargs(*arg))

    def ei_modifypointprop(self, *arg):
        self.callfemm("ei_modifypointprop" + self.doargs(*arg))

    def ei_moverotate(self, bx, by, shiftangle):
        self.callfemm(
            "ei_moverotate("
            + self.numc(bx)
            + self.numc(by)
            + self.num(shiftangle)
            + ")"
        )

    def ei_movetranslate(self, bx, by):
        self.callfemm("ei_movetranslate(" + self.numc(bx) + self.num(by) + ")")

    def ei_movetranslate2(self, bx, by, editaction):
        self.callfemm(
            "ei_movetranslate("
            + self.numc(bx)
            + self.numc(by)
            + self.num(editaction)
            + ")"
        )

    def ei_probdef(self, *arg):
        self.callfemm("ei_probdef" + self.doargs(*arg))

    def ei_purgemesh(self):
        self.callfemm("ei_purgemesh()")

    def ei_readdxf(self, docname):
        self.callfemm("print(ei_readdxf(" + self.quote(docname) + "))")

    def ei_refreshview(self):
        self.callfemm("ei_refreshview()")

    def ei_resize(self, nWidth, nHeight):
        self.callfemm("ei_resize(" + self.numc(nWidth) + self.num(nHeight) + ")")

    def ei_restore(self):
        self.callfemm("ei_restore()")

    def ei_saveas(self, fn):
        self.callfemm("ei_saveas(" + self.quote(self.fixpath(fn)) + ")")

    def ei_savebitmap(self, n):
        self.callfemm("ei_savebitmap(" + self.quote(n) + ")")

    def ei_savedxf(self, docname):
        self.callfemm_noeval("ei_savedxf(" + self.quote(docname) + ")")

    def ei_savemetafile(self, n):
        self.callfemm("ei_savemetafile(" + self.quote(n) + ")")

    def ei_scale(self, bx, by, sc):
        self.callfemm("ei_scale(" + self.numc(bx) + self.numc(by) + self.numc(sc) + ")")

    def ei_scale2(self, bx, by, sc, ea):
        self.callfemm(
            "ei_scale("
            + self.numc(bx)
            + self.numc(by)
            + self.numc(sc)
            + self.num(ea)
            + ")"
        )

    def ei_selectarcsegment(self, x, y):
        return self.callfemm("ei_selectarcsegment(" + self.numc(x) + self.num(y) + ")")

    def ei_selectcircle(self, *arg):
        self.callfemm("ei_selectcircle" + self.doargs(*arg))

    def ei_selectgroup(self, gr):
        self.callfemm("ei_selectgroup(" + self.num(gr) + ")")

    def ei_selectlabel(self, x, y):
        return self.callfemm("ei_selectlabel(" + self.numc(x) + self.num(y) + ")")

    def ei_selectnode(self, x, y):
        return self.callfemm("ei_selectnode(" + self.numc(x) + self.num(y) + ")")

    def ei_selectrectangle(self, *arg):
        self.callfemm("ei_selectrectangle" + self.doargs(*arg))

    def ei_selectsegment(self, x, y):
        return self.callfemm("ei_selectsegment(" + self.numc(x) + self.num(y) + ")")

    def ei_setarcsegmentprop(self, maxsegdeg, propname, hide, group, incond):
        self.callfemm(
            "ei_setarcsegmentprop("
            + self.numc(maxsegdeg)
            + self.quotec(propname)
            + self.numc(hide)
            + self.numc(group)
            + self.quote(incond)
            + ")"
        )

    def ei_setblockprop(self, blockname, automesh, meshsize, group):
        self.callfemm(
            "ei_setblockprop("
            + self.quotec(blockname)
            + self.numc(automesh)
            + self.numc(meshsize)
            + self.num(group)
            + ")"
        )

    def ei_seteditmode(self, editmode):
        self.callfemm("ei_seteditmode(" + self.quote(editmode) + ")")

    def ei_setfocus(self, docname):
        self.callfemm("ei_setfocus(" + self.quote(docname) + ")")

    def ei_setgrid(self, density, ptype):
        self.callfemm("ei_setgrid(" + self.numc(density) + self.quote(ptype) + ")")

    def ei_setgroup(self, n):
        return self.callfemm("ei_setgroup(" + self.num(n) + ")")

    def ei_setnodeprop(self, nodeprop, groupno, inconductor):
        self.callfemm(
            "ei_setnodeprop("
            + self.quotec(nodeprop)
            + self.numc(groupno)
            + self.quote(inconductor)
            + ")"
        )

    def ei_setsegmentprop(self, pn, es, am, hi, gr, inconductor):
        self.callfemm(
            "ei_setsegmentprop("
            + self.quotec(pn)
            + self.numc(es)
            + self.numc(am)
            + self.numc(hi)
            + self.numc(gr)
            + self.quote(inconductor)
            + ")"
        )

    def ei_showgrid(self):
        self.callfemm("ei_showgrid()")

    def ei_showmesh(self):
        self.callfemm("ei_showmesh()")

    def ei_shownames(self):
        self.callfemm("ei_shownames(1)")

    def ei_smartmesh(self, n):
        self.callfemm("ei_smartmesh(" + self.num(n) + ")")

    def ei_snapgridoff(self):
        self.callfemm('ei_gridsnap("off")')

    def ei_snapgridon(self):
        self.callfemm('ei_gridsnap("on")')

    def ei_zoom(self, x1, y1, x2, y2):
        self.callfemm(
            "ei_zoom("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def ei_zoomin(self):
        self.callfemm("ei_zoomin()")

    def ei_zoomnatural(self):
        self.callfemm("ei_zoomnatural()")

    def ei_zoomout(self):
        self.callfemm("ei_zoomout()")

    def eo_addcontour(self, x, y):
        self.callfemm("eo_addcontour(" + self.numc(x) + self.num(y) + ")")

    def eo_bendcontour(self, tta, dtta):
        self.callfemm("eo_bendcontour(" + self.numc(tta) + self.num(dtta) + ")")

    def eo_blockintegral(self, ptype):
        return self.callfemm("eo_blockintegral(" + self.num(ptype) + ")")

    def eo_clearblock(self):
        self.callfemm("eo_clearblock()")

    def eo_clearcontour(self):
        self.callfemm("eo_clearcontour()")

    def eo_close(self):
        self.callfemm("eo_close()")

    def eo_getconductorproperties(self, pname):
        return self.callfemm("eo_getconductorproperties(" + self.quote(pname) + ")")

    def eo_getd(self, x, y):
        z = self.eo_getpointvalues(x, y)
        return [z[1], z[2]]

    def eo_gete(self, x, y):
        z = self.eo_getpointvalues(x, y)
        return [z[3], z[4]]

    def eo_getelement(self, n):
        return self.callfemm("eo_getelement(" + self.num(n) + ")")

    def eo_getenergydensity(self, x, y):
        z = self.eo_getpointvalues(x, y)
        return z[7]

    def eo_getnode(self, n):
        return self.callfemm("eo_getnode(" + self.num(n) + ")")

    def eo_getperm(self, x, y):
        z = self.eo_getpointvalues(x, y)
        return [z[5], z[6]]

    def eo_getpointvalues(self, x, y):
        z = self.callfemm("eo_getpointvalues(" + self.numc(x) + self.num(y) + ")")
        if len(z) > 0:
            return z
        return [0, 0, 0, 0, 0, 0, 0, 0]

    def eo_getprobleminfo(self):
        return self.callfemm("eo_getprobleminfo()")

    def eo_getv(self, x, y):
        z = self.eo_getpointvalues(x, y)
        return z[0]

    def eo_groupselectblock(self, *arg):
        self.callfemm("eo_groupselectblock" + self.doargs(*arg))

    def eo_hidecontourplot(self):
        self.callfemm("eo_hidecontourplot()")

    def eo_hidedensityplot(self):
        self.callfemm("eo_hidedensityplot()")

    def eo_hidegrid(self):
        self.callfemm("eo_hidegrid()")

    def eo_hidemesh(self):
        self.callfemm("eo_hidemesh()")

    def eo_hidenames(self):
        self.callfemm("eo_shownames(0)")

    def eo_hidepoints(self):
        self.callfemm("eo_hidepoints()")

    def eo_lineintegral(self, ptype):
        return self.callfemm("eo_lineintegral(" + self.num(ptype) + ")")

    def eo_makeplot(self, *arg):
        self.callfemm("eo_makeplot" + self.doargs(*arg))

    def eo_maximize(self):
        self.callfemm("eo_maximize()")

    def eo_minimize(self):
        self.callfemm("eo_minimize()")

    def eo_numelements(self):
        return self.callfemm("eo_numelements()")

    def eo_numnodes(self):
        return self.callfemm("eo_numnodes()")

    def eo_refreshview(self):
        self.callfemm("eo_refreshview()")

    def eo_reload(self):
        self.callfemm("eo_reload()")

    def eo_resize(self, nWidth, nHeight):
        self.callfemm("eo_resize(" + self.numc(nWidth) + self.num(nHeight) + ")")

    def eo_restore(self):
        self.callfemm("eo_restore()")

    def eo_savebitmap(self, fn):
        self.callfemm("eo_savebitmap(" + self.quote(self.fixpath(fn)) + ")")

    def eo_savemetafile(self, fn):
        self.callfemm("eo_savemetafile(" + self.quote(self.fixpath(fn)) + ")")

    def eo_selectblock(self, x, y):
        self.callfemm("eo_selectblock(" + self.numc(x) + self.num(y) + ")")

    def eo_selectpoint(self, x, y):
        self.callfemm("eo_selectpoint(" + self.numc(x) + self.num(y) + ")")

    def eo_seteditmode(self, mode):
        self.callfemm("eo_seteditmode(" + self.quote(mode) + ")")

    def eo_setgrid(self, density, ptype):
        self.callfemm("eo_setgrid(" + self.numc(density) + self.quote(ptype) + ")")

    def eo_showcontourplot(self, numcontours, al, au):
        self.callfemm(
            "eo_showcontourplot("
            + self.numc(numcontours)
            + self.numc(al)
            + self.num(au)
            + ")"
        )

    def eo_showdensityplot(self, legend, gscale, ptype, bu, bl):
        self.callfemm(
            "eo_showdensityplot("
            + self.numc(legend)
            + self.numc(gscale)
            + self.numc(ptype)
            + self.numc(bu)
            + self.num(bl)
            + ")"
        )

    def eo_showgrid(self):
        self.callfemm("eo_showgrid()")

    def eo_showmesh(self):
        self.callfemm("eo_showmesh()")

    def eo_shownames(self):
        self.callfemm("eo_shownames(1)")

    def eo_showpoints(self):
        self.callfemm("eo_showpoints()")

    def eo_showvectorplot(self, *arg):
        self.callfemm("eo_showvectorplot" + self.doargs(*arg))

    def eo_smooth(self, flag):
        self.callfemm("eo_smooth(" + self.quote(flag) + ")")

    def eo_smoothoff(self):
        self.callfemm('eo_smooth("off")')

    def eo_smoothon(self):
        self.callfemm('eo_smooth("on")')

    def eo_snapgrid(self, flag):
        self.callfemm("eo_gridsnap(" + self.quote(flag) + ")")

    def eo_snapgridoff(self):
        self.callfemm('eo_gridsnap("off")')

    def eo_snapgridon(self):
        self.callfemm('eo_gridsnap("on")')

    def eo_zoom(self, x1, y1, x2, y2):
        self.callfemm(
            "eo_zoom("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def eo_zoomin(self):
        self.callfemm("eo_zoomin()")

    def eo_zoomnatural(self):
        self.callfemm("eo_zoomnatural()")

    def eo_zoomout(self):
        self.callfemm("eo_zoomout()")

    def hi_addarc(self, x1, y1, x2, y2, angle, maxseg):
        self.callfemm(
            "hi_addarc("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.numc(y2)
            + self.numc(angle)
            + self.num(maxseg)
            + ")"
        )

    def hi_addblocklabel(self, x, y):
        self.callfemm("hi_addblocklabel(" + self.numc(x) + self.num(y) + ")")

    def hi_addboundprop(self, *arg):
        self.callfemm("hi_addboundprop" + self.doargs(*arg))

    def hi_addconductorprop(self, *arg):
        self.callfemm("hi_addconductorprop" + self.doargs(*arg))

    def hi_addmaterial(self, *arg):
        self.callfemm("hi_addmaterial" + self.doargs(*arg))

    def hi_addnode(self, x, y):
        self.callfemm("hi_addnode(" + self.numc(x) + self.num(y) + ")")

    def hi_addpointprop(self, *arg):
        self.callfemm("hi_addpointprop" + self.doargs(*arg))

    def hi_addsegment(self, x1, y1, x2, y2):
        self.callfemm(
            "hi_addsegment("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def hi_addtkpoint(self, name, b, h):
        self.callfemm(
            "hi_addtkpoint(" + self.quotec(name) + self.numc(b) + self.num(h) + ")"
        )

    def hi_analyze(self, *arg):
        self.callfemm("hi_analyze" + self.doargs(*arg))

    def hi_analyse(self, n):
        self.hi_analyze(n)

    def hi_attachdefault(self):
        self.callfemm("hi_attachdefault()")

    def hi_attachouterspace(self):
        self.callfemm("hi_attachouterspace()")

    def hi_clearselected(self):
        self.callfemm("hi_clearselected()")

    def hi_cleartkpoints(self, n):
        self.callfemm("hi_cleartkpoints(" + self.quote(n) + ")")

    def hi_close(self):
        self.callfemm("hi_close()")

    def hi_copyrotate(self, bx, by, angle, copies):
        self.callfemm(
            "hi_copyrotate("
            + self.numc(bx)
            + self.numc(by)
            + self.numc(angle)
            + self.num(copies)
            + ")"
        )

    def hi_copyrotate2(self, bx, by, angle, copies, editaction):
        self.callfemm(
            "hi_copyrotate("
            + self.numc(bx)
            + self.numc(by)
            + self.numc(angle)
            + self.numc(copies)
            + self.num(editaction)
            + ")"
        )

    def hi_copytranslate(self, bx, by, copies):
        self.callfemm(
            "hi_copytranslate(" + self.numc(bx) + self.numc(by) + self.num(copies) + ")"
        )

    def hi_copytranslate2(self, bx, by, copies, editaction):
        self.callfemm(
            "hi_copytranslate("
            + self.numc(bx)
            + self.numc(by)
            + self.numc(copies)
            + self.num(editaction)
            + ")"
        )

    def hi_createmesh(self):
        return self.callfemm("hi_createmesh()")

    def hi_createradius(self, x, y, r):
        self.callfemm(
            "hi_createradius(" + self.numc(x) + self.numc(y) + self.num(r) + ")"
        )

    def hi_defineouterspace(self, Zo, Ro, Ri):
        self.callfemm(
            "hi_defineouterspace(" + self.numc(Zo) + self.numc(Ro) + self.num(Ri) + ")"
        )

    def hi_deleteboundprop(self, n):
        self.callfemm("hi_deleteboundprop(" + self.quote(n) + ")")

    def hi_deleteconductor(self, n):
        self.callfemm("hi_deleteconductor(" + self.quote(n) + ")")

    def hi_deletematerial(self, n):
        self.callfemm("hi_deletematerial(" + self.quote(n) + ")")

    def hi_deletepointprop(self, n):
        self.callfemm("hi_deletepointprop(" + self.quote(n) + ")")

    def hi_deleteselected(self):
        self.callfemm("hi_deleteselected()")

    def hi_deleteselectedarcsegments(self):
        self.callfemm("hi_deleteselectedarcsegments()")

    def hi_deleteselectedlabels(self):
        self.callfemm("hi_deleteselectedlabels()")

    def hi_deleteselectednodes(self):
        self.callfemm("hi_deleteselectednodes()")

    def hi_deleteselectedsegments(self):
        self.callfemm("hi_deleteselectedsegments()")

    def hi_detachdefault(self):
        self.callfemm("hi_detachdefault()")

    def hi_detachouterspace(self):
        self.callfemm("hi_detachouterspace()")

    def hi_drawarc(self, x1, y1, x2, y2, angle, maxseg):
        self.hi_addnode(x1, y1)
        self.hi_addnode(x2, y2)
        self.hi_addarc(x1, y1, x2, y2, angle, maxseg)

    def hi_drawline(self, x1, y1, x2, y2):
        self.hi_addnode(x1, y1)
        self.hi_addnode(x2, y2)
        self.hi_addsegment(x1, y1, x2, y2)

    def hi_drawrectangle(self, x1, y1, x2, y2):
        self.hi_drawline(x1, y1, x2, y1)
        self.hi_drawline(x2, y1, x2, y2)
        self.hi_drawline(x2, y2, x1, y2)
        self.hi_drawline(x1, y2, x1, y1)

    def hi_getmaterial(self, matname):
        self.callfemm("hi_getmaterial(" + self.quote(matname) + ")")

    def hi_hidegrid(self):
        self.callfemm("hi_hidegrid()")

    def hi_hidenames(self):
        self.callfemm("hi_shownames(0)")

    def hi_loadsolution(self):
        self.callfemm("hi_loadsolution()")

    def hi_makeABC(self, *arg):
        self.callfemm("hi_makeABC" + self.doargs(*arg))

    def hi_maximize(self):
        self.callfemm("hi_maximize()")

    def hi_minimize(self):
        self.callfemm("hi_minimize()")

    def hi_mirror(self, x1, y1, x2, y2):
        self.callfemm(
            "hi_mirror("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def hi_mirror2(self, x1, y1, x2, y2, editaction):
        self.callfemm(
            "hi_mirror("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.numc(y2)
            + self.num(editaction)
            + ")"
        )

    def hi_modifyboundprop(self, *arg):
        self.callfemm("hi_modifyboundprop" + self.doargs(*arg))

    def hi_modifyconductorprop(self, *arg):
        self.callfemm("hi_modifyconductorprop" + self.doargs(*arg))

    def hi_modifymaterial(self, *arg):
        self.callfemm("hi_modifymaterial" + self.doargs(*arg))

    def hi_modifypointprop(self, *arg):
        self.callfemm("hi_modifypointprop" + self.doargs(*arg))

    def hi_moverotate(self, bx, by, shiftangle):
        self.callfemm(
            "hi_moverotate("
            + self.numc(bx)
            + self.numc(by)
            + self.num(shiftangle)
            + ")"
        )

    def hi_movetranslate(self, bx, by):
        self.callfemm("hi_movetranslate(" + self.numc(bx) + self.num(by) + ")")

    def hi_movetranslate2(self, bx, by, editaction):
        self.callfemm(
            "hi_movetranslate("
            + self.numc(bx)
            + self.numc(by)
            + self.num(editaction)
            + ")"
        )

    def hi_probdef(self, *arg):
        self.callfemm("hi_probdef" + self.doargs(*arg))

    def hi_purgemesh(self):
        self.callfemm("hi_purgemesh()")

    def hi_readdxf(self, docname):
        self.callfemm("print(hi_readdxf(" + self.quote(docname) + "))")

    def hi_refreshview(self):
        self.callfemm("hi_refreshview()")

    def hi_resize(self, nWidth, nHeight):
        self.callfemm("hi_resize(" + self.numc(nWidth) + self.num(nHeight) + ")")

    def hi_restore(self):
        self.callfemm("hi_restore()")

    def hi_saveas(self, fn):
        self.callfemm("hi_saveas(" + self.quote(self.fixpath(fn)) + ")")

    def hi_savebitmap(self, n):
        self.callfemm("hi_savebitmap(" + self.quote(n) + ")")

    def hi_savedxf(self, docname):
        self.callfemm_noeval("hi_savedxf(" + self.quote(docname) + ")")

    def hi_savemetafile(self, n):
        self.callfemm("hi_savemetafile(" + self.quote(n) + ")")

    def hi_scale(self, bx, by, sc):
        self.callfemm("hi_scale(" + self.numc(bx) + self.numc(by) + self.numc(sc) + ")")

    def hi_scale2(self, bx, by, sc, ea):
        self.callfemm(
            "hi_scale("
            + self.numc(bx)
            + self.numc(by)
            + self.numc(sc)
            + self.num(ea)
            + ")"
        )

    def hi_selectarcsegment(self, x, y):
        return self.callfemm("hi_selectarcsegment(" + self.numc(x) + self.num(y) + ")")

    def hi_selectcircle(self, *arg):
        self.callfemm("hi_selectcircle" + self.doargs(*arg))

    def hi_selectgroup(self, gr):
        self.callfemm("hi_selectgroup(" + self.num(gr) + ")")

    def hi_selectlabel(self, x, y):
        return self.callfemm("hi_selectlabel(" + self.numc(x) + self.num(y) + ")")

    def hi_selectnode(self, x, y):
        return self.callfemm("hi_selectnode(" + self.numc(x) + self.num(y) + ")")

    def hi_selectrectangle(self, *arg):
        self.callfemm("hi_selectrectangle" + self.doargs(*arg))

    def hi_selectsegment(self, x, y):
        return self.callfemm("hi_selectsegment(" + self.numc(x) + self.num(y) + ")")

    def hi_setarcsegmentprop(self, maxsegdeg, propname, hide, group, incond):
        self.callfemm(
            "hi_setarcsegmentprop("
            + self.numc(maxsegdeg)
            + self.quotec(propname)
            + self.numc(hide)
            + self.numc(group)
            + self.quote(incond)
            + ")"
        )

    def hi_setblockprop(self, blockname, automesh, meshsize, group):
        self.callfemm(
            "hi_setblockprop("
            + self.quotec(blockname)
            + self.numc(automesh)
            + self.numc(meshsize)
            + self.num(group)
            + ")"
        )

    def hi_seteditmode(self, editmode):
        self.callfemm("hi_seteditmode(" + self.quote(editmode) + ")")

    def hi_setfocus(self, docname):
        self.callfemm("hi_setfocus(" + self.quote(docname) + ")")

    def hi_setgrid(self, density, ptype):
        self.callfemm("hi_setgrid(" + self.numc(density) + self.quote(ptype) + ")")

    def hi_setgroup(self, n):
        return self.callfemm("hi_setgroup(" + self.num(n) + ")")

    def hi_setnodeprop(self, nodeprop, groupno, inconductor):
        self.callfemm(
            "hi_setnodeprop("
            + self.quotec(nodeprop)
            + self.numc(groupno)
            + self.quote(inconductor)
            + ")"
        )

    def hi_setsegmentprop(self, pn, es, am, hi, gr, inconductor):
        self.callfemm(
            "hi_setsegmentprop("
            + self.quotec(pn)
            + self.numc(es)
            + self.numc(am)
            + self.numc(hi)
            + self.numc(gr)
            + self.quote(inconductor)
            + ")"
        )

    def hi_showgrid(self):
        self.callfemm("hi_showgrid()")

    def hi_showmesh(self):
        self.callfemm("hi_showmesh()")

    def hi_shownames(self):
        self.callfemm("hi_shownames(1)")

    def hi_smartmesh(self, n):
        self.callfemm("hi_smartmesh(" + self.num(n) + ")")

    def hi_snapgridoff(self):
        self.callfemm('hi_gridsnap("off")')

    def hi_snapgridon(self):
        self.callfemm('hi_gridsnap("on")')

    def hi_zoom(self, x1, y1, x2, y2):
        self.callfemm(
            "hi_zoom("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def hi_zoomin(self):
        self.callfemm("hi_zoomin()")

    def hi_zoomnatural(self):
        self.callfemm("hi_zoomnatural()")

    def hi_zoomout(self):
        self.callfemm("hi_zoomout()")

    def hideconsole(self):
        self.callfemm("hideconsole()")

    def hidepointprops(self):
        self.callfemm("hidepointprops()")

    def ho_addcontour(self, x, y):
        self.callfemm("ho_addcontour(" + self.numc(x) + self.num(y) + ")")

    def ho_bendcontour(self, tta, dtta):
        self.callfemm("ho_bendcontour(" + self.numc(tta) + self.num(dtta) + ")")

    def ho_blockintegral(self, ptype):
        return self.callfemm("ho_blockintegral(" + self.num(ptype) + ")")

    def ho_clearblock(self):
        self.callfemm("ho_clearblock()")

    def ho_clearcontour(self):
        self.callfemm("ho_clearcontour()")

    def ho_close(self):
        self.callfemm("ho_close()")

    def ho_getconductorproperties(self, pname):
        return self.callfemm("ho_getconductorproperties(" + self.quote(pname) + ")")

    def ho_getelement(self, n):
        return self.callfemm("ho_getelement(" + self.num(n) + ")")

    def ho_getf(self, x, y):
        z = self.ho_getpointvalues(x, y)
        return [z[1], z[2]]

    def ho_getg(self, x, y):
        z = self.ho_getpointvalues(x, y)
        return [z[3], z[4]]

    def ho_getk(self, x, y):
        z = self.ho_getpointvalues(x, y)
        return [z[5], z[6]]

    def ho_getnode(self, n):
        return self.callfemm("ho_getnode(" + self.num(n) + ")")

    def ho_getpointvalues(self, x, y):
        z = self.callfemm("ho_getpointvalues(" + self.numc(x) + self.num(y) + ")")
        if len(z) > 0:
            return z
        return [0, 0, 0, 0, 0, 0, 0]

    def ho_getprobleminfo(self):
        return self.callfemm("ho_getprobleminfo()")

    def ho_gett(self, x, y):
        z = self.ho_getpointvalues(x, y)
        return z[0]

    def ho_groupselectblock(self, *arg):
        self.callfemm("ho_groupselectblock" + self.doargs(*arg))

    def ho_hidecontourplot(self):
        self.callfemm("ho_hidecontourplot()")

    def ho_hidedensityplot(self):
        self.callfemm("ho_hidedensityplot()")

    def ho_hidegrid(self):
        self.callfemm("ho_hidegrid()")

    def ho_hidemesh(self):
        self.callfemm("ho_hidemesh()")

    def ho_hidenames(self):
        self.callfemm("ho_shownames(0)")

    def ho_hidepoints(self):
        self.callfemm("ho_hidepoints()")

    def ho_lineintegral(self, ptype):
        return self.callfemm("ho_lineintegral(" + self.num(ptype) + ")")

    def ho_makeplot(self, *arg):
        self.callfemm("ho_makeplot" + self.doargs(*arg))

    def ho_maximize(self):
        self.callfemm("ho_maximize()")

    def ho_minimize(self):
        self.callfemm("ho_minimize()")

    def ho_numelements(self):
        return self.callfemm("ho_numelements()")

    def ho_numnodes(self):
        return self.callfemm("ho_numnodes()")

    def ho_refreshview(self):
        self.callfemm("ho_refreshview()")

    def ho_reload(self):
        self.callfemm("ho_reload()")

    def ho_resize(self, nWidth, nHeight):
        self.callfemm("ho_resize(" + self.numc(nWidth) + self.num(nHeight) + ")")

    def ho_restore(self):
        self.callfemm("ho_restore()")

    def ho_savebitmap(self, fn):
        self.callfemm("ho_savebitmap(" + self.quote(self.fixpath(fn)) + ")")

    def ho_savemetafile(self, fn):
        self.callfemm("ho_savemetafile(" + self.quote(self.fixpath(fn)) + ")")

    def ho_selectblock(self, x, y):
        self.callfemm("ho_selectblock(" + self.numc(x) + self.num(y) + ")")

    def ho_selectpoint(self, x, y):
        self.callfemm("ho_selectpoint(" + self.numc(x) + self.num(y) + ")")

    def ho_seteditmode(self, mode):
        self.callfemm("ho_seteditmode(" + self.quote(mode) + ")")

    def ho_setgrid(self, density, ptype):
        self.callfemm("ho_setgrid(" + self.numc(density) + self.quote(ptype) + ")")

    def ho_showcontourplot(self, numcontours, al, au):
        self.callfemm(
            "ho_showcontourplot("
            + self.numc(numcontours)
            + self.numc(al)
            + self.num(au)
            + ")"
        )

    def ho_showdensityplot(self, legend, gscale, ptype, bu, bl):
        self.callfemm(
            "ho_showdensityplot("
            + self.numc(legend)
            + self.numc(gscale)
            + self.numc(ptype)
            + self.numc(bu)
            + self.num(bl)
            + ")"
        )

    def ho_showgrid(self):
        self.callfemm("ho_showgrid()")

    def ho_showmesh(self):
        self.callfemm("ho_showmesh()")

    def ho_shownames(self):
        self.callfemm("ho_shownames(1)")

    def ho_showpoints(self):
        self.callfemm("ho_showpoints()")

    def ho_showvectorplot(self, *arg):
        self.callfemm("ho_showvectorplot" + self.doargs(*arg))

    def ho_smooth(self, flag):
        self.callfemm("ho_smooth(" + self.quote(flag) + ")")

    def ho_smoothoff(self):
        self.callfemm('ho_smooth("off")')

    def ho_smoothon(self):
        self.callfemm('ho_smooth("on")')

    def ho_snapgrid(self, flag):
        self.callfemm("ho_gridsnap(" + self.quote(flag) + ")")

    def ho_snapgridoff(self):
        self.callfemm('ho_gridsnap("off")')

    def ho_snapgridon(self):
        self.callfemm('ho_gridsnap("on")')

    def ho_zoom(self, x1, y1, x2, y2):
        self.callfemm(
            "ho_zoom("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def ho_zoomin(self):
        self.callfemm("ho_zoomin()")

    def ho_zoomnatural(self):
        self.callfemm("ho_zoomnatural()")

    def ho_zoomout(self):
        self.callfemm("ho_zoomout()")

    def IEC(self, iec):
        return 7.959159641581004 * exp(-0.11519673572274754 * iec)

    def main_maximize(self):
        self.callfemm("main_maximize()")

    def main_minimize(self):
        self.callfemm("main_minimize()")

    def main_resize(self, nWidth, nHeight):
        self.callfemm("main_resize(" + self.numc(nWidth) + self.num(nHeight) + ")")

    def messagebox(self, msg):
        self.callfemm("messagebox(" + self.quote(msg) + ")")

    def mi_addarc(self, x1, y1, x2, y2, angle, maxseg):
        self.callfemm(
            "mi_addarc("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.numc(y2)
            + self.numc(angle)
            + self.num(maxseg)
            + ")"
        )

    def mi_addbhpoint(self, name, b, h):
        self.callfemm(
            "mi_addbhpoint(" + self.quotec(name) + self.numc(b) + self.num(h) + ")"
        )

    def mi_addblocklabel(self, x, y):
        self.callfemm("mi_addblocklabel(" + self.numc(x) + self.num(y) + ")")

    def mi_addboundprop(self, *arg):
        self.callfemm("mi_addboundprop" + self.doargs(*arg))

    def mi_addcircprop(self, pname, ic, ptype):
        self.callfemm(
            "mi_addcircprop("
            + self.quotec(pname)
            + self.numc(ic)
            + self.num(ptype)
            + ")"
        )

    def mi_addmaterial(self, *arg):
        self.callfemm("mi_addmaterial" + self.doargs(*arg))

    def mi_addnode(self, x, y):
        self.callfemm("mi_addnode(" + self.numc(x) + self.num(y) + ")")

    def mi_addpointprop(self, pname, ap, jp):
        self.callfemm(
            "mi_addpointprop(" + self.quotec(pname) + self.numc(ap) + self.num(jp) + ")"
        )

    def mi_addsegment(self, x1, y1, x2, y2):
        self.callfemm(
            "mi_addsegment("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def mi_analyze(self, *arg):
        self.callfemm("mi_analyze" + self.doargs(*arg))

    def mi_analyse(self, n):
        self.mi_analyze(n)

    def mi_attachdefault(self):
        self.callfemm("mi_attachdefault()")

    def mi_attachouterspace(self):
        self.callfemm("mi_attachouterspace()")

    def mi_clearbhpoints(self, n):
        self.callfemm("mi_clearbhpoints(" + self.quote(n) + ")")

    def mi_clearselected(self):
        self.callfemm("mi_clearselected()")

    def mi_close(self):
        self.callfemm("mi_close()")

    def mi_copyrotate(self, bx, by, angle, copies):
        self.callfemm(
            "mi_copyrotate("
            + self.numc(bx)
            + self.numc(by)
            + self.numc(angle)
            + self.num(copies)
            + ")"
        )

    def mi_copyrotate2(self, bx, by, angle, copies, editaction):
        self.callfemm(
            "mi_copyrotate("
            + self.numc(bx)
            + self.numc(by)
            + self.numc(angle)
            + self.numc(copies)
            + self.num(editaction)
            + ")"
        )

    def mi_copytranslate(self, bx, by, copies):
        self.callfemm(
            "mi_copytranslate(" + self.numc(bx) + self.numc(by) + self.num(copies) + ")"
        )

    def mi_copytranslate2(self, bx, by, copies, editaction):
        self.callfemm(
            "mi_copytranslate("
            + self.numc(bx)
            + self.numc(by)
            + self.numc(copies)
            + self.num(editaction)
            + ")"
        )

    def mi_createmesh(self):
        return self.callfemm("mi_createmesh()")

    def mi_createradius(self, x, y, r):
        self.callfemm(
            "mi_createradius(" + self.numc(x) + self.numc(y) + self.num(r) + ")"
        )

    def mi_defineouterspace(self, Zo, Ro, Ri):
        self.callfemm(
            "mi_defineouterspace(" + self.numc(Zo) + self.numc(Ro) + self.num(Ri) + ")"
        )

    def mi_deleteboundprop(self, n):
        self.callfemm("mi_deleteboundprop(" + self.quote(n) + ")")

    def mi_deletecircuit(self, n):
        self.callfemm("mi_deletecircuit(" + self.quote(n) + ")")

    def mi_deletematerial(self, n):
        self.callfemm("mi_deletematerial(" + self.quote(n) + ")")

    def mi_deletepointprop(self, n):
        self.callfemm("mi_deletepointprop(" + self.quote(n) + ")")

    def mi_deleteselected(self):
        self.callfemm("mi_deleteselected()")

    def mi_deleteselectedarcsegments(self):
        self.callfemm("mi_deleteselectedarcsegments()")

    def mi_deleteselectedlabels(self):
        self.callfemm("mi_deleteselectedlabels()")

    def mi_deleteselectednodes(self):
        self.callfemm("mi_deleteselectednodes()")

    def mi_deleteselectedsegments(self):
        self.callfemm("mi_deleteselectedsegments()")

    def mi_detachdefault(self):
        self.callfemm("mi_detachdefault()")

    def mi_detachouterspace(self):
        self.callfemm("mi_detachouterspace()")

    def mi_drawarc(self, x1, y1, x2, y2, angle, maxseg):
        self.mi_addnode(x1, y1)
        self.mi_addnode(x2, y2)
        self.mi_addarc(x1, y1, x2, y2, angle, maxseg)

    def mi_drawline(self, x1, y1, x2, y2):
        self.mi_addnode(x1, y1)
        self.mi_addnode(x2, y2)
        self.mi_addsegment(x1, y1, x2, y2)

    def mi_drawrectangle(self, x1, y1, x2, y2):
        self.mi_drawline(x1, y1, x2, y1)
        self.mi_drawline(x2, y1, x2, y2)
        self.mi_drawline(x2, y2, x1, y2)
        self.mi_drawline(x1, y2, x1, y1)

    def mi_getmaterial(self, matname):
        self.callfemm("mi_getmaterial(" + self.quote(matname) + ")")

    def mi_hidegrid(self):
        self.callfemm("mi_hidegrid()")

    def mi_hidenames(self):
        self.callfemm("mi_shownames(0)")

    def mi_loadsolution(self):
        self.callfemm("mi_loadsolution()")

    def mi_makeABC(self, *arg):
        self.callfemm("mi_makeABC" + self.doargs(*arg))

    def mi_maximize(self):
        self.callfemm("mi_maximize()")

    def mi_minimize(self):
        self.callfemm("mi_minimize()")

    def mi_mirror(self, x1, y1, x2, y2):
        self.callfemm(
            "mi_mirror("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def mi_mirror2(self, x1, y1, x2, y2, editaction):
        self.callfemm(
            "mi_mirror("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.numc(y2)
            + self.num(editaction)
            + ")"
        )

    def mi_modifyboundprop(self, *arg):
        self.callfemm("mi_modifyboundprop" + self.doargs(*arg))

    def mi_modifycircprop(self, *arg):
        self.callfemm("mi_modifycircprop" + self.doargs(*arg))

    def mi_modifymaterial(self, *arg):
        self.callfemm("mi_modifymaterial" + self.doargs(*arg))

    def mi_modifypointprop(self, *arg):
        self.callfemm("mi_modifypointprop" + self.doargs(*arg))

    def mi_moverotate(self, bx, by, shiftangle):
        self.callfemm(
            "mi_moverotate("
            + self.numc(bx)
            + self.numc(by)
            + self.num(shiftangle)
            + ")"
        )

    def mi_movetranslate(self, bx, by):
        self.callfemm("mi_movetranslate(" + self.numc(bx) + self.num(by) + ")")

    def mi_movetranslate2(self, bx, by, editaction):
        self.callfemm(
            "mi_movetranslate("
            + self.numc(bx)
            + self.numc(by)
            + self.num(editaction)
            + ")"
        )

    def mi_probdef(self, *arg):
        self.callfemm("mi_probdef" + self.doargs(*arg))

    def mi_purgemesh(self):
        self.callfemm("mi_purgemesh()")

    def mi_readdxf(self, docname):
        self.callfemm("print(mi_readdxf(" + self.quote(docname) + "))")

    def mi_readdxf2(self, docname, tol):
        self.callfemm(
            "print(mi_readdxf(" + self.quote(docname) + ", " + str(tol) + "))"
        )

    def mi_refreshview(self):
        self.callfemm("mi_refreshview()")

    def mi_resize(self, nWidth, nHeight):
        self.callfemm("mi_resize(" + self.numc(nWidth) + self.num(nHeight) + ")")

    def mi_restore(self):
        self.callfemm("mi_restore()")

    def mi_saveas(self, fn):
        self.callfemm("mi_saveas(" + self.quote(self.fixpath(fn)) + ")")

    def mi_savebitmap(self, n):
        self.callfemm("mi_savebitmap(" + self.quote(n) + ")")

    def mi_savedxf(self, docname):
        self.callfemm_noeval("mi_savedxf(" + self.quote(docname) + ")")

    def mi_savedxf2(self, docname, tol):
        self.callfemm(
            "print(mi_savedxf(" + self.quote(docname) + ", " + str(tol) + "))"
        )

    def mi_savemetafile(self, n):
        self.callfemm("mi_savemetafile(" + self.quote(n) + ")")

    def mi_scale(self, bx, by, sc):
        self.callfemm("mi_scale(" + self.numc(bx) + self.numc(by) + self.numc(sc) + ")")

    def mi_scale2(self, bx, by, sc, ea):
        self.callfemm(
            "mi_scale("
            + self.numc(bx)
            + self.numc(by)
            + self.numc(sc)
            + self.num(ea)
            + ")"
        )

    def mi_selectarcsegment(self, x, y):
        return self.callfemm("mi_selectarcsegment(" + self.numc(x) + self.num(y) + ")")

    def mi_selectcircle(self, *arg):
        self.callfemm("mi_selectcircle" + self.doargs(*arg))

    def mi_selectgroup(self, gr):
        self.callfemm("mi_selectgroup(" + self.num(gr) + ")")

    def mi_selectlabel(self, x, y):
        return self.callfemm("mi_selectlabel(" + self.numc(x) + self.num(y) + ")")

    def mi_selectnode(self, x, y):
        return self.callfemm("mi_selectnode(" + self.numc(x) + self.num(y) + ")")

    def mi_selectrectangle(self, *arg):
        self.callfemm("mi_selectrectangle" + self.doargs(*arg))

    def mi_selectsegment(self, x, y):
        return self.callfemm("mi_selectsegment(" + self.numc(x) + self.num(y) + ")")

    def mi_setarcsegmentprop(self, maxsegdeg, propname, hide, group):
        self.callfemm(
            "mi_setarcsegmentprop("
            + self.numc(maxsegdeg)
            + self.quotec(propname)
            + self.numc(hide)
            + self.num(group)
            + ")"
        )

    def mi_setblockprop(self, *arg):
        self.callfemm("mi_setblockprop" + self.doargs(*arg))

    def mi_setcurrent(self, name, x):
        self.mi_modifycircprop(name, 1, x)

    def mi_seteditmode(self, editmode):
        self.callfemm("mi_seteditmode(" + self.quote(editmode) + ")")

    def mi_setfocus(self, docname):
        self.callfemm("mi_setfocus(" + self.quote(docname) + ")")

    def mi_setgrid(self, density, ptype):
        self.callfemm("mi_setgrid(" + self.numc(density) + self.quote(ptype) + ")")

    def mi_setgroup(self, n):
        return self.callfemm("mi_setgroup(" + self.num(n) + ")")

    def mi_setnodeprop(self, nodeprop, groupno):
        self.callfemm(
            "mi_setnodeprop(" + self.quotec(nodeprop) + self.num(groupno) + ")"
        )

    def mi_setprevious(self, *arg):
        self.callfemm("mi_setprevious" + self.doargs(*arg))

    def mi_setsegmentprop(self, pn, es, am, hi, gr):
        self.callfemm(
            "mi_setsegmentprop("
            + self.quotec(pn)
            + self.numc(es)
            + self.numc(am)
            + self.numc(hi)
            + self.num(gr)
            + ")"
        )

    def mi_showgrid(self):
        self.callfemm("mi_showgrid()")

    def mi_showmesh(self):
        self.callfemm("mi_showmesh()")

    def mi_shownames(self):
        self.callfemm("mi_shownames(1)")

    def mi_smartmesh(self, n):
        self.callfemm("mi_smartmesh(" + self.num(n) + ")")

    def mi_snapgridoff(self):
        self.callfemm('mi_gridsnap("off")')

    def mi_snapgridon(self):
        self.callfemm('mi_gridsnap("on")')

    def mi_zoom(self, x1, y1, x2, y2):
        self.callfemm(
            "mi_zoom("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def mi_zoomin(self):
        self.callfemm("mi_zoomin()")

    def mi_zoomnatural(self):
        self.callfemm("mi_zoomnatural()")

    def mi_zoomout(self):
        self.callfemm("mi_zoomout()")

    def mo_addcontour(self, x, y):
        self.callfemm("mo_addcontour(" + self.numc(x) + self.num(y) + ")")

    def mo_bendcontour(self, tta, dtta):
        self.callfemm("mo_bendcontour(" + self.numc(tta) + self.num(dtta) + ")")

    def mo_blockintegral(self, ptype):
        return self.callfemm("mo_blockintegral(" + self.num(ptype) + ")")

    def mo_clearblock(self):
        self.callfemm("mo_clearblock()")

    def mo_clearcontour(self):
        self.callfemm("mo_clearcontour()")

    def mo_close(self):
        self.callfemm("mo_close()")

    def mo_gapintegral(self, bdryname, inttype):
        return self.callfemm(
            "mo_gapintegral(" + self.quotec(bdryname) + self.num(inttype) + ")"
        )

    def mo_geta(self, x, y):
        z = self.mo_getpointvalues(x, y)
        return z[0]

    def mo_getb(self, x, y):
        z = self.mo_getpointvalues(x, y)
        return [z[1], z[2]]

    def mo_getcircuitproperties(self, name):
        return self.callfemm("mo_getcircuitproperties(" + self.quote(name) + ")")

    def mo_getconductivity(self, x, y):
        z = self.mo_getpointvalues(x, y)
        return z[3]

    def mo_getelement(self, n):
        return self.callfemm("mo_getelement(" + self.num(n) + ")")

    def mo_getenergydensity(self, x, y):
        z = self.mo_getpointvalues(x, y)
        return z[4]

    def mo_getfill(self, x, y):
        z = self.mo_getpointvalues(x, y)
        return z[13]

    def mo_getgapa(self, bdryname, angle):
        return self.callfemm(
            "mo_getgapa(" + self.quotec(bdryname) + self.num(angle) + ")"
        )

    def mo_getgapb(self, bdryname, angle):
        return self.callfemm(
            "mo_getgapb(" + self.quotec(bdryname) + self.num(angle) + ")"
        )

    def mo_getgapharmonics(self, *arg):
        return self.callfemm("mo_getgapharmonics" + self.doargs(*arg))

    def mo_geth(self, x, y):
        z = self.mo_getpointvalues(x, y)
        return [z[5], z[6]]

    def mo_getj(self, x, y):
        z = self.mo_getpointvalues(x, y)
        return z[7] + z[8]

    def mo_getmu(self, x, y):
        z = self.mo_getpointvalues(x, y)
        return [z[9], z[10]]

    def mo_getnode(self, n):
        return self.callfemm("mo_getnode(" + self.num(n) + ")")

    def mo_getpe(self, x, y):
        z = self.mo_getpointvalues(x, y)
        return z[11]

    def mo_getph(self, x, y):
        z = self.mo_getpointvalues(x, y)
        return z[12]

    def mo_getpointvalues(self, x, y):
        z = self.callfemm("mo_getpointvalues(" + self.numc(x) + self.num(y) + ")")
        if len(z) > 0:
            return z
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def mo_getprobleminfo(self):
        return self.callfemm("mo_getprobleminfo()")

    def mo_groupselectblock(self, *arg):
        self.callfemm("mo_groupselectblock" + self.doargs(*arg))

    def mo_hidecontourplot(self):
        self.callfemm("mo_hidecontourplot()")

    def mo_hidedensityplot(self):
        self.callfemm("mo_hidedensityplot()")

    def mo_hidegrid(self):
        self.callfemm("mo_hidegrid()")

    def mo_hidemesh(self):
        self.callfemm("mo_hidemesh()")

    def mo_hidenames(self):
        self.callfemm("mo_shownames(0)")

    def mo_hidepoints(self):
        self.callfemm("mo_hidepoints()")

    def mo_lineintegral(self, ptype):
        return self.callfemm("mo_lineintegral(" + self.num(ptype) + ")")

    def mo_makeplot(self, *arg):
        self.callfemm("mo_makeplot" + self.doargs(*arg))

    def mo_maximize(self):
        self.callfemm("mo_maximize()")

    def mo_minimize(self):
        self.callfemm("mo_minimize()")

    def mo_numelements(self):
        return self.callfemm("mo_numelements()")

    def mo_numnodes(self):
        return self.callfemm("mo_numnodes()")

    def mo_refreshview(self):
        self.callfemm("mo_refreshview()")

    def mo_reload(self):
        self.callfemm("mo_reload()")

    def mo_resize(self, nWidth, nHeight):
        self.callfemm("mo_resize(" + self.numc(nWidth) + self.num(nHeight) + ")")

    def mo_restore(self):
        self.callfemm("mo_restore()")

    def mo_savebitmap(self, fn):
        self.callfemm("mo_savebitmap(" + self.quote(self.fixpath(fn)) + ")")

    def mo_savemetafile(self, fn):
        self.callfemm("mo_savemetafile(" + self.quote(self.fixpath(fn)) + ")")

    def mo_selectblock(self, x, y):
        self.callfemm("mo_selectblock(" + self.numc(x) + self.num(y) + ")")

    def mo_selectpoint(self, x, y):
        self.callfemm("mo_selectpoint(" + self.numc(x) + self.num(y) + ")")

    def mo_seteditmode(self, mode):
        self.callfemm("mo_seteditmode(" + self.quote(mode) + ")")

    def mo_setgrid(self, density, ptype):
        self.callfemm("mo_setgrid(" + self.numc(density) + self.quote(ptype) + ")")

    def mo_setweightingscheme(self, n):
        self.callfemm("mo_setweightingscheme(" + self.num(n) + ")")

    def mo_showcontourplot(self, numcontours, al, au, ptype):
        self.callfemm(
            "mo_showcontourplot("
            + self.numc(numcontours)
            + self.numc(al)
            + self.numc(au)
            + self.quote(ptype)
            + ")"
        )

    def mo_showdensityplot(self, legend, gscale, bu, bl, ptype):
        self.callfemm(
            "mo_showdensityplot("
            + self.numc(legend)
            + self.numc(gscale)
            + self.numc(bu)
            + self.numc(bl)
            + self.quote(ptype)
            + ")"
        )

    def mo_showgrid(self):
        self.callfemm("mo_showgrid()")

    def mo_showmesh(self):
        self.callfemm("mo_showmesh()")

    def mo_shownames(self):
        self.callfemm("mo_shownames(1)")

    def mo_showpoints(self):
        self.callfemm("mo_showpoints()")

    def mo_showvectorplot(self, *arg):
        self.callfemm("mo_showvectorplot" + self.doargs(*arg))

    def mo_smooth(self, flag):
        self.callfemm("mo_smooth(" + self.quote(flag) + ")")

    def mo_smoothoff(self):
        self.callfemm('mo_smooth("off")')

    def mo_smoothon(self):
        self.callfemm('mo_smooth("on")')

    def mo_snapgrid(self, flag):
        self.callfemm("mo_gridsnap(" + self.quote(flag) + ")")

    def mo_snapgridoff(self):
        self.callfemm('mo_gridsnap("off")')

    def mo_snapgridon(self):
        self.callfemm('mo_gridsnap("on")')

    def mo_zoom(self, x1, y1, x2, y2):
        self.callfemm(
            "mo_zoom("
            + self.numc(x1)
            + self.numc(y1)
            + self.numc(x2)
            + self.num(y2)
            + ")"
        )

    def mo_zoomin(self):
        self.callfemm("mo_zoomin()")

    def mo_zoomnatural(self):
        self.callfemm("mo_zoomnatural()")

    def mo_zoomout(self):
        self.callfemm("mo_zoomout()")

    def opendocument(self, fn):
        self.callfemm("open(" + self.quote(self.fixpath(fn)) + ")")

    def prompt(self, msg):
        return self.callfemm("prompt(" + self.quote(msg) + ")")

    def showconsole(self):
        self.callfemm("showconsole()")

    def showpointprops(self):
        self.callfemm("showpointprops()")

    def smartmesh(self, n):
        self.callfemm("smartmesh(" + self.num(n) + ")")
