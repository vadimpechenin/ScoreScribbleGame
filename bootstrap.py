import appEnvironment as AE
from kivy.lang import Builder

from kivy.core.window import Window

from model.applicationSettings import ApplicationSettings
from serverProxy import ServerProxy
from test import Test


class Bootstrap:

    @staticmethod
    def initEnviroment():
        if (AE.koef == 1):
            Window.size = (420, 800)
        else:
            Window.size = (1100, 2300)
        AE.kv = Builder.load_file("windows/navigationrail.kv")
        AE.TestObj = Test()
        AE.AppSetObj = ApplicationSettings()
        AE.AppSetObj.gamerNames = []
        AE.AppSetObj.gamerCount = []
        AE.AppSetObj.round = []
        AE.AppSetObj.timeOfGameInSec = ''
        AE.ServerProxyObj = ServerProxy(AE.ServerHost, AE.ServerPort)
    @staticmethod
    def run():
        AE.TestObj.run()
