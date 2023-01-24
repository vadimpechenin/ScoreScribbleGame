from kivymd.uix.screen import MDScreen
import appEnvironment as AE


class SettingsWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(SettingsWindow, self).__init__(*args, **kwargs)
        AE.SettingsWObj = self