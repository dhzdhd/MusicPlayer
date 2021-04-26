from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg


class SettingsFrame(qtw.QFrame):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setStyleSheet(f"background-color: rgb(0, 0, 0)")
