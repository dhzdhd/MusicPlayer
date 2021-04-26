import toml


class Settings:
    def __init__(self):
        with open("D:/Programming/Python/MusicPlayer/player/settings.toml") as f:
            self.toml_file = toml.load(f)

        self.fonts()
        self.font_size()
        self.colours()

    def fonts(self):
        fonts = self.toml_file["Font"]

        Settings.TITLE_FONT = fonts["title"]

    def font_size(self):
        font_sizes = self.toml_file["Font_Size"]

        Settings.TITLE_FONT_SIZE = font_sizes["title"]

    def colours(self):
        colours = self.toml_file["Colours"]

        Settings.MAIN_FRAME_COLOUR = colours["main_frame"]
        Settings.TITLE_BAR_FRAME_COLOUR = colours["title_bar_frame"]
        Settings.CONTENTS_FRAME_COLOUR = colours["contents_frame"]
        Settings.SLIDING_FRAME_COLOUR = colours["sliding_frame"]
        Settings.BOTTOM_BAR_FRAME_COLOUR = colours["bottom_frame"]

        Settings.TITLE_COLOUR = colours["title_colour"]
        Settings.MINIMISE_BUTTON_COLOUR = colours["minimise_button"]
        Settings.MAXIMISE_BUTTON_COLOUR = colours["maximise_button"]
        Settings.EXIT_BUTTON_COLOUR = colours["exit_button"]

