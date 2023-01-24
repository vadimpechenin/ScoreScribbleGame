from kivymd.uix.screen import MDScreen
import appEnvironment as AE


class ContinueWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(ContinueWindow, self).__init__(*args, **kwargs)
        AE.ContinueWObj = self