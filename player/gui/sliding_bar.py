import PySide2.QtWidgets as qtw
import PySide2.QtGui as qtg

from player.backend.settings import Settings
from player.constants import Icons as ico


class SlidingFrame(qtw.QFrame):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setMaximumWidth(70)
        self.setMinimumHeight(540)
        self.setStyleSheet(
            f"background-color: {Settings.SLIDING_FRAME_COLOUR}"
        )

    @staticmethod
    def slide_button(parent):
        slide_button = qtw.QPushButton(parent=parent)
        slide_button.setIcon(qtg.QPixmap(qtg.QImage(ico.SLIDE_ICON)))
        return slide_button

    @staticmethod
    def folder_button(parent):
        folder_button = qtw.QPushButton(parent=parent)
        folder_button.setIcon(qtg.QPixmap(qtg.QImage(ico.FOLDER_ICON)))
        return folder_button

    @staticmethod
    def settings_button(parent):
        settings_button = qtw.QPushButton(parent=parent)
        settings_button.setIcon(qtg.QPixmap(qtg.QImage(ico.SETTINGS_ICON)))
        return settings_button
