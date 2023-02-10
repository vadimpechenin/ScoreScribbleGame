from kivymd.uix.screen import MDScreen
import appEnvironment as AE
from threading import Thread
import time
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class GameWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(*args, **kwargs)
        self.item=0
        Thread(target=self.gameOn).start()
        self.ids.text_label.text = AE.title_of_windows[2]
        self.ids.text_label.font_size = 30 * AE.koef
        self.ids.text_label0.text = AE.title_label_game[3] + str(1)
        self.ids.text_label0.font_size = 30 * AE.koef
        if (len(AE.AppSetObj.gamerNames)>0):
            self.ids.text_label1.text = AE.title_label_game[0] + AE.AppSetObj.gamerNames[0]
        else:
            self.ids.text_label1.text = AE.title_label_game[2]
        self.ids.text_label1.font_size = 30 * AE.koef
        self.ids.text_label2.text = AE.title_label_game[1] +str(0)
        self.ids.text_label2.font_size = 30 * AE.koef
        self.ids.text_input1.font_size = 30 * AE.koef
        AE.GameWObj = self

    def gameOn(self):
        while True:
            time.sleep(0.3)
            if (self.item==1):
                self.ids.text_label1.text = AE.title_label_game[0] + AE.AppSetObj.gamerNames[AE.AppSetObj.gamerIndex]
                self.ids.text_label2.text = AE.title_label_game[1] + str(
                    AE.AppSetObj.gamerCount[AE.AppSetObj.gamerIndex])
                self.ids.text_label0.text = AE.title_label_game[3] + str(
                    AE.AppSetObj.round[-1])
                self.item = 0

            if (self.item==2):
                break

    def addResult(self):
        try:
            AE.AppSetObj.gamerCount[AE.AppSetObj.gamerIndex] = AE.AppSetObj.gamerCount[AE.AppSetObj.gamerIndex]+int(self.ids.text_input1.text)
            AE.AppSetObj.gamerIndex+=1
            if (AE.AppSetObj.gamerIndex==len(AE.AppSetObj.gamerNames)):
                AE.AppSetObj.gamerIndex=0
                AE.AppSetObj.round.append(AE.AppSetObj.round[-1]+1)
            self.ids.text_input1.text=''
            self.item = 1
        except:
            title = 'Предупреждение'
            text = 'Неверный ввод, попробуйте снова'
            self.popupForFilter(title, text)

    def addNullResult(self):
        AE.AppSetObj.gamerIndex += 1
        if (AE.AppSetObj.gamerIndex == len(AE.AppSetObj.gamerNames)):
            AE.AppSetObj.gamerIndex = 0
            AE.AppSetObj.round.append(AE.AppSetObj.round[-1] + 1)
        self.ids.text_input1.text = ''
        self.item = 1

    def reportWindow(self):
        pass

    def popupForFilter(self, title, text):
        PopupGrid = GridLayout(rows=2, size_hint_y=None)
        PopupGrid.add_widget(Label(text=text))
        content = Button(text='Закрыть')
        PopupGrid.add_widget(content)
        popup = Popup(title=title, content=PopupGrid,
                      auto_dismiss=False, size_hint=(None, None), size=(int(300 * AE.koef), int(200 * AE.koef)))

        content.bind(on_press=popup.dismiss)
        popup.open()