from kivymd.uix.screen import MDScreen
import appEnvironment as AE


class NewSettingsWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(NewSettingsWindow, self).__init__(*args, **kwargs)
        AE.NewSettingsWObj = self