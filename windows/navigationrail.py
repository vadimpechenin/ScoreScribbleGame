from kivymd.uix.screen import MDScreen
import appEnvironment as AE
from windows.fileChoose import FileChoose

from windows.fourthWindow import FourthWindow
from windows.logInOut import LogInOut
from windows.mainReportWindow import MainReportWindow
from windows.newItemWindow import NewItemWindow
from windows.photoWindow import PhotoWindow
from windows.profileWindow import ProfileWindow
from windows.qrWindow import QRWindow
from windows.reportsWindowDetail import ReportsWindowDetail
from windows.reportTableWindow import ReportTableWindow
from windows.filterOFItemWindow import FilterOFItemWindow
from windows.settingsWindow import SettingsWindow
from windows.operationMainWindow import OperationMainWindow


class ReportWindowDetail(object):
    pass


class Navigationrail(MDScreen):
    # Create the screen manager
    def __init__(self, *args, **kwargs):
        super(Navigationrail, self).__init__(*args, **kwargs)
        self.ids.scr_mng.add_widget(LogInOut(name='loginout'))
        self.ids.scr_mng.add_widget(ProfileWindow(name='profile'))
        self.ids.scr_mng.add_widget(PhotoWindow(name='photo'))
        self.ids.scr_mng.add_widget(QRWindow(name='qr'))
        self.ids.scr_mng.add_widget(FourthWindow(name='fourth'))
        self.ids.scr_mng.add_widget(MainReportWindow(name='mainreport'))
        self.ids.scr_mng.add_widget(FileChoose(name='filechoose'))
        self.ids.scr_mng.add_widget(ReportsWindowDetail(name='reportOfItem'))
        self.ids.scr_mng.add_widget(ReportTableWindow(name='reportTable'))
        self.ids.scr_mng.add_widget(FilterOFItemWindow(name='filterOfItem'))
        self.ids.scr_mng.add_widget(SettingsWindow(name='settings'))
        self.ids.scr_mng.add_widget(NewItemWindow(name='newItem'))
        self.ids.scr_mng.add_widget(OperationMainWindow(name='operationMain'))
        self.ids.scr_mng.current = 'loginout'
        AE.NavigationrailObj = self

    def switchToFourth(self):
        if (AE.login):
            self.ids.scr_mng.current = 'fourth'

    def switchToPhoto(self):
        if (AE.login):
            self.ids.scr_mng.current = 'photo'

    def switchToMainReport(self):
        if (AE.login):
            AE.listOfItemsView = 2
            self.ids.scr_mng.current = 'mainreport'

    def switchToQR(self):
        if (AE.login):
            self.ids.scr_mng.current = 'qr'

    def switch_to_profile(self):
        if (AE.login):
            self.ids.scr_mng.current = 'profile'

    def switchToLogInOut(self):
        AE.ServerProxyObj.logout()
        AE.LogInOutObj.clear()
        AE.login = False
        self.ids.scr_mng.current = 'loginout'

    def switchToFileChoose(self):
        if (AE.login):
            self.ids.scr_mng.current = 'filechoose'

    def switchToReportWindowDetail(self):
        if (AE.login):
            self.ids.scr_mng.current = 'reportOfItem'

    def switchToReportTable(self):
        AE.LogInOutObj.clear()
        self.ids.scr_mng.current = 'reportTable'

    def switchToFilterOFItem(self):
        if (AE.login):
            self.ids.scr_mng.current = 'filterOfItem'

    def switchToSettings(self):
        if (AE.login):
            self.ids.scr_mng.current = 'settings'

    def switchToNewItem(self):
        if (AE.login):
            self.ids.scr_mng.current = 'newItem'

    def switchToOparationMain(self):
        if (AE.login):
            AE.OperationMainWObj.dellWidgetFilter()
            AE.OperationMainWObj.ScrollWindowPartTypeFilter()
            AE.OperationMainWObj.ScrollWindowFilter()
            #AE.OperationMainWObj.ScrollWindow()
            self.ids.scr_mng.current = 'operationMain'
