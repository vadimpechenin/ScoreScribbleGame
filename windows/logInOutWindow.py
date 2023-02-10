from kivymd.uix.screen import MDScreen
import appEnvironment as AE


class LogInOutWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(LogInOutWindow, self).__init__(*args, **kwargs)
        self.ids.text_label.text = AE.title_of_windows[5]
        self.ids.text_label.font_size = 30 * AE.koef
        AE.LogInOutWObj = self

    def exit(self):
        AE.GameWObj.item = 2

