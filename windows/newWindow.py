from kivymd.uix.screen import MDScreen
import appEnvironment as AE


class NewWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(NewWindow, self).__init__(*args, **kwargs)
        AE.NewWObj = self