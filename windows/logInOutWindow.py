from kivymd.uix.screen import MDScreen
import appEnvironment as AE


class LogInOutWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(LogInOutWindow, self).__init__(*args, **kwargs)
        AE.LogInOutWObj = self