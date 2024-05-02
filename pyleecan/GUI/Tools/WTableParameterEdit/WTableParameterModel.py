from qtpy.QtCore import QSize, Qt, QAbstractTableModel, Signal
from qtpy.QtGui import QBrush, QColor, QFont

from ....Classes._ClassInfo import ClassInfo


NAME_KEY = "name"
VALUE_KEY = "value"
UNIT_KEY = "unit"
DESC_KEY = "description"
TYPE_KEY = "type"

NOT_AVAILABLE = "na"

SUPPORTED_TYPES = (int, float, bool, str)
SUPPORTED_TYPE_NAMES = [type(cls()).__name__ for cls in SUPPORTED_TYPES]

# TODO find better way to highlight non editable cells but with background color
#      since this will conflict with style sheets
COL_LIGHT_GRAY = QColor(211, 211, 211, 255)
COL_GRAY = QColor(127, 127, 127, 255)

COL_WHITE_SMOKE = QColor(245, 245, 245, 255)

HEADER_HEIGHT_HINT = 20


class WTableParameterModel(QAbstractTableModel):
    dataChanged = Signal()

    def __init__(self, obj):
        super(WTableParameterModel, self).__init__()
        self._class_dict = ClassInfo().get_dict()
        self._obj = obj
        self._propList = []
        self._items = [NAME_KEY, VALUE_KEY, UNIT_KEY, DESC_KEY]

        self.generatePropList(obj)

    def generatePropList(self, obj):
        if self.isPyleecanType(obj):
            props = self._class_dict[type(obj).__name__]["properties"]
            for _propDict in props:
                value = getattr(obj, _propDict["name"])
                # convert propsDict
                propDict = dict()
                propDict[NAME_KEY] = _propDict["name"]
                propDict[TYPE_KEY] = _propDict["type"]
                propDict[DESC_KEY] = _propDict["desc"]
                propDict[UNIT_KEY] = _propDict["unit"]
                if isinstance(value, SUPPORTED_TYPES):
                    propDict["_editable_"] = True
                elif propDict[TYPE_KEY] in SUPPORTED_TYPE_NAMES and value is None:
                    propDict["_editable_"] = True
                else:
                    propDict["_editable_"] = False
                self._propList.append(propDict)

        elif hasattr(obj, "as_dict"):
            objDict = obj.as_dict()
            for key in objDict.keys():
                if not key.startswith("_"):
                    value = getattr(obj, key)
                    typ = type(value).__name__
                    propDict = dict()
                    propDict[NAME_KEY] = key
                    propDict[TYPE_KEY] = typ
                    if isinstance(value, SUPPORTED_TYPES) or value is None:
                        propDict["_editable_"] = True
                    else:
                        propDict["_editable_"] = False
                    self._propList.append(propDict)

    def data(self, index, role=Qt.UserRole):
        propDict = self._propList[index.row()]
        item = self._items[index.column()]

        if not item in propDict.keys() and not item == VALUE_KEY:
            return None

        if role == Qt.DisplayRole:
            if item == VALUE_KEY and propDict["_editable_"]:
                return str(getattr(self._obj, propDict[NAME_KEY]))  # get actual value
            elif item == VALUE_KEY and not propDict["_editable_"]:
                return NOT_AVAILABLE
            return str(propDict[item])

        elif role == Qt.EditRole:
            value = getattr(self._obj, propDict[NAME_KEY])  # get actual value
            if value is None:
                return ""
            if propDict[TYPE_KEY] == "bool":
                return value
            if propDict[TYPE_KEY] == "int":
                return value
            return str(value)

        elif role == Qt.FontRole:
            if item == VALUE_KEY and getattr(self._obj, propDict[NAME_KEY]) is None:
                font = QFont()
                font.setItalic(True)
                return font

        elif role == Qt.TextAlignmentRole:
            if item == NAME_KEY or item == VALUE_KEY:
                return int(Qt.AlignRight | Qt.AlignVCenter)

        elif role == Qt.ToolTipRole:
            if item == NAME_KEY or item == DESC_KEY:
                return propDict[DESC_KEY] if DESC_KEY in propDict else None
            elif item == VALUE_KEY:
                return propDict[TYPE_KEY] if TYPE_KEY in propDict else None

        elif role == Qt.BackgroundColorRole:
            if item != VALUE_KEY:
                return QBrush(COL_WHITE_SMOKE)

        elif role == Qt.UserRole:
            if item == VALUE_KEY:
                return getattr(self._obj, propDict[NAME_KEY])
            return propDict[item]

    def setData(self, index, value_str, role):
        if role == Qt.EditRole:
            # get the class of the objects property that is edited
            propDict = self._propList[index.row()]
            old_value = getattr(self._obj, propDict[NAME_KEY])
            typ = propDict[TYPE_KEY] or type(old_value).__name__
            i = SUPPORTED_TYPE_NAMES.index(typ) if typ in SUPPORTED_TYPE_NAMES else None

            if i is not None:
                cls = SUPPORTED_TYPES[i]
            else:
                cls = type(old_value)

            try:
                new_value = cls(value_str)
            except:
                return False

            if self.data(index, role=Qt.EditRole) != new_value:
                setattr(self._obj, propDict[NAME_KEY], new_value)
            else:
                return False

            self.dataChanged.emit()
            return True
        return False

    def flags(self, index):
        if self._items[index.column()] == VALUE_KEY:
            if self.editable(index.row()):
                return Qt.ItemIsEnabled | Qt.ItemIsEditable  # | Qt.ItemIsSelectable
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled  # Qt.NoItemFlags

    def rowCount(self, index=None):
        return len(self._propList)

    def columnCount(self, index=None):
        return len(self._items)

    def headerData(self, column, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                return self._items[column]

            elif role == Qt.SizeHintRole:
                if self._items[column] == NAME_KEY:
                    return QSize(120, HEADER_HEIGHT_HINT)
                elif self._items[column] == VALUE_KEY:
                    return QSize(180, HEADER_HEIGHT_HINT)
                # elif self._items[column] == UNIT_KEY:
                #     return QSize(50, HEADER_HEIGHT_HINT)
                # elif self._items[column] == DESC_KEY:
                #     return QSize(300, HEADER_HEIGHT_HINT)

            elif role == Qt.FontRole:
                font = QFont()
                font.setBold(True)
                return font

    def editable(self, row):
        propDict = self._propList[row]
        if propDict["_editable_"]:
            return True
        return False

    def isPyleecanType(self, obj):
        return type(obj).__name__ in self._class_dict.keys()
