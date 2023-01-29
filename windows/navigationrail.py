from kivymd.uix.screen import MDScreen
import appEnvironment as AE

from windows.newWindow import NewWindow
from windows.continueWindow import ContinueWindow
from windows.gameWindow import GameWindow
from windows.reportWindow import ReportWindow
from windows.saveWindow import SaveWindow
from windows.settingsWindow import SettingsWindow
from windows.logInOutWindow import LogInOutWindow
from windows.newSettingsWindow import NewSettingsWindow

#  include the kv files for the other Screens
#: include windows/new.kv
#: include windows/continue.kv
#: include windows/game.kv
#: include windows/report.kv
#: include windows/save.kv
#: include windows/settings.kv
#: include windows/logInOut.kv
#: include windows/newSettings.kv


class ReportWindowDetail(object):
    pass


class Navigationrail(MDScreen):
    # Create the screen manager
    def __init__(self, *args, **kwargs):
        super(Navigationrail, self).__init__(*args, **kwargs)
        self.ids.scr_mng.add_widget(NewWindow(name='new'))
        self.ids.scr_mng.add_widget(ContinueWindow(name='continue'))
        self.ids.scr_mng.add_widget(GameWindow(name='game'))
        self.ids.scr_mng.add_widget(ReportWindow(name='report'))
        self.ids.scr_mng.add_widget(SaveWindow(name='save'))
        self.ids.scr_mng.add_widget(SettingsWindow(name='settings'))
        self.ids.scr_mng.add_widget(LogInOutWindow(name='logInOut'))
        self.ids.scr_mng.add_widget(NewSettingsWindow(name='newSettings'))
        AE.NavigationrailObj = self

    def switchToNew(self):
        AE.NewWObj.item = 0
        self.ids.scr_mng.current = 'new'

    def switchToContinue(self):
        self.ids.scr_mng.current = 'continue'

    def switchToGame(self):
        self.ids.scr_mng.current = 'game'

    def switchToReport(self):
        self.ids.scr_mng.current = 'report'

    def switchToSave(self):
        self.ids.scr_mng.current = 'save'

    def switchToSettings(self):
        self.ids.scr_mng.current = 'settings'

    def switchToLogInOut(self):
        self.ids.scr_mng.current = 'logInOut'

    def switchToNewGameSettings(self):
        self.ids.scr_mng.current = 'newSettings'
