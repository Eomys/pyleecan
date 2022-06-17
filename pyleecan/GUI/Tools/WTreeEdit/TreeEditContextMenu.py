# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QFileDialog, QMessageBox, QMenu, QInputDialog

from ....Functions.Load.import_class import import_class
from ....Functions.load import load

from ..ClassTreeWidget import ClassTreeWidget

FILE_TYPES = "Json (*.json);;HDF5 (*.h5)"


class TreeEditContextMenu(QMenu):
    def __init__(self, obj_dict, parent):
        super(TreeEditContextMenu, self).__init__()
        self._parent = parent  # parent widget
        self._obj_dict = obj_dict

        is_root = False
        if self._obj_dict["parent"] is None:
            is_root = True

        # === Common Actions ====
        # info
        info = self.addAction(self._obj_dict["property"] + " - Property")
        self.addSeparator()

        # new / load
        actionNewObj = self.addAction("New Object")
        actionImportObj = self.addAction("Import Object")
        self.addSeparator()

        # save / set none
        actionSaveObj = self.addAction("Save Object" if is_root else "Export Object")
        actionSetNone = self.addAction("Set to None")

        # === Filter Actions Aviability ===
        obj = self._obj_dict["obj"]
        ref_type = self._obj_dict["ref_typ"]

        info.setEnabled(False)

        if ref_type not in parent.class_dict.keys():
            actionSaveObj.setEnabled(False)

        if obj is None:
            actionSetNone.setEnabled(False)
            actionSaveObj.setEnabled(False)

        if is_root:
            actionNewObj.setEnabled(False)
            actionSetNone.setEnabled(False)
            actionImportObj.setEnabled(True)
            actionSaveObj.setEnabled(True)

        if isinstance(obj, (list, dict)) or ref_type in ["list", "dict"]:
            actionNewObj.setEnabled(False)
            actionSaveObj.setEnabled(False)
            actionImportObj.setEnabled(False)

        if parent.isListType(ref_type) or parent.isDictType(ref_type):
            self.addSeparator()
            actionAppendElement = self.addAction("Append Element")
            actionAppendElement.triggered.connect(self.appendElement)

        if obj_dict["parent_typ"] == "list":
            self.addSeparator()
            actionRemoveElement = self.addAction("Remove Element")
            actionRemoveElement.triggered.connect(self.removeElement)
            actionInsertElement = self.addAction("Insert Element")
            actionInsertElement.triggered.connect(self.insertElement)

        if obj_dict["parent_typ"] == "dict":
            self.addSeparator()
            actionRemoveElement = self.addAction("Remove Element")
            actionRemoveElement.triggered.connect(self.removeElement)

        # === Common Signals ===
        actionNewObj.triggered.connect(self.newObject)
        actionSaveObj.triggered.connect(self.saveObject)
        actionImportObj.triggered.connect(self.loadObject)
        actionSetNone.triggered.connect(self.setNone)

    def setProp(self, value):
        """
        Method to set the object, i.e. the respective parents property, list index or
        dict key respectively.
        """
        parent_obj = self._obj_dict["parent"]
        if isinstance(parent_obj, (list, dict)):
            parent_obj[self._obj_dict["index"]] = value
        else:
            setattr(parent_obj, self._obj_dict["property"], value)

        return True

    def setNone(self):
        """Set respective pyleecan class property to None."""
        self.setProp(None)

    def getNewObject(self, ref_type=None):
        """Get a new object from the user."""
        keys = [self._obj_dict["ref_typ"]] if ref_type is None else [ref_type]
        dialog = ClassTreeWidget(keys)
        if dialog.exec():
            cls_name = dialog.getSelectedClass()
            new_obj = import_class("pyleecan.Classes", cls_name, "")()
            return new_obj

    def newObject(self):
        """Get a new object from the user and set it to the respective property."""
        new_obj = self.getNewObject()
        if new_obj is not None:
            self.setProp(new_obj)

    def saveObject(self):
        """Slot for saving the data."""
        path = ""
        path = QFileDialog.getSaveFileName(self, self.tr("Save file"), path, FILE_TYPES)
        if path[0] == "":
            return False
        self._obj_dict["obj"].save(path[0])
        if self._obj_dict["parent"] is None:
            self._parent.setSaveNeeded(False)
        return True

    def loadObject(self):
        """Load an object."""
        if self._obj_dict["parent"] is None:
            reply = QMessageBox.warning(
                self,
                "Are you sure?",
                "The reference to the 'Design' machine will be lost, if an object is "
                + "imported. \nSwitching to 'Design' will restore the reference "
                + "but also replace the imported object without any warning.",
                QMessageBox.Ok | QMessageBox.Cancel,
                QMessageBox.Cancel,
            )
            if reply != QMessageBox.Ok:
                return

        # Ask the user to select a .json, h5, ... file to load
        path = ""
        load_path = str(
            QFileDialog.getOpenFileName(self, self.tr("Load file"), path, FILE_TYPES)[0]
        )
        if load_path != "":
            try:
                obj = load(load_path)

            except Exception as e:
                msg = self.tr("While loading file the follow error occured:\n")
                QMessageBox().critical(
                    self, self.tr("Error"), msg + f"{type(e).__name__}: {str(e)}"
                )
                return

            if self._obj_dict["parent"] is not None:
                obj_type = type(obj).__name__
                # get the allowed object types for this property
                ref_type = self._obj_dict["ref_typ"]
                daughter_types = self._parent.class_dict[ref_type]["daughters"]
                if obj_type == ref_type or obj_type in daughter_types:
                    print(f"Loaded class {type(obj).__name__}")
                    self.setProp(obj)
                else:
                    msg = f"Wrong object type '{obj_type}', '{ref_type}' expected."
                    QMessageBox().critical(self, self.tr("Error"), self.tr(msg))

            else:
                self._parent.update(obj)

    def appendElement(self):
        """Append an element to the list."""
        ref_type = self._obj_dict["ref_typ"]
        if not (self._parent.isListType(ref_type) or self._parent.isDictType(ref_type)):
            return  # this should not happen

        ref_type = ref_type[1:-1]

        obj = self._obj_dict["obj"]
        # get the new object
        new_obj = self.getNewObject(ref_type=ref_type)
        if new_obj is None:
            return

        # append the new object to the list
        if self._parent.isListType(self._obj_dict["ref_typ"]):
            if obj is None:
                self.setProp([])
                obj = getattr(self._obj_dict["parent"], self._obj_dict["property"])
            obj.append(new_obj)
        elif self._parent.isDictType(self._obj_dict["ref_typ"]):
            # get a valid dict key for the new object from user
            valid = False
            while not valid:
                key, ok = QInputDialog.getText(
                    self, self.tr("Input Dialog"), self.tr("Key:")
                )
                if ok:
                    if key in obj.keys():
                        msg = self.tr("Key already exists, please choose another one.")
                        QMessageBox().critical(self, self.tr("Error"), self.tr(msg))
                    else:
                        try:
                            if obj is None:
                                self.setProp({})
                                obj = getattr(
                                    self._obj_dict["parent"], self._obj_dict["property"]
                                )
                            obj[key] = new_obj
                            valid = True
                        except Exception as e:
                            msg = self.tr(
                                "While setting the key the follow error occured:\n"
                            )
                            QMessageBox().critical(
                                self,
                                self.tr("Error"),
                                msg + f"{type(e).__name__}: {str(e)}",
                            )
                else:
                    # user canceled
                    return

    def removeElement(self):
        """Remove an element from the list."""
        parent = self._obj_dict["parent"]
        if self._obj_dict["parent_typ"] == "list":
            parent.pop(self._obj_dict["index"])
        elif self._obj_dict["parent_typ"] == "dict":
            del parent[self._obj_dict["index"]]

    def insertElement(self):
        """Insert an element in the list."""
        if not self._obj_dict["parent_typ"] == "list":
            return

        parent = self._obj_dict["parent"]
        # get the new object
        new_obj = self.getNewObject()
        if new_obj is None:
            return

        # insert the new object to the list
        parent.insert(self._obj_dict["index"], new_obj)
