# -*- coding: utf-8 -*-
"""File generated according to WImportExcel/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Tools.WImport.WImportExcel.Ui_WImportExcel import Ui_WImportExcel


class Gen_WImportExcel(Ui_WImportExcel):
    def setupUi(self, WImportExcel):
        """Abstract class to update the widget according to the csv doc"""
        Ui_WImportExcel.setupUi(self, WImportExcel)
        # Setup of in_range
        txt = self.tr(
            """list of Excel column letters and column ranges (e.g. "A:E" or "A,C,E:F")"""
        )
        self.in_range.setWhatsThis(txt)
        self.in_range.setToolTip(txt)

        # Setup of le_range
        txt = self.tr(
            """list of Excel column letters and column ranges (e.g. "A:E" or "A,C,E:F")"""
        )
        self.le_range.setWhatsThis(txt)
        self.le_range.setToolTip(txt)
