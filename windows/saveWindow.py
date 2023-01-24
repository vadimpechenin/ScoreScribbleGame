from kivymd.uix.screen import MDScreen
import appEnvironment as AE


class SaveWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(SaveWindow, self).__init__(*args, **kwargs)
        AE.SaveWObj = self