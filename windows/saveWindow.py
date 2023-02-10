from kivymd.uix.screen import MDScreen
import appEnvironment as AE
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class SaveWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(SaveWindow, self).__init__(*args, **kwargs)
        self.ids.text_label.text = AE.title_of_windows[3]
        self.ids.text_label.font_size = 30 * AE.koef
        AE.SaveWObj = self

    def saveFile(self):
        try:
            AE.ServerProxyObj.saveAndLoadGame(2, '', AE.AppSetObj)
            title = 'Предупреждение'
            text = 'Успешно сохранено'
            self.popupForFilter(title, text)
        except:
            title = 'Предупреждение'
            text = 'Сохранение не удалось'
            self.popupForFilter(title, text)
    def popupForFilter(self, title, text):
        PopupGrid = GridLayout(rows=2, size_hint_y=None)
        PopupGrid.add_widget(Label(text=text))
        content = Button(text='Закрыть')
        PopupGrid.add_widget(content)
        popup = Popup(title=title, content=PopupGrid,
                      auto_dismiss=False, size_hint=(None, None), size=(int(300 * AE.koef), int(200 * AE.koef)))

        content.bind(on_press=popup.dismiss)
        popup.open()
