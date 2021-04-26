from PySide2.QtMultimedia import QMediaPlayer as qtm
from pygame import mixer


class Music:
    @staticmethod
    def load(file: str) -> None:
        mixer.music.load(file)

    @staticmethod
    def play():
        mixer.music.play(loops=0)

    @staticmethod
    def unpause():
        mixer.music.unpause()

    @staticmethod
    def pause():
        mixer.music.pause()
