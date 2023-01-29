from threading import Lock
from common.applicationSettingsHelper import ApplicationSettingHelper
import appEnvironment as AE


class ServerProxy:
    REQUEST_TEMPLATE = "http://%HOST%:%PORT%/ProcessingServer/handler"

    def __init__(self, host, port):
        self.requestUrl = self.REQUEST_TEMPLATE.replace("%HOST%", str(host)).replace("%PORT%", str(port))
        self.session = None
        self.requestLock = Lock()

    def saveAndLoadGame(self, pl, filename, parameters):
        #Функция для сохранения и загрузки параметров игры
        if (filename == ''):
            filename = AE.nameOfJson
        if (pl==1):
            ApplicationSettingHelper.readSettingsFromFile(filename, parameters)
        else:
            ApplicationSettingHelper.writeSettingsToFile(filename, parameters)