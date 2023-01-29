from kivymd.uix.screen import MDScreen
import appEnvironment as AE


class NewWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(NewWindow, self).__init__(*args, **kwargs)
        self.item = 0
        self.ids.text_label.text = AE.title_of_windows[0]
        self.ids.text_label.font_size = 30 * AE.koef
        self.ids.text_label1.text = AE.title_label_new[0] + str(self.item + 1)
        self.ids.text_label1.font_size = 30 * AE.koef
        self.ids.text_label2.text = AE.title_label_new[1]
        self.ids.text_label2.font_size = 30 * AE.koef
        self.ids.text_input1.font_size = 30 * AE.koef
        self.ids.text_input2.font_size = 30 * AE.koef
        AE.NewWObj = self

    def addNewGamer(self):
        if (self.item==0):
            AE.ApplicationSettingObj.gamerNames=[]
            AE.ApplicationSettingObj.gamerCount = []
            AE.ApplicationSettingObj.round = []
            AE.ApplicationSettingObj.timeOfGameInSec = []

        AE.ApplicationSettingObj.gamerNames.append(self.ids.text_input1.text)
        self.ids.text_input1.text = ''
        self.item += 1
        self.ids.text_label1.text = AE.title_label_new[0] + str(self.item + 1)


    def newGame(self):
        self.item = 0
        AE.ServerProxyObj.saveAndLoadGame(2, self.ids.text_input2.text, AE.ApplicationSettingObj)
        AE.NavigationrailObj.switchToGame()