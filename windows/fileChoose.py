"""
Окно для выбора фотографий
"""
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
import appEnvironment as AE

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
#Библиотека для всплывающих окон
from kivy.uix.popup import Popup



class FileChoose(MDScreen):

    def __init__(self, *args, **kwargs):
        super(FileChoose, self).__init__(*args, **kwargs)
        self.popup = None
        AE.FileChooseWObj = self
        Clock.schedule_once(self.init_widget, 0)

    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
        except:
            self.popupForSocketNo()
        else:
            try:
                self.popupForSocketYes(filename[0])
                AE.filenameEnv = []
                AE.filenameEnv.append(filename[0])
                strOfFile = AE.filenameEnv[0].split('\\')
                print(strOfFile[-1])
                AE.ContinueWObj.ids.text_input1.text = strOfFile[-1]
            except:
                pass

    def dellwidget(self):
        # удаляет все виджеты, которые находяться в another_box
        self.ids.my_image.source = ""

    def popupForSocketYes(self,filename):
        PopupGrid = GridLayout(rows=2, size_hint_y=None)
        PopupGrid.add_widget(Label(text=filename))
        content = Button(text='Закрыть')
        PopupGrid.add_widget(content)
        self.popup = Popup(title='Успех', content=PopupGrid,
                            auto_dismiss=False, size_hint=(None, None),
                            size=(int(300 * AE.koef), int(200 * AE.koef)))

        content.bind(on_press=self.popup.dismiss)
        self.popup.open()

    def popupForSocketNo(self):
        PopupGrid = GridLayout(rows=2, size_hint_y=None)
        PopupGrid.add_widget(Label(text='Ничего не вышло'))
        content = Button(text='Закрыть')
        PopupGrid.add_widget(content)
        self.popup = Popup(title='Провал', content=PopupGrid,
                           auto_dismiss=False, size_hint=(None, None),
                           size=(int(300 * AE.koef), int(200 * AE.koef)))

        content.bind(on_press=self.popup.dismiss)
        self.popup.open()

    def switchToContinue(self):
        AE.NavigationrailObj.switchToContinue()

    def init_widget(self, *args):
        #Попытка перекрасить цвета
        AE.FileChooseWObj.bind(on_entry_added=self.update_file_list_entry)
        AE.FileChooseWObj.bind(on_subentry_to_entry=self.update_file_list_entry)

    def update_file_list_entry(self, file_chooser, file_list_entry, *args):
        file_list_entry.children[0].color = (0.0, 0.0, 1.0, 1.0)  # File Names
        file_list_entry.children[1].color = (0.0, 0.0, 1.0, 1.0)  # Dir Names`