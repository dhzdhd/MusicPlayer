import sys

from PySide2 import QtCore as qtc
from PySide2 import QtGui as qtg
from PySide2 import QtWidgets as qtw
from pygame import mixer

from player.backend import music
from player.constants import Icons as ico
from .bottom_bar import BottomBarFrame
from .music_contents import MusicContentsFrame
from .sliding_bar import SlidingFrame
from .title_bar import TitleFrame
from player.backend.settings import Settings


class Main(qtw.QDialog):
    flag = False

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setMinimumSize(1280, 720)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        self.setWindowFlag(qtc.Qt.FramelessWindowHint)
        self.setContentsMargins(0, 0, 0, 0)

        mixer.init()

        self.make_widgets()
        self.make_layouts()
        self.add_to_layout()
        self.add_functionality()

    def make_widgets(self) -> None:
        self.main_frame = qtw.QFrame(self)
        self.main_frame.setMinimumSize(1280, 720)
        self.main_frame.setSizePolicy(qtw.QSizePolicy.MinimumExpanding, qtw.QSizePolicy.MinimumExpanding)
        self.main_frame.setStyleSheet(
            "border-radius: 5px;\nbackground-color: rgb(30, 30, 30);"
        )

        # Title
        self.title_frame = TitleFrame(self)
        self.title_label = TitleFrame.title_label(parent=self, text="Music Player")
        self.minimise_button = TitleFrame.minimise_button(parent=self)
        self.maximise_button = TitleFrame.maximise_button(parent=self)
        self.exit_button = TitleFrame.exit_button(parent=self)

        self.content_frame = qtw.QFrame(self)
        self.content_frame.setStyleSheet(
            "background-image: url(:/path/to/image.png)"  # Replace with path
        )

        # Sliding frame
        self.sliding_frame = SlidingFrame(self)
        self.slide_button = SlidingFrame.slide_button(self)
        self.folder_button = SlidingFrame.folder_button(self)
        self.settings_button = SlidingFrame.settings_button(self)

        # Music contents frame
        self.music_contents_frame = MusicContentsFrame(self)

        # Bottom bar frame
        self.bottom_bar_frame = BottomBarFrame(self)
        self.volume_button = BottomBarFrame.volume_button(self)
        self.previous_button = BottomBarFrame.previous_button(self)
        self.play_pause_button = BottomBarFrame.play_pause_button(self)
        self.next_button = BottomBarFrame.next_button(self)
        self.repeat_button = BottomBarFrame.repeat_button(self)

        self.size_grip = qtw.QSizeGrip(self)

    def make_layouts(self) -> None:
        self.main_layout = qtw.QVBoxLayout(self)
        self.main_frame_layout = qtw.QVBoxLayout(self.main_frame)
        self.title_frame_layout = qtw.QHBoxLayout(self.title_frame)
        self.content_frame_layout = qtw.QGridLayout(self.content_frame)
        self.sliding_frame_layout = qtw.QVBoxLayout(self.sliding_frame)
        self.music_contents_frame_layout = qtw.QVBoxLayout(self.music_contents_frame)
        self.bottom_bar_frame_layout = qtw.QHBoxLayout(self.bottom_bar_frame)

    def add_to_layout(self) -> None:
        self.main_layout.setSpacing(0)
        self.main_layout.setMargin(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_frame_layout.setSpacing(0)
        self.main_frame_layout.setMargin(0)
        self.main_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.main_frame_layout.addWidget(self.title_frame)
        self.main_frame_layout.addWidget(self.content_frame)
        self.main_frame_layout.addWidget(self.bottom_bar_frame)

        self.title_frame_layout.addSpacerItem(
            qtw.QSpacerItem(200, 0, hData=qtw.QSizePolicy.Policy.MinimumExpanding)
        )
        self.title_frame_layout.addSpacing(90)
        self.title_frame_layout.addWidget(self.title_label, alignment=qtc.Qt.AlignHCenter)
        self.title_frame_layout.addSpacerItem(
            qtw.QSpacerItem(200, 0, hData=qtw.QSizePolicy.Policy.MinimumExpanding)
        )
        self.title_frame_layout.addWidget(self.minimise_button, alignment=qtc.Qt.AlignRight)
        self.title_frame_layout.addWidget(self.maximise_button)
        self.title_frame_layout.addWidget(self.exit_button)

        self.content_frame_layout.setSpacing(0)
        self.content_frame_layout.setMargin(0)
        self.content_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.content_frame_layout.addWidget(self.sliding_frame, 0, 0)
        self.content_frame_layout.addWidget(self.music_contents_frame, 0, 1)

        self.sliding_frame_layout.setSpacing(0)
        self.sliding_frame_layout.setMargin(0)
        self.sliding_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.sliding_frame_layout.addSpacing(15)
        self.sliding_frame_layout.addWidget(self.slide_button, alignment=qtc.Qt.AlignTop)
        self.sliding_frame_layout.addSpacing(45)
        self.sliding_frame_layout.addWidget(self.folder_button)
        self.sliding_frame_layout.addSpacerItem(
            qtw.QSpacerItem(0, 100, vData=qtw.QSizePolicy.Policy.MinimumExpanding)
        )
        self.sliding_frame_layout.addWidget(self.settings_button, alignment=qtc.Qt.AlignBottom)
        self.sliding_frame_layout.addSpacing(15)

        self.bottom_bar_frame_layout.addSpacing(10)
        self.bottom_bar_frame_layout.addWidget(self.volume_button)
        self.bottom_bar_frame_layout.addSpacerItem(
            qtw.QSpacerItem(500, 0, hData=qtw.QSizePolicy.Policy.MinimumExpanding)
        )
        self.bottom_bar_frame_layout.addWidget(self.previous_button)
        self.bottom_bar_frame_layout.addSpacing(50)
        self.bottom_bar_frame_layout.addWidget(self.play_pause_button)
        self.bottom_bar_frame_layout.addSpacing(50)
        self.bottom_bar_frame_layout.addWidget(self.next_button)
        self.bottom_bar_frame_layout.addSpacerItem(
            qtw.QSpacerItem(500, 0, hData=qtw.QSizePolicy.Policy.MinimumExpanding)
        )
        self.bottom_bar_frame_layout.addWidget(self.repeat_button)
        self.bottom_bar_frame_layout.addSpacing(10)

        self.setLayout(self.main_layout)

    def add_functionality(self) -> None:
        def maximise():
            if not self.isMaximized():
                self.current_size = self.size()
                self.window().showMaximized()
            else:
                self.resize(self.current_size)

        def load():
            music.Music.load(file="D:/Programming/Python/MusicPlayer/temp_music/syt.mp3")

        def play():
            if not Main.flag:
                Main.flag = True
                self.play_pause_button.setIcon(qtg.QPixmap(qtg.QImage(ico.PAUSE_ICON)))
                music.Music.play()
            else:
                Main.flag = False
                self.play_pause_button.setIcon(qtg.QPixmap(qtg.QImage(ico.PLAY_ICON)))
                music.Music.pause()

        def settings():
            widget_list = []

            widget_list.extend([_ for _ in self.children()])
            widget_list.extend([_ for _ in self.main_frame.children()])
            widget_list.extend([_ for _ in self.title_frame.children()])
            widget_list.extend([_ for _ in self.content_frame.children()])
            widget_list.extend([_ for _ in self.sliding_frame.children()])
            widget_list.extend([_ for _ in self.bottom_bar_frame.children()])

            widget_list = [_ for _ in widget_list if not isinstance(_, qtw.QVBoxLayout)]
            widget_list = [_ for _ in widget_list if not isinstance(_, qtw.QHBoxLayout)]
            widget_list = [_ for _ in widget_list if not isinstance(_, qtw.QFormLayout)]

            for widget in widget_list:
                widget.setProperty("urgent", True)
                widget.setStyleSheet(widget.styleSheet())
                widget.style().unpolish(widget)
                widget.style().polish(widget)
                widget.update()
                widget.setProperty("urgent", False)

        load()

        self.maximise_button.clicked.connect(maximise)
        self.minimise_button.clicked.connect(lambda: [Settings(), settings()])
        self.exit_button.clicked.connect(lambda: [self.destroy(), sys.exit()])
        self.play_pause_button.clicked.connect(lambda: play())


def setup() -> None:
    Settings()
    app = qtw.QApplication(sys.argv)
    app.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True)
    window = Main()
    window.show()
    sys.exit(app.exec_())
