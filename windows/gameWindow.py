from kivymd.uix.screen import MDScreen
import appEnvironment as AE


class GameWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(*args, **kwargs)
        AE.GameWObj = self