from kivymd.uix.screen import MDScreen
import appEnvironment as AE


class GameWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(*args, **kwargs)
        self.item=0
        self.ids.text_label.text = AE.title_of_windows[2]
        self.ids.text_label.font_size = 30 * AE.koef
        if (len(AE.AppSetObj.gamerNames)>0):
            self.ids.text_label1.text = AE.title_label_game[0] + AE.AppSetObj.gamerNames[0]
        else:
            self.ids.text_label1.text = AE.title_label_game[2]
        self.ids.text_label1.font_size = 30 * AE.koef
        self.ids.text_label2.text = AE.title_label_game[1] +str(0)
        self.ids.text_label2.font_size = 30 * AE.koef
        self.ids.text_input1.font_size = 30 * AE.koef
        AE.GameWObj = self

    def addResult(self):
        pass

    def addNullResult(self):
        pass
    def reportWindow(self):
        pass