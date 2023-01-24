from kivymd.uix.screen import MDScreen
import appEnvironment as AE


class ReportWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(ReportWindow, self).__init__(*args, **kwargs)
        AE.ReportWObj = self