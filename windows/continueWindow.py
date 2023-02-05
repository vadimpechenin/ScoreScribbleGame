from kivymd.uix.screen import MDScreen
import appEnvironment as AE


class ContinueWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(ContinueWindow, self).__init__(*args, **kwargs)
        self.ids.text_label.text = AE.title_of_windows[1]
        self.ids.text_label.font_size = 30 * AE.koef
        self.ids.text_label1.text = AE.title_label_continue[0]
        self.ids.text_label1.font_size = 30 * AE.koef
        self.ids.text_input1.font_size = 30 * AE.koef
        AE.ContinueWObj = self

    def addLoadFile(self):
        AE.NavigationrailObj.switchToFileChoose()

    def reportContinueGame(self):
        #self.ids.text_input1.text = AE.filenameEnv[0]
        AE.ServerProxyObj.saveAndLoadGame(1, self.ids.text_input1.text, AE.AppSetObj)
        AE.NavigationrailObj.switchToGame()
