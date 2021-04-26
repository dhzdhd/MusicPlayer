import PySide2.QtWidgets as qtw
import PySide2.QtGui as qtg

from player.backend.settings import Settings


class TitleFrame(qtw.QFrame):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setMinimumWidth(720)
        self.setMaximumHeight(60)
        self.setSizePolicy(qtw.QSizePolicy.MinimumExpanding, qtw.QSizePolicy.MinimumExpanding)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(
            f"background-color: {Settings.TITLE_BAR_FRAME_COLOUR};"
        )

    @staticmethod
    def title_label(parent, text):
        title_label = qtw.QLabel(parent=parent, text=text)
        title_label.setStyleSheet(
            f"color: {Settings.TITLE_COLOUR};\n"
            f"font-family: {Settings.TITLE_FONT};\n"
            f"font-size: {Settings.TITLE_FONT_SIZE};"
        )
        return title_label

    @staticmethod
    def minimise_button(parent):
        minimise_button = qtw.QPushButton(parent)
        minimise_button.setMaximumSize(28, 28)
        minimise_button.setStyleSheet(
            f"border-radius: 14px;\nbackground-color: {Settings.MINIMISE_BUTTON_COLOUR}"
        )
        return minimise_button

    @staticmethod
    def maximise_button(parent):
        maximise_button = qtw.QPushButton(parent=parent)
        maximise_button.setMaximumSize(28, 28)
        maximise_button.setStyleSheet(
            f"border-radius: 14px;\nbackground-color: {Settings.MAXIMISE_BUTTON_COLOUR}"
        )
        return maximise_button

    @staticmethod
    def exit_button(parent):
        exit_button = qtw.QPushButton(parent)
        exit_button.setMaximumSize(28, 28)
        exit_button.setStyleSheet(
            f"border-radius: 14px;\nbackground-color: {Settings.EXIT_BUTTON_COLOUR}"
        )
        return exit_button

    def mouseMoveEvent(self, event: qtg.QMouseEvent) -> None:
        self.window().move(event.globalX() - 720, event.globalY() - 30)
        self.window().setWindowOpacity(0.7)

    def mouseReleaseEvent(self, event: qtg.QMouseEvent) -> None:
        self.window().setWindowOpacity(1)

