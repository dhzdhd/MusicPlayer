import PySide2.QtWidgets as qtw
import PySide2.QtGui as qtg
import PySide2.QtCore as qtc
from player.constants import Icons as ico

from player.backend.settings import Settings


class BottomBarFrame(qtw.QFrame):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setFixedHeight(70)
        self.setMinimumWidth(720)
        self.setStyleSheet(
            f"background-color: {Settings.BOTTOM_BAR_FRAME_COLOUR};"
        )

    @staticmethod
    def volume_button(parent):
        volume_button = qtw.QPushButton(parent=parent)
        volume_button.setFixedSize(30, 30)
        volume_button.setIconSize(qtc.QSize(30, 30))
        volume_button.setIcon(qtg.QPixmap(qtg.QImage(ico.VOLUME_ICON)))
        return volume_button

    @staticmethod
    def previous_button(parent):
        previous_button = qtw.QPushButton(parent=parent)
        previous_button.setFixedSize(30, 30)
        previous_button.setIconSize(qtc.QSize(30, 30))
        previous_button.setIcon(qtg.QPixmap(qtg.QImage(ico.PREVIOUS_ICON)))
        return previous_button

    @staticmethod
    def play_pause_button(parent):
        play_pause_button = qtw.QPushButton(parent=parent)
        play_pause_button.setFixedSize(30, 30)
        play_pause_button.setIconSize(qtc.QSize(30, 30))
        play_pause_button.setIcon(qtg.QPixmap(qtg.QImage(ico.PLAY_ICON)).scaled(100, 100, qtc.Qt.KeepAspectRatio))
        return play_pause_button

    @staticmethod
    def next_button(parent):
        next_button = qtw.QPushButton(parent=parent)
        next_button.setFixedSize(30, 30)
        next_button.setIconSize(qtc.QSize(30, 30))
        next_button.setIcon(qtg.QPixmap(qtg.QImage(ico.NEXT_ICON)))
        return next_button

    @staticmethod
    def repeat_button(parent):
        repeat_button = qtw.QPushButton(parent=parent)
        repeat_button.setFixedSize(30, 30)
        repeat_button.setIconSize(qtc.QSize(30, 30))
        repeat_button.setIcon(qtg.QPixmap(qtg.QImage(ico.REPEAT_ICON)))
        return repeat_button
