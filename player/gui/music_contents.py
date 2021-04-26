import PySide2.QtWidgets as qtw

from player.backend.settings import Settings


class MusicContentsFrame(qtw.QFrame):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setStyleSheet(
            f"background-color: rgb(0, 0, 0)"
        )